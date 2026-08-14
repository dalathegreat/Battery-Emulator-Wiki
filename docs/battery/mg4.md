---
title: "MG4"
---

** UNDER CONSTRUCTION **

## Specifications

| Year |  Model | Battery capacity | Supported? | Rated Voltage | Voltage Range |
| :--------: | :---------: | :---------: | :----------: | :----------: |  :----------: |
| 2024- | MG4 EH32 | 49kWh LFP       |   ✅⚠️ Testing ongoing | 315V | 250-365V 
| 2022- | MG4 EH32 | 51kWh LFP       |   ✅⚠️ Testing ongoing | 327V | 260-379.6V   |
| 2022- | MG4 EH32 | 64kWh NMC       |   ✅⚠️ Testing ongoing| 380V | 291.2-452.4V |
| 2022- | MG4 EH32 | 77kWh NMC       |   ✅⚠️ Testing ongoing| 380V | 302.4-469.8V |
| 2026- | MG4 EH?? | 64kWh LFP       |    TBC                 | 316V | ???          |

## Current status

There are a couple of current challenges:

- Most packs (~75% of ones tested) will close contactors when requested, and report the state-of-charge over the PT EXT CAN, but others do not. It is not clear why not, perhaps they are crash-locked and need resetting, the 49kWh pack is reported to have closed contactors once 12V was applied to PIN 4 on the LV connector.

- It is currently necessary to use the PT EXT (non-FD) bus for closing the contactors, but the PT (FD) bus for reading extended information (including temperatures, SoH, cell min, max and voltages). 

The buses can be linked together and it does work, but getting the diagnostic information is inconsistent.  

The better option is to have the PT EXT on the T2-CAN's 2515 interface with the PT bus connected to the 2518 add on board, the latest versions of the MG4 code support this on the shunt dropdown, select "Battery second interface" and select the interface PT EXT is connected to, you can ignore all the other settings.

The BMS SoC drifts over time, we're still work on how to get it to reset once max cell reaches the appropriate level, in the meantime the MG4 code now has the option to "Use estimated SOC" which will snap to 100% and coulomb count backwards from there, the BE SoC is persistent across reboots, but not power cycles.

- It is not known whether the packs are balancing, but the LFP packs seem to be 3-5mv accept at the extremes.

Both locked packs (using external contactor control and coulomb-counting) and non-locked packs (using BMS contactor control and SoC) are currently being tested, we've successfully replaced a locked BMU with an unlocked one from a catastrophically damaged pack, so this is worth keeping in mind as an option.

## Software configuration

For this battery type, use the option called "MG4 battery" under the "Battery config" setting.

![be](../images/mg4-01.jpg)

![image](../images/mg4-08.png){ width="782" height="146" }

## Connectors

The MG4 battery has an HV connector (Orange), and a 12 pin Low Voltage signal connector (Black/Red). There are also two coolant ports that can be used for thermal management, left is inlet, right is outlet (optional)

## Low voltage connector

![ESS_connector_pinout](../images/mg4-02.jpg)

## Low voltage socket

![39d3687d-7d61-4841-a597-aa59d4bf7a2a](../images/mg4-03.jpg)

![MG4_LV](../images/mg4-09.png){ width="545" height="382" }

This is the Low voltage connector plug: [aliexpress](https://www.aliexpress.com/item/1005004677986133.html)

The one you need is the female.

There's are non-wired versions avaialable too for doing your own crimping but this looks easier to implement.

![alilvplug](../images/mg4-10.png){ width="344" height="348" }

Lots of useful information here: [MG4 ESS SM.pdf](https://github.com/user-attachments/files/25114213/MG4.ESS.SM.pdf)

### Power connections

The battery needs a 12V-14V supply to pins 1 & 3, and draws 600mA continuous with the contactors closed, and ~3A briefly when closing the contactors. 
On the 49.1kWh pack, the pin 4 IgnRelay also requires 12V before the contactors will close.

To reduce potential issues with the isolation measurement, it is preferable to have a 12V supply that is isolated from the grid (eg, powered from a 2-pin double-insulated adapter).

### CAN connections

The battery has three CAN buses:

**CAN PT** is the powertrain bus, which connects the main powertrain components. The battery outputs its vital statistics (voltages, SoC and temperatures) on this bus. OBD requests (0x7e5 & 0x7DF) work over this bus. It is an FD interface which requires a 50000kbit CAN  2Mb CANFD connection.  

**CAN PT EXT** is the powertrain extension bus and it listens for the messages which control the contactors. It's a regular CAN interface at 50000kbit.

**CAN BMS** seems to be the raw data from the BMS, we're not currently sure what information it contains.  It's a regular CAN interface at 25000kbit.

## High Voltage Interlock (HVIL)

The HVIL connections don't seem to be an issue.

## Physical Size

The 51kWh packs are 1880mm x 1440mm x 110mm and 400kg, the 64/77kWh are 1880mm x 1440mm x 125mm and 410/450kg (including the mounting rails).  At the top of the pack is an Energy Distribution Module (EDM) which mounts the contactors, High and Low Voltage connections and the Battery Management Unit (BMU). If getting from a wrecker/breaker try to get the Power Distribution Box (PDU) as it has a number of useful connectors that can be reused.

![image](../images/mg4-04.webp)

![PXL_20251119_080901770 MP](../images/mg4-05.webp)

![565167202_24727149553573186_4603669578284620967_n](../images/mg4-06.jpg)

![goes-here](../images/mg4-07.jpg)

You will also need to use an isolated 12V power supply (a 2-pin power supply with no earth pin) to power the BMS as well as the Battery Emulator hardware (unless you are using isolated CAN), to ensure that there is no current path between the BMS case and the inverter's ground.
