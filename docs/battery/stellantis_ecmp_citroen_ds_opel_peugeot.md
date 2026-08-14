---
title: "Stellantis eCMP (Citroen, DS, Opel, Peugeot)"
---

## Note on stationary storage :notebook: :zap: 

1. To use the eCMP battery in stationary storage, the BMS needs to be isolated to keep contactors engaged. This requires opening the battery, exposing yourself to 400V. Only proceed with this battery if you are OK with High Voltage work. For the full procedure, see [this section of the wiki](stellantis_ecmp_citroen_ds_opel_peugeot.md#disabling-isolation-monitoring-via-hw-modification)
2. Also note that CAN communication needs to be completely electrically isolated to keep contactors engaged. **This can easiest be achieved by using a "LilyGo T-2CAN" board, or adding a separate CAN Bus isolator,** links in the [Lightning strike wiki page](../setup/hardware/lightning_strike.md)

Failure to fulfill the two requirements will lead to contactors opening after 60 seconds of use (2 minutes on some packs), due to Isolation DTC being set inside the battery.

### Supported Stellantis e-CMP batteries
The following eCMP ( Peugeot, Citroën, DS, Opel/Vauxhall ) batteries are currently supported.

- Citroen ë-C4 (2020-) ✔️
- DS DS3 (2020-) ❓ 
- Opel/Vauxhall Corsa-e/Mokka-e (2019-) ✔️
- Peugeot e-208/e-2008(2020-) ✔️

### Supported 50kWh & 75kWh VAN? platform batteries
The same Stellantis eCMP platform integration can be used for **some** Toyota/Citroen/Fiat/Opel/Peugeot/Vauxhall van batteries. These batteries come in 50 and 75kWh sizes. It is still unclear what packs work, and which require more integration. It is also unclear what specific platform these batteries are.

#### V1 vs V2 VANs
Only V1 VAN packs work, V2 does not. You can spot the V1 by looking at the small HV connector which has 4 screws. On the V2, this connector is larger and has two screws.

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-15.png)

- Toyota Proace / Proace Verso Electric ✔️
- Citroën e-Jumpy / e-SpaceTourer ✔️
- Fiat Scudo / Ulysse Electric ✔️
- Opel (Vauxhall) Zafira / Vivaro ✔️
- Peugeot Partner / Expert / Traveller ✔️
- Maybe more, feel free to add

### Supported 44kWh & 82kWh "STLA medium" platform batteries

Work in progress, values not valid yet.

- Peugeot e-3008 III (e-P64, 2024–present)  ❓ 
- Peugeot e-5008 III (e-P67, 2024–present)  ❓ 
- Opel Grandland II (2024–present)  ❓ 

### Battery dimensions

The 50kWh car battery weighs approximately 350kg
The 50kWh VAN battery weighs approximately 382kg
The 75kWh VAN battery weighs approximately 534kg
The 50kWh battery (108 2x cells) has an operating voltage between 356 and 448 VDC (108 double cells x 3.3 - 4.15V)

The eCMP platform comes in three different physical sizes, A, B and C type:

| Designation |  Type | Models | Length (mm) | Width (mm) | Height (mm) |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| A | eCMP L1 | eP2JO (Corsa-e), eP21 (208), eD34 (DS3), eP2QO (Mokka) | 2090| 1280| 280
| B | eCMP L2 V1 | eP24 (2008) | 2145| 1280| 280
| C | eCMP L2 V2 | eC41 (C4) | 2145| 1280| 280

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-01.png)

## Software configuration
For this battery type, use the option called "Stellantis ECMP battery" under the "Battery Protocol" setting.

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-02.png)

### HV connection

