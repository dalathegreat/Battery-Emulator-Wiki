---
title: "RJXZS BMS"
---

## Read this first

Preface, the entire Battery-Emulator project sets out to achieve safe re-use of EV batteries. By building your own battery, you will be taking larger risks. Cell balancing wire taps, shunts, busbar connections, BMS integration, temperature monitoring, fuses, contactors, interlocks, etc. all will have to be implemented by yourself instead of using a pre-made product. As with all things custom, there are higher risks of human error. This page covers emulating High Voltage protocols, so while most tinkerers might be familiar with 48V DIY batteries, building a 96S 400VDC battery is an entirely different beast that can be lethal. Take extra precaution when working on a custom DIY HV battery, you have been warned.

!!! warning "CAUTION"
    If you are unsure of your technical knowhow, avoid building a high voltage battery from scratch.

## Custom DIY battery with RJXZS BMS
The Battery-Emulator has support for the 4-192S RJXZS BMS. With this BMS you can construct your own high voltage battery, and connect the BMS via CAN to the Battery-Emulator. This allows you to use a DIY battery (instead of an EV battery) with any normal Battery-Emulator supported inverter.

### Where do I get the hardware?

- [aliexpress](https://www.aliexpress.com/i/1005005915643384.html)
- contact [sales@rjxzstech.com](mailto:sales@rjxzstech.com)

### Where do I get the User Manual?

User Manual can be found here: 
[4-192S BMS operation manual.pdf](https://github.com/user-attachments/files/19853501/4-192S.BMS.operation.manual.pdf)

### How do I calculate how many cells I need?
You need to see the voltage range of the inverter, and calculate based on the chemistry you intend to use. For instance, a Fronius Gen24 takes 160-531V on the battery input. Using the limits for NCM chemistry (3.0V empty, 4.2V full), this means the minimum viable battery configuration would be 160V empty (160V/3.0V=53S), and the largest battery configuration would be (531V/4.2V=126S). So a 53S at minimum, and a 126S config max.

## Setting up the BMS
You can download the latest official version from RJXZS at: [rjxzstech](https://www.rjxzstech.com/download/the-APP-of-192S-Ghost-BMS-for-android.html)

On some phones to run app you need to turn on GPS positioning and allow app to use that feature:

![image](../images/rjxzs-bms-01.png)

Settings are configured on the RJXZS BMS via the TOPBMS smartphone app. The most important settings are capacity (AH), cells in series, low voltage cutoff, and charge end voltage.

![image](../images/rjxzs-bms-02.png)

- Remember to calibrate AH. Without this, the SOC% will be 0 all the time. The best way is to charge battery to its maximum and set Battery used capacity in Top BMS APP to 0 Ah. 
   - To figure out how many AH your battery holds, you can calculate it with ((kWh * 1000) / nominalV). For instance a 30kWh LEAF battery would be ((30 * 1000)/370V) = 81AH
- It is recommended to activate function "Automatically Clear Capacity" - this will set SOC to 100% every time charge voltage limit is reached

**Main settings description** [taken from RJXZS manual](https://github.com/user-attachments/files/19853501/4-192S.BMS.operation.manual.pdf)

![image](../images/rjxzs-bms-09.png){ width="498" height="694" }

!!! warning "CAUTION"
    Failure to set correct voltage cutoff according to your battery chemistry can lead to catastrophic damage. For instance an Lifepo4 cell should charge max to 3.5V. Overcharging LFP cells to >4V will cause permanent damage and/or battery fire.

## Setting up the Battery-Emulator integration

!!! info "IMPORTANT"
    The RJXZS BMS runs at 250kbps CAN speed. Due to this it cannot be connected to same CAN bus as solar inverters. This BMS needs to be connected to the Native CAN (Built in CAN on LilyGo, CAN1 on Stark)

Start by connecting the CAN port of the BMS, to the CAN port on the Battery-Emulator.

![image](../images/rjxzs-bms-03.png)

- If you have a Modbus inverter, connect it to the RS485 port of the Battery-Emulator
- If you have a CAN inverter, you need to connect it to a separate 500kbps CAN channel, since the BMS runs at 250kbps on the native CAN
   - One option is to use [add on MCP2515](../setup/can_related/can_add_on_mcp2515.md) board
   - Another options is to use [add on CAN-FD MCP2518](../setup/can_related/can_fd_add_on_mcp2518fd.md) board 
   - Third option is to use [Stark CMR board](../hardware/stark_cmr.md)
   - Fourth option is to use [Double LilyGo](../setup/software/double_lilygo.md) setup

For this battery type, use the option called "RJXZS BMS, DIY battery" under the "Battery Protocol" setting.

![image](../images/rjxzs-bms-10.png){ width="664" height="345" }

Configure all the settings according to the specifications of the battery you have constructed, the general password to access settings is "0". CAN send ID and CAN receive ID should be 245 and 244 respectively, these settings are locked behind the password "770921".

After uploading the code to the Battery-Emulator, you can check cellvoltages, SOC etc. via the [Webserver](../setup/software/webserver_guide.md)

!!! info "IMPORTANT"
    During first startup, RJXZS will report faults, thats why first thing you need to do is clear all events in bluetooth app by holding CLR button for a few seconds:

    ![image](../images/rjxzs-bms-04.png)

    All events which are stored inside RJXZS BMS are marked very well in battery emulator Event List:

    ![image](../images/rjxzs-bms-05.png)

Example of value monitoring, and cellvoltage monitoring of a 70S battery

![image](../images/rjxzs-bms-06.png)

## Example integrations
Feel free to add your own pictures here!

![image](../images/rjxzs-bms-07.png)

![image](../images/rjxzs-bms-08.png)

