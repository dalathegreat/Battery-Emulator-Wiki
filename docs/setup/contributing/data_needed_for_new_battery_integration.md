---
title: "New battery integration"
---

# Introduction

This page describes the values that are used in the battery emulation SW. The values can come
from various sources, such as battery communication, data sheets, manual configuration, etc.

If you want to integrate a battery, this page will help you figure out what you need to be able to extract from the battery via CAN logs and such.

## CAN logs needed
Unless the communication protocol is already reverse engineered and available, it is usually far easier to start an integration with logs from a working vehicle. Usually, this capture will need to be completed from the powertrain bus (attached to the battery). The OBD port is most often behind a gateway that does not pass through the frames needed by the battery. Therefore, it is required to break into the harness at some point to get access to this CAN bus.

The minimum battery CAN communication logs needed to integrate a new battery are:

- CAN logs from a working vehicle
  - Vehicle idle
  - Vehicle startup
  - Vehicle charging
  - Vehicle completing charge
- CAN logs from a standalone battery

This data is typically matched to noted values "offline", such as reading the SOC in the instrument cluster to match it with the CAN data.

## Hardware for logging
You will first have to get some hardware capable of reading the communication. Here are some examples, listed from least expensive to more expensive. Do note that more expensive tools will be easier to use, since the software provided with the tools are very user friendly. Also more expensive tools will have better timing and accuracy on timestamps.

!!! tip "TIP"
    You can use the Battery-Emulator to log CAN messages. See the [CAN logging page](../can_related/can_logging.md)

    Battery-Emulator hardware, for instance a LilyGo board (can log data in testing mode!)💲 
    USBCAN PCAN clone 💲 Recommended,link: [aliexpress](https://www.aliexpress.us/item/1005006341852788.html) 
    Raspberry PI with CAN shield 💲💲
    USB2CAN Korlan 💲💲 Recommended, link: [8devices](https://www.8devices.com/products/usb2can_korlan) 
    Kvaser 💲💲💲
    Peak PCAN 💲💲💲
    Softing 💲💲💲

# Reading standalone battery
Take pictures of HV and LV connectors on the battery. Figure out the pinout with manuals found online, or behind paywalls. Add this info to wiki page for the new battery. If the wiki page for your battery does not exist yet, create a new page.

Start battery by applying 12V to it, and CAN H-L pins to a CAN reader / Battery-Emulator hardware. Note, on some batteries you might need to satisfy interlock or airbag / crash signals before they startup.

Get a CAN log of the battery in standalone operation. An example from start to finish can be seen here: [Nissan-Leaf-Battery-to-OBD2](https://github.com/dalathegreat/Nissan-Leaf-Battery-to-OBD2)

# Taking CAN logs with the Battery-Emulator (LilyGo hardware as an example)

The CAN-logging is available when using the `TEST_FAKE_BATTERY` mode. This enables easy CAN logging without expensive CAN reading hardware. When you are using this test mode, all the received CAN messages will get timestamp, ID, DLC, and data fields printed out via the Arduino IDE Serial. This can then be exported to a .txt file for later analysis. Example format:

```
7556  54A  8  10 0 70 2 0 0 0 2B 
7558  54B  8  1 8 80 12 4 0 0 0 
7560  54C  8  61 66 0 0 0 0 57 0 
7590  1DC  8  6E F 8F FD C E4 E0 D1 
7591  380  8  2 4 10 21 0 0 0 8D 
7592  5BF  8  0 0 0 0 28 0 0 1A 
7593  1D4  8  F7 7 0 0 47 46 0 BC 
```
!!! note "NOTE"
    If your serial monitor is filled with strange symbols "???!"?¤¤%" , change the baud rate in the serial monitor window from 9600 -> 115200  

# Reverse engineering values
Say you want to locate voltage from a CAN log. Read the physical value with a multimeter (370.0V), and try to find a CAN message that contains this value (0xE74)

Same with for instance temperature. If the pack is located in a 20*C environment, look for a value that has a typical -40 offset. Example, 0x3C would be decimal 60 (-40 offset) = 20*C.

Reverse engineering values is the most time consuming part of the new integration. Be prepared to spend weeks on this!

# Table of values

This table lists the typical values used. The more values available, the better. The more values
directly received from the battery, the better.

The **Source(s)** column describes the possible origins of the value.

- **Battery**: The value is extracted from battery communication
- **Manual configuration**: The value is known based on battery make/model, inverter make/model, etc
- **Estimation**: The value can be estimated based on various battery information

| Value                   | Type        | Source(s)                                     | Comment                                                                                                                  |
| ----------------------- | ----------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| SOC                     | Mandatory   | Battery                                       | State of charge. Shall be given by the battery BMS or calculated based on verified methods                               |
| DC voltage              | Mandatory   | Battery                                       | Total HV battery DC voltage                                                                                              |
| DC current              | Mandatory   | Battery                                       | HV battery DC current                                                                                                    |
| Pack max temperature    | Mandatory   | Battery                                       | HV battery max measured temperature                                                                                      |
| Pack min temperature    | Mandatory   | Battery                                       | HV battery min measured temperature                                                                                      |
| Maximum pack DC voltage | Mandatory   | Battery<br>Manual configuration               | The maximum allowed HV battery pack voltage                                                                              |
| Minimum pack DC voltage | Mandatory   | Battery<br>Manual configuration               | The minimum allowed HV battery pack voltage                                                                              |
| Pack capacity           | Mandatory   | Battery<br>Manual configuration               | Total HV battery pack capacity in kWh or similar                                                                         |
| Remaining pack capacity | Mandatory   | Battery<br>Manual configuration               | Remaining HV battery pack capacity in kWh or similar                                                                     |
| Allowed charge power    | Recommended | Battery<br>Estimation                         | The maximum allowed charge power of the HV battery. Preferably taken from battery communication, but can be estimated    |
| Allowed discharge power | Recommended | Battery<br>Estimation                         | The minimum allowed charge power of the HV battery. Preferably taken from battery communication, but can be estimated    |
| SOH                     | Optional    | Battery<br>Estimation<br>Manual configuration | State of health. Preferably taken from battery communication, but can be estimated                                       |
| Cell voltages           | Optional    | Battery                                       | Voltages of individual cells in the pack. Good for extra layers of safety and for judging the overall health of the pack |
| Number of cells         | Optional    | Battery<br>Manual configuration               | The total number of cells in the pack. Used for tracking min/max, displaying values in the web UI properly, etc          |
| Pack chemistry type     | Optional    | Battery<br>Manual configuration               | The chemistry leads to different values for min/max voltages (both pack and cell), etc                                   |

## Creating the integration
Once the mandatory info has been found for the battery communication, it can be integrated to the software. Create a battery .cpp and .h header, see the other batteries for how the structure should look like. If in doubt, contact the developers!