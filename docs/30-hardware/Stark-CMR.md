### What is this?
The Stark CMR (SCMR) is the only commercially available and CE certified product specifically designed for the Battery Emulator project. It aims to make installs clean, easy, expandable and electrician friendly.<br>Get the SCMR and other related hardware via the official [web shop](https://shop.redispo.se/).

![SCMR02](../images/stark-cmr-02.jpg){ width="400px" }![SCMR01](../images/stark-cmr-03.jpg){ width="400px" }<br>

## Overview of features
### Power
Supply voltage (+5VDC - +16VDC) protected with reverse polarity circuitry<br/>
Operating current < 300mA @ 3,3VDC when all outputs are activated<br/>
Simultaneous USB connection and external power supply supported<br/>
All 3V3 logic with resettable over-current protection<br/>
Four individually controllable power outputs, equal to the DC input voltage consisting of:<br/>
* 1 relay channel, 7A continuous, 12A maximum. Located on the main output 1 connector.
* 3 MOSFET channels, 0,65A continuous, 1,4A maximum with resettable over-current protection.<br/><br/>
The MOSFET channels are located on the secondary output connector.<br/>
Current specifications are valid at a surrounding temperature of 25°C or below.<br/>
### Communication
* 1 x RS485 channel using Texas Instruments transceiver
* 1 x CAN channel using Texas Instruments transceiver
* 1 x CAN/CAN-FD channel using Microchip technology MCP2518FD controller and Texas Instruments transceiver<br/><br/>
All of the above protected using GDT/ESD/TVS discrete components<br/>
Easily accessible DIP switches for termination on all three lines<br/>
### SoC
ESP32-WROOM-32E using ESP32-D0WDR2-V3<br/>
Xtensa® dual-core 32-bit LX6 microprocessor, up to 240 MHz<br/>
448 KB ROM, 520 KB SRAM, 16 KB SRAM in RTC<br/>
Equipped with 8MB Flash and 2MB PSRAM<br/>
### Status LEDs
* 1 x logic power indicator (Blue)<br/>
* 4 x outputs status indicators (Green: GPIO 25, Yellow: GPIO 33, Orange: GPIO 32, Red: GPIO 23)<br/>
* 1 x programmable REG WS2812B (GPIO 4)<br/><br/>
All except power indicator available on board as well as on perpendicular plug-in PCB for better visibility<br/>
### Extra headers
7 available GPIOs (5 freely usable, 1 bootstrapped, 1 conditioned)<br/>
SPI/JTAG header (or used as part of the 6 GPIOs)<br/>
Maximum current per GPIO must not exceed 20mA<br/>
### Physical control / Interaction
* 1 x USB-C power and data connector<br/>
* 3 x DIP-switches toggling individual termination resistors for RS585, CAN and CAN/CAN-FD<br/>
* 2 x Momentary switches for SoC manual reset and flash (GPIO-0 to GND) functions<br/>
* 1 x JTAG header<br/>

### Where can I get one?
Additional information on the Stark CMR and upcoming related products is available at [shop.redispo.se](https://shop.redispo.se/) where you also have the option to buy the unit<br/>
On the [project discord](https://www.patreon.com/c/dala) you'll find a thread called "Stark Hardware" where you can chat to Stark CMR users.<br/>
You're also welcome to contact [Johan](mailto:info@redispose.se) directly if you have any questions regarding the hardware.

### Documents
[Latest instruction manual SCMR01](https://redispose.se/documents/latest.php?type=SCMR01)

[Latest instruction manual SCMR02](https://redispose.se/documents/latest.php?type=SCMR02)

## Installing the software
Follow the [quickstart guide](https://github.com/dalathegreat/Battery-Emulator?tab=readme-ov-file#how-to-install-the-software-) to install the Battery-Emulator software onto the board for the initial setup

## Over the air (OTA) software updates
When updating this board [OTA](../40-setup/20-software/OTA-Update.md), be sure to select the software marked for this board. The files will be marked like this, signaling that this is **Stark** hardware

`BE_vX.Y.Z_StarkCMR.ota.bin`

## Interfaces
The board comes with 2 CAN channels, the second one of them being capable of CAN-FD. The board also has an RS485 channel, which can be used for Modbus inverters or RS485 batteries.

![image](../images/stark-cmr-04.png){ width="377" height="243" }

The interfaces correspond to the following options in the Battery-Emulator software

- CAN-1 -> **Native CAN**
   - CAN 1L (CAN-LOW)
   - CAN 1H (CAN-HIGH)
- CAN-2 -> **Native CAN FD**
   - CAN 2L (CAN-LOW)
   - CAN 2H (CAN-HIGH)
   - Note, this channel can be used as classic CAN by enabling "Use CanFD as classic CAN" option
- RS485 -> **RS485 / Modbus**
   - RS485 A
   - RS485 B

### Adding a third CAN channel
For integrations that need double/triple battery support via CAN, or an additional CAN-FD chanel, you can add an MCP251**8FD** add-on board via the GPIO expansion header. Connect the wires as following:

- IMT to 14
- CS to 12
- SCK to 17
- MISO to 34
- MOSI to 5
- 3.3V to 3.3V
- 5V to 5V
- GND to GND

![image](../images/stark-cmr-05.png){ width="458" height="291" }

After connecting the board, you can enable the add-on CAN by configuring it as **MCP2518FD (GPIO add-on)** to component

Example, Stark CMR used to control 3x separate Nissan LEAF batteries with one of them being on an add-on MCP2518FD board

![image](../images/stark-cmr-06.png){ width="413" height="470" }


## Example connection diagram
This is an example wiring diagram for connecting the Stark CRM, a Nissan Leaf battery pack, a Fronius inverter and an E-stop button (NC). This diagram shows _high side_ switching contactors which is found in most battery packs. I.e. +12V is "fed into" the battery on the dedicated pins to close the contactors.

![68747470733a2f2f7265646973706f73652e73652f696d6167652f636174616c6f672f73636d725f776972696e675f6c6561665f66726f2e706e67](../images/stark-cmr-07.png)

_Notes: All connections marked GND on the SCMR are joined via the GND plane of the PCB. 5V is the suggested voltage level for the E-stop in this case but it will also work using 12V or 3.3V._

The configuration for the above example would look like this:

![491962914-521d84d1-ed0a-47f9-ba9c-b26f861f1497](../images/stark-cmr-08.png){ width="534" height="887" }


The next wiring diagram shows an example for wiring a Renault Zoe battery. This differs from the previous example as the contactors use _low side_ switching, i.e. the contactors will be closed when the dedicated pins from the contactors on the battery are "shorted to ground". 
![image](../images/stark-cmr-01.png)

### Boot button 
The BOOT button has [special features to enable AP, wipe wifi settings or factory reset the device](../40-setup/20-software/BOOT-button-functions.md)

