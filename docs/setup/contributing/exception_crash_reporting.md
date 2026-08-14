---
title: "Exception Crash reporting"
---

### What is a crash?

![image](../../images/exception-crash-reporting-01.png){ width="435" height="269" }

#### :warning: Warning: The board was reset due to an exception or panic. Inform developers!

If you are seeing this message, it means the embedded code on the board crashed fatally, which resulted in an automatic reboot to be able to resume operation. This is unwanted behavior, and should be investigated by a developer.

### How do I help?
By providing debug logs and reporting a Github issue! This is explained in the steps below.

You can also try to isolate a specific component in the software, for instance try disabling MQTT, or switch some other functionality off. This can help narrow down the component causing the crash.

### Step 1: Gather logs
If you are seeing panic resets frequently, connect the USB cable to a PC, and enable serial monitor in the Arduino IDE, OR, use a terminal program like Putty. Let the log capture all data that the board spits out, and when the Panic reset occurs, store all the text into a .txt file.

:information_source: Remember to set baud rate to 115200 in the right hand side of the monitor, otherwise all text will be garbage =!"=%(=?!

This is what a reboot might look like.

`assert failed: xQueueGenericSend queue.c:872 (pxQueue)`
`Backtrace: 0x40082ce1:0x3ffd12a0 0x4008c611:0x3ffd12c0 0x40091cda:0x3ffd12e0 0x4008c9ff:0x3ffd1410 0x400ed07f:0x3ffd1450 0x400da90e:0x3ffd1490 0x400da847:0x3ffd14e0 0x400d6d58:0x3ffd1500 0x400d6da2:0x3ffd1520 0x400d3779:0x3ffd1540`
`ELF file SHA256: 575c5caf3b3eb57e`
`Rebooting...`

### Step 2: Store what configuration you are running.
Take screenshots of all active settings pages, so the developer can try to reproduce the issue.

### Step 3: Make a Github issue
The final step, is to make a descriptive issue on Github. A new issue can be created via this link: [Make new issue](https://github.com/dalathegreat/Battery-Emulator/issues/new)

Remember to post the settings screenshots, and an overall description on how frequent the panics occur, and if there is any easy way to reproduce it.

Thank you for helping improve the software!

## Advanced users, manually checking backtrace location
First, extract just the addresses (the hex values before the colons):

- 0x40117056
- 0x4037dff1
- 0x40375df2
- 0x420771de
- 0x420772f0
- 0x4207730e
- 0x4037ecc5

Then run each address through addr2line in the terminal:
`~/.platformio/packages/toolchain-xtensa-esp32/bin/xtensa-esp32-elf-addr2line -pfiaC -e "firmware.elf" 0x40117056`

This will output where the issue occurred:

`****0x40117056: transmit_can_frame_to_interface(CAN_frame const*, CAN_Interface) at /home/dala/Git/Battery-Emulator/Software/src/communication/can/comm_can.cpp:279****`

This info can be used to debug from where the crash originated.

