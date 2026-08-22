---
title: "CHAdeMO vehicles"
---

!!! warning "WARNING"
    The entire Battery-Emulator project focuses on re-using EV batteries for stationary storage. The following support page for CHAdeMO connection to the in-vehicle battery is only to be used for emergencies, where the grid is down and you need backup power. It is not intended for daily usage, the following info is ONLY for emergency situations!

!!! warning "CAUTION"
    🔥 The CHAdeMO connection requires a genuine CHAdeMO cable. This is to prevent electrical shock to the person plugging in the vehicle. Using 3d-printed parts where you are close to 500VDC is potentially lethal 💀 Do not use anything other than a genuine connector! Genuine connectors known to work will be listed in the wiring and parts detail below.

Be mindful that there is inherent risk to the rest of the vehicle and that you assume responsibility for that risk. Do not attempt on a vehicle you do not own. Be aware that some Nissan Leaf vehicles have experienced contactor welding when using other V2X equipment like Setec inverters; it is a possibility here even despite our best efforts to avoid such issues.

## Compatible CHAdeMO vehicles
Generally: CHAdeMO vehicles v1.0 and forward are OK for V2X. 

| Make and Model   | Compatible | Tested | Note |
| -------- | ------- | -------  | ------- |
| Nissan LEAF 2011-2012 | No | No | These use CHAdeMO v0.9 which is **not** compatible with V2X. However, testing shows that V2X is possible if the reported current back to the car is faked.  |
| Nissan LEAF 2013-2017 | Yes | Testing | These use CHAdeMO v1.0-1.1 V2X, albeit with some unique idiosyncrasies |
| Nissan LEAF 2018-2024 | Yes | Testing | These use CHAdeMO v1.2+ |
| Mitsubishi i-MiEV | Maybe | No | |

## Notes on software implementation
Dala 2025: I have updated the Wiki. There are some things we need to change with the Chademo integration:

- Remove Contactor_control. The vehicle will do precharge when starting.
- This will free up some GPIO on the board
- Add the GPIO logic for d1, d2, and charging sequence signal
- This previous integrations handled these externally. We should automate this by adding it to Battery-Emulator
- Implement a start/stop button. This is required for easy use.

## Required major components

 - CHAdeMO plug,
 - Isabellenhütte IVT shunt (IVT-Modular or IVT-S),
 - 3 x DC contactors (Precharge, Positive, Negative),
 - Precharge resistor,
 - 2 x DC fuses,
 - GPIO connections, logic level converter...

## Connection diagram
!!! warning "CAUTION"
    Use only OEM CHAdeMO cables. Do not compromise your safety by using a 3d-printed connector. Your life depends on it.

The 12V supply used needs to be able to handle 2A continuous load to engage the Chademo contactors in the vehicle.

* Connect pin 8 (CAN-H) to CAN_H on the board
* Connect pin 9 (CAN-L) to CAN_L on the board
* Connect pin 5 (HV-) to inverter -
* Connect pin 6 (HV+) to inverter +
* Connect pin 1 (Protective conductor) to Protection Ground and Ground (for 12V supply)
* Connect pin 7 (Connector proximity detection) to Ground (for 12V supply)
* Connect Start/Stop switch to the GPIO pin CHADEMO_PIN_7 on the board (not connect to CHAdeMO connector)
* Pin 2/10/4 should follow activation/deactivation sequence for CHAdeMO

![image](../images/chademo-vehicle-01.png)

### Activation sequence (pre-charge in inverter)

* Start is pressed, if the plug is connected, relay d1 is activated
* With d1 activated, the EV starts sending messages on can
* EV will send "vehicle charging enable" in can, and indicate the same with signal "k"
* BE detects the above and sends "vehicle connector lock" (mechanical lock not implemented at the moment) in can to the EV
* BE activates d2, which will lead to the EV closing its contactors
* BE measures the "high voltage", and activates its own contactor(s) towards the inverter
* BE sends "charger stop control"=0 and "station status"=1 in can

### Deactivation sequence, stop from BE

