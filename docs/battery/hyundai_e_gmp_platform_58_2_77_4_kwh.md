---
title: "Hyundai E-GMP"
---

# Hyundai E-GMP (Electric Global Modular Platform)

Shared between the following models

* [Genesis GV60 (JW)](https://en.wikipedia.org/wiki/Genesis_GV60) (2021–present)
* [Hyundai Ioniq 5 (NE)](https://en.wikipedia.org/wiki/Hyundai_Ioniq_5) (2021–present)
* [Kia EV6 (CV)](https://en.wikipedia.org/wiki/Kia_EV6) (2021–present)
* [Hyundai Ioniq 6 (CE)](https://en.wikipedia.org/wiki/Hyundai_Ioniq_6) (2022–present)
* [Kia EV9 (MV)](https://en.wikipedia.org/wiki/Kia_EV9) (2023–present)
* [Kia EV5 (OV)](https://en.wikipedia.org/wiki/Kia_EV5) (2023–present)

## 800V battery specifications

* Manufacturer - SK Innovation
* Chemistry - Lithium nickel manganese cobalt oxides (NCM)
* Format - Pouch
* Weight 
  * 10.5kg / module
  * 0.8625kg / cell

### 58.2kWh battery

* weight approx. 369 kg
* 144s2p, 24 modules of 6 groups
* nominal voltage 144*3.66=527 V
* max voltage 144*4.2=604.8 V
* min voltage 144*3=432 V
* Cell type NCM811
* Applications
  * 37501-GI100 is Ioniq 5, to 2022
  * 37501-GI150 is Ioniq 5, 2022 to 2023

### 63.0kWh battery

* 144s2p

### 72.6kWh battery

* weight approx. 450kg
* 180s2p, 30 modules of 6 groups
* nominal voltage 180*3.66=659 V
* max voltage 180*4.2=756 V
* min voltage 180*3=540 V
* Cell type NCM811

### 77.4kWh battery 

* weight 
  * pack 477 kg
  * cells 331 kg
* 192s2p, 32 modules of 6 groups
* nominal voltage 192*3.66=703 V
* nominal capacity = 111.11 Ah
* max voltage 192*4.2=806 V
* min voltage 192*3=576 V
* energy density 162 Wh/kg
* power
  * peak 239 kW (10 sec)
  * continuous 188 kW 
* Cell type NCM811
* Applications
  * 37501-GI300 is Ioniq 5
  * 37501-GI301 is Ioniq 5
  * 37501-GI351 is Ioniq 5
  * 37501-KL450 is Ioniq 6

### 84.0 kWh battery

* 192s2p
* Applications
  * 37501-NI050 is Ioniq 5 N

## Software configuration
For this battery type, use the option called "Kia/Hyundai EGMP platform" under the "Battery Protocol" setting.

![image](../images/hyundai-e-gmp-platform-58-2-77-4-kwh-01.png){ width="654" height="154" }

## Note on CAN-FD
The 800V battery architecture uses CAN-FD, so incase you plan on integrating this battery, you will need to get the [CAN-FD chip add-on](../setup/can_related/can_fd_add_on_mcp2518fd.md) , or even easier, get the Stark CMR hardware.

## Wiring diagram
See [KIA EV6 Battery](kia_ev6.md)

### More information about battery and it's internals
[batterydesign](https://www.batterydesign.net/2022-kia-ev6/)

