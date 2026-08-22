---
title: "Emulator Hardware"
hide:
  - toc
---

# Compatible Emulator Hardware

There are many hardware kits that can run the Battery-Emulator software. Cheap option is the "LilyGo T-2CAN" (2x CAN). For those that need more reliable and certifiable hardware, the "Stark CMR" is highly recommended. Amount of stars ⭐ signal how easy to use the hardware is for a newcomer:

|  Product | Notes | CAN interfaces | Newcomer friendly |
| :---------: | :---------: | :----------: | :----------: |
| [Stark CMR Module](stark_cmr.md) | Professional HW, CE certified, Massive I/O, DIN rail mount | 2 (+ 1 add-on) | ⭐⭐⭐
| [BECom](becom.md) | Open source triple-CAN and RS485 (fully isolated), DIN rail mount | 3 | ⭐⭐⭐
| [LilyGo T-2CAN](lilygo_t_2can.md) | Dual isolated CAN | 2 (+ 1 add-on) | ⭐⭐⭐
| [LilyGo T-2CANFD](lilygo_t_2can.md) | Isolated CAN & Isolated CAN-FD | 2 (+ 1 add-on) | ⭐⭐⭐
| [Waveshare ESP32-S3-RS485-CAN](waveshare_esp32_s3_rs485_can.md) | CAN & Modbus, DIN rail mount | 1 (+ 1 add-on) | ⭐⭐
| [DFRobot Edge101](dfrobot_edge101.md) | CAN & Modbus, metal enclosure, Massive I/O, DIN rail mount | 1 | ⭐⭐
| [3LB](https://github.com/malcolmputer/3lb) | Open source triple-CAN (fully isolated) | 3 (+ ? add-on) | ⚠️
| [LilyGo T-CAN485](lilygo_t_can485.md)   | CAN & Modbus! | 1 (+ 1 add-on) | ⭐
| [ESP32 Devkit V1](esp32_devkit_v1.md) | Build your own! For expert tinkerers | | ⭐

!!! note "NOTE"
    There is no way to purchase a pre-programmed device. This is a hobbyist open source project. You will be responsible for loading the software and setting it up correctly for your components. There is however a [support Discord group](https://www.patreon.com/dala) available.

## Status LED 🟢

Some boards has a built in LED that is used to signal current status. Most boards expose a GPIO pin where you can attach your own WS2812-compatible pixel you can cut off a LED strip. With this feature, it is easy to at a glance catch what info the board is getting. It will show the current colors:

* Pulses 🟢 if all is well and BMS is active
* Pulses 🟡 if battery has entered a warning state
* Solid 🔴 if battery goes into a fault state
* Pulses ⚪ when the BOOT button has [been long pressed for various tasks](../setup/software/boot_button_functions.md)

By visiting the "Events" page in the Webserver, you can see which specific warnings/faults are active.

## Connectivity 🛜

The board has wifi, and supports running a [Webserver that you can connect to for real time values](../setup/software/webserver_guide.md), [Over The Air updates](../setup/software/ota_update.md) (OTA), cellmonitoring, changing settings and more. See the [Webserver](../setup/software/webserver_guide.md) page for more info on how to use the system.

For those into home automation, the code is also compatible with [MQTT](../setup/software/mqtt.md) 

## Optional screen via ESPNow 🖥️
No Battery-Emulator hardware comes with displays by default. If you want to add a local display to your system, the best option is to add a [ESPNow](../setup/software/espnow.md/) compatible microcontroller, which will wirelessly connect to the Battery-Emulator board and display statistics.
