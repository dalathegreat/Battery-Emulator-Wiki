---
title: "Akasol Akasystem 15 OEM 50 PRC"
---

## Compatible batteries

AKASOL AKASYSTEM 15 OEM 50 PRC — a single-tray, 655 V nominal NMC pack (180 cells, 50 Ah, ~33 kWh) with one BMM01 controller.

Note: Only the single-tray BMM01 variant is implemented. Multi-tray systems use a different addressing scheme and are not covered.

### Physical Dimensions

| Parameter             | Value               |
| --------------------- | ------------------- |
| Pack Size (L × W × H) | 1700 × 700 × 150 mm |
| Weight                | 270 kg              |

### Electrical data

| Parameter                   | Value                              |
| --------------------------- | ---------------------------------- |
| Nominal voltage             | 655 V                              |
| Voltage range               | 540 – 756 V                        |
| Capacity                    | 50 Ah                              |
| Energy                      | 33 kWh                             |
| Cells                       | 180 in series (15 modules × 12s1p) |
| Chemistry                   | NMC                                |
| Internal HV fuse            | 200 A                              |
| Continuous charge power     | 45 kW                              |
| Continuous discharge power  | 50 kW (RMS)                        |
| Protection class            | IP67 / IP6K9K                      |
| Operating temperature range | −30 °C to +60 °C                   |

The pack reports far higher current limits than a typical inverter battery port accepts (roughly 137 A charge / 180 A discharge have been seen on the bus). The driver clamps to 30 A before the value reaches the datalayer.

### Special considerations

- The CAN bus is 250kbps on this battery, so it needs to be on its own separate CAN network
- Startup sequence: The battery requires a specific startup signal via KL30 / KL30_Safe / KL15. This has been implemented via the Pre/Neg/Pos contactor pins used in BE
- The LV supply is nominally **24 V**, not 12 V. The manual's integration chapter specifies 24 V, while the safety chapter refers to the safe-power signal as "12 V or 24 V". No voltage window is published, and the KL30 min/max thresholds are listed as optional parameters, so they may vary per unit. 24 V is the documented choice and is what this installation runs
- The pack closes its own HV contactors over CAN once it reaches Operational. GPIO contactor control in BE must stay disabled — the driver uses those three pins for KL30 / KL30_Safe / Wake instead
- The HV interlock (HVIL) loop must be closed, or the contactors will not close
- Liquid cooled. The battery must be kept inside its temperature range by an external thermal circuit

## Software configuration

For this battery type, use the option called "AKASOL" under the "Battery Protocol" section.

The three discrete control signals are taken from the HAL's contactor pins, so the mapping follows whatever the selected board defines:

| BE HAL pin                 | Akasol signal       |
| -------------------------- | ------------------- |
| `PRECHARGE_PIN()`          | KL30                |
| `NEGATIVE_CONTACTOR_PIN()` | KL30_Safe           |
| `POSITIVE_CONTACTOR_PIN()` | KL15 / Battery Wake |

On a LilyGo T-2CAN that is GPIO 21, 17 and 48 respectively.

The driver holds each step long enough for the previous one to settle: KL30_Safe alone for 500 ms, then KL30 added for 1000 ms, then Wake. Once the battery reports Standby it sends `req_batuse=1`. A `VCU1_to_BMM01` frame goes out every 100 ms with a rolling alive counter.

An equipment stop withdraws `req_batuse` rather than dropping Battery_Wake, which is the shutdown order the manual specifies (chapter 6.2.2). The request is held until the pack current the battery itself reports has settled, so the contactors do not open under load.

## Part numbers

Part numbers below are the ones AKASOL specifies in the user manual (doc 3-024001TEN_0001 v1.2). Search links are generic — check the listing matches the exact part number before ordering.

