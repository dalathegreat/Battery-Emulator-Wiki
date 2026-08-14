---
title: "Jaguar I‐PACE"
---

### WIP

This battery is currently being reverse engineered by [@obbardc](https://github.com/obbardc) and [Cory Mac - ØY Electrical](https://www.youtube.com/@corymac) (along with lots of help from [@dalathegreat](https://github.com/dalathegreat) and other community members).

### Current state

The battery has the internal contactor coils forceably controlled by the Battery-Emulator, using the `Contactor control via GPIO` setting. This is because the

We need to verify if the cells are being properly balanced by the iPace BMS with the contactors forcibly engaged.

We made two videos about the reverse engineering:

- [Part 1: Hacking an EV Battery From a £90,000 Car - DIY Vehicle to Grid](https://www.youtube.com/watch?v=C0RxlvLHm3Y)
- [Part 2: Hacking a Scrapped £90,000 EV Battery to get FREE Electricity - DIY Vehicle to Grid - Part 2
](https://www.youtube.com/watch?v=TKGAmPUtpQ0)

#### Reverse engineering threads/links

 - [openinverter](https://openinverter.org/forum/viewtopic.php?t=5124) - Connecting to standalone BECM including pinouts, UDS PIDs, UDS error codes etc. (by @obbardc)
 - [openinverter](https://openinverter.org/forum/viewtopic.php?t=4532) - BMS

 - [Car PIDs spreadsheet (incl. BECM)](https://docs.google.com/spreadsheets/d/1wNMtpPqMAejNeOZGsPCcgau8HODROzceFcUSfk2lVz8/edit?gid=445693275#gid=445693275)

#### TODO

- Engage battery contactors by sending the right CAN messages. See [Issue: Jaguar iPace Battery Contactors do not yet close](https://github.com/dalathegreat/Battery-Emulator/issues/471) for more information.
- Confirm that cells are balanced during operation.
- Poll for all cellvoltages. There does not seem to be a UDS register/CANBUS register for this.
- Different keepalive/other CAN messages for >2021 models.
- LG's pouch cells in I-PACE have a habit of tabs becoming disconnected. This leads to modules becoming 3P rather than 4P. The I-PACE BMS wasn't flagging this in earlier firmware revisions leading to the module becoming overcharged and fires. Determine which models are used.

#### CAN logs from working vehicle

- [here](https://drive.google.com/drive/folders/17RtvvRqCqwPwhIgQzoykOObO1e_TCcdt?usp=drive_link)

#### BECM

- BECM CAN ID is 0x7e4, returns data on 0x7ec.
- Appears to be in UDS format.
- [Spreadsheet containing UDS PIDs and UDS Error codes](https://docs.google.com/spreadsheets/d/1z68Okw8T8qvCoFy3QOkY0JGlpziNfyOmgKuFfwBVRm4/edit?usp=sharing)

### Specifications

### Pictures

### Wiring diagram (low voltage)

- For now see [connector pinout spreadsheet](https://docs.google.com/spreadsheets/d/17EmBsm7eqVYdQGEEauHqlMVK45hghRZNUVGEhLQdNIg/edit?usp=sharing)

### High voltage wiring

- 3x HV connectors with interlocks. TODO: Add diagram.

## Software setup
For this battery type, use the option called "Jaguar I-PACE" under the "Battery Protocol" setting.

![image](../images/jaguar-i-pace-01.png){ width="591" height="73" }

Also remember to enable "Contactor control via GPIO" to control the contactors manually.