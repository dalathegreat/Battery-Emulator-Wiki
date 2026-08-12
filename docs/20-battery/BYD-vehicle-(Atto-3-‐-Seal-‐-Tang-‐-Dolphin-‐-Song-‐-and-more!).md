
> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

# Compatible BYD batteries
The code supports a variety of BYD vehicle batteries. Check the product code sticker, and verify that the battery has already been tested with the Battery-Emulator, indicated by the ✅-mark that contactor closing works and the pack has been confirmed working

To get contactor closing to function, start BYD battery first, and Battery-Emulator afterwards. If you start Battery-Emulator before the battery, it wont close contactors before you restart the emulator. Also make sure no FAULT events are active when trying to start, this will open contactors.

|  Product Type |  Byd Model  | Energy | Capacity | Nominal voltage | Status |
| :-----------: | :---------: | :----: | :------: | :-------------: | :----: |
| PV2 | ? | 40 kWh | 150Ah | 300.8V | ✅ 
| PE4 | Seal | 61.66kWh | 150Ah | 409.6V | ✅
| ??? | Atto 3 | 50kWh | ? | ? | ✅ 
| P48 | Atto 3 | 60.48kWh | 150Ah | 403.2V | ✅ 
| VD6 | Seal U DM-i | 18,32kWh | 54Ah | 339.2V | :x: (Type B LV connector)
| PA4 | Tang | 86.4kWh  | 135Ah | 640V | :x: (Type B LV connector)
| PE2 | Han | 85.4kWh  | 150Ah | 569.6V | :x: (Type B LV connector)
| PE5 | Seal   | 82.56kWh | 150Ah | 550.4V | ✅ 
| PE6 | Seal   | 82.56kWh | 150Ah | 550.4V | ✅ 
| PK3 | Dolphin | 49.92kWh | 150Ah | 332.8V | -
| P0B | Dolphin | 43.2kWh | 150Ah | 288V | -
| P07 | T3     | 50.37kWh | 115Ah | 438V | -
| P94 | Dolphin | 44.928kWh | 135Ah | 332.8V | ✅ 
| P99 | ? | 44.928kWh | 135Ah | 320.0V | -
| PC5B | Dolphin mini | 38.8kWh | 135Ah | 288V | :x: (Type B LV connector)
| ? | Song Plus | 82.56kWh | 150Ah | 550.4V | ✅ 
| PM6 | Song Plus | 87.04 kWh | 170Ah | 512.0V | 
| PM7 | Seal U | 71.80 kWh | 170Ah | 422.4V | ✅ 
| VM7 | Sealion 8 DM-p (AU) | 35.62 kWh | 78.4Ah | 454.4V | :x: (Type C LV connector)
| PW4 | Seal 7 | 91.392 kWh | 170Ah | 537.6V | ✅

Confirmed working BYD Seal 60kWh battery example sticker:

![image](../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-01.png)

> [!NOTE]  
> If you intend to run two BYD batteries in [parallel](../40-setup/20-software/Double-Battery.md), make sure they are both the same model!

### Example battery install, Atto 3 P48 battery

The extended range nominal 60.48 kWh BYD Atto 3 blade battery pack is 1.2m wide by 2.1m long and 120mm high, weighing 402kg. 
The battery chemistry is LFP (LiFePO4). The battery configuration is 126s1p, estimated capacity of fully charged pack is 126 cells at nominal 3.2V x 150Ah connected in series = 60.48 kWh. Fully charged the pack produces total voltage of 441V max (3.5V/cell) and at 10% SOC, about 403V (3.2V/cell), as measured and monitored by OBD2 CarScanner during charging.

![](../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-02.png)
 
Viewed from the front, left is the low voltage connector, central is two refrigerant lines and right is the HV connector, with +ve on RHS.
<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-05.png" />

The front connectors end of the battery also includes the contactor block. There is a well-hidden 800V/350A fuse near the positive contactor(coil:12VDC/contactor:250A) on the RHS of the block, along with a mini pre-charge contactor (coil:12VDC/contactor:10A) and a pre-charge resistor, which is underneath the HV connector. There is no Tesla-like pyro fuse that blows when airbags are deployed; the system just opens the contactors.

## Software configuration
For this battery type, use the option called "BYD Atto 3/Seal/Dolphin" under the "Battery Protocol" setting

<img width="599" height="115" alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-06.png" />

