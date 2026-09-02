---
title: "Installation steps"
---

## Basics 🪛

Follow the [installation guidelines](installation_guidelines.md) section for how to install and commission your battery properly.

1. Connect your Battery Emulator hardware to your EV battery
2. Connect your Battery Emulator hardware to your inverter
3. Wire up high voltage cable between the inverter and the battery
4. Add a low voltage power supply to your Battery Emulator hardware
5. Configure any additional requirements to allow Battery Emulator to switch on your EV battery (also referred to as 'closing contactors')
6. Enjoy a big cheap grid connected battery!

For examples showing wiring, see each battery type's own Wiki page. For instance the [Nissan LEAF page](../battery/nissan_leaf_e_nv200.md).

## How to install the software 💻

Start by watching this [quickstart video guide](https://www.youtube.com/watch?v=sR3t7j0R9Z0)

1. Open the [webinstaller page](installer.md)
2. Follow the instructions on that page to install the software
3. After successful installation, connect to the wireless AP (`battery-emulator-....` , default password: `123456789`)
4. In the settings, connect it to your local wireless network
5. Configure your Inverter/Battery component selection
7. Read on how to connect your battery and inverter to the board and you are done! 🔋⚡

## Dependencies 📖

This code uses the following excellent libraries: 

- [adafruit/Adafruit_NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel) LGPL-3.0 license
- [ayushsharma82/ElegantOTA](https://github.com/ayushsharma82/ElegantOTA) AGPL-3.0 license 
- [bblanchon/ArduinoJson](https://github.com/bblanchon/ArduinoJson) MIT-License
- [eModbus/eModbus](https://github.com/eModbus/eModbus) MIT-License
- [ESP32Async/AsyncTCP](https://github.com/ESP32Async/AsyncTCP) LGPL-3.0 license
- [ESP32Async/ESPAsyncWebServer](https://github.com/ESP32Async/ESPAsyncWebServer) LGPL-3.0 license
- [pierremolinaro/acan-esp32](https://github.com/pierremolinaro/acan-esp32) MIT-License
- [pierremolinaro/acan2517FD](https://github.com/pierremolinaro/acan2517FD) MIT-License

It is also based on the information found in the following excellent repositories/websites:

- [gitlab/pelle8](https://gitlab.com/pelle8/inverter_resources) //new url
- [github/burra](https://github.com/burra/byd_battery)
- [github/flodorn](https://github.com/flodorn/TeslaBMSV2)
- [github/SunshadeCorp](https://github.com/SunshadeCorp/can-service)
- [github/openvehicles](https://github.com/openvehicles/Open-Vehicle-Monitoring-System-3)
- [leaf_can_bus_messages](https://github.com/dalathegreat/leaf_can_bus_messages)
- [github/rand12345](https://github.com/rand12345/solax_can_bus)
- [github/Tom-evnut](https://github.com/Tom-evnut/BMWI3BMS/) SMA-CAN
- [github/FozzieUK](https://github.com/FozzieUK/FoxESS-Canbus-Protocol) FoxESS-CAN
- [github/maciek16c](https://github.com/maciek16c/hyundai-santa-fe-phev-battery)
- [github/ljames28](https://github.com/ljames28/Renault-Zoe-PH2-ZE50-Canbus-LBC-Information)
- Renault Zoe CAN Matrix [google](https://docs.google.com/spreadsheets/u/0/d/1Qnk-yzzcPiMArO-QDzO4a8ptAS2Sa4HhVu441zBzlpM/edit?pli=1#gid=0)
- Pylon hacking [eevblog](https://www.eevblog.com/forum/programming/pylontech-sc0500-protocol-hacking/)
