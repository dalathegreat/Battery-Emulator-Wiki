---
title: "CAN filter hardware"
---

## What is a CAN filter?
Since some inverters need to see only certain CAN messages on the bus, we can achieve this by adding a CAN-filter between the inverter and the rest of the CAN-bus. By doing this you can use a board with a single CAN channel, such as the LilyGo T-CAN485, with an inverter that usually requires a dedicated CAN channel.

![image](../../images/can-filter-hardware-01.png)

## How do I get the hardware?
We utilize the cheaply and readily available CAN filter also used for Nissan LEAF battery upgrades. It is available on Aliexpress. Below are some purchase links, please note that you need the BLUE PCB for this code to work.

|  Hardware |  Purchase link |
| :--------: | :---------: |
| 2-port budget bridge | [AliExpress "MB CAN Filter 18 in 1](https://www.aliexpress.com/item/1005003112723581.html?)   |
| STM32 USB flasher | [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=ST+link+v2&_sacat=0&LH_TitleDesc=0&_odkw=ST+link+v23&_osacat=0)   |

## Where do I get the software?
Software for the CAN filter [can be found here](https://github.com/No-Signal/Can-Filter)

## Flashing the CAN filter

See this video: [youtube](https://www.youtube.com/watch?v=LssrvVYLtp8)

Flash with BridgeFlasher.exe located in software folder. The compiled .srec files are [located in the releases section](https://github.com/dalathegreat/Nissan-LEAF-Battery-Upgrade/releases)  . For ST LINK CLI, point the exe towards the "ST-LINK_CLI.exe" located in the "STM32 ST-LINK Utility" folder that appears after installing it. Incase the BridgeFlasher.exe doesn't run, make sure you have installed [vc++ 2015 x86](https://www.microsoft.com/en-us/download/details.aspx?id=48145) 

This is what the BridgeFlasher.exe should look like. Press Start to flash.
![alt text](../../images/can-filter-hardware-02.jpg)

Connect the ST Link V2 to the J1 ports on the PCB. It can be hard to connect dupont wires here, so I recommend getting needle pins. Pay close attention to the pin labels on the ST Link flasher, they can vary location depending on type.

| ST Link V2 Pin | CAN Filter Pin |
| :--------: | :---------: |
| 7 3.3V | J1 |
| Nothing | J2 |
| 3 GND | J3 |
| 2 SWDIO | J4 |
| 6 SWCLK | J5 |

![alt text](../../images/can-filter-hardware-03.jpg)

## Connecting the CAN Filter

The can filter is placed between the Battery-Emulator hardware and the inverter.

| CAN Filter Pin | Connection |
| :--------: | :---------: |
| CAN-1L | Battery-Emulator CAN_L |
| CAN-1H | Battery-Emulator CAN_H |
| CAN-2L | Inverter CAN L |
| CAN-2H | Inverter CAN H |
| +12V | 12V positive |
| GND | 12V negative |

![CanFilter](../../images/can-filter-hardware-04.png)