* Stop is pressed
* BE signals "charger stop control" in can
* BE waits until current is low, then signals "station status" as disabled in can
* BE deactivates its own contactor(s) towards the inverter
* BE waits until the car opens its contactors, detecting this by measuring the voltage, and then disables d2
* BE waits until the "high voltage" is low
* BE sends "vehicle connector lock" as deactivated (mechanical lock not implemented at the moment) in can to the EV
* BE waits a few seconds and then disables d1

### Deactivation sequence, stop from EV

* EV signals that session should stop, by using "vehicle charging enable" in can, and with signal "k"
* When BE detects the signals, it signals "charger stop control" in can
* See "Deactivation sequence, stop from BE", step 3 and forward

## Current sensor
Even though the vehicle will contain a measuring circuit that checks how much current is going in/out of the battery, this information is unfortunately not available on the Chademo-CAN bus. Most solar inverters require the actual current/power to be sent on the communication bus towards the inverter, so to solve this issue we need to add a current sensor.

This sensor gets attached to the Chademo high voltage wiring (either + or -), and connected via CAN to the Battery-Emulator. You can use the same CAN channel as the Chademo CAN, or use an isolated CAN bus for this sensor.

Compatible sensors:

- Isabellenhütte IVT shunt (IVT-Modular or IVT-S) [Can be purchased for instance here](https://www.evcreate.com/shop/charging/ivt-current-sensor/)

While the current sensor is not mandatory for all inverter protocols, it increases safety to have one connected.

## Lessons learnt Leaf ZE0/Gen24

Here follows some information that was gathered during an integration of a ZE0, a Gen24 and a battery emulator in an RPi.

### Setup

* Nissan Leaf ZE0
* Fronius Gen24-6kW
* RPi with canhat + rs485, running battery emulator in python
* USB-relays
* Contactor
* Batrium BMS
* Current sensor (INA260) for connector lock
* A few resistors, optocoupler etc

### CHAdeMO
In the protocol for 0.9, the charger sends values for voltage and current to the EV. If the EV detects a deviation, it will signal this back to the charger using fault bits.
Testing shows that at least for currents up to ~16A (Gen24 6kW), the ZE0 doesn't use own measurements for deviation checks, but trusts the values that it receives from the charger.
So, all in can, if the charger says it can do max 22A, and the ZE0 requests 20A, the charger can send 10A and the ZE0 will accept that. Even though the actual current is 0A. An example where the ZE0 does throw a fault back is when 19A is requested and 1A is reported back.

### Inverter slow start
When a charge session starts, the EV expects that the power can be ramped up quickly. Most inverters are slow starters, so if the reported output current back to the car is taken directly from the measured one, the EV will detect a current deviation and signal a fault. By faking the reported current, the fault can be avoided. It should be noted that this puts one of safety mechanisms out of play.

### SoC deduction
Normally SoC can be deduced from can messages, by dividing "charging_rate" with "constant_of_charging_rate_indication". On the ZE0 in the tests, this deduced SoC is about 10% higher than the SoC reported on EV-CAN (LeafSpy etc). So, in this case, if charging to 80% (real SoC) was expected, the charger had to stop when it got 90% as deduced SoC. 

### Connector lock
During initial testing, a 3d-printed connector was used, without any lock. In can, there is signalling from the charger that tells the EV if the connector is locked or not. At this stage, it had to be faked as locked to enable charge/discharge.
Later, with a "stock connector", the lock was present, and could be integrated. On this connector two cables facilitated both lock and sensing that the car was connected. A relay controlled the lock (12V ~0.3A), and an I2C current/voltage sensor (INA260) was used to detect if the EV was connected, in both locked and unlocked states.
 
### ZE0 charging only
If a more controlled behavior is wanted, the charger should output a current that is close to the requested. This implies that the inverter power has to be controlled from the charger. In the RPi integration, such a controller was in place. But due to the inverter being slow at startup, at least for the first minutes the reported current has to be faked.

### ZE0 V2X
As long as the reported (charging) current is faked, tests show that it's possible to do both charging and discharging. However, no long term testing has been performed yet.

## Sources used
- [Lars Rengersen, Chademo fast charging](https://www.evcreate.com/chademo-fast-charging-in-diy/)
