---
title: "Tesla Model 3/Y"
---

!!! warning "WARNING"
    Re-using the Tesla batteries might require opening the Penthouse to verify that fuses have not blown. To do this safely, the correct personal protective equipment (PPE) is required. The pyrofuse for instance contains a small explosive charge to be able to disconnect the high voltage quickly. When handling the inside of a Tesla battery, please make sure you check your local electrical legislation requirements. This is a good starting point when it comes to PPE:

* Electrical safety training valid
* Class 0 voltage gloves
* Face shield
* Workclothes with EN-61482 rating

It is a good idea to store the battery away from your house but still protected from the weather. A separated garage, roof or garden shed would seem appropriate, provided it is well ventilated with good ducting/cable management.

## Which packs work?
The Tesla Model 3/Y packs have many hardware/software revisions. Due to this it can be hard to know if a certain battery is compatible (or requires extra work with pre-charge / HVIL). Here is a list of packs we have used successfully:

* Model 3Y: 2019 RWD ✅ 
* Model 3/Y: 2020-2021 AWD ✅ 
* Model 3/Y: 1666968-00-C ✅ 
* Model 3/Y: 1522312-00-D ✅ 
* Model 3/Y: 2022 RWD - China manufactured pack - LFP cells - Part number 1666969-00-C ✅ 
* Model 3/Y: 1666969-24-E ✅ (NOTE: Requires DIGITAL_HVIL)
* Model 3/Y: 2022 RWD - China manufactured pack - LFP cells (60 kWh) - Part number 1666969-00-D ✅ 
* Model 3/Y: 2021 RWD - China manufactured pack - LFP cells - Part number 1567439-00-D ✅ 
* Model 3/Y: 2021 RWD - China manufactured pack - LFP cells - Part number 1567439-00-C ✅ 
* Model 3/Y: 2022 AWD - Part number 1700012-00-C ✅ 
* Model 3/Y: 2022 AWD - 1700012-00-B ✅ 
* Model 3/Y: 2023 AWD - 1700012-99-B ✅ 
* Model 3/Y: 2023 AWD - 1700012-00-C ✅ 
* Model 3/Y: 2023 1733002-D2-B Berlin "Bladerunner" ✅ 
* Model 3/Y: 2019 AWD - USA manufactured pack - Part number 1104423-00-M ✅ 
* Model 3/Y: 2022 AWD - China manufactured pack - Part number 1700012-00-B ✅ 
* Model 3/Y: 2024 RWD - China manufactured pack - Part number 1666969-55-F ✅ (NOTE: Requires DIGITAL_HVIL)
* Model 3/Y: 2024 AWD - China manufactured pack - Part number 1700012-00-E ✅ (NOTE: Requires DIGITAL_HVIL)
* Model 3/Y 2023 AWD - USA manufactured pack - part number 1234422-00-A ✅ NCA Chemistry 82Kwh
* Model ? 2025 Structural battery - (P)2620021-99-F ✅ 92s9p
* Model 3/Y 2025 RWD - LFP Part number 2084670-55-B ✅ (DIGITAL_HVIL)
* ? (feel free to add specs of your known working packs) 

Note that 2024 and onwards might require setting the "Digital HVIL (2024+)" option in the Settings page to get contactor closing to work.

![image](../images/tesla-model-s-3-x-y-15.png){ width="561" height="81" }

Also note that Tesla Model S/X needs to be newer than 2020+ to work with the current code!

