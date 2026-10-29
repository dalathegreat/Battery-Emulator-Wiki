---
title: "Compatible batteries"
hide:
  - toc
---

# Compatible batteries list

Be sure to checkout the [installation guidelines](../setup/installation_guidelines.md) section for how to install your battery. Amount of stars ⭐ signal how mature and stable the integration is.

- ⭐⭐⭐ Fully compatible battery. Longterm stability confirmed without user interaction. Many success stories from users.
- ⭐⭐ Integration has minor known issues or missing features. Manual interventions sometimes required.
- ⭐ Works, but many values estimated or functionality missing. Expect manual tweaking to keep battery operational.
- 🅱️ Cell balancing has been confirmed working (Important for longterm operation). Note that some batteries require powering off / opening contactors to balance, which can make them unsuitable for offgrid applications
- 2️⃣ Compatible with Double battery (two identical packs in parallel, see [Double Battery](../setup/software/battery_2x.md)).
- 3️⃣ Compatible with Triple battery (see [Triple Battery](../setup/software/battery_3x.md)). Every triple-capable integration is also compatible with double.

**Contactor control:** **CAN** means the battery closes its own contactors on CAN messages from the emulator. **GPIO** means the contactors are switched by hardwired 12 V signals, which the emulator can drive from its GPIO outputs, see [Contactor control via GPIO](../setup/software/contactor_control_via_gpio_pins.md).

