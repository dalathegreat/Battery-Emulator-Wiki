---
title: "Waveshare ESP32‐S3‐RS485‐CAN"
---

**MCU / flash:** ESP32-S3 R8 (Xtensa LX7 dual-core, 240 MHz) with 8 MB octal/OPI PSRAM, 16 MB flash. 

The Waveshare ESP32-S3-RS485-CAN is an affordable and easy to source board. It supports 1x CAN channel, and 1x RS485 port. It comes with a DIN mountable case, and accepts an input voltage between 7-36V.

![image](../images/waveshare-esp32-s3-rs485-can-01.png)

### Where this hardware shines

On setups that require RS485, and have CAN controlled contactors (E.g. Tesla Battery with a Fronius inverter), it's a plug and play solution. This board is a more future proof alternative compared to the [LilyGo T-CAN485](lilygo_t_can485.md).

| GPIO | Function |
|---|---|
| 0 | BOOT button — [long-press options available](../setup/software/contactor_control_via_gpio_pins.md) |
| 1 | I2C display SDA (Configurable port = I2C Display SSD1306) |
| 2 | [Status LED](index.md#status-led-) (default) — or I2C display SCL (I2C Display SSD1306) |
| 3 | Positive [contactor output](../setup/software/contactor_control_via_gpio_pins.md) — or inverter disconnect [contactor output](../setup/software/contactor_control_via_gpio_pins.md) |
| 4 | Negative [contactor output](../setup/software/contactor_control_via_gpio_pins.md) |
| 5 | Precharge [contactor output](../setup/software/contactor_control_via_gpio_pins.md) — or [HIA4V1 precharge control](../setup/hardware/high_voltage_source.md#option-b-hia4v1) |
| 6 | [BMS Power](../setup/hardware/periodic_bms_reset.md) output; held at its driven level across a firmware-initiated reset/OTA reboot |
| 7 | [Equipment stop](../setup/software/equipment_stop.md) input |
| 8 | [Second battery](../setup/software/battery_2x.md) contactors output — or battery wake-up 1 (WUP1) |
| 9 | SMA inverter contactor enable input — or battery wake-up 2 (WUP2) |
| 10 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SCK |
| 11 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SDI |
| 12 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: SDO |
| 13 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: CS |
| 14 | [MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) CAN FD add-on: INT |
| 15 | Native CAN TX |
| 16 | Native CAN RX |
| 17 | RS485 TX |
| 18 | RS485 RX |
| 21 | RS485 direction control (SP3485 DE and /RE tied together, HIGH = transmit) |

## Purchase link

The hardware can be bought via sites like Amazon, AliExpress, or the official [Waveshare](https://www.waveshare.com/esp32-s3-rs485-can.htm) shop.

## Limitations

As can be seen from the pin mapping table above, this board has a single CAN channel and single RS485 port. The 4-pin SH1.0 connector on the board exposes GPIO1 and GPIO2, which can be configured in firmware settings as either a status LED or an I2C display (see below).

Internal header exposes pins to be used for GPIO controlled contactors and an additional CAN interface.

!!! info "IMPORTANT"
    You can build a maximum [double battery](../setup/software/battery_2x.md) setup with this unit when used with an RS485 inverter, using its onboard CAN and a [second CAN interface](../setup/can_related/can_fd_add_on_mcp2518fd.md), as this will mostly max out the available GPIOs on the internal pin header. No way to add a third CAN interface to this board.

A Waveshare ESP32-S3-RS485-CAN with a [second CAN interface](../setup/can_related/can_fd_add_on_mcp2518fd.md) and external contactors control for a [double battery](../setup/software/battery_2x.md) setup:

![image](../images/waveshare-esp32-s3-rs485-can-07.png)

The plastic case has a bit of a headroom above the USB-C socket which allows for a small cutout to lead the cables from the header:

![image](../images/waveshare-esp32-s3-rs485-can-05.png)

![image](../images/waveshare-esp32-s3-rs485-can-06.png)

## Optional accessories

### Expansion header

The board has pads for a 20-pin **2.0mm** pitch pin header:

![image](../images/waveshare-esp32-s3-rs485-can-04.png){ width="551" height="449" }

Socket for own soldering: [AliExpress](https://www.aliexpress.com/item/4000597517515.html), 
Pigtail cable: [AliExpress](https://www.aliexpress.com/item/1005009728347159.html).

Choose the **2x10p** version!

### Status LED (NeoPixel via GPIO2)

The 4-pin SH1.0 connector (located directly behind the USB C connector) can power an optional **Adafruit NeoPixel** (or any WS2812-compatible single LED) connected to GPIO2, providing a visual status indicator.  Please note that the Waveshare only outputs 3.3v!

![Waveshare to NeoPixel wiring diagram](../images/waveshare-esp32-s3-rs485-can-02.png){ width="800" height="599" }

Once wired, open the **Settings** page in the web interface and set **GPIO 1/2 function** to **Status LED** (this is the default).

![Waveshare_settings](../images/waveshare-esp32-s3-rs485-can-03.png){ width="792" height="374" }

### I2C Display (SSD1306 via GPIO1 + GPIO2)

The same connector can alternatively drive an **SSD1306 128×64 I2C OLED display**, using GPIO1 as SDA and GPIO2 as SCL.

In the **Settings** page, set **GPIO 1/2 function** to **I2C Display (SSD1306)** to enable this.

!!! note "NOTE"
    The status LED and I2C display are mutually exclusive — only one can be active at a time.

### See also

- [BOOT button](../setup/software/boot_button_functions.md) for special features to enable AP, wipe wifi settings or factory reset the device
- [CAN add-on MCP2518FD](../setup/can_related/can_fd_add_on_mcp2518fd.md) for an additional CAN interface

