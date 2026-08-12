> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.


> [!IMPORTANT]  
> The EGMP battery platform cannot communicate over CAN. It only supports CAN FD!


Pinout on battery
![image](../images/kia-ev6-01.png)
![image](../images/kia-ev6-02.png)

![image](../images/kia-ev6-03.png)
![image](../images/kia-ev6-04.png)
![image](../images/kia-ev6-05.png)




Batterie Data (from Kia/Hyundai Service Manual)
![image](../images/kia-ev6-06.png)

Batterie BMU/CMU Info
![image](../images/kia-ev6-07.png)
![image](../images/kia-ev6-08.png)
![image](../images/kia-ev6-09.png)
![image](../images/kia-ev6-10.png)
![image](../images/kia-ev6-11.png)
<img alt="Zrzut_ekranu_2025-07-16_111425-1" src="../images/kia-ev6-12.png" />
<img alt="Zrzut_ekranu_2025-07-16_111419" src="../images/kia-ev6-13.png" />


Images etc.

Similar wiki: [E-GMP platform](Hyundai-E‐GMP-platform-(58.2-‐-77.4-kWh).md)

***** Below find pin connection required ******
 1,2,12 - 12v / 
 3+14 - shunt / 
 7+8 - resistor / 
 10+11 - can-fd (to MCP board) / 
 13 - 5v / 
 24+25 - shunt / 
 27+28 - resistor / 
 29+30 - resistor / 
 31+32+33 - gnd / 
 
You also need to shunt the 3 interconnect in the 3 HV connectors. You can measure if the shunt is connected correctly with a voltmeter. If closed correctly the shunt should measure 2.5V