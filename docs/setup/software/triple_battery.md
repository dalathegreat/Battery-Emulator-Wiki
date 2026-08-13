---
title: "Triple Battery"
---

## Hardware requirement
Triple-Battery, much like Double-Battery, requires a dedicated CAN channel for each battery.

At the moment the following 3-CAN boards are supported:
- [LilyGo T-2CAN with MCP2518FD add-on](../../hardware/lilygo_t_2can.md)
  - Connect Battery1 to CAN-A
  - Connect Battery2 to CAN-B
  - Connect Battery3 to MCP2518FD
  - Connect Inverter to CAN-A (Shared with battery1)

Coming soon hardware:
- 3LB
- BECom

## Supported integrations
The following batteries have support for Triple operation

- Nissan LEAF/eNV200 24/30/40/62kWh ✅

## GPIO controlled contactors
For batteries that require externally controlled contactors, you can automate this by enabling:

- Battery1 - Contactor control via GPIO: ✅
- Battery2 - Double-Battery Contactor control via GPIO: ✅
- Battery3 - Triple-Battery Contactor control via GPIO: ✅

![image](../../images/triple-battery-01.png){ width="580" height="155" }

This will start with connecting battery1, then once voltages match, battery2 and battery3 joins the DC link when voltages are close enough to first battery

See the HAL pin defitions for your hardware, to see which pin actuates the extra contactor set
