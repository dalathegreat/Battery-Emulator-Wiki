## Read this first

Preface, the entire Battery-Emulator project sets out to achieve safe re-use of EV batteries. By building your own battery, you will be taking larger risks. Take extra precaution when working on a custom DIY HV battery, you have been warned.

## BMW S-BOX
The BMW S-BOX is a safety box that includes precharge contactors as well as voltage and current probes and fuse. S-BOX can be used eg. on DIY HV Battery and with CHAdeMo vehicles 

|  Part Number |  Supported | Precharge resistor | Negative/Positive Relays | Precharge relay | Fuse |  Notes |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: |:---------: |
| 8686893 | ✅ | 15 Ω | AEV14012 120A/450V (400A 30s) | AEC51012 | 7GP074 450V 350A | HW 24.002, SW 10.050 |

## Wiring

White connector:

* PIN 1:  CAN-H  NOTE: 120ohm internal resistor!
* PIN 10: CAN-L
* PIN 3:  GND
* PIN 12: +12V (Electronics, ~250mA)
* PIN 14: +12V (Contactors)

## Integration with DIY project

The S-BOX uses the following CAN message IDs: 0x100, 0x110, 0x200, 0x210, 0x220, 0x230, 0x300, 0x310, 0x320, 0x321, 0x322, 0x410, 0x510, 0x511, 0x5F0, 0x5F1 and 0x600. 
When connecting the S-BOX to a shared CAN bus, ensure that these IDs are not already in use by other devices on the same bus to avoid conflicts.

## Configuration:

You can adjust the voltage limits and relay timers by modifying the BMW-SBOX.h file.

## More info
* [https://github.com/damienmaguire/BMW_SBox](https://github.com/damienmaguire/BMW_SBox)
* [https://openinverter.org/wiki/BMW_Hybrid_Battery_Pack#S-Box](https://openinverter.org/wiki/BMW_Hybrid_Battery_Pack#S-Box)