> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## FAQ: Renault Zoe Battery Gen2
The Renault Zoe Gen2 has good support in the Battery-Emulator project. Note that confused packs need NVROL reset, more info on that further down in this Wiki

## Variants of the Zoe
There are 4x batteries available for the Zoe, This page focuses on the Gen2 50/52kWh battery
* [22kWh 2012-2019, Gen1](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Zoe-Gen1)
* [41kWh 2016-2019, Gen1](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Zoe-Gen1)
* 50kWh 2019-, Gen2
* 52kWh 2020-, Gen2

Stickers signaling that the battery is the Gen2 50/52kWh battery
![test](../images/renault-zoe-gen2-01.jpg)

## Software configuration
For this battery type, use the option called "Renault Zoe Gen2 50kWh" under the "Battery Protocol" setting

<img width="593" height="73" alt="image" src="../images/renault-zoe-gen2-15.png" />

## Zoe Gen2 pictures and pinout
Credit goes to ljames28 for the excellent repo: https://github.com/ljames28/Renault-Zoe-PH2-ZE50-Canbus-LBC-Information

Beware that the plug for previous generations battery fits the Gen2 version but the pinout is different so it will not work.
Allso note plug pinout is seen from the rear of the plug where the wires come out. If you cannot source a plug and are comfortable opening the battery, theres a handy industry std connector just on the inside, but the colors of wires change. (white visible below)
![image](../images/renault-zoe-gen2-02.png)
![connections](../images/renault-zoe-gen2-03.png)
![image](../images/renault-zoe-gen2-04.png)



## Low voltage wiring diagram
Connect the pins from the battery to the Battery-Emulator, according to this diagram:

**Please note these circuit diagrams are currently work in progress, check validity yourself before powering on**

Example Wiring Diagram: LilyGo T-CAN485 + Zoe Gen2 + optional equipment stop button

![image](../images/renault-zoe-gen2-05.png)

Example Wiring Diagram: LilyGo T-CAN485 + Zoe Gen2 + optional equipment stop button + CAN Filter (as required for some invertors)

![image](../images/renault-zoe-gen2-06.png)

Example Wiring Diagram: LilyGo T-2CAN + Zoe Gen2 + optional equipment stop button

![image](../images/renault-zoe-gen2-07.png)

Example Wiring Diagram: Stark CMR + Zoe Gen2

<img width="1064" height="764" alt="image" src="../images/renault-zoe-gen2-16.png" />


> [!NOTE]
> This Zoe battery contains GND switched precharge relay and positive contactor. There is no negative contactor to control


> [!WARNING]
> It is very important to not mix up the wiring between precharge/positive-contactor. Running all the power thru the precharge will result in it blowing up 

<img alt="image" src="../images/renault-zoe-gen2-17.png" />


## Part list
Incase your battery is missing parts, here is a list of the spare part numbers along with purchase links

## Part numbers for Renault Zoe Gen2 batteries

|  Product |  Purchase Link |
| :--------: | :---------: |
| Battery communication connector, Yazaki 7283-8854-30 (plastic shell, female) + contacts and seals acc. datasheet or complete set at Aliexpress. Battery has the male connector. |  [AliExpress](https://de.aliexpress.com/item/4000174903780.html)   |
| High voltage connector complete cable assembly 297A26138R (However these 'may' also work 297A6-5SH1A OR 297A22581R) or RCS800 connector shell (1x) 13974469 + contacts (2x) 13893887 + retainer (2x) 13893889 + seal (2x) 13893888|  [Ebay](https://www.ebay.com/p/17067914686)   |
| *Safety switch/fuse OEM Part no. 297C 126 45R | Renault UK quoted £43.89+VAT   |

*Please note not all safety switches are the same there is at least 2 versions, using the incorrect one could result in blown fuses or worse.
* Also part no. 993B1 5333R is for the sticker on top of the safety fuse not the safety fuse itself.

**The correct part number can be found by looking at the area as shown below.**
![image](../images/renault-zoe-gen2-08.png)


My 52kwh battery came with following part:
![image](../images/renault-zoe-gen2-09.png)

Renault Zoe Gen 2 safety switch has continuity between terminals 1-2 and 3-4, as shown above. (Renault Zoe Gen 1 has continuity between terminal 1-4 and 2-3, there is also a fuse inside which Gen2 switch does not have).

### High Voltage Interlock (HVIL)
The battery has two HVIL circuits that need to be shorted together to get the battery to think that connectors are seated.

- Service disconnect needs to be fitted (Note, get the correct one!)
- High voltage connector needs to be fitted

If one of these are missing, the Event HVIL Failure (EVENT_HVIL_FAILURE) will be triggered. To recover from this mode, power everything down, fit both connectors, and power back up. Note that there are multiple versions of the service disconnect switch for Renault batteries, so get the one specifically for the Zoe Gen2

## NVROL reset

### Why do we need to perform NVROL reset?
"If the pack is in a state where it is confused about the time, you may need to reset it's NVROL memory. However, if the power is later power cycled, it will revert back to his previous confused state. Therefore, after resetting the NVROL you must enable "temporisation before sleep", and then stop streaming CAN message 0x373. It will then save the data and go to sleep. When the pack is confused, the state of charge may reset back to incorrect value every time the power is reset which will make it hard to use the battery. Balancing of the battery will also be halted in this state"

### How do I perform this reset?
Under the Webserver for the Battery-Emulator, select the "More Battery Info" page, and then press the "Perform NVROL reset" button, and "OK"

![image](../images/renault-zoe-gen2-10.png)

![image](../images/renault-zoe-gen2-11.png)

![image](../images/renault-zoe-gen2-12.png)

### Example procedure off NVROL to balance battery :b: 
Zoe gen2 52kWh. First balancing started at last. Procedure that worked on my setup sequentially:
- Nvrol reset performed
- 30-ish seconds wait
- Verify temporization active from More Battery Info page
- Remove battery can plug from Stark CMR
- Bms power down (removed plug from stark)
- Stark CMR power down
- Connect all back together
- Stark CMR power up
- Balancing started immediately, visible from Cellmonitor page

> [!NOTE]
> The reset requires a 30 seconds sleep after completion. To sleep properly, all CAN communication is halted. If the Battery is connected to the same CAN channel as an inverter, this inverter will prevent the sleep cycle. So in order to properly do the NVROL-sleep, a dedicated CAN channel for the Zoe battery is required

## Example integration
Wallmounted Zoe 41kWh battery:

![image](../images/renault-zoe-gen2-13.png)

![image](../images/renault-zoe-gen2-14.png)

## Troubleshooting
The Zoe2 pack has fuses that can be blown. Telltale sign of this being blown is that the voltage was dropping below what was read by BE, so the voltage was read via CAN as 358 but actual voltage measuring was 310-320v

<img alt="image" src="../images/renault-zoe-gen2-18.png" />

