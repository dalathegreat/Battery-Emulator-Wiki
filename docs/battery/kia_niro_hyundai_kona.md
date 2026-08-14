---
title: "Kia e-Niro/Hyundai Kona 64 kWh"
---

# Kia e-Niro 64 kWh / Hyundai Kona Electric 64 kWh

## A word of caution about battery fires 🔥
!!! warning "CAUTION"
    The batteries manufactured by LG Chem were recalled due to fire risk. If you are using a battery from a vehicle that did not get the recall, there is a higher risk to re-use these 64kWh batteries. The recall started in 2021, so if you are using a battery from a vehicle that was crashed before 2021, there is a high probability you have an pre-recall battery. **You have been warned!**

What are the affected vehicles? The subject vehicles include:

• Approximately 4,694 model year 2019-2020 Hyundai Kona Electric vehicles produced from August 28, 2018 through March 2, 2020. 

• Approximately 2 model year 2020 Hyundai Ioniq Electric vehicles produced from November 8, 2019 through November 11, 2019.
   
This was done under program Recall 200 - [nhtsa](https://static.nhtsa.gov/odi/rcl/2021/RCMN-21V127-9103.pdf)

So can it be that the battery donor car is from 2020 or 2021 but has received the new battery, good to check then the battery label production date.

## Specifications

* 64kWh, 98s, 352v nominal, 180Ah (Approx size 147cm w x 197cm l x 33cm) ~450kg
   * Note: 64kWh, 96S 358V, 68kWh net ( **37501-AO050** ) 2022+ uses CAN-FD! See part numbers for more info
* 39kWh, 90s, 324v nominal, 120Ah (Approx size 147cm w x 197cm l x 33cm) ~350kg

## Part numbers for batteries

Here is a list of Kia / Hyundai stickers. The Number K is used for Kona, and Number Q is used for Niro. ✅ means that someone has succesfully used the pack with the Battery-Emulator.

- 37501 AO050 is Hyundai Kona / Kia e-niro 64kWh ✅ This battery uses **CAN-FD**, Use `Kia 64kWh **FD** Battery` option in software!
![image](../images/kia-niro-hyundai-kona-64-kwh-16.png)
- 37501 GI050 is Hyundai Ioniq 5 72kWh (For this battery see [EGMP](hyundai_e_gmp_platform_58_2_77_4_kwh.md))
- 37501 CV050 is Kia EV6 78kWh (For this battery see [EGMP](hyundai_e_gmp_platform_58_2_77_4_kwh.md))
- 37510 E4050 is [Kia Soul 27kWh](kia_soul.md)

All Ioniq 28kWh packs use the following options

![image](../images/kia-niro-hyundai-kona-64-kwh-17.png)

- 37501 G7200 is Hyundai Ioniq 28kWh
- 37501 G7250 is Hyundai Ioniq 28kWh

All the following options use

![image](../images/kia-niro-hyundai-kona-64-kwh-18.png)

- 37501 DD150 is Hyundai Kona 64kWh ✅ 
- 37501 DD151 is Hyundai Kona 64kWh ✅ 
- 37501 DD250 is Hyundai Kona 40kWh 
- 37501 K4003 is Hyundai Kona 64kWh 
- 37501 K4050 is Hyundai Kona 64kWh? (reports itself as 40kWh) ✅ 
- 37501 K4050AS is Hyundai Kona 64kWh
- 37501 K4054 is Hyundai Kona 64kWh ✅ (does not require 5V supply) 
- 375A0 K4403 is Hyundai Kona 40kWh ✅
- 37501 K4454 is Hyundai Kona 40kWh ✅ 
- 37501 G7650 is Hyundai Ioniq 40kWh
- 37501 Q4000 is Kia Niro 64kWh ✅ 
- 37501 Q4002 64kWh ✅ 
- 37501 Q4052 is Kia eSoul 64kWh ✅ 
- 37501 Q4050 is Kia Niro 64kWh ✅ 
- 37501 Q4053 is Kia eSoul/Niro 64kWh ✅ 
- 37501 Q4151 is Kia Niro 64kWh ✅ 
- 37501 Q4452 is Kia Niro 64kWh

Remark;
It is possible the BMS in the battery needs a 12v powercycle for 10 ~ 20 sec , after that or at the same time boot the Lilly and contractors are closed and HIGH VOLTAGE !! is active on the battery pins.

This also applies when a emergency knob/button is installed in the interlock lus. when lus is interupted the whole battery systems needs a 12v powercycle to be active again.

## Part numbers
Incase your battery is missing some wires/disconnect switches, here are the OEM part numbers and purchase links. Do note that it might be cheaper to source from your local scrapyard!

|  Product |  Purchase Link |
| :--------: | :---------: |
| Service disconnect switch E437586000 |  [Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2332490.m570.l1313&_nkw=E437586000&_sacat=0)   |
| HV cable, 91662-K4500 CAN-FD, K4000 or K4100 (see below) |  x  |
| HV connector, Yura 110WP 2F, 18790 11883 |  KIA dealer, 11€ (Only has interlock, no HV pins)  |
| Low voltage connector KET MG656922-5 (requires [C025](https://m.alibaba.com/x/AxdkCn?ck=pdp) and [C060](https://m.alibaba.com/x/AxdkCS?ck=pdp) pins) |  [Alibaba](https://m.alibaba.com/x/AxdkBM?ck=pdp)  |

![image](../images/kia-niro-hyundai-kona-64-kwh-01.png)

(Optional for contactor control inside battery, by adding additional pins to unused positions in battery side low voltage connector (MG646089): 2pcs KET ST741378-3 | 2pcs DJ7019-6.3-21 | 4pcs KET ST741376-3 | 2pcs KET MG651026)

## Wiring info

⚠️ The CAN communication has no error checking. This means it is prone to corruption if it sits close to a high voltage line. Use shielded twisted pair cables for CAN-H and CAN-L , and connect the shield to protective earth in one end of the circuit. 

Attached below are pictures of the BMS pinouts. Connect the pins to the Battery-Emulator hardware and 12V supply like this:

* Pin 1/2 to 12V
* Pin 10 to CAN-H on the board (connect resistor 120 Ohm across 10 CAN - H and 11 CAN - L)
* Pin 11 to CAN-L on the board
* Pin 12 to 12V (Ignition)
* Pin 3 and 14 connect together (interlock loop)
* Pin 33 to 12V GND
* Place 12k resistor between Pin9  and Pin31
* Place 12k resistor between Pin8  and Pin30
* Place 12k resistor between Pin27 and Pin28

![bild](../images/kia-niro-hyundai-kona-64-kwh-02.png)

Pinout as viewed from the outside of the pack (note; photo/drawing is upside down in regards to the battery pack!)

![Kona LV Connector](../images/kia-niro-hyundai-kona-64-kwh-03.png)

Note: PIN side (pack) layout. Not female connector side.

![pinout 2023-11-30 222912](../images/kia-niro-hyundai-kona-64-kwh-04.jpg)

![bild](../images/kia-niro-hyundai-kona-64-kwh-05.png)

![batt-bms-connector](../images/kia-niro-hyundai-kona-64-kwh-06.jpg)

![bms-conn-wiring](../images/kia-niro-hyundai-kona-64-kwh-07.jpg)

![Schematic](../images/kia-niro-hyundai-kona-64-kwh-08.png)

## HighVoltage Wiring

Overview of battery, cooling ports, low voltage connector, HVDC connectors

![image](../images/kia-niro-hyundai-kona-64-kwh-19.png)

see picture for positive ( red ) and negative ( black ).

![HV-pos-neg](../images/kia-niro-hyundai-kona-64-kwh-09.jpg)

![Hv cable](../images/kia-niro-hyundai-kona-64-kwh-10.png)

[Battery specs.pdf](https://github.com/dalathegreat/Battery-Emulator/files/15015806/Battery.specs.pdf)

#### Notes on type of HV cable
39kwh (2022) was with metal silver HV socket (looks like early 39/64 packs), 64kwh pack was 2020 with orange plastic HV socket. And these HV sockets looks same but they are mechanically different. For easiest way, try to get the HV cable from the same vehicle that you are getting the battery from!

Silver one needs HV cable p/n 91662K4000 (Picture below)
Orange one needs HV cable p/n 91662K4100

![image](../images/kia-niro-hyundai-kona-64-kwh-20.png)

The two cables side by side 

![image](../images/kia-niro-hyundai-kona-64-kwh-21.png)

## HVIL
The battery packs has interlock monitoring on all high voltage connections. To get the contactors to engage, the battery needs to see that all plugs have been seated. If you dont have the original plugs, these are the HVIL connectors that need to be connected together to make the battery think the connectors are seated:

Low voltage side: Pin 3 and 14 must be connected on data plug.

These two pins on the high voltage plug:

![image](../images/kia-niro-hyundai-kona-64-kwh-11.png)

Two pins on the heater plug must be joined:

![image](../images/kia-niro-hyundai-kona-64-kwh-12.png)

If the service disconnect switch is missing, these two small pins must be shorted together.

![image](../images/kia-niro-hyundai-kona-64-kwh-13.png)

Plus, the HV side must be connected together (diagram missing for running without service disconnect plug). Due to this, it is recommended to get the OEM service disconnect plug before continuing.

## STL files for unused battery connections

There are STL files available to 3D print covers for the unused battery connectors.

## Special notes on 37501-AO050 battery
There is a 2022+ Hyundai Kona or Kia e-niro battery that uses CAN-FD, that comes with a AO050 part number sticker. It is CATL made, it consist in 24 modules(2.835 kwh) x 4 cells(3.7v), configured 96s1p(358v in total) 64.8kwh(68.4 in total)

This battery has the part number 37501-AO050, and this battery requires a CAN-FD hardware interface. Easiest to get a [Stark CMR](../hardware/stark_cmr.md), but you can also add a [CANFD addon interface](../setup/can_related/can_fd_add_on_mcp2518fd.md). To use this battery, enable the `Kia 64kWh FD battery` option in the software.

!!! info "IMPORTANT"
    The contactor control for these FD batteries are not working, they open after a few seconds. To get around this, you need to force the contactors closed with 12V/GND. This can be automated with GPIO Controlled contactors.

![image](../images/kia-niro-hyundai-kona-64-kwh-14.png)

### Manual contactor control on the 37501-AO050 FD battery
To setup manual contactor control, open the battery lid, and locate the contactor assembly box.

![image](../images/kia-niro-hyundai-kona-64-kwh-22.png)

You can connect your own contactor control wiring directly to the white plug.

![image](../images/kia-niro-hyundai-kona-64-kwh-23.png)

To get the contactor control wires out of the battery (and into the Battery-Emulator GPIO), you can use the unused pins on the low voltage connector:

![image](../images/kia-niro-hyundai-kona-64-kwh-24.png)

For controlling the contactors, it is enough to take out 3 wires outside the battery (precharge+, contPos+, contNeg+), the negative side is common with the BMS power supply.

- white for contactor control positive
- brown/orange for contactor control negative
- yellow/orange for pre-charging

Connect these three wires to the GPIO via relay/SSR.

## Troubleshooting 

If you see Battery Voltage being reported as 6553.5V, it means that the battery is having internal issues.

- Check if all cells are visible on the Cellmonitor page
   - If all cells are not visible, you have a blown fuse on one of the balancing lines
   - Another user reported corrosion on one of the balance lead plugs
   - Whatever the case, opening the battery and investigating is required if cellvoltages are missing

## Notes on waterdamage :droplet: 

!!! warning "WARNING"
    These batteries are not waterproof. Water can easily enter thru the service disconnect switch. Store and operate in a dry area!

Attached pictures from packs that did not detect all cells. Root cause was water damage, causing fuses and PCB traces to blow up. Placing batteries vertically can make water sloosh around and short out. You have been warned!

![image](../images/kia-niro-hyundai-kona-64-kwh-15.png)

## Explanation of More Battery Info page

More battery info:
Cells: 98S						= Total amount of cells of battery build
12V voltage: 11.9					= State of 12V battery input, actual value (minimum 12V!)
Waterleakage: 160					= Don’t know
Temperature, water inlet: 17				= Temperature on inlet side of water cooling.
Temperature, power relay: 26				= Temperature of power relays of battery.
Batterymanagement mode: 1				= Don’t know.
BMS ignition: 9						= Don’t know.
Battery relay: 135					= Don’t know.

## Internal schematics of the Battery ( 37501-AO050  version ) 
[technical-schematics-kia-64kwh-SG2-spanish.pdf](https://github.com/user-attachments/files/26716116/technical-schematics-kia-64kwh-SG2-spanish.pdf)

## Credits
Here are the sources used
[Kona.64.kWh.contactors.log.files.zip](https://github.com/dalathegreat/BYD-Battery-Emulator-For-Gen24/files/13322609/Kona.64.kWh.contactors.log.files.zip)

* [google](https://docs.google.com/spreadsheets/d/1dbOT9I-Aj7lU7yCiJDpXERjYRVOL_M1Tm2QFgmyYt4Y/htmlview?fbclid=IwAR3HZMGhDfGsOdJrbMfRUDkS8c-25cSwnZcwzIewC10mJ1gy6hf719BUBNM#)
* [google](https://docs.google.com/spreadsheets/d/1-9jZafV9eZeBUnPQo7qQHbX2-_4qZfWfRVpidoF1owA/edit#gid=660740603)
Massive thanks to Lubos, Tyrel Haveman, goev1390, Peter Lord, Projectgus, JejuSoul, Heikki Jaakkola
[technical-schematics-kia-64kwh-SG2-spanish.pdf](https://github.com/user-attachments/files/26715929/technical-schematics-kia-64kwh-SG2-spanish.pdf)
