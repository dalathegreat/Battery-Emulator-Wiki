---
title: "Stellantis Pro One"
---

**110 kWh · 90S · MCA Battery Platform**

## 🚐 Compatible vehicles

The following vehicle batteries are compatible with the Stellantis Pro One / MCA 110 kWh battery platform:

- Fiat E-Ducato 110 kWh
- Ram ProMaster 110 kWh
- Toyota Proace Max 110 kWh
- Opel Movano 110 kWh
- Citroën Jumper 110 kWh
- Peugeot Boxer 110 kWh

## 🔵 Battery specifications

| Specification | Value |
|:--|:--|
| Battery capacity | 110 kWh |
| Cell configuration | 90S |
| Minimum voltage | Approximately 270 V |
| Maximum voltage | Approximately 380 V |

## ⚠️ Inverter power limitations

!!! warning "WARNING"
    This battery has a relatively low voltage. The inverter's maximum output power may therefore be limited by its maximum battery input current.

    For example, the Solis 20K has a maximum battery input current of 50 A.

| Battery voltage | Maximum current | Theoretical DC power |
|:--:|:--:|--:|
| 380 V (high state of charge) | 50 A | **19 kW** |
| 270 V (low state of charge) | 50 A | **13.5 kW** |

These figures represent the theoretical maximum DC power available at the specified battery voltages. Actual AC output power will be lower due to conversion losses and may be further limited by the inverter.

## ⚡ High-voltage (HV) connector

### Capacitor requirements

The battery requires capacitance across the HV lines before the contactors will engage.

The following capacitor configurations have been confirmed to work:

- **2 × 470 µF** capacitors connected in parallel (940 µF total)
- **1 × 1000 µF** capacitor

!!! warning "WARNING"
    Ensure that the capacitors have a suitable voltage rating for the battery's HV system. High-voltage components can retain dangerous energy even after the battery has been disconnected.

### 🔹 Standard HV connector — 175 A

This is the easiest connector to source and use. The other options are much harder to find.

!!! important "IMPORTANT"
    The HVIL (high-voltage interlock loop) must be properly connected.

![HV connector](../images/stellantis-pro-one-01.png)

**Purchase link:** [HV connector on AliExpress](https://nl.aliexpress.com/item/1005003639011124.html?spm=a2g0o.order_list.order_list_main.18.252f79d2fTtchH&gatewayAdapt=glo2nld)

### 🔹 Alternative HV connector — up to 600 A

This alternative connector can also be used if you can find one.

!!! important "IMPORTANT"
    The HVIL must be properly connected.

![Alternative HV connector](../images/stellantis-pro-one-02.png)

### 🚫 DC fast-charging connector

The HV connector on the right-hand side, intended for DC fast charging, **cannot be used with the Battery Emulator**.

![DC fast-charging connector](../images/stellantis-pro-one-03.png)

## 🔋 Low-voltage connector

![Low-voltage connector](../images/stellantis-pro-one-04.png)

**Purchase link:** [Low-voltage connector on AliExpress](https://nl.aliexpress.com/item/1005005787269820.html?spm=a2g0o.order_list.order_list_main.12.252f79d2fTtchH&gatewayAdapt=glo2nld)

### 📌 Wiring pinout

| Pin | Function |
|:--:|:--|
| 4 | GND |
| 12 | 12 V |
| 14 | 12 V |
| 15 | CAN H |
| 16 | CAN L |
| 22 | 12 V |
| 24 and 25 | Connect together to close the interlock circuit |

## 💻 Software configuration

To use this battery, select the following battery profile in the Battery Emulator software: **Stellantis Pro One 110kWh (E-Ducato/ProMaster/Proace)**.
