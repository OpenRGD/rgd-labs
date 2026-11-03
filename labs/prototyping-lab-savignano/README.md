# Prototyping Lab Savignano

**Site ID:** `LAB-SAV`  
**Kind:** domestic prototyping and robot-electronics laboratory (Italia Robotica / OpenRGD)  
**Inventory revision:** 0.1 — 2026-11-03  
**Evidence status:** operator-reported assets; no on-site inspection performed.

## Purpose

This folder is the **site-specific inventory and bench notes** for Prototyping Lab Savignano. It is distinct from both the shared [OpenRGD Labs repository](../../README.md) and per-robot as-built repositories (`italiarobotica/paky-01`, `italiarobotica/paky-02`).

- [Equipment inventory](equipment.md): human-readable asset list, specifications and caveats.
- [Structured inventory](equipment.yaml): machine-readable asset register for future scripts and reports.
- Shared procurement/test-method planning: [global instrumentation index](../../laboratory/equipment.md).

## Scope and publication policy

Public information here may include **generic lab name, make/model, product reference, documented electrical specifications and technical unknowns**. Do not commit the residential street address, purchase invoice, order ID, payment card, unredacted screenshots, serial numbers, network endpoints or access credentials.

Unknown instruments are recorded as unknown rather than assigned guessed specifications. A matching retailer model code establishes **product identification**, not physical bench verification, calibration, or safety certification.

## Current available instruments

| Asset | Instrument | State |
| --- | --- | --- |
| `LAB-SAV-PSU-001` | Jesverty SPS-3010M adjustable DC PSU, 30 V / 10 A nominal | Available, identified from order screenshot and product ASIN; bench specs not independently measured |
| `LAB-SAV-CHG-001` | Robot battery charger, model to identify | Available, operator reported |
| `LAB-SAV-DMM-001` | Budget digital multimeter, model to identify | Available, operator reported |

## Next intake

1. Read the **physical** PSU rating plate and check whether the actual DC range is 0–30 V or 0–32 V: public listings disagree.
2. Identify battery charger model, output / supported chemistries, and balance features.
3. Identify multimeter model, input protection and measurement safety ratings.
4. Specify a suitable 4-channel oscilloscope and safe measurement probes for 24 V servo drives.
5. Only after bench safety planning, define a reproducible test record for the 5010 / 6512 actuator campaign.

No note in this repository authorizes actuating equipment or energizing a robot.
