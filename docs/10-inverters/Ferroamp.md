> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Compatible Ferroamp inverters
* FerroAmp EnergyHub

## Bill of Material of FerroAmp components
* 1x [FerroAmp EnergyHub](https://ferroamp.com/en/products/energyhub/)
* 1x [FerroAmp DC Distribution](https://support.ferroamp.com/en/support/solutions/articles/47001258010-how-should-i-think-when-choosing-dc-distribution-)
* 1x [FerroAmp Power Case](https://ferroamp.com/wp-content/uploads/2022/05/PD10008_ESS-Power-Case-Installation-Manual_En_A02.pdf)
* 1x or 2x [FerroAmp ESO (Energy Storage Optimizer) Module](https://ferroamp.com/wp-content/uploads/2022/05/ESO-Module_Datasheet_En.pdf), installed inside the Power Case.

## Communication wiring
The Ferroamp inverter works via CAN. The LilyGo board can have both a CAN battery and a CAN inverter connected on the same pins. When the board is used with two CAN devices at the same time that have termination resistors in all ends, the terminating resistor needs to be removed from the board. Please measure CAN termination if you have issues, or before removing the resistor. This is explained in [CAN-troubleshooting](../40-setup/index.md#can-wiring-troubleshooting)

> [!NOTE]  
> While the Ferroamp will work on the same CAN channel as an EV battery, it sometimes can cause "ESO fault code 2 - communication issues". If you are seeing this error, put the inverter on its own dedicated CAN channel.


ℹ️ Always check the termination resistance of the system! That way you know if resistor needs to be removed or not.

ℹ️ Grounding is extremely important. Make sure the battery case is connected to protective earth, and the shield part of the twisted pair CAN is connected to PE also! Failing to do this will result in CAN errors.


![Skarmbild_2024-07-10_211612](../images/ferroamp-01.png)

[PD10008_ESS-Power-Case-Installation-Manual_A02b.pdf](https://github.com/user-attachments/files/16394301/PD10008_ESS-Power-Case-Installation-Manual_A02b.pdf)

## Which protocol to use
For this inverter type, use the option called "Ferroamp Pylon battery over CAN Bus" under the "Inverter Protocol" setting

> [!IMPORTANT]  
> The Pylon protocol is very versatile. By default we emulate a 4x96V Force H2 battery. Not all inverters like this setup, so please adjust the configuration if needed. If 0 is left as default values, the below options will be used

![image](../images/ferroamp-02.png){ width="565" height="273" }

- TOTAL_CELL_AMOUNT 420 // Edit steps of 30, as how much your battery Wh is. 30 = 3552Wh, so 420 = 49728Wh*
- MODULES_IN_SERIES 4
- CELLS_PER_MODULE 30
- VOLTAGE_LEVEL 384
- AH_CAPACITY 37

*If you want Ferroamp support to see our battery in correct way you can't change in 30 steps since the battery that matches EV-packs voltage comes in 4 modules 30x4=120. So to look good to Ferroamp support you can only change in steps of 120.

## Troubleshooting
Experiences with various troubles and solutions.
1) Ensure ESO(s) and EnergyHub are updated to latest firmware. (Call FerroAmp support and confirm!)
2) If you are getting "precharge" or "ESO fault 2 - communication" issues - try separating battery and inverter communication channels using MCP add on chip. Read more here: [CAN add-on (MCP2515)](../40-setup/40-can-related/CAN-add‐on-(MCP2515).md)
3) If you bought a second hand ESO and you're having communications issues - it might be the CAN transciever that has taken a beating. (Seems not too uncommon on Ferroamp ESOs!) Read more here: [Lightning strike](../40-setup/10-hardware/Lightning-strike.md)