!!! info "IMPORTANT"
    **There are High Voltage Interlock (HVIL) connections that need to be seated on the battery.**

    Depending on which battery you get, there will be multiple pins to jumper.

    If you fail to jumper all HVIL pins, an event will be raised, and under the More Batter info page you will see a low IN reading.

    HVIL circuit open (bad)<br>
    HVIL IN Voltage: 2mV<br>
    HVIL Out Voltage: 4998mV<br>

    HVIL circuit closed (good)<br>
    HVIL IN Voltage: 4970mV<br>
    HVIL Out Voltage: 4998mV<br>

Example of jumpered HVIL on **unused** HV connector on the rear end of the battery:

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-16.png){ width="50%" }

Polarity on cable side for the VAN Pack:

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-17.png)

!!! warning "CAUTION"
    **For the 50kWh CAR Packs this polarity is REVERSED!!!**

    ![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-18.png){ width="50%" }

<a name="HVIL"></a>
!!! tip "TIP"
    To disable completely the HVIL, just short the 2 wires from the BMS connector:

    ![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-03.png)

### Wiring pinout
The following pinout has been reverse engineered on an ë-C4.

| Pin | color | Signal | Note |
| --- | --- | --- | --- |
| 1 | green | CAN H | (Connect to Battery Emulator CAN H)
| 2 | white | CAN L | (Connect to Battery Emulator CAN L)
| 5 | yellow | 12V WAKE UP | (Connect to permanent 12V)
| 6 | green | Crash signal | (Connect to permanent 12V)
| 7 | red | 12V permanent | (Connect to permanent 12V)
| 10 | grey | 12V permanent | (Connect to permanent 12V)
| 11 | yellow | HVIL | (Connect to pin 12) [*](#HVIL)
| 12 | pink | HVIL | (Connect to pin 11) [*](#HVIL)
| 14 | light grey | GND | (Connect to GND for the 12V feed)

This platform shares its low voltage connector with the [Stellantis SMP platform](stellantis_smp_platform.md)

### Part numbers and purchase links
Did your battery not come with all the required cables/plugs? No worries, here are the part numbers and purchase links!

#### High voltage connectors

- [aliexpress](https://a.aliexpress.com/_EImj7ZG)

- J9D3-14N236

![J9D3-14N236](../images/stellantis-ecmp-citroen-ds-opel-peugeot-04.webp)

- J9D3-14N238

![J9D3-14N238](../images/stellantis-ecmp-citroen-ds-opel-peugeot-05.webp)

- 5QE971015 (~110cm long)

![5QE971015B](../images/stellantis-ecmp-citroen-ds-opel-peugeot-06.jpeg)

- 5Q0971015 (~310cm long)

![5Q0971015](../images/stellantis-ecmp-citroen-ds-opel-peugeot-07.jpeg)

#### Class-Y Capacitors 10NF 400V:

- [aliexpress](https://a.aliexpress.com/_EH7Rw0k)

#### Low voltage connector

LFP low voltage connector in stock on Mouser incase you are not able to get the harness with connector when you buy the battery. The connector has the pin numbering stamped on it.

![image](../images/stellantis-cmp-smart-car-platform-07.png)

- Connector: 27ZRO-B-1A
- Pins 0.3 to 0.5 mm$`^2`$: SZRO-A021T-M0.64 
- Pins 0.75 to 0.85 mm$`^2`$: SZRO-A031T-M0.64 
- Dummy Plug: WPHDP-H-1A-H
- [aliexpress](https://aliexpress.com/item/1005010560783903.html)

### Disabling isolation monitoring via HW modification

The eCMP BMS performs real time insulation monitoring. When installing the battery to a stationary storage system, the solar inverter will start to perform insulation monitoring. This means the vehicle monitoring is no longer required, and unfortunately on the eCMP this monitoring will incorrectly detect leakage and open contactors after 1 minute when in use.

#### Step 1, isolating BMS by floating it

To get around this issue, we need to disable the insulation monitoring on the BMS. The only known way at this stage is to open up the battery, and insulate the BMS grounding points. This effectively disables the isolation monitoring from interfering with the contactors.

To perform this, open up the battery and locate the BMS. Isolate the part circled in red.

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-08.png)

#### Step 2, Install capacitors

On this PCB inside the battery, place 2x Y capacitors 10nF between:

- BAT+ and GND
- BAT- and GND

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-09.png)

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-10.png)

In a (75kwh) Van pack it looks a bit different, there doesn't seem to be a BMS ground in the contactor enclosure. But! You can run a wire from the BMS ground through the pack (30cm distance) to meet up in the contactor box. The pcb in the contactor box also looks a bit different. The top yellow wire is B-, the bottom pink wire is B+:

![WhatsApp Image 2026-04-18 at 22 06 23 (3)](../images/stellantis-ecmp-citroen-ds-opel-peugeot-20.jpeg)
 
In the BMS enclosure, the 2 bottom blue wires of the top plug are BMS ground: 

![WhatsApp Image 2026-04-18 at 22 06 23 (2)](../images/stellantis-ecmp-citroen-ds-opel-peugeot-21.jpeg)
 
And an overview of the components in a Van Pack: 

![WhatsApp Image 2026-04-18 at 22 06 23](../images/stellantis-ecmp-citroen-ds-opel-peugeot-22.jpeg)
(open the image in a new tab to see the details)
<br><br>
End result: 

![WhatsApp Image 2026-04-18 at 22 06 23 (4)](../images/stellantis-ecmp-citroen-ds-opel-peugeot-23.jpeg)
<br><br>
Alternatively, the same capacitors can be installed on the OUTSIDE of the battery, for a much safer install, not requiring dismantling the contactor box.

![capacitors](../images/stellantis-ecmp-citroen-ds-opel-peugeot-11.jpg)

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-12.png)

#### Step 3, Insulate CAN bus from inverter
CAN needs to be on separate GND plane compared to inverter. Use a CAN opto isolator, or a board that has isolation between CAN chips like for instance the LilyGo T-2CAN. You can also add a CAN Bus isolator, links in the [Lightning strike wiki page](../setup/hardware/lightning_strike.md)

### Unlocking the battery
Under the "More Battery Info" page you can run collision unlock, contactor stuck unlock, and isolation error unlocking procedures. Remember to press the "Open contactors" button via the main page before running these requests, otherwise they wont work.

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-13.png)

