---
title: "Double Battery"
---

### What is this feature?
Double Battery means running two battery packs at the same time. This doubles the capacity of the system. Incase you need more energy than one EV pack can provide, this functionality is for you.

Good info on running multiple packs and associated risks: [orionbms](https://www.orionbms.com/manuals/pdf/parallel_strings.pdf)

If you need more capacity than Double Battery provides, you can also go [Triple Battery](triple_battery.md)

### How does parallel operation work?
The batteries get connected in parallel. This means the voltage stays the same, but the capacity doubles.

!!! info "IMPORTANT"
    The batteries need to be of the same model and size, and preferably as close as possible in state of health. Do not connect battery packs with too much variation in condition, this lowers overall efficiency significantly!

!!! warning "CAUTION"
    Do not connect packs in series. There are no safeties implemented for operation in series connection!

### Which inverters are supported?
Double-Battery can be run on all inverters. The inverter will think that there is just one large battery attached.

!!! note "NOTE"
    Double-Battery should not be confused with Dual Input inverters. Dual input can have 2 separate batteries operating at the same time (Foxess or Sofar for instance).  lookup how to in your inverter type/brand Wiki for more information about Dual input.

### Which batteries are supported?
Double battery support is only available for highly stable battery types. The ones with checkmark have been confirmed working well.

- Bolt Ampera
- [BMW i3](../../battery/bmw_i3.md) ✅ (CAN contactors)
- [BYD Atto 3](../../battery/byd_vehicle_atto_3_seal_tang_dolphin_song_and_more.md) ✅ (CAN contactors)
- [Nissan LEAF](../../battery/nissan_leaf_e_nv200.md) ✅ (GPIO contactors built-in)
- [CMFA Platform (Dacia Spring, Renault KZE](../../battery/dacia_spring_renault_k_ze.md) ✅ (GPIO contactors)
- Stellantis CMP Smart Car ✅ (CAN contactors)
- Stellantis ECMP ✅ (CAN contactors)
- [Renault Zoe Gen1](../../battery/renault_zoe_gen1.md) ✅ (GPIO contactors)
- [Renault Zoe Gen2](../../battery/renault_zoe_gen2.md) ✅ (GPIO contactors)
- [Relion LV](../../battery/relion_lv.md) ✅ (GPIO contactors)
- [Kia-Hyundai 39/64 kWh](../../battery/kia_niro_hyundai_kona_64_kwh.md) ✅ (CAN contactors)
- Pylon Battery
- Santa Fe PHEV
- Tesla 2020+ (Testing ongoing in PR) (CAN contactors)
If your batteries are not on this list, get in touch with a developer.

#### CAN communication

:information_source: If your inverter does not support seeing automotive CAN messages and need a separate channel, you need a [CAN-Filter](../can_related/can_filter_hardware.md).

If you are using LilyGo:

* The first battery connects to CAN on the LilyGo. 
* The second battery connects to an add-on MCP2515 chip connected via GPIO. [See this page for more info on how to set up Dual CAN.](../can_related/can_add_on_mcp2515.md)

![image](../../images/double-battery-01.png)

If you are using [Stark CMR](../../hardware/stark_cmr.md):

* The first battery connects to CAN
* The second battery connects to CANFD

![image](../../images/double-battery-02.png)

### High voltage connection diagram
:warning: Dealing with one EV battery pack can be dangerous. Using two batteries increases the risks associated with lithium batteries with 100%. Accidentally connecting together the DC side of two batteries at varying SOC% will cause massive amounts of current to be dumped between the packs. Always use fuses to limit the risk and avoid melting wires.

There are two types of EV battery packs:

- Externally powered contactors 
- CAN activated contactors

Externally powered contactors behave deterministically based on Battery-Emulator status. Contactors get connected directly to GPIO pins on the Battery-Emulator hardware, and the batteries are started up in a controlled manner. The second battery is allowed to join if the voltages are close enough (<3V).

When using batteries with CAN controlled contactors (Tesla/Kia/Hyundai etc.), since CAN control acts on its own by the BMS, it can be very hard to troubleshoot these systems, and figure out why a specific pack is not closing contactors properly, or why it is opening them. 

#### CAN-controlled contactors
Connect the high voltage lines like in this diagram. Remember to place fuses both between the Inverter and packs, and the interconnect between the packs.

![image](../../images/double-battery-03.png){ width="785" height="306" }

After battery 1 is started, the system will automatically close the interconnect contactor for Battery 2 (Cont ext), if it falls within 1.5V of the Battery 1. Note that if you skip the interconnect contactor and rely on only closing via CAN, you need to manually sync up the system first, otherwise you will blow the fuses.

To control the second battery, you need to install an extra contactor in series with it. Secondary battery does not use precharge, thus you can switch both positive and negative at the same time. Consult the appropriate board hardware description for which GPIO pin controls this contactor.

Enable "Double-Battery Contactor control via GPIO:" in the Settings page. When Battery #2 voltage matches Battery #1 the extra relay will engage and combine the two batteries into one large battery.

### Taking Double Battery into use.
Example configuration, Stark CMR + Fronius Gen24 + 2x Nissan LEAF batteries, controlled via GPIO contactors

![image](../../images/double-battery-04.png)

### Example wiring diagram - Stark Box + 2x BMW i3 + Fronius Gen24

![image](../../images/double-battery-05.png)

