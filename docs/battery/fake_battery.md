---
title: "Fake battery (for testing)"
---

### What is this?

The Fake battery is a built-in battery integration that generates plausible battery data entirely inside the emulator, without any real pack, BMS or CAN traffic. In the Settings page it is listed as **Fake battery for testing purposes**.

It is meant for:

- Bringing up a new inverter integration without risking a real pack
- Testing the web UI, cell monitor, MQTT / Home Assistant autodiscovery, ESP-NOW and the display
- Verifying double and triple battery setups on a single board
- Reproducing SOC-, voltage- and balancing-dependent behaviour on demand, by simply typing a pack voltage

!!! danger "CAUTION"
    The Fake battery reports a healthy pack that always allows charge and discharge. If it is selected while real hardware is connected, the inverter will happily push power into or out of whatever is actually on the DC bus. Only use it on a bench setup, or with the HV side disconnected.

### Taking it into use

1. Open the emulator web UI and go to **Settings**.
2. In the **Battery** dropdown, select `Fake battery for testing purposes`.
3. Set **Battery communication interface** to any available interface (e.g. `CAN native`). The Fake battery never transmits and does not need a bus, but an interface must be selected.
4. Optionally tick **Double battery** and/or **Triple battery** (both are supported, see below) and select their interfaces.
5. Press **Save**, then **Reboot**.

After the reboot the status page shows the protocol name `Fake battery for testing purposes`, the emulator raises the normal "battery detected" event, and the system goes to ACTIVE just as with a real pack.

### The only dedicated setting: Fake battery voltage

Once the Fake battery is running, an extra blue box appears on the Settings page:

**Fake battery voltage: `<value>` V** with an **Edit** button.

| Property | Value |
|:---|:---|
| Unit | Volts (decimals accepted, stored with 0.1 V resolution) |
| Useful range | 245.0 – 404.0 V (the design limits of the fake pack) |
| Applied | Immediately, no reboot needed |
| Persisted | No — after a reboot the pack is back at 370.0 V (see the double/triple contactor note below) |
| Affects | Battery 1; batteries 2 and 3 mirror the same voltage |

This single value drives almost everything else the Fake battery reports: SOC, remaining energy, cell voltages and the simulated balancing state.

!!! note "NOTE"
    The box is only rendered for integrations that implement `supports_set_fake_voltage()`, so it is invisible for every real battery.

### How SOC is derived from the voltage

SOC is interpolated linearly between the fake pack's design limits, 245.0 V (0.00 %) and 404.0 V (100.00 %):

```
SOC [%] = (pack voltage - 245.0) / (404.0 - 245.0) * 100
```

Values at or below 245.0 V clamp to 0.00 %, values at or above 404.0 V clamp to 100.00 %.

| Fake voltage | Real SOC | Remaining energy | Note |
|:---:|:---:|:---:|:---|
| 245.0 V | 0.00 % | 0 Wh | Battery empty event, discharge blocked |
| 280.0 V | 22.01 % | 6603 Wh | |
| 320.0 V | 47.16 % | 14148 Wh | |
| 370.0 V | 78.61 % | 23583 Wh | Default after boot |
| 380.2 V | 85.03 % | 25509 Wh | Simulated balancing starts |
| 390.0 V | 91.19 % | 27357 Wh | |
| 404.0 V | 100.00 % | 30000 Wh | Battery full event, charge blocked |

Remaining energy is always `30 kWh × SOC`, so it stays consistent with the SOC shown.

The SOC that the inverter sees is still the **scaled** SOC, so the usual **SOC max/min percentage** settings apply on top of this. With the default 80 % / 20 % scaling, a fake voltage of 370.0 V (78.61 % real) reads as roughly 97.7 % towards the inverter.

### Simulated cell voltages

The pack voltage is divided evenly over 96 cells and a random spread of ±20 mV is applied per cell, re-rolled once per second:

```
cell [mV] = pack voltage [V] * 1000 / 96 + random(-20 .. +20)
```

| Fake voltage | Nominal cell voltage |
|:---:|:---:|
| 245.0 V | 2552 mV |
| 320.0 V | 3333 mV |
| 370.0 V | 3854 mV |
| 404.0 V | 4208 mV |

Because the spread never exceeds 40 mV between highest and lowest cell, the cell deviation event (500 mV default) never fires by itself. The constantly changing values make the cell monitor page, the MQTT cell voltage payloads and the ESP-NOW cell frames behave like a live pack.

### Simulated balancing

Above **85.00 % calculated SOC** (about 380.2 V) the Fake battery starts a simulated balancing session:

