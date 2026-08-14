---
title: "Kia Soul"
---

## Work in progress integration :construction: 

Kia Soul EV had two types of batteries:

* E375 cell is a 37.5Ah cell. This is the cell used in the **27 kWh Kia Soul EV from June 2014 to June 2017**. It is NMC622 LMO Free
* E400 cell is a 40.0 Ah cell. This is the cell used in the **30 kWh Kia Soul EV from June 2017 to May 2019**.

Pack consists of 4x10S and 4x14S modules = 96S in total (96S2P configuration)

There is an Android App available which may be used to further experiments: [Soul EV Spy](https://play.google.com/store/apps/details?id=com.evranger.soulspy&hl=pl&pli=1)

### Parts List

Connectors: MG656922-5 KET (pins are included) can be ordered here [alibaba](https://xhxqsm.en.alibaba.com/)

Connector pin: [KET Female Terminal ST731438-3 C060](https://www.alibaba.com/product-detail/KET-ST731438-3-C060-WP-Female_1600912337153.html)

Main connector (out of stock?): [KET Connector MG645649-5](https://www.amazon.com/Connecting-MG645649-5-HR212-10R-8SC-MG642357-5-SDK-9BNS-K13-GS-T/dp/B0DM58ZJMD?th=1)

HV Cable part no. 91876E 4000

![image](../images/kia-soul-27kwh-01.png)

### Wiring diagram

Connect the following pins to 12V, GND and CAN;

| Battery Pin  | Connected to |
| ------------- | ------------- |
| 1 B+  | To 12V feed  |
| 2 CAN-H  | To CAN-H port of Battery-Emulator  |
| 3 Crash | Not used |
| 4 Ainrsa1 | Not used |
| 5 F Speed1 | Not used |
| 6 CAN-L | To CAN-L port of Battery-Emulator |
| 7 GND | To GND of 12V system |
| 8 B2+ | To 12V |
| 9 CAN2-L | To CAN-L port of Battery-Emulator |
| 10 RCTL | Not used |
| 11 Wake up | Not used |
| 12 VF1 | Not used |
| 13 CAN2-H | to CAN-H port of Battery-Emulator |
| 14 GND | To GND of 12V system |
| 15 IGN+ | To 12V |
| 16 Main + RLY2 | To GPIO for automatic contactor control, via SSR relay |
| 17 Main - RLY2 | To GPIO for automatic contactor control, via SSR relay |
| 18 Empty | Not used |
| 19 GND | To GND of 12V system |
| 20 GND | To GND of 12V system |

![image](../images/kia-soul-27kwh-02.png)

### Pictures

![soul2](../images/kia-soul-27kwh-03.jpg)

![image](../images/kia-soul-27kwh-04.png)