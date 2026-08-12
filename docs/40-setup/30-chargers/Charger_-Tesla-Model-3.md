This is not a finished (nor working) charger, but a work in progress.

If you have the full Tesla model 3 battery (with penthouse), then you have a charger built in.

If you got a whole (crashed) Tesla just for the battery, you can scavenge a few extra parts from it (otherwise you will have to buy them) to get a charge port (in my case, a CCS charge port) along with the cables to connect them to the HV battery and the charge port ECU, and the Charge Port ECU to the Penthouse.

> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

# Parts Required
Remove the lining material from the trunk so you can access the "CP ECU" (Charge Port Electronic Control Unit) plus the Charge Port itself, and the wiring harness in this area. The CP ECU has three electrical connectors and a 10mm bolt holding it in.  Remove the connectors and unbolt.  One of the connectors goes to the charge port flap, keep it and the flap.  One of the connectors appears to be bundled into the wiring harness, but actually it is self contained (it only goes between the CP ECU and the CP) - so unwrap the tape around the harness so you can keep this cable.  The last connector does disappear into the wiring harness, you will need the connector and some of the wire coming out of it so you can bond new (longer) wires to it.

The charge port itself is accessed by removing three 10mm bolts, and a 10mm bolt for the manual "pull to release" charge port lever.  The Charge Port needs to have the bigger low-voltage connector removed, so you can remove the high voltage (orange) cable bundle that goes to the penthouse.  Remove the entire HV cable going to the penthouse - which will require removing the rear seats and miscellaneous trim to follow it all the way to the penthouse.  Keep this HV cable.

Remove and keep the CP flap.  Possibly (if you are up for it) cut the sheet metal around the Charge Port area to make a housing. mostly I am interested in this as my HV battery (and charge port) are outdoors, so a water-resistant enclosure for the Charge Port is required.

Keep all the coolant hoses you can from the HV battery, and maybe the radiator and pump and fan and coolant??  I suspect cooling will be required if you are using the AC charger to full (11kW single phase) capacity.

Keep the 16 volt auxiliary battery - you can use it with all the rest of the Tesla parts, but will require a DC-DC converter to connect it to the Lilygo (I used a cheap 12-24v DC in, 5v DC out converter).

# cabling

connector X096 (on the CP ECU) needs to have the following connections.  The connector is an AMP 1452349-1.

| X096 pin | goes to | what |
| -------- | --------- | --------------- |
| 5 | 11 on X098 | CP Latch Enable |
| 6 | 10 on X098 | CP Fault |
| 7 | 6 on X098 | CP-CAN L |
| 8 | 7 on X098 | CP-CAN H |
| 9 | 16v minus | ground |
| 10 | 16v plus | battery |

# Cooling

As the PCS (Power Conversion System, in the penthouse) might be handling a lot of kW (up to 11kW) it might need cooling.  Ports 3 and 9 (in the imageof the penthouse below) connect to PCS, and we might need to connect a cooling system to these ports - a pump, a radiator, maybe a fan; all powered from the Tesla 16v battery via a relay or switch (triggering mechanism yet to be decided).

# Specs
* Maximum power: 11000w
* Input AC Voltage: 240V single or three phase
* Device is water-cooled using glycol mix.

# Photos

Charge Port flap, with cable that goes to CP ECU.  This is useful for weather resistance.
![Charge Port flap](../../images/charger-tesla-model-3-01.jpg)
Charge Port ECU.  Requires three cables to be connected
![Charge Port ECU](../../images/charger-tesla-model-3-02.jpg)
Cable that goes from Charge Port to the CP ECU.  This is the bit you need to unwrap from the left rear wiring harness.
![Charge Port cable](../../images/charger-tesla-model-3-03.jpg)
Charge Port.  Mine (Australian) is a CCS style.
![Charge Port](../../images/charger-tesla-model-3-04.jpg)
My battery, mounted outside the shed.  Note the Charge port HV cable hanging down the right hand side.
![My battery install](../../images/charger-tesla-model-3-05.jpg)
Penthouse diagram, note coolant pipes 3 and 9 connected to PCS 4.
![tesla-model-3-battery-pack-3](../../images/charger-tesla-model-3-06.jpg)

# Integration
Not done yet.

There is a separate CAN bus (CP-CAN) between the Charge Port and the X098 connector on the penthouse.  I assume that we do not need to connect into this CAN bus, and that (if required) command and control will go through the existing Vehicle CAN connection.  If connecting to the CP-CAN is required, in at least my case (due to physical layout) I will need to cut out the 60 ohm resistor on one end of that bus (the CP ECU is the physically easiest and safest to access).

# TODO: get it working

Charging the battery with a solar inverter battery connection and / or using the charge port is possible and does work. You can use solar inverter battery connection and charge port at the same time. Note that normally charging will prevent the motor from spinning, but this might be via CAN bus messages, rather than HV connection shutdown.

How do I open the charge port flap ?

What triggers the cooling system (pump and maybe fan) for the PCS?