| Component | Part Number | Purchase Link |
| --------- | ----------- | ------------- |
| LV connector, Ampseal 23 (female, mates with BMU) — Tyco Electronics | 770680-1 | [eBay](https://www.ebay.com/sch/i.html?_nkw=770680-1) / [AliExpress](https://www.aliexpress.com/w/wholesale-770680-1.html) |
| HV connector HVP800, 180° — Tyco Electronics | 1-2177053-1 | [eBay](https://www.ebay.com/sch/i.html?_nkw=1-2177053-1) / [AliExpress](https://www.aliexpress.com/w/wholesale-1-2177053-1.html) |
| HV connector HVP800, 90° — Tyco Electronics | 1-2141154-1 | [eBay](https://www.ebay.com/sch/i.html?_nkw=1-2141154-1) / [AliExpress](https://www.aliexpress.com/w/wholesale-1-2141154-1.html) |
| EloSeal contacts, 0.5 / 0.75 mm² — Tyco | 5-1393462-5 | [eBay](https://www.ebay.com/sch/i.html?_nkw=5-1393462-5) |
| EloPower contacts, 1.5 / 2.5 mm² — Tyco | 5-1393462-9 | [eBay](https://www.ebay.com/sch/i.html?_nkw=5-1393462-9) |
| Superseal / Ampseal crimp tool 16/18-20 — Tyco | 354940-1 | [eBay](https://www.ebay.com/sch/i.html?_nkw=354940-1) |

## Wiring, Low voltage connector

The BMU uses a 23-position Ampseal connector. Only the pins below are used for a single-tray installation — the manual is explicit that no other pin should be connected.

| PIN | SIGNAL             | PIN | SIGNAL            |
| --- | ------------------ | --- | ----------------- |
| 1   | PublicCAN_Low_In   | 13  | KL30              |
| 2   | PublicCAN_High_In  | 14  | KL15_Wake         |
| 3   | BMU-ID_3           | 15  | KL15_Wake         |
| 4   | KL30_Safe          | 16  | PublicCAN_GND_In  |
| 5   | KL30_Safe          | 17  | PublicCAN_GND_In  |
| 6   | PublicCAN_Low_Out  | 18  | BMU-ID_2          |
| 7   | PublicCAN_High_Out | 19  | KL31_GND          |
| 8   | AkaCAN_Low         | 20  | KL31_GND          |
| 9   | BMU-ID_0           | 21  | PublicCAN_GND_Out |
| 10  | BMU-ID_1           | 22  | PublicCAN_GND_Out |
| 11  | BMU-ID_4           | 23  | AkaCAN_High       |
| 12  | KL30               |     |                   |

Pins 12/13 (KL30), 14/15 (KL15_Wake), 4/5 (KL30_Safe) and 19/20 (KL31_GND) are redundant pairs — in a multi-tray harness they are used for daisy chaining. For a single tray, one of each pair is enough.

`AkaCAN` is the battery's internal private bus. Leave pins 8 and 23 unconnected.

The BMU-ID pins set the BMU's CAN address through enumerator bridges in the harness. For a single tray you want **Tray 01**, which needs two bridges: **AD2 – AD3** and **AD0 – AD1**. This gives the BMU address `0xF3`, which is what the driver expects.

| Parameter                | Value                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| LV supply voltage        | 24 V nominal (see note above — 12 V is mentioned elsewhere in the manual, but no range is published)                            |
| Consumption — operation  | 18.9 W (≈0.8 A at 24 V)                                                                                                         |
| Consumption — standby    | 8 W (≈0.33 A at 24 V)                                                                                                           |
| Consumption — sleep      | 4.6 mW                                                                                                                          |
| Consumption — peak start | Not specified in the manual                                                                                                     |
| CAN type                 | 250 kbit/s, 29-bit extended (SAE J1939). 120 Ω termination must be in the harness — the BMU does not terminate                  |
| Contactor Control        | Not used. The battery closes its own contactors over CAN; the BE contactor pins drive KL30 / KL30_Safe / Wake                   |

## Wiring, High voltage connector

The HV connector is an HVP800. HV+ is on pin 2 and HV− on pin 1. HV wires must be shielded.

| PIN    | CONNECTION                               |
| ------ | ---------------------------------------- |
| HV 1   | High voltage negative pole               |
| HV 2   | High voltage positive pole               |
| HVIL 1 | HV interlock sink (low voltage signal)   |
| HVIL 2 | HV interlock source (low voltage signal) |

| Parameter            | Value                                 |
| -------------------- | ------------------------------------- |
| Interlock Required   | Yes                                   |
| Number of Interlocks | 1 (HVIL pair inside the HV connector) |

Earthing: the tray has M8 earthing bolts, tightened to 20 Nm, thread depth 11 mm. Bolt material minimum A2-70. Bond the housing before energising anything.

## Troubleshooting tips

**Battery never appears on CAN, or the driver sees nothing at all.**
Check the BMU-ID enumerator bridges first. Without the Tray 01 bridges (AD2 – AD3 and AD0 – AD1) the BMU claims address `0x00` instead of `0xF3`, and every message ID shifts with it. There is no `0x00` tray identity anywhere in the CAN matrix, so an unbridged BMU can also raise a generic configuration error.

**Battery reports Error and will not leave it, even after a power cycle.**
The Akasol Error state latches. Warnings and alarms can clear themselves; Error cannot. Per the manual you must deactivate Battery_Wake, fix the underlying cause, and redo the full start-up sequence. Simply rebooting the emulator is not enough — the battery itself has to be taken down.

**Battery stays in Init and never reaches Standby.**
KL30_Safe must be stable and bounce-free before `req_batuse=1` is sent. If it is applied at the same time as KL30, or if it is noisy, the battery will sit in Init. The driver's timed state machine handles this, but only if the signals actually reach the BMU — measure at the connector rather than at the GPIO.

**Contactors never close.**
Check the HVIL loop. If the external HV cables are not fitted, the interlock is open and the battery will refuse to close its contactors regardless of what the CAN handshake says.

**A persistent SCUConfig error bit with everything else healthy.**
Worth checking the grounding of the 24 V supply before anything else. On one installation the 0 V rail was left floating and the BMU raised SCUConfig continuously; bonding 0 V to PE cleared it. A multimeter showed only 142 mV between 0 V and PE beforehand, so the disturbance was high-frequency common-mode noise that a DMM cannot see — a clean reading does not rule this out.

**Reading the fault bits.**
The "More Battery Info" page shows BMM01 state, both contactor bits, the alive-counter handshake, and all 64 error/alarm/warning bits by name, taken from Akasol's own `PublicCAN.sym`. `BMM01_Error_info` additionally reports an internal `Errorvalue` / `Errornumber` / `ErrDetectDevice` triplet — these are undocumented Akasol-internal codes and generally will not map to anything you can act on directly.

### Notes for SolaX inverters

The pack works with the "SolaX Triple Power LFP over CAN" protocol. SolaX battery types describe LFP packs of 16 cells per module, so pick the type whose voltage window is closest to the Akasol's:

- Battery type **89 (HS25)**, **13 modules** → 665.6 V nominal, 759.2 V max, 50 Ah per string. That is within about 1.6 % of the Akasol's 655 V and 0.4 % of its 756 V ceiling.
- Contactor workaround: **No Workaround**.

Because SolaX assumes 208 LFP cells with a 3650 mV ceiling and the Akasol is 180 NMC cells to 4200 mV, the SolaX driver rescales the reported cell voltages to the assumed cell count. Without that, a real pack at high SOC would look like an overvoltage to the inverter.
