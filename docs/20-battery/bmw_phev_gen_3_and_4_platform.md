---
title: "BMW Gen3 & 4 PHV Platform - (330e 530e X5-45e)"
---

# BMW Gen3 & 4 PHV Platform - (330e 530e X5-45e)

BMW uses a shared modular platform across various vehicles with a common BMS (SME).

!!! info "IMPORTANT"
    Currently integration needs manual contactor control - We have Gen 3 logs, still looking for Gen4 (~2021+) can-logs from a BMW PHEV vehicle to build contactor control (K-CAN5)

# Pin Assignments at Plug Connector A332*1B

A332*1B is the external low voltage connection. 

| Pin | Type | Description / Signal Type               | Connection / Measuring Information               |
|-----|------|----------------------------------------|-------------------------------------------------|
| 1   | E    | Supply, terminal 30                    | Power distribution box, rear                    |
| 2   | E    | High-voltage interlock loop signal      | Electric-machine electronics                    |
| 3   | E    | Terminal 30c signal                    | Connector, terminal 30C                         |
| 4   | --   | not used                               |                                                 |
| 5   | --   | not used                               |                                                 |
| 6   | --   | not used                               |                                                 |
| 7   | --   | not used                               |                                                 |
| 8   | --   | not used                               |                                                 |
| 9   | --   | not used                               |                                                 |
| 10  | A    | Supply                                 | Refrigerant shutoff valve, high-voltage battery unit |
| 11  | A    | Activation                             | Refrigerant shutoff valve, high-voltage battery unit |
| 12  | M    | Ground                                 | Ground point                                   |
| 13  | E/A  | K-CAN bus signal                       | K-CAN5 bus connection                          |
| 14  | E/A  | K-CAN bus signal                       | K-CAN5 bus connection                          |
| 15  | --   | not used                               |                                                 |
| 16  | --   | not used                               |                                                 |
| 17  | --   | not used                               |                                                 |
| 18  | --   | not used                               |                                                 |
| 19  | --   | not used                               |                                                 |
| 20  | --   | not used                               |                                                 |
| 21  | --   | not used                               |                                                 |
| 22  | --   | not used                               |                                                 |
| 23  | E    | High-voltage interlock loop signal      | High-voltage safety connector                   |
| 24  | --   | not used                               |      
