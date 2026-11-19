---
title: "Renault Zoe Gen1"
---

# Renault Zoe Gen1
Zoe Generation 1 batteries are fully compatible with the Battery-Emulator.

## Variants of the Zoe
There are 3x batteries available for the Zoe, this page focuses on the Gen1 22/40kWh batteries.

* 22kWh 2012-2019, Gen1
* 40kWh 2016-2019, Gen1
* [52kWh 2019-2024, Gen2](renault_zoe_gen2.md)

## Zoe 41kWh pictures and pinout

![bild](../images/renault-zoe-gen1-01.png)
![ZOE_Gen1_battery_dimensions](../images/renault-zoe-gen1-02.jpg)
![image](../images/renault-zoe-gen1-03.png)

## Testing a battery before purchasing
You can connect the Battery-Emulator to a 12V source (AGM Battery, UPS, AC-DC source, etc.) and read the cell voltages and statistics before purchasing a battery. To do this, you will need **Pin 1 3 4 5 6 7 12** (see the wiring diagram further down)

Example: Zoe battery being tested with a Stark CMR and lead-acid battery before purchase

![image](../images/renault-zoe-gen1-04.png)

## Software configuration
For this battery type, select "Renault Zoe Gen1 22/40kWh" under the "Battery Protocol" setting.

![image](../images/renault-zoe-gen1-11.png){ width="591" height="79" }

You can also enable "Contactor Control via GPIO" to automate contactor opening and closing.

## Safety fuse/switch
**Note the battery fuse**. 
Do not confuse it with the version from the 52kWh battery; using the wrong one could blow fuses or worse. 
Use the OEM fuse, part#: 
- [297C13111R](https://www.ebay.com/sch/i.html?_nkw=297C13111R) for 22kWh.
- [297C12645R](https://www.ebay.com/sch/i.html?_nkw=297C12645R) for 40kWh.

Both 297C13111R and 297C12645R are interchangeable for 22/40 kWh batteries.

![image](../images/renault-zoe-gen1-05.png)
![image](../images/Zoe_fuse_gen1_2.jpg)


Renault ZOE Gen 1 fuse has to have **continuity** between the two external sides (positive line):
![image](../images/renault-zoe-gen1-06.png)
![image](../images/Zoe_fuse_gen1_1.jpg)


Two other fuses are also inside the pack. One fuse is under the contactor cover, and another is at the joint between the two halves of the pack at the end opposite the connectors. If the middle fuse blows, this shows as a cell imbalance, with cell 48 around 0V. Replacing the fuse restores operation.

## Part numbers for Renault Zoe 23/41kWh batteries

|  Product |  Purchase Link |
| :--------: | :---------: |
| Battery communication connector, Yazaki 7282-8854-30 |  [AliExpress](https://s.click.aliexpress.com/e/_c3Tr3Yu5)  OR [Aliexpress wired](https://s.click.aliexpress.com/e/_c4FmGS2t) - You need the **Female** plug|
| High voltage connector 80kW 297A6-5SH1A OR 297A22581R |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A65SH1A&_sacat=0)   |
| Safety switch/fuse | OEM Part no: [297C13111R](https://www.ebay.com/sch/i.html?_nkw=297C13111R) for 22kWh and [297C12645R](https://www.ebay.com/sch/i.html?_nkw=297C12645R)  for 40kWh |
| Relays | [AliExpress DIN](https://s.click.aliexpress.com/e/_c4pTXxG1) - get the "DC control DC CN" version (schematic to be added to this page)|

## Wiring diagrams

!!! info "IMPORTANT"
    This battery has no negative contactor. You control only the precharge and the positive contactor. The control of these are NEGATIVE switched, which is very rare for automotive contactors. This means you supply GND to get the pre/pos-contactor to operate.

Example of contactor control via SSR relays, connected to a LilyGo T-CAN485 board:

![image](../images/renault-zoe-gen1-07.png)

Example of contactor control via SSR relays, connected to a Stark CMR board:

![image](../images/renault-zoe-gen1-08.png)

Alternate version with one power supply and 2 SSR DD NO relays using StarkCMR v2 (this version does not have BMS reset relay/function): 
![Image](../images/renault-zoe-gen1-09.jpeg)

## Notes on balancing :b: 
The Zoe Gen1 batteries appear to start top-balancing at around 93% SOC. Because of this, we recommend fully charging the battery from time to time to allow it to balance the cells.

You can observe cell-mV-delta at high SOC to confirm when balancing is active; unfortunately, the Zoe Gen1 battery does not indicate which specific cells are being balanced, so there is no visualization on the Cellmonitor page.

## Troubleshooting

- If the inverter does not want to use the battery with more than a few watts of power, check your precharge wiring. You might be pulling all the power through the precharge resistor instead of the contactor. A classic mistake is swapping them!
- If the cell number 48 is low, your internal battery fuse most likely has blown. Then you need to open up the battery and replace the fuse.

![image](../images/renault-zoe-gen1-10.png)

