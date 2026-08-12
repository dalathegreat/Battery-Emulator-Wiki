> [!CAUTION]
> Working with high voltage is dangerous. Always follow local laws and regulations regarding high voltage work. If you are unsure about the rules in your country, consult a licensed electrician for more information.

## General battery info
The Rivian R1T comes in three different battery sizes. A checkbox means that an user has successfully used this battery.
- Gen1 105 kWh, x kg Lifepo4
- Gen1 135 kWh, x kg Samsung NCM ✅
- Gen1 149 kWh, x kg Samsung NCM
- Gen2 NOT SUPPORTED :x:

> [!WARNING]  
> If the battery pack is sourced from a crashed vehicle, the battery could be permanently locked. That means contactors will not turn on, and values will NOT update via CAN. Right now we have no way of unlocking a crashed battery, it requires assistance from Rivian. If the battery is not crashed, the contactors will turn on when the battery gets CAN data from the Battery-Emulator 

![image](../images/rivian-r1t-01.png)

## Software configuration
For this battery type, use the option called "Rivian R1T large 135kWh battery" under the "Battery Protocol" setting

![image](../images/rivian-r1t-02.png)

## Pinout Low voltage

> [!WARNING]  
> Protective earth is very important. The battery case needs to be grounded, otherwise the BMS can detect missing PE and stop operation

The battery LV connector part number is **PT00051975** , and can be sourced via Ebay. 

- All red wires go to 12V, **which needs to be >13.8V minimum**, so using a lead acid battery that is being charged is recommended, alternatively a lab PSU providing enough amperage and voltage. The battery consumes 1.5A when operating
- All black wires go to GND
- All green/blue twisted pairs are CAN.
   - Battery CAN is unstriped green wire CAN-H, and blue wire CAN-L
   - Failover CAN is white striped green CAN-H and blue CAN-L
   - Platform CAN (this is the one we want!) is yellow striped green CAN-H and blue CAN-L(Connect this to Battery-Emulator)
- Light blue wire DO NOT CONNECT TO ANYTHING
- White whire DO NOT CONNECT TO ANYTHING

![image](../images/rivian-r1t-03.png)

## High voltage connectons
The battery has a large amount of connectors available for tapping into the high voltage system. Some connections only have 3-4mm² wiring (OBC, EAC, DC/DC), others 95mm² internal wiring (FDU, DCFC). Due to this, it is recommended to use the largest connector if possible

One alternative for **lower power connections**: This connector plugs into for instance the DC/DC port It can be sourced via Ebay, Part number **PT00001586-K**, wiring attached to it is fairly long.

![image](../images/rivian-r1t-04.png)

Another alternative for **high power connections**: This connector plugs into the DCFC port and handles 500A peak. It can be found on Ebay by searching for "Rivian Charge port door cable"

![image](../images/rivian-r1t-05.png)

![image](../images/rivian-r1t-06.png)

> [!NOTE]  
> Low power connection handles max 30A, High power connection handles max 500A. Choose wisely according to your inverter need!

## High Voltage Interlock (HVIL)
The battery pack has a few HVIL loops that need to be seated. You can add jumpers on the connectors you are not using, so for instance if you use the DCFC HV connector, attach jumpers on all unused HV ports. Be careful also to isolate the connectors, so nobody accidentally touches them when the pack is in operation.