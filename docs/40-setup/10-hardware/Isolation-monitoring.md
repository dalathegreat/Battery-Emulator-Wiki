> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

# What is insulation monitoring?

## Insulation monitoring inside an EV battery
All EVs have some form of insulation monitoring. The vehicle/battery constantly checks the insulation resistance between the HV+ to chassis ground, along with HV- to chassis ground. If a high voltage leak is detected, the vehicle will set a fault code, and if the leak is severe it will halt the operation of the vehicle.

Generally it can be said than EV batteries have to comply to at least 100 Ω per volt for DC, meaning that a 400V battery needs to provide at least 40 kΩ insulation resistance (ISO 6469-3 / UNECE R100). PV inverters / stationary energy storage systems may be stricter, tend to be designed to comply to 1kΩ per volt, thus they offer measurement ranges between 100 kΩ and 1 MΩ. 

> [!TIP]  
> **Why the difference exists**: EV packs are designed to operate inside a vehicle occupants sit in (they don't contact with ground), so the 100 Ω/V rule is tuned to the "worst case single fault while a person is present" scenario - automotive points of view. PV/home energy storage installations are stationary, often outdoors, and the people at risk are typically installers/technicians during maintenance — these standards are imposing stricter values with regards to the conditions.

See [this excellent Youtube video](https://www.youtube.com/watch?v=00eEj_EgMas) explaining insulation resistance on EV side. 

## Insulation monitoring on solar inverter side
All solar inverters perform insulation monitoring. The inverter keeps track of PV panel strings, and if these leak high voltage DC to protective earth, error codes are set. The solar inverter also keeps track of HV Battery, and if either HV+ or HV- is leaking towards protective earth, error codes are set and operation might be halted.

## Insulation monitoring in hybrid inverters
Hybrid inverters usually have two different types of insulation monitoring:

1. Active pre-check insulation monitoring

   Before the inverter connects the battery to the grid, it checks for leakage between the HV terminals and the grounded battery case, by creating a known-impedance current path from one terminal to ground and measuring the effect on the other, and repeating for the other terminal. If no leakage is detected, the inverter will allow the startup to continue.

2. Passive residual-current monitoring

   Once the inverter is in use, the inverter checks for leakage by measuring the 'residual current' (the difference between the currents in both battery terminals), to detect if any current is leaking to ground.

## How inverters affect the battery insulation monitoring
Most hybrid inverters are 'transformerless', meaning they do not have galvanic insulation between the battery HV connections and the grid live/neutral. When an EV battery is connected and in use, a current path is created from the HV connections, through the inverter to grid neutral, through the neutral-PE tie, and back through PE to the battery case. This appears to the battery as a low (and very noisy) insulation resistance.

This is readily detected by the battery as an insulation failure. Despite this, most EV batteries will still allow the contactors to remain closed:

- Some batteries only perform insulation measurement at start up, before the inverter has connected, and don't check again.

- Some batteries see the insulation failure, but allow the battery to continue to be used (so the driver can safely get off the highway).

- Some batteries have more sophisticated insulation monitoring using DSP that can distinguish between the transformerless inverter leakage and a real insulation fault.

## How batteries affect the inverter insulation monitoring

EV batteries do not normally cause problems with the inverter's insulation monitoring. The battery's test currents are usually low enough to not be detected as leakage by the inverter, although an exceptionally sensitive inverter might still detect them.

Some batteries do have Y-capacitors between the HV terminals and ground, for interference suppression (and sometimes also as part of the insulation measurement circuit). These will leak some AC to ground, which may cause a leakage current high enough for the inverter to detect (or even to trip an RCD, if the capacitors are large enough).

## Battery/inverter compatibility
In stationary use, insulation resistance cam be a key early indicator of the battery pack health (moisture ingress, degrading waterproofing). For several supported battery types it is visible in the More Battery Info page, but that's just the momentary value, which is completely irrelevant in the majority of the cases. Being exposed over MQTT integration allowing long-term trending, dashboards and alerting in various third patry systems.

> [!NOTE]  
> Whenever the inverter does insulation measurement the value reported by the battery dips low. How often this is done depends on the inverter type. Usually it correlates with the tests imposed by the PV inputs of the inverter. This will influence the insulation resistance seen by the battery, which is passed to Battery Emulator. Evaluation of the insulation resistance needs to be done on long term, not by finding unique outlier peaks!

For critical failure prevention it's enough to rely on the inverter, plus the earth bonding which grounds the battery case, ensuring safety and detecting any true insulation failures.

It is hard to be sure whether a given battery/inverter combination will have problems with insulation monitoring, without testing it, as there are many variables - the type of insulation testing each uses, the current thresholds that cause trips, the timing of when these tests are performed, and the response if insulation failures are detected.

If the battery or inverter detects an insulation failure and decides to open the contactors under load, this is bad as it will damage contactors.

### Contactor opening issues
Telltale signs of an issue might be that the battery runs fine for a few seconds/minutes, but then instantly opens contactors. This has been noticed on many EV platforms, for instance the Stellantis ECMP is notorious for opening contactors if battery detects leakage.

To get around this issue, users have experimented with disabling the insulation monitoring on the battery side, either via software mod or hardware mod.

#### Disabling insulation monitoring via software
It is very rare to be able to do this, but for instance on the "Stellantis CMP Smart" platform, we are able to via CAN command the battery to not perform any type of insulation testing. This avoids any issues when using the battery in stationary storage mode. No other EV platform has been cracked as well as this one!

#### Disabling insulation monitoring via hardware
Another way to get around this issue is to break the battery BMS way of performing insulation monitoring. This can involve isolating the BMS from the ground plane, clever connection of PE wiring, using galvanically isolated CAN wiring setups etc. See each batteries Wiki page for more info on any potential workarounds needed. [Example of ECMP platform, disabling insulation check via HW mod](../../20-battery/Stellantis-eCMP-(Citroen,-DS,-Opel,-Peugeot).md#disabling-isolation-monitoring-via-hw-modification)