If you're looking at an existing pack and are wanting to try and decipher more information about it, you can try looking here for serial number information [Tesla Model 3 2024 service manual](https://service.tesla.com/docs/Model3/ServiceManual/2024/en-us/GUID-70E58915-D9C5-42E4-BB41-3CA992532667.html).
Tesla Model 3 Electrical Reference can be found [Here](https://service.tesla.com/docs/Model3/ElectricalReference/).
Tesla Model Y Electrical Reference can be found [Here](https://service.tesla.com/docs/ModelY/ElectricalReference/).
Tesla Service Mode User Guide [Here](https://service.tesla.com/docs/Public/ServiceMode/service_mode_user_guide.pdf).

### How do I test a battery before buying ?

It is possible to test a battery quite easily before purchase. For this you need the X098 connector, some 60/120Ohm resistors, a board running Battery-Emulator (a LilyGo for instance), and a 12V battery. See [this video for a step by step on how to connect to a Tesla battery](https://youtu.be/Zikb94dxlTM?si=u05h9BuUjtZo3BW2&t=122) , and also check out the wiring instructions below. Note, you do not need to connect anything else than the X098 connector, and contactor closing is not required to get a readout.

![I’m the first person in the world to do this! 2](../images/tesla-model-s-3-x-y-01.jpg)

!!! tip "TIP"
    When you want to test only battery, do not use any inverter protocol at the same time. Only compile software for Tesla battery to make life easier.

Example, LilyGo board with 12V battery used to test a Tesla Model Y battery, which had sat for 2 years and turned out to have a nasty 500mV defect. So the person really avoided a costly mistake by testing the battery beforehand!

![image](../images/tesla-model-s-3-x-y-02.png)

## Software configuration
For this battery type, use the option called "Tesla Model 3/Y", or "Tesla Model S/X" under the "Battery Protocol" setting.

![image](../images/tesla-model-s-3-x-y-16.png){ width="543" height="386" }

Configure all the options correctly, according to what pack size and from which country the donor car came from. This is very important to get right, otherwise fault codes will be active on the battery side.

Manual charging/discharge power also needs to be set, due to not being able to use the values sent by the BMS yet. It is important to set these values to the same Power size as your inverter, for instance 6000 W if you have a 6kW inverter. 

### Note on LFP chemistry

All Model S/X packs are NCM/A chemistry.

Some Model 3/Y packs are LFP chemistry, and some are NCM/A chemistry.

The code autodetects incase you have an LFP battery, but the detection method can take up to 5minutes. Incase you want to speed this up for additional safety, configure "Battery chemistry" as LFP. Why you might ask? Well in some rare circumstances, like say you restart everything when the battery sits at true 100% charge, it will be treated as a NCM battery for the first few minutes of boot. This might overcharge the battery, until it figures out it is an LFP pack and should use the more restricted voltage range.

![image](../images/tesla-model-s-3-x-y-17.png){ width="592" height="33" }

## Part numbers for Tesla Model 3 batteries

Incase your battery is missing some wires/fuses, here are the OEM part numbers and purchase links. Do note that it might be cheaper to source from your local scrapyard!

|  Product | Part # | Purchase Link |
| :--------: | :---------: | :---------: |
| Pyrofuse | 1064689 106469-00-J 1064689-00 10646900J 1064689-00 | [amazon](https://www.amazon.com/dp/B0CBRQJL7B?psc=1&ref=ppx_yo2ov_dt_b_product_details) |
| HV connector | 1109000-00 | [ingenext](https://ingenext.ca/products/tesla-model-3-asy-hv-harn-rdu-m3-1109000-00-d) |
| X098 connector | 6189-7077 13 Pin Sumitomo Sealed Female | [aliexpress](https://a.aliexpress.com/_EyTbzzK)  |
| Penthouse socket | Torx Socket 10EPR | [fcpeuro](https://www.fcpeuro.com/products/epr-torx-plus-socket-set-1-4-drive-5-piece-cta-manufacturing-5064) or [aliexpress](https://vi.aliexpress.com/item/1005006015748803.html)  |

## Replace the Pyrofuse

The Pyrofuse is located inside penthouse cover. It blows if the car’s airbags go off, so it’s likely you’ll need to replace it. Whilst it is possible to bypass it (using a DC circuit breaker and 2 Ohm resistor across the monitoring pins) this is not recommended as the Pyro fuse self-monitors load and can trip on its own (even though the car central computer isn’t running) so it’s best to use a proper pyro fuse and retain the original safety functionality that it provides. This is probably the most dangerous part of the process. Refer to the safety section and ensure you’re wearing PPE
and take care not to short anything with your tools. I used a plastic case around the fuse so the screws didn’t drop or touch the side. Socket was either half-inch or 13mm. After removing the fuse, always check the voltage potentials before putting in a new Pyrofuse. Check ground to each
of the Pyrofuse connections, and also between them. Voltage between them is usually 100-180 volts but starts sagging slowly as soon as you connect the multi meter. It’s normal although a bit unintuitive. (The battery gets split into 2 halves when the pyro blows).

## Pre-charge capacitor

The battery runs a “pre charge” circuit before closing the contactors. This is done to avoid sending full power out to the drive unit instantaneously. Effectively the “pre charge” procedure involves ramping up the voltage from 0 to 350v in a relatively short space of time (approx. 1s). The battery needs to see a response from a capacitor charging otherwise it detects an issue and faults. Therefore, it is necessary to install a capacitor to simulate a motor connected, in order to complete the pre-charge procedure and close the contactors. The capacitor is installed directly across the main High Voltage cables. It can be done inside the penthouse but it’s preferable to do it outside the battery (to leave the battery unmodified) and inside an electrical box so that if the capacitor blows it doesn’t make a mess.

## High voltage wiring

Here is a simplified picture for the high voltage wiring on the Tesla battery. Depending on if your battery has the Power Conversion System (PCS), or not, the wiring varies. PCS is needed for contactor closing precharge circuit. Without it, pack wont turn on via CAN.

![bild](../images/tesla-model-s-3-x-y-03.png)
![bild](../images/tesla-model-s-3-x-y-04.png)

⚠️ Please note that the non-PCS version is much more dangerous if handled incorrectly. Manually pre-charging the circuit is very dangerous, since it requires redistributing 400V during the procedure ⚠️ If possible, try to opt for a battery that has the PCS intact, or add a PCS if your battery is missing one. Also note, that on non-PCS packs, you have to manually write an allowed discharge value, [like explained here](https://github.com/dalathegreat/Battery-Emulator/issues/429).

The 650-1000uF (500V) capacitor can be installed inside the battery housing (aka penthouse) -OR- be wired to one of the HV connectors on the battery. The capacitor simulates the presence of a driverunit, without it the battery controller will not allow the internal battery contactors to close.

This picture shows how to connect the capacitor. If you're using the Tesla HV connector connected outside the pack (recommended) then your load or inverter will be connected to that HV connector and you will only connect the capacitor to the bolts inside shown here.
![bild](../images/tesla-model-s-3-x-y-05.png)

If you are adding the capacitor to the outside of battery, connect it to the correct polarity (1=- , 2=+)

![image](../images/tesla-model-s-3-x-y-18.png)

## Low voltage wiring

The X098 connector has a few connections itself, scroll down to see where the pins should go.
If you want to run with the penthouse lid open, ground has to be connected to the two boltholes on each side of X098.
![Tesla_X098](../images/tesla-model-s-3-x-y-06.png)

The connector above will need the following connections...(apart the grounding of the holes if the lid is open)

* Pin 1 and 3 - 60  Ohm resistor between these pins on RWD(68also works), 120 Ohm on AWD packs
* Pin 8 and 18 - To +12V
* Pin 9 - GND 
* Pin 16 and 15 - To CAN-H and CAN-L on the board (Note, you might need to add 120Ohm resistor here, depending on CAN network structure)

![Tesla X098 HVC](../images/tesla-model-s-3-x-y-19.png){ width="520" height="298" }

![Tesla X098](../images/tesla-model-s-3-x-y-20.png){ width="1313" height="894" }

![Tesla HV Battery and HVIL](../images/tesla-model-s-3-x-y-21.png){ width="1301" height="923" }

### 12 Volt or 16 Volt?
Tesla used a standard Lead Acid 12 Volt battery in most applications. Beginning in Mid-2021, Tesla began converting the low voltage battery system in its vehicles to utilize a 15.5V 6.9Ah Li-Ion battery. [ohmmu.com](https://support.ohmmu.com/battery-product-support/tesla-all-models-identifying-low-voltage-battery-system-12v-vs-15-5v) Has some information to know if your car has the standard LA or Li-Ion. In 2024+ a new 12.8V LFP battery was introduced. More information from Weber State University YouTube Channel [Tesla 16V](https://www.youtube.com/watch?v=8-MNFgashpQ), [Tesla Low Voltage Charging System](https://www.youtube.com/watch?v=M1ZEorMeuDo), [Tesla 12.8V LFP](https://www.youtube.com/watch?v=QJsy1ay6tXs)
At this time, BE does not support the use of the 16V Li-Ion or 12.8V LFP battery for communication to tell the PCS DCDC LV Voltage to charge above the standard 12V LA battery. Using the standard 12 Volt Lead Acid battery will work normally in place of the other Li-Ion/LFP.

Make sure to connect the 12V battery to the PCS (two M8 screws close to the X098) with recommended wire size to supply the 30+ Amp demands.

ℹ️ The 12V requirement is quite large for the Tesla packs. Use a high power 14V source (large fully charged lead acid battery OR 30A lab power supply set to 12-16V). If the 12V supply is too weak, closing contactors wont be possible. The cables also need to be quite thick to avoid voltage drop. 1.5mm² is too small, the cables need to be 13mm² (6AWG) at minimum!

![image](../images/tesla-model-s-3-x-y-22.png){ width="895" height="750" }

## High voltage interlock circuit (HVIL)

The Tesla battery contains pyro and glass fuses that can be broken if the battery comes from a crashed vehicle. Do not use the battery unattended with these fuses bypassed !

For testing purposes, temporary copper cables can be used to replace glass fuses, but you should ideally use a replacement pyro fuse as you can't simply replace that fuse with wire.  The reason is that there are 2 small pins below the pyro fuse that expect to see around 2 Ohms of resistance from the Pyro fuse so simply putting wire across where the pyro fuse would usually be be will not work.  You will need to put a resistor across the 2 pins below where the pyro fuse would normally sit, but this is definitely not recommended and you should ideally just buy a replacement pyro fuse instead of doing anything temporary.

Remember, if you do anything temporary to make sure you install a proper fuse later on !!!

The battery has many High Voltage InterLock (HVIL) checks on each high voltage connector. These HVILs need to be jumpered in case you are not using the original connectors, otherwise the battery wont start. There is a big plate covering the high voltage components, called the "penthouse".  If you have a complete battery pack, the only HVIL connectors that need to be jumped are those of the HV connectors that you are not using.

Below is the HVIL for the AC connector, jumper location is shown (not the actual jumper itself).
![Tesla_hvil_ac](../images/tesla-model-s-3-x-y-07.jpg)

With the penthouse lid open, there are jumpers for the two HV-connectors. In this picture, the pyro fuse has been removed and replaced with a copper cable and a jumper. NOTE: Some packs cannot have pyro fuse jumpered, it needs to be a proper Pyro Fuse with a certain resistance! Also, if your battery is coming from a crashed vehicle you should absolutely expect the pyrofuse to be blown.
![Tesla_hvils_and_pyro_fuse](../images/tesla-model-s-3-x-y-08.jpg)

## HVIL Troubleshooting

There seems to be many hardware and firmware revisions of the Tesla Model 3/Y battery. Not all batteries will allow for contactor closing easily. Incase you run into a battery that cannot close contactors, you might have to tweak some resistor values between pin 1 and 3 (try 60 and 120 ohms first). 

It is recommended to turn on `Enable general logging via USB serial` OR `Enable general logging via Webserver` in the settings page get more info why HVIL is not allowing to close. Below are some messages you can encounter, along with troubleshooting tips:

![image](../images/tesla-model-s-3-x-y-23.png){ width="556" height="271" }

| Symptom | Fix   |
| :-----: | :---: |
| "Solar inverter does not allow for contactor closing. Check communication connection to the inverter OR disable the inverter protocol to proceed with contactor closing" | Some inverter protocols (Solax) require approval from inverter before contactors can close. You can remove the inveter protocol while testing if the battery works. |
| "Check high voltage connectors and interlock circuit! Closing contactor not allowed!" | Verify that all HVIL jumpers are satisfied. Verify that 60 / 120 Ohm resistor is seated |
| All HVIL connectors are ok, but battery stuck in Pyro test ("Please wait for Pyro Connection check to finish, HV cables successfully seated!") | Pyro fuse control pins not ok. Should have 1.8-2 Ohm when the fuse is OK |
| HVIL status is CURRENT_SOURCE_FAULT | HVIL has been incorrectly cut and crimped together |
| HVIL connectors are OK but battery still does not pass “Check high voltage connectors and interlock circuit!” | Penthouse lid open? Pyro fuse defect. Replace pyro fuse |
| "STATUS: Contactor: CLOSING" and low 12V "Low Voltage: 9V" | You dont get past the precharge state. Check that 12V cables to PCS are thick enough (2.5mm2), and that the 12V power supply is strong enough to close the contactors. Lead acid battery recommended. |
| “pyro squib is not connected!” | Pyro fuse defective, replace pyro fuse OR reseat pyro fuse (I had a good pyro fuse but reseating it cleared the error) |
| Your battery seems to be working and your contactors close, but at some point something happens and you can hear your pack contactors opening and closing every 30 - 60 seconds.   When you look on the Battery-Emulator console it shows that Negative contactor open and Positive contactor is closed, then after 30 - 60 seconds you hear the contactors clunk and now it's showing the opposite, Negative contactor is closed and Positive is Open and it continues over and over” | Only solution for this issue so far is to remove the x098 cable from the pack and also remove the power cables from the PCS which are attached to the outside of the pack.    Anything left plugged in seems to supply power to the logic boards inside the Penthouse and won't allow it to reset.   This will remove 12v power to the whole pack as well as CANBUS connection.  Leave pack unplugged for at least a minute (sometimes longer is needed) and then plug the x098 connector and bolt PCS 12V cables back onto the pack and reset your Battery-Emulator hardware and the pack should close both contactors as expected again.   |
| When testing the battery all the cell voltages load correctly and the other data is read correctly as well, but pack voltage shows 1V. | This indicates that the pyrofuse is blown and needs to be replaced. After replacing the pyrofuse, the pack voltage should show the correct value.  |

If the battery gets really stuck, removing the yellow connector here for a few minutes also helps:

![bild](../images/tesla-model-s-3-x-y-09.png)

If all else fails and you can not get HVIL loop to close, the last resort method is to solder 2 wires on the back of this PCB board:
![bild](../images/tesla-model-s-3-x-y-10.png)
The downside of this is that you will never have any shutdown incase a high voltage cable gets unplugged while the system runs. Do not go for this method if possible!

## Penthouse components
** To gain access to the penthouse you will need a specialist socket (example of one listed above in parts table) **

![bild](../images/tesla-model-s-3-x-y-12.png)
Connections info: [electrek](https://electrek.co/2017/08/24/tesla-model-3-exclusive-battery-pack-architecture/)

| Number | Description |
| :-----: | :---: |
| 1 | Charge port connector |
| 2 | Fast charge contactor assembly |
| 3 | Coolant line to PCS |
| 4 | PCS – Power Conversion System (often refered to as OBC) |
| 5 | HVC – High Voltage Controller |
| 6 | Low voltage connector to HVC from the vehicle (X098 connector) |
| 7 | 12V output from PCS |
| 8 | Positive HV contactor |
| 9 | Coolant line to PCS |
| 10 | HV connector to cabin heater and compressor |
| 11 | Cabin heater, compressor and PCS DC output fuse |
| 12 | HV connector to rear drive unit |
| 13 | Shunt? |
| 14 | HV pyro fuse |
| 15 | HV connector to front drive unit |
| 16 | Negative HV contactor |
| 17 | Connector for 3 phase AC charging |

## Complete wiring diagram

![bild](../images/tesla-model-s-3-x-y-13.png)

![image](../images/tesla-model-s-3-x-y-14.png)

## Note on balancing :b: 

Tesla batteries are very specific when they want to balance, and it is hard to get a battery to balance. NMC chemistry seems to be more stable long term, and millivolt deviations between cells are kept low even years in operation in stationary storage. LFP chemistry however get out of balance more easily. LFP also has a very specific need to be charged to 100% to calibrate SOC, and sit at this state to balance, which is unlikely to occur in stationary systems that are used 24/7.

### Current theory on balancing conditions

!!! warning "WARNING"
    Not all inverters are OK with contactors opening in operation. One user damaged their Fronius inverter while opening contactors under load. Always ensure 0 current before opening contactors, and if unsure, power off inverter.

Tesla batteries are intended to fully charge, and then enter a balancing phase after charging is completed and contactors open. This means that in order to balance the Tesla batteries, you cannot use them 24/7, and have to periodically charge the batteries full (99%) and press the "Pause" button, wait for current to go to 0A, and then press "Open Contactors" button in the webserver.

Tesla batteries will balance ~2mV per 24h or balancing.

Once you are done balancing, you can press the "Close Contactors" button, and "Unpause" to resume operation.

!!! warning "WARNING"
    During balancing with contactors open, 12V lead acid battery will NOT be charged. Make sure the lead acid battery has an external charger available while in this state.

![image](../images/tesla-model-s-3-x-y-24.png){ width="902" height="289" }

### Periodic forced charge-balancing (Can potentially aid to balance LFP)

To help keep LFP batteries balanced outside of a Tesla vehicle, the emulator has a forced charging mode. The forced charging mode can be enabled via the Settings page. It is recommended to run this ?once per month? on Tesla LFP batteries. Before enabling, make sure battery is close to full, and you have enough sun or grid power to continue charging and forcing the balance!

When enabling the Manual LFP balancing , the forced top charge runs for the specified amount of time, set in Balancing max time. The balancing parameters, Balancing float power , Max battery voltage , Max cell voltage and Max cell voltage deviation can also be adjusted from here. During this time, the SOC% is faked towards the inverter, and we allow the charge W set by user. This will help the battery reach higher SOC needed to balance?

![image](../images/tesla-model-s-3-x-y-25.png){ width="414" height="382" }

### Replacement BMS to balance

There is an ongoing open source project called the CellKeeper that aims to replace the BMS inside the Tesla battery with a standalone controller. This would instantly solve the balancing issue. Note that this board is still in development, and as soon as it is ready this page will be updated.

## Example integration

Check out this excellent summary from user "k" on the Discord server 🙌 
[Tesla battery for solar storage - tips and resources.pdf](https://github.com/user-attachments/files/16316246/Tesla.battery.for.solar.storage.-.tips.and.resources.pdf) **Be careful, this PDF shows a red wire going to the negative terminal of the 12V PCS input**

Or this installation option, simpler wiring example, with reference to the Charge Port ECU: 
[Battery installation.pdf](https://github.com/user-attachments/files/16918052/Battery.installation.pdf)
