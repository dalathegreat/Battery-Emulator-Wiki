---
title: "Triple Battery"
---

## Hardware requirement

Triple-Battery, much like [Double Battery](battery_2x.md), requires a dedicated CAN channel for each battery.

![image](../../images/battery-3x-01.png)

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

Only these integrations offer the "Triple battery" option in the Settings page. The ones with a checkmark have been confirmed working well.

- [CMFA platform (Dacia Spring, Renault K-ZE)](../../battery/dacia_spring_renault_k_ze.md)
- [Nissan LEAF / e-NV200 24/30/40/62kWh](../../battery/nissan_leaf_e_nv200.md) ✅
- [Relion LV](../../battery/relion_lv.md)
- [Stellantis ECMP](../../battery/stellantis_ecmp_citroen_ds_opel_peugeot.md)
- [Fake battery for testing purposes](../../battery/fake_battery.md) (no hardware needed, useful for trying out a triple setup)

All of these are also compatible with [Double Battery](battery_2x.md). 

## GPIO controlled contactors

Connect the high voltage lines like in this diagram. Remember to place fuses both between the Inverter and packs, and the interconnect between the packs.

![image](../../images/be_battery_3x.png)

After the main battery is started, the system will automatically close the interconnect contactors for the second battery, if it's within 1.5V of the main battery. After that next step is to connect the third battery with the same logic.

To control the second and the third battery, you need to install an extra contactor in series with them. They don't use precharge, thus you can switch both positive and negative at the same time.

Check out the pinout table for each board, to see which pin is defined to actuate the extra contactor.

- Battery1 - Contactor control via GPIO: ✅
- Battery2 - 2ⁿᵈ battery contactor control via GPIO: ✅
- Battery3 - 3ʳᵈ battery contactor control via GPIO: ✅

![image](../../images/battery-3x-02.png)

This will start with connecting battery 1, then once voltages match, battery 2 and battery 3 join the DC link when their voltages are close enough to the first battery.

Check out the pinout table for each board, to see which pin is defined to actuate the extra contactor set.
