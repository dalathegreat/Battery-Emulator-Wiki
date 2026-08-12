> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

# SEA Platform (Volvo EX30 + others) battery wiki
The Geely SEA platform is [used on the following vehicles](https://en.wikipedia.org/wiki/Sustainable_Experience_Architecture) , batteries that have been successfully tested with Battery-Emulator are marked with a ✅ , feel free to expand this list!

SEA1/PMA1

- Ji Yue 01 (2023–2024)
- Ji Yue 07 (2024)
- Lynk & Co Z10 (E371) (2024–present)
- Polestar 4 (P417) (2023–present)
- Volvo EM90 (2024–present)
- Zeekr 001 (DC1E) (2021–present) ✅
- Zeekr 009 (EF1E) (2022–present)[16]

SEA2/PMA2

- Lynk & Co Z20/02 (E335) (2024–present)
- Smart #1 (2022–present) ✅
- Smart #3 (HC11) (2023–present)
- Volvo EX30 (2023–present) ✅
- Zeekr X (BX1E) (2023–present)

## Volvo EX30 Battery specifications / Serial numbers
The following batteries are available for the EX30
* 55kWh LFP
   * 51kWh net, 120S
   * Nominal voltage 392V, Max voltage 438V
   * 409,5kg, 1569(L) x 1450(W) x 150(H)
* 69kWh NCM Part No: NBE661
   * 66kWh net, 107S , 169AH
   * Nominal voltage 380V, Max voltage 465V
   * 390kg , 1837.6(L) × 1450(W) × 150(H)

## Note on crash lock :boom:
Batteries that have been involved in a severe collision will be crash locked. You can unlock the battery by pressing the "Unlock crashed BMS" button in the More Battery Info weserver page. Remember that the pyrofuse most likely also is blown if the crash status is set.

![image](../images/volvo-ex30-06.png){ width="711" height="179" }

Volvo EX30 batteries can be unlocked this way, but Zeekr SEA based batteries require a more involving security algoritm that is not yet implemented in the software.

## Note on recall :fire: 
If you are planning to use a 69kWh NMC pack from an EX30, be aware that there is a recall on ~3000 vehicles related to risk of battery fires at high SOC. Try to avoid using one of these affected batteries.

Affected VINs seem to all be:
EK = E400V14 '25- EX30 AWD, '26- EX30 Cross Country AWD
EL = E400V18 '25- EX30 RWD

## Pictures

69kWh NCM battery:

![image](../images/volvo-ex30-01.png)

Contactors and fuses:

![image](../images/volvo-ex30-02.png)

BMS inside:

![image](../images/volvo-ex30-03.png)

LV connector:

![image](../images/volvo-ex30-04.png)

|  Pin |   Function   |  Connect |
| :--------: | :---------: | :---------: |
| 1 | KL30 | +12v |
| 4 | Coolant level sensor | 1 kOhm resistor between pin 4 and pin 5 |
| 5 | Coolant level sensor | 1 kOhm resistor between pin 4 and pin 5 |
| 7 | Ground | 12v ground |
| 8 | HVIL 3 In | Connect direct to pin 12 |
| 9 | HVIL 2 In | Connect direct to pin 10 |
| 10 | HVIL 2 Out | Connect direct to pin 9 |
| 12 | HVIL 3 Out | Connect direct to pin 8 |
| 19 | Ground | 12v ground |
| 22 | Fast charge temp sensor | 12 kOhm resistor between pin 22 and pin 29 |
| 24 | Propulsion CAN L | CAN-L |
| 25 | Fast charge temp sensor | 12 kOhm resistor between pin 31 and pin 25 |
| 26 | CPSR | +12v |
| 27 | Propulsion CAN H | CAN-H |
| 29 | Fast charge temp sensor | 12 kOhm resistor between pin 22 and pin 29 |
| 31 | Fast charge temp sensor | 12 kOhm resistor between pin 31 and pin 25 |
| 32 | KL30 | +12v |

* Connect 12v ground to the battery chassis.
* Make sure that the correct (60ohm) termination resistance is present between CAN-H and CAN-L, there is no built in resistor in the battery. (you should most likely add a 120ohm resistor at the battery connector)
* Also make sure to jumper the HVIL loop in the unused high voltage connectors. (make sure to isolate/block the access to the connectors as they will/could have over 400v accessible when the system is running)

![image](../images/volvo-ex30-07.png){ width="320" height="240" }
![image](../images/volvo-ex30-08.png){ width="320" height="240" }



|  Product |  Purchase Link |
| :--------: | :---------: |
| 32pin battery connector |  [AliExpress](https://www.aliexpress.com/item/1005006903919964.html?spm=a2g0s.imconversation.0.0.22843e5fievrj6&algo_pvid=0d3a6b52-d689-48f3-8fee-d9399a21c4b9&algo_exp_id=0d3a6b52-d689-48f3-8fee-d9399a21c4b9-12&pdp_ext_f=%7B%22order%22%3A%22-1%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21SEK%2178.74%2178.74%21%21%2152.50%2152.50%21%40%2112000038668960607%21sea%21SE%21719678987%21X&curPageLogUid=a9Nu2brAcpj0&utparam-url=scene%3Asearch%7Cquery_from%3A&_gl=1*4ksojr*_gcl_aw*R0NMLjE3NDA0MjI0MjYuQ2p3S0NBaUE1ZUM5QmhBdUVpd0EzQ0t3UXFERmxwZmpGQ1lvczV2R3Bndi1QcDAtOXhlS0FaTFNZcm1JOGZvZk0xTjkxa0ZvWWdoMklCb0NtUDRRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3NDA0MjI0MjYuQ2p3S0NBaUE1ZUM5QmhBdUVpd0EzQ0t3UXFERmxwZmpGQ1lvczV2R3Bndi1QcDAtOXhlS0FaTFNZcm1JOGZvZk0xTjkxa0ZvWWdoMklCb0NtUDRRQXZEX0J3RQ..*_gcl_au*OTk0ODQ4NTg2LjE3MzgxODgwMTE.*_ga*NTU2OTE1NDk0LjE3MzgxODgwMDc.*_ga_VED1YSGNC7*MTc0MDQ3OTIzNy42LjEuMTc0MDQ3OTczNy4xOS4wLjA.)   |
| High voltage connector |  ???   |

## Reading DTCs
1. To read the DTCs you have to open another browser tab with the CAN-logger view.
2. Enter filter 1588, press OK. Then press "Stop & Back to main page" (the filter setting will persist), reopen CAN logger and it should be cleared and the filter is active. 
3. Press "More battery info" in the other tab and press read DTC.
4. Refresh the CAN-log and you should have the readout there. (BE performs a bunch of diag requests once a minute that also will end up in the log with that filter, but that is normal)


DTCs are presented with 4 bytes, last byte of each code is status. (Permanent, Intermittent)

Codes might be divided between consecutive CAN frames, but just add them together like marked in the image below.

![DTCs_2](../images/volvo-ex30-05.jpg)


## DTC explanation
- 065868 - Actuator Supply Voltage A Circuit Low
- 0A0A00 - High Voltage System Interlock Circuit
- 0A2900 - Battery Power Off Circuit High
- 0A9500 - High Voltage Fuse A
- 0AA700 - EV Battery Voltage Isolation Sensor Circuit
- 0AA800 - EV Battery Voltage Isolation Sensor Circuit Range/Performance
- 0C7663 - EV Battery System Discharge Time Too Long
- 0CEE00 - EV Electronics Coolant Temperature Sensor Circuit
- 0D1500 - Battery Charging System High Voltage Interlock Circuit/Open
- 0D5C00 - Battery Charger EV Battery Output Power Performance
- 0D9A00 - Battery Charger Coupler Temperature Sensor A Circuit Range/Performance
- 0D9B00 - Battery Charger Coupler Temperature Sensor A Circuit Low
- 0D9C00 - Battery Charger Coupler Temperature Sensor A Circuit High
- 0E0F00 - Generator Inverter Power Supply Circuit/Open
- 0EE900 - Battery Charger Coupler Temperature Sensor B Circuit Low
- 0EEA00 - Battery Charger Coupler Temperature Sensor B Circuit High
- 106800 - EV Battery Pack Coolant Level Low
- 125200 - Lost Communication with Battery Charger Power Converter Module "A"
- 127800 - EV Battery Voltage System Isolation Internal
- 127900 - EV Battery Voltage System Isolation Front electrical machine
- 920600 - Crash Occurred
- 908787 - LIN Bus "A" Bus. Signal / Message Failures. Missing message
- C06488 - CAN Bus Message Failures BECM going Bus off
- C10000 - Lost Communication With Engine Control Module
- C11000 - Lost Communication With Drive Motor Control Module A
- C29200 - Lost Communication With Drive Motor Control Module B
- C29900 - Lost Communication With On Board Charger