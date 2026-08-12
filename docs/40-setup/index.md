---
title: Setup & Docs
hide:
  - toc
---

# Setup

## How do I get started?
- Pick a [supported solar inverter](../10-inverters/index.md#supported-inverters-list) (solar panels optional) 🌞 
- Pick a [supported battery](../20-battery/index.md#supported-batteries-list) 🔋 
- Order the Battery-Emulator [compatible hardware](../30-hardware/index.md) 🤖 
- Follow the [installation guidelines](10-hardware/Installation-guidelines.md) section for how to install and commission your battery properly 📓 

## CAN wiring troubleshooting

This section has been expanded [and moved here](40-can-related/CAN-wiring-practices-and-troubleshooting.md) 

Note! CAN networks are vulnerable to lightning strikes. [See the dedicated wiki page for this for more info](10-hardware/Lightning-strike.md) :cloud_with_lightning: 

## Supported chargers list (optional)
Emergency charging batteries via a generator, supported via the following standalone chargers:
* [Chevrolet Volt Gen1](30-chargers/Charger_-Chevrolet-Volt-Gen1.md)
* [Nissan LEAF 2013-2024 PDM](30-chargers/Charger_-Nissan-LEAF-PDM.md)

## Shunts
* [BMW S-BOX](10-hardware/Shunt_BMW-SBOX.md)

## What about safety? ⚠️ ℹ️
Reusing old often crashed EV packs always comes with risks. The system performs a few safety functions for safer charging and discharging. Apart from this, the data sent to the Inverter is also processed on the inverter side, and depending on which inverter is used a few additional safety checks are performed there. Here is a list of all safety functionalities that are in the system. Note that almost all safety features rely on communication data, so a physical error (damaged cell casings, ruptured/leaking cells, corrosion etc.) wont be detectable via software. For this you need fuses, and periodic visual inspections. 

> [!TIP]
> Be sure to checkout the [installation guidelines](10-hardware/Installation-guidelines.md) section for how to install your battery

> [!CAUTION]
> ***At the end of the day, you alone are responsible for the system.***

Safety features run on (most) inverter(s):
- Battery sends max total voltage allowed for charging. Incase this value is reached, inverter stops charging. (For instance 404V)
- Battery sends min total voltage allowed for discharging. Incase this value is reached, inverter stops discharge (For instance 300V)
- Battery sends max cell temperature. Incase this value goes too high, inverter stops charge/discharge (For instance 40*C)
- Battery sends min cell temperature. Incase this value goes too low, inverter stops charge/discharge (For instance -15*C)
- Battery sends max allowed charge in Watts. Incase this goes to 0W, no further charging is possible. (This can happen when battery is full)
- Battery sends max allowed discharge in Watts. Incase this goes to 0W, no further discharge is possible. (This can happen when battery is completely empty)
- Battery sends state of health %. Incase this value drops too low, the inverter will alert the user that it is time to recycle the battery.
- Inverter analyzes insulation resistance of the battery connection. Incase a leakage to ground is detected, the system stops.

Safety features run on Battery-Emulator side:
- If the code enters FAULT state, inverter gets notified, all charging/discharging stops, and contactors are opened ([if they are controlled via GPIO pins](20-software/Contactor-Control-via-GPIO-pins.md)).
- If CAN communication is lost between emulator and battery for more than 60s, the code enters FAULT state.
- Total pack voltage is sampled, if it goes too high it sets allowed charge power to 0. If it continues to rise, we enter FAULT mode
- Total pack voltage is sampled, if it goes too low it sets allowed discharge power to 0. If it continues to fall, we enter FAULT mode
- Minimum cell voltage is sampled, and if one cell goes too low the code enters FAULT state. (For instance <2900mV)
- Maximum cell voltage is sampled, and if one cell goes too high the code enters FAULT state. (For instance >4250mV) 
- Battery state of health % is sampled, if it is below 25% the code stops and informs the user that it is time to recycle the battery.
- BMS fault codes are sampled, if any serious code is set, the code enters FAULT state (For instance LB_Failsafe_Status on Nissan LEAF packs)
- High voltage wiring is unhooked during operation. This will trigger interlock messages, and the code enters FAULT state
- Incase of a high voltage leak to battery casing (Protective earth), the code enters FAULT state (For instance LB_Failsafe_Status on Nissan LEAF packs)

> [!IMPORTANT]  
> Do note that all actual limits are battery/inverter specific, the values here are only used for example purposes. The amount of safeties will vary depending on your choice of battery.

> [!TIP]  
> You can also add an [equipment stop button](20-software/Equipment-Stop.md) to the Battery-Emulator, to increase the amount of safety.