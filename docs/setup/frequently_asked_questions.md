---
title: "Frequently Asked Questions"
hide:
  - toc
---

The questions below are the ones most often asked by people evaluating whether this project fits their situation, before any hardware is bought.

## What is Battery Emulator, and what does it actually do?
It is open source firmware that acts as a translation layer between a used EV battery pack and a home hybrid inverter. On one side it speaks the pack's native protocol and simulates enough of a car to make the battery turn itself on; on the other side it presents the pack as a home battery product the inverter already knows. The result is stationary storage at a fraction of the cost per kWh of a commercial home battery.

## Is this only for packs removed from a vehicle?
Yes. The scope of the project is battery reuse outside a vehicle. Driving the pack through a vehicle charge port while it is still in the car is technically imaginable, but the connector alone costs more than several kWh of salvage storage would.

## Can I buy this as a finished, pre-programmed unit?
No, and there are no plans to sell one. This is a DIY project for competent individuals: you source the board, flash it, wire the system and commission it yourself. It is nonetheless a well-trodden path — over 2500 installations had been done by the start of 2026 — and there is an active community behind it.

## What skills and approvals does a deployment require?
Qualified electrician skills, plus enough IT literacy to run and secure a small network device. Familiarise yourself with local regulations for solar inverters and stationary storage, and confirm your inverter model is approved by your grid operator **before** ordering parts. At the end of the day, you alone are responsible for the system.

## What hardware does the firmware run on?
ESP32 only. Several ready-made boards are documented on the [Emulator Hardware](../hardware/index.md) page, ranging from cheap dual-CAN modules to certified DIN-rail hardware, each rated for how newcomer-friendly it is. Any other ESP32 variant can be brought up by writing a Hardware Abstraction Layer file to the source code; other architectures are deliberately out of scope.

## How do I check that my battery and inverter will work together?
Start with the [compatible batteries](../battery/index.md#compatible-batteries-list) and [compatible inverters](../inverter/index.md#compatible-inverters-list) lists — both carry star ratings showing how mature each integration is, plus notes on known limitations. Verify that the voltage windows of pack and inverter overlap, and check whether your combination needs extra hardware such as a separate CAN channel, a [CAN filter](can_related/can_filter_hardware.md), [GPIO contactor control](software/contactor_control_via_gpio_pins.md) or an [external precharge source](hardware/high_voltage_source.md).

## Can I evaluate the software before buying a battery or an inverter?
Yes. A built-in [fake battery](../battery/fake_battery.md) integration generates plausible pack data with no bus traffic and no hardware attached, so you can flash a board on your desk and explore the web interface, cell monitor, home automation integration and even multi-pack setups. 

## What safety functions are performed, and what can they not catch?
Pack and cell voltages, cell temperatures, BMS fault codes and communication health are all monitored continuously; anything out of bounds drops the system into a `FAULT` state that zeroes charge and discharge and opens the contactors. Your inverter layers its own protections on top, including insulation monitoring. Almost every check relies on communication data, so physical defects — damaged cell casings, leaking cells, corrosion — are not detectable in software. Fuses, correct [HV](hardware/wiring_tips_hv.md) and [LV](hardware/wiring_tips_lv.md) wiring, an optional [equipment stop button](software/equipment_stop.md) and periodic visual inspection are what cover that gap.

## Where am I allowed to put the battery?
Only somewhere a potential fire would not endanger human life: outdoors, a detached garage, a tool shed, underground, or a shipping container. Most salvage packs come from crashed vehicles with unknown history, which makes placement the single most consequential decision in the build. Keep rain out, and plan for temperature — the firmware halts power transfer and raises a fault if the pack gets too hot or too cold. See the [installation guidelines](installation_guidelines.md) for worked examples.

## Does it depend on the internet, a cloud service or a subscription?
No. The real-time control loop runs entirely on the board and keeps the system operating with no network present at all. Wi-Fi only serves the [web interface](software/webserver_guide.md), firmware updates and optional integrations. Never port-forward the device to the internet — use a VPN into your own network if you need remote access.

## How do I get the firmware on the board, and how do I keep it updated?
The first flash goes over USB from a browser-based [web installer](installer.md), or manually with `esptool` if you prefer. From then on, updates are done [over the air](software/ota_update.md) from the web interface, using the release image matching your board. Saved settings persist across updates, so there is no reconfiguration after each release.

## How do I monitor and troubleshoot a running system?
The built-in web server shows live values, which side is currently limiting charge or discharge, a timestamped event log split into info/warning/error, and a per-cell voltage monitor; a status LED gives the same green/yellow/red picture at a glance. For long-term trending there is [MQTT](software/mqtt.md) with [Home Assistant](software/home_assistant.md) autodiscovery, and an [ESP-NOW](software/espnow.md) link for a wireless local display. Debug logs can be sent to USB serial, an SD card or a remote syslog server.

## Can I run more than one pack?
Yes — two or three packs in parallel, multiplying capacity while the inverter still sees a single large battery. They must be the same model and size and as close as possible in state of health, each pack needs its own CAN channel (so this influences which board you buy), and only some integrations support it. Never connect packs in series: no safeties exist for it and the isolation is not rated for it. See [Double Battery](software/battery_2x.md) and [Triple Battery](software/battery_3x.md).

## What ongoing maintenance should I plan for?
Check for new releases every two to three months, and apply anything safety-related promptly. Monthly, review the event log and visually inspect for corrosion, water ingress, pest damage and overheated cabling. Yearly, re-check terminal tightness on the HV connections. Track state of health and cell deviation over time — a degrading cell shows up there before it shows up anywhere else. [Periodic maintenance](installation_guidelines.md#periodic-maintenance) describes it in detail.

## What if my battery or inverter isn't supported yet, or I get stuck?
New integrations are welcome, but they need [real data](contributing/data_needed_for_new_battery_integration.md): CAN logs from a working vehicle covering idle, startup, charging and charge completion, plus logs from the standalone pack. Documentation fixes and issue triage are just as valuable as code — see [contributing](contributing/contributing.md). For questions, use the GitHub discussions and issue tracker, or join the community Discord.
