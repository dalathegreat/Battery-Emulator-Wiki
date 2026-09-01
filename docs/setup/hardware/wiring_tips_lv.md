---
title: "Low Voltage wiring tips"
---

## Data signal

By standard, CAN communication at 500kbps is good for 100meter max. RS485 or Modbus, with proper cabling, can co up to 1km.

!!! note "IMPORTANT"
    Data wires carrying CAN and Modbus data need to be in **twisted pair** to ensure signal integrity. 

!!! tip "IMPORTANT"
    Make sure the cable you are using is **shielded**. Only **one side of the shield** should be connected to a pin labelled SHIELD (or PE if no dedicated shield exists). This avoids ground loops. 

Maximum data cable lengths may be specified by inverter manufacturers. Respect these distances if possible, to avoid problems. However, since EV batteries may not be installed [in the same circumstances](../installation_guidelines.md) as home battery packs, you may need to use longer cable runs. Compensation can be made by choosing carefully. 

The easiest choice is shielded CAT6 cabling used for Ethernet networks, where you only use one pair of the four. Other options include cables designed for Modbus, BACnet MS/TP, CANopen, or DMX512. Choose a good quality shielded twister pair model of at least 0.2 - 0.3mm² (22 - 24 AWG) cross section per wire. As usual, the longer, the tchicker.

If you're into deciding where to place Battery Emulator, closer to the battery, or closer to the inverter, if there are no other influencing factors, place it closer to the battery. This advice is based on the thought that the CAN interface in the battery is originally designed to take part in a network of CAN devices within a car, at maximum distance of a few meters, whilst inverter data interfaces (be it CAN or Modbus) are rated to work on longer cable runs on purpose. Do that especially if you using an RS485/Modbus inverter - that protocol is especially optimal for long distances.
    
!!! danger "CAUTION"
    Grounding everything is especially important for certain inverters. If you fail to ground inverter or battery casing to a commoon protective earth potential (PE), a voltage difference between the two components may develop, which can fry the CAN communication chips on the Battery Emulator board. Always connect every component, and the communication shield wire to **the same** protective earth before turning the system on!

See this example for grounding: 

![image](../../images/lightning-strike-02.png)


![image](../../images/can-wiring-practices-and-troubleshooting-03.png)

Here is the best way to ensure that there are no paths for spikes in CAN voltage to fry chips on the boards (Important for [Solax](../../inverter/solax.md) and [Foxess](../../inverter/foxess_h1_h3_ac1_kh.md), other inverters are more lenient on what power supply you use)

![image](../../images/can-wiring-practices-and-troubleshooting-04.png)

!!! warning "CAUTION"
    Never connect the signal wire shields in both sides. This creates a ground loop. One side of the shield should be free floating, like shown in the above pictures.

## Control signal (12V)

HV battery packs from EVs usually require an external 12V input at least to power the BMS. Many packs despite having built-in HV contactors, they are controlled externally with 12V signals. Since contactors themselves contain coils which draw rather high currents compared to what a microcontroller can provide, external relays/SSRs/Mosfets are used to drive these.

Contactors within HV packs drain continuously around 0.5A each, at 12V. Usually there are at least two of them, one for positive and one for negative, and a third one for circuit precharging. Varrying by type, an inrush current can develop for a very small amount of time when applying power to these contactors.

Thus, the 12V power source (and backup battery) you use must be able to handle these. Generally a 12V 2.5A power supply should be enough for Battery Emulator hardware and the battery pack with it's own contactors, and this applies even if the contactors are controlled over CAN. If you use multiple packs in a double of triple setup, you'll need a bigger 12V supply accordingly.

Don't use the free CAT5/6 cable wires you have next to the CAN bus to externally drive contactors at 12V. Not only they are too thin, the contactors's inrush currents may cause interference with CAN / Modbus if you do that. Regular Ethernet cable wires go between 0.12 - 0.25mm² (23 - 26 AWG). You need at least 0.5mm² (20 AWG) which rated for max 0.5A on a few meters distance. 

Increasing distance significantly will need to increase wire tchickness too, in order to avoid energy loss on the cable itself, just like it happens for [for high voltage](wiring_tips_hv.md) For tens of meters of cable path, use at least 1.5mm² (AWG 14) cable to drive the BMS and the contactors with 12V.

If you wanna go really pro, you can use automotive grade cable (FLRY-A or B ISO 6722):

* FLRY-A Automotive low voltage cable (FL) with reduced thickness of insulation (R) made of PVC (Y), with regularly stranded conductor (A)
* FLRY-B Automotive low voltage cable (FL) with reduced thickness of insulation (R) made of PVC (Y), with irregularly stranded conductor (B)
