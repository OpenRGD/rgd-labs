# OpenRGD / Italia Robotica — Laboratory equipment inventory

**Revision:** 0.1 (2026-11-03)  
**Purpose:** shared inventory of equipment that can support repeatable electronics, robotics and mechatronics experiments. Not a shopping receipt, not a safety certification, and not a per-robot BOM.

## 1. Bench instruments — available

| ID | Equipment | Model / identity | Reported / advertised specifications | Status | What still needs checking |
| --- | --- | --- | --- | --- | --- |
| LAB-PSU-001 | Adjustable DC bench power supply | **Jesverty SPS-3010M** | 0–30 V DC; 0–10 A; nominal output envelope up to **300 W** if both maxima can be sustained; CV/CC modes; OVP/OCP controls; output enable; USB-A and USB-C ports, USB charging advertised at 20 W | **OPERATOR_REPORTED** (2026-11-03 order/product screenshot); ratings **MANUFACTURER_ADVERTISED**, not validated | Read exact nameplate and manual; test loaded voltage/current accuracy, ripple, current-limit response and thermal limits; establish whether 300 W is continuous; verify USB port behavior and protective-earth/GND relationship |
| LAB-CHG-001 | Robot battery charger | Exact model unknown | Charger for the robot battery | **OPERATOR_REPORTED** (2026-11-03) | Photograph nameplate; supported battery chemistries / cell count; balancing, charge current and safety procedures |
| LAB-DMM-001 | Digital multimeter | Exact model unknown | Budget handheld multimeter; no verified accuracy/ranges | **OPERATOR_REPORTED** (2026-11-03) | Model, probe ratings, CAT ratings, fuses, current measurement limits and test status |

**Important:** the 30 V / 30 A / 900 W unit shown in a sponsored banner above the order is **not** the purchased/owned PSU. The pictured order is the 30 V / 10 A Jesverty SPS-3010M. Numbers on promotional display renders are not measurements.

### PSU implications for actuator tests

- At a 24 V setpoint, 10 A corresponds to **240 W nominal DC** (24 V × 10 A). This is the rated current ceiling, not evidence that the supply supports transient or continuous motor demand without droop.
- Use current limiting conservatively. Sudden motor acceleration or braking can cause voltage transients; regenerative energy handling and reverse-current tolerance of this PSU are **unknown**.
- PSU display readings are operational indicators, not independently calibrated metrology.
- Until verified, do not assume the front-panel `GND`, DC negative and oscilloscope probe ground are interchangeable.

## 2. Development and diagnostics hardware — operator-reported

| ID | Equipment | Information known | Status / open questions |
| --- | --- | --- | --- |
| LAB-CAN-001 | USB-to-CAN adapter | OpenMoko / `gs_usb` family; `can0` previously used at 1 Mbit/s on the Paky-01 bench | OPERATOR_REPORTED; exact adapter model, isolation and electrical ratings to verify |
| LAB-DBG-001 | ST-LINK debugger | ST-LINK/V2.1 previously used for controller flashing | OPERATOR_REPORTED; physical revision and compatibility to verify |

These entries document shared **test tools**, not proof that a given robot currently has them connected.

## 3. Fabrication and compute — operator-reported, pending detailed inventory

| Category | Reported setup | Pending |
| --- | --- | --- |
| 3D printers | 2 × Anycubic, 1 × Bambu; at least one **Anycubic Kobra 3** | Exact models, nozzle configurations, build volumes, maintenance and enclosure/ventilation status |
| Robot-side development computer | Ubuntu 22.04 mini-PC; Intel N150; approximately 15 GiB visible RAM | Storage, ports, PSU, installed interfaces and software snapshot |
| Remote compute workstation | ASUS TUF Z890-PRO Wi-Fi; 64 GB RAM; NVIDIA RTX 5080 | Full inventory and agreed benchmark/test procedures |

Treat these as existing operator notes, **not** a completed physical stocktake.

## 4. Planned instrumentation (not owned)

| Priority | Instrument | Baseline target / rationale | Status |
| --- | --- | --- | --- |
| P1 | Bench oscilloscope | 4 channels; 100 MHz preferred; ≥1 GSa/s where channel configuration allows; sufficient capture memory; useful CAN/UART/I²C/SPI decoding | PLANNED — compare models, feature licensing and probe kit before purchase |
| P1 / safety-dependent | Suitable differential voltage probe and/or isolated measurement setup | Safe inspection of high-side switching nodes; choose adequate common-mode voltage, bandwidth and category for the actual circuits | PLANNED — scope purchase alone does not make high-side probing safe |
| P2 | Current measurement solution | Appropriate current clamp/probe or correctly specified shunt + differential front end | PLANNED — indispensable for phase/bus-current waveforms |
| P2 | USB logic analyzer | Extended captures / digital protocol inspection; complement to scope | PLANNED |
| P2 | Contact temperature probes or thermal camera | ESCs, wiring, terminals and motors during repeatable load tests | PLANNED |
| P3 | Better reference multimeter | Calibrated accuracy and safety class suitable for intended electrical work | PLANNED; the existing DMM remains useful for basic continuity checks after inspection |

## 5. First experimental campaign — proposed

**Candidate:** 5010 and later 6512 actuator characterization, under a separately reviewed electrical and mechanical procedure.

Desired data channels (not yet available from this inventory):

- Supply: setpoint, bus voltage at ESC, bus current, current-limit events, ripple and transient spikes.
- Communications: CAN physical layer (CAN-H / CAN-L using an electrically appropriate acquisition technique), packet timestamps and errors.
- Actuator: command, joint position, velocity, torque/current telemetry and fault state.
- Thermal: motor, ESC and connector temperatures; ambient temperature.
- Context: actuator ID, ESC firmware/configuration, imposed load, test duration, test operator and equipment revision.

**Safety / scope gate:** no assumption that the existing power supply can absorb regenerative braking; do not connect a conventional earth-referenced oscilloscope probe ground to a switching phase or unknown-potential node. Select rated probes and verify grounding first. High-load, unattended, energized or moving-robot tests need separate risk review.

## 6. Inventory maintenance

When a model/serial is confirmed, record the following in a **private** asset ledger as appropriate; use a public generalized identifier here:

```yaml
asset_id: LAB-XXX-001
category: instrument
make: null
model: null
spec_source: operator_reported # or manufacturer_advertised / physically_verified
acquisition_date: null # optional, PRIVATE
verified_at: null
verified_by: null
calibration_status: unknown
manual_reference: null
current_condition: unknown
known_limitations: []
next_action: confirm_model
```

A future measurement record must include calibration assumptions, raw acquisition files where shareable, date, operator and data provenance. Do not represent tests on the physical robot as complete until actually performed.

**Next intake:** photo/model of robot charger and multimeter; actual PSU nameplate and manual; confirmation of printer models.
