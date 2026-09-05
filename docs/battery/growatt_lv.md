---
title: "Growatt LV (GBLI-series)"
---

## Compatible Growatt LV batteries

- [Growatt GBLI6532](https://solsol.eu/file/view/1805/growatt_instman_gbli-6532-quick-guide_en.pdf) ✅ — confirmed live for weeks against a Solis S6-EH1P8K-L-PLUS inverter
- If you try another GBLI-series pack, please add it to this list!

## Software configuration

For this battery type, use the option called "Growatt LV (GBLI-series) battery via CAN, 500kbit/s" under the "Battery Protocol" setting.

![Screenshot_20260905_232649](../images/growatt-lv-02.png)

## Wiring notes

The GBLI6532 has three RJ45 sockets. Use **PCS** (the inverter-facing one), not Link-In/Link-Out — those carry the inter-battery bus on different pins and will silently not work.

| Pin | Signal |
|---|---|
| 4 | CAN_H |
| 5 | CAN_L |
| 7 | PCS-WAKE− |
| 8 | PCS-WAKE+ |

WAKE (pins 7/8) is documented for waking the pack from a non-Growatt inverter, but it is not needed — a CAN-only connection (just pins 4/5) is enough to both enable and revive the pack, confirmed by wiring a cable with WAKE deliberately left disconnected.

A standalone battery still needs the correct master-select plug fitted in Link-In/Link-Out, or it may never enumerate on the bus.

## References used

- [Growatt BMS CAN-Bus protocol, low voltage V1.04](https://www.amosplanet.org/wp-content/uploads/2022/04/Growatt-BMS-CAN-Bus-protocol-low-voltage-V1.04-1.pdf)
- [schmellic/growatt2solis](https://github.com/schmellic/growatt2solis) — the standalone ESP32 gateway this driver was ported from, including its full CAN capture and reverse-engineering notes
