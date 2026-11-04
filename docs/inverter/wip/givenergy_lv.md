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
| 7 | RS485 A+ |
| 8 | RS485 B− |

Count the pins with the clip away from you and the contacts up, 1 to 8 from left to right. The cable has no ground core. Connect pins 7 and 8 to Battery-Emulator's RS485 A and B. Leave the board's 120 ohm termination off, because the bus is already terminated.

The bus runs at 9600 baud, 8N1.

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
