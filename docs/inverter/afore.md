---
title: "Afore"
---

## Compatible Afore Inverters

- AF17K-THA 230V ✅ 

Depending on software version, you might need to do an inverter firmware update to get the BYD CAN option.

## Communication wiring

The Afore inverter works via CAN. A board with a single CAN channel can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor needs to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../setup/can_related/can_wiring_practices_and_troubleshooting.md)

--8<-- "snippets/grounding_termination.md"

## Which protocol to use

For this inverter type, use the option called **BYD HVS/HVM over CAN** or **Afore battery over CAN** under the **Inverter Protocol** setting.

![image](../images/afore-01.png)

!!! info "Note on CAN ID with Nissan LEAF"
    If you intend on using **Afore battery over CAN** protocol with a 2018+ Nissan LEAF battery, the battery needs to be on a separate CAN bus. The LEAF is using the same CAN IDs as Afore does, so if you try to run them both on the same bus the IDs will collide and values get interpreted wrong.

