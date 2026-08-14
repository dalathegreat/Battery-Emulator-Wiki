---
title: "New inverter integration"
---

# Introduction
This page describes the values needed for an inverter integration. If you want to integrate a new inverter type , this page will help you figure out what you need to be able to extract from the battery via CAN/Modbus logs.

## Logs needed
Unless the communication protocol is already reverse engineered and available, you will be looking at quite the amount of work :) Start out with a fully functional system (Brand inverter + Brand battery). You can try to find someone willing to let you sniff the communication between these, or someone will have to purchase/borrow a system.

The communication between the brand inverter and brand battery can be either CAN based or Modbus based. Check the manual of the inverter to figure out if it is CAN or RS485.

### CAN based system
If the system is CAN based, you will first have to get some hardware capable of reading the communication. Here are some examples, listed from least expensive to more expensive. Do note that more expensive tools will be easier to use, since the software provided with the tools are very user friendly. Also more expensive tools will have better timing and accuracy on timestamps.

- Battery-Emulator hardware, for instance a LilyGo board (using [CAN logging](../can_related/can_logging.md))💲
- Arduino with CAN shield 💲
- Raspberry PI with CAN shield 💲💲
- USB2CAN Korlan 💲💲 [Recommended, link:](https://www.8devices.com/products/usb2can_korlan)
- Kvaser 💲💲💲 
- Peak PCAN 💲💲💲
- Softing 💲💲💲

### Modbus/RS485 based systems
If the system is modbus based, the difficulty grows a bit more. Here is a list of hardware that can be used,

- USB RS485 reader from Ebay 💲
- TODO: Add more options
- LilyGo board, see [example here](../../inverter/kostal.md#traces-for-reverse-engineering)

The following sniffer is recommended: [github/alerighi](https://github.com/alerighi/modbus-sniffer)

This provides an output possibility as Wireshark PCAP file which improves the analysis and filtering capability.

## I have the logger, and a working system, what's next?
Once the hardware is ready, take logs of each of these events.

- System startup
- System shutdown
- Charging battery from sun/grid for a few hours
- Discharging battery for a few hours
- Sudden turn off of battery. Check which CAN IDs stop broadcasting
- Sudden turn off of inverter. Check which CAN IDs stop broadcasting

When logging, keep track of the parameters. SOC% start to stop, Temperatures, charging power, discharge power etc. The more physical reference points you note down while taking the logs, the easier it will be to decipher them.

## I have the logs!
Great! Feel free to share them on the Discord / Github issues page. Then it is time to reverse engineer the data. Once the logs are present, others without the brand battery can join in to help.

For instance, here looking for a Hot battery, vs a Cold battery in two CAN logs.

- 0x245, 0x01 0x00 0x02 0x19 **0x38** 0x25 0x90 0xF6
- 0x245, 0x01 0x00 0x02 0x19 **0x36** 0x25 0x90 0xF8

0x38 = 56 (offset -40deg) = 16C

0x36 = 54 (offset -40deg = 14C

Perform the same detective work for the following parameters.

- SOC%
- Voltage
- Temperature
- Charge power allowed
- Discharge power allowed,
- Current
- +Any other relevant parameters

## Creating the integration
Once the mandatory info has been found for the inverter communication, it can be integrated to the software. Create an inverter.cpp and .h header, see the other inverter protocols for how the structure should look like. If in doubt, contact the developers!

<img width="1408" height="811" alt="kép" src="https://github.com/user-attachments/assets/4d44671c-f923-457e-9abb-96dc78e38f90" />
