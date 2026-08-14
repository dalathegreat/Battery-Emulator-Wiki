---
title: "Stellantis Pro One"
---

### Supported Stellantis Pro One / MCA batteries

110kWh - 90S - min ~270V max ~380V 

The following vehicles are supported

- E-Ducato 110kWh
- ProMaster 110kWh
- Proace Max 110kWh
- Movano 110Kwh
- Jumper 110Kwh
- Boxer 110Kwh

## Connectors

## HV connector
The battery needs to see capacitance on the HV lines in order to engage contactors. Two 470uF capacitors in parallel is confirmed working.

HV connector (175 A max). This is the easiest one to source and use, while the others are much harder to find. (Has HVIL that needs to be seated!)

![image](../images/stellantis-pro-one-01.png){ width="532" height="504" }

[aliexpress](https://nl.aliexpress.com/item/1005003639011124.html?spm=a2g0o.order_list.order_list_main.18.252f79d2fTtchH&gatewayAdapt=glo2nld)

Another HV connector, rated for up to 600 A, can also be used if you can find one. (Has HVIL that needs to be seated!)

![image](../images/stellantis-pro-one-02.png){ width="642" height="568" }

The HV connector on the right side (DC fast charging) cannot be used with the Battery Emulator. (Has HVIL that needs to be seated!)

![image](../images/stellantis-pro-one-03.png){ width="648" height="469" }

## Low voltage connector

![image](../images/stellantis-pro-one-04.png){ width="691" height="1019" }

[aliexpress](https://nl.aliexpress.com/item/1005005787269820.html?spm=a2g0o.order_list.order_list_main.12.252f79d2fTtchH&gatewayAdapt=glo2nld)

### Wiring pinout

- Pin 4 is GND
- Pin 12 is 12v
- Pin 14 is 12v
- Pin 15 is CAN H
- Pin 16 is CAN L
- Pin 22 is 12v
- Pin 24 and 25 interlock together

## Software configuration
To use this battery, select the "Stellantis Pro One 110kWh (E-Ducato/ProMaster/Proace)" battery option.

