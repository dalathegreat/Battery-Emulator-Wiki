---
title: "CAN logging"
---

## CAN logging basics
The board can operate as a CAN logger, skipping the need for purchasing an expensive tool. There are three ways to log CAN messages, via USB (more reliable), via [Webserver](../software/webserver_guide.md) (easiest), and via SD-CARD (requires LilyGo)

### Logging a live vehicle :warning: 
If you intend to log CAN messages from a functional vehicle, remember to:

* Use Battery protocol: "Test Fake Battery" to avoid any CAN messages being sent towards the vehicle
* Use Inverter/Shunt protocol: "None" to avoid any CAN messages being sent towards the vehicle
* Remove any termination resistors from the board (Either remove jumper on Stark, or desolder on LilyGo)

## CAN logging via Webserver

!!! note "NOTE"
    CAN logging via Webserver does not store all messages due to limited RAM. If you need to log absolutely everything, do it via USB or to SD-CARD.

!!! note "NOTE"
    Some mobile phone browsers can have issues displaying long data lists. If you see no data, try using a Desktop PC / Laptop.

Start by accessing the [Webserver](../software/webserver_guide.md)

On the main page, there is a button named "CAN logger" .When opened, the system starts logging CAN messages. This is disabled by default to not disturb the system.

![image](../../images/can-logging-01.png)

Refresh the page to get an updated list of incoming (RX) and sent (TX) CAN messages.

![image](../../images/can-logging-02.png)

Press the "Export to .txt" button to save the CAN log into a SavvyCAN compatible CANdump format, for further analysis.

## USB CAN logging

![image](../../images/can-logging-03.png){ width="482" height="186" }

To access the CAN-logging, enable the `Enable CAN message logging via USB serial:` feature. When this is enabled, all the incoming/outgoing CAN&CAN-FD messages will get timestamp, direction, ID, DLC, and data fields printed out via the Arduino IDE serial monitor. This can then be exported to a .txt file for later analysis.

Alternatively, a much better way to log the data is via Putty. Connect to the COM port and set baud rate, and configure Putty to save the output to a file [putty](https://www.putty.org/)

##Log file format
The log file format is compatible with the CANdump format. This can be read natively by tools like [SavvyCAN](https://github.com/collin80/SavvyCAN). 

TX1 / RX0 = Native CAN port
TX3 / RX2 = Native CANFD port
TX5 / RX4 = Add-on CAN MCP2515
TX5 / RX4 = Add-on CAN-FD MCP2518

Example format, CAN log:

```
(7.556) TX1 54A [8] 10 0 70 2 0 0 0 2B 
(7.558) TX1 54B [8] 1 8 80 12 4 0 0 0 
(7.560) TX1 54C [8] 61 66 0 0 0 0 57 0 
(7.561) TX1 1D4 [8] F7 7 0 0 7 46 0 7B 
(7.573) TX1 11A [8] 1 40 0 AA C0 0 0 3 
```
Example format, CAN-FD log:
```
(64.644) TX3 10A [32] D8 DE 99 00 00 00 00 01 FF 01 00 00 36 39 35 35 C9 02 00 00 10 00 00 35 00 00 0A 00 00 00 00 00  
(64.656) TX3 120 [32] 6E F3 99 00 00 00 00 01 FF 01 00 00 37 35 37 37 C9 02 00 00 00 00 00 35 00 00 0A 00 00 00 00 00 
(64.668) TX3 19A [32] 19 48 88 55 44 64 D8 1B 40 20 00 00 00 00 11 52 00 12 02 64 00 00 00 08 13 00 00 00 00 32 00 00 
(64.669) TX3 10A [32] 12 35 9A 00 00 00 00 01 FF 01 00 00 36 39 35 35 C9 02 00 00 10 00 00 35 00 00 0A 00 00 00 00 00 
(64.681) TX3 120 [32] A4 18 9A 00 00 00 00 01 FF 01 00 00 37 35 37 37 C9 02 00 00 00 00 00 35 00 00 0A 00 00 00 00 00 
```

!!! note "NOTE"
    If your serial monitor is filled with strange symbols "???!"?¤¤%" , change the baud rate in the serial monitor window from 9600 -> 115200  
    When a large amount of CAN traffic is present on the bus, you may need to increase the serial monitor baud rate to 460800 in Software.ino (  by changing Serial.begin(115200); to Serial.begin(460800); ) of course the serial baud rate of the serial monitor then also needs to be increased to 460800.

## SD card CAN logging

To enable logging of CAN messages to an SD card enable the `Enable CAN message logging via SD card: ` feature. To maximize performance you should not enable other debug features at the same time as it could lead to CAN messages not being logged. The format of the log file is the same as the USB can log feature and can be read by tools like Savvy CAN directly.

![image](../../images/can-logging-04.png){ width="471" height="87" }

If you have debug logging enabled and there are too many messages on the CAN bus to write to the SD card the error `Failed to send message to can ring buffer!` will be logged.

Once enabled the `CAN logger` button will be enabled on the webserver, no data will be shown on the website, instead the CAN log file can be downloaded by clicking on the `Export to .txt` button which will download the file from the battery emulator. You can also delete the CAN log file by clicking on the `Delete log file` button. For very large captures it may be quicker to remove the SD card and plug it into a PC directly.

The SD card must be formatted using the FAT file system, if you are using an SD card larger than 32GB you will need to partition the card otherwise exFAT will be used which the ESP32 does not support.
The best tool to use for formatting of the SD card is [SD Card Formatter](https://www.sdcard.org/downloads/formatter/)

On startup the SD card is checked and if you have debug logging enabled a message will be output showing success or failure.

Success Example
```
SD Card initialization successful.
SD Card Type: SDHC
SD Card Size: 61183 MB
Total space: 7984 MB
Used space: 2MB
```

Failure Example
```
sdmmc_init_ocr: send_op_cond (1) returned 0,107
vfs_fat_sdmmc: sdmmc_card_init failed ()x107).
Failed to initialize the card (0x107). Make sure SD_card lines have pull-up resistors in place.
SD Card initialization failed!
```

If you get the SD Card initialization error you may need to remove power to the board for a couple of seconds to reset it. Simply rebooting the emulator or even using OTA or reflashing will not fix it.

Also try another SD card, and make sure it is not locked. Also make sure it is seated OK, and formatted as FAT32

## Interpreting the CAN logs
The log files stored by the Battery-Emulator is in a format that [SavvyCAN](https://github.com/collin80/SavvyCAN) can interpret. This program can also be connected to a translation .DBC file for an even easier interpretation of the log.