---
title: "Hyundai Santa Fe PHEV"
---

Information on re-using the 13.8 kWh lithium-ion polymer battery out of a 2018-Present Hyundai Santa Fe **PHEV** vehicle.

ℹ️ The pack is separated in two packs, be sure to get both pieces!

![bild](../images/hyundai-santa-fe-phev-01.png)

# Communication wiring
![bild](../images/hyundai-santa-fe-phev-02.png)

ℹ️ Note, the P-CAN and H-CAN networks need to be joined together. The Battery-Emulator needs to send messages towards both CAN buses for the battery to be able to close contactors.

Connect the following:

- P/H-CAN High -To LilyGo CAN-H
- P/H-CAN Low - To LilyGo CAN-L
- Pin 1 & 2 - To 12V supply
- Pin 3 & 14 - Short together by installing the Service Plug
- Pin 33 & 32 - To GND for 12V supply
- Pin 12 - To 12V Supply (this is the wakeup signal) 

![bild](../images/hyundai-santa-fe-phev-03.png)

## Software configuration
For this battery type, use the option called "Santa Fe PHEV" under the "Battery Protocol" setting.

![image](../images/hyundai-santa-fe-phev-04.png){ width="603" height="74" }

# Credits
Credits go to maciek16c for the CAN findings!
Massive thanks to GoSmart on the Discord for testing this!
https://github.com/maciek16c/hyundai-santa-fe-phev-battery
https://openinverter.org/forum/viewtopic.php?p=62256