---
title: "CAN add‐on (MCP2515)"
---

!!! tip "TIP"
    If you're considering using a Lilygo T-CAN485, you may find the [Lilygo T-2CAN](../../hardware/lilygo_t_2can.md) to be a better choice:

    - It has two CAN interfaces already
    - The interfaces are galvanically-isolated, so you don't need separate CAN isolators for troublesome inverters (like Solax)
    - It has a wider input voltage range (up to 24V)
    - Can add-on RS485 if needed, which is simpler than soldering a MCP2515

# Why add another CAN channel?
Some Inverters do not like to see automotive CAN frames on the CAN channel meant for stationary storage. When they see these messages, they enter a fault state. To get around this, we can add an additional MCP2515 chip to the Battery-Emulator hardware, to get an isolated secondary CAN bus.

- Another options is to use [add on CAN-FD MCP2518](can_fd_add_on_mcp2518fd.md) board 
- Another option is to use [Stark CMR board](../../hardware/stark_cmr.md)

## How to add an MCP2515 chip?

The solution is to add a separate CAN channel, via an additional MCP2515. The additional MCP2515 can be connected to the board in multiple ways. The wiring below is given for the LilyGo T-CAN485 as an example, other boards work the same way with their own pin names.

### Option 0: MCP2515 powered via 3.3V (no extra power connections needed)
You can use this MCP2515 board from Seeed Studio - it operates directly on the lilygo 3.3V supply. [seeedstudio](https://www.seeedstudio.com/Seeed-Studio-CAN-Bus-Breakout-Board-for-XIAO-and-QT-Py-p-5702.html)

![image](../../images/can-add-on-mcp2515-01.png)

These pins need to be connected between the LilyGo header and the MCP2515 board: (Warning! the print of the 2x3 connectors on the board itself is WRONG, it's mirrored! Use the added pindescription.)

| Pin on 3.3V MCP2515 board | MCP2515 board comment | Pin on Lilygo |
| - | - | - |
| SCK |SCK input of MCP2515 | IO12 |
| SI | SDI input of MCP2515| IO05 |
| SO | SDO output of MCP2515 | IO34 | 
| CS | CS input of MCP2515 | IO18 | 
| INT | INT output of MCP2515 | IO35 |
| GND | GND input of MCP2515 | GND |
| 3V | GND input of MCP2515 | VDD | 

Note on CAN termination: The board doesn't have a 120 ohm terminating resistor enabled by default. If you want to enable this resistor (which is in most cases when running battery emulator extended can through this board), solder over the p1 pads on the back of the board.

### Option 1: MCP2515 powered via 5V (easiest no-solder method)
(Available here: [aliexpress](https://aliexpress.com/item/1005006646252397.html))

If you want to avoid soldering and just use the MCP2515 module, supply the VCC pin on the MCP2515 module with 5V.

![image](../../images/can-add-on-mcp2515-02.png)

### Option 2: MCP2515 powered via Lilygo VDD pin converted to 5V
(Available here: [aliexpress](https://aliexpress.com/item/1005006646252397.html))

As a 5V pin is not directly available on the Lilygo, it would be ideal if the VDD pin can be used to power the MCP2515 board. This can be achieved in the following manner.

The MCP2515 modules widely available have a 5V only CAN transceiver (TJA1050).
The Lilygo has a 3.3V CAN transceiver (SN65HVD231). The Lilygo also has a level shifter circuit already provisioned on board to use 5V transceivers.
Therefore, it is viable to change the voltage from 3.3V to 5V and solder the 5V CAN transceiver from an MCP2515 module onto the Lilygo board. This requires basic SMD reworking skills.

This solution eliminates the need:

- for an intermediary level shifter board to 5V
- to pick up 5V from a component pad on the Lilygo
- for an external supply of 5V.

After the chip swap is done, another MCP2515 module can be powered from the VDD pin of the Lilygo.

#### Steps for making the Lilygo use a TJA1050 CAN transceiver and supply 5V.
1.  With a hot air soldering gun remove the CAN transceiver (SN65HVD231) from the Lilygo and swap the CAN transceiver from the MCP2515 (TJA1050) onto the Lilygo. An alternative to desoldering the TJA1050 from an MCP2515, is to buy a TJA1050 chip, and solder it to the Lilygo.
2.  Move resistor from RF to RD. Since it is a zero Ohm resistor you can remove the RF resistor and put a blob of solder or wire in RD. This will power the transceiver on the Lilygo with 5V.
⚠️ Do not power up the board before swapping the 3.3V transceiver for the 5V transceiver.

![lilygo-schematic](../../images/can-add-on-mcp2515-03.png)
![lilygo](../../images/can-add-on-mcp2515-04.png)

## Wiring diagram

These pins need to be connected between the LilyGo header and the MCP2515 board:

| Pin on MCP2515 board | MCP2515 board comment | Pin on Lilygo | Lilygo comment |
| - | - | - | - |
| MCP2515_SCK | SCK input of MCP2515 | Pin 12 | |
| MCP2515_MOSI | SDI input of MCP2515 | Pin 5  | |
| MCP2515_MISO | SDO output of MCP2515 | Pin 34 | Pin 34 is input only, without pullup/down resistors |
| MCP2515_CS | CS input of MCP2515 | Pin 18 | |
| MCP2515_INT  | INT output of MCP2515 | Pin 35 | Pin 35 is input only, without pullup/down resistors |
| GND | | Any GND pin on LilyGo | |
| VCC | | Any VDD pin on LilyGo if you performed chip swap. If no chip swapped, this pin needs 5V |

![bild](../../images/can-add-on-mcp2515-05.png)

## ℹ️ Note on crystal
The extra board has either an 8Mhz / 12Mhz or 16Mhz crystal. Be sure to set the correct value in USER_SETTINGS.h if needed. This line:
`#define CRYSTAL_FREQUENCY_MHZ 8  //CAN_ADDON option, what is your MCP2515 add-on boards crystal frequency?` can be changed to suit the crystal located on your board.

![bild](../../images/can-add-on-mcp2515-06.png)

## Software configuration
When using the MCP2515, make sure that the can_config inside USER_SETTINGS.cpp is defined correctly. Be sure to add the CAN_ADDON_MCP2515 to the component that is connected to the add-on-CAN. 

![image](../../images/can-add-on-mcp2515-07.png)

Also make sure the option #define CAN_ADDON is enabled in the USER_SETTINGS.h.

![image](../../images/can-add-on-mcp2515-08.png)

## Troubleshooting steps
If you are having problems with the MCP2515 add-on chip not detecting/sending any CAN messages, check the following:

- Check that you have #define CAN_ADDON enabled, and the interface configured
- Check that you have the correct crystal setting!
- Check that board is fed with 5V
- CAN termination OK? 
   - With everything off, do you have 60 Ohm between CAN-H and CAN-L? If not, add 120 Ohm termination resistors to the ends of the CAN network
   - The MCP2515 board has a jumper (J1) which you can enable to get a 120Ohm termination resistor
- Verify cabling is correct
   - Take a multimeter, and flip the both boards upside down. Then with everything OFF, measure continuity for each pin pad on the bottom between MCP-LilyGo. All pins should have good continuity. If you have high resistance, you might have a corroded pin somewhere.

## Testing that the interface works
If you are unsure if the newly added add-on chip works, you can perform the following loopback test. Connect CAN-H and CAN-L to the native CAN channel with two wires, and set up the code to transmit messages via for instance the SCHNEIDER_CAN protocol. Remember to configure the .inverter CAN channel to CAN_ADDON_MCP2515. Once it is all set up, use the [CAN logging page](can_logging.md) to verify that you get incoming RX messages that match the TX.

## End result
End result, extra CAN channel added:

![bild](../../images/can-add-on-mcp2515-09.png)
