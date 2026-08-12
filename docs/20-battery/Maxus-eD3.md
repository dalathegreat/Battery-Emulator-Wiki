> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Battery general info
Maxus eDeliver 3.
There are different battery models:
- 35kWh / 52.5kWh NCM by UABC "United Auto Battery System Co.,Ltd" (model year 2020, 2021)
- 50,2 kWh LFP by CATL "Contemporary Amperex Technology Co., Limited" (model year 2022+)

<img width="1128" height="756" alt="image" src="../images/maxus-ed3-01.png" />

<img width="1128" height="756" alt="image" src="../images/maxus-ed3-02.png" />


## Battery overview

<img width="1333" height="697" alt="image" src="../images/maxus-ed3-03.png" />

Left to right,  Low voltage connector, service disconnect switch, high voltage connector

## Low voltage wiring

Apart from the HV plug, the BMS has two plugs "A" and "B", A seems to be responsible for charging, B for everything else.
Service manual wiring attached, (PT CAN = PowerTrain CAN):

<img width="447" height="367" alt="image" src="../images/maxus-ed3-04.png" />

Other BMS connections
<img width="1542" height="645" alt="image" src="../images/maxus-ed3-05.png" />

The battery has an interlock on Connector B that needs to be shorted
<img width="583" height="518" alt="image" src="../images/maxus-ed3-06.png" />

### How do I connect the battery to the Battery-Emulator?
TODO
- Connector B: Pin 3 to Pin 2 to satisfy interlock detection

## High voltage wiring
Cable for heater?

<img width="974" height="372" alt="image" src="../images/maxus-ev80-04.png" />

