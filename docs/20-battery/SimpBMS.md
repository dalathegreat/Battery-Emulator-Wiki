## Read this first

Preface, the entire Battery-Emulator project sets out to achieve safe re-use of EV batteries. By building your own battery, you will be taking larger risks. Cell balancing wire taps, shunts, busbar connections, BMS integration, temperature monitoring, fuses, contactors, interlocks, etc. all will have to be implemented by yourself instead of using a pre-made product. As with all things custom, there are higher risks of human error. This page covers emulating High Voltage protocols, so while most tinkerers might be familiar with 48V DIY batteries, building a 96S 400VDC battery is an entirely different beast that can be lethal. Take extra precaution when working on a custom DIY HV battery, you have been warned.

!!! warning "CAUTION"
    If you are unsure of your technical knowhow, avoid building a high voltage battery from scratch

## Custom DIY battery with SimpBMS

The SimpBMS is an open source (software) BMS for reusing various EV battery modules in a custom pack, instead of using the OEM BMS, for example if you want to use fewer/more modules than the OEM battery had.

There's some instructions here https://github.com/Tom-evnut/SimpBMS and there's support for the BMW PHEV modules, VW PHEV and ID modules, Tesla modules, Outlander PHEV modules etc.

### Where do I get the hardware?

https://evshop.eu/en/bms/280-simp-bms-battery-management-system.html still seem to have stock, but the original hardware isn't readily available any more. It has been ported to newer Teensy boards and also ESP32, some of which are open source.

## Setting up the BMS

****Attention!**** Different SimpBMS clones have different pin layouts in the RJ45 connector. In the original schematic, CAN is on pins 7 and 8, while pins 3, 4, and 1, 2 are 12V. However, I have a clone where CAN is on pins 1 and 2. As a result, you can easily burn the CAN chip if you connect it incorrectly!

Also be aware to enter the settings and setup correctly for you pack. The setting _pack end of charge current_ should be set to 0 when used for static storage or else the BMS will report the value as the allowed charge current even when full.

## Software configuration
For this battery type, use the option called "SIMPBMS battery" under the "Battery Protocol" setting

<img width="666" height="266" alt="image" src="../images/simpbms-01.png" />

Also remember to configure all cellvoltage limits and pack design voltage limits according to your battery build