| Car (Manufacturer)<br>Product Name | Capacity (kWh)<br>Voltage min / max (V) | Compatibility | Balancing | Parallel Packs | Contactor control | Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Aiways<br>[U5](wip/aiways_u5_2021.md) | 63 | ⚠️ Wiring documented, integration not started |  |  |  |  |
| Akasol<br>[Akasystems](akasol_battery.md) | 33<br>540 / 756 | ⭐ |  |  | CAN |  |
| BMW<br>[i3 (all sizes)](bmw_i3.md) | 18 / 22 / 40<br>259 / 403 | ⭐⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>1</sup> |
| BMW<br>[iX & i4-7 Platform](bmw_ix_i4_i7_gen5_platform.md) | 68 / 80.7<br>218 / 464 | ⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| BMW<br>[PHEV (330e/530e etc)](bmw_phev_gen_3_and_4_platform.md) | 12/24<br>300 / 465 | ⚠️ Testing ongoing (2021+ Gen4 CAN logs wanted!) |  |  | CAN |  |
| BYD<br>[Atto 3](byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) | 50 / 60<br>380 / 440 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>2</sup> |
| BYD<br>[Yuan Plus](byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) | 50 / 60<br>380 / 440 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>2</sup> |
| BYD<br>[Dolphin mini/E3](byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) | Multiple<br>307 / 332 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>2</sup> |
| BYD<br>[Seal](byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) | Multiple<br>380/510 / 440/597 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>2</sup> |
| BYD<br>[Song](byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) | Multiple<br>380 / 440 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>2</sup> |
| Chevrolet<br>[Bolt](ampera_e_64_kwh.md) | 60/66<br>251 / 404 | ⭐ |  | 2️⃣ | GPIO |  |
| Citroen<br>[Basalt (Stellantis CMP Smart Car)](stellantis_cmp_smart_car_platform.md) | 44<br>290 / 370 | ⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| Citroen<br>[C-Zero](i_miev_czero_ion.md) | 16<br>316 / 370 | ⭐ | ⚠️ |  | GPIO |  |
| Citroen<br>[ë-C3 / Aircross (Stellantis CMP Smart Car)](stellantis_cmp_smart_car_platform.md) | 29/44<br>290 / 370 | ⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| Citroen<br>[ë-C4 2020+ (Stellantis eCMP)](stellantis_ecmp_citroen_ds_opel_peugeot.md) | 50<br>358 / 455 | ⭐⭐ | 🅱️ | 2️⃣3️⃣ | CAN |  |
| Citroen<br>[Spacetourer (Stellantis eCMP)](stellantis_ecmp_citroen_ds_opel_peugeot.md) | 50/75<br>358 / 455 | ⭐⭐ | 🅱️ | 2️⃣3️⃣ | CAN |  |
| Dacia<br>[Spring](dacia_spring_renault_k_ze.md) | 27<br>216 / 302 | ⭐⭐ |  | 2️⃣3️⃣ | GPIO |  |
| Fiat<br>[Grande Panda (Stellantis CMP Smart Car)](stellantis_cmp_smart_car_platform.md) | 44<br>290 / 370 | ⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| Fisker<br>[Ocean](wip/fisker_ocean.md) | 73 / 106 / 113 | ⚠️ Work in progress |  |  |  |  |
| Ford<br>[Mustang Mach-E](ford_mach_e.md) | 66/88<br>249 / 414 | ⭐⭐ |  |  | CAN |  |
| Ford<br>[E-Transit](ford_mach_e.md) | 66<br>300 / 410 | ⭐⭐ |  |  | CAN |  |
| Ford<br>[F‐150 Lightning](wip/ford_f_150_lightning.md) | 107 / 143 gross | ⚠️ Work in progress |  |  | CAN |  |
| Geely<br>[Geometry C](geely_geometry_c.md) | 53/70<br>270 / 442 | ⚠️ Testing ongoing |  |  |  | <sup>3</sup> |
| Geely<br>[GEA platform (Galaxy, eMAS)](wip/geely_gea_platform_galaxy_emas.md) |  | ⚠️ Work in progress |  |  |  |  |
| Hyundai<br>[E‐GMP platform](hyundai_e_gmp_platform_58_2_77_4_kwh.md) | 58.2/72.6/77.4/84<br>430 / 806 | ⚠️ Integration ongoing! |  |  | CAN | <sup>4</sup> |
| Hyundai<br>[Ioniq Electric 28kWh](kia_niro_hyundai_kona.md) | 28<br>288 / 405 | ⚠️ Not confirmed by users yet |  |  | CAN |  |
| Hyundai<br>[Kona 39/64kWh](kia_niro_hyundai_kona.md) | 39/64<br>230 / 410 | ⭐⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>3,5</sup> |
| Hyundai<br>[Kona Hybrid](kia_niro_hybrid.md) | 2 | ⚠️ Testing ongoing |  |  |  |  |
| Hyundai<br>[Santa Fe PHEV](hyundai_santa_fe_phev.md) | 14<br>290 / 400 | ⭐⭐ |  | 2️⃣ | CAN |  |
| Jaguar<br>[I-PACE](jaguar_i_pace.md) | 90 | ⚠️ Testing ongoing |  |  | GPIO |  |
| Kia<br>[e-Niro 39/64kWh](kia_niro_hyundai_kona.md) | 39/64<br>230 / 410 | ⭐⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>3,5</sup> |
| Kia<br>[Niro HEV / Ceed PHEV](kia_niro_hybrid.md) | 2 / 8.9 | ⭐ |  |  |  |  |
| Kia<br>[XCeed PHEV](wip/kia_xceed_phev.md) | 8.9<br>300 / 404 | ⚠️ Integration ongoing! |  |  |  |  |
| Kia<br>[EV6](kia_ev6.md) | 58.2/72.6/77.4<br>430 / 806 | ⚠️ Testing ongoing |  |  | CAN | <sup>4</sup> |
| Kia<br>[Soul EV](wip/kia_soul.md) | 27 / 30 | ⚠️ Work in progress |  |  | GPIO |  |
| Land Rover<br>[Land Rover](wip/land_rover.md) |  | ⚠️ Untested base added |  |  |  |  |
| Maxus<br>[eD3 / eDeliver 3](wip/maxus_ed3.md) | 35 / 50.2 / 52.5 | ⚠️ Work in progress |  |  |  |  |
| Maxus<br>[EV80](wip/maxus_ev80.md) |  | ⚠️ Needs an aftermarket BMS, no contactors or shunt in pack |  |  |  |  |
| Mercedes<br>[B250E "W246"](mercedes_b_class_b250e_w246.md) | 36<br>250 / 350 | ⭐ |  |  | CAN | <sup>6</sup> |
| Mini<br>[Cooper electric](bmw_i3.md) | 32<br>259 / 403 | ⭐⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| Mitsubishi<br>[i-Miev](i_miev_czero_ion.md) | 16<br>316 / 370 | ⭐ | ⚠️ |  | GPIO |  |
| Mitsubishi<br>[eK X EV](nissan_sakura_mitsubishi_ek_x_ev.md) | 20<br>300 / 400 | ⭐ |  |  | GPIO |  |
| MG<br>[HS PHEV](mg_hs_phev.md) | 16<br>310 / 378 | ⭐ | 🅱️ (Automatic) | 2️⃣ | CAN |  |
| MG<br>[MG4](wip/mg4.md) | 51/64/77<br>260 / 470 | ⚠️ Testing ongoing |  |  | CAN |  |
| MG<br>[MG5 - Marvel R](mg5_marvel_r.md) | 50/52/61/70<br>268 / 438 | ⭐⭐ | 🅱️ | 2️⃣ | CAN | <sup>7</sup> |
| MG<br>[ZS](mg_zs.md) | 44.5 / 69.9 | ⭐ |  | 2️⃣ | CAN | <sup>8</sup> |
| Nissan<br>[Ariya](wip/nissan_ariya.md) | 87/63 | ⚠️ CAN logs wanted |  |  | GPIO |  |
| Nissan<br>[LEAF](nissan_leaf_e_nv200.md) | 24/30/40/62<br>240 / 406 | ⭐⭐⭐ | 🅱️ | 2️⃣3️⃣ | GPIO |  |
| Nissan<br>[e-NV200](nissan_leaf_e_nv200.md) | 24/40<br>240 / 406 | ⭐⭐⭐ | 🅱️ | 2️⃣3️⃣ | GPIO |  |
| Nissan<br>[Sakura](nissan_sakura_mitsubishi_ek_x_ev.md) | 20<br>300 / 400 | ⭐ |  |  | GPIO |  |
| Omoda<br>[E5](wip/omoda.md) | 58.9 | ⚠️ Work in progress |  |  |  |  |
| Opel<br>[eCorsa 2020+ (Stellantis eCMP)](stellantis_ecmp_citroen_ds_opel_peugeot.md) | 50<br>358 / 455 | ⭐⭐ | 🅱️ | 2️⃣3️⃣ | CAN |  |
| Opel<br>[Frontera (Stellantis CMP Smart Car)](stellantis_cmp_smart_car_platform.md) | 44<br>290 / 370 | ⭐⭐ | 🅱️ | 2️⃣ | CAN |  |
| Opel<br>[Ampera-e](ampera_e_64_kwh.md) | 60/66<br>251 / 404 | ⭐ |  | 2️⃣ | GPIO |  |
| Peugeot<br>[e-208 2020+ (Stellantis eCMP)](stellantis_ecmp_citroen_ds_opel_peugeot.md) | 50<br>358 / 455 | ⭐⭐ | 🅱️ | 2️⃣3️⃣ | CAN |  |
| Peugeot<br>[Ion](i_miev_czero_ion.md) | 16<br>316 / 370 | ⭐ | ⚠️ |  | GPIO |  |
| Polestar<br>[2](volvo_spa_xc40_polestar2.md) | 78<br>290 / 450 | ⭐⭐ |  |  | CAN |  |
| Porsche, Audi<br>[Taycan / e-tron GT (MSB)](wip/taycan_e_tron.md) | 79.2 / 93.4 | ⚠️ Work in progress |  |  |  |  |
| Renault<br>[Kangoo](renault_kangoo.md) | 22/33<br>250 / 415 | ⭐⭐ |  |  | GPIO |  |
| Renault<br>[Fluence ZE](renault_fluence_ze.md) | 22/36<br>300 / 400 | ⭐ |  |  |  |  |
| Renault<br>[K‐ZE](dacia_spring_renault_k_ze.md) | 27<br>216 / 302 | ⭐⭐ |  | 2️⃣3️⃣ | GPIO |  |
| Renault<br>[Twizy](renault_twizy.md) | 6.1<br>48 / 58 | ⚠️ Testing ongoing |  |  |  |  |
| Renault<br>[Zoe Gen1](renault_zoe_gen1.md) | 22/41<br>300 / 400 | ⭐⭐⭐ | 🅱️ (Automatic, Top Balancing) | 2️⃣ | GPIO |  |
| Renault<br>[Zoe Gen2](renault_zoe_gen2.md) | 52<br>300 / 410 | ⭐⭐⭐ | 🅱️ | 2️⃣ | GPIO |  |
| Rivian<br>[R1T](rivian_r1t.md) | 135<br>292 / 448 | ⭐⭐ |  |  | CAN |  |
| Seres<br>[3 / E3](wip/seres_3.md) | 53.61 | ⚠️ Work in progress |  |  |  |  |
| Smart<br>[EQ Fortwo / Forfour](wip/smart_eq_fortwo_forfour.md) |  | ⚠️ Work in progress |  |  |  |  |
| Sono Motors<br>Sion | 54<br>250 / 500 | ⚠️ Not confirmed by users yet |  |  |  |  |
| Tesla<br>[Model 3 & Y (all sizes)](tesla_model_3_y.md) | All<br>280 / 400 | ⭐ | ⚠️ | 2️⃣ | CAN | <sup>2</sup> |
| Tesla<br>[Model S & X (2021+)](tesla_model_s_x_2021.md) | All<br>285 / 460 | ⭐ |  | 2️⃣ | CAN | <sup>2</sup> |
| Tesla<br>[Model S & X (2012-2020)](tesla_model_s_x_2012_2020.md) | All<br>280 / 400 | ⭐ |  |  | CAN |  |
| Stellantis<br>[Pro One / MCA (Ducato, ProMaster, Boxer, Jumper, Movano, Proace Max)](stellantis_pro_one.md) | 110<br>288 / 378 | ⭐ |  |  | CAN |  |
| Stellantis<br>[SmallWide 4x4 (Renegade, 500X, Compass, Tonale)](stellantis_smallwide_4x4.md) |  | ⚠️ Work in progress |  |  |  |  |
| Stellantis<br>[SMP platform](wip/stellantis_smp_platform.md) |  | ⚠️ Work in progress |  |  |  |  |
| Think<br>[City](think_city.md) |  | ⭐ |  |  | CAN | <sup>9</sup> |
| Toyota<br>[Proace (Stellantis eCMP)](stellantis_ecmp_citroen_ds_opel_peugeot.md) | 50/75<br>358 / 455 | ⭐⭐ | 🅱️ | 2️⃣3️⃣ | CAN |  |
| Volkswagen, Audi, Škoda, Cupra and Ford<br>[MEB Platform](vw_meb.md) | 48/55/61/82<br>252 / 450 | ⭐⭐ | 🅱️ |  | CAN | <sup>3,10</sup> |
| Volkswagen, Audi, Škoda, Cupra and Ford<br>[MQB Evo 2024+ Platform](vw_mqb.md) | 20<br>288 / 403 | ⭐⭐ | 🅱️ |  | CAN | <sup>10</sup> |
| Volvo<br>[EX30](volvo_sea_ex30.md) | 55/69<br>312 / 452 | ⭐ |  |  | CAN |  |
| Volvo<br>[XC40/C40](volvo_spa_xc40_polestar2.md) | 69/78/82<br>262 / 454 | ⭐⭐ |  |  | CAN | <sup>11</sup> |
| Volvo<br>[SPA PHEV](volvo_spa_s60_90_v60_90_xc60_90_hybrid_batteries.md) | 19<br>275 / 429 | ⭐ |  |  | CAN | <sup>11</sup> |

