---
title: "GivEnergy LV"
---

!!! warning "Work in progress"
    This inverter is not yet supported by Battery-Emulator. Its protocol is in an open pull request, not in a release, so it isn't in the Settings yet. This page collects what is known so far, so it may be incomplete. Can you help? See [data needed for a new inverter integration](../../setup/contributing/data_needed_for_new_inverter_integration.md).

GivEnergy's low-voltage (48 V) hybrid inverters talk to their battery over RS485. The battery's BMS answers the inverter's Modbus polls. With this protocol, Battery-Emulator takes the BMS's place, so a third-party LV battery can run on a GivEnergy inverter.

## Compatible inverters

| Inverter | Firmware | State |
|---|---|---|
| GivEnergy Gen 3 hybrid | 316 | tested with a Fogstar 32 kWh battery over Growatt LV CAN |
| GivEnergy Gen 3 hybrid | DSP 319, ARM 319 | untested |
| Other GivEnergy LV inverters | | untested |

Please add your inverter and firmware if you try it.

## Which protocol to use

Use the option called "GivEnergy LV battery via RS485" under the "Inverter Protocol" setting. Battery-Emulator drives only one RS485 port, so the battery has to use a CAN protocol, e.g. Growatt LV over CAN.

## Wiring

The inverter's BMS cable ends in an RJ45 plug at the battery. Only two of its cores are used:

| RJ45 pin | Signal |
|---|---|
| 6 | RS485 A+ |
| 7 | RS485 B− |

Count the pins with the clip away from you and the contacts up, 1 to 8 from left to right. The cable has no ground core. Connect pin 6 to Battery-Emulator's RS485 A and pin 7 to its B. Pins 6 and 7 aren't one of the cable's twisted pairs, but at 9600 baud over a few metres that doesn't matter.

The bus runs at 9600 baud, 8N1. At that speed over a few metres, the RS485 link doesn't need termination, so leave the board's RS485 120 ohm termination off. Turn the CAN termination on, because Battery-Emulator is one end of the CAN bus to the battery. On the Waveshare ESP32-S3-RS485-CAN, the H1 (CAN) and H2 (RS485) headers inside the case set these. Pins 1 and 2 bridged turn the 120 ohm on, and pins 2 and 3 turn it off.

## Settings

Battery-Emulator sends the inverter the lower of the battery's own limits and its settings:

- "Max charge current" and "Max discharge current" cap the limits sent in holding registers 26 and 27, which the inverter obeys. Battery-Emulator's default is 30 A for both. A Gen 3 also caps the charge at 60 A and the discharge at 75 A itself.
- With "Manual charge voltage limits" on, Battery-Emulator reports the battery full when the pack reaches the target charge voltage, and empty when it falls to the target discharge voltage. Each stays set until the pack voltage moves 2 V back. Set both values before you turn it on. The defaults of 450 V and 300 V are for high-voltage batteries, and with them a 48 V pack always reads as empty. For a 16-cell LFP pack, 56.8 V (3.55 V a cell) and 48.0 V suit.

You don't need either of the two charge-shaping options:

- The protocol always tapers the charge limit by the highest cell voltage, as a GivEnergy battery does. The limit falls from full at 3.45 V to 3 A at 3.55 V. It holds 3 A until the highest cell falls below 3.40 V, and charging stops at 3.60 V. The settings don't change this.
- "Charge power tapering based on SOC" adds a second taper, by state of charge, from the start percentage down to the float power at 100%. If you turn it on, the lower of the two tapers applies.
- "Ramp up charge limits gradually" raises a limit over about 10 seconds instead of at once. A limit still drops at once.

## What Battery-Emulator sends

- It answers as battery 1. Slots 2 to 5 answer as empty, as a single real battery does.
- It reports BMS firmware 3022, the current release. Above 3010 the inverter takes its charge and discharge limits from holding registers 26 and 27.
- The charge limit tapers as the highest cell nears full, down to 3 A, and holds there until the cells come off the top. A real GivEnergy battery does the same.
- It raises the "full" and "empty" alarm bits when the battery stops charge or discharge.
- It replies about 75 ms after each request. A real battery replies after 72 to 96 ms, and the inverter isn't ready for a reply sooner than about 30 ms.

## Battery calibration

During a battery calibration the inverter ignores the battery's current limits. It discharges until the battery reports "empty" and then charges until it reports "full". Nothing on the inverter times a calibration out. Battery-Emulator watches for the inverter charging or discharging beyond the limits it sent. If that goes on for a minute, it reports the end of the calibration. If the inverter still doesn't obey, Battery-Emulator stops answering, and the inverter then reports the battery as lost. Two events show this. The warning says the inverter "charged or discharged beyond the battery's limits", and Battery-Emulator ends the calibration by reporting empty, then full. The error says the inverter "keeps ignoring the battery's limits", and Battery-Emulator stops the link. To recover, set HR29 (battery calibration) to 0 on the inverter, then restart Battery-Emulator.

## Known limitations

- The "full" and "empty" alarm bits are raised for any stop, temperature included. A real battery uses separate alarm bits for temperature and over-current.
- Writes from the inverter are logged but not acted on, including the battery shutdown request.
- The heating interface that BMS firmware 3021 and later offer isn't emulated. The heating status always reads as off.

## More information

- [open-giv/bms-analysis](https://github.com/open-giv/bms-analysis): the protocol, register maps and wire captures.
- [abedegno/forgiv](https://github.com/abedegno/forgiv): byte-exact reconstructions of the GivEnergy BMS firmware (3020 and 3022) and the Gen 3 inverter firmware, which this protocol was checked against.
