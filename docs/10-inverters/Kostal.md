> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Notes on RS485
Kostal uses a proprietary RS485 protocol. The protocol uses the RS485 pins on the Battery-Emulator hardware and has been mostly decoded. The integration is mostly stable.

## Compatible Kostal inverters 
A checkmark (✅) indicates that an user has reported back successfully using the Battery-Emulator.

* PLENTICORE plus 3.0 / 4.2 / 5.5 / 7.0 / 8.5 / 10 ✅
* PLENTICORE plus G2 4.2 / 5.5 / 7.0 / 8.5 / 10
* PLENTICORE G3 S / M / L ✅
* PLENTICORE BI 5.5-13/ 5.5-26 ✅
* PLENTICORE BI 10.0-26 ✅
* PIKO MP Plus 1.5-1/2.0-1/ 2.5-1
* PIKO MP Plus 3.0-1, 3.0-2, 3.5-1, 3.5-2, 4.6-2, 5.0-2
* PIKO 6.0 BA / 8.0 BA / 10 BA

Note that for some models the battery feature is optional, and needs to be activated via an activation code (or "PLENTICOIN") that needs to be purchased first.  This code must be entered either via the onscreen menu or the web interface. On older firmware versions this was possible with the regular user login, on newer firmware versions this requires a service code. The same applies for the battery configuration screen. More details: https://www.kostal-solar-electric.com/Guideline_PLENTICORE-BYD/

![image](../images/kostal-01.png)

## Which protocol to use
For this inverter type, use the option called "BYD battery via Kostal RS485" under the "Inverter Protocol" setting. Also set the "Inverter Interface" to the "RS485" option.

![image](../images/kostal-02.png){ width="488" height="66" }

## Communication wiring

The Kostal inverter works via RS485. Connect pins A, B and GND from the Kostal connector X601 to the corresponding points of the lilygo RS485 connector. Setup the Kostal inverter to use the BYD battery option.

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Traces for reverse engineering


|  Inverter |  Battery | Source | Traces | 
| :--------: | :---------: | :---------: | :---------: |
| Kostal Plenticore Plus 5.5 |  BYD B-Box HV 6.4 | [huntworker from secondlifestorage forum](https://secondlifestorage.com/index.php?threads/communication-between-byd-battery-and-kostal-plenticore-inverter.10513/) | [startup](https://gist.githubusercontent.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/248240da6c212601708c3305cdd924a2de513b5f/hunterwork-startup-log-02.txt) |
| Kostal Plenticore Plus G2 10 | Dyness Tower T17, Firmware version 119 | SauliusS from Discord | [01_start_inverter](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/38feb21eba7086fd83f8dc4b32a4f1bcebd081eb/SauliusS_dyness_tower_t17_01-start-inverter.txt), [02_start_battery](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/38feb21eba7086fd83f8dc4b32a4f1bcebd081eb/SauliusS_dyness_tower_t17_02-start-battery.txt), [03_discharging](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/38feb21eba7086fd83f8dc4b32a4f1bcebd081eb/SauliusS_dyness_tower_t17_03-discharging_first-slow-than-fast.txt), [04_charging](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/38feb21eba7086fd83f8dc4b32a4f1bcebd081eb/SauliusS_dyness_tower_t17_04-charging_first-slow-than-fast.txt), [05_discharged to minimum allowed SoC 20%, with audible click](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/4a94411feb20515eae8c7dee91ccb9cf83cb5ece/SauliusS_dyness_tower_t17_05-discharged-to-minimum-allowed-SoC-20percent-with-audible-relay-click.txt), [08_battery-charging-then-DC-switch-turned-OFF](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/248240da6c212601708c3305cdd924a2de513b5f/SauliusS_dyness_tower_t17_08-battery-was-charging-turn-OFF-DC-switch-then-stopped-charging-waited-for-3min-THEN-turn-ON-DC-switch-THEN-takes-around-a-minute-to-charge.txt), [10_charging-reaches-SoC-98](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/248240da6c212601708c3305cdd924a2de513b5f/SauliusS_dyness_tower_t17_10-charging-until-SoC-98.txt), [11_charging-reaches-SoC-99](https://gist.github.com/lewurm/ab9de61bbcbd6f585b2894d0404a03f2/raw/248240da6c212601708c3305cdd924a2de513b5f/SauliusS_dyness_tower_t17_11-charging-until-SoC-99.txt) |

## Setup to capture a trace

***

**WANTED**: Setups involving BYD HVM or HVS. Even better if there are multiple units in parallel via the HV Combiner Box.


***


Use this tree of the battery emulator on a LilyGo: https://github.com/lewurm/Battery-Emulator/tree/rs485-sniffing
Compile with Arduino ide ESP32 firmware 3.1.3.
It will just print whatever bytes are seen on the RS485 line to the USB serial.

In terms of wiring, connect A/B/GND accordingly between inverter and LilyGo.  Power the LilyGo via USB-C (connect to a Laptop) and observe the serial monitor.

![Screenshot 2025-02-21 at 23 33 04](../images/kostal-03.png){ width="1220" }
![Screenshot 2025-02-21 at 23 33 23](../images/kostal-04.png){ width="1223" }
![Screenshot 2025-02-21 at 23 33 16](../images/kostal-05.png){ width="1216" }

