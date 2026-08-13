---
title: "Volkswagen MEB"
---

# Volkswagen MEB battery platform

!!! info "IMPORTANT"
    The MEB batteries do **not** have any precharge resistors built in. They need to see actual battery voltage on the high voltage terminals before the battery can turn on the contactors. Due to this requirement the MEB batteries are harder to re-use compared to most EV battery packs. To achieve this, a standalone lab PSU or high voltage isolated boost converter can be used to generate the high voltage needed to start the battery.

---

This platform is used across the brands of the Volkswagen Group (VW / ŠKODA / CUPRA / AUDI).
It is composed of cell modules, cell management controllers, a battery management system and some auxiliary components (pyrofuse, fuse, current measuring, contactors, etc.).

The capacity of the battery is determined by the number of modules. Each module has a capacity of 6.85 kWh. The chemistry is NCM712.

| Modules | Configuration | Capacity | Cells in series |
|---------|---------------|----------|-----------------|
| 7       | 2p12s         | 48 kWh   | 84              |
| 8       | 2p12s         | 55 kWh   | 96              |
| 9       | 2p12s         | 61 kWh   | 108             |
| 12      | 3p8s          | 82 kWh   | 96              |

<details markdown="1">
<summary><strong>Vehicles using the MEB platform</strong></summary>

- Audi Q4 e-tron (2021–present)
- Audi Q4 Sportback e-tron (2021–present)
- Audi Q5 e-tron (2021–present)
- Cupra Born (2021–present)
- Cupra Tavascan (2023–present)
- Volkswagen ID. UNYX (2024–present)
- Ford Explorer EV (2024–present)
- Ford Capri EV (2024–present)
- Škoda Enyaq iV (2020–present)
- Škoda Enyaq Coupé iV (2022–present)
- Škoda Elroq iV (2025–present)
- Volkswagen ID.3 (2019–present)
- Volkswagen ID.4 (2020–present)
- Volkswagen ID.5 (2021–present)
- Volkswagen ID.6 (2021–present)
- Volkswagen ID.7 (2023–present)
- Volkswagen ID.7 Tourer (2024–present)
- Volkswagen ID. Buzz (2022–present)
- Volkswagen ID. Buzz Cargo (2022–present)

</details>

