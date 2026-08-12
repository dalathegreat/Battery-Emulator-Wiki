> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Read this first

Preface, the entire Battery-Emulator project sets out to achieve safe re-use of EV batteries. By building your own battery, you will be taking larger risks. Cell balancing wire taps, shunts, busbar connections, BMS integration, temperature monitoring, fuses, contactors, interlocks, etc. all will have to be implemented by yourself instead of using a pre-made product. As with all things custom, there are higher risks of human error. This page covers emulating High Voltage protocols, so while most tinkerers might be familiar with 48V DIY batteries, building a 96S 400VDC battery is an entirely different beast that can be lethal. Take extra precaution when working on a custom DIY HV battery, you have been warned.

> [!CAUTION]
> If you are unsure of your technical knowhow, avoid building a high voltage battery from scratch

## Custom DIY battery with Orion BMS

## Software configuration
For this battery type, use the option called "DIY battery with Orion BMS (Victron setting)" under the "Battery Protocol" setting

![image](../images/orion-bms-02.png){ width="668" height="272" }

Also remember to configure the designed voltage for your pack, and the chemistry/cellvoltage limits

## Setting up the BMS

You need to set the Orion BMS to transmit using the Victron protocol

![image](../images/orion-bms-01.png)
