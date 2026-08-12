## ESP32 DevKit V1 hardware compatible with Battery-Emulator

> [!WARNING]  
> The Devkit is for advanced users that are OK with troubleshooting wiring and complex software setups. For easy use of Battery-Emulator, consider using LilyGo or Stark CMR

The ESP32 DevKit V1 hardware can be used with Battery-Emulator, and has the following advantages:
- 25 configurable GPIO pins, allowing the following features simultaneously:
  - 2x CAN
  - 1x CANFD (or 2 BMW I3 wakeup pins)
  - Emergency Stop Button
  - Inverter enable connection
  - Inverter allows contactor closing LED
  - 3x contactor pins for negative, pre-charge and positive contactors

## Overview of features
### Power
* Power via USB
* Supply voltage (+6.5VDC - +16VDC), if used with ESP32 DevKit V1 breakout board.
> [!WARNING]  
> USB connection and simultaneous external power may not be supported. Ensure to disconnect the external power before connecting USB.
### Communication
* 1 x CAN channel using Texas Instruments SN65HVD230 breakout board
* 1 x CAN channel using Microchip Technology MCP2515 breakout board
* 1 x CAN-FD channel using Microchip Technology MCP2518FD breakout board
* 1 x RS485 using Analog Devices MAX13487E breakout board
### Status LEDs
* 1 x logic power indicator (Red)
* 1 x output status indicator (Blue: GPIO 2), used to indicate if the inverter allows contactor closing.
### Headers
* 2 x 15 pins
### Physical control / Interaction
* 1 x micro USB OR USB-C power and data connector
* 1 x `BOOT` button
* 1 x `EN` button

## Hardware connections
The pins to be used for the different breakout boards are defined in [hw_devkit.h](https://github.com/dalathegreat/Battery-Emulator/blob/ea2d57a4a557d537d23770faf848322384704b0f/Software/src/devboard/hal/hw_devkit.h#L23-L47)

## Flashing settings

Set the following options in the top of the Arduino IDE, Tools section.

![image](../images/esp32-devkit-v1-01.png)

Make sure that `HW_DEVKIT` is set in the `USER_SETTINGS.h` file.

## Where can I get one?
Google `ESP32 DevKit V1` and you should be able to find plenty of resellers.

Google `ESP32 DevKit breakout board`, to also buy the breakout board. The DevKit and breakout board can sometimes also be purchased as a set.

## References:
- Hardware documentation: [lastminuteengineers.com](https://lastminuteengineers.com/esp32-pinout-reference/)
