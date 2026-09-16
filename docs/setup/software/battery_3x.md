---
title: "Triple Battery"
---

## Hardware requirement

Triple-Battery, much like [Double Battery](battery_2x.md), requires a dedicated CAN channel for each battery.

At the moment the following 3-CAN boards are compatible:

- [LilyGo T-2CAN with MCP2518FD add-on](../../hardware/lilygo_t_2can.md)
    - Connect Battery1 to CAN-A
    - Connect Battery2 to CAN-B
    - Connect Battery3 to MCP2518FD
    - Connect Inverter to Modbus, RS485 or CAN-A (shared with battery1)
- [BECom](../../hardware/becom.md)

### How does parallel operation work?

The same principles apply as described at the [Double Battery](battery_2x.md).

## Which batteries are compatible?
The list below is generated from `battery_supports_triple()` in `Software/src/battery/BATTERIES.cpp`. Only these integrations offer the "Triple battery" option in the Settings page. The ones with a checkmark have been confirmed working well.

- [CMFA platform (Dacia Spring, Renault K-ZE)](../../battery/dacia_spring_renault_k_ze.md)
- [Nissan LEAF / e-NV200 24/30/40/62kWh](../../battery/nissan_leaf_e_nv200.md) ✅
- [Relion LV](../../battery/relion_lv.md)
- [Stellantis ECMP](../../battery/stellantis_ecmp_citroen_ds_opel_peugeot.md)
- [Fake battery for testing purposes](../../battery/fake_battery.md) (no hardware needed, useful for trying out a triple setup)

All of these are also compatible with [Double Battery](battery_2x.md). 

## GPIO controlled contactors

For batteries that require externally controlled contactors, you can automate this by enabling:

- Battery1 - Contactor control via GPIO: ✅
- Battery2 - Double-Battery Contactor control via GPIO: ✅
- Battery3 - Triple-Battery Contactor control via GPIO: ✅

![image](../../images/triple-battery-01.png){ width="580" height="155" }

This will start with connecting battery 1, then once voltages match, battery 2 and battery 3 join the DC link when their voltages are close enough to the first battery.

Check out the pinout table for each board, to see which pin is defined to actuate the extra contactor set.
