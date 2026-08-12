> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Compatible Growatt inverters
The current implementation "Growatt High Voltage protocol via CAN Bus" emulates a "HVC 60050-A1 BMS". This means the following inverters work:
* Growatt SPH 10 10000TL3 BH-UP ✅
* Growatt SPA 4000-10000TL3 BH-UP :question:

We can also emulate a WIT battery when selecting the "Growatt WIT compatible battery via CAN" option. This enables support for the following inverters
* Growatt WIT 50XHU ✅
* Growatt WIT 100HU ✅

### Word of caution, isolated CAN requirement
These inverters does not handle a CAN connected EV battery on the same channel. If the inverter sees standard automotive CAN frames, the inverter will enter a fault state.

This can be solved in 4 different ways:

* You can [add an isolated MCP2515 CAN channel](../40-setup/40-can-related/CAN-add‐on-(MCP2515).md)
* You can [add an isolated MCP2518 CANFD channel, and run it in classic CAN mode](../40-setup/40-can-related/CAN‐FD-add‐on-(MCP2518FD).md)
* You can use the [Stark CMR](../30-hardware/Stark-CMR.md) hardware
* You can use a [CAN filter](../40-setup/40-can-related/CAN-filter-hardware.md) between inverter and the rest of the system 

## Incompatible Growatt inverters
* Growatt MIN TL-XH (This inverter does not have the DC-DC converter between internal DC-bus and battery connectors, also the RS485 protocol is not modbus and Growatt support does not release the internal protocol.)

## Communication wiring
The Growatt HV inverter works via CAN. The LilyGo board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor needs to be removed from the board. Please measure CAN termination if you have issues. This is explained in [CAN-troubleshooting](../40-setup/index.md#can-wiring-troubleshooting)

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Which protocol to use
For this inverter type, use the option called "Growatt High Voltage protocol via CAN Bus" under the "Inverter Protocol" setting

![image](../images/growatt-hv-01.png){ width="491" height="66" }

**If you have the Growatt WIT inverter, instead use the "Growatt WIT compatible battery via CAN" option!**

## Connecting the low voltage wiring
