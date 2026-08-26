---
title: "MQTT"
---

The Battery-Emulator is compatible with MQTT. It can be configured to publish data to your MQTT broker and then be used in whatever way you choose (like for example [Home Assistant](home_assistant.md)). You can modify the Battery-Emulator code to publish more data, less data, or other data, as well as subscribing to MQTT topics. There are also advanced functions that can be triggered via MQTT, such as charge limits.

The main purpose of this implementation is better integration with popular home automation platforms such as Home Assistant, in order to (for example) keep track of battery temperature and cell deviation. If "MQTT" and "Home Assistant" are not familiar words, you will likely not benefit from this until you're up to speed on the current state of home automation.

!!! note "NOTE"
    The MQTT topic name, the Home Assistant object-ID prefix, the HA device name, and the HA device identifier are no longer independently configurable settings. All four are automatically set to the device's **hostname**, which itself defaults to `battery-emulator-xxxx` (`xxxx` being the last two bytes of the device's MAC address) unless a custom hostname has been set on the Connectivity settings page. The examples on this page use `battery-emulator-a1b2` as a stand-in for this value - substitute your device's actual hostname wherever you see it.

!!! note "NOTE"
    This page documents the MQTT implementation as found in `Software/src/devboard/mqtt/mqtt.cpp`. The behaviour described here matches recent builds. Older releases behave differently - see [Migrating from older releases](#migrating-from-older-releases).

## Enabling MQTT

To start using MQTT, enable the **Enable MQTT** checkbox under the Integration settings in the Web UI. The remaining MQTT fields only appear once that box is ticked.

| Setting | Range / default | Meaning |
| ------- | --------------- | ------- |
| **MQTT server** | hostname or IP | Broker address (plain TCP; TLS is not implemented) |
| **MQTT port** | 1–65535, default `1883` | Broker port |
| **MQTT user** / **MQTT password** | printable ASCII | Credentials; leaving the password field blank keeps the stored one |
| **MQTT timeout ms** | 1–60000, default `2000` | Network timeout of the underlying esp-mqtt client |
| **MQTT publish interval (seconds)** | 1–300, default `5` | Main publish cadence (see [Published data](#published-data)) |
| **Send all cellvoltages via MQTT** | off | Enables the `spec_data*` topics |
| **Publish heap metric diagnostics** | off | Adds four heap sensors to `/info` and to autodiscovery |
| **Allow remote BMS reset via MQTT** | off | Gates the `BMSRESET` command |
| **Home Assistant autodiscovery** | off | Publishes retained HA discovery configs |
| **Autodiscovery topic** | default `homeassistant` | Base topic for discovery messages |
| **Publish at firmware updates** | off | Publish the discovery configs whenever a firmware update is detected |
| **Publish at next boot** | off | Publish the discovery configs at next boot (unticks automatically) |

The device's **Hostname** field (set in the Network config section) determines the MQTT topic name, the HA object-ID prefix, the HA device name, and the HA device identifier - see the note at the top of this page.

!!! note "NOTE"
    The publish interval is applied when the MQTT client is started, and the heap-metrics checkbox changes which sensors are auto-discovered. Both take effect **after a restart**.

!!! note "NOTE"
    Make sure that your LAN is not on `192.168.4.x`, since this conflicts with the built-in ESP access point!

## Published data

Out of the box, the implementation publishes the following topics. All topics are prefixed with the device's topic name (its hostname), shown here as `battery-emulator-a1b2`.

| Topic | Contents | Retained |
| ----- | -------- | -------- |
| `battery-emulator-a1b2/status` | Availability string (`online` / `offline`) | Yes (both values) |
| `battery-emulator-a1b2/info` | System/emulator status + battery #1 state JSON | No |
| `battery-emulator-a1b2/info_2` | Battery #2 state JSON (double-battery setups) | No |
| `battery-emulator-a1b2/info_3` | Battery #3 state JSON (triple-battery setups) | No |
| `battery-emulator-a1b2/spec_data` | All cell voltages and per-cell balancing status (when enabled) | No |
| `battery-emulator-a1b2/spec_data_2` | Battery #2 cell voltages and per-cell balancing status (when enabled) | No |
| `battery-emulator-a1b2/spec_data_3` | Battery #3 cell voltages and per-cell balancing status (when enabled) | No |
| `battery-emulator-a1b2/events` | Battery-Emulator events | No |

When a **second battery** is configured, its values are published to its **own topic** `.../info_2`, using the **same key names** as battery #1 (`SOC`, `battery_voltage`, …, without any suffix), and its cell data goes to `.../spec_data_2`. A **third battery**, on compatible integrations, follows the same pattern with `.../info_3` and `.../spec_data_3`. The global emulator values (`bms_status`, `pause_status`, `event_level`, `emulator_status`, `hardware`, `software_version`, `cpu_temp`, `emulator_uptime`, `heap_*`) are only present on `.../info`.

Two publish cadences are used:

- The **main interval** is the configurable **MQTT publish interval** (default **5 s**) and covers `events` and all `info` topics. On each cycle the order is: `events` → `info` → `info_2` → `info_3`.
- **Cell data** (`spec_data*`) is published on a fixed **60-second** cadence, independent of the main interval. Cell voltages change slowly, and these are by far the largest payloads.

Publishing is skipped entirely while an **OTA update** is in progress, so a firmware upload is not competing with MQTT traffic.

Values are only published once **valid data** exists. Battery values appear only after the battery has actually been seen on CAN (not merely expected), CAN sending is allowed, and the post-boot startup delay has passed. Individual values that arrive later - such as `total_capacity` on batteries that derive it from received data, `insulation_resistance`, or `charged_energy`/`discharged_energy` - are omitted from the JSON until they are known. In Home Assistant this shows as **"unknown"** rather than a false `0` (or a false default like `370.0 V`) during boot.

**`<hostname>/info` (and `/info_2`, `/info_3`)**

`.../info` holds the system/emulator status plus battery #1's state. `.../info_2` and `.../info_3` hold only the respective battery's state, with identical key names. Numeric scaling notes:

- All voltages (`battery_voltage`, `cell_min_voltage`, `cell_max_voltage`) are published in **volts** as floats.
- `cell_voltage_delta` is the raw difference and is published in **millivolts**.
- `battery_current` is in amperes, power values in watts, energy/capacity values in watt-hours.
- `insulation_resistance` is in **kΩ**.
- Temperatures are in °C. `cpu_temp` is published as a float (display precision is suggested to HA as 1 decimal).
- Heap values are in **bytes**, `heap_fragmentation` in percent.

Example payload (single battery), published to `battery-emulator-a1b2/info`:

```json
{
  "bms_status": "ACTIVE",
  "pause_status": "RUNNING",
  "SOC": 63.30,
  "SOC_real": 61.05,
  "state_of_health": 92.00,
  "temperature_min": 5.8,
  "temperature_max": 7.4,
  "stat_batt_power": -1450.0,
  "battery_current": -3.5,
  "battery_voltage": 386.4,
  "cell_max_voltage": 3.787,
  "cell_min_voltage": 3.765,
  "cell_voltage_delta": 22.0,
  "total_capacity": 75000.0,
  "remaining_capacity_real": 45780.0,
  "remaining_capacity": 47475.0,
  "max_discharge_power": 30000.0,
  "max_charge_power": 12000.0,
  "balancing_active_cells": 0,
  "balancing_status": "Ready",
  "charging_state": "Discharging",
  "limiting_factor": "Battery",
  "event_level": "INFO",
  "emulator_status": "RUNNING",
  "hardware": "Waveshare ESP32-S3 RS485 CAN",
  "software_version": "11.2.dev",
  "cpu_temp": 41.3,
  "emulator_uptime": 10001
}
```

Keys appear conditionally:

- All battery values - only once the battery has been detected on CAN, is still communicating, CAN sending is allowed and the board has finished booting. Before that, `.../info` contains only the global emulator values.
- `total_capacity` - only once known (non-zero); some battery integrations derive it from received data.
- `charged_energy` / `discharged_energy` - only on batteries that support charged-energy tracking, and only once both totals are non-zero. Each battery reports **its own** totals.
- `cell_max_voltage` / `cell_min_voltage` / `cell_voltage_delta` - only once per-cell voltages have been populated.
- `insulation_resistance` - only on batteries that report insulation resistance, and only once a valid sample has been decoded.
- `cpu_temp` - only when **Measure CPU temperature** is enabled in the settings.
- `heap_free`, `heap_max_block`, `heap_min_free`, `heap_fragmentation` - only when **Publish heap metric diagnostics** is enabled.
- `dc_dc_current` / `dc_dc_voltage` - only for Tesla Model 3/Y and Model S/X.
- `autocal_taper`, `autocal_dwell_s`, `autocal_cooldown_ready`, `autocal_soc_drift`, `min_cell_number`, `max_cell_number` - only for the BYD Atto 3.
- `leaf_hx` - only for the Nissan Leaf, and only once a battery-group reply with a known layout has been decoded.

**Status strings**

`balancing_status` is one of: `Unknown`, `Error`, `Ready`, `Active`, `Pending`. `Pending` means cells are flagged for balancing but the BMS is not bleeding them yet.

`charging_state` is one of: `Idle`, `Charging`, `Discharging` (derived from the sign of the battery current).

`limiting_factor` tells you what is currently capping the allowed power in the active direction: `Inverter`, `UserSetting`, `Battery`, or `Idle` when the battery is neither charging nor discharging.

**Heap metric diagnostics**

When enabled, four internal-RAM heap values are added to `.../info`, using the same sources and fragmentation formula as the ESPHome debug component, so they are directly comparable with an ESPHome node's:

```json
{
  "heap_free": 157284,
  "heap_max_block": 110592,
  "heap_min_free": 141020,
  "heap_fragmentation": 29.7
}
```

`heap_fragmentation` is the share of the free heap that is not reachable as one contiguous block. It is omitted rather than published as `NaN` if the free heap ever reads zero.

**`<hostname>/spec_data`**

Published only when **Send all cellvoltages via MQTT** is enabled, and only on battery implementations that report per-cell voltages. Published every **60 seconds** (see above). Cell voltages are in **volts** as floats; the per-cell balancing status is included in the same message.

```json
{
  "cell_voltages": [3.779, 3.780, 3.782, 3.767, 3.783, 3.769, 3.782, 3.768],
  "cell_balancing": [true, true, false, false, false, false, false, true]
}
```

The two arrays always have the same length and describe the same snapshot: element *N* of `cell_balancing` is the balancing state of the cell whose voltage is element *N* of `cell_voltages`. The `cell_voltages` key is **absent** until the BMS has actually filled the voltages in, so the very first messages after boot may contain only `cell_balancing`.

The whole message must fit the 4 KB MQTT message buffer. If a pack has so many cells that the payload would overflow it, the message is skipped (with `Cell data MQTT msg too large for buffer` in the log) rather than truncated, and the rest of the publish cycle continues normally.

**`<hostname>/events`**

One message is published per new, not-yet-published event, in ascending timestamp order. All values are strings.

```json
{
  "event_type": "RESET_SW",
  "severity": "INFO",
  "count": "1",
  "data": "3",
  "message": "Info: The board was reset via software, webserver or OTA. Normal operation",
  "millis": "10001"
}
```

**`<hostname>/status` (availability / LWT)**

A plain-text availability topic (not JSON), following the standard MQTT Last-Will pattern:

- `online` is published **once, retained**, each time the device connects to the broker.
- `offline` is registered as the broker's Last Will and Testament (QoS 1, **retained**), so the broker publishes it automatically if the connection drops unexpectedly.

Because both values are retained, any subscriber (including Home Assistant after a restart) immediately receives the current availability without waiting for the next publish. The MQTT keepalive is set to 30 seconds, so after a sudden failure (power loss, Wi-Fi drop) the broker marks the device `offline` within roughly 45 seconds.

This topic is referenced by the `availability` block of every Home Assistant discovery message.

### Connection robustness

A few implementation details are worth knowing if you are debugging a flaky broker or a weak Wi-Fi link:

- **Publishes use QoS 0**; the command subscription uses QoS 1.
- The esp-mqtt **outbox is capped at 16 KB**. Queued traffic that cannot reach the broker fails to enqueue instead of growing on the heap until the device runs out of memory.
- **A failed publish is logged once per outage.** The first failure of an outage produces a `... MQTT msg could not be sent` line; the message is not repeated every cycle until a complete publish cycle has succeeded again.
- The MQTT client id is `BatteryEmulatorClient-<hostname>`.

## Subscriptions

The Battery-Emulator subscribes to `<hostname>/command/+`, e.g. `battery-emulator-a1b2/command/+` (subscription QoS 1).

The currently supported commands are:

- `BMSRESET` - Triggers a hardware power-cycle of the BMS. **Only acted upon if remote BMS reset is enabled** (see [Remote trigger through MQTT](../hardware/periodic_bms_reset.md#remote-trigger-through-mqtt)); otherwise the message is ignored.
- `PAUSE` - Triggers the pause feature
- `RESUME` - Resumes from the paused state, and clears an equipment stop, allowing contactors to re-close (see [Opening and closing contactors](#opening-and-closing-contactors-stop-and-pause-vs-resume))
- `RESTART` - Restarts the Battery-Emulator (pauses, then reboots the board after a short delay)
- `STOP` - Triggers the equipment stop (opens contactors); see [Opening and closing contactors](#opening-and-closing-contactors-stop-and-pause-vs-resume)
- `SET_LIMITS` - Sets a temporary charge and/or discharge limit

For example: `battery-emulator-a1b2/command/PAUSE`

### Opening and closing contactors (`STOP` and `PAUSE` vs. `RESUME`)

The auto-discovered button labelled **"Open Contactors"** is the `STOP` command. There is **no separate "Close Contactors" command or button** - closing the contactors is exposed through MQTT as the `RESUME` command (the auto-discovered "Resume charge/discharge" button). The naming is asymmetric, which is why it can look as though closing is missing: `STOP` is named after its contactor effect, while its inverse `RESUME` is named after its pause effect.

Under the hood, `STOP` latches an equipment-stop state, and `RESUME` clears it:

- `STOP` sets the equipment-stop flag, which forces the contactor state machine open and prevents it from re-closing.
- `RESUME` clears the equipment-stop flag, which allows the contactor state machine to run through precharge and close again.

So the effective mapping is:

| Command | Effect on contactors | HA button label |
| ------- | -------------------- | --------------- |
| `STOP`   | Opens (sets equipment stop) | Open Contactors |
| `RESUME` | Closes (clears equipment stop) | Resume charge/discharge |

Two things to keep in mind:

- `RESUME` *allows* the contactors to close; it does not *force* them closed. They only actually close if the inverter also permits closing and the normal preconditions are met (battery detected, past the post-boot startup delay, no faults). If the inverter is what is holding the contactors open, `RESUME` will not override that.
- `RESUME` does double duty - it both ends a `PAUSE` and clears an equipment stop. There is no command that closes the contactors without also resuming charge/discharge, just as `STOP` cannot open them without also pausing.

### SET_LIMITS

Sets a **temporary** charge and/or discharge current limit for `timeout` seconds. While the limit is active it overrides the manual (user-set) limit in settings.

Limits are set as deciampere, i.e. `300` = 30.0 A.

| Parameter      | Data type | Default       |
| -------------- | --------- | ------------- |
| `max_charge`    | number    | disable limit |
| `max_discharge` | number    | disable limit |
| `timeout`       | seconds   | 30            |

If `max_charge` or `max_discharge` is omitted (or not an integer), the corresponding limit is disabled. If `timeout` is omitted, it defaults to 30 seconds.

Example payload (max charge 30 A, max discharge 40 A, timeout 60 seconds), published to `battery-emulator-a1b2/command/SET_LIMITS`:

```json
{
  "max_charge": 300,
  "max_discharge": 400,
  "timeout": 60
}
```

#### How the limit is applied and expires

- **Temporary by design.** The main loop checks every cycle whether `now > (timestamp_of_last_command + timeout)`. Once that is true, the remote limit flags are cleared and the remote values are zeroed, so the limit must be **re-sent before each timeout** to stay in effect.
- **Not persisted.** The remote limit is never written to flash, so it is also cleared by a reboot. After power-on no remote limit is active until a new `SET_LIMITS` is received.
- **Reverts to the manual/BMS limit, not to "unrestricted".** When the remote limit expires, the allowed current falls back to the manual (user-set) limit, or to the BMS/inverter-derived limit if no manual limit applies.
- **Overrides rather than combines with the manual limit.** While a remote limit is active, the manual user limit is bypassed - the remote value is used instead. The remote limit can therefore sit *above* your manual limit during the active window. It still only ever *lowers* the BMS/inverter-derived allowed current (it caps, it cannot raise the battery's own limit).

To cancel a limit quickly, send a new message with a short timeout (for instance `1` second).

## Home Assistant Discovery

When [Home Assistant](home_assistant.md) auto-discovery is enabled, the device publishes retained configuration topics so entities are created automatically. Discovery topics are published under the configurable **Home Assistant auto discovery topic** (default `homeassistant`); the entity/object portion and the device identity are both derived from the device's hostname.

All discovery payloads share a common block:

```json
{
  "device": {
    "identifiers": ["battery-emulator-a1b2"],
    "model": "Battery Emulator",
    "manufacturer": "FOSS",
    "name": "battery-emulator-a1b2",
    "hw_version": "Waveshare ESP32-S3 RS485 CAN",
    "sw_version": "11.2.dev",
    "configuration_url": "http://192.168.1.50"
  },
  "availability": [{ "topic": "battery-emulator-a1b2/status" }],
  "payload_available": "online",
  "payload_not_available": "offline",
  "enabled_by_default": true
}
```

`manufacturer` and `model` are fixed values; `identifiers` and `name` are the device's hostname, so each Battery-Emulator on the network appears as its own distinct HA device as long as each has a unique hostname (the default, MAC-based hostname already guarantees this). `hw_version` is the board name, `sw_version` the running firmware version, and `configuration_url` links straight to the device's Web UI from the Home Assistant device page.

The full set of auto-discovered sensors is generated from the battery and global templates.

**Per battery:** `SoC (scaled)`, `SoC (real)`, `State of Health`, `Temperature Min/Max`, `Battery Power`, `Battery Current`, `Cell Max/Min Voltage`, `Cell Voltage Delta`, `Battery Voltage`, `Total Capacity`, `Remaining Capacity (scaled)` and `(real)`, `Max Charge/Discharge Power`, `Battery Charged/Discharged Energy`, `Insulation Resistance`, `Balancing Cells`, `Balancing Status`, `Charging State`, `Limiting Factor`, plus the battery-specific `DC-DC Current/Voltage` (Tesla), the `BYD Auto-cal` set and `Min/Max Cell Number` (BYD Atto 3), and `Hx` (Nissan Leaf).

**Emulator-level (diagnostic):** `BMS Status`, `Pause Status`, `Event Level`, `Emulator Status`, `Emulator Uptime`, `Emulator Version`, `CPU Temperature`, `Event`, and - when enabled - `Heap Free`, `Heap Max Block`, `Heap Min Free`, `Heap Fragmentation`. These are published with `"entity_category": "diagnostic"`, so Home Assistant files them under the device's Diagnostic section instead of the main sensor list. The **Reboot Emulator** button is a diagnostic entity too.

With a second (or third) battery, each battery sensor is duplicated with a ` 2` (or ` 3`) name suffix and a `_2` (`_3`) suffix on its `unique_id` and object ID; its `state_topic` points at `.../info_2` (`.../info_3`), and its `value_template` uses the plain, un-suffixed key.

### Sensor discovery

Topic: `<discovery topic>/sensor/<hostname>/<entity_id>/config` (battery 2/3 sensors use the `_2`/`_3`-suffixed entity id in the topic, e.g. `.../SOC_2/config`).

Example (`homeassistant/sensor/battery-emulator-a1b2/SOC/config`):

```json
{
  "name": "SoC (scaled)",
  "state_topic": "battery-emulator-a1b2/info",
  "unique_id": "battery-emulator-a1b2_SOC",
  "default_entity_id": "sensor.battery-emulator-a1b2_SOC",
  "value_template": "{{ value_json.SOC | default(none) }}",
  "unit_of_measurement": "%",
  "device_class": "battery",
  "state_class": "measurement",
  "suggested_display_precision": 1,
  "device": { "identifiers": ["battery-emulator-a1b2"], "model": "Battery Emulator", "manufacturer": "FOSS", "name": "battery-emulator-a1b2", "hw_version": "Waveshare ESP32-S3 RS485 CAN", "sw_version": "11.2.dev", "configuration_url": "http://192.168.1.50" },
  "availability": [{ "topic": "battery-emulator-a1b2/status" }],
  "payload_available": "online",
  "payload_not_available": "offline",
  "enabled_by_default": true
}
```

The same sensor for a second battery (`.../SOC_2/config`) differs only in: `"name": "SoC (scaled) 2"`, `"unique_id": "battery-emulator-a1b2_SOC_2"`, `"default_entity_id": "sensor.battery-emulator-a1b2_SOC_2"`, and `"state_topic": "battery-emulator-a1b2/info_2"` - the `value_template` stays `{{ value_json.SOC | default(none) }}`.

#### How the discovery payload is built

- **`value_template` uses `| default(none)`.** Keys that are legitimately absent (a battery that has not been detected yet, a capacity that is not known yet) therefore land in Home Assistant as *unknown* instead of raising a template error on every message.
- **`state_class`** is set to `measurement` for every sensor that has a `device_class`. The numeric sensors that deliberately have no `device_class` - `balancing_active_cells`, `insulation_resistance`, `leaf_hx`, `heap_fragmentation` - get `measurement` explicitly.
- **Capacity sensors use `device_class: energy_storage`**, not `energy`. Home Assistant rejects `energy` combined with `state_class: measurement`, and `total_capacity` / `remaining_capacity*` represent a currently stored amount rather than a running total.
- **`charged_energy` / `discharged_energy` keep `device_class: energy`** but use `state_class: total_increasing`, since they are genuine lifetime counters.
- **`suggested_display_precision`** is set to 3 for cell min/max voltage, 2 for `leaf_hx`, 1 for battery current, CPU temperature, both SoC sensors and heap fragmentation, and 0 for insulation resistance. It is deliberately not applied to `battery_voltage`.
- **MDI icons** are assigned centrally: by entity for the status-like sensors (`mdi:fuel-cell` for the balancing pair, `mdi:information-box-outline` for BMS status, `mdi:resistor` for insulation, `mdi:battery-heart-variant` for Hx, `mdi:home-battery` / `mdi:home-battery-outline` for charging state and limiting factor, `mdi:information-outline` for emulator status / event level, `mdi:battery-outline` for pause status, `mdi:tag-outline` for the version, `mdi:memory` for the heap sensors), and by device class for the rest (`mdi:current-dc` for voltage, `mdi:equal` for current).

### Cell-voltage discovery

Topic: `<discovery topic>/sensor/<hostname>/cell_voltage<N>/config` (second battery uses a `_2_` suffix in the topic, third battery `_3_`).

Example (`homeassistant/sensor/battery-emulator-a1b2/cell_voltage96/config`):

```json
{
  "name": "Battery Cell Voltage 96",
  "default_entity_id": "sensor.battery-emulator-a1b2_battery_voltage_cell96",
  "unique_id": "battery-emulator-a1b2battery-emulator-a1b2__battery_voltage_cell96",
  "device_class": "voltage",
  "state_class": "measurement",
  "state_topic": "battery-emulator-a1b2/spec_data",
  "unit_of_measurement": "V",
  "suggested_display_precision": 3,
  "icon": "mdi:current-dc",
  "value_template": "{{ value_json.cell_voltages[95] }}",
  "device": { "identifiers": ["battery-emulator-a1b2"], "model": "Battery Emulator", "manufacturer": "FOSS", "name": "battery-emulator-a1b2", "hw_version": "Waveshare ESP32-S3 RS485 CAN", "sw_version": "11.2.dev", "configuration_url": "http://192.168.1.50" },
  "availability": [{ "topic": "battery-emulator-a1b2/status" }],
  "payload_available": "online",
  "payload_not_available": "offline",
  "enabled_by_default": true
}
```

Cell-voltage entities update every 60 seconds, matching the `spec_data` publish cadence.

Cell-voltage discovery is **retried until the cell count is known**. A battery that has not yet reported how many cells it has does not block the rest of the discovery pack - the per-cell configs are simply published on a later cycle, once the count arrives.

### Event discovery

Topic: `<discovery topic>/sensor/<hostname>/event/config`

```json
{
  "name": "Event",
  "state_topic": "battery-emulator-a1b2/events",
  "unique_id": "battery-emulator-a1b2_event",
  "default_entity_id": "sensor.battery-emulator-a1b2_event",
  "value_template": "{{ value_json.event_type ~ ' (c:' ~ value_json.count ~ ',m:' ~ value_json.millis ~ ') ' ~ value_json.message }}",
  "json_attributes_topic": "battery-emulator-a1b2/events",
  "json_attributes_template": "{{ value_json | tojson }}",
  "icon": "mdi:information-outline",
  "entity_category": "diagnostic",
  "device": { "identifiers": ["battery-emulator-a1b2"], "model": "Battery Emulator", "manufacturer": "FOSS", "name": "battery-emulator-a1b2", "hw_version": "Waveshare ESP32-S3 RS485 CAN", "sw_version": "11.2.dev", "configuration_url": "http://192.168.1.50" },
  "availability": [{ "topic": "battery-emulator-a1b2/status" }],
  "payload_available": "online",
  "payload_not_available": "offline",
  "enabled_by_default": true
}
```

### Button (command) discovery

In addition to sensors, Home Assistant **Button** entities are auto-discovered for the supported commands, so they can be triggered from the HA dashboard. These are published once on MQTT connect, and only marked as done once *all* of them went out - a mid-list failure is retried on the next connect rather than leaving the remaining buttons undiscovered.

Topic: `<discovery topic>/button/<hostname>/<command>/config`

| Button | Command | Icon | Action |
| ------ | ------- | ---- | ------ |
| Reset BMS | `BMSRESET` | `mdi:star-four-points-box-outline` | Triggers the BMS reset feature (only if remote BMS reset is enabled) |
| Pause charge/discharge | `PAUSE` | `mdi:battery-minus-outline` | Triggers the pause feature |
| Resume charge/discharge | `RESUME` | `mdi:battery-sync-outline` | Resumes from the paused state |
| Reboot Emulator | `RESTART` | `mdi:restart` | Restarts the Battery-Emulator (diagnostic entity) |
| Open Contactors | `STOP` | `mdi:battery-remove-outline` | Triggers the stop feature |

## Running multiple Battery Emulators on one broker

Multiple Battery Emulators can share the same MQTT broker, and they separate themselves automatically: the MQTT topic name, the HA object-ID prefix, the HA device name, and the HA device identifier all default to the device's hostname, which itself defaults to `battery-emulator-a1b2` (`a1b2` being the last two bytes of the device's MAC address) - making it unique out of the box without any manual configuration. If you'd prefer a friendlier name, set a custom hostname on the Connectivity settings page; just make sure each device on the same broker gets a different one.

## Migrating from older releases

Recent builds changed the MQTT layout in several ways that affect anyone consuming the raw topics (manually configured `mqtt:` sensors, Node-RED flows, Telegraf, custom scripts). **Home Assistant auto-discovery users are migrated automatically** - the discovery configs are updated and all `unique_id`s are preserved, so existing entities keep their history and no duplicates appear. Some entity *display names* changed (`SOC (Scaled)` → `SoC (scaled)`, `Stat Batt Power` → `Battery Power`, `State Of Health` → `State of Health`, the `RESTART` button → `Reboot Emulator`); any custom name you set in Home Assistant is untouched.

- **Battery 2/3 moved to their own topics.** Previously, a second/third battery's values were added to `.../info` with suffixed keys (`SOC_2`, `battery_voltage_3`, …). They are now published to `.../info_2` and `.../info_3` using the same plain key names as battery #1. Update raw consumers to subscribe to the per-battery topic and drop the key suffix.
- **`balancing_data*` topics were removed.** The per-cell balancing arrays are now part of the `spec_data*` messages, under the `cell_balancing` key. Update raw consumers to read `cell_balancing` from `.../spec_data` (or `.../spec_data_2` / `_3`).
- **`balancing_status` no longer reports `Blocked`.** That state is now published as `Pending`. Any automation matching on the literal string needs updating.
- **The discovery prefix is configurable.** It still defaults to `homeassistant`, so nothing changes unless you set the new **Home Assistant auto discovery topic** field.
- **Several emulator-level entities became diagnostic.** They still exist with the same `unique_id`, but Home Assistant now lists them under the device's Diagnostic section.

!!! note "NOTE"
    Cell data now updates every 60 seconds rather than at the main publish interval, and battery values are omitted from the JSON until real data has been received from the battery - consumers must tolerate absent keys rather than assuming every key is present in every message.

## References

- [Home Assistant](home_assistant.md) - quick start guide with Battery Emulator
- [Home Assistant MQTT overview](https://www.home-assistant.io/integrations/mqtt/) - brokers, discovery, configuration and HA services related to MQTT
- [Home Assistant MQTT Sensor](https://www.home-assistant.io/integrations/sensor.mqtt/) - manual (non-discovery) setup of MQTT sensors
- [ESP-IDF MQTT (esp-mqtt) documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html) - the MQTT client library currently used
