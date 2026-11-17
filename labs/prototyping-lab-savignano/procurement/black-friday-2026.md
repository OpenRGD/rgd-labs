# Black Friday 2026 — Prototyping Lab Savignano

**Status:** candidate shopping / watchlist; **NOT** an order list, cart access, or proof of ownership.  
**Created:** 2026-11-17  
**Retailer focus:** Amazon.it  
**Sale window:** 2026-11-19 → 2026-11-30 (Black Friday 2026-11-27, Cyber Monday 2026-11-30).  
**Lab inventory:** [equipment.md](../equipment.md).

## Purchasing rules

1. Buy only after checking whether an equivalent working tool is already owned.
2. A price threshold below is **our proposed purchase target**, **not** an observed historical low, confirmed discount, or guarantee.
3. Price comparisons must use **the exact brand/model/variant** on **Amazon.it**, delivered price incl. IVA and shipping, seller identity, coupons, warranty and return conditions. Treat prices discovered off Amazon as non-Amazon reference only.
4. Use a source such as Keepa for 3- to 12-month price history before purchasing; do not trust crossed-out list prices.
5. Do not substitute safety-critical high-current connectors, leads, probes, crimpers or power devices with an unverified cheap alternative.
6. Physical instrument selection/compatibility must be reviewed before any energized measurement; oscilloscope probes are generally earth-referenced unless documented otherwise.

## Watchlist: known candidates

| Priority | Equipment | Target model / identifying query | Threshold (EUR, all-in) | State | Notes |
| --- | --- | --- | ---: | --- | --- |
| P1 | Oscilloscope | **OWON VDS1022I** OR **Hantek DSO2C10** | 115 for OWON / 210 for Hantek | OPERATOR_REPORTED_CART_UNSPECIFIED | User said scope added to Amazon cart, **exact model not confirmed**. Prefer Hantek if budget allows; investigate computer integration/OS compatibility and probe safety. Do **not** assume a specific item is in cart. |
| P1 | Temperature-controlled soldering station | **YIHUA 926LED-III** | **43** | WATCH | Suitable electronics bench option if no quality soldering station already exists. Verify tip ecosystem, EU voltage, temperature controls. |
| P1 | Digital multimeter backup / upgrade | **UNI-T UT61B+** | **50** | WATCH | Confirm lead safety, fuse specifications, actual measurement CAT rating and intended use. Budget DMM remains available. |
| P1 | Open-barrel crimp tool | **IWISS iCrimp SN-28B** | **21** | WATCH | Check compatibility with the *actual* contact family and wire gauge; not a universal JST crimper. |
| P1 | ESD mat + proper grounding accessories | **StarTech ESD work mat** OR equivalent purpose-designed grounded mat | **35** | WATCH | Confirm continuity/resistance, grounding point and included accessories. Avoid falsely treating a heat-resistant silicone mat as ESD protective. |
| P2 | USB logic analyzer (8ch) | **SEENGREAT 24 MHz 8-channel / CY7C68013A with PulseView/sigrok support** | **14** | WATCH | Hobby/debug tool only; verify operating voltage, supported interfaces and real sustained sampling. |
| P2 | Hot-air rework station | **YIHUA 959D** | **55** | WATCH | Mainly for SMD rework; avoid buying if there is no need to rework PCBs. |
| P2 | Precision-bit tool kit | **iFixit Manta Kit** | **55** | WATCH | Useful only if no comparable tools already available. |
| P2 | Solder fume extraction | **YIHUA 948DQ-I** or better properly ventilated system | **45** | WATCH | Desk fan/carbon pad does **not** replace proper local extraction and ventilation. |
| P3 | Digital caliper | **INSIZE 1108-150 / reliable 150 mm** | **45** | RESEARCH | Verify variant, authentic seller, calibration requirements; avoid counterfeit-prone offerings. |
| P3 | Thermal camera | Model TBD; minimum useful PCB focus and resolution to be specified | TBD | RESEARCH | Defer until precise PCB thermal measurement needs are set. |
| P3 | Differential voltage/current measurement | Rated probes and/or engineered shunt as required by ESC circuit | TBD | SAFETY_REVIEW_REQUIRED | Do not buy incompatible cheap probes just to satisfy a budget. |

**Amazon search shortcuts (search results, not product-detail ASIN guarantees):**

- [YIHUA 926LED-III](https://www.amazon.it/s?k=YIHUA+926LED+III)
- [UNI-T UT61B+](https://www.amazon.it/s?k=UNI-T+UT61B%2B)
- [IWISS SN-28B](https://www.amazon.it/s?k=IWISS+SN-28B)
- [StarTech ESD mat](https://www.amazon.it/s?k=StarTech+tappetino+ESD)
- [SEENGREAT logic analyzer](https://www.amazon.it/s?k=SEENGREAT+24MHz+8+channel+logic+analyzer)
- [YIHUA 959D](https://www.amazon.it/s?k=YIHUA+959D)
- [iFixit Manta](https://www.amazon.it/s?k=iFixit+Manta+Kit)
- [YIHUA 948DQ-I](https://www.amazon.it/s?k=YIHUA+948DQ-I)
- [INSIZE 1108-150](https://www.amazon.it/s?k=INSIZE+1108-150)
- [OWON VDS1022I](https://www.amazon.it/s?k=OWON+VDS1022I)
- [Hantek DSO2C10](https://www.amazon.it/s?k=Hantek+DSO2C10)

## Consumables and non-optional safety planning (candidate, verify already owned)

- Heat-shrink assortments, high-flex appropriately sized silicone wire, labelled CAN wiring and terminating resistors, ferrules and genuine matching connector contacts.
- Quality low-voltage test leads with safe insulated clips; suitable stand, fixture and E-stop for motor test bench.
- Inspect charger/battery chemistry compatibility and define proper battery charging / fire risk controls.
- ESD grounding and appropriate solder-fume management; a small carbon-filter desk fan alone is not adequate ventilation.

## Price monitoring protocol

Twice-daily public listing checks **while 2026 Black Friday is running**, with notification only for a **confirmed exact-model offer at or below the target threshold**, or an unusually strong, independently verified price drop. Include link, retailer/seller, final cost, date of observation and price history if available. If Amazon blocks automated access or the variant/seller is ambiguous, report as **unverified** rather than guessing and do not alert as if the price were confirmed.

This project uses a public GitHub watchlist, not access to the user's Amazon basket or account. User retains full decision and purchase control.

## Changes after purchase

Only change `state` to `PURCHASED` and add an item to [site inventory](../equipment.md) after operator confirmation, not merely because the model was put in a shopping cart.