**Notes**

1. Cell balancing only works while the battery is powered off.
2. Cell balancing only works while the contactors are open.
3. The voltage range covers all pack variants supported (cell count is detected at runtime).
4. SoC not updating and contactors not closing.
5. CAN-FD models (Kia 64 kWh FD) need external contactor control via GPIO, see the [battery page](kia_niro_hyundai_kona.md).
6. Uses the Tesla Model S/X 2012-2020 protocol.
7. Double battery is only supported via the MG Gen1 integration.
8. Uses the MG Gen1 protocol. No LFP packs tested yet.
9. Molten salt or NCM variants. Isolation monitoring is very sensitive.
10. Requires a precharge circuit.
11. Requires a DC/DC load, otherwise the battery can lock itself permanently.

### Other batteries

DIY HV battery:

* [RJXZS BMS](bms/rjxzs_bms.md) ✅
* [Orion BMS](bms/orion_bms.md) ✅
* [Simp BMS](bms/simpbms.md) ✅
* [DALY BMS](bms/daly_smartbms.md) ✅
* [EMUS G1 BMS](bms/emus_g1_bms.md) ✅
* [Ennoid BMS](bms/ennoid_maxkgo_bms.md) ⚠️
  (Not tested)
* [Batrium BMS](bms/batrium_bms.md) ✅
* [Cellpower BMS](bms/cellpower_bms.md) ✅ (250kbps CAN, needs its own CAN channel)
* [Growatt ARK HV BMS](bms/growatt_ark_bms_hv.md) ✅
* [Thunderstruck BMS](bms/thunderstruck_bms.md) ⚠️ (Work in progress)

DIY LV battery:

* [DALY BMS](bms/daly_smartbms.md) ✅

[Growatt 48V LV batteries](growatt_lv.md) ✅

[Relion LV 48V batteries](relion_lv.md) ✅ 2️⃣3️⃣

[FoxESS HV2600 batteries](foxess_hv2600.md) ✅

[Pylon HV batteries (Dyness Tower)](pylon_hv.md) ✅ 2️⃣

BYD Battery-Box Premium ⚠️ (Not confirmed by users yet)

Samsung SDI LV batteries ⚠️ (Not confirmed by users yet)

[CHAdeMO vehicles](wip/chademo_vehicle.md) ⚠️ (Experimental compatibility)

[CCS bidirectional charging](wip/ccs_bidirectional_charging.md) ⚠️ (Experimental compatibility)

