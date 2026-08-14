---
title: "Contactor Control via GPIO"
---

!!! warning "CAUTION"
    Contactors can weld themselves together if handled improperly, which may result in high voltage being present on connectors even when the system is powered down. Always assume high voltage is present on any high voltage wiring. To ensure safety, unplug the wiring from the battery or remove safety disconnect switches before working on the system. Then measure with a multimeter to confirm the system is off.

Start by familiarizing yourself with how contactor and precharge circuits work. [Here is a good whitepaper](https://www.sensata.com/sites/default/files/a/sensata-how-to-design-precharge-circuits-evs-whitepaper.pdf) that explains how precharging works in great detail.

## Automatic control 🤖
The Battery-Emulator simulates an entire car to get EV batteries to turn themselves on. Some batteries have CAN controlled contactors (e.g. Tesla,Kia,Hyundai), but some require hardwired signals (e.g. LEAF, Zoe) to turn on contactors and the precharge sequence. Instead of having to wire manual on/off switches for these signals, you can have the emulator hardware perform this (feature called `CONTACTOR_CONTROL`). This will automatically handle precharge, contactor closing, and optional economization. 

It will also automatically open contactors when a critical FAULT event is encountered, if the FAULT event sticks for longer than 10 seconds contactors are opened. To recover from a latched fault, rebooting the emulator is required. You can then check which event led to the unrecoverable contactor opening via the [Webserver events](webserver_guide.md#events) view. This improves safety for batteries that require manual control over the contactors, compared to manual on/off switches that will stay in their set state when a critical FAULT occurs. So to summarize, if you have a battery that needs hardwired signals for contactors, this feature is highly recommended!

### Hardware requirements
This is done via the 3.3V digital output header that is located on the board. To use these, you need to solder a 2x6 row connector onto the board (Easier with the [Stark CMR](../../hardware/stark_cmr.md), no soldering needed there). After the row connector is fitted, you can connect cables between the pins, and the relays.

For instance, 3x ASR-10DD can be used. ASR-M02DD is a din mounted version. If you don't need SSR, and just want a relay, you can use a 4-channel-relay such as [this](https://www.aliexpress.com/item/1005007431826795.html?)

!!! warning "CAUTION"
    Be sure to get a **DC** SSR. Using an AC triggered SSR will not work, these will latch while waiting for zero crossing.

### Software setup

To enable the feature in the software, Enable the "Contactor Control via GPIO" option under Hardware Config, Save and reboot.

![image](../../images/contactor-control-via-gpio-pins-04.png)

By default a 100 millisecond long precharge is performed. This value should be set to account for the resistance and capacitance of the inverter you use. 

There is also an option to use "Use Normally Closed logic:" This is for very rare contactor setups, and should for 99.99% of users not be enabled :warning: 

!!! note "NOTE"
    Normally EVs perform a much more robust precharge, measuring motor inverter voltage and basing precharge duration based on this info, but since we dont have this info available a simple timer is used. Not optimal, but better than nothing!

### Example wiring diagram 🗺️ 
To keep things simple, it is recommended to use Solid State Relays (SSR). These can be activated with 3Volt, and control large DC currents. 

This schematic shows a wiring example with LilyGo T‐CAN485:

- Precharge pin 25 - Precharge SSR + input
- Positive Contactor pin 32 - Positive SSR + input
- Negative Contactor pin 33 - Negative SSR + input
- GND - All 3x SSR - input

![bild](../../images/nissan-leaf-e-nv200-07.png)

[Stark CMR](../../hardware/stark_cmr.md), doesn't need an SSR since its outputs are rugged.

### Troubleshooting
Before the contactors turn on, both Inverter and Battery needs to give OK ✅ signal. This can be verified via the Webinterface. In this screenshot, battery is preventing startup:

![bild](../../images/nissan-leaf-e-nv200-08.png)

!!! warning "WARNING"
    In case the whole Emulator goes into Fault state, the contactors will open, and latch. To get them to close again, you need to restart the entire Battery-Emulator (after having analysed the fault)

You can check the Event view in the webserver, to see if any critical Error has been encountered

#### Overloaded GPIO pins
Incase the current draw on the GPIO pins is exceeded, for instance incase you use an unsupported SSR, the webserver will appear this way:

![image](../../images/contactor-control-via-gpio-pins-03.png)

Note the "X" on both contactors, even though the emulator is in active state and should have contactors engaged. If you see this, remove the wires and restart the emulator, to confirm that activation of the pins is possible. Then switch to a supported SSR.

## PWM control for lower power draw 🧊 
Optional: It is also possible to reduce power consumption of keeping the big contactors engaged via PWM control. This requires Solid State Relays (SSR). The PWM signal will very quickly turn on/off the SSR, and still keep the contactor engaged. Do be careful, and test this properly before using it. It is very much depending on what SSR and battery contactor combination you use. 

To use the PWM function, enable the "PWM contactor control" option

![image](../../images/contactor-control-via-gpio-pins-05.png)

By default we use a Hold value of 250, which is suitable for Nissan LEAF contactors. Tweak this value to suit your contactors.

### Benefits of PWM
* Less load on the 12V supply
* Better for offgrid solutions where every Watt counts
* Less heat inside battery is good for summer

!!! note "NOTE"
    PWM can only be used with electromechanical contactors. It's not applied to the BMS power control pin, despite that's also usually wired using a SSR.
