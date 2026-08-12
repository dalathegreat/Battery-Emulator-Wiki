> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

### WIP :construction: 
This page contains info on how to re-use the Kia Niro Hybrid batteries (Also applies to Hyundai Kona Hybrid & Kia Xceed)

## Software configuration
For this battery type, use the option called "Kia/Hyundai Hybrid" under the "Battery Protocol" setting

![image](../images/battery-kia-niro-hybrid-06.png){ width="588" height="72" }

## Specifications
There are two variants of the hybrid battery, HEV and PHEV. Currently only HEV batteries have been tested, but PHEV might also work.
* 1.56kWh, HEV, 64 Cellss, 168-235VDC ( Nominal 240V ) , weight 33kg

* 8.9kWh, PHEV, 96 Cells, 360v nominal. The PHEV is split into two packs, both 4.45kWh 180V.


## Part numbers for batteries
Here is a list of Kia / Hyundai part numbers. The Number G is used for Kia Niro HEV. Checkboxes are added to batteries confirmed working by users.

- 37501 G5000, 37501 G2000 is Kia Niro HEV 1.56kWh ✅


## Pictures

Kia Niro 1.6 GDi Hybrid Accu Data (2016)
Accutype : Lithium-ion
Accu voltage : 240 V
Accu capaciteit : 1.56 kWh

![image](../images/battery-kia-niro-hybrid-01.png)

## Wiring diagram HEV ( confirmed for 1.56 Kwh version )

On the 32-pin BMS connector we have the following pin out.

![afbeelding](../images/battery-kia-niro-hybrid-02.png)
![afbeelding](../images/battery-kia-niro-hybrid-03.png)





The battery can be interfaced to the 32-pin BMS connector, via the external white BF11 connector.


![afbeelding](../images/battery-kia-niro-hybrid-04.png)



Wires connected to a HEV battery:

![image](../images/battery-kia-niro-hybrid-05.png)


Battery emulator software ( 13-3-2025 ) is able to read voltage, current etc. but we did not yet found normal way to close relais.

i removed relais module from battery and use it directly connected to inverter battery "input".
Also BMS will run into a stall after maybe 30 seconds a current is flowing. ( voltage reading will still work )
We build a simple rule into the battery code to stop charging when voltage is above 245v for now as workarround.
overall some manual handling is needed at this point. 

need for CANlogs to complete the full potential...
  

##  PHEV
The PHEV battery consists of 2 battery packs. A main pack and a sub pack. Both packs are 180V 4.45kWh. Both packs have separate BMS.
The main pack has the relay module onboard. 
The sub pack does not have a relay module onboard. The HV terminals are LIVE AT ALL TIMES unless you remove the safety plug. 

The wiring for the sub pack is built into the main pack, allowing it to plug directly in.

Some example battery packs are 

Main pack - 37503 -CR710
Sub pack - 37504-CR620