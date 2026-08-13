---
title: "Chevrolet Volt Gen1"
---

# Charger Details
## Overview
The Battery-Emulator project has support for the independent battery chargers starting in release 5.0. This feature is optional, intended to facilitate emergency charging from generators, supplemental charging when inverter lacks an onboard charger, or as part of battery commissioning/maintenance. 

This page describes chargers from the Chevy Volt and Opel Ampera between model years 2011 and 2015, referred to as Gen1 (generation 1) chargers. They are occasionally referenced as Lear chargers in resale/parts/surplus, as Lear is manufacturer supplying many OEMs. Physically similar models were also used in Coda vehicles, but notably they run different firmware from Chevy/Ampera models (e.g. different CAN messages). Coda variants may be supported in future revisions.

## Specs
* Maximum power: 3300w
* Output LVDC Voltage output: 13.5V constant (for charging 12v batteries)
* Output HVDC Voltage range: 200-420v DC
* Output current range: 0-11.5A
* Input AC Voltage: 120V, 240V single phase

* Device is water-cooled using glycol mix.
* Weight: 9.3kg/20.5lb
* Dimensions: 330mm * 280mm * 127mm, 13" * 11" * 5"
* Efficiency: 90-92%

## Part Information
This charger is most commonly available as GM part# 22799689 

Equivalents: 22793073, 22799689, 24265980, 24270696

Note: 2015, 2015 Cadillac ELR hybrids used the same charger and may provide results not found if referring solely to Chevy Volt or Ampera Opel.

Related cables: 20972413 and 22889574

### Vehicle Placement
![W](../../images/charger-chevrolet-volt-gen1-01.png)

### Appearance
![s-l1600](../../images/charger-chevrolet-volt-gen1-02.jpg)
![s-l1600](../../images/charger-chevrolet-volt-gen1-03.jpg)
![s-l1600](../../images/charger-chevrolet-volt-gen1-04.jpg)

# Integration
Integration with T-CAN485 is straightforward.

The charger is controlled and monitored solely via CAN. High and Low signals are available via the 12 wire pigtail to the right of the 12V aux charger output. No modification of termination resistor is necessary.

TODO photos, diagram
+12V needs to be connected to pins 1, 6, 7.
12v Bat +, - must be connected to the aux LVDC output.

CAN High is pin 2

CAN Low is pin 3

Many parts have leads clipped, but the charger can be disassembled and wires spliced without a great deal of effort.

The 12 pin IO connector on the charger is a Delphi GT150 part number 15326854. The terminals
are part number 15326268, and the cable seals 15366021. The required mating connector (vehicle side)
is Delphi GT150 part number 15326849 and uses terminals part number 12191818. The cable seals are
also 15366021.

## Charger IO connector

| Vehicle Connector | Pin # | Charger Connector | Inside Charger | Function |
| ----------------- | ----- | ----------------- | -------------- | -------- |
| Blue / Red | A | Purple / white | JA1 pin 1 | Enable |
| Orange | B | Blue / Yellow | JA2 pin 2 | CAN A High |
| Green | C | White | JA2 pin 1 | CAN A Low |
| NA | D | Blue / Green | JA3 pin 2 | CAN A High |
| NA | E | White | JA3 pin 1 | CAN A Low |
| Blue / Red | F | Purple / Yellow | JA1 pin 2 | M/S1 |
| Black | G | Purple / Yellow | JA1 pin 3 | M/S2 |
| NA | H | Blue | JA2 pin 4 | CAN B High |
| NA | J | White | JA2 pin 3 | CAN B Low |
| NA | K | Blue | JA3 pin 4 | CAN B High |
| NA | L | White | JA3 pin 3 | CAN B Low |
| NA | M | N/C |

The 2 pin Low Voltage power connector on the charger is a Yazaki part number 7282-5596-10. The terminals are part number 7114-4142-02, and the cable seals 7159-3083. The required mating connector (vehicle side) is Yazaki part number 7283-5596-10 and uses terminals part number 7116-4142-02. The cable seals are also 7158-3083.

The High Voltage DC connector on the charger is a Delphi HV280 part number 13757523. There are two mating connectors (vehicle side), the power connector and the interlock connector. The  interlock is not necessary for the charger to function, it is there to interlock with the vehicle HV battery system. The pins are simply shorted together inside the charger. The function is such that if the interlock is disconnected, then the HV battery will shut off HV to the entire vehicle. In order to remove the HV connector, you must first remove the interlock connector as they are mechanically interlocked. The mating power connector is part number 13861585 and the mating interlock connector is a Delphi OCS 1.2 part number 13738744.