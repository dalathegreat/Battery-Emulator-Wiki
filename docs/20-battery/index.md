---
title: Supported batteries
hide:
  - toc
---

# Supported batteries list

Be sure to checkout the [installation guidelines](https://github.com/dalathegreat/Battery-Emulator/wiki/Installation-guidelines) section for how to install your battery. Amount of stars ⭐ signal how mature and stable the integration is.

- ⭐ Works, but many values estimated or functionality missing. Expect manual tweaking to keep battery operational
- ⭐⭐ Integration has minor known issues or missing features. Manual interventions sometimes required.
- ⭐⭐⭐ Very well supported battery. Longterm stability confirmed without user interaction. Many success stories from users.

If the battery has a 🅱️ symbol, cell balancing has been confirmed working (Important for longterm operation)

If the battery has a 2️⃣ or 3️⃣ symbol, double- or triple battery is supported


| Car (Manufacturer) | Product Name | Capacity (kWh) | Supported status | Support level | Balancing (🅱️) | Parallel Packs (2️⃣/3️⃣) | Voltage min (V) | Voltage max (V) | Notes |
| :--------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| BMW | [BMW i3 (all sizes)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BMW-i3) | 18 / 22 / 40 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 270 | 400 | Balancing only when powered off |
| BMW | [iX & i4-7 Platform](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BMW-iX,-i4%E2%80%90i7-(Gen5-platform)) | 68 / 80.7 | ✅ | ⭐⭐ | 🅱️ |  | 270 | 464 | Manual contactor control |
| BMW | [PHEV (330e/530e etc)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BMW-PHEV-(Gen-3&4-platform)) | 12/24 | ⚠️ | Testing ongoing (2021+ Gen4 CAN logs wanted!) |  |  | 270 | 400 | Manual contactor control |
| BYD | [BYD Atto 3](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BYD-vehicle-(Atto-3-%E2%80%90-Seal-%E2%80%90-Tang-%E2%80%90-Dolphin-%E2%80%90-Song-%E2%80%90-and-more!)) | 50 / 60 | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| BYD | [BYD Yuan Plus](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BYD-vehicle-(Atto-3-%E2%80%90-Seal-%E2%80%90-Tang-%E2%80%90-Dolphin-%E2%80%90-Song-%E2%80%90-and-more!)) | 50 / 60 | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| BYD | [BYD Dolphin mini/E3](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BYD-vehicle-(Atto-3-%E2%80%90-Seal-%E2%80%90-Tang-%E2%80%90-Dolphin-%E2%80%90-Song-%E2%80%90-and-more!)) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 307 | 332 |  |
| BYD | [BYD Seal](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BYD-vehicle-(Atto-3-%E2%80%90-Seal-%E2%80%90-Tang-%E2%80%90-Dolphin-%E2%80%90-Song-%E2%80%90-and-more!)) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 380/510 | 440/597 |  |
| BYD | [BYD Song](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BYD-vehicle-(Atto-3-%E2%80%90-Seal-%E2%80%90-Tang-%E2%80%90-Dolphin-%E2%80%90-Song-%E2%80%90-and-more!)) | Multiple | ✅ | ⭐⭐ |  | 2️⃣ | 380 | 440 |  |
| Chevrolet | [Bolt](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Ampera%E2%80%90e-64-kWh) | 60/66 | ✅ | ⭐ |  |  | 330 | 403 |  |
| Citroen | [Basalt (Stellantis CMP Smart Car)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-CMP-Smart-Car-platform) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Citroen | [C-Zero](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-i%E2%80%90Miev-CZero-Ion) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Citroen | [ë-C3 / Aircross (Stellantis CMP Smart Car)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-CMP-Smart-Car-platform) | 29/44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Citroen | [ë-C4 2020+ (Stellantis eCMP)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot)) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Citroen | [Spacetourer (Stellantis eCMP)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot)) | 50/75 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Dacia | [Spring](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Dacia-Spring-%E2%80%90-Renault-K%E2%80%90ZE) | 27 | ✅ | ⭐⭐ |  | 2️⃣ | 216 | 302 |  |
| Fiat | [Grande Panda (Stellantis CMP Smart Car)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-CMP-Smart-Car-platform) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Ford | [Mustang Mach-E](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Ford-Mach%E2%80%90E) | 66/88 | ✅ | ⭐⭐ |  |  | 300 | 410 |  |
| Ford | [E-Transit](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Ford-Mach%E2%80%90E) | 66 | ✅ | ⭐⭐ |  |  | 300 | 410 |  |
| Geely | [Geometry C](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Geely-Geometry-C) | 53/70 | ⚠️ | Testing ongoing |  |  | 270 | 417* |  |
| Hyundai | [E‐GMP platform](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Hyundai-E%E2%80%90GMP-platform-(58.2-%E2%80%90-77.4-kWh)) |58.2/72.6/77.4/84 | ⚠️ | Integration ongoing! |  |  | 430 | 806 | SoC not updating, contactors not closing |
| Hyundai | [Kona 39/64kWh](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Kia-Niro---Hyundai-Kona-64-kWh) | 39/64 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 230 | 410* |  |
| Hyundai | [Kona Hybrid](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Kia-Niro-Hybrid) | 2 | ⚠️ | Testing ongoing |  |  |  |  |  |
| Hyundai | [Santa Fe PHEV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Hyundai-Santa-Fe-PHEV) | 14 | ✅ | ⭐⭐ |  |  | 290 | 400 |  |
| Jaguar | [I-PACE](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Jaguar-I%E2%80%90PACE) | 90 | ⚠️ | Testing ongoing |  |  |  |  |  |
| Kia | [e-Niro 39/64kWh](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Kia-Niro---Hyundai-Kona-64-kWh) | 39/64 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 230 | 410* |  |
| Kia | [Niro HEV / Ceed PHEV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Kia-Niro-Hybrid) | 2 / 8.9 | ✅ | ⭐ |  |  |  |  |  |
| Kia | [XCeed PHEV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:%E2%80%90Kia%E2%80%90Xceed%E2%80%90PHEV) | 8.9 | ⚠️ | Integration ongoing! |  |  | 240 | 413 |  |
| Kia | [EV6](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Kia-EV6) | 58.2/72.6/77.4 | ⚠️ | Testing ongoing |  |  | 430 | 806 | SoC not updating, contactors not closing |
| Land Rover | [Land Rover](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Land-Rover) |  | ⚠️ | Untested base added |  |  |  |  |  |
| Mini | [Cooper electric](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-BMW-i3) | 32 | ✅ | ⭐⭐⭐ | 🅱️ |  | 270 | 400 |  |
| Mitsubishi | [i-Miev](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-i%E2%80%90Miev-CZero-Ion) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Mitsubishi | [eK X EV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Nissan-Sakura---Mitsubishi-eK-X-EV) | 20 | ✅ | ⭐ |  |  | 300 | 400 |  |
| MG | [HS PHEV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-MG-HS-PHEV) | 16 | ✅ | ⭐ | 🅱️ (Automatic) |  | 310 | 378 |  |
| MG | [MG4](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-MG4) | 51/64/77 | ⚠️ | Testing ongoing |  |  | 260 | 470 |  |
| MG | [MG5 - Marvel R](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-MG5-%E2%80%90-Marvel-R) | 50/52/61/70 | ✅ | ⭐⭐ | 🅱️ |  | 268 | 438 |  |
| Nissan | [Ariya](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Nissan-Ariya) | 87/63 | ⚠️ | CAN logs wanted |  |  |  |  |  |
| Nissan | [LEAF](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Nissan-LEAF---e%E2%80%90NV200) | 24/30/40/62 | ✅ | ⭐⭐⭐ | 🅱️ | 3️⃣ | 300 | 400 |  |
| Nissan | [e-NV200](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Nissan-LEAF---e%E2%80%90NV200) | 24/40 | ✅ | ⭐⭐⭐ | 🅱️ | 3️⃣ | 300 | 400 |  |
| Nissan | [Sakura](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Nissan-Sakura---Mitsubishi-eK-X-EV) | 20 | ✅ | ⭐ |  |  | 300 | 400 |  |
| Opel | [eCorsa 2020+ (Stellantis eCMP)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot)) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Opel | [Frontera (Stellantis CMP Smart Car)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-CMP-Smart-Car-platform) | 44 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 350 |  |
| Opel | [Ampera-e](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Ampera%E2%80%90e-64-kWh) | 60/66 | ✅ | ⭐ |  |  | 330 | 403 |  |
| Peugeot | [e-208 2020+ (Stellantis eCMP)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot)) | 50 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Peugeot | [Ion](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-i%E2%80%90Miev-CZero-Ion) | 16 | ✅ | ⭐ | ⚠️ |  | 310 | 370 |  |
| Polestar | [2](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Volvo-XC40---Polestar-2) | 78 | ✅ | ⭐⭐ |  |  | 290 | 450 |  |
| Renault | [Kangoo](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Kangoo) | 22/33 | ✅ | ⭐⭐ |  |  | 300 | 400 |  |
| Renault | [Fluence ZE](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Fluence-ZE) | 22/36 | ✅ | ⭐ |  |  | 300 | 400 |  |
| Renault | [K‐ZE](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Dacia-Spring-%E2%80%90-Renault-K%E2%80%90ZE) | 27 | ✅ | ⭐⭐ |  |  | 216 | 302 |  |
| Renault | [Twizy](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Twizy) | 6.1 | ⚠️ | Testing ongoing |  |  | 48V | 48V |  |
| Renault | [Zoe Gen1](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Zoe-Gen1) | 22/41 | ✅ | ⭐⭐⭐ | 🅱️ (Automatic, Top Balancing) | 2️⃣ | 300 | 400 |  |
| Renault | [Zoe Gen2](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Renault-Zoe-Gen2) | 52 | ✅ | ⭐⭐⭐ | 🅱️ | 2️⃣ | 300 | 400 |  |
| Rivian | [R1T](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Rivian-R1T) | 135 | ✅ | ⭐⭐ |  |  | 300 | 400 |  |
| Tesla | [Model 3 & Y (all sizes)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Tesla-Model-S-3-X-Y) | All | ✅ | ⭐ | ⚠️ |  | 280 | 400 | Note, balancing only when contactors are opened! |
| Tesla | [Model S & X (2021+)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Tesla-Model-S-X) | All | ✅ | ⭐ |  |  | 310 | 460 | Note, balancing only when contactors are opened! |
| Tesla | [Model S & X (2012-2020)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Tesla-Model-S-X-2012%E2%80%902020) | All | ✅ | ⭐ |  |  | 280 | 400 |  |
| Toyota | [Proace (Stellantis eCMP)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot)) | 50/75 | ✅ | ⭐⭐ | 🅱️ |  | 320 | 450 |  |
| Volkswagen, Audi, Škoda, Cupra and Ford | [MEB Platform](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-MEB) | 48/55/61/82 | ✅ | ⭐⭐ | 🅱️ |  | 252 | 450* | Requires precharge circuit |
| Volkswagen, Audi, Škoda, Cupra and Ford | [MQB Evo 2024+ Platform](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-MQB) | 20 | ✅ | ⭐⭐ | 🅱️ |  | 300 | 400 | Requires precharge circuit |
| Volvo | [EX30](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Volvo-EX30) | 55/69 | ✅ | ⭐ |  |  | 300 | 460 |  |
| Volvo | [XC40/C40](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Volvo-XC40---Polestar-2) | 69/78/82 | ✅ | ⭐⭐ |  |  | 290 | 450 | Requires DC/DC load, can lock itself permanently |
| Volvo | [SPA PHEV](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Volvo-SPA-S60-90-V60-90-XC60-90-Hybrid-batteries) | 19 | ✅ | ⭐ |  |  | 290 | 450 | Requires DC/DC load, can lock itself permanently |

### Other batteries
* DIY HV battery:
   * [RJXZS BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-RJXZS-BMS) ✅
   * [Orion BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Orion-BMS) ✅
   * [Simp BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-SimpBMS) ✅
   * [DALY BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Daly-SmartBMS) ✅
   * [EMUS G1 BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-EMUS-G1-BMS) ✅
   * [Ennoid BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Ennoid-BMS) ⚠️ (Not tested)
* DIY LV battery:
   * [DALY BMS](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Daly-SmartBMS) ✅
* [FoxESS HV2600 batteries](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-FoxESS-HV2600) ✅
* [Pylon HV batteries (Dyness Tower)](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Pylon-HV) ✅
* [CHAdeMO vehicles](https://github.com/dalathegreat/Battery-Emulator/wiki/Chademo-vehicle) ⚠️ (Experimental support for emergencies)

