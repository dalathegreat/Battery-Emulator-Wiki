---
title: "ESP32 DevKit V1"
---

## ESP32 DevKit V1 hardware compatible with Battery-Emulator

**MCU / flash:** ESP32-D0WDQ6 (Xtensa LX6 dual-core, 240 MHz), 4 MB flash, no PSRAM.

!!! note "NOTE"
    The Devkit is for advanced users that are OK with troubleshooting wiring and complex software setups. For easy use of Battery-Emulator, consider using a ready-made board.

The ESP32 DevKit V1 hardware can be used with Battery-Emulator, and has the following features:

- 25 configurable GPIO pins, allowing the following features simultaneously:
    - 2x CAN
    - 1x CANFD (or 2 BMW I3 wakeup pins)
    - Emergency Stop Button
    - Inverter enable connection
    - Inverter allows contactor closing LED
    - 3x contactor pins for negative, pre-charge and positive contactors

| GPIO | Function |
|---|---|
| 0 | BOOT button — [long-press options available](../setup/software/boot_button_functions.md) |
| 1 | RS485 TX (UART0, shared with the USB serial console) |
| 2 | SMA inverter "contactor allowed" indicator LED output |
| 3 | RS485 RX (UART0, shared with the USB serial console) |
| 4 | [Status LED](index.md#status-led-) (addressable) — or [HIA4V1 precharge control](../setup/hardware/high_voltage_source.md#option-b-hia4v1) output when automatic precharging is used |
| 5 | Positive [contactor output](../setup/software/contactor_control_via_gpio_pins.md) — or inverter disconnect [contactor output](../setup/software/contactor_control_via_gpio_pins.md) when automatic precharging is used |
| 12 | [Equipment stop](../setup/software/equipment_stop.md) input |
| 14 | SMA inverter contactor enable input |
| 16 | Negative [contactor output](../setup/software/contactor_control_via_gpio_pins.md) |
| 17 | Precharge [contactor output](../setup/software/contactor_control_via_gpio_pins.md) |
| 18 | MCP2515 CAN add-on: CS |
| 19 | MCP2515 CAN add-on: MISO (SDO) |
| 21 | MCP2515 CAN add-on: MOSI (SDI) |
| 22 | MCP2515 CAN add-on: SCK |
| 23 | MCP2515 CAN add-on: INT |
| 25 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: CS — or battery wake-up 1 (WUP1) |
| 26 | Native CAN RX |
| 27 | Native CAN TX |
| 32 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SDI — or [second battery](../setup/software/battery_2x.md) contactors output — or battery wake-up 2 (WUP2) |
| 33 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SCK |
| 34 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: INT |
| 35 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SDO |

!!! note "NOTE"
    The MCP2515/MCP2517 pins are defined in the HAL, but `available_interfaces()` for this board offers only Modbus, RS485 and native CAN, so the add-on interfaces cannot currently be selected in the UI.

## Overview of features

### Power

* Power via USB
* Supply voltage (+6.5VDC - +16VDC), if used with ESP32 DevKit V1 breakout board.

!!! warning "WARNING"
    USB connection and simultaneous external power are not be compatible. Ensure to disconnect the external power before connecting USB.

### Communication

* 1 x CAN channel using Texas Instruments SN65HVD230 breakout board
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

## Where can I get one?

Google `ESP32 DevKit V1` and you should be able to find plenty of resellers.

Google `ESP32 DevKit breakout board`, to also buy the breakout board. The DevKit and breakout board can sometimes also be purchased as a set.

## See also

- [BOOT button](../setup/software/boot_button_functions.md) for special features to enable AP, wipe wifi settings or factory reset the device
- Hardware documentation: [lastminuteengineers.com](https://lastminuteengineers.com/esp32-pinout-reference/)
