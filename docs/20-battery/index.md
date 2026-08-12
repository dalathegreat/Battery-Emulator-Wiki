---
title: Supported batteries
hide:
  - toc
---

# Supported batteries list

Be sure to checkout the [installation guidelines](../40-setup/10-hardware/Installation-guidelines.md) section for how to install your battery. Amount of stars ⭐ signal how mature and stable the integration is.

- ⭐ Works, but many values estimated or functionality missing. Expect manual tweaking to keep battery operational
- ⭐⭐ Integration has minor known issues or missing features. Manual interventions sometimes required.
- ⭐⭐⭐ Very well supported battery. Longterm stability confirmed without user interaction. Many success stories from users.

If the battery has a 🅱️ symbol, cell balancing has been confirmed working (Important for longterm operation)

If the battery has a 2️⃣ or 3️⃣ symbol, double- or triple battery is supported


| Car (Manufacturer) | Product Name | Capacity (kWh) | Supported status | Support level | Balancing (🅱️) | Parallel Packs (2️⃣/3️⃣) | Voltage min (V) | Voltage max (V) | Notes |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| BMW | [BMW i3 (all sizes)](BMW-i3.md) | 18 / 22 / 40 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 270 | 400 | Balancing only when powered off |
| BMW | [iX & i4-7 Platform](BMW-iX,-i4‐i7-(Gen5-platform).md) | 68 / 80.7 | ✅ | ⭐⭐ | 🅱️ |  | 270 | 464 | Manual contactor control |
| BMW | [PHEV (330e/530e etc)](BMW-PHEV-(Gen-3&4-platform).md) | 12/24 | ⚠️ | Testing ongoing (2021+ Gen4 CAN logs wanted!) |  |  | 270 | 400 | Manual contactor control |
| BYD | [BYD Atto 3](BYD-vehicle-(Atto-3-‐-Seal-‐-Tang-‐-Dolphin-‐-Song-‐-and-more!).md) | 50 / 60 | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| BYD | [BYD Yuan Plus](BYD-vehicle-(Atto-3-‐-Seal-‐-Tang-‐-Dolphin-‐-Song-‐-and-more!).md) | 50 / 60 | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| BYD | [BYD Dolphin mini/E3](BYD-vehicle-(Atto-3-‐-Seal-‐-Tang-‐-Dolphin-‐-Song-‐-and-more!).md) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 307 | 332 |  |
| BYD | [BYD Seal](BYD-vehicle-(Atto-3-‐-Seal-‐-Tang-‐-Dolphin-‐-Song-‐-and-more!).md) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 380/510 | 440/597 |  |
| BYD | [BYD Song](BYD-vehicle-(Atto-3-‐-Seal-‐-Tang-‐-Dolphin-‐-Song-‐-and-more!).md) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| Chevrolet | [Bolt](Ampera‐e-64-kWh.md) | 60/66 | ✅ | ⭐ |  |  | 330 | 403 |  |
| Citroen | [Basalt (Stellantis CMP Smart Car)](Stellantis-CMP-Smart-Car-platform.md) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Citroen | [C-Zero](i‐Miev-CZero-Ion.md) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Citroen | [ë-C3 / Aircross (Stellantis CMP Smart Car)](Stellantis-CMP-Smart-Car-platform.md) | 29/44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Citroen | [ë-C4 2020+ (Stellantis eCMP)](Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Citroen | [Spacetourer (Stellantis eCMP)](Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md) | 50/75 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Dacia | [Spring](Dacia-Spring-‐-Renault-K‐ZE.md) | 27 | ✅ | ⭐⭐ |  | 2️⃣ | 216 | 302 |  |
| Fiat | [Grande Panda (Stellantis CMP Smart Car)](Stellantis-CMP-Smart-Car-platform.md) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Ford | [Mustang Mach-E](Ford-Mach‐E.md) | 66/88 | ✅ | ⭐⭐ |  |  | 300 | 410 |  |
| Ford | [E-Transit](Ford-Mach‐E.md) | 66 | ✅ | ⭐⭐ |  |  | 300 | 410 |  |
| Geely | [Geometry C](Geely-Geometry-C.md) | 53/70 | ⚠️ | Testing ongoing |  |  | 270 | 417* |  |
| Hyundai | [E‐GMP platform](Hyundai-E‐GMP-platform-(58.2-‐-77.4-kWh).md) |58.2/72.6/77.4/84 | ⚠️ | Integration ongoing! |  |  | 430 | 806 | SoC not updating, contactors not closing |
| Hyundai | [Kona 39/64kWh](Kia-Niro---Hyundai-Kona-64-kWh.md) | 39/64 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 230 | 410* |  |
| Hyundai | [Kona Hybrid](Battery_‐Kia‐Niro‐Hybrid.md) | 2 | ⚠️ | Testing ongoing |  |  |  |  |  |
| Hyundai | [Santa Fe PHEV](Hyundai-Santa-Fe-PHEV.md) | 14 | ✅ | ⭐⭐ |  |  | 290 | 400 |  |
| Jaguar | [I-PACE](Jaguar-I‐PACE.md) | 90 | ⚠️ | Testing ongoing |  |  |  |  |  |
| Kia | [e-Niro 39/64kWh](Kia-Niro---Hyundai-Kona-64-kWh.md) | 39/64 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 230 | 410* |  |
| Kia | [Niro HEV / Ceed PHEV](Battery_‐Kia‐Niro‐Hybrid.md) | 2 / 8.9 | ✅ | ⭐ |  |  |  |  |  |
| Kia | [XCeed PHEV](Battery_‐Kia‐Xceed‐PHEV.md) | 8.9 | ⚠️ | Integration ongoing! |  |  | 240 | 413 |  |
| Kia | [EV6](Kia-EV6.md) | 58.2/72.6/77.4 | ⚠️ | Testing ongoing |  |  | 430 | 806 | SoC not updating, contactors not closing |
| Land Rover | [Land Rover](Land-Rover.md) |  | ⚠️ | Untested base added |  |  |  |  |  |
| Mini | [Cooper electric](BMW-i3.md) | 32 | ✅ | ⭐⭐⭐ | 🅱️ |  | 270 | 400 |  |
| Mitsubishi | [i-Miev](i‐Miev-CZero-Ion.md) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Mitsubishi | [eK X EV](Nissan-Sakura---Mitsubishi-eK-X-EV.md) | 20 | ✅ | ⭐ |  |  | 300 | 400 |  |
| MG | [HS PHEV](MG-HS-PHEV.md) | 16 | ✅ | ⭐ | 🅱️ (Automatic) |  | 310 | 378 |  |
| MG | [MG4](MG4.md) | 51/64/77 | ⚠️ | Testing ongoing |  |  | 260 | 470 |  |
| MG | [MG5 - Marvel R](MG5-‐-Marvel-R.md) | 50/52/61/70 | ✅ | ⭐⭐ | 🅱️ |  | 268 | 438 |  |
| Nissan | [Ariya](Nissan-Ariya.md) | 87/63 | ⚠️ | CAN logs wanted |  |  |  |  |  |
| Nissan | [LEAF](Nissan-LEAF---e‐NV200.md) | 24/30/40/62 | ✅ | ⭐⭐⭐ | 🅱️ | 3️⃣ | 300 | 400 |  |
| Nissan | [e-NV200](Nissan-LEAF---e‐NV200.md) | 24/40 | ✅ | ⭐⭐⭐ | 🅱️ | 3️⃣ | 300 | 400 |  |
| Nissan | [Sakura](Nissan-Sakura---Mitsubishi-eK-X-EV.md) | 20 | ✅ | ⭐ |  |  | 300 | 400 |  |
| Opel | [eCorsa 2020+ (Stellantis eCMP)](Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Opel | [Frontera (Stellantis CMP Smart Car)](Stellantis-CMP-Smart-Car-platform.md) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Opel | [Ampera-e](Ampera‐e-64-kWh.md) | 60/66 | ✅ | ⭐ |  |  | 330 | 403 |  |
| Peugeot | [e-208 2020+ (Stellantis eCMP)](Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Peugeot | [Ion](i‐Miev-CZero-Ion.md) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Polestar | [2](Volvo-XC40---Polestar-2.md) | 78 | ✅ | ⭐⭐ |  |  | 290 | 450 |  |
| Renault | [Kangoo](Renault-Kangoo.md) | 22/33 | ✅ | ⭐⭐ |  |  | 300 | 400 |  |
| Renault | [Fluence ZE](Renault-Fluence-ZE.md) | 22/36 | ✅ | ⭐ |  |  | 300 | 400 |  |
| Renault | [K‐ZE](Dacia-Spring-‐-Renault-K‐ZE.md) | 27 | ✅ | ⭐⭐ |  |  | 216 | 302 |  |
| Renault | [Twizy](Renault-Twizy.md) | 6.1 | ⚠️ | Testing ongoing |  |  | 48V | 48V |  |
| Renault | [Zoe Gen1](Renault-Zoe-Gen1.md) | 22/41 | ✅ | ⭐⭐⭐ | 🅱️ (Automatic, Top Balancing) | 2️⃣ | 300 | 400 |  |
| Renault | [Zoe Gen2](Renault-Zoe-Gen2.md) | 52 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 300 | 400 |  |
| Rivian | [R1T](Rivian-R1T.md) | 135 | ✅ | ⭐⭐ |  |  | 300 | 400 |  |
| Tesla | [Model 3 & Y (all sizes)](Tesla-Model-S-3-X-Y.md) | All | ✅ | ⭐ | ⚠️ |  | 280 | 400 | Note, balancing only when contactors are opened! |
| Tesla | [Model S & X (2021+)](Tesla-Model-S-X.md) | All | ✅ | ⭐ |  |  | 310 | 460 | Note, balancing only when contactors are opened! |
| Tesla | [Model S & X (2012-2020)](Tesla-Model-S-X-2012‐2020.md) | All | ✅ | ⭐ |  |  | 280 | 400 |  |
| Toyota | [Proace (Stellantis eCMP)](Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md) | 50/75 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Volkswagen, Audi, Škoda, Cupra and Ford | [MEB Platform](MEB.md) | 48/55/61/82 | ✅ | ⭐⭐ | 🅱️ |  | 252 | 450* | Requires precharge circuit |
| Volkswagen, Audi, Škoda, Cupra and Ford | [MQB Evo 2024+ Platform](MQB.md) | 20 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 400 | Requires precharge circuit |
| Volvo | [EX30](Volvo-EX30.md) | 55/69 | ✅ | ⭐ |  |  | 300 | 460 |  |
| Volvo | [XC40/C40](Volvo-XC40---Polestar-2.md) | 69/78/82 | ✅ | ⭐⭐ |  |  | 290 | 450 | Requires DC/DC load, can lock itself permanently |
| Volvo | [SPA PHEV](Volvo-SPA-S60-90-V60-90-XC60-90-Hybrid-batteries.md) | 19 | ✅ | ⭐ |  |  | 290 | 450 | Requires DC/DC load, can lock itself permanently |

### Other batteries
* DIY HV battery:
   * [RJXZS BMS](RJXZS-BMS.md) ✅
   * [Orion BMS](Orion-BMS.md) ✅
   * [Simp BMS](SimpBMS.md) ✅
   * [DALY BMS](Daly-SmartBMS.md) ✅
   * [EMUS G1 BMS](EMUS-G1-BMS.md) ✅
   * [Ennoid BMS](Ennoid-BMS.md) ⚠️ (Not tested)
* DIY LV battery:
   * [DALY BMS](Daly-SmartBMS.md) ✅
* [FoxESS HV2600 batteries](FoxESS-HV2600.md) ✅
* [Pylon HV batteries (Dyness Tower)](Pylon-HV.md) ✅
* [CHAdeMO vehicles](Chademo-vehicle.md) ⚠️ (Experimental support for emergencies)

