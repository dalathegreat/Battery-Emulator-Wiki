> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Compatible Solax inverters
* Solax X3 (all revisions)
* Solax X3 Ultra (all revisions)
* Solax X1 (all revisions)
* Solax X1 VAST (all revisions)

# ⚠️ Word of caution, CAN overvoltage ⚠️
Solax inverters can have high voltage potential on the CAN chip. They can be 110V when measuring between CAN and PE. It can burn up your Battery-Emulator CAN chips if there is a path to protective earth. This becomes a problem if the board you are using has GND on the same plane as PE. Then the 110V diff might leak over and damage the chips. A way to avoid this is to use a PSU to power the Battery-Emulator board that is not connected to PE. For instance a 2-prong phone charger would effectively be isolated from PE.

![image](../images/foxess-h1-h3-ac1-kh-01.png)

An even better way to tackle this is with the use of a CAN isolator between the inverter and the rest of the system. Examples found in the [lightning strike wiki](https://github.com/dalathegreat/Battery-Emulator/wiki/Lightning-strike#suggested-hardware)

![image](../images/foxess-h1-h3-ac1-kh-02.png)

Failure to implement any of the above solutions will lead to the VP231 CAN transceiver chip burning up! 🔥

Alternatively, using hardware with built-in galvanic isolation (such as the [LilyGo T-2CAN](https://github.com/dalathegreat/Battery-Emulator/wiki/Hardware%3A-LilyGo-T‐2CAN/)) should avoid this problem without imposing extra power supply requirements.

# Word of caution, isolated CAN
⚠️ This inverter does not handle a CAN connected EV battery on the same channel.
If the inverter which likes to see only extended CAN frames sees standard automotive CAN frames, the inverter will enter a fault state.

This can be solved in three ways:

* You can [add an isolated MCP2515 CAN channel](https://github.com/dalathegreat/Battery-Emulator/wiki/CAN-add%E2%80%90on-(MCP2515))
* You can [add an isolated MCP2518 CANFD channel, and run it in classic CAN mode](https://github.com/dalathegreat/Battery-Emulator/wiki/CAN%E2%80%90FD-add%E2%80%90on-(MCP2518FD))
* You can use the [Stark CMR](https://github.com/dalathegreat/Battery-Emulator/wiki/Hardware:-Stark-CMR) hardware
* You can use the [LilyGo T-2CAN](https://github.com/dalathegreat/Battery-Emulator/wiki/Hardware%3A-LilyGo-T‐2CAN/) hardware
* You can use a [CAN filter](https://github.com/dalathegreat/Battery-Emulator/wiki/CAN-filter-hardware) between inverter and the rest of the system 

ℹ️ The inverter contains a 120 Ohm terminating resistor on CAN-H/L pins

ℹ️ Grounding is extremely important for Solax inverters. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Which protocol to use
For this inverter type, use the option called "SolaX Triple Power LFP over CAN bus" under the "Inverter Protocol" setting

<img width="569" height="160" alt="image" src="../images/solax-04.png" />

> [!WARNING]
> Never use lead-acid battery mode to force a battery to operate. This means there is no communication between the EV battery and inverter, and battery has no way to stop the charge. Users have permanently degraded batteries by operating in this mode!

> [!IMPORTANT]  
> If you see a **BattVoltFault** fault code on the inverter, you might need to edit the CAN data content. This can happen if you use a 60S battery instead of 96S battery. Follow the steps below

1. Start with checking that your battery contactors are closing, and that high voltage is present on the inverter input pins. 
2. If the inverter has voltage, but is still throwing the BattVoltFault error, "Reported module count" and the "Reported battery type" option

<img width="556" height="69" alt="image" src="../images/solax-05.png" />

## Battery type information (pre-2026)

Change the settings to suit your voltage range

|  139S [400-584V] |  108S [325-455V] |  98S [295-412V] |  96S (default) [290-404V] | 75S [225-315V] | 56S [170-235V] |
| :--------: | :--------: | :--------: | :--------: | :---------: | :---------: |
| Reported module count 10 | Reported module count 8 | Reported module count 7 | Reported module count 0 |  Reported module count 4 | Reported module count 6 |
| Reported battery type 131 | Reported battery type 131 | Reported battery type 131 | Reported battery type 80 | Reported battery type 84 | Reported battery type 91 |

Note, if you are using a custom DIY battery, make sure to define the max voltages accordingly!

Feel free to experiment, and post what settings worked for your voltage range. The default values are OK for a 300-400V 96S battery.

Also note, if you are using Custom batteries, remember to configure the max/min design voltage marked in red here. Solax will listen to these limits on Pylon/RJXZS/Orion/DIY packs

<img width="551" height="289" alt="image" src="../images/solax-06.png" />

## Battery type information (2026)

The latest (ARM 1.57) firmware no longer allows the battery type 80 recommendation given above (and will result in the IE102 error). Instead, choose a different battery type from the list below.

A good choice is type 131, which is the T-BAT-SYS-HV-R2.5, a 16S LFP pack:

Battery type | Num modules | Min voltage | Nom voltage | Max voltage
-- | -- | -- | -- | --
131 | 2 | 89.6 | 102.4 | 116.8
131 | 3 | 134.4 | 153.6 | 175.2
131 | 4 | 179.2 | 204.8 | 233.6
131 | 5 | 224 | 256 | 292
131 | 6 | 268.8 | 307.2 | 350.4
131 | 7 | 313.6 | 358.4 | 408.8
131 | 8 | 358.4 | 409.6 | 467.2
131 | 9 | 403.2 | 460.8 | 525.6
131 | 10 | 448 | 512 | 584
131 | 11 | 492.8 | 563.2 | 642.4
131 | 12 | 537.6 | 614.4 | 700.8
131 | 13 | 582.4 | 665.6 | 759.2

(note that the enforced min/max limits will be wider than the range shown here - choose a setting where the maximum is high enough for your battery).

List of battery names and type codes (decimal):
```
BAK: 81
T58 V1: 82
Sinowatt: 83
T30: 84
T50: 85
TR25: 86
TR36: 87
THS50E: 88
HS25: 89
HS36: 90
T58 V2: 91
LR25/36: 92
LD53: 93
LD150: 94
LD51: 95
TP012: 96
TP013: 97
TP014: 98
LD117: 99
T58V3: 100
LD160: 101
LD143: 102
X-BP 2700: 103
TP020(LD321): 104
TP021(LD51E): 105
TP022(LD160E): 106
BMS-Parallel BOX-II: 129
T50_P: 130
TR25_P: 131
BMS-Parallel BOX-II V2: 132
TCBox-70: 140
BMS-Parallel BOX-II G2: 141
HS51: 145
HS50A: 146
TPCU001_R140: 161
TPCU002_R460: 162
TR-HR140: 163
TPCU004_R522_DC: 164
TPCU005_HR1044_FOREGIN: 165
TPCU006_HR1044_CHINA: 166
TPCU007_HR76: 167
TPCU008_1044KWH: 168
TPCU009_HR522_CHINA: 169
TPCU010(B57): 170
TPCU011(HR522): 171
```

## Notes on CAN controlled contactors

> [!IMPORTANT]  
> Solax is one of the few protocols that demands contactors to open from time to time. This works great with GPIO controlled contactors, but on battery packs that are only controllable via CAN (Like Tesla), this does not play nice. Tesla batteries like to treat contactor opening requests as a really bad thing, and require 12V removal to get going again.

To get around this issue for instance on Tesla batteries, enable the "Inverter should ignore contactors" checkbox

<img width="430" height="30" alt="image" src="../images/solax-07.png" />

This will make Battery Emulator ignore requests from the inverter to open contactors, and always report to the inverter that the contactors are closed (regardless of their actual state), preventing the inverter from waiting for the contactors to open.

> [!WARNING]
> This contactor-opening-suppression seems to cause issues with double-input inverters, since the inverter insists on waiting for both batteries to open their contactors before starting. (Note: even if only one battery input is occupied!) There is a pending change to allow stubborn integrations to suspend their initial closing (but then not to reopen once closed), but this needs further testing.

Additional: When experiencing a "waiting" status when all other settings are good, unchecking this box can result in normal operation. Be aware of this, as Solax is not too helpful in telling why it is in actual "waiting" status, this can be an easy test.

## Reverse engineering information

Some interesting findings based on dynamically changing some of the CAN values for testing:

- The Inverter does obey the Contactor flag from the BMS (1875 byte 2) and if this is not 1 it will sit in waiting and not go into "Checking" phase and if inverter already active it will go back to "waiting" if you send 0 instead of 1 and internal contactors click (presumably open). So this could be a good initial alarm control to have less wear on the battery contactors.

- The battery kind can be changed during normal operation and this will cause a BattVoltFault - presumably due to different voltage ranges.

- Seems each battery kind has a different hardcoded voltage range as with 7 as number of packs only works with 0x83 (TP201)

- Adjusting the number of packs during normal operation (from 7>6 for example) causes a BattVoltFault so seems this is being monitored constantly and not just on BMS initialisation (checking phase)

For a pack with actual voltage of 337v (21% soc) and using different Battery Kinds (1877, Byte 4)

Previously known Kinds:
- 0x50 (Blank) 6 works works - 7 does not ("About" menu has no info)
- 0x51 (BAK) 6 works
- 0x52 (REPT) 6 packs works - 5 + 7 do not
- 0x53 (SINOWATT) 6 works
- 0x54 (GOT) 3+4 works, 2, 5>10 do not work
- 0x55 (TP001) 6 works, 2>5, 7>8 do not
- 0x81 (TP200) 6 works 4/5 and 7>9 do not
- 0x82 (TP201) 6 works 4/5 and 7-9 do not
- 0x83 (TP202), 7 packs works fine and even changing it to 8 works despite being out of range (should be min 348.5v) but going lower to 6 causes battvoltfault. So it seems to prefer higher voltages than lower ones.
- Type 129(dec) = REP TP58
- Yype 97(dec) is TP013

New Kinds Tested:
- 0x00 NA - 6 works, 0/5/7 does not
- 0x5B (TP007) 6 works 4>5 and 7>9 do not (4 was the no of packs I recorded in logs from real setup with 2 x triple batteries which reported voltage min/max of 180>262v and actual voltage of 238v at 97% SoC)

Other battery Kind ranges I checked just to see if they showed in the about menu - didnt try no of packs (sorry numbers below in Dec not HEX):
0-10 N/A
85-93: TP001>TP009
94>99: TP010 > TP015
100>128 - NA
129 - REP-T58-P1
130>139: TP201>TP210
140>160 NA

- BTW, according to SOLAX documentation the RP-T58-P1 modules (these are the older, first generation modules) can be UP TO 4pcs! That's why the setting Battery type 129 can be only up to 4 MODULE COUNT.

- It doesn't seem to matter too much what voltage min/max you send on frame 1872 - if the real voltage or even voltage sent on 1873 is outside of these ranges it does not impact operation worryingly. Clearly the limits on battery kind are overriding this.

- With battery at actual voltage at 342v inverter senses this at 336v (6v lower I dont know why). Min/Max set to 300v/399v:
- if I send <150v it goes back to waiting (not battvoltfault)
- if I send 151v/245v works fine
- If you send no voltage on frame 1872 then it just stays in "Waiting" mode

- Like others said before you dont seem to need the announce 0100a001 frame or even respond to the 1871 frame the inverter sends every 1000ms. I am sending all frames every 900ms at a non-synced interval and it plays fine.


all credits to the guys from this thread: 
https://secondlifestorage.com/index.php?threads/help-with-older-solax-x1-g4-firmware-ie07-batvoltfault.12493/


## Connection diagram
BMS port pin 4 is CAN-H pin 5 CAN-L (for Solax X3 G4). Connect only these two wires to the Battery-Emulator

![image](../images/solax-03.png)

## Troubleshooting tips 

|  Problem |  Possible fix |
| :--------: | :---------: |
| Inverter stuck in "Waiting..." | Check that high voltage is present on inverter terminals, and that polarity is right way. Also check that the precharge/positive-contactor control has not been accidentally swapped around. A telltale of this accidental swap is that the voltage reading on the inverter side will be jump +-50VDC all the time. |
| Contactors close, then after a few seconds they open. With the battery on its own, without inverter connected, contactors stay on. | Solax controls contactor opening, this is not working good on CAN controlled packs. See the [Notes on CAN controlled contactors](https://github.com/dalathegreat/Battery-Emulator/wiki/Inverter:-Solax#notes-on-can-controlled-contactors) |
| Inverter screen showing "Bat Mismatch IE102" error | Configure "Reported battery type (in decimal):" to 81 in the webserver settings, OR update Battery-Emulator to latest version |


## Notes about Ultra
When using two batteries, the Ultra inverter only connects both batteries if the second one closes its contactor exactly at the time the inverter requests it to close. if both contactors are closed from the beginning then it will not turn on. I tried a bit the last days and the best option at least for tesla batteries is to start with inverter_allows_contactor_closing = false and after the inverter requests it set inverter_allows_contactor_closing = true. After that happened I will never reset it to false since tesla batteries sometimes won't be able to close the contactor any more.

## Notes on Offgrid Solax
Using any inverter in offgrid mode can result in overdischarging of the battery. Make sure you have a way for the Battery to open the contactors incase the battery gets overdischarged. Either use GPIO controller contactors, or make sure that the Battery-Emulator is able to open the contactors on demand. A good test is to use the "Open Contactors" button in the Battery-Emulator Webserver, and observe if the system is able to shut itself down. If the system does not shut down, it is not safe for offgrid use.
