---
title: "Cellpower"
---

The Battery-Emulator is compatible with Cellpower BMS, used on Intercel CLPL batteries.

## Configuration

!!! info "IMPORTANT"
    The Cellpower BMS runs at 250kbps CAN speed. Due to this it cannot be connected to same CAN bus as solar inverters.

Start by connecting the CAN port of the BMS, to the Native CAN port on the Battery-Emulator.

- If you have a Modbus inverter, connect it to the RS485 port of the Battery-Emulator
- If you have a CAN inverter, you need to connect it to a separate 500kbps CAN channel, since the BMS runs at 250kbps
    - choose an Emulator board which has more CAN channels like [LilyGO T-2CAN](../../hardware/lilygo_t_2can.md), [BECom](../../hardware/becom.md), [Stark CMR](../../hardware/stark_cmr.md) 
    - add a [separate MCP2518 CANFD channel](../../setup/can_related/can_fd_add_on_mcp2518fd.md)

## Software configuration

For this battery type, use the option called "Cellpower BMS" under the "Battery Protocol" setting. Also make sure to configure the interface to Native CAN.

![image](../../images/cellpower-bms-01.png){ width="665" height="350" }

Also remember to configure all battery limits to suite the battery you are using!

