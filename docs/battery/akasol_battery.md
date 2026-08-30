---
title: "Akasol Akasystem 15 OEM 50 PRC"
---

## Compatible batteries

AKASOL AKASYSTEM 15 OEM 50 PRC — a single-tray, 655 V nominal NMC pack (180 cells, 50 Ah, ~33 kWh) with one BMM01 controller.

Note: Only the single-tray BMM01 variant is implemented. Multi-tray systems use a different addressing scheme and are not covered.

### Physical Dimensions

| Parameter | Value |
|----------|-------|
| Pack Size (L × W × H) | <!-- e.g. 2400 × 1500 × 150 mm --> |
| Weight | <!-- e.g. 540 kg --> |

### Special considerations

- The CAN bus is 250kbps on this battery, so it needs to be on its own separate CAN network
- Startup sequence: The battery requires a specific startup signal via KL30 / KL30_Safe / KL15. This has been implemented via the Pre/Neg/Pos contactor pins used in BE

## Software configuration
For this battery type, use the option called "AKASOL" under the "Battery Protocol" section.

## Part numbers 
Part numbers for connectors/cables, along with purchase links to ebay/aliexpress.

| Component | Part Number | Purchase Link |
|-----------|-------------|---------------|
| <!-- e.g. HV Connector --> | <!-- e.g. TE 123456 --> | [eBay](#) / [AliExpress](#) |

## Wiring, Low voltage connector

Post picture of LV connector
Add diagram of LV connections needed.

| Parameter | Value |
|----------|-------|
| 12V Consumption — Peak Start | <!-- e.g. 15 A --> |
| 12V Consumption — Continuous | <!-- e.g. 5 A --> |
| CAN type | <!-- CAN or CAN-FD or RS485 --> |
| Contactor Control | <!-- CAN-controlled or Externally controlled --> |

## Wiring, High voltage connector

<!-- Add a photo of the HV connector and a wiring diagram below -->

| Parameter | Value |
|----------|-------|
| Interlock Required | <!-- Yes / No --> |
| Number of Interlocks | <!-- e.g. 2 --> |

## Troubleshooting tips

<!-- Document common issues and their solutions -->

## Example picture from completed install

<!-- Add a photo of a finished installation for reference -->