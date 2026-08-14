---
title: "FoxESS H1 H3 AC1 KH"
---

!!! info "⚠️ Word of caution, CAN overvoltage ⚠️"
    FoxESS inverters can have high voltage potential on the CAN chip. They can be 110V when measuring between CAN and PE. It can burn up your Battery-Emulator CAN chips if there is a path to protective earth. This becomes a problem if the board you are using has GND on the same plane as PE. Then the 110V diff might leak over and damage the chips. A way to avoid this is to use a PSU to power the Battery-Emulator board that is not connected to PE. For instance a 2-prong phone charger would effectively be isolated from PE. 
    
    Note: This does not impact the lilygo T-2CAN, it is galvanically isolated, Foxess cannot fry the T-2CAN!

![image](../images/foxess-h1-h3-ac1-kh-01.png)

Another way to tackle this is with the use of a CAN isolator between the inverter and the rest of the system. Examples found in the [lightning strike wiki](../setup/hardware/lightning_strike.md#suggested-hardware)

![image](../images/foxess-h1-h3-ac1-kh-02.png)

!!! info "Word of caution, isolated CAN"
    This inverter does not handle a CAN connected EV battery on the same channel. If the inverter which likes to see only extended CAN frames sees standard automotive CAN frames, the inverter will enter a fault state.

This can be solved in a few ways:

   - One option is to use [add on MCP2515](../setup/can_related/can_add_on_mcp2515.md) board
   - Another options is to use [add on CAN-FD MCP2518](../setup/can_related/can_fd_add_on_mcp2518fd.md) board 
   - Third option is to use [Stark CMR hardware](../hardware/stark_cmr.md)
   - Fourth option is to use a [CAN filter](../setup/can_related/can_filter_hardware.md) between inverter and the rest of the system 

## Compatible FoxESS inverters

* FoxESS H1
   * Use `FoxESS compatible HV2600/ECS4100` primarily.
   * Can also use `SolaX Triple Power LFP over CAN bus` protocol, but some values will be wrong
* FoxESS H3
   * Uses `FoxESS compatible HV2600/ECS4100` protocol
* FoxESS AC1
   * Uses `SolaX Triple Power LFP over CAN bus` protocol
* FoxESS KH
   * Works with both `SolaX Triple Power LFP over CAN bus` and `FoxESS compatible HV2600/ECS4100` protocols
* FoxESS KP
   * Uses `FoxESS compatible HV2600/ECS4100` protocol
## Communication wiring

The FoxESS inverter works via CAN. Connect the Inverter side CAN-H & CAN-L to the Battery-Emulator.

!!! info "IMPORTANT"
    Different versions of the Foxess have different pinouts. Check user manual to see which pins are CAN-H / CAN-L.

![image](../images/foxess-h1-h3-ac1-kh-03.png)

## Which protocol to use

For this inverter type, use the option called "FoxESS compatible HV2600/ECS4100" under the "Inverter Protocol" setting.

![image](../images/foxess-h1-h3-ac1-kh-07.png){ width="495" height="63" }

The default values allow for a 400V EV battery to be used. If you are using a low voltage battery, you can lower the "FoxESS module count", it works in steps of 1-8 , each step being 50V. So if you are using a 200V battery, set the module count to 4

![image](../images/foxess-h1-h3-ac1-kh-08.png){ width="570" height="97" }

By default the battery will appear as a HV2600 battery. If you want to change this, the following enumerations have been successfully tested:

Fox ESS Battery Type Enum Lookup
Reverse-engineered Fox ESS battery type enum list.

Test conditions
Values were tested by changing the battery type enum and observing:
Battery name shown in Fox Cloud
Battery icon

CAN communication status
Battery telemetry availability (SOC, voltage, charge/discharge)

Test settings:
Battery subtype: 131 used for all entries. 

Module count: default value used

![11750](../images/foxess-h1-h3-ac1-kh-09.jpg){ width="652" height="4096" }

Notes

Last confirmed valid battery profile found: 134 (0x86) S28-H2.0
Values above 134 tested as empty/no battery profiles.

## Note on smartmeter

Note in the CHINT DDSU666 (single phase) meters with the fox. _I bought a generic meter off a UK electrical wholesaler initially as the FoxESS instructions didn’t say it had to be a Fox branded version. It read accurately on the meter, but gave rogue readings to the inverter so was inoperable. I just installed a FoxESS branded meter and it works perfectly out the box (settings 8n1, Ch01, 9600)_

![image](../images/foxess-h1-h3-ac1-kh-10.png)

![image](../images/foxess-h1-h3-ac1-kh-11.png)

## Troubleshooting

|  Problem |  Possible fix |
| :--------: | :---------: |
| Inverter stuck in "Waiting..." | Check that high voltage is present on inverter terminals, and that polarity is right way |
| Event CAN_INVERTER_MISSING active | Check that can_config is set properly for .inverter . It also might be a good idea to restart the inverter itself. It sometimes does not recover the startup routine if you have disconnected wires on the fly |
| Inverter switched off ("Switch off" on screen) / Inverter not using battery | ‘long press to activate’ on the inverter screen. Countdown will begin and inverter will start once it finishes |
| Inverter keeps losing internet/wifi connection | If you have early firmware running on an H1-G2 inverter (e.g. after a factory reset), some users have reported issues with flaky connections when using the official WiFi adaptor (also known as the datalogger). The symptom (as well as it dropping off the network) is the status light on the datalogger going from a slow blink (connected) back to rapid flashing (connecting). The solution is to use Fox ESS cloud platform to update your inverter and datalogger to newer firmware, however this cannot be achieved while Battery Emulator is connected. First disconnect the BMS port, then use the cloud platform as an installer to push firmware updates to the inverter. There are not currently any known issues running the latest Fox ESS firmware. Once you have updated you can reconnect the BMS port to Battery Emulator and your WiFi should be stable |
| Unable to force charge after inverter firmware update | Remote control has been disabled as part of an update. On the inverter, go in to Settings -> Feature -> Remote Control and select **Enable** |
| Inverter reports "Bat Volt Fault" | Can happen when voltage sags under load. Common cause is miswired high voltage lines/precharge, pulling power thru precharge resistor instead of contactors. Especially likely wiring mistake to make on Renault setups. |

## Installation examples
![alt](../images/foxess-h1-h3-ac1-kh-04.jpg)
FOX H1-6.0-E and renault zoe 26 kwh
Feel free to add your own images here!

# Video Guide
To aid installation Battery Man has produced a video series using the H3 Pro inverter which documents an install with Tesla LFP batteries and both the LilyGo and Stark CMR. There is a full playlist touching on different aspects.
![thumb for YT opt 7 FINAL](../images/foxess-h1-h3-ac1-kh-05.jpg)
Installing inverter - [youtube](https://youtu.be/9YnuPMdJaoI?si=odCptB7YAE56yFHq)
![THUMB HACK V3](../images/foxess-h1-h3-ac1-kh-06.jpg)
Work to add inverter integration - [youtube](https://youtu.be/BYqYpsv5svQ?si=oxXq-E-KLXL0grea)
[youtube](https://youtu.be/PYyTD87KQpo?si=jaSvQWiqEct-WYPS)
