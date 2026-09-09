---
title: "DFRobot Edge101"
---

**MCU / flash:** ESP32-WROOM-32E (Xtensa LX6 dual-core, 240 MHz), 16 MB flash, 520 KB SRAM, no PSRAM.

The DFRobot Edge101 is a rugged board, with the following features.

- Isolated CAN
- Isolated RS485
- Ethernet (Will become compatible in later BE releases)
- External Wifi antenna
- PCIe expansion slot with UART
- Case with DIN Rail mount (that fits perfectly inside of a Fronius Verto)
- External IO header (where you could attach an external MCP2518FD - not supported yet)
- SD Card slot
- 16MB Flash

![image](../images/dfrobot-edge101-01.png){ width="337" height="461" }

| GPIO | Function |
|---|---|
| 5 | SD card CS |
| 12 | SD card MOSI |
| 14 | SD card SCLK |
| 15 | User LED |
| 16 | RS485 direction control (TPT75176H DE and /RE tied together) |
| 17 | RS485 TX |
| 32 | Native CAN TX (isolated TJA1050) |
| 35 | Native CAN RX (isolated TJA1050) |
| 36 | RS485 RX |
| 38 | User button — [long-press options available](../setup/software/contactor_control_via_gpio_pins.md) (input-only pin, external pull-up on the board, no resistors needed) |
| 39 | SD card MISO |

!!! note "NOTE"
    This board defines no contactor, precharge, [BMS Power](../setup/hardware/periodic_bms_reset.md), [Equipment stop](../setup/software/equipment_stop.md) or wake-up pins yet.

![dfrobot101_verto](../images/dfrobot-edge101-02.jpg){ height="461" }

## Purchase link
The hardware can be bought via sites like AliExpress, the [official store](https://www.dfrobot.com/product-2934.html) and [various distributors](https://octopart.com/de/part/dfrobot/DFR0886)
