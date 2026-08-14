---
title: "Volvo SPA (XC40, C40 / Polestar 2)"
---

# Volvo SPA XC40, C40 / Polestar 2

!!! warning "CAUTION"
    Battery can lock itself permanently if started without DC-DC converter on HV side! You have been warned, please read the Wiki carefully!

### Measurements

148x176cm and about 500kg

## Battery specifications

The following SPA platform batteries are supported, checkbox on those confirmed by users to work.

* Volvo XC40 2021-present
   * 64 kWh (usable), 69 kWh (gross) ✅
   * 75 kWh (usable), 78 kWh (gross) ✅
   * 79 kWh (usable), 82 kWh (gross) Extended range ✅
* Polestar 2 2020-present
   * 64 kWh (usable), 69 kWh (gross) Standard range ✅
   * 75 kWh (usable), 78 kWh (gross) Long range ✅
   * 79 kWh (usable), 82 kWh (gross) Long range ✅

![bild](../images/volvo-xc40-polestar-2-01.png)

## Software configuration
For this battery type, use the option called "Volvo / Polestar 69/78kWh SPA battery" under the "Battery Protocol" setting.

![image](../images/volvo-xc40-polestar-2-11.png){ width="592" height="72" }

## Buying tips

Make sure the contactor assembly (Left picture, silver box) is included with the battery. Some places remove it and sell it separately. Without this you wont get contactors,current sensor, precharge, fuses etc., rendering the battery unusable.

![image](../images/volvo-xc40-polestar-2-02.png)

!!! note "NOTE"
    It is OK to buy a battery from an airbag crashed vehicle. It is possible to clear that fault code via the "More Battery Info" page.

!!! warning "CAUTION"
    If you want to use Battery-Emulator to read info, check cells, on a standalone battery before buying, comment out any sending of 0x140 messages in the VOLVO-SPA-BATTERY.cpp file. Otherwise it will try to close contactors, and without the DC/DC converter it will permanently lock the contactors as welded. See further down for more info on DC/DC requirement.

## Wiring diagram, low voltage
Connect HVIL2_EXT_IN and HVIL2_EXT_OUT together with a cable. (this will close the HVIL loop in BECM.)
Dont forget the driveline connector. When using the 4wd it's only for on the connector to the rear axle. If you have a different type it can be multiple connectors. For the wiring diagram see [loopybunny](https://www.loopybunny.co.uk/schematics/MY24_Schematic.pdf)

The BECM has no built in 120ohm resistor. (BECM = Battery Energy Control Module) 
Make sure the terminating resistors are correct. CAN networks should have two 120 Ohm resistors in each end of the network. With everything OFF, you can measure resistance between CAN-H and CAN-L. The result should be 60 Ohm.
You can connect a 120ohm resistor between pin 44 and 45 to terminate the bus in the BECM end.

Attached below are pictures of the BMS pinout. Connect the pins to the Battery-Emulator hardware and 12V supply like this:

* Pin 42 to CAN-H on the board
* Pin 43 to CAN-L on the board
* Pin 44 - 120ohm termination resistor - Pin 45
* Pin 24 & 33 to +12V 
* Pin 47 This wire needs to be connected to the battery casing for isolation measurement
* Pin 48 12v GND (47 and 48 are internally connected)

![bild](../images/volvo-xc40-polestar-2-03.png)
![bild](../images/volvo-xc40-polestar-2-04.png)

To use the CAN contactors on Volvo XC40 and Polestar2, you need to connect the GND from the battery connector (PIN47) to the battery case. This GND is used for insulation monitoring. Without it, the battery will not be able to check the insulation integrity and will not engage contactors.

## Wiring diagram, High voltage :zap: 
Here are the ports that you can use on the battery to get voltage out:
![image](../images/volvo-xc40-polestar-2-05.png)

Positive LH, Negative RH

![image](../images/volvo-xc40-polestar-2-06.png)

Test wires attached:

![image](../images/volvo-xc40-polestar-2-07.png)

!!! warning "CAUTION"
    Battery can lock itself permanently if started without DC-DC converter on HV side!

In order to start the battery you need to have capacitance and current draw ready on HV lines. This can be achieved by connecting a DC-DC converter (which you can purchase from the link below) to the high-voltage output from the front motor. If you skip this step and try to start the battery directly, an irreversible fault code will trigger (Contactor welded). After this fault code is set, you won't be able to engage the contactors via the CAN bus anymore.

Connect the DC/DC converter to the high voltage output lines shown above. Pay attention to the polarity to avoid damaging the DC/DC converter.

