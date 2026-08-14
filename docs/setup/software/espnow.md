---
title: "ESPNow"
---

## Some background

ESP-NOW is a low-latency wireless protocol by Espressif that allows direct device-to-device communication without a router. It works on the data-link layer, bypassing higher OSI layers, which results in fast response times and minimal overhead. It supports ESP8266, ESP32, ESP32-S, and ESP32-C series chips and can coexist with Wi-Fi and Bluetooth LE.
It’s ideal for smart home devices, remote controls, and sensor networks, supporting one-to-one, one-to-many, and many-to-many communication.

### **Key Features:**
* Low latency (millisecond-level delay)
* No gateway required
* Encrypted or unencrypted communication
* Range up to ~220 meters in open space
* Supports callbacks for send/receive events
* Payload up to 250 bytes in ESP-NOW v1, raised to 1470 bytes in ESP-NOW v2 (ESP-IDF 5.4+)

Battery Emulator implements ESP-NOW v2 in the **ESPNow** integration.

!!! note "NOTE" 
    Enabling ESPNow increases the temperature of the ESP chip, as it shares the radio interface with Wi-Fi. Without ESP-NOW, the Wi-Fi client connection lets the modem duty-cycle down to the network's DTIM interval. The moment ESP-NOW is active, the connectionless path needs the PHY/RX chain powered continuously — Espressif's own FAQ states that once the device enters modem-sleep it can't service ESP-NOW. So you flip from a low duty-cycle radio to a ~100%-on radio, and the PA/PHY idle current is what generates heat with ESPNow enabled. It's the radio staying lit.

## **ESPNow in Battery Emulator context**

Any ESP32 device nearby can display Battery Emulator data without any physical connection to the Battery Emulator. The emulator broadcasts (or unicasts) its full telemetry set: emulator-wide state, per-battery values for all three batteries, cell voltages and balancing bits, and the recent event log.

### Enabling it

On the settings page, under **Integration settings**:

| Setting | Meaning |
| --- | --- |
| **Enable ESPNow** | Turns telemetry transmission on. |
| **ESPNow receiver MACs** | Comma-separated list of receiver MAC addresses, max 8, e.g. `AA:BB:CC:DD:EE:FF, 11:22:33:44:55:66`. Separators are flexible (`:`, `-`, or none). Leave **empty to broadcast** to every device in range. Takes effect after a restart. |

Each node's own station MAC is shown on its web UI, which is the address to enter in another node's receiver list. The emulator's station MAC is also the source address of the ESPNow frames.

ESPNow peers are registered with channel 0, meaning they follow the emulator's current Wi-Fi channel. **A receiver must be on the same Wi-Fi channel as the emulator.** A receiver that joins the same access point ends up there automatically; a standalone receiver that never associates stays on channel 1 and will hear nothing if the emulator is joined to a network on a different channel.

## **Protocol version 2**