- Balancing status is reported as **Active**
- Every cell sitting more than 7 mV above the pack average has its balancing resistor flagged as on
- Since the cell spread is re-randomised every second, the set of balancing cells keeps changing, which is exactly what a display or MQTT consumer sees on a real pack

Below 85.00 % SOC the balancing status is reported as **Ready** and all balancing flags are cleared.

### Fixed values reported

Everything not derived from the voltage is a constant:

| Parameter | Reported value |
|:---|:---|
| State of health | 99.00 % |
| Total capacity | 30 000 Wh (30 kWh) |
| Current | 0.0 A (so active power is always 0 W) |
| Max charge power | 5000 W |
| Max discharge power | 5000 W |
| Min / max temperature | 5.0 °C / 6.0 °C |
| Number of cells | 96 |
| Max / min design voltage | 404.0 V / 245.0 V |
| Max / min cell voltage | 4250 mV / 2500 mV |
| Max cell deviation | 500 mV (datalayer default) |
| Total charged energy | 123 555 Wh |
| Total discharged energy | 123 444 Wh |
| CAN alive | Always alive, faked once per second |

The **Battery capacity** setting on the Settings page has no effect with this integration: the driver rewrites the capacity to 30 kWh every second. The **Max charge/discharge speed (A)**, **Manual charge voltage limits**, **SOC scaling** and remote limit settings do work normally, since they are applied by the common layers after the battery driver has run.

The Fake battery implements none of the optional BMS functions (reset BMS, reset SOC, clear isolation, DTC reading, manual balancing, …), so none of those buttons appear on the battery info pages.

### Double and triple battery

The Fake battery supports both **Double battery** and **Triple battery**. Each extra instance is created on its own configured interface and gets its own datalayer entry, its own cell voltages, its own randomisation and its own balancing state. Batteries 2 and 3 copy the pack voltage of battery 1, so all packs stay at the same voltage and SOC — which is what a healthy parallel installation looks like. Total capacity becomes 60 kWh (double) or 90 kWh (triple).

#### The second and third contactors stay open at the default voltage

!!! warning "CAUTION"
    With external (GPIO) contactor control on a double or triple setup, the contactors of battery 2 and 3 will **not** engage while the fake voltage is left at its default 370.0 V. Change the **Fake battery voltage** to any other value, for example 370.1 V or 380.0 V, and they close normally.

This is not a bug in the parallel logic, it is the parallel voltage-sync safety check protecting itself against uninitialised data. Before it compares the packs, `check_parallel_battery_safety()` aborts if either pack reads 0.0 V **or exactly 370.0 V**, because 3700 dV is the value most integrations leave in the datalayer until the first real measurement arrives. The Fake battery boots at exactly that voltage and mirrors it to packs 2 and 3, so the check keeps bailing out, the "battery allows contactor closing" flag is never raised, and the extra contactors stay open.

Nothing is logged when this happens: the check returns before it can raise `Voltage difference between batteries` (that event only appears when the packs really are more than 1.5 V apart for over 3 seconds), so the symptom looks like a silent refusal to close.

Once the voltage is anything else, the mirrored packs are bit-for-bit identical, the difference is 0.0 V, and both extra contactors are allowed to close as soon as the main precharge sequence reaches COMPLETED.

### Events you can provoke on purpose

Because the pack voltage is a free input, the Fake battery is a convenient way to walk the safety layer through its states:

| Fake voltage | What happens |
|:---:|:---|
| Below 245.0 V | Battery undervoltage event, then cell undervoltage below about 242 V |
| Exactly 245.0 V or lower | SOC 0.00 %, battery empty event, discharge power forced to 0 W |
| 404.0 V | SOC 100.00 %, battery full event, charge power forced to 0 W |
| Above 404.0 V | Battery overvoltage event, followed by cell overvoltage and critical cell overvoltage |
| Around 380 V and up | Balancing goes Active in the UI, MQTT and ESP-NOW |

### Quirks

- **DC bus reported as not live.** The Fake battery declares the DC bus dead at startup. With GPIO contactor control enabled, the flag is corrected as soon as precharge completes. Without contactor control it stays false, and inverters that gate on it — notably BYD-Modbus — report **STANDBY** instead of **ACTIVE** to the inverter. Enable contactor control, or expect standby on the inverter side.
- The fake voltage is not stored in NVM, every reboot returns to 370.0 V — which is also the value that blocks the second and third contactors, so on a double or triple setup the voltage has to be re-entered after every reboot.
- The input validation message on the voltage prompt mentions 0–1000 while the check itself accepts 0–5000.
- Charged/discharged energy counters are frozen constants, they never move.


