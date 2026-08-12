# Home Assistant goodies

> [!TIP]
> In the examples below, replace the dummy hostname `battery-emulator-a1b2` with the hostname of your own Battery Emulator device!

## Chart examples

Using the [Plotly Graph Card](https://github.com/dbuezas/lovelace-plotly-graph-card) you can generate much better graphics than Home Assistant's built-in ones.

### 2D cell monitor with balancing info

![image](../../images/home-assistant-01.png){ width="504" height="327" }

Add to your Home Assistant `configuration.yaml` a manual MQTT sensor to read all the cell data of the battery into a single sensor's attributes (and a recorder exclusion to save database from load):

```yaml
mqtt:
  sensor:
    - name: "Battery Cells"
      unique_id: battery_emulator_a1b2_cells
      state_topic: "battery_emulator_a1b2/spec_data"
      value_template: "{{ value_json.cell_voltages | count }}"
      json_attributes_topic: "battery-emulator-a1b2/spec_data"
      json_attributes_template: "{{ value_json | tojson }}"
      icon: mdi:battery-high

recorder: # add this to prevent HA database to fill with battery cell data of this sensor
  exclude:
    entities:
      - sensor.battery_emulator_a1b2_cells
```

For double and triple battery setups, create separate sensors pointing at `spec_data_2` and `spec_data_3` topics respectively. Restart Home Assistant after adding this config.

In Lovelace, add a custom card for the battery:

```yaml
type: custom:plotly-graph
raw_plotly_config: true
fn: |-
  $ex {
    vars.a     = hass.states["sensor.battery_emulator_a1b2_cells"]?.attributes || {};
    vars.cells = vars.a.cell_voltages || [];
    vars.bal   = vars.a.cell_balancing || [];
    vars.x = vars.cells.map((_, i) => i + 1);
    vars.y = vars.cells;
    vars.colors = vars.cells.map((_, i) => vars.bal[i] === true ? "#BA6834" : "#2f7ed8");
    vars.delta = vars.cells.length
      ? (Math.max(...vars.cells) - Math.min(...vars.cells)) * 1000
      : 0;
    vars.ymin = vars.cells.length ? Math.min(...vars.cells) - 0.010 : 0;
    vars.ymax = vars.cells.length ? Math.max(...vars.cells) + 0.005 : 1;
  }
entities:
  - entity: sensor.battery_emulator_a1b2_cells
    type: bar
    x: $ex vars.x
    "y": $ex vars.y
    marker:
      color: $ex vars.colors
    texttemplate: "%{y:.3f}"
    hovertemplate: $ex "Cell %{x}<br>%{y:.3f} V<br>%{customdata}<extra></extra>"
    customdata: "$ex vars.cells.map((_, i) => vars.bal[i] ? \"balancing/pending\" : \"idle\")"
    refresh_interval: 2
layout:
  height: 300
  xaxis:
    showgrid: false
    zeroline: false
    showticklabels: false
    ticks: false
    nticks: 1
    visible: false
  margin:
    t: 10
    l: 15
    r: 45
    b: 35
  annotations:
    - text: >-
        $ex "Cell Voltage Delta: " + (isNaN(vars.delta) ? "--" :
        vars.delta.toFixed(0)) + "mV"
      xref: paper
      yref: paper
      x: 0.5
      "y": -0.02
      xanchor: center
      yanchor: top
      showarrow: false
      font:
        size: 13
        color: "#9e9e9e"
  yaxis:
    side: right
    range:
      - $ex vars.ymin
      - $ex vars.ymax
config:
  displayModeBar: false
  scrollZoom: false

```

### 3D Cell monitor (in relation with time) for 96 cells

![image](../../images/home-assistant-02.png){ width="606" height="542" }

```yaml
type: custom:plotly-graph
raw_plotly_config: true
hours_to_show: 1d
defaults:
  entity:
    internal: true
    filters:
      - resample: 1m
    fn: |
      $ex {
          vars.data.push(ys);
          vars.xs = xs;
       }
fn: $ex vars.data = []
layout:
  height: 380
  margin:
    t: 0
    l: 0
    r: 40
    b: 0
  scene:
    domain:
      x:
        - 0
        - 1
      "y":
        - 0
        - 1
    xaxis:
      title: Hour of Day
      tickformat: "%H:%M"
    yaxis:
      title: Cells
      tickmode: linear
      dtick: 1
    zaxis:
      title: V
    camera:
      center:
        x: 0
        "y": 0
        z: -0.1
config:
  displayModeBar: false
entities:
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell1
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell2
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell3
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell4
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell5
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell6
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell7
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell8
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell9
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell10
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell11
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell12
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell13
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell14
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell15
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell16
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell17
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell18
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell19
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell20
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell21
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell22
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell23
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell24
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell25
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell26
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell27
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell28
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell29
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell30
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell31
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell32
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell33
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell34
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell35
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell36
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell37
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell38
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell39
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell40
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell41
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell42
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell43
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell44
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell45
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell46
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell47
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell48
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell49
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell50
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell51
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell52
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell53
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell54
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell55
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell56
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell57
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell58
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell59
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell60
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell61
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell62
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell63
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell64
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell65
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell66
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell67
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell68
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell69
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell70
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell71
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell72
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell73
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell74
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell75
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell76
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell77
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell78
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell79
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell80
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell81
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell82
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell83
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell84
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell85
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell86
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell87
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell88
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell89
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell90
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell91
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell92
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell93
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell94
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell95
  - entity: sensor.battery_emulator_a1b2_battery_voltage_cell96
  - entity: ""
    internal: false
    type: surface
    x: $ex vars.xs
    "y": $ex vars.data.map((_,i)=>i)
    z: $ex vars.data
    colorbar:
      thickness: 7
      len: 0.7
      outlinewidth: 0
      tickfont:
        size: 10
      x: 1
      xpad: 1
      xanchor: left
```

## Pause Charge/Discharge switch (instead of just two buttons)

Create a manually configured template switch which not only will toggle Battery Emulator paused state, but will also reflect this in reality.

```yaml
template:
  - switch:
      - name: Pause Charge/Discharge
        default_entity_id: switch.battery_emulator_a1b2_charge_discharge_paused
        availability: "{{ states('sensor.battery_emulator_a1b2_pause_status') in ['RUNNING', 'RESUMING', 'PAUSED', 'PAUSING'] }}" # Unavailable when the state is unknown or BE is offline
        state: "{{ states('sensor.battery_emulator_a1b2_pause_status') in ['PAUSED', 'PAUSING'] }}" # OFF = running/resuming, ON = paused/pausing — reflects the real state
        icon: mdi:battery-remove
        turn_off:
          - action: mqtt.publish
            data:
              topic: "battery_emulator_a1b2/command/RESUME"
              payload: "PRESS"
        turn_on:
          - action: mqtt.publish
            data:
              topic: "battery_emulator_a1b2/command/PAUSE"
              payload: "PRESS"
```

## [SET_LIMITS](MQTT.md#set_limits) user interface

Use an input number helper to select the **limit timeout**, and create two MQTT number entities to select the desired current limits. Always set the desired timeout first, and change the current values after.

```yaml
input_number:
  - be_limit_timeout:
      name: BE limit timeout
      min: 1
      max: 86400
      step: 1
      icon: mdi:camera-timer
      mode: box
      unit_of_measurement: 's'

mqtt:
  - number:
      - name: "BE charge current limit"
        unique_id: be_charge_current_limit
        command_topic: "battery_emulator_a1b2/command/SET_LIMITS"
        availability_topic: "battery_emulator_a1b2/status"
        payload_available: "online"
        payload_not_available: "offline"
        device:
          identifiers: ["battery_emulator_a1b2"]
        min: 0
        max: 30          # set to your battery/inverter max
        step: 0.5
        unit_of_measurement: "A"
        icon: mdi:battery-arrow-up
        retain: false
        command_template: >-
          {"max_charge": {{ ((value | float(0)) * 10) | round(0) | int }},
           "max_discharge": {{ ((states('number.be_discharge_current_limit') | float(0)) * 10) | round(0) | int }},
           "timeout": {{ states('input_number.be_limit_timeout') | float(30) | int }}}

  - number:
      - name: "BE discharge current limit"
        unique_id: be_discharge_current_limit
        command_topic: "battery_emulator_a1b2/command/SET_LIMITS"
        availability_topic: "battery_emulator_a1b2/status"
        payload_available: "online"
        payload_not_available: "offline"
        device:
          identifiers: ["battery_emulator_a1b2"]
        min: 0
        max: 30
        step: 0.5
        unit_of_measurement: "A"
        icon: mdi:battery-arrow-down
        retain: false
        command_template: >-
          {"max_charge": {{ ((states('number.be_charge_current_limit') | float(0)) * 10) | round(0) | int }},
           "max_discharge": {{ ((value | float(0)) * 10) | round(0) | int }},
           "timeout": {{ states('input_number.be_limit_timeout') | float(30) | int }}}
```