---
title: "ZCS Azzurro"
---

## Compatible ZCS Azurro inverters
TODO: Add list

## Which protocol to use
For this inverter type, use the option called "Pylontech battery over CAN" under the "Inverter Config" setting. Send group 1 might be needed if inverter throws error.

![image](../images/zcs-azzurro-01.png)

## Communication wiring
The ZCS Azurro inverter works via CAN. The Battery-Emulator board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor might need to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../40-setup/index.md#can-wiring-troubleshooting)

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.