!!! warning "This replaces the v1 protocol"
    Protocol v1 broadcast raw C structs copied byte-for-byte out of the datalayer. That broke every receiver whenever a field was inserted, reordered or resized, and it quantized cell voltages to 20 mV to fit the 250 byte v1 frame. **v1 receivers will not decode v2 frames** — see [Migrating from v1](#migrating-from-v1).

v2 is a self-describing key/length/value (TLV) stream:

* Adding a new field never breaks an existing receiver. Unknown keys are skipped using the length that is always present in the record.
* Adding a new *data type* never breaks an existing receiver either: the length is encoded in the tag independently of the type, so a parser that has never heard of a type can still skip past it. This is the property that lets the protocol grow without another compatibility break.
* Fields a given battery integration does not provide are simply not emitted, so receivers can tell **"not supported" apart from "zero"**.
* Cell voltages are transmitted as raw millivolts. No quantization, for all three batteries.

### Wire format

Every ESP-NOW packet is one frame: a 12 byte header followed by TLV records.

Header (12 bytes, little-endian):

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| 0 | uint8 | magic[0] | `'B'` (0x42) |
| 1 | uint8 | magic[1] | `'E'` (0x45) |
| 2 | uint8 | protocol_version | 2 |
| 3 | uint8 | frame_type | see below |
| 4 | uint16 | emulator_id | low 16 bits of the emulator's factory MAC |
| 6 | uint8 | battery_id | 0 = emulator-wide, 1..3 = battery number |
| 7 | uint8 | flags | bit 0 = `MORE_CHUNKS`, another chunk of this frame type follows |
| 8 | uint32 | uptime_s | emulator uptime in seconds, so a receiver can detect reboots |

TLV record:

| Field | Notes |
| --- | --- |
| uint8 key | see the key registry below |
| uint8 tag | `(type_class << 5) \| length_code` |
| length | `length_code` < 30: none, value length **is** the length code. `== 30`: a uint8 length follows. `== 31`: a uint16 length follows (LE). |
| value | `length` bytes |

Type classes (`tag >> 5`) are advisory: a receiver never needs them to parse the stream, only to interpret a key it already knows.

| Class | Type | Encoding |
| --- | --- | --- |
| 0 | UINT | unsigned integer, little-endian, 1/2/4/8 bytes |
| 1 | INT | signed two's complement, little-endian, 1/2/4/8 bytes |
| 2 | FLOAT | IEEE-754 binary32, little-endian, 4 bytes |
| 3 | BOOL | 1 byte, 0 or 1 |
| 4 | STR | UTF-8 text, **not** NUL terminated |
| 5 | BYTES | opaque octets |
| 6 | ARR16 | array of little-endian uint16 |
| 7 | BITS | bit array, LSB first within each byte |

The whole of forward compatibility is this skip loop:

```C
while (i + 2 <= len) {
  uint8_t key = buf[i++];
  uint8_t tag = buf[i++];
  uint8_t lc  = tag & 0x1F;
  uint16_t n;
  if      (lc < 30)  n = lc;
  else if (lc == 30) n = buf[i++];
  else             { n = buf[i] | (buf[i + 1] << 8); i += 2; }
  handle_or_ignore(key, tag >> 5, &buf[i], n);
  i += n;
}
```

Key `0xFF` is reserved as an escape for a future 16 bit key space. The extended key is carried **inside** the value — its first two bytes, little-endian — and *not* between the key and the tag. That keeps the tag as the second byte of every record, so the loop above stays correct with no knowledge of extended keys at all.

### Frame types

| Value | Frame | battery_id | Contents |
| --- | --- | --- | --- |
| 0x01 | `SYSTEM` | 0 | emulator-wide state |
| 0x02 | `BATTERY` | 1..3 | per-battery scalars |
| 0x03 | `CELLS` | 1..3 | cell voltages + balancing bits |
| 0x04 | `EVENT` | 0 | one emulator event |

### Transmission schedule

One frame is emitted per tick with at least 20 ms between frames, so the Wi-Fi stack always finishes a send before the next one starts. A full round is:

* **SYSTEM + BATTERY** frames every **1 s**.
* **CELLS** frames every **5 s** — the largest payload, so it goes out less often.
* **EVENT** frames every **10 s**, or immediately when something new happens.

Events are not streamed as they occur: the **10 most recent** entries are re-sent as a batch, so a receiver that starts after the emulator still gets the history. Every frame of a batch carries `EVENT_INDEX` and `EVENT_TOTAL`, and all but the last set `MORE_CHUNKS`. A receiver should therefore **replace** its list on each batch rather than append, and should **not** de-duplicate — the repetition is intended.

### Frame size and chunking

ESP-NOW v2 raises the maximum payload from 250 to 1470 bytes, which is what makes unquantized 16 bit cell voltages practical. v2 is assumed on the emulator side: every SoC the emulator runs on supports it, so there is no runtime version negotiation.

The limit that matters is the **receiver's** buffer, not its silicon. A receiver that has not raised its own receive buffer above the 250 byte default silently drops larger frames — ESPHome's `espnow` component is one such case, where `max_payload_size: 1470` has to be set explicitly. The cell voltage array is therefore always split into index-tagged chunks sized by `ESPNOW_MAX_PAYLOAD`, so lowering that one constant in `espnow.cpp` is enough to talk to a 250 byte receiver.

**Receivers must always honour `ESPNOW_KEY_CELL_INDEX` rather than assuming a chunk starts at cell 0.**

## Key registry

Keys are globally unique across all frame types, so a receiver can use a single dispatch table.

| Range | Purpose |
| --- | --- |
| 0x01..0x2F | emulator-wide |
| 0x30..0x4F | battery configuration / nameplate |
| 0x50..0x8F | battery live measurements |
| 0x90..0x9F | cell arrays |
| 0xA0..0xAF | events |
| 0xB0..0xEF | free for future upstream use |
| 0xF0..0xFE | **reserved for private forks** — upstream will never allocate here |
| 0xFF | escape for a future 16 bit key space |

### Emulator-wide (`SYSTEM`)

| Key | Name | Type | Meaning |
| --- | --- | --- | --- |
| 0x01 | `FW_VERSION` | STR | firmware version string |
| 0x02 | `HOSTNAME` | STR | device hostname |
| 0x03 | `SOURCE_MAC` | BYTES | 6 bytes, factory MAC of the emulator |
| 0x04 | `SYSTEM_STATUS` | UINT8 | `system_status_enum` |
| 0x05 | `PAUSE_STATUS` | UINT8 | `battery_pause_status` |
| 0x06 | `EVENT_LEVEL` | UINT8 | highest active `EVENTS_LEVEL_TYPE` |
| 0x07 | `EMULATOR_STATUS` | UINT8 | `EMULATOR_STATUS` |
| 0x08 | `CPU_TEMP_C` | FLOAT | degrees C, **omitted** if measurement is disabled |
| 0x09 | `CPU_FREE_HEAP` | UINT32 | bytes |
| 0x0A | `BATTERY_COUNT` | UINT8 | number of configured batteries, 1..3 |
| 0x0B | `WIFI_RSSI_DBM` | INT8 | station RSSI, **omitted** when not associated |
| 0x0C | `INVERTER_ALIVE` | UINT8 | inverter keepalive countdown |
| 0x0D | `CONTACTORS` | UINT8 | 0 = starting up, 1 = engaged, 2 = opened |
| 0x0E | `DC_BUS_LIVE` | BOOL | DC bus energized towards the inverter |
| 0x0F | `EQUIPMENT_STOP` | BOOL | equipment stop latched |
| 0x10 | `IP_ADDRESS` | BYTES | 4 octets in display order, **omitted** when not associated |
| 0x11 | `SSID` | STR | SSID the station is joined to, **omitted** when not associated |
| 0x12 | `AP_ACTIVE` | BOOL | the emulator's own AP is up *right now* — reflects the live Wi-Fi mode, so it goes false once the AP is torn down on provisioning timeout even though the setting stays enabled |

### Battery nameplate (`BATTERY`)

| Key | Name | Type | Meaning |
| --- | --- | --- | --- |
| 0x30 | `NUMBER_OF_CELLS` | UINT8 | cells in the pack |
| 0x31 | `CHEMISTRY` | UINT8 | `battery_chemistry_enum` |
| 0x32 | `TOTAL_CAPACITY_WH` | UINT32 | Wh, **omitted** while still zero |
| 0x33 | `REPORTED_CAPACITY_WH` | UINT32 | Wh, as presented to the inverter |
| 0x34 | `MAX_DESIGN_VOLTAGE_DV` | UINT16 | deciVolt |
| 0x35 | `MIN_DESIGN_VOLTAGE_DV` | UINT16 | deciVolt |
| 0x36 | `MAX_CELL_DESIGN_MV` | UINT16 | mV |
| 0x37 | `MIN_CELL_DESIGN_MV` | UINT16 | mV |
| 0x38 | `MAX_CELL_DEVIATION_MV` | UINT16 | mV |

### Battery live values (`BATTERY`)

Link state (`BATTERY_DETECTED`, `CAN_ALIVE`, `CAN_ERROR_COUNTER`, `REAL_BMS_STATUS`, `LED_MODE`) is always sent. The measurement keys below are only emitted once the battery has actually been seen and the system has booted up, mirroring the MQTT gating — otherwise the datalayer defaults look like real readings for the first minute after boot.

| Key | Name | Type | Meaning |
| --- | --- | --- | --- |
| 0x50 | `SOC_PPTT` | UINT16 | 0.01 %, scaled/reported SOC |
| 0x51 | `SOC_REAL_PPTT` | UINT16 | 0.01 %, real SOC from the BMS |
| 0x52 | `SOH_PPTT` | UINT16 | 0.01 % |
| 0x53 | `VOLTAGE_DV` | UINT16 | deciVolt |
| 0x54 | `CURRENT_DA` | INT16 | deciAmpere, + = charging |
| 0x55 | `REPORTED_CURRENT_DA` | INT16 | deciAmpere, all batteries summed |
| 0x56 | `ACTIVE_POWER_W` | INT32 | W, + = charging |
| 0x57 | `REMAINING_CAPACITY_WH` | UINT32 | Wh, real |
| 0x58 | `REPORTED_REMAIN_WH` | UINT32 | Wh, as presented to the inverter |
| 0x59 | `MAX_CHARGE_POWER_W` | UINT32 | W |
| 0x5A | `MAX_DISCHARGE_POWER_W` | UINT32 | W |
| 0x5B | `MAX_CHARGE_CURRENT_DA` | UINT16 | deciAmpere |
| 0x5C | `MAX_DISCHARGE_CURRENT_DA` | UINT16 | deciAmpere |
| 0x5D | `OVERRIDE_CHARGE_W` | UINT32 | W, user override |
| 0x5E | `OVERRIDE_DISCHARGE_W` | UINT32 | W, user override |
| 0x5F | `CELL_MAX_MV` | UINT16 | mV, **omitted** until the cell array has been populated |
| 0x60 | `CELL_MIN_MV` | UINT16 | mV, same gating |
| 0x61 | `TEMPERATURE_MAX_DC` | INT16 | 0.1 degrees C |
| 0x62 | `TEMPERATURE_MIN_DC` | INT16 | 0.1 degrees C |
| 0x63 | `TOTAL_CHARGED_WH` | INT32 | Wh lifetime, **omitted** unless the integration supports it |
| 0x64 | `TOTAL_DISCHARGED_WH` | INT32 | Wh lifetime, same gating |
| 0x65 | `INSULATION_KOHM` | UINT16 | kOhm, **omitted** until a valid sample exists |
| 0x66 | `BALANCING_STATUS` | UINT8 | `balancing_status_enum` |
| 0x67 | `BALANCING_ACTIVE_CELLS` | UINT16 | count of shunts currently on |
| 0x68 | `CHARGING_STATE` | UINT8 | `ChargingState` |
| 0x69 | `LIMITING_FACTOR` | UINT8 | `LimitingFactor` |
| 0x6A | `REAL_BMS_STATUS` | UINT8 | `real_bms_status_enum` |
| 0x6B | `CAN_ALIVE` | UINT8 | battery keepalive countdown |
| 0x6C | `CAN_ERROR_COUNTER` | UINT16 | CAN CRC error count |
| 0x6D | `LED_MODE` | UINT8 | `led_mode_enum` |
| 0x6E | `BATTERY_DETECTED` | BOOL | at least one frame ever received |
| 0x6F | `DCDC_CURRENT_DA` | INT16 | deciAmpere, **Tesla only** |
| 0x70 | `DCDC_VOLTAGE_MV` | UINT16 | mV, **Tesla only** |
| 0x71 | `AUTOCAL_TAPER` | BOOL | **BYD Atto 3 only** |
| 0x72 | `AUTOCAL_DWELL_S` | UINT32 | s, **BYD Atto 3 only** |
| 0x73 | `AUTOCAL_COOLDOWN_READY` | BOOL | **BYD Atto 3 only** |
| 0x74 | `AUTOCAL_SOC_DRIFT` | FLOAT | %, **BYD Atto 3 only** |

### Cell arrays (`CELLS`)

| Key | Name | Type | Meaning |
| --- | --- | --- | --- |
| 0x90 | `CELL_COUNT` | UINT16 | total cells in this battery |
| 0x91 | `CELL_INDEX` | UINT16 | zero-based index of the first cell in this chunk |
| 0x92 | `CELL_VOLTAGES_MV` | ARR16 | raw mV, one entry per cell, unquantized |
| 0x93 | `CELL_BALANCING` | BITS | one bit per cell, set = shunt on, relative to `CELL_INDEX` |

### Events (`EVENT`)

| Key | Name | Type | Meaning |
| --- | --- | --- | --- |
| 0xA0 | `EVENT_ID` | UINT16 | `EVENTS_ENUM_TYPE` ordinal |
| 0xA1 | `EVENT_NAME` | STR | symbolic name, e.g. `EVENT_CAN_RX_FAILURE` |
| 0xA2 | `EVENT_SEVERITY` | UINT8 | `EVENTS_LEVEL_TYPE` |
| 0xA3 | `EVENT_STATE` | UINT8 | `EVENTS_STATE_TYPE` |
| 0xA4 | `EVENT_COUNT` | UINT8 | occurrences since boot |
| 0xA5 | `EVENT_DATA` | UINT8 | event specific payload byte |
| 0xA6 | `EVENT_MILLIS` | UINT64 | `millis64()` at the last occurrence |
| 0xA7 | `EVENT_MESSAGE` | STR | human readable description |
| 0xA8 | `EVENT_INDEX` | UINT8 | position in the replay batch, 0 = most recent |
| 0xA9 | `EVENT_TOTAL` | UINT8 | events in this replay batch, 1..10 |

### Enumerated values

| Enum | Values |
| --- | --- |
| `system_status_enum` | 0 STANDBY, 1 INACTIVE, 3 ACTIVE, 4 FAULT, 5 UPDATING |
| `battery_pause_status` | 0 NORMAL, 1 PAUSING, 2 PAUSED, 3 RESUMING |
| `EVENTS_LEVEL_TYPE` | 0 INFO, 1 DEBUG, 2 WARNING, 3 UPDATE, 4 ERROR |
| `EMULATOR_STATUS` | 0 OK, 1 WARNING, 2 ERROR, 3 UPDATING |
| `EVENTS_STATE_TYPE` | 0 PENDING, 1 INACTIVE, 2 ACTIVE, 3 ACTIVE_LATCHED |
| `battery_chemistry_enum` | 0 Autodetect, 1 NCA, 2 NMC, 3 LFP, 4 ZEBRA |
| `real_bms_status_enum` | 0 DISCONNECTED, 1 STANDBY, 2 ACTIVE, 3 FAULT |
| `balancing_status_enum` | 0 UNKNOWN, 1 ERROR, 2 READY, 3 ACTIVE, 4 BLOCKED (shown as "Pending") |
| `ChargingState` | 0 Idle, 1 Charging, 2 Discharging |
| `LimitingFactor` | 0 None, 1 Inverter, 2 UserSetting, 3 Battery |
| `led_mode_enum` | 0 CLASSIC, 1 FLOW, 2 HEARTBEAT (plus GRB variants on T-2CAN) |


!!! warning "Compatibility rules for future changes"
    * Never reuse or change the meaning of an allocated key. Retire it instead.
    * Never change the unit or scaling of an allocated key. Allocate a new key.
    * New keys, new type classes and new frame types may be added freely.
    * Bump `ESPNOW_PROTOCOL_VERSION` only for a change that violates the above.

## **Examples of implementation**

### ESPHome

ESPHome's `espnow` component can receive the frames directly, with the TLV loop written as a lambda. Two settings matter:

```yaml
espnow:
  max_payload_size: 1470   # the default 250 silently drops CELLS frames
  # ...
```

If you cannot raise the receive buffer, lower `ESPNOW_MAX_PAYLOAD` in `espnow.cpp` on the emulator instead — the cell array is chunked to whatever fits, and the rest of the protocol already fits inside 250 bytes.

### Arduino

Contents of **be_espnow.h** — the protocol constants and a complete decoder. It has no Arduino or ESP-IDF dependency, so the same file also works in a plain C or C++ receiver:

```C
/*
 * Battery Emulator ESP-NOW v2 receiver - protocol decoder.
 *
 * Self contained: no Arduino, no ESP-IDF, no dynamic allocation. Feed every received
 * ESP-NOW payload to be_espnow_receive() and read the be_state_t it fills in.
 */
#ifndef BE_ESPNOW_H_
#define BE_ESPNOW_H_

#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#define BE_MAX_CELLS 192
#define BE_MAX_BATTERIES 3
#define BE_EVENT_LOG 10

/* ---- wire constants, mirrored from Software/src/devboard/espnow/espnow.h ---- */
#define BE_MAGIC_0 0x42 /* 'B' */
#define BE_MAGIC_1 0x45 /* 'E' */
#define BE_PROTOCOL_VERSION 2
#define BE_HEADER_SIZE 12
#define BE_FLAG_MORE_CHUNKS 0x01

enum be_frame_type { BE_FRAME_SYSTEM = 0x01, BE_FRAME_BATTERY = 0x02, BE_FRAME_CELLS = 0x03, BE_FRAME_EVENT = 0x04 };

enum be_type {
  BE_TYPE_UINT = 0,
  BE_TYPE_INT = 1,
  BE_TYPE_FLOAT = 2,
  BE_TYPE_BOOL = 3,
  BE_TYPE_STR = 4,
  BE_TYPE_BYTES = 5,
  BE_TYPE_ARR16 = 6,
  BE_TYPE_BITS = 7
};

enum be_key {
  /* emulator wide */
  BE_KEY_FW_VERSION = 0x01,
  BE_KEY_HOSTNAME = 0x02,
  BE_KEY_SOURCE_MAC = 0x03,
  BE_KEY_SYSTEM_STATUS = 0x04,
  BE_KEY_PAUSE_STATUS = 0x05,
  BE_KEY_EVENT_LEVEL = 0x06,
  BE_KEY_EMULATOR_STATUS = 0x07,
  BE_KEY_CPU_TEMP_C = 0x08,
  BE_KEY_CPU_FREE_HEAP = 0x09,
  BE_KEY_BATTERY_COUNT = 0x0A,
  BE_KEY_WIFI_RSSI_DBM = 0x0B,
  BE_KEY_INVERTER_ALIVE = 0x0C,
  BE_KEY_CONTACTORS = 0x0D,
  BE_KEY_DC_BUS_LIVE = 0x0E,
  BE_KEY_EQUIPMENT_STOP = 0x0F,
  BE_KEY_IP_ADDRESS = 0x10,
  BE_KEY_SSID = 0x11,
  BE_KEY_AP_ACTIVE = 0x12,
  /* battery nameplate */
  BE_KEY_NUMBER_OF_CELLS = 0x30,
  BE_KEY_CHEMISTRY = 0x31,
  BE_KEY_TOTAL_CAPACITY_WH = 0x32,
  BE_KEY_REPORTED_CAPACITY_WH = 0x33,
  BE_KEY_MAX_DESIGN_VOLTAGE_DV = 0x34,
  BE_KEY_MIN_DESIGN_VOLTAGE_DV = 0x35,
  BE_KEY_MAX_CELL_DESIGN_MV = 0x36,
  BE_KEY_MIN_CELL_DESIGN_MV = 0x37,
  BE_KEY_MAX_CELL_DEVIATION_MV = 0x38,
  /* battery live */
  BE_KEY_SOC_PPTT = 0x50,
  BE_KEY_SOC_REAL_PPTT = 0x51,
  BE_KEY_SOH_PPTT = 0x52,
  BE_KEY_VOLTAGE_DV = 0x53,
  BE_KEY_CURRENT_DA = 0x54,
  BE_KEY_REPORTED_CURRENT_DA = 0x55,
  BE_KEY_ACTIVE_POWER_W = 0x56,
  BE_KEY_REMAINING_CAPACITY_WH = 0x57,
  BE_KEY_REPORTED_REMAIN_WH = 0x58,
  BE_KEY_MAX_CHARGE_POWER_W = 0x59,
  BE_KEY_MAX_DISCHARGE_POWER_W = 0x5A,
  BE_KEY_MAX_CHARGE_CURRENT_DA = 0x5B,
  BE_KEY_MAX_DISCHARGE_CURRENT_DA = 0x5C,
  BE_KEY_OVERRIDE_CHARGE_W = 0x5D,
  BE_KEY_OVERRIDE_DISCHARGE_W = 0x5E,
  BE_KEY_CELL_MAX_MV = 0x5F,
  BE_KEY_CELL_MIN_MV = 0x60,
  BE_KEY_TEMPERATURE_MAX_DC = 0x61,
  BE_KEY_TEMPERATURE_MIN_DC = 0x62,
  BE_KEY_TOTAL_CHARGED_WH = 0x63,
  BE_KEY_TOTAL_DISCHARGED_WH = 0x64,
  BE_KEY_INSULATION_KOHM = 0x65,
  BE_KEY_BALANCING_STATUS = 0x66,
  BE_KEY_BALANCING_ACTIVE_CELLS = 0x67,
  BE_KEY_CHARGING_STATE = 0x68,
  BE_KEY_LIMITING_FACTOR = 0x69,
  BE_KEY_REAL_BMS_STATUS = 0x6A,
  BE_KEY_CAN_ALIVE = 0x6B,
  BE_KEY_CAN_ERROR_COUNTER = 0x6C,
  BE_KEY_LED_MODE = 0x6D,
  BE_KEY_BATTERY_DETECTED = 0x6E,
  BE_KEY_DCDC_CURRENT_DA = 0x6F,
  BE_KEY_DCDC_VOLTAGE_MV = 0x70,
  BE_KEY_AUTOCAL_TAPER = 0x71,
  BE_KEY_AUTOCAL_DWELL_S = 0x72,
  BE_KEY_AUTOCAL_COOLDOWN_READY = 0x73,
  BE_KEY_AUTOCAL_SOC_DRIFT = 0x74,
  /* cells */
  BE_KEY_CELL_COUNT = 0x90,
  BE_KEY_CELL_INDEX = 0x91,
  BE_KEY_CELL_VOLTAGES_MV = 0x92,
  BE_KEY_CELL_BALANCING = 0x93,
  /* events */
  BE_KEY_EVENT_ID = 0xA0,
  BE_KEY_EVENT_NAME = 0xA1,
  BE_KEY_EVENT_SEVERITY = 0xA2,
  BE_KEY_EVENT_STATE = 0xA3,
  BE_KEY_EVENT_COUNT = 0xA4,
  BE_KEY_EVENT_DATA = 0xA5,
  BE_KEY_EVENT_MILLIS = 0xA6,
  BE_KEY_EVENT_MESSAGE = 0xA7,
  BE_KEY_EVENT_INDEX = 0xA8,
  BE_KEY_EVENT_TOTAL = 0xA9
};

/* A 256 bit set recording which keys a frame actually carried, so "not supported by this
 * battery" stays distinguishable from "reported as zero". */
typedef struct {
  uint8_t bits[32];
} be_keyset_t;

static inline void be_keyset_clear(be_keyset_t* k) {
  memset(k->bits, 0, sizeof(k->bits));
}
static inline void be_keyset_mark(be_keyset_t* k, uint8_t key) {
  k->bits[key >> 3] |= (uint8_t)(1u << (key & 7));
}
static inline bool be_has(const be_keyset_t* k, uint8_t key) {
  return (k->bits[key >> 3] & (1u << (key & 7))) != 0;
}

typedef struct {
  be_keyset_t seen;
  char fw_version[24];
  char hostname[32];
  uint8_t source_mac[6];
  uint8_t system_status;    /* 0 STANDBY 1 INACTIVE 3 ACTIVE 4 FAULT 5 UPDATING */
  uint8_t pause_status;     /* 0 NORMAL 1 PAUSING 2 PAUSED 3 RESUMING */
  uint8_t event_level;      /* 0 INFO 1 DEBUG 2 WARNING 3 UPDATE 4 ERROR */
  uint8_t emulator_status;  /* 0 OK 1 WARNING 2 ERROR 3 UPDATING */
  float cpu_temp_C;
  uint32_t cpu_free_heap;
  uint8_t battery_count;
  int8_t wifi_rssi_dBm;
  uint8_t inverter_alive;
  uint8_t contactors; /* 0 starting up, 1 engaged, 2 opened */
  bool dc_bus_live;
  bool equipment_stop;
  bool ap_active;
  uint8_t ip[4];
  char ssid[33];
} be_system_t;

typedef struct {
  be_keyset_t seen; /* keys from the last BATTERY frame */
  bool detected;
  uint8_t number_of_cells;
  uint8_t chemistry; /* 0 Autodetect 1 NCA 2 NMC 3 LFP 4 ZEBRA */
  uint32_t total_capacity_Wh;
  uint32_t reported_capacity_Wh;
  uint16_t max_design_voltage_dV;
  uint16_t min_design_voltage_dV;
  uint16_t max_cell_design_mV;
  uint16_t min_cell_design_mV;
  uint16_t max_cell_deviation_mV;
  uint16_t soc_pptt;
  uint16_t real_soc_pptt;
  uint16_t soh_pptt;
  uint16_t voltage_dV;
  int16_t current_dA;
  int16_t reported_current_dA;
  int32_t active_power_W;
  uint32_t remaining_capacity_Wh;
  uint32_t reported_remaining_Wh;
  uint32_t max_charge_power_W;
  uint32_t max_discharge_power_W;
  uint16_t max_charge_current_dA;
  uint16_t max_discharge_current_dA;
  uint32_t override_charge_W;
  uint32_t override_discharge_W;
  uint16_t cell_max_mV;
  uint16_t cell_min_mV;
  int16_t temperature_max_dC;
  int16_t temperature_min_dC;
  int32_t total_charged_Wh;
  int32_t total_discharged_Wh;
  uint16_t insulation_kOhm;
  uint8_t balancing_status; /* 0 UNKNOWN 1 ERROR 2 READY 3 ACTIVE 4 BLOCKED */
  uint16_t balancing_active_cells;
  uint8_t charging_state;  /* 0 Idle 1 Charging 2 Discharging */
  uint8_t limiting_factor; /* 0 None 1 Inverter 2 UserSetting 3 Battery */
  uint8_t real_bms_status; /* 0 DISCONNECTED 1 STANDBY 2 ACTIVE 3 FAULT */
  uint8_t can_alive;
  uint16_t can_error_counter;
  uint8_t led_mode;
  int16_t dcdc_current_dA;   /* Tesla only */
  uint16_t dcdc_voltage_mV;  /* Tesla only */
  bool autocal_taper;        /* BYD Atto 3 only */
  uint32_t autocal_dwell_s;  /* BYD Atto 3 only */
  bool autocal_cooldown_ready;
  float autocal_soc_drift;
  /* cell arrays, reassembled from ESPNOW_FRAME_CELLS chunks */
  uint16_t cell_count;
  uint16_t cell_mV[BE_MAX_CELLS];
  bool cell_balancing[BE_MAX_CELLS];
} be_battery_t;

typedef struct {
  uint16_t id;
  char name[40];
  char message[160];
  uint8_t severity;
  uint8_t state; /* 0 PENDING 1 INACTIVE 2 ACTIVE 3 ACTIVE_LATCHED */
  uint8_t occurrences;
  uint8_t data;
  uint64_t millis;
} be_event_t;

typedef struct {
  uint16_t emulator_id;
  uint32_t uptime_s;
  bool valid;
  be_system_t system;
  be_battery_t battery[BE_MAX_BATTERIES];
  be_event_t events[BE_EVENT_LOG];
  uint8_t event_count;
  /* scratch for reassembling one replay batch */
  be_event_t event_rx[BE_EVENT_LOG];
  uint8_t event_rx_total;
} be_state_t;

/* ---- primitive readers ------------------------------------------------------------ */

static inline uint64_t be_u(const uint8_t* v, uint16_t n) {
  uint64_t r = 0;
  if (n > 8) {
    n = 8;
  }
  for (uint16_t i = 0; i < n; i++) {
    r |= (uint64_t)v[i] << (8 * i);
  }
  return r;
}

static inline int64_t be_i(const uint8_t* v, uint16_t n) {
  uint64_t r = be_u(v, n);
  if (n > 0 && n < 8 && (v[n - 1] & 0x80)) {
    r |= ~0ULL << (8 * n); /* sign extend */
  }
  return (int64_t)r;
}

static inline float be_f(const uint8_t* v, uint16_t n) {
  float f = 0.0f;
  if (n == 4) {
    memcpy(&f, v, 4);
  }
  return f;
}

static inline void be_str(char* dst, size_t cap, const uint8_t* v, uint16_t n) {
  if (n > cap - 1) {
    n = (uint16_t)(cap - 1);
  }
  memcpy(dst, v, n);
  dst[n] = '\0';
}

/* ---- key handlers ----------------------------------------------------------------- */

static void be_apply_system(be_state_t* s, uint8_t key, const uint8_t* v, uint16_t n) {
  be_system_t* y = &s->system;
  switch (key) {
    case BE_KEY_FW_VERSION:
      be_str(y->fw_version, sizeof(y->fw_version), v, n);
      break;
    case BE_KEY_HOSTNAME:
      be_str(y->hostname, sizeof(y->hostname), v, n);
      break;
    case BE_KEY_SOURCE_MAC:
      if (n == 6) {
        memcpy(y->source_mac, v, 6);
      }
      break;
    case BE_KEY_SYSTEM_STATUS:
      y->system_status = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_PAUSE_STATUS:
      y->pause_status = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_EVENT_LEVEL:
      y->event_level = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_EMULATOR_STATUS:
      y->emulator_status = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_CPU_TEMP_C:
      y->cpu_temp_C = be_f(v, n);
      break;
    case BE_KEY_CPU_FREE_HEAP:
      y->cpu_free_heap = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_BATTERY_COUNT:
      y->battery_count = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_WIFI_RSSI_DBM:
      y->wifi_rssi_dBm = (int8_t)be_i(v, n);
      break;
    case BE_KEY_INVERTER_ALIVE:
      y->inverter_alive = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_CONTACTORS:
      y->contactors = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_DC_BUS_LIVE:
      y->dc_bus_live = be_u(v, n) != 0;
      break;
    case BE_KEY_EQUIPMENT_STOP:
      y->equipment_stop = be_u(v, n) != 0;
      break;
    case BE_KEY_AP_ACTIVE:
      y->ap_active = be_u(v, n) != 0;
      break;
    case BE_KEY_IP_ADDRESS:
      if (n == 4) {
        memcpy(y->ip, v, 4);
      }
      break;
    case BE_KEY_SSID:
      be_str(y->ssid, sizeof(y->ssid), v, n);
      break;
    default:
      break; /* unknown key: already skipped by length */
  }
}

static void be_apply_battery(be_battery_t* b, uint8_t key, const uint8_t* v, uint16_t n) {
  switch (key) {
    case BE_KEY_NUMBER_OF_CELLS:
      b->number_of_cells = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_CHEMISTRY:
      b->chemistry = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_TOTAL_CAPACITY_WH:
      b->total_capacity_Wh = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_REPORTED_CAPACITY_WH:
      b->reported_capacity_Wh = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_MAX_DESIGN_VOLTAGE_DV:
      b->max_design_voltage_dV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_MIN_DESIGN_VOLTAGE_DV:
      b->min_design_voltage_dV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_MAX_CELL_DESIGN_MV:
      b->max_cell_design_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_MIN_CELL_DESIGN_MV:
      b->min_cell_design_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_MAX_CELL_DEVIATION_MV:
      b->max_cell_deviation_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_BATTERY_DETECTED:
      b->detected = be_u(v, n) != 0;
      break;
    case BE_KEY_SOC_PPTT:
      b->soc_pptt = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_SOC_REAL_PPTT:
      b->real_soc_pptt = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_SOH_PPTT:
      b->soh_pptt = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_VOLTAGE_DV:
      b->voltage_dV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_CURRENT_DA:
      b->current_dA = (int16_t)be_i(v, n);
      break;
    case BE_KEY_REPORTED_CURRENT_DA:
      b->reported_current_dA = (int16_t)be_i(v, n);
      break;
    case BE_KEY_ACTIVE_POWER_W:
      b->active_power_W = (int32_t)be_i(v, n);
      break;
    case BE_KEY_REMAINING_CAPACITY_WH:
      b->remaining_capacity_Wh = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_REPORTED_REMAIN_WH:
      b->reported_remaining_Wh = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_MAX_CHARGE_POWER_W:
      b->max_charge_power_W = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_MAX_DISCHARGE_POWER_W:
      b->max_discharge_power_W = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_MAX_CHARGE_CURRENT_DA:
      b->max_charge_current_dA = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_MAX_DISCHARGE_CURRENT_DA:
      b->max_discharge_current_dA = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_OVERRIDE_CHARGE_W:
      b->override_charge_W = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_OVERRIDE_DISCHARGE_W:
      b->override_discharge_W = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_CELL_MAX_MV:
      b->cell_max_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_CELL_MIN_MV:
      b->cell_min_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_TEMPERATURE_MAX_DC:
      b->temperature_max_dC = (int16_t)be_i(v, n);
      break;
    case BE_KEY_TEMPERATURE_MIN_DC:
      b->temperature_min_dC = (int16_t)be_i(v, n);
      break;
    case BE_KEY_TOTAL_CHARGED_WH:
      b->total_charged_Wh = (int32_t)be_i(v, n);
      break;
    case BE_KEY_TOTAL_DISCHARGED_WH:
      b->total_discharged_Wh = (int32_t)be_i(v, n);
      break;
    case BE_KEY_INSULATION_KOHM:
      b->insulation_kOhm = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_BALANCING_STATUS:
      b->balancing_status = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_BALANCING_ACTIVE_CELLS:
      b->balancing_active_cells = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_CHARGING_STATE:
      b->charging_state = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_LIMITING_FACTOR:
      b->limiting_factor = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_REAL_BMS_STATUS:
      b->real_bms_status = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_CAN_ALIVE:
      b->can_alive = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_CAN_ERROR_COUNTER:
      b->can_error_counter = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_LED_MODE:
      b->led_mode = (uint8_t)be_u(v, n);
      break;
    case BE_KEY_DCDC_CURRENT_DA:
      b->dcdc_current_dA = (int16_t)be_i(v, n);
      break;
    case BE_KEY_DCDC_VOLTAGE_MV:
      b->dcdc_voltage_mV = (uint16_t)be_u(v, n);
      break;
    case BE_KEY_AUTOCAL_TAPER:
      b->autocal_taper = be_u(v, n) != 0;
      break;
    case BE_KEY_AUTOCAL_DWELL_S:
      b->autocal_dwell_s = (uint32_t)be_u(v, n);
      break;
    case BE_KEY_AUTOCAL_COOLDOWN_READY:
      b->autocal_cooldown_ready = be_u(v, n) != 0;
      break;
    case BE_KEY_AUTOCAL_SOC_DRIFT:
      b->autocal_soc_drift = be_f(v, n);
      break;
    default:
      break;
  }
}

/* ---- frame entry point ------------------------------------------------------------ */

typedef void (*be_event_batch_cb)(const be_state_t* s);

static void be_espnow_receive(be_state_t* s, const uint8_t* buf, int len) {
  if (len < BE_HEADER_SIZE || buf[0] != BE_MAGIC_0 || buf[1] != BE_MAGIC_1) {
    return; /* not ours */
  }
  if (buf[2] != BE_PROTOCOL_VERSION) {
    return; /* a future major revision - nothing sensible to do */
  }

  const uint8_t frame_type = buf[3];
  const uint16_t emulator_id = (uint16_t)(buf[4] | (buf[5] << 8));
  const uint8_t battery_id = buf[6];
  const uint8_t flags = buf[7];
  const uint32_t uptime_s = (uint32_t)buf[8] | ((uint32_t)buf[9] << 8) | ((uint32_t)buf[10] << 16) |
                            ((uint32_t)buf[11] << 24);
  (void)flags;

  if (s->valid && emulator_id != s->emulator_id) {
    return; /* another emulator on the same channel */
  }
  s->emulator_id = emulator_id;
  s->uptime_s = uptime_s;
  s->valid = true;

  be_battery_t* bat = NULL;
  if (battery_id >= 1 && battery_id <= BE_MAX_BATTERIES) {
    bat = &s->battery[battery_id - 1];
  }
  if (frame_type == BE_FRAME_SYSTEM) {
    be_keyset_clear(&s->system.seen);
  }
  if (frame_type == BE_FRAME_BATTERY && bat) {
    be_keyset_clear(&bat->seen);
  }

  /* per frame scratch for the chunked / indexed records */
  uint16_t cell_index = 0;
  be_event_t ev;
  memset(&ev, 0, sizeof(ev));
  uint8_t ev_index = 0, ev_total = 0;
  const uint8_t* cell_v = NULL;
  uint16_t cell_v_len = 0;
  const uint8_t* cell_b = NULL;
  uint16_t cell_b_len = 0;

  int i = BE_HEADER_SIZE;
  while (i + 2 <= len) {
    const uint8_t key = buf[i++];
    const uint8_t tag = buf[i++];
    const uint8_t lc = tag & 0x1F;
    uint16_t n;
    if (lc < 30) {
      n = lc;
    } else if (lc == 30) {
      if (i + 1 > len) {
        break;
      }
      n = buf[i++];
    } else {
      if (i + 2 > len) {
        break;
      }
      n = (uint16_t)(buf[i] | (buf[i + 1] << 8));
      i += 2;
    }
    if (i + n > len) {
      break; /* truncated frame */
    }
    const uint8_t* v = &buf[i];
    i += n;

    switch (frame_type) {
      case BE_FRAME_SYSTEM:
        be_keyset_mark(&s->system.seen, key);
        be_apply_system(s, key, v, n);
        break;

      case BE_FRAME_BATTERY:
        if (bat) {
          be_keyset_mark(&bat->seen, key);
          be_apply_battery(bat, key, v, n);
        }
        break;

      case BE_FRAME_CELLS:
        if (!bat) {
          break;
        }
        if (key == BE_KEY_CELL_COUNT) {
          bat->cell_count = (uint16_t)be_u(v, n);
        } else if (key == BE_KEY_CELL_INDEX) {
          cell_index = (uint16_t)be_u(v, n);
        } else if (key == BE_KEY_CELL_VOLTAGES_MV) {
          cell_v = v;
          cell_v_len = n;
        } else if (key == BE_KEY_CELL_BALANCING) {
          cell_b = v;
          cell_b_len = n;
        }
        break;

      case BE_FRAME_EVENT:
        switch (key) {
          case BE_KEY_EVENT_INDEX:
            ev_index = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_TOTAL:
            ev_total = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_ID:
            ev.id = (uint16_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_NAME:
            be_str(ev.name, sizeof(ev.name), v, n);
            break;
          case BE_KEY_EVENT_MESSAGE:
            be_str(ev.message, sizeof(ev.message), v, n);
            break;
          case BE_KEY_EVENT_SEVERITY:
            ev.severity = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_STATE:
            ev.state = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_COUNT:
            ev.occurrences = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_DATA:
            ev.data = (uint8_t)be_u(v, n);
            break;
          case BE_KEY_EVENT_MILLIS:
            ev.millis = be_u(v, n);
            break;
          default:
            break;
        }
        break;

      default:
        break; /* unknown frame type: ignored, but the loop still parsed it */
    }
  }

  /* cells: place this chunk at its own index, never assume it starts at 0 */
  if (frame_type == BE_FRAME_CELLS && bat) {
    const uint16_t count = (uint16_t)(cell_v_len / 2);
    for (uint16_t c = 0; c < count && (cell_index + c) < BE_MAX_CELLS; c++) {
      bat->cell_mV[cell_index + c] = (uint16_t)(cell_v[c * 2] | (cell_v[c * 2 + 1] << 8));
    }
    for (uint16_t c = 0; c < count && (cell_index + c) < BE_MAX_CELLS; c++) {
      const uint16_t byte = (uint16_t)(c / 8);
      bool on = false;
      if (cell_b && byte < cell_b_len) {
        on = (cell_b[byte] >> (c % 8)) & 1u;
      }
      bat->cell_balancing[cell_index + c] = on;
    }
  }

  /* events: a replay batch is a snapshot, so REPLACE the list rather than appending */
  if (frame_type == BE_FRAME_EVENT && ev_total > 0) {
    if (ev_total > BE_EVENT_LOG) {
      ev_total = BE_EVENT_LOG;
    }
    if (ev_index < ev_total) {
      s->event_rx[ev_index] = ev;
      s->event_rx_total = ev_total;
    }
    if (ev_index + 1 >= ev_total) { /* last frame of the batch */
      memcpy(s->events, s->event_rx, sizeof(s->events));
      s->event_count = ev_total;
    }
  }
}

#endif /* BE_ESPNOW_H_ */
```

Contents of **BE_ESPNow_Console.ino** — prints everything the emulator sends:

```C
/*
 * Battery Emulator ESP-NOW v2 telemetry receiver - console example.
 *
 * Prints every value the emulator broadcasts. Drop be_espnow.h next to this sketch.
 */
#include <Arduino.h>
#include <WiFi.h>
#include <esp_now.h>
#include <esp_wifi.h>
#include "be_espnow.h"

// Set to the channel the emulator's Wi-Fi is on, or 0 to join an AP instead. ESP-NOW only
// works between nodes on the same channel; a station that is not associated stays on
// channel 1 and will never hear an emulator joined to a network on another channel.
#define ESPNOW_CHANNEL 1

static be_state_t state;
static uint32_t last_print = 0;

// ---------------- RECEIVE ----------------
// ESP-IDF 5.x callback signature (Arduino-ESP32 3.x). On older cores the first argument
// is a const uint8_t* MAC instead.
void OnDataRecv(const esp_now_recv_info_t* info, const uint8_t* data, int len) {
  be_espnow_receive(&state, data, len);
}

// ---------------- HELPERS ----------------
static const char* txt_system_status(uint8_t v) {
  switch (v) {
    case 0: return "Standby";
    case 1: return "Inactive";
    case 3: return "Active";
    case 4: return "Fault";
    case 5: return "Updating";
    default: return "?";
  }
}
static const char* txt_pause(uint8_t v) {
  static const char* t[] = {"Normal", "Pausing", "Paused", "Resuming"};
  return v < 4 ? t[v] : "?";
}
static const char* txt_level(uint8_t v) {
  static const char* t[] = {"Info", "Debug", "Warning", "Update", "Error"};
  return v < 5 ? t[v] : "?";
}
static const char* txt_emulator(uint8_t v) {
  static const char* t[] = {"OK", "Warning", "Error", "Updating"};
  return v < 4 ? t[v] : "?";
}
static const char* txt_contactors(uint8_t v) {
  static const char* t[] = {"Starting up", "Engaged", "Opened"};
  return v < 3 ? t[v] : "?";
}
static const char* txt_chemistry(uint8_t v) {
  static const char* t[] = {"Autodetect", "NCA", "NMC", "LFP", "ZEBRA"};
  return v < 5 ? t[v] : "?";
}
static const char* txt_bms(uint8_t v) {
  static const char* t[] = {"Disconnected", "Standby", "Active", "Fault"};
  return v < 4 ? t[v] : "?";
}
static const char* txt_balancing(uint8_t v) {
  static const char* t[] = {"Unknown", "Error", "Ready", "Active", "Pending"};
  return v < 5 ? t[v] : "?";
}
static const char* txt_charging(uint8_t v) {
  static const char* t[] = {"Idle", "Charging", "Discharging"};
  return v < 3 ? t[v] : "?";
}
static const char* txt_limiting(uint8_t v) {
  static const char* t[] = {"None", "Inverter", "User setting", "Battery"};
  return v < 4 ? t[v] : "?";
}
static const char* txt_evstate(uint8_t v) {
  static const char* t[] = {"Pending", "Inactive", "Active", "Latched"};
  return v < 4 ? t[v] : "?";
}

// ---------------- RENDERERS ----------------
static void print_system() {
  const be_system_t* y = &state.system;
  Serial.println("======== EMULATOR ========");
  Serial.printf("Emulator id          = %04X\n", state.emulator_id);
  Serial.printf("Uptime               = %u s\n", state.uptime_s);
  Serial.printf("Firmware             = %s\n", y->fw_version);
  Serial.printf("Hostname             = %s\n", y->hostname);
  Serial.printf("Source MAC           = %02X:%02X:%02X:%02X:%02X:%02X\n", y->source_mac[0], y->source_mac[1],
                y->source_mac[2], y->source_mac[3], y->source_mac[4], y->source_mac[5]);
  Serial.printf("System status        = %s\n", txt_system_status(y->system_status));
  Serial.printf("Pause status         = %s\n", txt_pause(y->pause_status));
  Serial.printf("Emulator status      = %s (highest event: %s)\n", txt_emulator(y->emulator_status),
                txt_level(y->event_level));
  Serial.printf("Contactors           = %s\n", txt_contactors(y->contactors));
  Serial.printf("DC bus live          = %s\n", y->dc_bus_live ? "yes" : "no");
  Serial.printf("Equipment stop       = %s\n", y->equipment_stop ? "ACTIVE" : "no");
  Serial.printf("Inverter alive       = %u\n", y->inverter_alive);
  Serial.printf("Batteries            = %u\n", y->battery_count);
  Serial.printf("Free heap            = %u B\n", y->cpu_free_heap);
  if (be_has(&y->seen, BE_KEY_CPU_TEMP_C)) {
    Serial.printf("CPU temperature      = %.1f C\n", y->cpu_temp_C);
  }
  if (be_has(&y->seen, BE_KEY_IP_ADDRESS)) {
    Serial.printf("Wi-Fi                = %s, %u.%u.%u.%u, %d dBm\n", y->ssid, y->ip[0], y->ip[1], y->ip[2], y->ip[3],
                  y->wifi_rssi_dBm);
  } else {
    Serial.println("Wi-Fi                = not associated");
  }
  Serial.printf("Access point         = %s\n", y->ap_active ? "up" : "down");
}

static void print_battery(uint8_t n) {
  const be_battery_t* b = &state.battery[n];
  if (!be_has(&b->seen, BE_KEY_NUMBER_OF_CELLS)) {
    return;  // never heard from this one
  }
  Serial.printf("======== BATTERY %u ========\n", n + 1);
  Serial.printf("Link                 = %s, CAN alive %u, CAN errors %u\n", b->detected ? "detected" : "MISSING",
                b->can_alive, b->can_error_counter);
  Serial.printf("BMS status           = %s\n", txt_bms(b->real_bms_status));
  Serial.printf("Chemistry            = %s, %u cells\n", txt_chemistry(b->chemistry), b->number_of_cells);
  Serial.printf("Design pack voltage  = %u.%u .. %u.%u V\n", b->min_design_voltage_dV / 10,
                b->min_design_voltage_dV % 10, b->max_design_voltage_dV / 10, b->max_design_voltage_dV % 10);
  Serial.printf("Design cell voltage  = %u .. %u mV, max deviation %u mV\n", b->min_cell_design_mV,
                b->max_cell_design_mV, b->max_cell_deviation_mV);
  if (be_has(&b->seen, BE_KEY_TOTAL_CAPACITY_WH)) {
    Serial.printf("Capacity             = %u Wh (reported %u Wh)\n", b->total_capacity_Wh, b->reported_capacity_Wh);
  }
  if (!be_has(&b->seen, BE_KEY_SOC_PPTT)) {
    Serial.println("(no measurements yet)");
    return;
  }
  Serial.printf("SOC                  = %u.%02u %% real, %u.%02u %% reported\n", b->real_soc_pptt / 100,
                b->real_soc_pptt % 100, b->soc_pptt / 100, b->soc_pptt % 100);
  Serial.printf("SOH                  = %u.%02u %%\n", b->soh_pptt / 100, b->soh_pptt % 100);
  Serial.printf("Pack                 = %u.%u V, %d.%d A\n", b->voltage_dV / 10, b->voltage_dV % 10,
                b->current_dA / 10, abs(b->current_dA % 10));
  Serial.printf("Active power         = %d W (%s, limited by %s)\n", b->active_power_W, txt_charging(b->charging_state),
                txt_limiting(b->limiting_factor));
  Serial.printf("Remaining            = %u Wh (reported %u Wh)\n", b->remaining_capacity_Wh, b->reported_remaining_Wh);
  Serial.printf("Charge limit         = %u W / %u.%u A\n", b->max_charge_power_W, b->max_charge_current_dA / 10,
                b->max_charge_current_dA % 10);
  Serial.printf("Discharge limit      = %u W / %u.%u A\n", b->max_discharge_power_W, b->max_discharge_current_dA / 10,
                b->max_discharge_current_dA % 10);
  Serial.printf("User override        = charge %u W, discharge %u W\n", b->override_charge_W, b->override_discharge_W);
  if (be_has(&b->seen, BE_KEY_CELL_MAX_MV)) {
    Serial.printf("Cell voltage         = %u .. %u mV (delta %u mV)\n", b->cell_min_mV, b->cell_max_mV,
                  (uint16_t)(b->cell_max_mV - b->cell_min_mV));
  }
  Serial.printf("Temperature          = %d.%d .. %d.%d C\n", b->temperature_min_dC / 10,
                abs(b->temperature_min_dC % 10), b->temperature_max_dC / 10, abs(b->temperature_max_dC % 10));
  if (be_has(&b->seen, BE_KEY_TOTAL_CHARGED_WH)) {
    Serial.printf("Lifetime             = %d Wh charged, %d Wh discharged\n", b->total_charged_Wh,
                  b->total_discharged_Wh);
  }
  if (be_has(&b->seen, BE_KEY_INSULATION_KOHM)) {
    Serial.printf("Insulation           = %u kOhm\n", b->insulation_kOhm);
  }
  Serial.printf("Balancing            = %s, %u cell(s) shunting\n", txt_balancing(b->balancing_status),
                b->balancing_active_cells);
  if (be_has(&b->seen, BE_KEY_DCDC_VOLTAGE_MV)) {
    Serial.printf("DC/DC (Tesla)        = %u mV, %d.%d A\n", b->dcdc_voltage_mV, b->dcdc_current_dA / 10,
                  abs(b->dcdc_current_dA % 10));
  }
  if (be_has(&b->seen, BE_KEY_AUTOCAL_TAPER)) {
    Serial.printf("Autocal (BYD Atto 3) = taper %s, dwell %u s, cooldown %s, drift %.2f %%\n",
                  b->autocal_taper ? "on" : "off", b->autocal_dwell_s, b->autocal_cooldown_ready ? "ready" : "not ready",
                  b->autocal_soc_drift);
  }
  if (b->cell_count > 0) {
    Serial.printf("Cells (%u):\n", b->cell_count);
    for (uint16_t c = 0; c < b->cell_count && c < BE_MAX_CELLS; c++) {
      Serial.printf("  %3u:%4u%s", c + 1, b->cell_mV[c], b->cell_balancing[c] ? "*" : " ");
      if ((c % 8) == 7) {
        Serial.println();
      }
    }
    Serial.println();
  }
}

static void print_events() {
  if (state.event_count == 0) {
    return;
  }
  Serial.println("======== EVENTS ========");
  for (uint8_t e = 0; e < state.event_count; e++) {
    const be_event_t* v = &state.events[e];
    Serial.printf("[%s/%s] %s (#%u, data %u, %llu ms): %s\n", txt_level(v->severity), txt_evstate(v->state), v->name,
                  v->occurrences, v->data, (unsigned long long)v->millis, v->message);
  }
}

// ---------------- SETUP ----------------
void setup() {
  Serial.begin(115200);
  Serial.println("Battery Emulator ESP-NOW v2 receiver");

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  esp_wifi_set_channel(ESPNOW_CHANNEL, WIFI_SECOND_CHAN_NONE);
  Serial.printf("Own MAC: %s\n", WiFi.macAddress().c_str());

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  esp_now_register_recv_cb(OnDataRecv);
}

// ---------------- LOOP ----------------
void loop() {
  if (millis() - last_print < 5000) {
    return;
  }
  last_print = millis();
  if (!state.valid) {
    Serial.println("waiting for an emulator...");
    return;
  }
  print_system();
  for (uint8_t n = 0; n < BE_MAX_BATTERIES; n++) {
    print_battery(n);
  }
  print_events();
  Serial.println("========================");
}
```

Example of output:

```
Battery Emulator ESP-NOW v2 receiver
Own MAC: 24:6F:28:AA:BB:CC
======== EMULATOR ========
Emulator id          = A1B2
Uptime               = 48213 s
Firmware             = 11.2.dev
Hostname             = battery-emulator-a1b2
Source MAC           = 24:6F:28:12:A1:B2
System status        = Active
Pause status         = Normal
Emulator status      = OK (highest event: Info)
Contactors           = Engaged
DC bus live          = yes
Equipment stop       = no
Inverter alive       = 120
Batteries            = 1
Free heap            = 157320 B
CPU temperature      = 52.3 C
Wi-Fi                = HomeNet, 192.168.1.42, -63 dBm
Access point         = down
======== BATTERY 1 ========
Link                 = detected, CAN alive 60, CAN errors 0
BMS status           = Active
Chemistry            = NMC, 96 cells
Design pack voltage  = 250.0 .. 403.2 V
Design cell voltage  = 2700 .. 4200 mV, max deviation 500 mV
Capacity             = 30000 Wh (reported 27000 Wh)
SOC                  = 52.10 % real, 50.00 % reported
SOH                  = 89.12 %
Pack                 = 370.1 V, -15.2 A
Active power         = -5625 W (Discharging, limited by Inverter)
Remaining            = 15630 Wh (reported 13500 Wh)
Charge limit         = 5000 W / 13.5 A
Discharge limit      = 6000 W / 16.2 A
User override        = charge 0 W, discharge 0 W
Cell voltage         = 3854 .. 3901 mV (delta 47 mV)
Temperature          = 18.4 .. 22.1 C
Balancing            = Active, 12 cell(s) shunting
Cells (96):
    1:3872    2:3874    3:3871    4:3877    5:3872    6:3874*   7:3873    8:3870
    9:3876   10:3875   11:3877*  12:3875   13:3876   14:3875   15:3874   16:3875
  ...
======== EVENTS ========
[Info/Active] EVENT_BATTERY_CHEMISTRY (#1, data 2, 4103 ms): Battery chemistry detected
[Info/Inactive] EVENT_CAN_RX_FAILURE (#3, data 0, 118440 ms): No CAN communication detected for 60s
========================
```

## Migrating from v1

| v1 | v2 |
| --- | --- |
| 4 fixed struct types (`BAT_INFO`, `BAT_STATUS`, `BAT_BALANCE`, `BAT_CELL_STATUS`) copied with `memcpy` | 4 TLV frame types (`SYSTEM`, `BATTERY`, `CELLS`, `EVENT`), parsed key by key |
| every field breaks on insert/reorder/resize | unknown keys are skipped by length |
| cell voltages quantized to 20 mV (`uint8_t`) | raw mV (`uint16_t`), unquantized |
| battery 1 only in practice, 250 byte cap | all three batteries, chunked to any frame size |
| no emulator state, no events | full system state, Wi-Fi details, and the last 10 events |
| absent field indistinguishable from zero | absent field is simply not emitted |

A v1 receiver reading a v2 frame sees `'B'`, `'E'`, `2` where it expected `emulator_id` and `esp_message_type`, so it will not accidentally decode anything — but it will not work either. The decoder above replaces it wholesale.
