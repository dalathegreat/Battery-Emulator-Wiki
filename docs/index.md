---
title: "Welcome"
description: This revolutionary software enables EV battery packs to be easily reused for stationary storage in combination with solar inverters 
hide:
  - navigation
---

# Battery-Emulator ⚡🔋

![GitHub release (with filter)](https://img.shields.io/github/v/release/dalathegreat/Battery-Emulator?color=%23008000)
![GitHub Repo stars](https://img.shields.io/github/stars/dalathegreat/Battery-Emulator?style=flat&color=%23128512)
![GitHub forks](https://img.shields.io/github/forks/dalathegreat/Battery-Emulator?style=flat&color=%23128512)
![GitHub actions](https://img.shields.io/github/actions/workflow/status/dalathegreat/Battery-Emulator/compile-common-image.yml?color=0E810E)
![Static Badge](https://img.shields.io/badge/made-with_love-blue?color=%23008000)

## What is Battery Emulator?

Many manufacturers sell home battery systems to enable homeowners to store power collected from the grid, or renewable sources, to use at times when electricity demand is higher. However almost all of these home battery systems charge a high cost for every kilowatt hour (kWh) of capacity you buy.

At the same time, EV manufacturers have been putting high capacity battery packs into their cars, with no firm plan for what should happen to those batteries if the car is damaged in a crash, or reaches the end of its life as a vehicle. As it turns out, in the vast majority of the cases the battery pack is the part that outlives the car on very long term. Even after more than ten years, the remaining usable capacity in an EV battery pack is still above the magnitude of a household need.

**Battery Emulator** enables EV battery packs to be repurposed for stationary storage. It acts as a translation layer between the EV battery and the home inverter. This makes it extremely cheap and easy to use large EV batteries in a true plug'n'play and environment-friendly fashion!

!!! danger "DANGER"
    This project requires qualified electrician skills along IT knowledge. Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. 
    
    If you are unsure about the rules in your country, consult a licensed electrician for more information.

The software runs on specific ESP32 hardware boards, supports [Over The Air updates](setup/software/ota_update.md), has a [web interace that you can connect to for real time values](setup/software/webserver_guide.md), cellmonitoring, change settings and more. For those into [home automation](setup/software/home_assistant.md), it also supports [MQTT](setup/software/mqtt.md). 

## Quick start steps 📜

- Pick a [compatible inverter](inverter/index.md#compatible-inverters-list) (solar panels optional) :sun_with_face: 
- Pick a [compatible battery](battery/index.md#compatible-batteries-list) :battery: 
- Order a Battery-Emulator board or module [compatible hardware](hardware/index.md) :robot: 
- Follow the [installation guidelines](setup/installation_guidelines.md) section for how to install and commission your battery properly :notebook: 

[![video](https://img.youtube.com/vi/sR3t7j0R9Z0/0.jpg)](https://www.youtube.com/watch?v=sR3t7j0R9Z0)

## What about safety? ⚠️ ℹ️

Reusing old often crashed EV packs always comes with risks. The system performs certain safety functions for safer charging and discharging. Apart from this, the data sent to the Inverter is also processed on the inverter side, and depending on which inverter is used some additional safety checks are performed there. Here is a list of some of the safety functionalities that are in the system. Note that almost all safety features rely on communication data, so a physical error (damaged cell casings, ruptured/leaking cells, corrosion etc.) wont be detectable via software. For this you need fuses, and periodic visual inspections. 

!!! tip "TIP"
    Check out the [installation guidelines](setup/installation_guidelines.md) section for how to install your battery. There are dedicated [High Voltage](setup/hardware/wiring_tips_hv.md) and [Low Voltage](setup/hardware/wiring_tips_lv.md) wiring pages with tips and examples on how to make the connections safely. Consider protection against [lighning strikes](setup/hardware/lightning_strike.md) when choosing a location deploying cabling.

!!! warning "CAUTION"
    ***At the end of the day, you alone are responsible for the system.***

Safety features implemented in (most) inverters are respected. Parameters sent by the battery are taken in consideration in real time:

- Maximum total voltage allowed for charging and minimum total voltage allowed for discharging. In case any of these value is reached, inverter stops charging and discharging.
- Maximum and minimum cell temperature. In case this value goes too high or too low, inverter stops charging or discharging (for instance above 40°C or below -15°C).
- Maximum allowed charge or discharge power in Watts. In case this goes to 0W, no further charging or discharge is possible. This can happen when battery is full or completely empty.
- Sate of health in percentage. In case this value drops too low, the inverter will alert the user that it is time to recycle the battery.
- Inverter analyzes insulation resistance of the battery connection. In case a leakage to ground is detected, the system automatically stops and an alert is being logged.

Examples of additional safety features implemented on Battery Emulator side:

- If the code enters `FAULT` state, inverter gets notified, all charging/discharging stops, and contactors are opened ([when controlled directly via GPIO](setup/software/contactor_control_via_gpio_pins.md)).
- If CAN communication is lost between emulator and battery for more than 60s, `FAULT` state is triggered.
- Total pack voltage is sampled, if it goes too high or too low, it sets allowed charge/discharge power to 0. If it continues to rise `FAULT` state is triggered.
- Maximum and minimum cell voltage is sampled, and if one cell goes too high or too low `FAULT` state is triggered.
- State of health % is sampled, if it is below 25% the code stops and informs the user that it is time to recycle the battery.
- BMS fault codes are sampled, if any serious code is set, the code enters `FAULT` state (For instance the factory `LB_Failsafe_Status` on [Nissan LEAF packs](battery/nissan_leaf_e_nv200.md)).
- In case of a high voltage leak to battery casing ([Protective earth](setup/installation_guidelines.md#protective-earth)), the code enters FAULT state.
- High voltage wiring is unhooked during operation. This will trigger interlock messages, and the code enters `FAULT` state.

!!! info "IMPORTANT"
    All actual limits are battery/inverter specific. The amount of safeties will vary depending on your choice of battery.

!!! tip "TIP"
    You can also add an [equipment stop button](setup/software/equipment_stop.md) to the Battery-Emulator, to increase the amount of safety.
    
## Like this project? 💖
Consider hopping onto my [Patreon](https://www.patreon.com/dala) to encourage more open-source projects! As a bonus, you will get access to the Discord server, where we hangout, develop, support, share, discuss etc. all things related to DIY EV storage solutions. See you on the server? ;)
