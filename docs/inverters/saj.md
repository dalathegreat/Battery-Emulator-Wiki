---
title: "SAJ"
---

## Types of compatible SAJ inverters
[H2 Hybrid](https://global.saj-electric.com/solarenergy-detail/63)

   - 3~6K-S2 Ver. ✅
   - 5~10K-S3 Ver. ✅
   - 5~10K-T2 Ver. ✅
   - 15~20K-T2 Ver. ✅

SAJ H2-10K-T2 was the first SAJ inverter to be successfully used with Battery-Emulator

SAJ H2-8K-T2 hybrid inverter also used with Battery Emulator:

* Module Firmware : V1.214 (upgraded by SAJ to allow Modbus)
* Display Board : V2.231 (upgraded by SAJ to allow AI mode)
* Control Board : V4.139

## Inverter protocol
The SAJ inverter uses the Pylon CAN protocol (Pylon-SC0500)

## Settings on the Battery Emulator side 
`#define PYLON_CAN`

For >255Ah batteries, the latest version contains a [bugfix](https://github.com/dalathegreat/Battery-Emulator/pull/1192) for the 732x frames to the inverter

Specific settings are not needed regarding geometry of the battery

For a 72-cell battery 280Ah LFP battery, this works for me:

* TOTAL_CELL_AMOUNT = 72;
* MODULES_IN_SERIES = 4;
* CELLS_PER_MODULE = 18;
* VOLTAGE_LEVEL = 230;
* AH_CAPACITY = 280;

This is the can_config part for the inverter:

* .inverter = CAN_ADDON_MCP2515,

The battery shows up in the Elekeeper APP with the following parameters as reported by the Battery Emulator:

* Design Capacity
* Actual Ah Remaining Capacity
* Actual % Remaining Capacity
* (Dis)charge Power
* Temperature
* Number of Modules

When going deeper into the Elekeeper APP (change battery settings) via BT or cloud
* Zero voltage displayed for the 4 modules
* Modules appear as 16 cell instead of declared 18 cell
* The inverter only looks at low and high SOC% disconnect values implement on inverter side, no effect by changing the battery threshold settings on webinterface of BE

WIP on the mapping of the battery modules towards the Pylon modules.

