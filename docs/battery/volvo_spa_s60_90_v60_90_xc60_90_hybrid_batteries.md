---
title: "Volvo SPA (S60 90 V60 90 XC60 90)"
---

# Volvo SPA S60 90 V60 90 XC60 90 Hybrid 

Battery list with part numbers up to MY2022. This is the list of Volvo supported batteries not the list of BE supported batteries. For the moment none of those are supported.

So everything before MY2022 is assumed to be 96 cells batteries with capacity 10-12kWh (30-34 Ah) and then some break from MY2022 and beyond with 102 cells batteries with capacity 18.83kWh (51 Ah). Not sure if the way older 27 Ah are representative (mostly for older XC90)

![WhatsApp_Image_2025-01-21_at_14 33 28](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-01.jpeg)

Testing is ongoing with the 18.83kWh (51 Ah) battery with serial number 32336936 and it's assumed that the other batteries of the same capacity should behave the same way. Some of the CAN communication is shared with full electric Volvo SPA platform but not all.

!!! warning "CAUTION"
    If you want to use Battery-Emulator to read info, check cells, on a standalone battery before buying, comment out any sending of 0x140 messages in the VOLVO-SPA-BATTERY.cpp file and build a custom .bin file with this mod. Otherwise it will try to close contactors, and without the DC/DC converter it will permanently lock the contactors as welded. See further down for more info on DC/DC requirement.

## Software configuration

For this battery type, use the option called "Volvo PHEV battery" under the "Battery Protocol" setting.

![image](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-06.png){ width="592" height="73" }

## Battery specifications
The following SPA platform batteries are supported, checkbox on those confirmed by users to work.

* Volvo hybrid SPA 2017-2022
   * 7.26 kWh (usable), 10.37 kWh (gross)
   * 8.23 kWh (usable), 11.75 kWh (gross)
* Volvo hybrid SPA 2022-present
   * 14.69 kWh (usable), 18.83 kWh (gross)
       * Volvo P/N 32290825
       * Volvo P/N 32336936

![Battery_location](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-02.png)

## Wiring diagram, low voltage

Connect HVIL_2_IN and HVIL_2_OUT together with a cable. (this will close the HVIL loop in BECM)
Connect HVIL_3_IN and HVIL_3_OUT together with a cable. (this will close the HVIL loop in BECM)
Connect the MSD to close HVIL1. (this will close the HVIL loop in BECM)

The BECM has no built in 120ohm resistor. (BECM = Battery Energy Control Module) 
Make sure the terminating resistors are correct. CAN networks should have two 120 Ohm resistors in each end of the network. With everything OFF, you can measure resistance between CAN-H and CAN-L. The result should be 60 Ohm.

Attached below are pictures of the BECM pinout. Connect the highlighted red pins to the Battery-Emulator hardware and 12V supply like this:

![Connector](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-03.png)

Additionnally you need to mimic the presence of the cooling valve and level sensor. Therefore the experimental approach was to:

* Bridge PIN3 and PIN9 across a safe value resistor (to be determined, DTC removed with 10k resistor)
* Insert a safe value resistor (to be determined, DTC removed with 10k resistor) between PIN8 and your BAT+ 

![LV_receptacle](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-04.jpg)

## Wiring diagram, High voltage :zap: 

!!! warning "CAUTION"
    Battery can lock itself if started without load on HV side!

In order to start the battery you need to have capacitance and current draw ready on HV lines. This can be achieved by connecting a DC-DC converter (which you can purchase from the link below) to the high-voltage output from the front motor. If you skip this step and try to start the battery directly, an irreversible fault code will trigger (Contactor welded). After this fault code is set, you won't be able to engage the contactors via the CAN bus anymore.

Connect the DC/DC converter to the high voltage output lines. Pay attention to the polarity to avoid damaging the DC/DC converter.

The DC/DC converter can also be used to charge a 12V lead acid battery, or left totally unused. The purpose of it is to mainly just enable contactors safely without triggering any fault codes.

![Battery_on_wheels](../images/volvo-spa-s60-90-v60-90-xc60-90-hybrid-batteries-05.jpg)

## Part numbers
Incase your battery is missing some wires/disconnect switches, here are the OEM part numbers and purchase links. Do note that it might be cheaper to source from your local scrapyard!

|  Product |  Purchase Link |
| :--------: | :---------: |
| Service disconnect switch for 18.83kWh battery |  Volvo P/N 32299597   |
| Low voltage connector (naked) |  TE CONNECTIVITY 1-1563759-1   |
| Low voltage connector pins |  TE CONNECTIVITY 1418884-3   |
| Low voltage connector wire seal |  TE CONNECTIVITY 964971-1   |
| DC-DC converter |  [Aliexpress](https://a.aliexpress.com/_EvAwmxw)   |

## How to compile the software for this battery type
Integration under testing/development

