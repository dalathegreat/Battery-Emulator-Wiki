---
title: "Nissan LEAF / e-NV200"
---

## Physical size
The Leaf battery packs (24/30/40kWh) are all the same physical size. The 62kWh battery however is 40mm taller.

- 24kWh (2011–2012, ZE0) = 277kg (601lb) 1547.0 (L) × 1188.0 (W) × 264.0 (H) mm
- 30kWh (2013–2017, AZE0) = 294kg (648lb) 1547.0 (L) × 1188.0 (W) × 264.0 (H) mm
- 40kWh (2018–2023, ZE1) = 303kg (668lb) 1547.0 (L) × 1188.0 (W) × 264.0 (H) mm
- 62kWh (2018–2023, ZE1) = 410kg (903lb) 1547.0 (L) × 1188.0 (W) × 304.0 (H) mm

![Leaf 24/30/40kWh pack](../images/nissan-leaf-e-nv200-01.png)

The e-NV200 battery pack is 1578 (L) x 1102 (W) x 266 (H) mm and is packaged differently from the Leaf packs (active cooling and service disconnect at front instead of middle).

![e-NV200 24/40kWh battery pack](../images/nissan-leaf-e-nv200-02.jpg)

## Software configuration
For this battery type, use the option named **Nissan LEAF battery** under the **Battery Protocol** setting.

![image](../images/nissan-leaf-e-nv200-26.png)

