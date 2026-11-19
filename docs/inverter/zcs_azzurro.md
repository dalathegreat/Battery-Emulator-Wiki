---
title: "ZCS Azzurro"
---

## Compatible ZCS Azzurro inverters

TODO: Add list

## Which protocol to use

For this inverter type, use the option called "Pylontech HV over CAN" under the "Inverter Config" setting. Send group 1 might be needed if inverter throws error.

![image](../images/zcs-azzurro-01.png)

## Communication wiring

The ZCS Azzurro inverter works via CAN. The Battery-Emulator board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor might need to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../setup/can_related/can_wiring_practices_and_troubleshooting.md)

--8<-- "snippets/grounding_termination.md"
