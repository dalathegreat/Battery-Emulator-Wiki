---
title: "Tesla Model S/X 2012-2020"
---

## Tesla Model S/X 2012-2020 Legacy

The earlier Tesla batteries use a radically different CAN structure compared to the 2021+ S/3/X/Y platform, so we have separate integrations for each platform.

When using a Legacy battery, make sure to select the "Tesla Model S/X 2012-2020" option.

![image](../images/tesla-model-s-x-2012-2020-01.png){ width="517" height="118" }

## High voltage connectors

The BMS expects a capacitance of 940 µF (1000 µF will also work) at the DC bus, otherwise it won't successfully precharge. The HVIL in and out need to be connected with a 180 Ohm resistor in series. The Tesla BMS does isolation measurements, these could interfere with an inverter. 

The Tesla Model S/X is equipped with an HV Rapid Mate connector. When using the original plug, connect terminal 1 to positive and terminal 2 to negative.

The plug also features two pins; the smaller one is responsible for the HVIL continuity. The bigger one should be connected to battery frame. 
From the battery side, the pinout is as follows:

![images](../images/tesla-model-s-x-2012-2020-02.png){ width="298" height="169" }

## Low voltage connectors

Connector X035:

![image](../images/tesla-model-s-x-2012-2020-03.png){ width="451" height="347" }

Connector X036:

![image](../images/tesla-model-s-x-2012-2020-04.png){ width="465" height="360" }

Pinout X035:

* 2 + 5: +12 V (10 A fuse)
* 8 + 12: GND
* 10: HVIL in

Pinout X036:

* 2 + 5: +12 V (10 A fuse)
* 8 + 12: GND
* 9: PT_CAN-
* 10: PT_CAN+
* 11: HVIL out

Digikey links:

* X035: [digikey](https://www.digikey.be/nl/products/detail/molex/0334721201/1756779)
* X036: [digikey](https://www.digikey.be/nl/products/detail/molex/0334721202/3838609)
* 18-20AWG pins (CANbus + HVIL): [digikey](https://www.digikey.be/nl/products/detail/molex/0330122002/2421383)
* 14-16AWG pins (+12 V + GND): [digikey](https://www.digikey.be/nl/products/detail/molex/0330122001/2404852)

## Notes on balancing

Note that the capacity of a pack is limited by the brick with the lowest capacity. When that brick is charging, it will gain voltage faster than other bricks. The HVBMS will stop charge when any brick reaches its ceiling voltage (~4.2V). If one brick has a significantly lower capacity that others, the pack will be limited by that brick which will get to 4.2V faster than the other ones. We refer to the brick with the lowest capacity as: minCAC. 

Another limitation could come from bricks being imbalanced, or some bricks with a voltage higher/lower than others. This would limit ability to charge the pack as the brick with a higher voltage than others would reach the ceiling voltage early. Same idea when discharging, the brick with the lowest voltage would hit the floor voltage early which would cause the HVBMS to open contactors from low power.

To mitigate this imbalance, Batman has some bleed resistor that can be placed and removed in parallel of each brick via a FET relay. Batman can put that resistor across the brick with the highest voltage which would slightly discharge that brick and bring it back to the level of the other bricks. Batman closes a FET which puts that resistor
across the brick. The HVBMS will order Batman to put that bleed resistor across the brick with the highest voltage when Delta V is > 5mv MinBrickV > 4.0v (~85% SOC) && HVBMS State == STAND BY.

Note that Batman can also do balancing when the HVBMS is asleep :).

The best way to balance the Model 3 pack is to set charge limit to 90% or higher and let the vehicle sit idle for hours (plugged in or not). 24 hours of balancing can reduce imbalance by 1mV.

## Examples

The first testing of a 85kWh battery with a Deye inverter

![](../images/tesla-model-s-x-2012-2020-05.png)
