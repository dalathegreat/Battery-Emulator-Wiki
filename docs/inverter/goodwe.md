---
title: "GoodWe"
---

## Compatible Goodwe inverters

* ET/BT ✅ 
* ET G2  ✅ 
* EH/BH ✅ 
* EH-Plus ✅ 
* EHB ✅ 
* A-ES ✅ 
* A-BP ✅ 

Note: Some Goodwe inverters require an activation code that must be purchased to enable battery mode. Activation code is expensive!

There are probably more compatible GoodWe inverters, feel free to add confirmed working ones to the list!

!!! info "IMPORTANT"
    The software version "ARM No. 17(449)" is currently preventing battery use. It is recommended to not update GoodWe inverters until we find out why this is. Contact Goodwe support to assist with rollback.

!!! warning "WARNING"
    An important point is to be prepared for potential issues if you have an RCD (residual current device) on the inverter's AC side while also using solar panels. In this case, you may need to replace the RCD with the 300mA version recommended in the manual, as a 30mA version might trip during the inverter's self-check process.

## Note on double battery ports
Some Goodwe inverters have dual battery ports. You can connect two independant Battery-Emulator systems to the same inverter this way. Check the operating manual of your Goodwe inverter for more info.

![image](../images/goodwe-01.png)

## Communication wiring
The GoodWe inverter works via CAN. The Battery-Emulator board can have both a CAN battery and a CAN inverter connected on the same pins.

ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important for GoodWe inverters. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.

## Installation instructions
Good idea to watch the installation video from GoodWe's training services, on how to install a BYD battery: [youtube](https://www.youtube.com/watch?v=RLzMI-2JOB0)

1. Follow the GoodWe inverter installation manual up to the point when you plug the comms and battery connector terminals in
2. Unsolder (If needed!) the canbus terminating resistor on the board (as per above)
3. Connect both the inverter canbus and battery canbus to the board
4. Double check your code to make sure the contactors will isolate under the required fault conditions
5. Plug in the battery connector (make sure the terminals are not live)
6. Double double check all your wiring.
7. Switch your battery breaker on
8. Enable the contactors and the inverter will configure and connect if all has gone well.
9. Configure the inverter with the battery connected
10. Use app Solar Go to connect to inverter via Bluetooth
11. Go to quick settings (password: goodwe2010)
12. Select battery. Hopefully it recognizes battery without any user intervention. (HVM*2 works if using both battery inputs from same battery).

![image](../images/goodwe-04.png){ width="448" height="909" }

13. Suggest setting power limit (ampere limit) in Battery-Emulator Webserver at this point, if not already done. Take something low (5A?) until you feel confident the system works as intended.
13. Set charging schedule. (app is very buggy here!)

![afbeelding_2023-11-25_153042647](../images/goodwe-02.png)

## Starting and stopping the system
When turning the system on, follow this startup procedure. Work quick, to avoid the inverter getting stuck in battery not detected mode.

### Startup

1. First start the GoodWe inverter via AC switch
2. Turn ON the Solar DC safety disconnect switch
3. Turn ON the Battery DC safety disconnect switch
5. Start the Battery-Emulator hardware
4. Start the Battery BMS
6. Then either handle precharge/contactor closing manually or let the Battery-Emulator hardware handle it automatically

### Shutdown

1. If relevant; set power limit (ampere) for charge and discharge to 0 in Battery-Emulator Webserver.
2. Turn off the Battery BMS, cut the 12V supply to it.
3. Wait 60 seconds
4. Battery-Emulator status LED will turn red when no battery detected. The inverter will stop using the battery.
5. Wait 30 seconds.
5. Turn off the power to battery contactors incase the Battery-Emulator isn't setup to automatically open them
6. Turn off the Battery-Emulator board
7. Turn off the Battery DC safety disconnect switch

## Which protocol to use

For this inverter type, use the option called "BYD Battery-Box Premium HVS over CAN Bus" under the "Inverter Protocol" setting.

![GoodWe Settings](../images/goodwe-03.jpg)

## Troubleshooting tips 