- leave the **BMS starting sequence request** setting at its **other (default)** value if this pack is newly deployed. You can start experimenting with the other settings when you gained some experience on how balancing and degradation performs over time (using some monitoring solution over [MQTT](../setup/software/mqtt.md), like for example [Home Assistant](../setup/software/home_assistant.md). to observe behavior is strongly recommended when using experimental settings). Changing this setting requires a BMS reset.
- on a ZE0 (2011-2012 24kWh) battery, you can enable **Interlock required** for extra safety. The system checks that the original high voltage connectors and SDS are properly seated in before you can start.
       - If you enable this setting on a AZE0 or ZE1 (2013-2023) battery, both HV plugs need to be seated (80kW motor and 6kW heater). Thus for these it is recommended to **not** use **Interlock required** due to the inconvenience of having to source both HV connectors (and insulate manually one of them). Instead just block off the unused HV port with a 3D printed [cover](../setup/hardware/list_of_3d_printable_parts.md#heater-port-cover).
- set the **Battery chemistry** to **NMC**.

## Wiring diagram
The following pictures show an example of hooking up a LEAF battery to a Fronius Gen24 inverter. The same diagram can be useful for planning other inverter combinations.

!!! note "NOTE"
    The LEAF battery requires a 12V supply capable of delivering 1.5A

Remember to seat the service disconnect switch. Without this fitted, the battery will not output any voltage when contactors are closed.
This is how the SDS is used [(Youtube)](https://www.youtube.com/watch?v=tbo2Qzdj-Rg).

**Here's how to connect the high voltage lines**

The Positive (+) wire is close to the data port and the Negative (-) wire is close to the PTC High Voltage port (Aux Max 6kW).

![HighVoltageWiring](../images/nissan-leaf-e-nv200-03.png)

![423205153-0e4498c8-f8b8-41d3-bd6f-fa9e5d0640d2](../images/nissan-leaf-e-nv200-04.jpg)
![Zoe_harness](../images/nissan-leaf-e-nv200-05.jpg)

An even more detailed connection diagram, with automatic contactor control via solid state relays for maximum safety. This diagram features the optional BMS reset relay (if you are not using this, just supply BAT+IGN with constant 12V), and an optional equipment stop circuit.

Nissan's own documentation uses pin numbering on the 36 pin low voltage connector which does not match the moulded connector. The connections on this diagram have been renumbered so that they do.
![lilygo draw](../images/nissan-leaf-e-nv200-06.png)

## Precharge/Contactor closing
Almost all EV batteries contain contactors and precharge relays. Contactors act like big relays, and are used to control electrical circuits where currents are high. They are designed to be able to break the flow of current in a safe manner without electrical arcing. There are two contactors, one for positive and one for negative. To avoid electrical arcing when turning on the battery, the initial inrush of current is led thru a precharge resistor, to allow for slow charging of the capacitors inside the inverter. If the inverter has been turned off for a long time, the capacitors inside will act almost as a dead-short, 0 ohm resistance. If you would skip using the precharge, then your contactors will spark every time you close them, wearing them out prematurely. Negative, precharge and positive need to be switched separately in order, to ensure safe operation even if some malfunction would occur. Now that we know what the contactors/precharge does, we can look at how to control it.

### Automatic control 🤖
Battery Emulator hardware can act on its own, and turn on/off the contactors/precharge resistor when the battery says it is OK and turn off when not OK to proceed. This is done via the 3.3V digital output header that is located on the board. To use these, you need to solder a 2x6 row connector onto the board. After the row connector is fitted, you can connect a flat ribbon cable between the pins, and the relays.

To enable the feature in the software, Enable the "Contactor control via GPIO" option on the Settings page.

![image](../images/nissan-leaf-e-nv200-22.png){ width="505" height="42" }

To keep things simple, it is recommended to use Solid State Relays (SSR). These can be activated with 3Volt, and control large DC currents. Follow this schematic to complete the circuit:

The pin numbers below are the ones used on the LilyGo T-CAN485, check the HAL definitions of your own board if you use a different one:

- Precharge pin 25 - Precharge SSR + input
- Positive Contactor pin 32 - Positive SSR + input
- Negative Contactor pin 33 - Negative SSR + input
- GND - All 3x SSR - input

OPTIONAL: If you use SSR relays with the Battery-Emulator hardware, you can also enable PWM mode for reduced power consumption. Here are parameters confirmed working with the LEAF contactors+PWM.

![image](../images/nissan-leaf-e-nv200-23.png){ width="624" height="118" }

![bild](../images/nissan-leaf-e-nv200-07.png)

Before the contactors turn on, both Inverter and Battery needs to give OK ✅ signal. This can be verified via the Webinterface:

![bild](../images/nissan-leaf-e-nv200-08.png)

### Manual control 🖐️
!!! warning "WARNING"
    New hardware requirement for Fronius :warning: Battery voltage is reported towards Fronius inverters only after contactors are engaged. **This means that old legacy installs using manual A/B/C switches for turning on battery contactors will no longer function with Fronius inverters.** Only automatically controlled  contactors via GPIO will work. This is a new stricter safety requirement to get the Fronius inverter to startup faster and with less errors. The bonus is that GPIO controlled contactors is inherently safer than manual A/B/C triggering.

## Periodic restart of BMS
The BMS in the Nissan LEAF packs was not designed originally to operate 24/7 under all conditions. Over time the SOC% will become less accurate, and in some conditions even the GIDS (Wh remaining) becomes confused (see [Issue 86](https://github.com/dalathegreat/Battery-Emulator/issues/86)).

See the [Periodic Reset page](../setup/hardware/periodic_bms_reset.md) for details. Based on empiric observations the 30kWh (2013–2017, AZE0) pack benefits most from the 24h period together with the **Skip reset for one period if balancing** option enabled. Changing **BMS starting sequence request** to **normal charge** may improve balancing on AZE0 packs.

!!! tip "TIP"
    The LEAF battery is fully charged at 92-96% SOC. Use the [Rescale SOC](../setup/software/webserver_guide.md#rescale-soc) function to get a nicer looking 100% curve! However, Nissan specifically advises against habitual full charging, which adds wear - thus, for longer lifetime, you should set **SOC max percentage** to **80.0**.


## Insulation resistance

!!! note "NOTE"
    When contactors are closed, the Battery's own insulation measurement shows values averaging around 100kΩ - this is normal!

For further information about how insulation measurement values should be interpreted, check out the [Insulation monitoring](../setup/hardware/insulation_monitoring.md) page.

## Part numbers for Nissan LEAF batteries
In case your battery is missing some wires/disconnect switches, here are the OEM part numbers and purchase links. Do note that it might be cheaper to source from your local scrapyard!

|  Product |  Purchase Link |
| :--------: | :---------: |
| Service disconnect switch (2011-2012) 2971C13NA0B |  [Ebay](https://www.ebay.com/sch/i.html?_nkw=fuse+2971C13NA0B)   |
| Service disconnect switch (2013-2023) 297C1-3NF0A |  [Ebay](https://www.ebay.com/sch/i.html?_nkw=nissan+297C1-3NF0A&_sacat=0)   |
| 22pin battery connector (2011-2012) Yazaki 7283-8750-30 |  [AliExpress](https://www.aliexpress.com/item/1005003344398420.html)   |
| 36pin battery connector (2013-2023) Yazaki 7287-1065-30 |  [AliExpress](https://www.aliexpress.com/item/1005004180391674.html)   |
| Precrimped 22/36 connectors | [AliExpress](https://www.aliexpress.com/item/1005005815234149.html)   |
| High voltage connector 80kW 297A6-5SH1A |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A65SH1A&_sacat=0)   |
| High voltage connector 80kW 297A22581R ZOE, also works |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A22581R&_sacat=0)   |
| High voltage 80kW cable 297A21061R from ZOE41 ( Both end have the good connector ) |  [Ebay](https://www.ebay.com/sch/i.html?_from=R40&_nkw=297A21061R&_sacat=0)   |
| 4ch SSR on DIN rail. Make sure you get DC-CN. | [AliExpress](https://aliexpress.com/item/1005007825084745.html) |

A [spreadsheet](https://docs.google.com/spreadsheets/d/14ghFL5mUg0hlUOsraOJc9BExlsMp5ClRRITRSQVLfkA/edit?gid=0#gid=0) with parts and links for a Nissan 40kwh battery and 8kW inverter (30A fuses).

297A6 3NA0A does not fit, you have to cut a part of it to use the pins!

![image](../images/nissan-leaf-e-nv200-09.png)

**Incompatible cables**
When searching on eBay you may come across other cables in the Zoe which use a connector that is similar in appearance but is much smaller:

* Zoe HV Wiring Harness - PN: 240419193R
* Zoe HV Engine Bay Wiring Harness - PN: 240413370R

These will *not* connect to the Leaf battery terminals.

## Communication cable AWG limits
22 or 36pin connector are designed with an hole of 2.1mm that would contain cable and included elastic ring for water proof seal.
AWG 22 (0.5mm²) is enough cable section for the supported Amps.

Normal cable of the above section (22AWG) have a protective rubber that is too thick (usually 2.1mm external diameter) => need to choose automotive cable that follow reduced rubber cable standard (FLRY-A or B ISO 6722) that shouldn't be thicker than 1.5/1.7mm (better 1.5) outside diameter.

Need at least 0.7/1mm thick cable (e.g. cable + wrap) to allow correct water proof e.g. no ethernet cable can be used because too thin. Ethernet cable can go from 23 to 26 AWG. Normal AWG is usually 24 AWG that is rated for max 0.5A.
HV battery contactors drain continuously 0.4A each one at 12v.

BTW it's not strictly necessary to be automotive grade cable if it has enough copper diameter (0.5mm²) and outer diameter of ~1.5mm.

NOTE: If you pin your connector yourself - ensure the pins go all the way to the bottom and the pin is seated properly. If they are inserted incorrectly (not far enough, "wonky") then you won't have proper communication.

Here is a nice example of a completed 22-pin 2011-2012 cable:

![image](../images/nissan-leaf-e-nv200-10.png)

![Yazaki_22pin](../images/nissan-leaf-e-nv200-11.png)

Crimping B24 (36pin) connector in progress.

![image](../images/nissan-leaf-e-nv200-12.png)

### NOTE about cable code

* FLRY-A Automotive low voltage cable (FL) with reduced thickness of insulation (R) made of PVC (Y), with regularly stranded conductor (A)
* FLRY-B Automotive low voltage cable (FL) with reduced thickness of insulation (R) made of PVC (Y), with irregularly stranded conductor (B)

### Alternative HV connectors 
Original part number for Nissan Leaf battery is 297A65SH1A but a cheaper alternative for battery HV connector can be found in scrapyards. Renault Zoe or Kangoo Batteries use the same connector as Leaf battery. 297A22581R is the part numbers for both car.

The connector used is an [Aptiv HV RCS 800](https://www.ttieurope.com/content/dam/tti-europe/manufacturers/aptiv/doc/aptiv-hv-rcs-800-automotive-connectors-datasheet-specifications.pdf).

## 3D-printable parts

You can print your own safety cover for the **unused heater port**, a dust protector for the **LV connector** and a fixation ring, even a complete **Service Disconnect Switch** or even your own **HV Connector**. Check out the [3D‐printable parts page](../setup/hardware/list_of_3d_printable_parts.md#nissan-leaf).

## Examples of wiring installs
Here are some examples on how to wire up the high voltage output from the battery, into a fusebox or DC junction box.

![image](../images/nissan-leaf-e-nv200-16.png)
![image](../images/nissan-leaf-e-nv200-17.png)
![cabluri2](../images/nissan-leaf-e-nv200-18.jpg)

Phoenix 3049408 DIN rail connectors
![Phoenix 3049408 DIN rail connectors](../images/nissan-leaf-e-nv200-19.jpg)

## Notes on 30kWh battery
The 2016-2017 30kWh LEAF battery had a software bug in the BMS that caused the amount of kWh reported by the battery to be incorrect, and the state of health % to drop too fast. If you have one of these batteries, and it shows below 50% SOH, your battery might be affected. The Battery-Emulator can perform a degradation reset, and bring the SOH% back to 100%. This can be accessed from the Webserver, via the "More battery info" page. By pressing the "Reset degradation data", the clear is performed. 

Performing this clear can restore a few kWh of usable energy back. 

!!! info "IMPORTANT"
    The degradation reset only works on 2011-2017 batteries. Performing it on 2018+ 40/62kWh packs will have a negative effect, since it will restore the battery data too low. So only perform this reset on ZE0/AZE0 (24/30kWh) packs!

![image](../images/nissan-leaf-e-nv200-20.png)

### Performing the reset in detail
To perform a proper SOH% reset, [that sticks between reboots](https://github.com/dalathegreat/Battery-Emulator/issues/900#issuecomment-3482162856), perform the following steps:

- Open contactors
- Reset battery degradation via the More Battery Info page
- Disconnect CAN cables (also disconnect them from the inverter if they share a single CAN bus)
- Keep BMS power ON, but remove CHG/IGN 12V signal
- Wait 3 minutes
- Reconnect CAN cables
- Restore 12V to GHG/IGN
- Close contactors
- Reboot Battery Emulator

After these steps, the SOH reset to 100% becomes persistent. 

### Set your own, real limits
Note that after you reset the SOH to 100%, the BMS will let charging and discharging the cells likely beyond the limits which are safe to use on long term, in respect to the longevity of the cells. In stationary usage the battery charges and discharges much slower, and in a different pattern than when it used to do in a car, so a SOH recalibration in the BMS will take very long to happen, to match reality. 

You can set up [Home Assistant](../setup/software/home_assistant.md) which lets you track cell voltages and delta on longer term, to be able to investigate the behavior. 

To see some results, follow these steps after you do the reset (in normal ambient conditions, avoid extreme cold or hot periods):

- Disable [Rescale SOC](../setup/software/webserver_guide.md#rescale-soc) if you have it set
- Let the battery to charge to empty
- Let the battery to charge to full
- Let the battery to charge to empty again
- Watch how the values of **Cell Voltage Delta** and **SOC (real)** change over time as approaching full and empty

For example:
![image](../images/nissan-leaf-e-nv200-25.png){ width="2200" height="1000" }

Try to find the widest time area of **Cell Voltage Delta** where the value changes least - that's the most comfortable and safe "zone" for the cells to operate. Look at the **SOH** graph in the same time period - that should give you the min and the max percentage of SOC rescaling you can set in Battery Emulator, to prevent the battery to go in the high cell voltage delta zone. Take into account the absolute minimum SOC value your inverter is willing to go until (eg. Fronius allows discharging to 5% only, doesn't go below), you can reduce min SOC rescale about by that amount. 

In the example above, the top graph establishes the red lines, which show the comfortable area of **Cell Voltage Delta**. The green lines show where the SOC curve intersects the red lines: this gives the min and the max SOC rescale values for a safe zone. (note the slight hysteresis between charge and discharge, take the highest value for safety).

This way you'll still be in the safe zone with your battery, but you'll likely be able to use bigger capacity than the original SOH allowed in the BMS before reset. Re-evaluate this graph periodically, every 3 months (no need to do full charge-discharge so often, just keep your eye on **Cell Voltage Delta** and **SOC (real)** relation on normal usage)
