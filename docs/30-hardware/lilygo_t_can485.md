---
title: "LilyGo T‐CAN485"
---

## Hardware basics
The LilyGo T-CAN485 is what the Battery-Emulator originally started development with. It is a very cheap microcontroller, that runs the entire project easily. It has 1x CAN, 1x RS485, and GPIO pins for expansion.

!!! tip "TIP"
    Only get this board if you need Modbus/RS485. For CAN components, the new [T-2CAN](lilygo_t_2can.md) board is easier for beginners.

![image](../images/lilygo-t-can485-02.png)

!!! warning "WARNING"
    This board has limited memory. Starting from 2027, it might not get new integrations added to it. All other hardware choices are better suited for those seeking new feature development and new integrations

## Purchase link
The hardware can be bought via sites like [AliExpress](https://www.aliexpress.com/item/1005003624034092.html)

## Hardware info
The hardware has more details on LilyGo's Github page
https://github.com/Xinyuan-LilyGO/T-CAN485

## Expanding the board
The board comes with 1x CAN channel, and 1x RS485 channel. Some integrations need more than 1 channel, in these cases the LilyGo can be extended with add-on CAN channels:

- [CAN add‐on](../40-setup/40-can-related/can_add_on_mcp2515.md)
- [CAN-FD add on](../40-setup/40-can-related/can_fd_add_on_mcp2518fd.md)

Example, LilyGo + MCP2515 board

![image](../images/lilygo-t-can485-03.png)

### Expanding the board with more IO pins
The SD card slot can be used to gain more pins. This can be useful on setups that need lots of inputs/outputs, for instance add-on CAN + contactor control and/or enable line inputs. To use the SD card slot, you will need a "SD Card breakout board"

![image](../images/lilygo-t-can485-04.png)

By installing one of these breakout boards, you can then remap the src/devboard/hal/hw_lilygo.h file to suit your newfound pins

- GPIO_NUM_2 corresponds to DAT0  (SD_MISO)
- GPIO_NUM_13 corresponds to DAT3 (SD_CS)
- GPIO_NUM_14 corresponds to CLK  (SD_SCLK)
- GPIO_NUM_15 corresponds to CMD  (SD_MOSI)

Completed product:

![image](../images/lilygo-t-can485-05.png)

### Expanding the board further
To make the board even more professional (DIN mounting solution with CANFD and contactor drivers built in), you can get the [LilyGo T‐CAN485 & CAN‐FD Motherboard](lilygo_t_can485_and_can_fd_motherboard.md)

![image](../images/lilygo-t-can485-06.png)

## Enhancements notes, things to know
The chip has the tendacy to run quite hot. Some people book good results by adding a RAM or Raspberry Pi heatsinks on the chip, reducint the heat.
Above 80 degrees the BE screen turns yellow as a warning, and above 95 degrees damage is possible.
Take this into consideration when building enclosures for it.
If the situation is crifical (hot and direct sun), you can use a [Peltier element with fan](https://s.click.aliexpress.com/e/_c4LFUPAt).

There are several enclosure designs that can be 3D printed, so it can be mounted on a DIN rail.
https://www.thingiverse.com/thing:6788996
https://www.thingiverse.com/thing:7029497

The lilygo has an internal voltage regulator, and input is rated at 5-12 volts. 
Not all lilygos actually work on 5V. A higher input is needed often. 
Some report issues above 12 volts, other run boards fine at 14.4 volts. It is not yet determined what causes these variations.

If the controller is not outside (under 0C temperature), it is recommended to use a PSU like [DC1036P](https://www.aliexpress.com/w/wholesale-DC1036P.html) or Well DC-HALE36-WL (36W).
If it is outside, in the cold, use a 12V source like [**HDR-60-12**](https://www.meanwell.com/Upload/PDF/HDR-60/HDR-60-SPEC.PDF) and a 12V AGM battery.

![HDR-60-12](../images/lilygo-t-can485-01.jpg)

### Boot button 
The BOOT button has [special features to enable AP, wipe wifi settings or factory reset the device](../40-setup/20-software/boot_button_functions.md)

