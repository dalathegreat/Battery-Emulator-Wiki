---
title: "Nissan Ariya"
---

## Work in progress integration :construction: 

## General info

⚠️ CAN LOGS WANTED FOR THIS BATTERY! ⚠️ 

The Nissan Ariya [battery](https://www.batterydesign.net/2022-nissan-ariya/) comes in two variants.

- 63kWh - 96S 400V Architecture - 451kg 1456x384x2099mm
- 87kWh - 96S 400V Architecture - 578kg 1456x384x2099mm

![image](../images/nissan-ariya-01.png)

## Pinout BMS
The Ariya battery uses the same 36-pin Yazaki connector as the Nissan LEAF, but it uses more pins:

![bild](../images/nissan-ariya-02.png)

![image](../images/nissan-ariya-04.png)

* Pin 34 CAN-H - Connect to LilyGo CAN-H
* Pin 35 CAN-L - Connect to LilyGo CAN-L
* Pin 6 Ground - Connect to Ground
* Pin 13 Ground - Connect to Ground
* Pin 15 Ground - Connect to Ground
* Pin 20 Ground - Connect to Ground
* Pin 12 12V - Connect to 12V constant

Depending on which high voltage port you use the next pins will differ. 
If using MAIN-HV: (the safe bet, since we control both contactors)

* Pin 1 Main relay 1 GND - Connect to Ground
* Pin 7 Main relay 2 GND - Connect to Ground
* Pin 14 Precharge GND - Connect to Ground
* Pin 33 Precharge Sig - Connect to 12V to control precharge (either manual or automatic)
* Pin 19 Main relay 1 Sig - Connect to 12V to control contactor (either manual or automatic)
* Pin 26 Main relay 2 Sig - Connect to 12V to control contactor (either manual or automatic)

If using QC-HV: (UNCLEAR HOW THIS WORKS)

* Pin 2 QC relay 1 GND - Connect to Ground
* Pin 8 QC relay 2 GND - Connect to Ground
* Pin 11 QC cont sig - Connect to ?
* Pin 25 QC state sig - Connect to ?

You can use either QC-HV or the MAIN-HV connector. The QC-HV uses the same high voltage cable as the Nissan LEAF.
![bild](../images/nissan-ariya-03.png)

## Precharge/Contactor closing

Almost all EV batteries contain contactors and precharge relays. Contactors act like big relays, and are used to control electrical circuits where currents are high. They are designed to be able to break the flow of current in a safe manner without electrical arcing. There are two contactors, one for positive and one for negative. To avoid electrical arcing when turning on the battery, the initial inrush of current is led thru a precharge resistor, to allow for slow charging of the capacitors inside the inverter. If the inverter has been turned off for a long time, the capacitors inside will act almost as a dead-short, 0 ohm resistance. If you skip using the precharge, then your contactors will spark every time you close them, wearing them out prematurely. Now that we know what the contactors/precharge does, we can look at ways to control it.

The Nissan Ariya battery can be used in two ways. Manual and automatic startup/shutdown of the contactors/precharge circuit.

### Manual control 🖐️

Using switches and manual timing, it is possible to turn on the precharge(A), negative contactor(B), and positive contactor(C). This is the simplest method, but it increases the risk of failures. Accidentally flipping the wrong switch at the wrong time may damage the battery and/or inverter. Also if you leave your battery un-attended, the battery has no way of disconnecting from the inverter incase it senses a fault. **Due to all this, the manual control method is NOT recommended.** 

### Automatic control 🤖

The LilyGo hardware can act on its own, and turn on/off the contactors/precharge resistor when the battery says it is OK and turn off when not OK to proceed. This is done via the 3.3V digital output header that is located on the board. To use these, you need to solder a 2x6 row connector onto the board. After the row connector is fitted, you can connect a flat ribbon cable between the pins, and the relays.

To enable the feature in the software, uncomment the following line in the `USER_SETTINGS.h` file.

`#define CONTACTOR_CONTROL     //Enable this line to have pins 25,32,33 handle automatic precharge/contactor+/contactor- closing sequence`

To keep things simple, it is recommended to use Solid State Relays (SSR). These can be activated with 3Volt, and control large DC currents. Follow this schematic to complete the circuit:

- (LilyGo) Precharge pin 25 - Precharge SSR -> Pin 33 Precharge Sig on B36 connector on battery
- (LilyGo) Positive Contactor pin 32 - Positive SSR -> Pin 19 Main relay 1 Sig on B36 connector on battery
- (LilyGo) Negative Contactor pin 33 - Negative SSR -> Pin 26 Main relay 2 Sig on B36 connector on battery
- (LilyGo) GND - All 3x SSR - input

- Detailed circuit picture will be placed here

## Part numbers

|  Product |  Purchase Link |
| :--------: | :---------: |
| 36pin battery connector (2013-2023) Yazaki 7287-1065-30 (female with cables) |  [AliExpress](https://s.click.aliexpress.com/e/_onL8Fx6)   |
| High voltage connector QC 297A6-5SH1A |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A65SH1A&_sacat=0)   |
| High voltage connector Main |  ???   |
| Service disconnect switch |  ???   |