|  Problem |  Possible fix |
| :--------: | :---------: |
| Inverter app showing "Battery Communication Failure" | Check that high voltage is present on inverter terminals, and that polarity is right way. Check that CAN communication is up via the CAN logging webserver page. |
| Battery not detected in SolarGo App | Update inverter firmware to latest version |
| Inverter not using battery | Make sure the Maximum Charging Current and Maximum Discharging Current is set under the Goodwe App, Parameter Setting page. Sometimes these can be cleared incorrectly after a firmware update |
| No CAN comm with inverter | Make sure the software on the inverter is not too new. One user reported "After upgrade ARM No. 17(449) and restart communication with BE is abnormal". Another user reported "I have GW25K-ET operating smoothly with firmware version 111117 since October 2025. I intentionally refrained from updating since Octber 2025". It is recommended to downgrade inverter firmware incase you have CAN issues and not able to use battery  |

## Reading values from the inverter
There is an excellent repository [available here](https://github.com/marcelblijleven/goodwe) for sniffing data from Goodwe inverters on the network.

# Controlling the inverter via Home Assistant

There is a HACS integration for Home Assistant that lets you control the operation mode of the inverter. It's called [GoodWe solar inverter for Home Assistant (experimental)](https://github.com/mletenay/home-assistant-goodwe-inverter).

The documentation for the integration is quite sparse and the terminology differs a bit from the [SolarGo app](https://en.goodwe.com/Ftp/EN/Downloads/User%20Manual/GW_SolarGo_User%20Manual-EN.pdf). 

There is a [Discord server for the integration](https://discord.gg/TaXyWXT).

Some screenshots from the integration:

![GoodWeConfigurationPane](../images/goodwe-05.png){ width="541" }
![GoodWeControlsPane](../images/goodwe-06.png){ width="541" }

## Controls

This is an attempt to explain what the different exposed values mean, written by a member of Dala's Discord and slightly edited:

### Controls

- **Fast Charging Power** tells the system how much percentage of the configured max charging amps are being used (100% of 10A for example)
- **Fast Charging SoC** tells the system till what percentage the battery should be charged (80% for example)
- **Fast Charging Switch** tells the inverter to charge the battery, this overrides any other setting/mode (like eco discharge mode)

### Configuration

- **Depth of discharge (on-grid)**, this is the percentage of discharge when the mode is set to Eco discharge mode or General mode, 80% will discharge the battery till 20%, 95% will discharge it to 5% etc.
- **Eco mode power** tells the system what percentage of power is used for charging/discharging. 50% will be 5A if 10A is the max charge/discharge etc.
- **Eco mode SoC** tells the inverter till what percentage the battery should be charged in Eco (Eco charge mode). 80% to save battery life or 100% if you already use scaled SoC in Battery Emulator.
- **Grid Export limit** This tells the system maximum watt output to grid.
- **Grid export limit switch** enables this value.

## Examples

These examples assume the **Depth of discharge (on-grid)** is set to a high value. There are other ways to control the inverter, in the [Discord server](https://discord.gg/TaXyWXT) it seems to be more common to use the **Fast Charging Switch** to force charge. 

### Force charge example

- Set **Eco mode SoC** to 100%, or a lower value if you don't wish to fill the battery.
- Set **Eco mode power** to a value that suits your setup and fuses, in this case it's set to 30%. 
- Switch operation mode to **eco_charge**
- Wait 10 seconds and then switch the operation mode to **eco_charge** again, occasionally it doesn't stick the first time.

![EcoModeSoC100](../images/goodwe-07.png){ width="540" }
![EcoModePower30](../images/goodwe-08.png){ width="543" }
![EcoCharge](../images/goodwe-09.png){ width="544" }
![Delay](../images/goodwe-10.png){ width="552" }

### Force discharge example

- Set **Eco mode SoC** to 20% indicating you don't wish to discharge below 20%, change this to a value that suits your setup.
- Set **Eco mode power** to 50% of your maximum energy output from the battery and inverter. Change this value depending on your main fuses or perhaps output 100% and set **Grid Export limit** to max allowed output to the grid if you have the smart meter installed.
- Switch operation mode to **eco_discharge**
- Wait 10 seconds and then switch the operation mode to **eco_discharge** again, occasionally it doesn't stick the first time.
