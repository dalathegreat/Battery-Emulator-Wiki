> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## Compatible Hoymiles inverters
- Hoymiles HAT-HV and HYT-HV series, tested with HYT-HV-10.0-EUG1


## Communication wiring
The Hoymiles inverter works via CAN. 

![image](../images/hoymiles-01.png){ width="1039" height="747" }

* Use the BMS RJ45 port on the Hoymiles
    * Pin 4 CAN-H , and Pin 5 CAN-L. With default Ethernet cable color scheme, that's solid blue for CAN-H and blue-white for CAN-L. (See Hoymiles manual for further details)

## Which protocol to use
For this inverter type, use the "Pylon HV" option which is found under the "Inverter Protocol" setting. Also required to enable the "30k offset", and the "Invert byteorder" option. The inverter **will not** see correct data unless you enable these options. 

Hoymiles's battery compatibility list claims compatibility with BYD HVS too, but the protocol doesn't seem to match BE implementation. Pick Pylontech brand as the battery type in the S-Miles Installer app.

Note that Hoymiles inverter talks classic CAN, not CAN-FD, which in the screenshot's just the name of the second CAN port in a Stark CMR.

![image](../images/hoymiles-02.png){ width="788" height="473" }

TODO: Try with the default 'PYLONTECH' manufacturer name

## Automation
There's [a python library](https://github.com/suaveolent/hoymiles-wifi) that allows controlling the inverter via the DTS wifi connection.

## Installation examples
TODO add pic of working setup

## Troubleshooting
Common problems encountered go here