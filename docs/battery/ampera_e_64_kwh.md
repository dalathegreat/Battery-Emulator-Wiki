---
title: "Ampera‐e 64 kWh"
---

## GM BEV2 platform
The 60-66kWh battery in the GM BEV2 platform can be found in the following vehicles

* Opel Ampera-E (2017-2021)
* Chevrolet Bolt (2016-2023)

2020+ models are 64 KWh, earlier are 57 kWh

## Software configuration
For this battery type, use the option called "Chevrolet Bolt EV/Opel Ampera-E" under the "Battery Protocol" setting

![image](../images/ampera-e-64-kwh-23.png){ width="656" height="156" }

Also remember to configure the allowed charging power, since we do not read this value via CAN.

The battery uses 12V controlled contactors, so use `Contactor Control via GPIO` if you want Battery-Emulator to also control the contactors via GPIO

![image](../images/ampera-e-64-kwh-24.png){ width="514" height="49" }

One user reported using 3x this type of relay with the LilyGo hardware 
https://nl.aliexpress.com/item/1005005622431177.html?spm=a2g0o.order_list.order_list_main.126.d91579d2FEesY4&gatewayAdapt=glo2nld

## Wiring diagrams
Connect the low voltage wiring like this:

X358 connector (black) 

- Pin 1 & 2 should be grounded (if pin 1 has 5V we lock the battery?)
- Pin 3 12v+ positive contactor
- Pin 4 12v+ negative contactor
- Pin 5 12v+ positive contactor for aux connector 
- Pin 7 12v+ precharge
- Pin 8 is coolant temp, pin 9 is ref. to pin 8.
- Pin 10 to ground

X357 connector (gray)
- Pin 1 fused with 10A (+12V)
- Pin 2 we wake up the sensors (+12V)
- Pin 3 & 4 relevant CAN H/L (?)
- Pin 5 & 6 relevant CAN H/L (?)
- Pin 7 & 8 relevant CAN H/L (?)
- Pin 9 is blocking ignition if we feed 5V
- Pin 10 wake up BMS (+12V)
- Pin 11 wake up communication (+12V)
- Pin 12 to ground

**All three CAN's should be connected to BE device.**

The following diagrams will help you to connect to the CAN buses on the Opel/Chevy batteries:

!!! note "NOTE"
    These batteries have multiple CAN buses that needs to be jumpered together to form one large CAN bus
    the resistor on the Lilygo must be removed
Example, development environment with contactor control via GPIO, and all 3x CAN buses connected together as one single bus

![image](../images/ampera-e-64-kwh-01.png)

![AC laden](../images/ampera-e-64-kwh-02.png)
![DC laden](../images/ampera-e-64-kwh-03.png)
![temperatuur regeling accu verwarming ](../images/ampera-e-64-kwh-04.png)

![aansluitingen hoogspannings kabels ](../images/ampera-e-64-kwh-05.png)
![activeren seriele gegevens ](../images/ampera-e-64-kwh-06.png)
![activeren seriele gegevens canbus ](../images/ampera-e-64-kwh-07.png)
![blokkeerlus](../images/ampera-e-64-kwh-08.png)
![bus hoogspanning beheer](../images/ampera-e-64-kwh-09.png)
![canbus in schakelen ](../images/ampera-e-64-kwh-10.png)
![contactors hoogsanning regeling ](../images/ampera-e-64-kwh-11.png)
![contactors hoogspanning regeling](../images/ampera-e-64-kwh-12.png)
![contactors negatief](../images/ampera-e-64-kwh-13.png)
![contactors positief](../images/ampera-e-64-kwh-14.png)
![Hi speed 1](../images/ampera-e-64-kwh-15.png)
![Hi speed 2](../images/ampera-e-64-kwh-16.png)
![voeding en massa HV accu 2 ](../images/ampera-e-64-kwh-17.png)
![voeding en massa HV accu](../images/ampera-e-64-kwh-18.png)
Stekker X 357 OEM 33472-1259 Service Connector 19333239
* X357
![x357](../images/ampera-e-64-kwh-19.png)
![x357 pen pos](../images/ampera-e-64-kwh-20.png)

X358 
![X358](../images/ampera-e-64-kwh-21.png)

![X358 pin pos ](../images/ampera-e-64-kwh-22.png)

 I had connectors but these fits also, one needs to modify by yourself 

 https://nl.aliexpress.com/item/1005008320223516.html?spm=a2g0o.detail.similar_items.1.3023vs3wvs3wW0&utparam-url=scene%3Aimage_search%7Cquery_from%3Adetail_bigimg&algo_pvid=8f883bc9-24d0-4568-842b-10652fe911a8&algo_exp_id=8f883bc9-24d0-4568-842b-10652fe911a8&pdp_ext_f=%7B%22order%22%3A%2216%22%7D&pdp_npi=4%40dis%21EUR%213.12%213.00%21%21%2125.47%2124.53%21%402103892f17530145939331841e26a9%2112000044596715592%21sea%21NL%21828630060%21X

Disconnect switch 24281696 24288304  24291219  or latest part number 24294004

Cotactors must be connected with lilygo via the GPIO pins see:
[Contactor control via GPIO pins](../setup/software/contactor_control_via_gpio_pins.md)

Please note that the precharge contactor is placed in the negative line of battery. To make precharge work the positive contactor must close before precharge contactor. Workaround: Swap Positive and negative control-lines to relays.

