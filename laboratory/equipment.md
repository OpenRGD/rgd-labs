# Shared equipment and instrumentation index

**Updated:** 2026-11-03. Site-specific ownership and specifications are canonical in each lab folder.

## Lab sites

| Lab | Site identifier | Inventory |
| --- | --- | --- |
| **Prototyping Lab Savignano** | `LAB-SAV` | [Human-readable equipment list](../labs/prototyping-lab-savignano/equipment.md) · [Structured YAML inventory](../labs/prototyping-lab-savignano/equipment.yaml) |

The Savignano inventory currently includes the **Jesverty SPS-3010M** bench PSU (matching supplied Amazon ASIN `B0CZ92WTQ3`), an unidentified robot battery charger, and an unidentified low-cost multimeter. This is **operator-reported**, not independently inspected.

## Shared or not yet assigned to a site

Previous operator notes refer to the following development resources, but their **current physical location or ownership at a specific lab has not been established**:

| Resource | Previously reported | Next verification |
| --- | --- | --- |
| CAN debugger interface | OpenMoko / `gs_usb` adapter; previously used as `can0` at 1 Mbit/s | Model, isolation, location |
| ST-LINK debugger | ST-LINK/V2.1 previously used for flashing | Actual revision, location |
| 3D printing | 2 × Anycubic; 1 × Bambu; an Anycubic Kobra 3 was reported at home | Models, allocation to laboratory, service |
| Robot compute | Ubuntu mini-PC (Intel N150, approximately 15 GiB available RAM) | Where assigned, hardware spec, runtime |
| Remote development compute | ASUS TUF Z890-PRO Wi-Fi, 64 GB RAM, RTX 5080 | Physical site and benchmarks |

Do not automatically assign these to **Prototyping Lab Savignano** without operator confirmation.

## Instrumentation priorities — proposal, not purchased

1. **P1** — 4-channel oscilloscope, 100 MHz preferred and adequate memory; CAN/UART/I²C/SPI decode to be checked before purchase.
2. **P1 (safety)** — Proper differential voltage probing / grounding plan for high-side switching measurements; a normal grounded scope probe must not be connected to an unknown potential.
3. **P2** — Appropriate current measurement (rated clamp/probe or engineered shunt), logic analyzer, temperature probes/thermal camera.
4. **P3** — Reference multimeter once accuracy/safety requirements justify replacing or complementing a basic unit.

## Experimental evidence direction

Proposed 5010/6512 actuator characterization: log bus voltage/current, CAN physical layer/errors, commanded vs observed motion, motor and ESC temperatures, firmware/configuration and repeatable load conditions. Design a separate physical test approval and electrical safety review before energized or moving-robot experiments.

## Provenance and privacy

- `OPERATOR_REPORTED`: user-supplied statements, screenshots or earlier notes.
- `MANUFACTURER_ADVERTISED`: documented product specification; not verified on installed hardware.
- `PHYSICALLY_VERIFIED`: measured or inspected on the actual equipment, with date, method, and reviewer.
- `PLANNED`: a proposed future purchase or capability.

Never store private residential addresses, invoices, full order numbers, card details, device credentials or sensitive network details in this public repository. Device and site inventory is **not** a new OpenRGD standard or a replacement for the OpenRGD Console.
