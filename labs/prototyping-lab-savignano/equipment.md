# Prototyping Lab Savignano — Instrument inventory

**Site:** `LAB-SAV` (domestic prototyping lab; street address intentionally omitted)  
**Revision:** 0.1 — 2026-11-03  
**Verification mode:** operator report and linked product references; no physical verification performed.

| Asset ID | Equipment | Model | Availability | Evidence |
| --- | --- | --- | --- | --- |
| `LAB-SAV-PSU-001` | Variable DC power supply | **Jesverty SPS-3010M** | Owned / reported | Operator purchase screenshots + Amazon ASIN match |
| `LAB-SAV-CHG-001` | Robot battery charger | Unknown | Owned / reported | Operator report |
| `LAB-SAV-DMM-001` | Digital multimeter (budget) | Unknown | Owned / reported | Operator report |

## LAB-SAV-PSU-001 — Jesverty SPS-3010M

| Field | Value / status |
| --- | --- |
| Manufacturer | Jesverty |
| Model | **SPS-3010M** |
| Amazon product ID (ASIN) | `B0CZ92WTQ3` |
| Identification evidence | Matching model & variant in operator's Amazon product page and purchase history; independent matching ASIN/product model listings |
| DC output (nominal) | **0–30 V, 0–10 A** as shown on the purchased Italian listing; some published references say **0–32 V** — verify on physical unit/manual before treating range as authoritative |
| Power envelope | **300 W nominal** (= 30 V × 10 A); sustained delivery and transients have **not** been characterized |
| Control | Encoder for voltage/current adjustment; separate output ON/OFF |
| Operating modes | CV (constant voltage) / CC (constant current) |
| Published protection features | Overcurrent protection (OCP), overvoltage protection (OVP); must be functionally validated for planned tests |
| Extra ports | USB-A + USB-C fast charging; advertised **20 W** charging feature (not an additional calibrated lab supply) |
| Other marketed features | 4-digit LED display; optional output-on-at-startup behavior (OPN); temperature-controlled fan |
| Status | **OPERATOR_REPORTED** as owned; model matched to product listing, **not PHYSICALLY_VERIFIED** |
| Open checks | Physical label/range; ground/negative relationship; output accuracy/ripple and behavior at 24 V load; output protection response; regenerative-current tolerance; supplied lead rating |

**References:**

- [Exact Amazon listing supplied by operator](https://www.amazon.it/dp/B0CZ92WTQ3) (product ASIN, *not* an order receipt).
- [Manufacturer SPS-M product series and manual pointer](https://www.jesverty.com/products/view?id=21839&lang=en).
- [ASIN and model matching cross-reference](https://device.report/jesverty/sps-3010m).

**For Paky-01/Paky-02 actuator prototyping:** at a 24 V setpoint, a 10 A current ceiling implies **240 W nominal**, not evidence of capacity to sustain any specific motor's transient or continuous demand. Motor braking can feed energy back into a supply that may not tolerate sink current. Do not assume the PSU handles regeneration. Do not join an earth-referenced oscilloscope ground to an ESC switching node. Design safe probe/earthing procedures before testing.

**Source hygiene:** the screenshot also contains an unrelated 30 V / 30 A sponsored unit. That unit was **not** purchased and is not in the inventory.

## LAB-SAV-CHG-001 — Robot battery charger

- **Presence:** operator-reported owned.
- **Make/model:** unknown.
- **Battery chemistry, voltage / cell count, maximum charge current, balance capability:** unknown.
- **Next intake:** identify the exact make/model and manufacturer manual, then verify safe operating limits for the actual robot battery.
- Do not extrapolate these parameters from the PSU.

## LAB-SAV-DMM-001 — Digital multimeter

- **Presence:** operator-reported owned.
- **Make/model:** unknown, described as an inexpensive multimeter.
- **Ranges, accuracy, lead insulation, fuses, input safety category:** unknown.
- **Next intake:** physical photographs and manual; verify test leads and current input fuse ratings before using higher-energy circuits.

## Planned additions (not owned or allocated to this site)

- 4-channel scope (100 MHz preferred) with verified protocol decode options.
- Appropriate rated differential probes / current-measurement tools for ESC work.
- Logic analyzer and temperature sensing for repeatable long-duration tests.
- Higher-confidence/reference multimeter once the planned measurements require it.

Physical inventory, calibration records and energized test authorization require their own dated review. For the structured entries see [equipment.yaml](equipment.yaml).
