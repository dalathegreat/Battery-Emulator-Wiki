---
title: "MG HS PHEV"
---

## Contents

- Models
- Current status
- Prerequisites
- Software configuration
- Connections
  - Low Voltage (LV)
  - CAN communication
  - High Voltage Interlock (HVIL)
- Issues
  - Earth leakage / isolation resistance testing modification
- Additional information

## Current status

The Gen1 MG HS PHEV battery is fully usable, although a modification may be necessary (depending on your inverter/RCD) that requires opening up the battery.

In some situations the battery may detect an isolation failure and open its contactors, which BE will detect, resetting the battery and closing contactors again. This doesn't seem to occur when under load, but sometimes happens during inverter startup.

Battery voltage and current, min/max cell temperatures, and individual cell voltages are reported to BE. The battery appears to be balancing automatically.

## Models

| Year |  Model | Battery capacity | Supported? | Notes |
| :--------: | :---------: | :---------: | :----------: | :----------: |
| 2018- | MG HS PHEV | 16.6kWh | ✅ | 
| 2022- | MG HS PHEV (Gen2) | 24.7kWh | Untested | Same as [Roewe RX5](https://en.wikipedia.org/wiki/Roewe_RX5)

Initial focus has been on getting the 16.6kWh battery working with Battery-Emulator (BE).

The Gen2 batteries use a different architecture (similar to the MG4), so are unlikely to work with this integration.

## Prerequisites

You will need:

 - A battery (with the MSD included)
 - A 12-14V power supply, ideally isolated (2-pin plug), capable of 3A output
 - HV connector and cable assembly (from scrapper)
 - LV connector (from scrapper or AliExpress)
 - Battery Emulator hardware with a CAN channel

## Software configuration
For this battery type, use the option called "MG Gen1 (HS/ZS/MG5/MarvelR)" under the "Battery Protocol" setting.

## Connections

The MG HS PHEV battery has 3 separate HV connectors (Orange), and a Low Voltage signal connector (Green). There are also two coolant ports that can be used for thermal management, left is inlet, right is outlet (optional)

![image](../images/mg-hs-phev-01.png)

### Low Voltage (LV)

![image](../images/mg-hs-phev-02.png)

![mg_lv_diagram](../images/mg-hs-phev-03.png)

This is the LV connector plug: [aliexpress](https://www.aliexpress.com/item/1005004815715620.html)
The one you need is the one with the black face.
There's a non-wired version too for doing your own crimping but this looks easier to implement.

![20250617_192645](../images/mg-hs-phev-04.jpg)

This is how Molex and MG label the terminals in the connector:

![32 Pin Molex MG](../images/mg-hs-phev-05.png){ width="897" height="691" }

The battery needs a 12V-14V supply, and draws 600mA continuous with the contactors closed, and ~3A briefly when closing the contactors. It also needs a 12V signal to wake it up (via a 1kR resistor, or connected directly) as shown.

To reduce potential issues with the isolation measurement, it is preferable to have a 12V supply that is isolated from the grid (eg, powered from a 2-pin double-insulated adapter).

### CAN communication

The battery has (at least) three CAN buses:

**CAN1** is (likely) the powertrain bus, which connects the main powertrain components. The battery outputs its vital statistics (voltages, SoC and temperatures) on this bus, and listens for the messages which control the contactors. This bus outputs about 500 messages/sec.

**CAN2** is (likely) the wider status/diagnostics bus. This has fewer messages (80 msgs/s), and some messages are abridged (eg, it includes a scaled SoC but not real SoC, voltage or current). OBD requests (0x7e5) work over this bus, and can be used to query for detailed statistics such as SoH.

**CANHV** seems to be the raw data from the HV-side controller in the BMS, and contains raw cell voltages and temperatures, and the current sensor output. This is useful for battery diagnostics, but has high rate of messages (1000 msgs/s).

The CAN1 and CAN2 buses should be bridged together (connecting the high/low pins in parallel) which provides the necessary information as well as allowing OBD/UDS communication (necessary to reset the battery if isolation failure detection occurs).

> Previous reverse engineering notes:
>
> [MG HS battery front panel.xlsx](https://github.com/user-attachments/files/20715269/MG.HS.battery.front.panel.xlsx) -
> this pinout map is based on continuity testing with and identification of internal battery components.
> There are some pins on the bottom row that go to the same chip and I'm not certain what two of them are, so have marked them as do not connect +12V in case it causes damage. I could be wrong, so please update this if you can elaborate.
> I have a running system based on this.
> I have only used one of the 4 CAN channels available through the low voltage connector (CAN2), but this is enough to run the battery emulator (although closing the HV contactors is WiP).

### High Voltage Interlock (HVIL)

The HVIL connections under the MSD are bridged together by the MSD itself.

The other HVIL connections on the front panel (on each of the three HV connectors) can be left alone, as the BMS doesn't care whether they're bridged or not.

## Issues

### Earth leakage / isolation resistance testing modification

The battery has two 90nF Y capacitors inside the contactor module between each HV output terminal and the battery case. It is therefore important to ground/earth the battery case, since with a transformerless inverter these will cause an earth leakage current of >20mA which could be hazardous if an ungrounded battery is touched.

Depending on your inverter and/or RCD, this current may be too high and trip the earth leakage detection, in which case you will need to modify the capacitor circuit to reduce the leakage. Check whether this is necessary by testing with your inverter/RCD first.

The BMS seems to rely on these capacitors when checking the isolation resistance between the HV connections and the battery case - when closing the contactors, and every few seconds whilst the contactors are closed. If it decides that there is a problem, the contactors will open, and the BMS will go into error state 15. Battery Emulator will detect this state and reset the BMS over CAN.

Isolation failure errors may be triggered by your inverter's own isolation tests (which are usually performed whilst it is connecting). The extent and inconvenience of this will depend on your exact inverter - a Solax X1-AC seems to only perform these tests before connecting, so as long as the inverter runs continuously without dropping out (or going into standby), it does not seem to trigger isolation failures in the BMS.

**Obligatory warning - taking the cover off a high voltage battery is dangerous. Remove the MSD first, wear insulating gloves, and check the voltage on all terminals before touching them.**

**The high voltages within the pack are reasonably well contained once the MSD is removed, but be careful around the orange-wrapped wires and connectors which may have ~175V between them.**

#### Step 1: Disconnecting the capacitors from ground

The isolation resistance measuring circuit does not have a DC connection to the case - it seems to rely on these Y capacitors to conduct the AC isolation resistance measuring waveforms. It is therefore possible to disconnect the centerpoint of the capacitors from the chassis ground, leaving them as an effective 45nF capacitance between the HV terminals, and simulating an infinite isolation resistance.

This can be done by removing the ground connection from the chassis to the contactor board, which is the dangling wire here (ignore the missing capacitor!):

![image](../images/mg-hs-phev-06.png){ width="934" height="744" }

and reinstalling the screw without the wire, and then insulating the dangling wire with some heatshrink:

![Screenshot_20250712_120242](../images/mg-hs-phev-07.png){ width="1078" height="757" }

#### Step 2: Floating the BMS ground above the case ground

There are two connections between the battery case and the electronics within:

- inside the contactor module (as disconnected in Option 1 above)
- underneath one of the BMS mounting bolts to the battery case

If you disconnect both, then the BMS ground will no longer be referenced to the battery case. You can then run an extra wire between the GND screw in the contactor module (shown in the image above), and the case of the BMS, which will bypass the battery case, and keep the isolation measurement completely separate. The wire will not carry much current, but should be well insulated as it will pass close to the main battery terminals.

You will also need to use an isolated 12V power supply (a 2-pin power supply with no earth pin) to power the BMS as well as the Battery Emulator hardware (unless you are using isolated CAN), to ensure that there is no current path between the BMS case and the inverter's ground.

## Additional information

### Second-generation (2022-?) LV pinout (untested)

Here is a list of functions for those pins on the second generation model:

![32 Pin Molex pins](../images/mg-hs-phev-08.png){ width="433" height="731" }

Lots of useful information here: [cardiagn](https://cardiagn.com/2022-2024-mg-ehs-hybrid-service-and-repair-manual-incl-wiring/)
