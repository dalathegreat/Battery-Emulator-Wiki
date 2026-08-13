---
title: "Afore"
---

## Compatible Afore Inverters
- AF17K-THA 230V :ballot_box_with_check: (Works with "BYD Battery-Box Premium HVS over CAN Bus" or "Afore CAN" option)
   - Depending on software version, you might need to do an inverter firwmare update to get the BYD CAN option

## Communication wiring
The Afore inverter works via CAN. The LilyGo board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor needs to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../40-setup/index.md#can-wiring-troubleshooting)

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Which protocol to use
For this inverter type, use the option called "BYD Battery-Box Premium HVS over CAN Bus" under the "Inverter Protocol" setting

![image](../images/afore-01.png){ width="484" height="68" }

## Note on CAN ID with Nissan LEAF
!!! info "IMPORTANT"
    If you intend on using "Afore CAN" protocol with a 2018+ Nissan LEAF battery, the battery needs to be on a separate CAN bus. The LEAF is using the same CAN IDs as Afore does, so if you try to run them both on the same bus the IDs will collide and values get interpreted wrong

