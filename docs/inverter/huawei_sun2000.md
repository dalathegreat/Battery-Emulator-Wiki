---
title: "Huawei SUN2000"
---

LUNA2000 support is not planned at the moment due to requiring DC/DC converter.

## ⚠️ DC/DC link

!!! warning "WARNING"
    Batterysystem (LUNA2000) is a Battery including DC/DC. So this system is more like a current source. Voltage is given by the DC-Link of the inverter. This DC-Link is depending on the PV-Voltage. If PV-Voltage is less than 600V, the DC Link is at around 600V. For PV-Systems with a String voltage of >600V the DC-Link Voltage is higher. **This means there is no way to directly connect a battery to the SUN2000 Inverter.** There is always a need of an additional DC/DC stage.

The SUN2000 inverters are compatible with both 400V and 800V systems. However, when using a 400V system, your PV strings cannot exceed 495 V. This is a problem for many, since the Huawei SUN2000 inverters often have large arrays with 700-900 V. The second problem is that this low voltage mode requires emulating a LG RESU battery, which we don't have logs of yet.

## Installation manual

See this manual for more info on 400V LG Resu: [huawei](https://support.huawei.com/enterprise/en/doc/EDOC1100011910)