The DC/DC converter can also be used to charge a 12V lead acid battery, or left totally unused. The purpose of it is to mainly just enable contactors safely without triggering any fault codes.

DC/DC connected: 

![image](../images/volvo-xc40-polestar-2-08.png)

## Part numbers
Incase your battery is missing some wires/disconnect switches, here are the OEM part numbers and purchase links. Do note that it might be cheaper to source from your local scrapyard!

|  Product |  Purchase Link |
| :--------: | :---------: |
| Service disconnect switch 32324494 |  [Volvoshop](https://www.volvopartswebstore.com/products/volvo/Drive-Motor-Battery-Pack-Disconnect-Switch/17175319/32324494.html?srsltid=AfmBOorBmq44EIa0XG8wFXfUVbIYV8hX9a3dqO7GA3DVw_9dIVlpyGXg)   |
| Low voltage 48pin connector |  [Aliexpress](https://a.aliexpress.com/_ExZIFZS)   |
| Low voltage 48pin connector with cable (take black one) |  [Aliexpress](https://www.aliexpress.com/item/1005004818455812.html?srcSns=sns_Copy&spreadType=socialShare&bizType=ProductDetail&social_params=61005201509&aff_fcid=852b913266dc4024815ddb438eb8b7d6-1740411633747-06052-_EzfBvMG&tt=MG&aff_fsk=_EzfBvMG&aff_platform=default&sk=_EzfBvMG&aff_trace_key=852b913266dc4024815ddb438eb8b7d6-1740411633747-06052-_EzfBvMG&shareId=61005201509&businessType=ProductDetail&platform=AE&terminal_id=84fbcc707632424bb0d05791812b9bdb&afSmartRedirect=y)   |
| DC-DC converter |  [Aliexpress](https://a.aliexpress.com/_EvAwmxw)   |

## Handy tips :bulb: 

### Contactor closing with Deye 30kW, 50kW ,Solis S6-series and Fronius Gen 24.
There is a known issue with Deye inverters, that when starting it up with a Volvo battery that requires DC/DC power present, there is a risk that the Deye will cause an isolation issue that prevents contactor closing.

To solve this, Power off inverter by switching off the grid and PV. After the inverter has shut down, you can power on the battery. After it powers on, and the invertor starts, than power one the grid and PV connection. So basically the battery needs to be the thing that starts the Deye, Solis and Fronius first.

You will also need a robust 12V power supply, as contactors (models from 2024 onward) draw approximately 30–40W.

### Opening the contactor assembly

Use a heat gun to warm up the glued seal between the cover and the bay. Use a lever to open the cover then.
 
![image](../images/volvo-xc40-polestar-2-09.jpeg)

### No CAN comm issue
When 12V power is applied to the battery and the Battery-Emulator hardware, there is occasionally an issue where the CAN bus and the transceiver in the BMS control unit do not "wake up," making communication impossible. So far, I’ve found only one solution to this problem — adding an external MCP2515 module and configuring it for communication with the BMS. In this setup, everything works smoothly and without any issues, ensuring reliable data transmission over the CAN bus.

Another thing to test if issue with comm is to leave pin 24 (+12V) disconnected during the first startup of BECM.

![image](../images/volvo-xc40-polestar-2-10.png)

## Reading DTCs
To read Diagnostic Trouble Codes, go to the More Battery Info page and press Read DTC.

![image](../images/volvo-xc40-polestar-2-12.png){ width="543" height="432" }

## Unlocking a permanently locked BMS

If the BMS is permanently locked, replacing the BMS is the easiest solution.

There is a chance that reflashing the BMS can help, but the success rate is low. Some .hex files available on Discord.

![image](../images/volvo-xc40-polestar-2-13.png)

Miniwiggler v3 dap attached to BMS board via PCI-e from old motherboard to avoid soldering.

![image](../images/volvo-xc40-polestar-2-14.png)

![image](../images/volvo-xc40-polestar-2-15.png){ width="900" height="485" }

![image](../images/volvo-xc40-polestar-2-16.png){ width="621" height="480" }

![image](../images/volvo-xc40-polestar-2-17.png){ width="624" height="475" }

![image](../images/volvo-xc40-polestar-2-18.png){ width="624" height="475" }

Flashing tips;

- External 5V to VREF and GND is required
- If it is toggling "Device has no ID register", thhe supplied current might be too low. You must apply external 5v with around 1A
- If you cannot make connection with memtool, it could be that access is blocked via code, see picture below. password is unknown until now, if blocked like picture then BECM board needs to be swapped
![image](../images/volvo-xc40-polestar-2-19.png){ width="630" height="262" }

