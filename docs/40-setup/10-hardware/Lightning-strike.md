## ⚡️ Lightning Strikes and System Protection :cloud_with_lightning: 

> [!CAUTION]
> Lightning strikes near your inverter, battery, or smartmeter can result in costly damage to sensitive equipment. Always power down or disconnect your system when thunderstorms are in the area to minimize the risk of damage!

## How Lightning Strikes Damage Systems

Even lightning strikes that occur a kilometer away can produce electromagnetic surges or ground potential rises of tens of thousands of Volts for very short times, that affect electrical and electronic systems. These indirect effects can cause significant damage, particularly to communication interfaces and sensitive electronic components.

* **CAN Transceivers:** The transceiver chips that handle communication on the CAN bus are especially vulnerable to surge damage, which can result in communication errors or permanent failure. Inverters usually have rugged designs, but automotive BMS were never intended to be tied to the ground this way, so similar protection is often lacking.
* **Modbus Inputs:** Just like CAN transceivers, Modbus communication ports can take damage from surge voltages, leading to miscommunication or failure in the system's data exchange.
* **Signal Wires:** Long runs of signal cables can act as antennas, picking up electromagnetic pulses (EMPs) from nearby lightning strikes, which may induce damaging voltages into the system.
* **Separate PE connections:** Earth points can quickly come to different potentials during thunderstorms. When lightning hits the ground nearby, if PE connection is not common, the interconnected equipment may see tens of thousands of Volts between their grounds for a moment, just enough to instantly damage the components.

## How to troubleshoot a damaged system

If your system has been exposed to a nearby lightning strike, or if it’s showing erratic behavior following a storm, there are a few key steps you can take to diagnose where the damage has occured.
1. Measure CAN Bus Termination Resistance

The CAN bus should have a termination resistance of 120Ω between CAN High and CAN Low wires at each end of the bus. Here's how to check it:

- Step-by-step:
   - Power down your system completely.
   - Use a multimeter to measure the resistance between the CAN High (H) and CAN Low (L) wires.
   - The expected reading should be close to 60Ω if both terminators are present (120Ω in parallel). If you get a significantly different reading, check the terminations or for potential damage along the bus.
   - Disconnect each device, and if they contain a termination resistor, it should read 120Ω when measuring.

> [!TIP]
> Not all CAN devices contain a terminating resistor. So be sure to confirm this before stating it broken

2. Inspect CAN Transceivers

CAN transceivers are often the first to fail due to surges caused by lightning. Look for:

- Visual signs of damage: Burn marks, melted or deformed chips, or any discoloration around the transceiver circuits, especially on both the battery BMS and emulator boards.
- Symptoms of damage:
   - Loss of communication between components.
   - Faulty or dropped messages on the CAN bus.
   - Random or erratic behavior of devices connected to the CAN network.

If you suspect damage, you may need to replace the transceiver ICs or even the entire BMS.

Below is an example of a damaged CAN transceiver, caused by direct lightning strike to equipment.
![image](../../images/lightning-strike-01.png)


3. Check Modbus Communication Ports

- Inspect the Modbus connections and ports for any visible signs of damage, like burn marks or scorched connectors.
- Check if you have an event on the Battery-Emulator for INVERTER_MISSING_ON_MODBUS. If you see this, you might have a burned modbus chip somewhere.

4. Inspect power supplies and Protective Earth grounding

Lightning strikes can also affect the power supply used by the Battery-Emulator, so check the voltage regulation and grounding of your system. You can also try to use another power supply for the Battery-Emulator, a phone charger usually works great. 

Bad protective earth grounding or improper surge protection increases the vulnerability of your equipment to electrical surges.

## Preventative Measures

While it’s impossible to completely eliminate the risk of lightning damage, you can take steps to protect your system from electrical surges:

1. Disconnect During Storms: When thunderstorms are imminent, power down the solar inverter, battery, and unplug communication wires.
2. Proper PE Grounding: Ensure that all components are properly grounded, and that there is a solid, **common** PE (earth) connection to divert surges safely away from sensitive equipment. Both Inverter, Battery and communication wire shield should have a good connection to PE. If there's a big distance between the elements of the installation, you can use local PE rods, but you also have to connect them together with strong wire to ensure that PE potential differences cannot develop between them when lightning of a thunderstorm hits the ground nearby.
3. Opto-coupler circuits. You can fit CAN opto couplers to the system to get an air-gap between the components. If you have components you have used successfully for this, feel free to add info to this wiki!

### Suggested hardware
Below are some products you can use to increase the resilience of your CAN/RS485 network

|  Product |  Purchase Link |
| :--------: | :---------: |
| CAN BUS Isolator/Repeater DIN mounted |  [Ebay](https://www.ebay.co.uk/itm/175524303800)   |
| RS485 repeater |  [Aliexpress](https://www.aliexpress.com/item/1005006063614713.html)   |
| PHOENIX CONTACT CAN Repeater IXXAT |  [Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2332490.m570.l1313&_nkw=PHOENIX+CONTACT+CAN+Repeater+IXXAT&_sacat=0)   |
| Phoenix contact  PSI-REP-DNET CAN - Repeater | [Datasheet](https://www.phoenixcontact.com/en-pc/products/repeater-psi-rep-dnet-can-2313423)

Example of CAN isolator in use, and PE connections between elements:

<img width="1350" height="787" alt="image" src="../../images/lightning-strike-02.png" />


