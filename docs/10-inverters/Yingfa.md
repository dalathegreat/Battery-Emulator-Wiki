# Yingfa inverter wiki page

## Types of compatible Yingfa inverter(s)
* [YF5K-HES-1A](https://a.aliexpress.com/_EvdEBRw)

This inverter works with pylon can. 
It hasbeen tested with the Ferroamp compatible pylon protocol. 
There seem to be no issues as of now. 

## Setting up the Yingfa inverter for a I3 battery
The i3 battery cannot handle the precharge because the capacitance of the inverter is larger than it expects, so a switch with a resistor has to be added.
In my case I have 2 separate circuit breakers one negative and one positive. 
You need to have one of the breakers closed and one open. 
Once you close the contactors you can use a switch with a resistor in series to bypass the open circuit breaker. A 25 Ohm 50 Watt resistor will precharge the capacitor in less than a second. You will notice the screen of the inverter turn on, close the the second breaker before the inverter starts to pull power as it might burn out the resistor!

## Battery
Confirmed working with a I3 battery and a lilygo T-2Can. SOC is properly displayed,  voltage and power limits as well.

#### Special Notes
if you want to connect this inverter to the grid then you HAVE to use the CT sensor, otherwise it will throw a grid fault.

There are 2 pages for the password as it is 8 digits.
11110000
One page is all 1s and after pressing enter a second page will appear with all 0s jist keep pressing enter until you cycle through the second page and the advanced settings will appear.

## Starting and stopping the system
There is a Pause button in the battery emulator web page that will tell the inverter to stop charge/discharging the battery.

### Shutdown
Make sure there is no load on the battery before opening contactors or turning the battery emulator off! 
• Use pause button.
• disconnect the inverter from the battery via mcb.
• remove 12V from battery and battery emulator.

## Day to day monitoring
This inverter uses the solar man App.

## Troubleshooting
If the inverter gets no can signal for that battery it will constantly look for it so you can mess around even for hours and once it sees can data it will start to work so no constant reboots required.