How to deal with red screens:

![image](../images/stellantis-ecmp-citroen-ds-opel-peugeot-14.png)

If you have this red screen, check if you did connect the main contactors box (the second one is not needed, it's only used for DC charging)
Also you might have stored errors in BMS. When trying to clear the codes you MUST press multiple times the buttons (the commands are not always executed successfully so you need to press them more than once). Then reboot BE and do a hard reset (cut 12V then turn on again)

### Reverse engineering info

Can Logs can be found here: [google](https://drive.google.com/drive/folders/1S-Nf0dN5nZi71HhXIoM3GTydEk_VHHuM?usp=drive_link)

### Troubleshooting tips

- Try feeding the battery from separate 12V supply than your BE device. A 12V lead-acid battery is fine for troubleshooting.

### Double battery operation :battery: :battery: 
ECMP integration supports running two packs in parallel
For double ECMP batteries you need:

- 2 separate AC/DC PSU or another way to isolate the GND from the 2 BMS
- 2 HV DC contactors for the 2nd battery to join the 1st one (as long as the DC voltage difference is 2V or lower)
- an additional CAN communication for BE in order to talk to the 2nd battery
- an additional fuse for the 2nd battery

For T2CAN you can get a MCP2518FD and set it up as classic CAN. The 2 onboard CAN connectors will be used for the 2 battery pacs:  native (CANB) for 1st battery, CANA for 2nd battery and the additional MCP2518FD for the inverter
Currently you cant clear the 2nd battery error codes from BE, only the 1st battery.

Schematics below. As always - take extra care when working with HV batteries.
![double-ecmp-battery-emulator](../images/stellantis-ecmp-citroen-ds-opel-peugeot-24.jpg)

NOTE: When  