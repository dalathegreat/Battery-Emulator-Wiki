---
title: "Mitsubishi i-MiEV / Citroen C-Zero / Peugeot Ion"
---

There are 3 OEM battery combinations possible and some DIY aftermarket packs.
The first generation packs have 88 Yuasa LEV50 cells. If the car you are getting the battery from is year 2012 or older, then the chances are high you would get a LEV50 one. You do not want such a battery pack. The cells inside have known high degradation. Also do not age well.
If the pack you are getting is from Citroen C-Zero / Peugeot Ion and have 88 cells inside, its always LEV50.
From the beginning of the year 2013 Mitsubishi changed from Yuasa LEV50 to Yuasa LEV50N. Those cells have modern chemistry and last like other cells on other modern cars. There are no known issues with LEV50N cells. Citroen C-Zero / Peugeot Ion with LEV50N cells build in have from this time always just 80 and not 88 cells inside. That is why the max voltage is smaller on such cars.
In Japan there was a rare third battery. It had LTO cells inside and around 10.5kWh of capacity. The reason why the LTO model got released is because Mitsubishi had to replace the known bad LEV50 batteries on warranty on masses and was loosing money. They was searching for alternative and that is why there was this LTO model that got released. If you get a rare LTO model, it should last the longest. Those LTO cells are known to have nearly no degradation.

The chemistry between the LEV50 and LEV50N changed a bit. Because of that the BMU got a firmware update. This firmware update was send to the Mitsubishi shop on a CD. Sadly there is no copy of this CD anywhere. It would be great if someone could get a copy of this cd and put the ISO online. You can read out the firmware from LEV50 BMU and LEV50N BMU and crossflash it.
A Russian developer from Novosibirsk https://github.com/kolyandex modded the BMU firmware and told that the BMU firmware can be modified. Sadly this was sold as a service and not offered open source. The very few people who got this from him, probably does not know how to read out the BMU firmware and that is why it is still not documented how to mod the BMU firmware.

The DIY battery packs have CATL93Ah NMC cells that replace the trash LEV50 cells. Most people are using a CAN bridge because of the missing knowledge how to modify the BMU firmware.
These days some people get smaller EVE58Ah NMC cells to save some weight. Because of their smaller capacity, most just leave out the CAN bridge and use the original LEV50 BMU firmware with the EVE58Ah NMC cells.

It would make sense to add in the future two BMU firmware dumps. One for the LEV50 and one for the LEV50N cells.

Other cars build around the MiEV technology are the Minicab Miev, the Citroën Berlingo Electric and the Peugeot Partner Electric (from the MiEV time period).

## Word of caution when buying batteries ⚠️ 
!!! info "IMPORTANT"
    The battery out of a triplet does not always contain the required parts needed for safe re-use of the battery. The early battery design (pre 2015), had the Battery Management Unit (BMU) located outside of the battery, under the rear left seat. The BMU tells the individual modules inside the battery when to perform cell balancing, and the BMU also calculates state of charge %, and measures how much energy is going in/out of the battery. So without the BMU, it is very hard to safely reuse the battery for stationary storage as-is.

If you are using a 2015 and below battery with external BMU, try to also source the BMU from the same vehicle to not have to search for one that is either for LEV50 or LEV50N.
The service manual containing also information about the pinouts is available here: http://mmc-manuals.ru/Mitsubishi_i-MiEV/en

## Connection diagram
Here is a connection diagram of a 201#? battery:
![bild](../images/i-miev-czero-ion-01.png)

Connect the following wires:

* C26-10 CAN L - To LilyGo CAN L
* C26-5 CAN H - To LilyGo CAN H
* C22-4 to 12V+ supply
* C22-5 to GND for 12V

Handle precharge/contactors manually or use [GPIO control](../setup/software/contactor_control_via_gpio_pins.md)

* C22-7 Precharge
* C22-3 Positive contactor
* C22-6 Negative contactor

## Software configuration
For this battery type, use the option called "I-Miev / C-Zero / Ion Triplet" under the "Battery Protocol" setting.

![image](../images/i-miev-czero-ion-03.png){ width="641" height="146" }

Also remember to configure the allowed charging power, since we do not read this value via CAN.

## Example installation
From left, Solax X3 hybrid 15d inverter, in the middle LilyGo with dual can solution, on the right on the floor i-miev battery and the grey box contains 12V 4Ah battery relays to drive contactors and mitsubishi BMU (Battery is pre 2016, so external BMU mandatory).

![image](../images/i-miev-czero-ion-02.png)

## Further reading
Checkout this repository for more information on the triplet battery: https://github.com/dadantech/czero-ev-battery

