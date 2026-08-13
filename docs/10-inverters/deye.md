---
title: "Deye"
---

## Compatible Deye inverters
* Deye SUN 5-25K-SG01HP3-EU-AM2 ✅ 
* Deye SUN 29.9-50K SG01HP3-EU-BM3 ✅
* Deye SUN 8/10/12/15K-SG01HP2-US-AM2 ✅️ 
* Deye SUn 80K-SG02HP3 ✅️ 

Most likely way more Deye inverters work, since they are all BYD / Pylon compatible!

## Notes on protocol violation :warning: 
This inverter will skip any 0W requests, so incase we overvoltage cells, and request stop charge, **Deye will happily continue charging** This is due to poor programming on Deye side, they simply do not follow the CAN message 0x110 (Discharge current max byte 4-5) & (Charge current max byte 6&7)

Deye only listens to two things when it comes to stopping charge.
- 0%, 100% SOC reached
- Pack voltage limit reached

That is the only time Deye inverters stop charging/discharging. Due to this we recommend reaching out to Deye and demand improved firmware on the Inverter side. It is simply not fully safe to operate a Deye inverter

Be sure to enable the "Deye avoid over/undercharge fix: " option in the meantime
![image](../images/deye-06.png){ width="660" height="210" }

This will force SOC% to either fully charged (100%), fully discharged (0%) incase we need to stop. It looks odd on the inverter side, but it is the only way we can stop Deye inverters at the moment. You have been warned about Deye's lackluster software!

## Notes on dual battery input :battery: :battery: 
Most Deye inverters have two ports for adding batteries. The smaller 25k and lower units have non-isolated ports, which means there are two ports that behind the scenes are merged as one. The larger 30k-50-etc. have totally independent battery ports. This means you can easily connect two batteries, they can even differ in size and type.

When using the larger >30k inverters with two batteries, you will need one BE for each BMS port. This means you will have two totally independent BE systems, and the inverter treats them as separate batteries.

When using the smaller <25k inverters with two batteries, you will need to join them together in parallel using the [Double-Battery support](../40-setup/20-software/double_battery.md). You will need one single BE unit with Double-CAN for this, and the Deye will see 1 single battery (even though you have 2 in parallel!)

## Notes on geo-lock :world_map: 

!!! warning "WARNING"
    Sol-Ark manufacturer has turned on location validation in recent firmwares. This in turn disabled the inverters if they are used in the UK, US, Canada and Pakistan. Be careful with connecting your Deye inverter to the internet!

Picture of remotely disabled unit in the US:

![image](../images/deye-01.png)

## Communication wiring
The Deye inverter works via CAN. The LilyGo board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor needs to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../40-setup/index.md#can-wiring-troubleshooting)

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Which protocol to use
For this inverter type, the recommended option is the "BYD Battery-Box Premium HVS over CAN Bus" m which is found under the "Inverter Protocol" setting. Also be sure to enable the "Deye avoid over/undercharge fix:" checkbox, otherwise the Deye inverter can over/undercharge the battery.

![image](../images/deye-07.png)

!!! warning "WARNING"
    Never use lead-acid battery mode to force a battery to operate. This means there is no communication between the EV battery and inverter, and battery has no way to stop the charge. Users have permanently degraded batteries by operating in this mode!

### Manual charge voltage limits
The Deye inverters can rely on charge voltage instead of only SOC%. Battery charge voltage defaults to the value set in the integration. This is the theoretical max the battery can take. This becomes the charge target for Deye. To make things safer, you can enable "Manual Charge Voltage Limits", and set the max voltage to your liking. Note that this will reduce the capacity you can extract from the battery, and on integrations that rely on getting fully charged in order to balance/calibrate, you will also disrupt it.
. To enable this feature, go to the Settings page on BE, and enable manual voltage control and set charge voltage max and min discharge voltage.

![image](../images/deye-08.png){ width="410" height="202" }

#### Note on Pylon
Not recommended, but it is also possible to use the Pylon HV protocol. For this to work, 30k offset and inverterd byteorder is required. Set manufacturer to "Deye". Most users should go for the BYD protocol instead, since it is simpler to setup.

![image](../images/deye-09.png){ width="795" height="472" }

## Connecting the low voltage wiring

* Use the BMS1 (or BMS2) port on the Deye
    * Pin 4 CAN-H , and Pin 5 CAN-L (See Deye manual for RJ45 pinout)

![bild](../images/deye-02.png)

Set the Deye to Lithium Mode, 01

![bild](../images/deye-03.png)

If you connected everything correctly, you will see data on the display:

![bild](../images/deye-04.png)

## Installation examples
![bild](../images/deye-05.png)

## Special notes on usage with BMW i3

!!! note "NOTE"
    If you intend on using BYD-CAN with the BMW i3, the battery needs to be on a separate CAN bus. The BMW i3 is using the same CAN IDs as BYD do, so if you try to run them both on the same bus the IDs will collide and values get interpreted wrong. There are a few ways to solve this:

* You can [add an isolated MCP2515 CAN channel](../40-setup/40-can-related/can_add_on_mcp2515.md)
* You can [add an isolated MCP2518 CANFD channel, and run it in classic CAN mode](../40-setup/40-can-related/can_fd_add_on_mcp2518fd.md)
* You can use the [Stark CMR](../30-hardware/stark_cmr.md) board
* You can use the lilygo T-2can with 2 native can ports 

## Troubleshooting

- If you see F58 BMS_COMMUNICATION_FAULT, make sure the Max Discharge Speed is not set too high, this will make the Deye fault (For instance having it set to 150.0A will crash it)
- If the inverter appears to be OFF on the LCD, make sure that both power switches on the inverters are ON. One switch which apparently is only for PV panels - the one that you turn 90 degrees AND another one which is a push button that is ONLY for battery side

