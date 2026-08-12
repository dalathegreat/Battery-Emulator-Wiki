# Dacia Spring / Renault K-ZE ( CMFA-EV platform )

The Dacia Spring Electric (27.4kWh) / Renault K-ZE (26.8kWh), are both vehicles in the CMFA-EV platform. 

There are also a few Chinese EVs that also share the same CMFA-EV battery platform, all the following models are compatible with the Battery-Emulator integration:

* Dacia Spring Electric (2021–present)
* Renault City K-ZE (2019–present)
* Dongfeng Aeolus EX1 (2019–2021)
* Dongfeng Fengxing T1 (2019–2021)
* Dongfeng Fengguang E1 (2019–2024)
* Dongfeng Nano Box (2022–2024)
* Venucia e30 (2019–2023)

### Note on model year
Some 2024+ batteries seem to not respond to CAN. Investigation ongoing!

2024+ can be identified with an additional "Pressure Sensor" near the HV/LV connector

![image](../images/dacia-spring-renault-k-ze-21.png)

### General info

These batteries have 72 cells in series, which creates an operating voltage of approximately **216 to 302VDC**. Make sure [the inverter](../10-inverters/index.md#supported-inverters-list) you are planning to use is compatible with this voltage range!

![image](../images/dacia-spring-renault-k-ze-01.png)

### Testing the battery
In order to read the informations from the BMS, you need:
- [LiLyGo T-CAN485](https://s.click.aliexpress.com/e/_oDPdyMg) with Battery Emulator installed and configured for this battery and NO inverter.
- 12V source for LilyGo and battery (it can be a Gel battery, UPS, 12V adapter etc)
- Low Voltage battery Connector with those wires connected: 12V, GND, CAN-L and CAN-H (see the [connections](../images/dacia-spring-renault-k-ze-24.png))

### Shopping list
Here is a detailed [shopping list](https://docs.google.com/spreadsheets/d/14ghFL5mUg0hlUOsraOJc9BExlsMp5ClRRITRSQVLfkA/htmlview#gid=1550632359) for this battery implementation.

## Software configuration
For this battery type, use the option called "CMFA platform, 27kWh battery" under the "Battery Protocol" section, NMC chemistry.

![setari](../images/dacia-spring-renault-k-ze-02.jpg)

See [Fronius Gen24 settings](../images/dacia-spring-renault-k-ze-25.jpg)

## Battery module - BMS pin diagram. 
BMS reads from each module the cells voltage + one GND and 2 temp sensors (one for each module). should be ~17Kohm range

![image](../images/dacia-spring-renault-k-ze-22.png)

![image](../images/dacia-spring-renault-k-ze-23.png)

## Wiring diagram, Low Voltage

The battery contains a terminating resistor. 

![image](../images/dacia-spring-renault-k-ze-03.jpg)

The LV connector on the battery has the following pinout:

![image](../images/dacia-spring-renault-k-ze-04.png)

The pin numbering is engraved on the LV connector (PT06A-12-10S)

![image](../images/dacia-spring-renault-k-ze-05.png)

Try to source at least the LV connector; scrapers are happy to cut the cables and usually give them for free.
The LV connector usually goes to scrap with the car.

Get the HV connector too; it makes things look nicer. 
Search for HV cable and connector on [eBay](https://www.ebay.com/sch/i.html?_nkw=297A21306R), part#: 297A21306R

Connect the battery to the Battery-Emulator according to this diagram:

![conexiuni](../images/dacia-spring-renault-k-ze-06.jpg)

![schema_conectare](../images/dacia-spring-renault-k-ze-24.png)

12V power info: The preacharge+contactors consume 1.5A. The BMS itself uses 0.1A

Use a relay board (NO) (5V or 12V) to apply GND to the pins (pin 2AE / 2AD / 2AC all accept a **GND signal** to be toggled on).

See  [4ch SSR on DIN rail **(DC-CN)**](https://s.click.aliexpress.com/e/_olDgyMC)

![4ch SSR on DIN GND](../images/dacia-spring-renault-k-ze-07.jpg)

## Wiring, High voltage
The battery has a service disconnect switch:

![image](../images/dacia-spring-renault-k-ze-08.png)

Note that there are two versions of the service disconnect switch. The 2021 model is different to 2022+. So, if you purchase a service disconnect switch, make sure you get the correct model year!

![image](../images/dacia-spring-renault-k-ze-09.png)

The polarity of the High Voltage outputs can be seen here, Left is **positive**, Right is **negative**.

![Polarity](../images/dacia-spring-renault-k-ze-10.jpg)

## HV Cable preparation
Beware of the the mantle strings (cut them) = not to touch the copper conductor.
The optional [ferrule](https://www.aliexpress.com/item/1005007192861678.html) for the copper conductor is 35smm
![HV cable](../images/dacia-spring-renault-k-ze-11.jpg)

![HV_box](../images/dacia-spring-renault-k-ze-12.jpg)

## Configuring the software
Enable the `CMFA platform, 27 kWh battery` option in the software

Do **NOT** use PWM contactor control.

Spring keeps the HV voltage between 220V (0% SOC) and 296V (100% SOC)
You can adjust SOC min percentage and SOC max percentage from the emulator settings to keep the battery voltage somewhere in the above voltage range. Like -5 / 85 with current build (june 2025).

This battery also benefits from automated 30s daily resets, which can be automated with BMS power output. See the [Periodic Reset page](../40-setup/10-hardware/Periodic-BMS-reset.md) for details.

## Fuse sizing:

For fuse sizing, we use the max inverter power / 218V = max fuse size.
ex, for a 5kW inverter: 5000W / 218V = 23A => use a [25A fuse](https://s.click.aliexpress.com/e/_onOPNy8)

* [Fronius Gen24 6-12kW](../10-inverters/Fronius.md) accepts max 22A on the battery input, so you will be able to draw from this battery 4.7-6.6kW, depending on voltage (SoC)
* [Fronius Gen24 3-5kW](../10-inverters/Fronius.md) accepts max 12.5A on the battery input.

## Completed builds:
1. DIY wooden support, with space for the fuse underneath
![wooden_support](../images/dacia-spring-renault-k-ze-13.jpg)

![2025-06-07-6131-s](../images/dacia-spring-renault-k-ze-14.jpg)

2. Metallic box
![Dacia Spring battery metalic box](../images/dacia-spring-renault-k-ze-15.jpeg)
![PE on the case](../images/dacia-spring-renault-k-ze-16.jpg)

## Note on missing cell voltages
If you are not seeing all 72 cells in the cell monitor page, the fuses on the cell taps might be damaged.
A telltale sign is that some values get corrupted, and the charge current goes to 0. This can be repaired by opening the battery and repairing the damaged traces.

![image](../images/dacia-spring-renault-k-ze-17.png)

## Inside the battery:

1. One 225A main DC fuse
![Dacia Spring battery 225A fuse](../images/dacia-spring-renault-k-ze-18.jpg)

2. One main BMS + 6 slaves BMS
The Master <=> Slaves BMSs seem **not** to be software locked, so you can easily swap the main BMS if it's the same part number (printed on the box).

![Dacia Spring battery BMS](../images/dacia-spring-renault-k-ze-19.jpg)

3. Inside look.
The battery case opens very easily. It has many M7 screws; no glue is used to seal it.
![inside Dacia Spring battery](../images/dacia-spring-renault-k-ze-20.jpeg)