## Video example
Here is a great video made by "Flying Tools" showcasing how to connect the BYD Atto 3 battery

https://www.youtube.com/watch?v=YBYWBapnnyM

## Battery specifications

## LV Connector Type A
The connection diagram is derived from reverse engineering the pins. The following pinout is valid for, but not limited to, PE4, PE5, PE6 and P48 battery. It can be identified easily by seeing that there are 4 rows of pins, and three thicker pins on the side
 
<img width="489" height="205" alt="BYD_Atto_BK51_pinout" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-07.png"/>
<img width="489" height="257" alt="BYD_Atto_BK51_wiring" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-08.png"/>

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-09.png" />
<html><body>

## LV Connector Type B
This connector appears on newer battery types, such as the PA4. The software does NOT have full support for TypeB batteries yet. :x:
Pinout varies between different batteries despite the plug & socket being the same.

*Development ongoing, many details can be found in the Discord*

| Battery | Plug Image | Wiring Diagram | Pinout |
|---|---|---|---|
| **PA4** | <img width="280" alt="PA4 plug" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-10.png" /> | — | Not yet documented |
| **PC5B** (upside down compared to PA4) | <img width="280" alt="PC5B plug" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-11.png" /> | <img width="280" alt="PC5B wiring diagram" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-12.png" /> | [See below](#pc5b-pinout-from-manual) |
| **VD6** | <img width="280" alt="VD6 plug" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-13.png" /> | <img width="280" alt="VD6 wiring diagram" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-14.png" /> | [See below](#vd6-pinout-from-manual) |
| **VM7** | <img width="280" alt="VM7 plug" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-15.png" /> | — | Mostly unknown at the moment, derived from in car measurements and comparison to VD6 |

### Pinout comparison

| Pin | PC5B | VD6 | VM7 |
|---|---|---|---|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |
| 4 | Constant 12V power | Constant power supply | Constant 12V |
| 5 | Ignition 12V power | Power network CAN-H | Power network CAN-H |
| 6 | — | Power network CAN-L | Power network CAN-L |
| 7 | — | — | GND (CAN twisted pair shield) |
| 8 | Charging Subnet CAN-L | IG3 | ? (maybe IG, based on VD6) |
| 9 | — | Vehicle battery GND | GND |
| 10 | Energy Subnet CAN-L | Vehicle battery GND | GND |
| 11 | — | Charging connection signal | ? |
| 12 | DC charging pos/neg power supply (12V in) | — | ? |
| 13 | HV interlock signal 1 | Collision signal | ? |
| 14 | DC+ temp sensor signal | — | ? |
| 15 | Charging Subnet CAN-H | — | — |
| 16 | GND | — | — |
| 17 | Energy Subnet CAN-H | Charging CAN-H | Charging CAN-H |
| 18 | HV interlock signal 2 | Charging CAN-L | Charging CAN-L |
| 19 | — | Temperature test 1+ | ? |
| 20 | DC- temp sensor signal | Temperature test 2+ | ? |
| 21 | DC charging port temp sensor GND | Fast-charging pos/neg contactor GND | — |
| 22 | Collision signal | Fast-charging positive contactor 1 | — |
| 23 | GND | Fast-charging negative contactor 1 | — |
| 24 | DC charging pos contactor control signal | — | — |
| 25 | Charging connection confirmation CC | CC contactor burn-detection point | — |
| 26 | DC charging aux power supply wakeup A+ | DC charging port voltage status signal CC+ | — |
| 27 | — | Temperature detection GND | ? |
| 28 | — | — | — |
| 29 | Ignition 12V power | — | — |
| 30 | On board charging connection signal | HV interlock input signal 1 | ? (Interlock +?) |
| 31 | DC charging negative contactor control signal | HV interlock output signal 1 | ? (Interlock -?) |
| 32 | DC charging sensor signal | — | — |
| 33 | Charging connection confirmation CC2 | CC contactor burn-detection GND | — |

## HV Connectors
High voltage connectors vary a bit between the different BYD variants. Due to this, it is best to try and source the high voltage cable from the same type of vehicle that the battery came from.

## Contactor Block Modification
In the event of the battery being locked, the pre-charge and two contactors can be wired to manually switch on, or preferably to automatically activate via 3 SSRs with the GPIO pins on the Lilygo board (see [Contactor control via GPIO pins](../40-setup/20-software/Contactor-Control-via-GPIO-pins.md)).
When accessing the internals of the battery, wear the appropriate safety gloves and follow safe procedures to avoid shorting across HV terminals. To access the contactor block, first remove the top cover, which fortunately is not sealed down; ~ 76 screws and 2 central top bolts require removal. In the pictorial description that follows, details of the full removal of the contactor block is shown, to identify the various parts. With connection points identified, it is now not necessary to remove the block as these 12V connection points are accessible from the top of the block. This current protocol involved connecting 3 circuits individually to the precharge and two contactor relays. This was achieved merely by wiring in extra lines on top of existing wiring connector points. With hindsight, a more effective alternative is included in the discussion below (Unlocking a crashed battery).
https://github.com/juancruz1953/Images/blob/main/Atto3ContactorBlockRewire.pdf

## Contactor control over CAN (software — no teardown)
As an alternative to wiring the contactor block to GPIO via SSRs, Battery-Emulator
can open and close the pack's **own** contactors **over CAN**. For a healthy (non-crashed) pack this means **you don't need to open
the battery or fit any relays.**
> Requires firmware **[10.11.0]+**
### Behaviour
- **Closing is automatic** — Battery-Emulator closes the contactors once the inverter
  signals it is ready and there is no active fault.
- **Opening is sequenced like the car** — power is commanded to zero first, BE waits
  for current to fall to a safe level (with a timeout), then runs
  shutdown → open-request → standby. **The pack is never dropped under load.**
- Manual open/close is available from the **More Battery Info** page.
  *[confirm exact button labels]*
### Safety interlocks
Contactors are commanded **open automatically** whenever:
- the equipment-stop is active,
- the inverter withdraws permission to close (e.g. Solax / SMA not yet ready), or
- the system enters a **FAULT** state — including loss of CAN communication with the
  battery or inverter (faults after ~60 s).
### Notes
- Keep the original startup order: **power the BYD battery first, then
  Battery-Emulator.**
- There is no remote dead-man on the control link — if you lose the web UI / VPN, the
  contactors stay in their current state. For unattended installs, rely on the
  fault / e-stop / inverter interlocks above and treat manual control as on-site only.

## Parts list
Here are some of the part numbers and purchase links, incase your battery came without them
|  Part |  Product Link | Notes |
| :--------: | :---------: | :---------: |
| LV connector |  [AliExpress](https://a.aliexpress.com/_EugRLIo)   | 19pin 1192800MB 1192800FB BYD
LV connecor Pre-wired  | https://a.aliexpress.com/_EHMKS3i
| HV cable | ---- | OEM numbers: 1364774600 & SC2EM215300A or SC2EM-2105300
| HV cable PE5/PE6 | ---- | OEM numbers: EKEA2105300Y / 13568667-00

Example, high voltage cable for P48 Pack # 1364774600

![](../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-03.jpg)

Example, high voltage cable for PE5/PE6 Pack # EKEA2105300Y / 13568667-00

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-16.jpg" />

### Note on reusing HV cable :zap: 
If you are using the HV cable that came with the battery, and plan to cut off the ends to crimp on new terminals, be aware that the cables contain an outer shield layer. It is very important to properly insulate this, so you do not short high voltage to protective earth accidentally.

When preparing the cable, special attention must be taken the cable's shielding:

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-17.png" />

First make sure to leave at least 8mm space:

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-18.png" />

Then apply hot glue or other insulation adhesive:

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-19.png" />

Final insulation layer applied:

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-20.png" />

It is recommended to check your handiwork, by performing an insulation test on the cable after completing the work

<img alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-21.png" />

## How do I know if I have a crashed&locked battery?
If the contactors do not engage when sending CAN towards the battery, the pack is most likely locked.

Another way to check is to inspect the "More battery info" on the webserver. This page contains the SOC% value sent by battery (SOC Highprec). If this value stays the same when charging, discharging, the battery is locked.

## SOC Drift overtime
All users will experience a phenomenon where the battery’s SOC appears to drift when using SOC measured by BMS, causing the charging process to stop before the SOC reaches 100%. This drift will gradually increase over time, reducing the available capacity of the battery. Typical value is 1-2% SOC underreported drift per day.

> [!NOTE]
> As of firmware **10.10.1+** there is an Auto-calibration function to counteract this but the following manual method can still be used for SOC and capacity manipulation if required.

- Go to the "Calibrate SOC" option. From version **10.3.0** this can be done from the "More Battery info" page.
- Set the "Calibration target SOC:" option to the desired SOC% you want.
- Set the "Calibration target capacity:" option to the desired AH capacity (this value will be copied by default from the BMS and will effect your SOH (State Of Health) values!
- Finally, press the "Calibrate SOC" button

<img width="493" height="199" alt="image" src="../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-22.png" />

### Automatic SOC calibration

Rather than running the manual *Calibrate SOC* procedure periodically, Battery-Emulator
can **recalibrate SOC to 100% automatically** whenever it detects the pack is genuinely
full — correcting the BMS's gradual coulomb-count drift on its own.

> Requires firmware **[10.10.1]+**. (on by default).

#### What it does
When enabled, BE watches for the pack sitting at a true, settled top-of-charge and then
performs the **same calibration write as the manual button** — a security-access write
into the BMS — so the correction persists across reboots. It then starts a cooldown so it
won't repeat unnecessarily.

#### When it triggers
A calibration is performed only when **all** of these are true at once (whose status is visible in the more batt info page):

- Automatic calibration is **enabled**.
- The pack is at the **top of charge** — the charge taper has reached its critical stage
  (cells near full and current capped to the ~1 A tail).
- The **main contactors are closed** (the pack itself reports closed).
- **Current is essentially at rest** — roughly between 0.5 A discharge and 3 A charge.
- That settled, full condition has held **continuously for ≥10 minutes** (a brief current
  excursion of up to 60 s is tolerated without resetting the timer).
- Reported SOC has **drifted below 100 % by more than your configured threshold** (so it
  only acts when there's meaningful drift to correct).
- At least **1 hour** has passed since the last calibration (cooldown).

If any condition isn't met — for example your setup never quite reaches a sustained full
charge — it simply won't fire, and you can still calibrate manually.

#### Configuration
On the **More Battery Info** page:
- **Auto-calibrate SOC to 100% when full** — the on/off toggle.
- **Auto-calibrate trigger drift (%)** — how far below 100 % SOC must drift before an automatic
  recalibration is allowed (higher = less frequent corrections).
- A live status panel shows each trigger condition (taper reached, current in-window,
  dwell timer, drift %, cooldown ready, contactors closed) so you can see exactly why a
  calibration has or hasn't happened.

#### Notes
- It is deliberately conservative: it requires a genuine, *sustained* full charge **and**
  real drift **and** the cooldown, so it won't spam writes to the BMS.
- It writes to the BMS exactly like the manual procedure, so the same persistence and
  caveats apply.

## How do I unlock a crashed battery?
There are two methods to try and unlock the battery. The methods are via More Battery Info page (easy), and alternatively via CAN Replay (harder)

> [!IMPORTANT]
> To be able to unlock, you need separate control over B+ and IGN pin going towards battery (The two 12V pins on the battery). These need to be powered on/off in a specific sequence

- Pin 4 12v+ BMS
- Pin 5 12v+ ignition
- Also make sure 12V supply has atleast 12.8V and 2A available before starting the unlock procedure

### More Battery Info Unlock
There is a button in the "More Battery Info" page in the webserver, that when pressed will attempt to unlock the crashed battery.

![image](../images/byd-vehicle-atto-3-seal-tang-dolphin-song-and-more-04.png)

### CAN replay
One user reported success by manually sending the CAN log file while the battery 

[resetLockedBYD_v1.txt](https://github.com/user-attachments/files/20038227/resetLockedBYD_v1.txt)

User 1: About the power cycle and how I did it..
- Battery-Emulator compiled with only TEST_FAKE_BATTERY and no inverter selected
- Started with no power to either 12V constant or 12V ignition. I have separate switches for them though.
- So first Battery-Emulator hardware is powered on.
- Then 12V constant switch on, wait a few seconds and ignition on.
- At this point no communication is present on CAN, complete radio silence.
- Run unlock commands, upload resetLockedBYD_v1.txt in the CAN replay page in Battery-Emulator, and transmit it towards the battery
- Once again radio silence.
- Switch off 12V ignition.
- Wait a few seconds and then switch off 12V constant.

User 2 success story:
- I have B+ and the 2 ignition wires on seperate switches.
- I turn on B+ first then ignition.
- Software was setup for BYD ATTO 3, v8.13.0
- Then I ran unlock procedure via "More Battery Info" page
- After the unlock I turned off ignition then B+ and the Liligo together then reverse process turning back on.
- Contactors closed after.

