---
title: "Batrium BMS"
---

## Read this first

Preface, the entire Battery-Emulator project sets out to achieve safe re-use of EV batteries. By building your own battery, you will be taking larger risks. Cell balancing wire taps, shunts, busbar connections, BMS integration, temperature monitoring, fuses, contactors, interlocks, etc. all will have to be implemented by yourself instead of using a pre-made product. As with all things custom, there are higher risks of human error. Take extra precaution when working on a custom DIY HV battery, you have been warned.

!!! warning "CAUTION"
    If you are unsure of your technical knowhow, avoid building a high voltage battery from scratch.

## Custom DIY battery with Batrium BMS

Start by connecting the CAN port of the BMS, to the CAN port on the Battery-Emulator. Refer to the "How to Wire Up and
Configure the CANbus Network" document which is available from Batrium. In short, the settings on the Batrium should be set to Base Address 0x500 , and the protocol mode should be set to Native 2.0

![image](../images/batrium-bms-01.png)
