---
title: "Fronius"
---

## Types of compatible Fronius inverters

The code works with the following Fronius inverters:

* Fronius Primo Gen24 Plus (all sizes) ✅
* Fronius Symo Gen24 Plus (all sizes) ✅
* Fronius Symo Gen24 Plus SC 12.0 ✅
* Fronius Symo Hybrid 3.0/4.0/5.0-3-S ✅ (ℹ️ Legacy product, no longer available for purchase)
* Fronius Verto Plus (all sizes) ✅

On the date of 23.04.2025 Fronius deployed a firmware update that momentarily broke compatibility with Battery-Emulator. This was fixed and interoperability was restored.

- ROW 1.35.8-1 (Working ✅ ) worked with BE versions **below** 8.11.0
- ROW 1.36.5-1 (Breaks ❌ ) worked with BE versions **above** 8.12.0
- ROW 1.41.11-1 works with the current BE version (as of 2026-08-12).

It is recommended to always use latest software version of both the Fronius inverter and the Battery-Emulator.

![working](../images/fronius_anim.gif)

## Hardware limitation :zap:

* Fronius GEN24 **Symo** inverters (3-5kW) are capped to max 12.5A on the battery port.
* Fronius GEN24 **Symo** inverters (6-10kW) are capped to max 22A on the battery port.
* All Fronius GEN24 **Primo** inverters are capped to max 22A on the battery port.
* All Fronius **Verto** inverters are capped to max 50A on the battery port.

This means that if you have a high voltage battery (450V), you will see much higher charge/discharge speed (22A x 450V = 10kW), compared to a low voltage battery (22A x 250V = 5,5kW)

Keep this amperage limit of 22A/50A in mind when designing a battery system for the Fronius!

!!! note "Software limitation :floppy_disk:"
    There is a non-Plus variant of Gen24 available, for this you have to purchase a battery license before you can add a battery to the configuration. In **System > Information > License** you should see something like below. Contact your installer incase "Battery Operation" feature is missing!

    ![activefeats](../images/fronius-01.png)

    This can also be seen from the label on the inverter, incase "Plus" is missing:

    ![bild](../images/fronius-02.png)

## Setting up the Fronius inverter with Battery Emulator

You will need a technician login to the inverter to make changes to the setup. Contact your solar installer incase you don't have the technician login!

!!! note "NOTE"
    You will also need a Fronius Smartmeter so that the system can measure consumption and generation. The Fronius Smart Meter models "63A-3", "TS 65A-3" and "IP"(wireless) are all compatible. For Home Assistant users: there's an [add-on](https://github.com/M4rt1nCh/ha-fronius-virtual-smart-meter) that creates a Virtual Smartmeter using data from HA entities.

To use a Fronius inverter with a used EV battery, it needs to be setup for battery operation. This is done via the "Solar.start" app or **Device Configuration > Components > Add Component > Battery**, and select **BYD HVS/M (2020-25)**:

![FroniusSetup](../images/fronius-03.png)

After adding the battery, connect the Modbus/RS485 terminals of the Battery-Emulator hardware to the inverter according to this diagram (LilyGo T-CAN485 and LEAF battery example):

![FroniusWiring](../images/fronius-06.png)

When the low voltage communication is handled, also connect the high voltage side (Nissan LEAF battery example):

![HighVoltageWiringFronius](../images/fronius-07.png)

!!! warning "WARNING"
    New hardware requirement for Fronius :warning: Battery voltage is reported towards Fronius inverters only after contactors are engaged. **This means that old legacy installs using manual A/B/C switches for turning on battery contactors will no longer function with Fronius inverters.** Only automatically controlled  contactors via GPIO or CAN will work. This is a new stricter safety requirement to get the Fronius inverter to startup faster and with less errors. 

## Which protocol to use
For this inverter type, use the option called **BYD 11kWh HVM battery over Modbus** under the **Inverter Protocol** setting. Also select the Inverter interface as **Modbus**.

![image](../images/fronius-12.png){ width="490" height="65" }

!!! note "NOTE"
    If you intend to use the [Periodic Reset](../setup/hardware/periodic_bms_reset.md) option with your battery, make sure to enable the "Defer reset if SOC less than 15%" option to avoid charging from grid if you reached the reserved level, and if Battery Emulator would want to do that at night.

