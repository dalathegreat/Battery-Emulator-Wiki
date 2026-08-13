---
title: "Renault Kangoo"
---

## FAQ: Renault Kangoo Battery
Renault Zoe support is still being developed. The Kangoo shares a fair share of CAN data with the Renault Zoe and Renault Fluence

## Variants of the Kangoo
There are 3x batteries available for the Kangoo:
* 22kWh 2011-2016
   * Can be used with the `Renault Kangoo` setting
   * NOTE: Sometimes SOC does not update on these packs, this can be solved by switching to the "Use Estimated SOC" option
* 33kWh 2017-2021
   * Can be used with Zoe Gen1 software setting: `Renault Zoe Gen1 22/40kWh`
* 44kWh 2022+
   * Pinout unknown, NOT SUPPORTED YET since nobody has tested it

![image](../images/renault-kangoo-01.png){ width="393" height="91" }

Physical size;
* Weight 295 kg (22kWh)
* Weight 260 kg (33kWh)
* Dimensions 1214 x 802 x 290mm

**The 33kWh pack doesn't have a negative contactor, the only way to isolate it is to pull the service disconnect.** In the contactor box there's a current sensor, pre-charge resistor, pre-charge relay, main contactor and a 275a 1000V fuse. The main contactor is 150a rated.

44kWh pack example:

![image](../images/renault-kangoo-02.png){ width="622" height="913" }

## Part numbers for Renault Kangoo batteries

|  Product |  Purchase Link |
| :--------: | :---------: |
| Battery communication connector, Yazaki 7282-8854-30 |  [AliExpress](https://de.aliexpress.com/item/4000174903780.html)   |
| High voltage connector 80kW 297A6-5SH1A OR 297A22581R |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A65SH1A&_sacat=0)   |

There are 2 external Low voltage Connectors for the 33kWh battery pack

Grey Yazaki x

| Pin | Internal Wire | Function |
| :--------: | :---------: | :---------: |
| 1 | Black | 12v BMS supply via 10a fuse  |
| 6 | Yellow | Can High |
| 7 | White | 12v Contactor supply via 15a fuse |
| 12 | Blue | Can Low |

Black Yazaki 7283-8854-30

| Pin | Internal Wire | Function |
| :--------: | :---------: | :---------: |
| 1 | Black | Ground  |
| 3 | Green | Main Contactor (ground to close) |
| 5 | Blue | Pre-charge relay (ground to close) |

The 22kWh pack pinout (black connector)

| Pin | Internal Wire | Function |
| :--------: | :---------: | :---------: |
| 1 | Red | fused +12V permanent to BMS  |
| 3,4,5 | Black | electrical earth |
| 6 | White | Can High |
| 7 | Violet | fused +12V to pwer relays|
| 8 | Orange | Power relay 1 - positiv (ground to close) |
| 9 | Green | Power relay 2 - negativ (ground to close) |
| 10 | Brown | Precharge relay (ground to close) |
| 12 | Violet | Can Low |

6 Violet and 12 White are twisted together (CAN bus)
