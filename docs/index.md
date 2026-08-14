---
title: "Welcome"
description: This revolutionary software enables EV battery packs to be easily reused for stationary storage in combination with solar inverters 
hide:
  - navigation
---

# Battery-Emulator ⚡🔋
![GitHub release (with filter)](https://img.shields.io/github/v/release/dalathegreat/BYD-Battery-Emulator-For-Gen24?color=%23008000)
![GitHub Repo stars](https://img.shields.io/github/stars/dalathegreat/Battery-Emulator?style=flat&color=%23128512)
![GitHub forks](https://img.shields.io/github/forks/dalathegreat/Battery-Emulator?style=flat&color=%23128512)
![GitHub actions](https://img.shields.io/github/actions/workflow/status/dalathegreat/BYD-Battery-Emulator-For-Gen24/compile-common-image-lilygo-TCAN.yml?color=0E810E)
![Static Badge](https://img.shields.io/badge/made-with_love-blue?color=%23008000)

## What is Battery Emulator?

Many manufacturers sell home battery systems to enable homeowners to store power collected from the grid, or renewable sources, to use at times when electricity demand is higher. However almost all of these home battery systems charge a high cost for every kilowatt hour (kWh) of capacity you buy.

At the same time, EV manufacturers have been putting high capacity battery packs into their cars, with no firm plan for what should happen to those batteries if the car is damaged in a crash, or reaches the end of its life as a vehicle.

**Battery Emulator** enables EV battery packs to be repurposed for stationary storage. It acts as a translation layer between the EV battery and the home inverter. This makes it extremely cheap and easy to use large EV batteries in a true plug'n'play fashion!

## Quickstart guide 📜
- Pick a [supported inverter](inverter/index.md#supported-inverters-list) (solar panels optional) :sun_with_face: 
- Pick a [supported battery](battery/index.md#supported-batteries-list) :battery: 
- Order a Battery-Emulator board or module [compatible hardware](hardware/index.md) :robot: 
- Follow the [installation guidelines](setup/hardware/installation_guidelines.md) section for how to install and commission your battery properly :notebook: 

!!! warning "CAUTION"
    Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## What about safety? ⚠️ ℹ️
Reusing old often crashed EV packs always comes with risks. The system performs a few safety functions for safer charging and discharging. Apart from this, the data sent to the Inverter is also processed on the inverter side, and depending on which inverter is used a few additional safety checks are performed there. Here is a list of all safety functionalities that are in the system. Note that almost all safety features rely on communication data, so a physical error (damaged cell casings, ruptured/leaking cells, corrosion etc.) wont be detectable via software. For this you need fuses, and periodic visual inspections. 

!!! tip "TIP"
    Be sure to checkout the [installation guidelines](setup/installation_guidelines.md) section for how to install your battery.

!!! warning "CAUTION"
    ***At the end of the day, you alone are responsible for the system.***

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

- If the code enters FAULT state, inverter gets notified, all charging/discharging stops, and contactors are opened ([if they are controlled via GPIO pins](software/contactor_control_via_gpio_pins.md)).
- If CAN communication is lost between emulator and battery for more than 60s, the code enters FAULT state.
- Total pack voltage is sampled, if it goes too high it sets allowed charge power to 0. If it continues to rise, we enter FAULT mode
- Total pack voltage is sampled, if it goes too low it sets allowed discharge power to 0. If it continues to fall, we enter FAULT mode
- Minimum cell voltage is sampled, and if one cell goes too low the code enters FAULT state. (For instance <2900mV)
- Maximum cell voltage is sampled, and if one cell goes too high the code enters FAULT state. (For instance >4250mV) 
- Battery state of health % is sampled, if it is below 25% the code stops and informs the user that it is time to recycle the battery.
- BMS fault codes are sampled, if any serious code is set, the code enters FAULT state (For instance LB_Failsafe_Status on Nissan LEAF packs)
- High voltage wiring is unhooked during operation. This will trigger interlock messages, and the code enters FAULT state
- Incase of a high voltage leak to battery casing (Protective earth), the code enters FAULT state (For instance LB_Failsafe_Status on Nissan LEAF packs)

!!! info "IMPORTANT"
    Do note that all actual limits are battery/inverter specific, the values here are only used for example purposes. The amount of safeties will vary depending on your choice of battery.

!!! tip "TIP"
    You can also add an [equipment stop button](software/equipment_stop.md) to the Battery-Emulator, to increase the amount of safety.
    
## Like this project? 💖
Consider hopping onto my [Patreon](https://www.patreon.com/dala) to encourage more open-source projects! As a bonus, you will get access to the Discord server, where we hangout, develop, support, share, discuss etc. all things related to DIY EV storage solutions. See you on the server? ;)