More background on batterydesign.net: [MEB](https://www.batterydesign.net/volkswagen-meb-battery-pack-id-family/) and [ID4 82kWh](https://www.batterydesign.net/vw-id-4-82kwh-battery/).

## Testing the battery before purchase

You can test a battery before buying it with a simple LilyGo + CAN-FD add-on board. With this setup you can see if the battery is in crashed mode (blown pyrofuse). Explained in this Swedish video (use English subtitles): <https://www.youtube.com/watch?v=PsB-5heAPhg>.

For even more info on the MEB battery, you can use ODIS to read out the full error registers.

## Software configuration

For this battery type, use the option **"Volkswagen Group MEB platform via CAN-FD"** under the **Battery Protocol** setting.

![Battery Protocol setting](../images/meb-01.png){ width="584" }

## LV connector

![MEB connector](../images/meb-02.png){ width="600" }

For communication with the battery, **slot C** must be used.
You can either reuse an existing connector or buy a new one.

![Slot C female](../images/meb-03.png){ width="500" }

The original TE connector is restricted, no information will be given by TE, but it can be found via AliExpress or Alibaba (some will arrive without terminals/receptacles — ask the seller up front). The easiest and quickest way to get the connector housing is to buy it as a spare part from a VAG dealer.

![VAG part 5Q0973733A](../images/meb-04.jpg){ width="500" }

- **Connector housing** (complete spare part kit including connector cover etc., but without pins):
  - TE part: `0-2315221-1` or `5-2315221-1`
  - VAG part: `5Q0 973 733 A`
- **Small pins** 0.5 × 0.4 mm: `1-2177909-1` (or `2177909-1`)
- **Large pins** 1.2 × 0.6 mm: `7-1452671-1`
- **3D-printed cover** for the connector: [meb_CAN_cover_v1.zip](https://github.com/user-attachments/files/19849815/meb_CAN_cover_v1.zip)

The pins can also be requested directly from TE.com as a (free) sample.

## HV connector

![MEB HV connector description](../images/meb-05.png){ width="600" }

The connector marked **AC Charger** is wired in parallel to the **motor inverter** port. The DC-charging port has its own contactors.

- 3D-printed cover for the AC Charger port: [MEB-Cover_for_internal_Charger.zip](https://github.com/user-attachments/files/27005556/MEB-Cover_for_internal_Charger.zip)
- 3D-printed cover for the CCS or Inverter connector: [MEB-Cover_for_inverter_or_CCS.zip](https://github.com/user-attachments/files/26513415/MEB-Cover_for_inverter_or_CCS.zip)

Cable part number for the inverter connector: `1EA971015T`, `1EA971015AA` or `1EA973732X`.

If reusing cables from a donor car:

| Cable | Cross-section |
|-------|---------------|
| DC charge port      | 70 or 95 mm² |
| Motor inverter      | 35 or 50 mm² |
| Onboard AC charger / A/C / PTC etc. | 6 mm² |

## Wiring details

![Slot C pin description](../images/meb-06.png){ width="600" }
![Slot C details](../images/meb-07.png){ width="600" }
![Wiring example](../images/meb-08.png){ width="600" }

An AWG24 ethernet cable seems to work well: one pair for CAN, one for the pilot line, two pairs for 12 V — with two wires crimped together on pin 1 for GND.

For the 12 V supply a 30 W power supply has been found to work fine; the BMS draws around 21 W.

!!! note "NOTE"
    **Wiring size:** Using a single strand of a pair for +12 VDC, ignition and GND also works, but the maximum allowable length is **< 10 m**. Going longer leads to contactors failing to close, and this failure does **not** show up in ODIS as an error. You may hear one contactor close, but it will open again because the voltage drop is too big when the BMS tries to close both contactors.

### Important information

- The battery control unit uses **CAN-FD** for its communication!
- If CAN communication is lost, the contactors open immediately (nice safety feature).
- The **pilot line** circuit must be closed; without this connection, the control unit will not allow the contactors to close. Pins **16** and **22** must therefore be connected. If the pilot line circuit is broken, the Battery-Emulator raises an event.
- The `KL30C` message on the **More battery info** page shows the status of the ~~+12 VDC ignition~~ service-disconnect input (pin C5). This needs to be high (12 VDC) to allow the battery to operate.

Another requirement from the BMS: it evaluates the presence of voltage on the external terminals of the battery before closing the contactors. Under normal circumstances in the car, the main inverter starts generating the actual voltage (depending on battery model and SOC, 300–450 V) from the 12 V battery. The battery controller detects this external voltage; if it is close enough (within a few volts) and everything else is OK, the battery is switched on. This is to prevent arcing of the contactors — an alternative to a precharge resistor.

The same approach is required when the battery is outside the car and you want to turn it on. You need an external voltage source that connects to the battery terminals (output to the motor inverter) and puts the same voltage as the battery on those terminals to within a few volts. Then it is only possible to switch on the battery by command via the CAN bus. For info on high voltage sources, see [this page](../setup/hardware/high_voltage_source.md).

You can check if your battery fulfills the required preconditions by opening the **More Battery Info** page. This is what a functional battery looks like, with the contactors ON:

![Status](../images/meb-09.png){ width="600" }

### Hardware list

- Lilygo TCAN / Stark CMR module — see the main wiki page
- CAN-FD add-on board — see the [CAN-FD add-on wiki page](../setup/can_related/can_fd_add_on_mcp2518fd.md)
- A high voltage boost converter, e.g. the HIA4V1 (see above)
- Low voltage connector + pins (see above)
- 12 V power supply, e.g. Meanwell HDR-30 12 V
- High voltage connector + cable (see above for options)
- High voltage DC circuit breakers + e.g. DIN rail clamps to step down from 50 mm² to a smaller diameter wire (if using the motor inverter connector)
- _Nice-to-have:_ Emergency / maintenance shutdown button, preferably protected against accidental turn-on with a lock — [example](https://nl.aliexpress.com/item/1005006825289029.html)

!!! tip "TIP"
    For beginners it is much easier to use the **Stark CMR** with this battery compared to the LilyGo boards.

### SW settings example

Stark CMR based, automatic precharge enabled.

![SW settings 1](../images/meb-10.png){ width="600" }
![SW settings 2](../images/meb-11.png){ width="600" }

### Strange behaviors

#### Pilot line does not function as expected

- Disconnecting the pilot line **before** turning the battery on results in contactors not closing.
- Disconnecting the pilot line **when contactors are closed** only results in `HVIL status: Open!`, but contactors stay closed (pilot line alone is therefore **not** suitable for emergency shutdown).
- In all cases the pilot line bit in `0x5A2` does not change.

An alternative is to remove 12 V from `T30C` (service disconnect), which directly results in the contactors opening.

#### `AUTOMATIC_PRECHARGE_FAILURE`

At startup, the HV init process starts and the precharge relay is activated. In case precharge fails for some reason (e.g. a cabling issue), the pack can log `P0C7800`, and BE logs `AUTOMATIC_PRECHARGE_FAILURE`, which can be recovered as follows:

1. Remove power from the full system (BE and battery 12 V).
2. Open the precharging breaker, which disconnects the HIA4V1 from the battery.
3. Apply power again — the system tries to start precharging but fails → BE gives `AUTOMATIC_PRECHARGE_FAILURE`.
4. Remove power from the full system.
5. Reconnect precharging.
6. Re-apply power.
7. The BMS is in an error state which requires ODIS to reset (`Precharge Time Too Long P0C7800`).
8. After clearing it via ODIS, it works again normally.

### Info for specific inverters

#### Solax G4

Set the following Solax settings to get the battery to work:

```
NUMBER_OF_MODULES 8
BATTERY_TYPE 131
```

---
# Water coolant connection:

The connection is indicated as a VDA c-lock connection size NW16.
After some searching i found these at Autodock for a few Euro's.
See picture below, they fit perfect.
![20260526_165440](../images/meb-12.jpg){ width="600" height="700" }
![20260526_165433](../images/meb-13.jpg){ width="600" height="700" }

# Unlocking a MEB battery

## Steps

1. Communicate to the battery and identify issues.
2. Physically repair the battery.
3. Build and connect ODIS via the bridge.
4. Battery unlock procedure.

## Tools

- T25 Torx to open the metal cover
- 24 mm (?? check size) socket wrench
- T27 isolated Torx
- Personal protection equipment
- Additional Lilygo flashed with the [ODIS relay](https://github.com/dalathegreat/Battery-Emulator/archive/refs/heads/feature/ODIS-relay.zip) firmware (adjust AP name if you already have the same name)
- CAN-FD interface (remove the 120 Ω resistors R2 and R3)
- Windows 10 laptop with ODIS installed
- VAS 6154 dongle or clone

## Procedure

### Battery issues that can be unlocked

> **Crash locked:** on the **More Battery Info** page the error _"BMS fault emergency shutdown"_ has state _Active!_

> **Welded contactor locked:** on the **More Battery Info** page the error _"Welded contactors"_ has state _At least 1 contactor welded_.

## Clearing the crash log from MEB using ODIS V25

1. Go to **Self-diagnoses**. ODIS will try to detect the VIN but will fail — this can take some time, just wait. When it fails, add a VIN. Any VIN should work, e.g. `WVGZZZE2ZPE010564`. Then start **OBD** to launch ODIS.
   ![ODIS step 1](../images/meb-14.png){ width="900" }

2. After starting ODIS you get this screen, where you can select the vehicle.
   ![ODIS step 2](../images/meb-15.png){ width="900" }

3. We need to access `008C` — just double-click it. Sometimes this throws an error; when it does, just restart the ODIS gateway and continue.
   ![ODIS step 3](../images/meb-16.png){ width="900" }

4. After selecting `008C` we get the following screen.
   ![ODIS step 4](../images/meb-17.png){ width="900" }

5. Here we can see the crash log is active.
   ![ODIS step 5](../images/meb-18.png){ width="900" }

6. Go to **Access Authorization** and press the small green arrow.
   ![ODIS step 6](../images/meb-19.png){ width="900" }

7. To get access, use code `20103` and press **Implement**.
   ![ODIS step 7](../images/meb-20.png){ width="900" }

8. Switch to **Basic settings** and press the small green arrow again. Then we can start clearing the crash log memory.
   ![ODIS step 8](../images/meb-21.png){ width="900" }

9. In Basic settings, select **DTC memory entry deletion trigger** and move it to the right with the arrows in the middle. Press **Next** (arrow bottom-right above the red cross), and **Next** again on the following page.
   ![ODIS step 9](../images/meb-22.png){ width="900" }

10. You will see many entries, but the one we need is **Crash signal**. Search for it and move it to the right. **Only clear this one!**
    ![ODIS step 10](../images/meb-23.png){ width="900" }

11. Press **Start** and go back to **DTC Memory** via the small arrow top-right.
    ![ODIS step 11](../images/meb-24.png){ width="900" }

12. Finally, to clear out the crash log press **OBD-System** and **OK** on the next screen.
    ![ODIS step 12](../images/meb-25.png){ width="900" }

13. If everything went successfully, there should be no more crash log after pressing **Update NOW**.
    ![ODIS step 13](../images/meb-26.png){ width="900" }

### Battery disassembly and replacing the pyrofuse

1. Remove all the small Torx screws (TX20) around the top. There are many, so make use of an electric impact screwdriver.
   ![Step 1](../images/meb-27.jpg){ width="480" }

2. Remove the larger big-head bolts (TX30), coated in paraffin. Remove the 4 big lug nuts (28 mm). They are really tight — a large impact wrench is advised.
   ![Step 2](../images/meb-28.jpg){ width="480" }

3. Remove the lid so you can access the BMS, and remove its orange protection cap (loose fit — just grab and lift).
   ![Step 3](../images/meb-29.jpg){ width="480" }

4. BMS top view.
![Step 4](../images/meb-30.jpg){ width="480" }

5. Remove both HV bus bars, preferably with insulated tools (TX30).
![Step 5](../images/meb-31.jpg){ width="480" }

6. Pull the red lid up to unlock the connector and get it out of the BMS.
![Step 6](../images/meb-32.jpg){ width="480" }

7. Push both sides of this connector and pull it up.
![Step 7](../images/meb-33.jpg){ width="480" }

8. The black connectors just have a locking latch — push them to the side and lightly pull to remove (mark them **R** and **L** to avoid swapping). The pyrofuse can be stuck; wiggle with a small screwdriver.
![Step 8](../images/meb-34.jpg){ width="480" }

9. Loosen all 4 long bolts in the corners of the BMS. Loosen the 4 black bolts of the bus bar. Put a small screwdriver under the BMS to loosen the adhesive thermal paste, and push it as far to the back as possible to create space for the bus bar.
![Step 9](../images/meb-35.jpg){ width="480" }

10. When you know how, it’s easy. Spoiler: lift the bus bar vertically. 🙂
![Step 10](../images/meb-36.jpg){ width="480" }

11. All clear to take it out.
![Step 11](../images/meb-37.jpg){ width="480" }

12. There are small locking hooks on the left and right. Push them in with a screwdriver while you pull upwards. You can use a screwdriver on the corners to push the lid up. (Keep the locking hooks in your line of attention!)
![Step 12a](../images/meb-38.jpg){ width="480" }
![Step 12b](../images/meb-39.jpg){ width="480" }

13. Opened.
![Step 13](../images/meb-40.jpg){ width="480" }

14. The culprit: defective pyrofuse.
![Step 14](../images/meb-41.jpg){ width="480" }

15. When disassembled, measure your pyrofuse. There are 2 dimensions: one 83 mm long and one 85 mm long. Holes of 7 mm at 63 vs 70 mm heart-to-heart. A nickel-plated grounding bar of 20 mm wide and 6 mm thick was used, capable of 360 A.
![Step 15a](../images/meb-42.jpg){ width="480" }
![Step 15b](../images/meb-43.jpg){ width="480" }
![Step 15c](../images/meb-44.jpg){ width="480" }

16. Note the differences.
![Step 16](../images/meb-45.jpg){ width="480" }

17. Try to recover the pins of the pyrofuse.
![Step 17](../images/meb-46.jpg){ width="480" }

18. Bus bar in place.
![Step 18a](../images/meb-47.jpg){ width="480" }
![Step 18b](../images/meb-48.jpg){ width="480" }
![Step 18c](../images/meb-49.jpg){ width="480" }
![Step 18d](../images/meb-50.jpg){ width="480" }

19. Close it up.
![Step 19](../images/meb-51.jpg){ width="480" }

20. The recovered pins connected to a 2.7 Ω resistor, insulated with shrink tube.
![Step 20](../images/meb-52.jpg){ width="480" }

21. Install it on the pyrofuse connector.
![Step 21](../images/meb-53.jpg){ width="480" }

22. Put a shrink tube on the connector and resistor so it cannot come loose.
![Step 22a](../images/meb-54.jpg){ width="480" }
![Step 22b](../images/meb-55.jpg){ width="480" }

23. Install everything in reversed order. Don’t forget the cable ties to keep it all in place.
![Step 23](../images/meb-56.jpg){ width="480" }

24. Install the 2 HV bus bars. Don’t be afraid of a little protest — it’s charging the capacitors and electronics. (Be very careful though — HV DC is not to be joked with!)
![Step 24](../images/meb-57.jpg){ width="480" }

25. Put the orange cap on and assemble the lid again. (Testing first is advised.)
![Step 25](../images/meb-58.jpg){ width="480" }

Good luck, and have fun with your beautiful battery! 🔋

### Battery repair procedures

!!! warning "CAUTION"
    When disconnecting the BMS (battery internal), the repair manual specifies a specific order of disconnection!
    Failing to do this can **trigger the pyro fuse**. Make sure to follow the correct procedures when performing internal repairs to the battery — a service manual is available.

    1. First remove any external connections to the battery (motor/inverter, AC charging, DC charging and data connection).
    2. Then remove the orange bus bar connections to the positive and negative connector/contactor blocks.
    3. Split the pack in 2 by removing the small orange bus bar at the end of the pack.
    4. Finally the BMS can be disconnected.

    Reconnection happens in reverse order.

**Welded contactor:** test the contactor and check if it is welded. If needed, replace the contactor.

> TODO: add contactor part numbers.

**Pyro fuse:** replace pyro fuse options
- New pyro fuse _(TODO: add type number)_
- Normal fuse, like _(TODO: add type number)_ and a 2.5 Ω resistor to the BMS connection (can replace the external fuse)
- Jumper bridge (DIY) and a 2.5 Ω resistor to the BMS connection (external fuse still required)

![Pyrofuse](../images/meb-59.jpg){ width="600" }

There are 2 different lengths of pyrofuses used: 63 mm and 70 mm (screw holes center-to-center). _(Note: my pack only had 1 pyrofuse.)_

| Center-to-center | Part number |
|------------------|-------------|
| 63 mm | `9j1915463a` |
| 70 mm (black)  | `11k915463b` |

- Genuine Volkswagen sealant part number: `D454300H2` (blue sealant between the top cover of the battery)
- Oval hexagon socket head bolt part number: `WHT009218`

### Lilygo ODIS setup

Below is the connection diagram for the setup. When Wi-Fi APs are used, make sure both Lilygos have a different name.
Remove the 2 × 60 Ω resistors in series.

![Lilygo ODIS setup](../images/meb-60.png){ width="700" }

### Short unlock procedure

1. Go to **OBD**.
2. Start diagnostics.
3. Manually insert VIN and car type.
4. Read modules.
5. Open the Hybrid battery module.
6. Check errors.
7. Enable access via code `20103`.
8. Basic settings — clear the DTC that is needed _(create list here)_.
9. Enable access via code `20103`.
10. Clear OBD memory.

Check if the error is gone via the Lilygo.

🎉 Party time!

---

# Manually balancing a module

## Important information

The balancing of the modules works and is automatically controlled by the BMS when there is a significant imbalance. It seems to only get activated during the charging cycle of the battery, but this needs to be verified by other users. If there is a significant imbalance when first buying the battery, it is easier to manually balance the battery first.

Depending on the type of battery pack you have, make sure to buy the correct balancer, as the supply voltage is different.

Module voltages:

| Module       | Pack capacity                 | Nominal voltage |
|--------------|-------------------------------|-----------------|
| 8s3p         | 82 kWh                        | ±33 V           |
| 12s2p        | 62 kWh, 55 kWh & 48 kWh       | ±50 V (OK for 48 V systems) |

For the **8s3p** module you need the **JK BMS B2A16S** active balancer, as it has a lower voltage range of 24 V – 70 V. The **B2A24S** (the standard one on the JK BMS website) has a voltage range of 40 V – 100 V and will not start up because the module voltage is out of range. While you can use a DC-DC boost module to make it work according to JK BMS, it becomes unnecessarily complex — you don't need the 24-cell balancer for either MEB module type.

For the **12s2p** it doesn't really matter which one you use, as the module voltage is high enough and within range of both balancers.

![JK B2A16S](../images/meb-61.jpg){ width="500" }

## Making the connectors

Follow the guide at <https://www.evcreate.com/using-volkswagen-meb-battery-modules/#connecting-bms>.

The white connector is the module connector for the **8s** module; the black connector is the module connector for the **12s** module.

Cut the wires of the blue/brown connector and solder them to the corresponding leads of the balancer. The wire of the last positive cell also needs to be connected to the **PWR** input of the balancer.

![20s battery wiring diagram](../images/meb-62.jpg){ width="600" }

## Module layout

The battery modules follow the order they are plugged into the CMU modules. You can see the alternating brown / blue / … connectors indicating the module order.

![MEB module order](../images/meb-63.jpg){ width="600" }

In this example, cells 31, 33, 49, 65, 72 and 88 need to be balanced (or modules 4, 5, 7, 9 and 11).

![MEB cell monitor](../images/meb-64.png){ width="600" }

## Steps

1. Charge the entire pack to 100 %, or until all of the cells are around 4.15 V.
2. Split the battery pack in two by removing the middle connector in the back.
3. Remove all of the other orange module connectors. Make sure to follow the correct order as mentioned above.
4. Remove all the BMS connectors and unplug all of the module connectors (black/white).
5. Verify that all the modules are at approximately the same voltage and connect them in parallel. All modules will now start to equalize their voltage on module level.

    !!! info "IMPORTANT"
        It is important that all of the modules have the same voltage before connecting them in parallel, to prevent high balancing currents! 1.5 mm² wire can be used; the maximum current in this case was ± 5 A. Make sure the parallel wire does not touch anything other than the intended terminals!

   Connecting the modules in parallel is important to prevent the module being balanced from having a lower module voltage than the rest of the pack. The active balancer actively moves charge from one cell to another, but it is never 100 % efficient. The parallel connection keeps all modules at the same voltage while the balancer balances individual cells.

6. Plug the balancer into the module that needs to be balanced. When first plugging in the balancer, configure the cell number and the maximum balancing current.

    !!! warning "WARNING"
        **Do NOT exceed 300 mA!** If the balancing current is too high you risk blowing the fuse inside the module, which cannot be repaired. Even though the B2A16S claims a minimum balancing current of 100 mA, the settings don't allow anything lower than 300 mA.

7. Enable balancing and wait. The 120 mV imbalance of cell 31 took about 8 days to fully equalize.
8. Reassemble the battery when finished. Make sure to follow the torque specs when tightening the bolts ⬇️

![MEB torque specifications](../images/meb-65.png){ width="600" }

Example of balancing current after connecting the modules in parallel ⬇️

![Balancing current example](../images/meb-66.jpg){ width="600" }

### Extra info

From safety testing, we have concluded that the MEB batteries will automatically open the contactors if the temperature sensors inside the battery go over **70 °C**. (We automatically write `0W allowed` if the temperature goes too high, but it's nice to know there is an extra layer of safety built into the MEB BMS.)
