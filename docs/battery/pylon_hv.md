---
title: "Pylon HV"
---

Any high voltage battery compatible with the Pylontech defacto standard can now be used with the Battery-Emulator. Do note that the support is experimental, and should be considered as a starting point when refining support for your battery. There has been many revisions to the Pylon CAN standard over the years, so some batteries might behave differently than others, even though they both support the Pylon protocol.

## Who is the Pylon-Battery support for?
* Incase you bought an expensive home battery, and want it to show up as a BYD/SMA/SOLAX/SOFAR/Dyness compatible battery for use with another inverter, this is for you!
* Incase you built your own HV battery, and want to integrate it, feel free to use the Pylon protocol!

## Example of Pylon compatible batteries

SWA HV Batteries - With enough voltage range to be used as HV

- SWA-204.8V50  180V-228V ✅
- SWA-307.2V503 270V-340V ✅
- SWA-409.6V50 ✅
- If you try one that works, please add it to this list!

Dyness Tower

- Dyness Tower T7  ✅
- Dyness Tower T10 ✅
- Dyness Tower T14 ✅

Configuration:

![image](../images/pylon-hv-01.png){ width="545" height="86" }

Currently the cell voltages might be off and the contactor did not work.

PylonTech Force H3

## Software configuration
For this battery type, use the option called "Pylon compatible battery" under the "Battery Protocol" setting.

![image](../images/pylon-hv-02.png){ width="670" height="271" }

Finally, remember to configure the voltage limits to match the Pylon battery you are using (e.g. 180-228V)

## References used
- [eevblog](https://www.eevblog.com/forum/programming/pylontech-sc0500-protocol-hacking/)
- [gcsolar](https://onlineshop.gcsolar.co.za/wp-content/uploads/2021/07/CAN-Bus-Protocol-Sermatec-high-voltage-V1.1810kW.pdf)