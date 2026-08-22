---
title: "Why add CAN-FD"
---

# Why add CAN-FD
Some batteries use CAN-FD instead of just CAN. Batteries like Kia EV6 are moving towards the faster and more flexible CAN-FD. Most boards, for instance the LilyGo T-CAN485 and T-2CAN, are not compatible with the CAN-FD protocol, but this can be added with an extra MCP2518FD chip via the GPIO pins, similar to the CAN add-on setup.

!!! tip "TIP"
    The CAN-FD chip can also be used for normal CAN. Just enable the "Use CanFD as classic CAN" , and you can use the add-on chip with classic CAN batteries.

### Hardware
The hardware used is an inexpensive chip, "MCP2518FD Pro", which can be purchased [HERE](https://www.aliexpress.com/item/1005006433378885.html)

!!! note "NOTE"
    While the code technically works with MCP2517FD chips, these chips have nasty hardware bugs and should be avoided. Please source MCP2518FD chips instead to ensure proper CAN-FD operation.

### Connecting it to LilyGo T-2CAN
See the [T-2CAN expansion header](../../hardware/lilygo_t_2can.md#expansion-header)

### Connecting it to LilyGo T-CAN485

![lilygo-and-canfd](../../images/can-fd-add-on-mcp2518fd-01.jpg)

    MCP2518FD -> Lilygo
    ___________________
    SCK  -> IO 12
    MOSI -> IO 5
    MISO -> IO 34
    CS   -> IO 18
    INT  -> IO 35
    GND (next to 3V3) -> Any GND pin on LilyGo
    3V3  -> VDD on LilyGo
    GND (next to 5V) -> Any GND pin on LilyGo (+ to GND on external 5V source)
    5V   -> 5V source, can be same as feeds LilyGo via the input pins.

#### Alternative 5V source
The Lilygo also has a 3V3 to 5V boost switch-mode power supply (it is used for the RS485 chip on the Lilygo). It does not have an overly convenient location for connecting, but it can be soldered to one side of C62 (side closest to C64). The Lilygo can then be powered with 12V, which can be more convenient than powering the Lilygo with 5V. See the red wire in the image below. Of course the 5V supply on the Lilygo must be enabled for this to work.

![image](../../images/can-fd-add-on-mcp2518fd-02.png)

#### Alternative hardware
[Another board](https://www.aliexpress.com/item/1005007349452566.html) built around the same "MCP2518FD Pro" chip has been shown to work once the oscillator is configured to `OSC_20MHz` - see details below

![CAN_FD_Lilygo](../../images/can-fd-add-on-mcp2518fd-03.jpg)

The labelling on this board is slightly different:

    MCP2518FD -> Lilygo
    ___________________
    SCK -> IO 12
    SDI -> IO 5
    SDO -> IO 34
    nCS -> IO 18
    INT -> IO 35
    GND (next to 3V3) -> Any GND pin on LilyGo
    3V3 -> VDD on LilyGo
    GND (next to 5V) -> Any GND pin on LilyGo (+ to GND on external 5V source)
    5V -> 5V source, can be same as feeds LilyGo via the input pins.

NB: Only one GND connector is technically required if the same ground is being used for the LilyGo

### Software setup
Then configure the component you want to use CANFD on, by selecting "CAN FD (MCP2518 add-on)" on the component that you intend to connect to the chip.

![image](../../images/can-fd-add-on-mcp2518fd-07.png)

!!! note "NOTE"
    Remember to configure crystal according to your PCB!

Depending on your add-on board, there may be different oscillator crystals. On the "MCP2518FD Pro" board, it is 40MHz, while on some others, it is 20MHz. If you don’t have a 40MHz oscillator, you need to update `CAN-FD-addon crystal (Mhz):` from `40` to `20` in the settings page.

![image](../../images/can-fd-add-on-mcp2518fd-08.png)

Example picture, board with 40.0Mhz crystal:

![image](../../images/can-fd-add-on-mcp2518fd-04.png)

The default settings are 500kbit/s arbitration bit rate, and 2 Mbit/s data bit rate. Incase you have a battery that needs some other bit rate settings, this can be changed in the Software.ino file.

## Testing that the interface works
If you are unsure if the newly added add-on chip works, you can perform the following loopback test. Connect CAN-H and CAN-L to the native CAN channel with two wires, and set up the code to transmit messages via for instance the Schneider V2 protocol. Remember to enable Use CanFD as classic CAN , and also to configure the interfaces as shown below. Once it is all set up, use the [CAN logging page](can_logging.md) to verify that you get incoming RX messages that match the TX.

Test settings, for looping back CAN with Schneider CAN to battery CAN.

![image](../../images/can-fd-add-on-mcp2518fd-09.png)

Example where wires not connected: (Only TX, no RX messages)

![image](../../images/can-fd-add-on-mcp2518fd-05.png)

Example where wires connected (Everything works, TX and RX incoming on native)

![image](../../images/can-fd-add-on-mcp2518fd-06.png)

## Logging CAN-FD messages
It is possible to log CAN messages via USB serial or Webserver, see the [CAN logging page](can_logging.md) for more info.