---
title: "CAN replay"
---

### What is the CAN replay useful for?

The Battery-Emulator can replay CAN and CAN-FD log files, making it a powerful reverse engineering tool. This feature is useful when working with a new unsupported battery, and makes it easy to replay a vehicle log to for example try to get contactor closing to function. This makes it more accessible especially on the CAN-FD side, where previously you would have to spend lots of money on CAN tools. Now just use the Battery-Emulator hardware!

### How to use the CAN replay feature
Access the feature via the Webserver, and click the "CAN Replay" button.

![image](../../images/can-replay-01.png)

This opens the Replay page. Via this page you can:

- Select which CAN interface to replay towards
- Upload the .txt CANdump log file you want to replay
- Start/Stop/Loop the log

![image](../../images/can-replay-02.png)

!!! info "IMPORTANT"
    The log file needs to be a .txt CANdump format (same format the CAN logging feature uses)

The CANdump format looks like this:

`(28291.286) TX1 1F2 [8] 10 64 00 B0 00 1E 00 8F`

