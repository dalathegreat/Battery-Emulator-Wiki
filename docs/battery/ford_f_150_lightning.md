---
title: "Ford F‐150 Lightning"
---

## Compatible batteries
The model years 2022-2025 came with the following batteries.

- 107kWh gross (98kWh net usable) 
- 143kWh gross (131kWh net usable)

There are stickers on the battery that informs gross capacity

![image](../images/ford-f-150-lightning-01.png){ width="1018" height="303" }

### Physical Dimensions

| Parameter | Value |
|----------|-------|
| Pack Size (L × W × H) | 38"wide 105"long  12.5" high  back half(52") portion  6.5" front half  portion with the exception  of where the bms is. That part is 8" high. |
| Weight | <!-- e.g. 540 kg --> |

> **Battery holder frame design:** <!-- Link to frame design if available -->

## Software configuration
For this battery type, use the option called "xyz" under the "Battery Protocol" section.

## Part numbers 
Part numbers for connectors/cables, along with purchase links to ebay/aliexpress.

| Component | Part Number | Purchase Link |
|-----------|-------------|---------------|
| <!-- e.g. HV Connector --> | <!-- e.g. TE 123456 --> | [eBay](#) / [AliExpress](#) |

## Wiring, Low voltage connector

![image](../images/ford-f-150-lightning-02.png)

A replacement LV connector can be purchased from AliExpress. 
[aliexpress](https://www.aliexpress.com/item/1005008121256506.html)

Detailed LV connector C144 pin description

![image](../images/ford-f-150-lightning-03.png){ width="450" }

![image](../images/ford-f-150-lightning-04.png){ width="450" }

[![MachE-2 SMA inverter setup](../images/ford-f-150-lightning-05.png){ width="900" }](../images/ford-f-150-lightning-05.png)

For communication only:

- Pin 1 to 12V constant (BMS+)
- Pin 6 to 12V constant
- Pin 26 to GND for 12V
- Pin 15 or 21 to CAN-L on Battery-Emulator
- Pin 16 or 22 to CAN-H on Battery-Emulator

For communication AND contactors:

- Pin 1 to 12V constant (BMS+)
- Pin 5 to 12V constant
- Pin 6 to 12V constant
- Pin 8 to 12V constant (Closing battery contractors)
- Pin 25 to GND for 12V
- Pin 26 to GND for 12V
- Pin 15 or 21 to CAN-L on Battery-Emulator
- Pin 16 or 22 to CAN-H on Battery-Emulator

Tip: use pin 15 and 16 for CAN Communication. Use pin 21 and 22 to add a 120Ω terminating resistor

Battery uses 1.4 amps to run the 12v 1mm2 cable should be enough.

Note: The battery does NOT contain a terminating resistor, so it is a good idea to add a 120 Ohm resistor between CAN-L and CAN-H on the battery side.

| Parameter | Value |
|----------|-------|
| 12V Consumption — Peak Start | 2.0A |
| 12V Consumption — Continuous | 1.5A |
| CAN type | CAN |
| Contactor Control | CAN-controlled |

## Wiring, High voltage connector

<!-- Add a photo of the HV connector and a wiring diagram below -->

| Parameter | Value |
|----------|-------|
| Interlock Required | Yes |
| Number of Interlocks | <!-- e.g. 2 --> |

The interlocks on these connectors need to be seated:

## Troubleshooting tips

<!-- Document common issues and their solutions -->

## Example picture from completed install

<!-- Add a photo of a finished installation for reference -->