---
title: "Kia Xceed PHEV"
---

## ia Xceed (8.9 kWh) Battery

The Kia Xceed (and Hyundai equivalent) uses a <strong>dual-pack 8.9 kWh high-voltage battery system</strong>, consisting of a <strong>Main Pack</strong> and a <strong>Sub Pack</strong>, each rated at approximately <strong>4.45 kWh at 180V nominal</strong>.</p>

Parameter | Value
-- | --
Total Capacity | 8.9 kWh
Nominal Capacity | 24.7 Ah
Pack Configuration | 2 × packs (Main + Sub)
Capacity per Pack | ~4.45 kWh
Nominal Voltage (combined) | 360V
Nominal Voltage per Pack | ~180V
Operating Voltage Range | 240V – 413V
Cell Configuration | 96S (4 cells × 24 modules)
Cell Type | LiB Pouch (Lithium Ion)
Cell Nominal Voltage | 3.75V
Cell Voltage Range | 2.5V – 4.3V
Max Discharge Power | 59 kW (at 55% SOC)
Max Charge Power | 43 kW (at 55% SOC)
Max Continuous Current | ±250A


⚠️ Pins 19 and 22 are linked as part of the service plug (safety interlock) circuit. Breaking this link disables HV output.

<hr>
<h3>BB12 — BMS Data (12-pin)</h3>
<ul>
<li>Part of the HV harness physically attached to the Main Pack</li>
<li>Carries <strong>BMS data from the Main Pack back to the Sub Pack</strong></li>
<li>Full pinout to be documented</li>
</ul>
<hr>
<h2>High Voltage Circuit Flow</h2>
<pre><code>[Sub Pack]
    │
    │  HV output (always live — breaks only at safety plug)
    ▼
[Main Pack]
    │  Relay assembly
    │  (controlled via BF21 → BF11)
    ▼
[Inverter]
</code></pre>
<hr>
<h2>Photos</h2>
<h3>BF21 Connector (Sub Pack, 24-pin)</h3>
<p markdown="1">![BF21 connector](../images/battery-kia-xceed-phev-01.png)</p>
<p><em>BF21 — 24-pin connector on the Sub Pack. Top row: pins 1–12, bottom row: pins 13–24.</em></p>
<hr>
<h3>Battery Packs — Overview</h3>
<p markdown="1">![Battery packs overview](../images/battery-kia-xceed-phev-02.jpg)</p>
<p><em>Top: Main Pack (black enclosure, underside view). Bottom: Sub Pack (silver/aluminium enclosure) with orange HV interconnect harness and BMS visible.</em></p>
<hr>
<h3>Battery Packs — HV &amp; Signal Connectors</h3>
<p markdown="1">![Battery packs connectors detail](../images/battery-kia-xceed-phev-03.jpg)</p>
<p><em>Detail of the inter-pack connection point showing the orange HV connector (always live), the orange safety plug, and the low-voltage signal harness (BF21/BF11 and BB12).</em></p>
<hr>
<h2>Safety</h2>
<blockquote>
<p>⚠️ <strong>Warning:</strong> The HV connection between the Sub Pack and Main Pack is <strong>always live</strong> when the safety plug is installed. Always remove the safety (service disconnect) plug before working on either pack.</p>
</blockquote>
<hr>
<h2>Notes</h2>
<ul>
<li>BMS data and relay control travel on <strong>separate harnesses/connectors</strong> — do not confuse BB12 (data) with BF21/BF11 (relay control)</li>
<li>The Sub Pack hosts the BMS for the entire system, meaning the Main Pack has no standalone BMS capability</li>
<li>This architecture is shared across the <strong>Kia/Hyundai platform</strong> for this battery generation</li>
</ul>

<p>Here are some useful tools I created. My pack developed a P1B25 fault before finished integration so I have abandoned the project and ordered a different pack.
[Kia 8.9kWh PHEV.zip](https://github.com/user-attachments/files/30602101/Kia.8.9kWh.PHEV.zip) <p>