### Notes on Scaled SOC + Fronius min/max SOC
In the Fronius settings it is possible to configure "SoC Minimum" and "SoC Maximum" values. If you are using the [Rescale SOC](../setup/software/webserver_guide.md#rescale-soc) functionality in the Battery-Emulator, you will be applying double-rescaling of the usable capacity. It is recommended to always leave in Fronius the "SoC Maximum" to 100%, and adjust the "SOC max percentage" setting in Battery Emulator instead, to be able to take advantage of the "Charge power tapering based on SOC" which avoids power oscillations.

Avoid double-rescaling:

![image](../images/fronius-04.png)

![scaled](../images/fronius-05.png)

Optional setting: If you have multiple AC coupled inverters in your network, and they all reside behind the SmartMeter, you can enable **Battery charging from other sources** and select **from other generators in the home network**.

## Starting and stopping the system

When turning the system on, follow this startup procedure. Work quick, to avoid the inverter getting stuck in battery not detected mode.

### Startup

1. First start the Fronius inverter via AC breaker
2. Turn on the Solar DC switch
3. Turn on the Battery DC switch
4. Power on the EV battery with 12V & and the Battery-Emulator hardware
6. Wait until contactors close at the EV battery (CAN controlled / GPIO control), and Fronius will start to use the battery

### Shutdown

Important to note when shutting down is to not open any DC breakers/isolators under load! Doing so can cause DC arcs and prematurely wear them out, and in worst case start a fire.

1. Signal to the inverter that battery is not available, with any of the following options:
   
       - Press PAUSE in the Webserver (best option)
   
       - Press optional Equipment stop if installed
   
       - Press Open contactors in the Webserver
       
3. Once Fronius stops using battery after a few seconds (verify in app to make sure) it can be powered down
4. Turn off the Fronius inverter via AC breaker
5. Turn off the Fronius inverter via the DC switch on the Fronius itself
6. Turn off the Battery DC isolator switch
7. Turn off the Solar DC isolator switch

## Day to day monitoring

The performance of the system can be tracked with the app "Solar.web". This app gives direct info on current output/input, SOC% level of battery, graphs, and more. No settings can be changed via this app, but it is a great tool for visualizations and quick status checks. You can also see at a glance if an inverter firmware update becomes available for you.

![SolarApp](../images/fronius-08.png)

## Troubleshooting

### Battery not detected

![err2](../images/fronius-09.png)

If you see `No bat­tery de­tec­ted` or `No bat­tery voltage meas­ured but bat­tery is act­ive` in the **Service Messages**:

![err1](../images/fronius-err.png)

Then verify the following:

- Make sure High Voltage is present on inverter battery input. Also make sure the DC isolator switch on the front of the Fronius is turned ON

![image](../images/fronius-10.png)

- Make sure the Precharge/Positive has not been accidentally swapped (Easy mistake on GPIO controlled packs). This will show up as voltage still on inverter pins, but as soon as any load is put on the system the voltage will sag heavily and inverter will report **Battery not detected**.
- If using PWM contactors, make sure they are not dropping voltage momentarily. Try disabling PWM.
- Next step is checking that Modbus connection is active. Check the Events page, if you see this MODBUS_INVERTER_MISSING event;

![image](../images/fronius-11.png)

It means that the Modbus connection is down. Verify that:

- Polarity of M0+ and M0- is correct
- Protective earth is attached in both Inverter and Battery side
- Modbus cable shielding is attached only an one side
- Wires are seated correctly in the Fronius connector. It is very easy to miss that the wires are not pushed in all the way.
- Try a different power supply for the Battery Emulator board. Powering it via USB from a computer can cause noise on the signal output. Powerbank or phone charger might have cleaner voltage output. If you see strange modbus errors, your power supply might be noisy.

Make sure the Battery-Emulator has a good modbus connection to the Inverter.

 - Use shielded wires for a stable connection
 - If you see `ModbusServerRTU.cpp [252] serve: RTU received: E5 - packet length error` in the [logs](../setup/software/webserver_guide.md#log) of the board, it is an indication that wiring is not perfect and occasionally get corrupted

### Invalid battery size detected

![image](../images/fronius-13.png)

If you see this error, it might be because the battery you are using is having higher allowed maxvoltage than the Fronius inverter accepts. A good example is using BYD Atto3 battery (Max 460V), with a Fronius Primo single phase inverter, that only can take 450.

A quick solution is to enable the "450V maxvoltage cap" setting. This fakes it so that all batteries appear as 450V max. 

![image](../images/fronius-14.png){ width="675" height="172" }

!!! danger "NOTE"
    This setting should not be used with Fronius Symo 3-phase inverters. These inverters are designed to work with battery voltages up to 700VDC.

## Advanced control of energy (Spot price, scheduled charge/discharge etc.)
Once you have your battery connected to the Fronius, it is possible to add additional hardware into the mix for advanced control of how energy should flow in the system. This is useful for those with spot-price electricity, or a nightly tariff. Below are some examples you can utilize to control the Fronius Gen24 directly via Modbus TCP.

- You can setup forced nightly charging via the webinterface of the Gen24 (Requires connecting to the inverter directly, not available via SolarWeb). This is very useful if you have a cheap night tariff, and want to charge the battery during the night and use the energy during the day
- [Arska-node](https://github.com/Netgalleria/arska-node/) reads Nordpool electricity prices (from EntsoE/Elering) and renewal energy forecast (solar from Open Meteo, solar/wind from Finnish FMI) as well as local real-time net power consumption/sales (smart meter HAN P1-port -tested in FI, Shelly 3EM). Based on this and time based data (+ optional ds18b20) the system updates variables ([github/Netgalleria](https://github.com/Netgalleria/arska-node/wiki/Channels#variables)) which are used in channel rules deciding whether the channel should be up/down/charging/discharging. Arska has also basic load management functionality (limits loads if consumption exceeds given limits). So far users have used the system mainly to optimise self-consumption of PV production and for scheduling flexible consumption at the cheapest time and selling any surplus when the price is high. Arska has controlled (through GPIO, Shelly and Tasmota relays) water boilers and (underfloor) heating. According to the developer, version 1.3 controls the Fronius GEN24 charging/discharging parameters (nWRte, OutWRte, StorCtl_Mod) based on given channel rules.
- Info on how to [control Fronius Modbus via Homeassistant (German)](https://www.libe.net/byd-modbus)
- [SBAM: Charge Fronius battery using SolCast weather forecast](https://github.com/atbore-phx/sbam/tree/main)
- [This integration](https://github.com/callifo/fronius_modbus) gives you full control over the charge and discharge of the battery.

## Off-Grid/Backup Configuration

Symo/Primo Gen24 inverters that are smaller than 6.0kW are **not** compatible with running full backup mode (the Primo 5.0 is). On these smaller inverters, your best bet is to utilize the PVpoint outlet to get power out of the battery.

A Smart-Meter is mandatory for battery use when connected to a grid (or generator). However, the Gen24 can run 'Off-Grid' if configured specifically for this scenario and limitations. 

To run the Gen24 as off-grid but have the facility to connect to a grid (or generator) at some point, then you must follow the Full-Backup configuration design as documented by Fronius. 

If you intend to never connect the inverter to a grid source (or generator), then you can hard wire the Gen24 in Full-Backup mode. In both cases, the smart-meter **MUST NOT** be detected when running in Full-Backup mode. 

If needed for a future grid or generator power source, the smart-meter can be wired in as per normal ready for a grid or generator input, but the modbus comms (D+) must be disconnected to ensure it does not send data to the Gen24. If the gen24 detects a smart-meter when running in full-backup, then it assumes the grid is connected and will shutdown the inverter and not work reliably.  

To hard wire the Gen24 as off-grid and 'cold-start' using the EV battery pack or PV, I/O pins 6 and 7 need to be jumpered to the V+ on the I/O connector as shown below. 

![Screenshot 2026-05-12 at 12 19 41 pm](../images/fronius-15.png){ width="403" height="478" }

Additionally, Full-Backup mode needs to be configured on the Gen24 as follows:

![image](../images/fronius-16.png){ width="610" height="671" }

Pin0 is not used when hard wiring for full backup. Pin0 is used for automatic switchover to full-backup int the event of a grid failure. Follow the Fronius documentation for this type of configuration. 

The Fronius Gen24 configuration documents describe both automatic and manual switch-over to backup mode using combination of switches and/or relays. Both options can be commercially sourced if you need a non hard-wired off-grid only solution. 

!!! note "NOTE"
    When running as Full-Backup, the inverter will run by default at 53Hz. As such, no other inverter can be active on the AC circuit. Only the Gen24 can be providing power! If you need additional power, then a true Micro-Grid should be used (AC coupling with Victron etc).

!!! warning "IMPORTANT"
    Fronius officially supports a maximum of 2000h off-grid (full-backup) per year on the Gen24. Exceeding this hour count voids the warranty. There are no reports of any inverters shutting down after 2000hours. 

    To get around this off-grid limitation, you can create a microgrid using a 48V battery that powers a small inverter, and then connect the Gen24 to this microgrid. Then it will be essentially offgrid, without incrementing the 2000h max counter. Example of this running successfully has been done with a Victron a 7.2kwh(LV) , and FroniusGen24 with a 75Kwh battery(HV). A smart meter is required if running as a true micro-grid.

All normal earthing requirements when running in 'off-grid' must still be followed. Consult a qualified electrician for advice. 

## Notes on capacity reporting

Fronius is designed to work with 22kWh BYD batteries, and the protocol has a max value of 65535 Wh (unsigned 16bit value) for reporting Wh towards inverter. That means we have to restrict reported Wh number towards the inverter, for example when using a 75kWh Tesla battery, it will show up as max 60kWh in Fronius portal.

Note that this is just a REPORTED value, you can still use the full capacity of the battery. For instance, a 400kWh battery will show up as  60kWh, but the inverter will still use the full 400kWh.

