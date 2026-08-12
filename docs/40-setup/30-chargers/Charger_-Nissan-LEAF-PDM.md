> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Supported PDMs 🏅 
There are two different 2013+ LEAF charger (PDM) variants that work with the Battery-Emulator as a charger. One is 3.3kW, and the other is 6.6kW (both are only 1-phase chargers). There is a sticker on the PDM that signals how fast it can charge.
![Nissan_PDM](../../images/charger-nissan-leaf-pdm-01.jpg) ![PDM66](../../images/charger-nissan-leaf-pdm-02.jpg)

The following LEAF PDMs are supported:
- 2011 to 2012 ZE0 ❌  Not supported!
- 2013 to 2017 AZE0 ✅ 
- 2018 to 2024 ZE1 ✅ 

## Low voltage wiring diagram 🗺️ 
The PDM has a 36pin Yazaki connector that handles all low voltage signals.

***!!! BEAWARE !!! pinout mapping change depending on car production year***

![pins](../../images/charger-nissan-leaf-pdm-03.jpg)

### >= 2015 PDM pinout (need to verify that pinout is the same for > 2017 ZE1 models)

![image](../../images/charger-nissan-leaf-pdm-04.png)

- Pin 9 - 12V
- Pin 10 - Ground
- Pin 11 - CAN L on Emulator (parallel to the emulator with the battery)
- Pin 18 - 12V
- Pin 27 - CAN H on Emulator (parallel to the emulator with the battery)
- Pin 29 - Connect to white wire on the Type1 port (For type 2 connect to the green wire - PP)
- Pin 30 - Connect to green wire on the Type1 port (For type 2 connect to the white wire - CP)

here the complete pinout
<img src="../../images/charger-nissan-leaf-pdm-14.png" />


### 2014 PDM Pinout

<img src="../../images/charger-nissan-leaf-pdm-15.png" />


### 2013 PDM Pinout

<img src="../../images/charger-nissan-leaf-pdm-16.png" />

## Type 2 AC wiring
![type_2](../../images/charger-nissan-leaf-pdm-05.jpg) ![type2_socket](../../images/charger-nissan-leaf-pdm-06.jpg) ![type2_wires](../../images/charger-nissan-leaf-pdm-07.jpg)

## High voltage wiring diagram ⚡ 
The PDM has two high voltage connectors, battery and A/C compressor. Both can be used to connect to the battery. If you use the A/C compressor connector, the wires are quite thin so they are not recommended for 6.6kW charging, max 3.3kW

The PDM also has the AC input Type1/Type2 connector that needs to be connected to the charging port. You have to use the actual charging port, so the CP/PP logic is interpreted by the PDM. You cannot wire in AC directly to the connector.

### Cooling the charger 🥵 
The charger will get hot when in use. It has coolant ports for liquid cooling. Running the charger dry will only work for a few minutes, after that it will shut off. So having coolant circulating thru it is mandatory. A good waterpump option is the Nissan LEAF waterpump, or a generic electric circulation pump.
Tesla Model S uses the [same pump](https://s.click.aliexpress.com/e/_oCcqWTy) and it's 50% cheaper.

The inlet is marked in this picture:

![image](../../images/charger-nissan-leaf-pdm-08.png)

Nissan LEAF waterpump pinout:
- Brown pin 1 - 12V
- Yellow/black pin 2 - GND

![image](../../images/charger-nissan-leaf-pdm-09.png) ![Leaf water pump pinout](../../images/charger-nissan-leaf-pdm-10.jpg)


ℹ️ The LEAF waterpump takes 8 seconds to start after supplying power to it.

### Charging 12V battery 🔋 
The PDM will output 12V when running. You can use this to charge a 12V lead acid battery (or supply power to a water pump for cooling!). The 12V circuit can be loaded to 1.5kW max. Connect the positive and negative lead as shown in this picture:

![image](../../images/charger-nissan-leaf-pdm-11.png) ![12v](../../images/charger-nissan-leaf-pdm-12.jpg)

### Software setup 💻 
Compiling the software for LEAF PDM support is done by enabling `NISSANLEAF_CHARGER` option in the `USER_SETTINGS.h` file. After uploading the software to the board, you will have a new view in the webserver. When charging is active you can monitor the power coming from the charger.

![301633922-e3ff4a69-e536-4ff8-b651-d64d06f9a372](../../images/charger-nissan-leaf-pdm-13.png)

### Using the charger 💪 
To charge via the PDM, connect an EVSE to the Type1/2 port. This will activate the PDM, and it will start powertransfer into the battery. You can monitor the process via the webserver.

The EVSE can be powered via grid, or via an emergency generator. Keep in mind the PDM will only use one phase, 3.3kW(16A) or 6.6kW(32A) max. If you use an EVSE with max 8A, for example the LEAF portable wallcharger, it will only consume max 8A (1.8kW).

**Example:** If you use a small, portable gas generator like the Honda EU22i (2.2kW), select 8A on the Type 2 Charger. 
This will signal the PDM to charge with a max of 8A.
The Type 2 charging standard requires a minimum of 6A for charging.

If you have a generator larger than the maximum PDM power rating (e.g., more than 7 kW), set the charger to 32 A.
Schuko outlets support a max of 16A (3.1 kW).

#### Notes from testing:

- After connecting the EVSE connector, you need to go to the BE settings and manually set the final battery voltage and charging current. Then manually start the HV charger. In automatic mode, simply inserting the gun doesn't work.
- BUG: It's impossible to set the current higher than 6A - neither before nor during charging.
- The pause before the contactors activate and charging begins is about 10 seconds - you have to wait.
- The displayed HV voltage - 370V - doesn't correspond to reality. The actual voltage is not displayed.
