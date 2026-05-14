# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-18 / run 1 (task a, combo-A v4)**: System now has a literature
  baseline for L1×L3 (physics-grounded maintenance consensus). Three
  papers adopted into `references/combo-A-physics-consensus/INDEX.md`.
  No code changes. No physical link opened.
- **2026-05-14 / run 2 (Research & Build Routine v6)**: Full pass over
  all four v6 combos.
  - `references/combo-A-physics-input/INDEX.md` — 2 adopted (RUL +
    aleatoric/epistemic UQ on PHM benchmarks).
  - `references/combo-B-cost-surplus/INDEX.md` — 2 adopted (DfR and
    Repair-Oriented Design for circular electronics).
  - `references/combo-C-priority-from-measurement/INDEX.md` — 3
    adopted (Extended Exergy Accounting industrial study, Digital
    Product Passport for circular SCM, Circular Economy Metrics
    review).
  - `references/combo-D-near-sensor-judgment/INDEX.md` — 3 adopted
    (MMEdge on-device multimodal inference, Sensing-to-Action at
    the edge, TZ-LLM TEE-secured on-device LLM).
  No code changes. No physical link opened.

## Open work queue

Carry-over from run 1 (still valid):

1. Stub `nodes/l1-reliability/` with a PHM skeleton reducing paper
   **arXiv:2412.11967** (PINN-based engine health monitoring) into a
   degradation-indicator function. (task b)
2. Stub `nodes/l3-consensus/` with a peer-ranked consensus skeleton
   reducing **arXiv:2510.24801** (Fortytwo). (task b)
3. Draft candidate `PHYSICAL_LINK: l1-reliability ↔ l3-consensus`
   citing **arXiv:2510.03807** (6G Digital Twin for industrial bearing
   fault detection) as physical basis. Status will enter as `proposed`.
   (task c)

New from run 2 (v6 pass):

4. Extend the `l1-reliability` stub's first callable from
   `health_indicator(window) → score` to
   `health_indicator(window) → (score, σ_aleatoric, σ_epistemic)`,
   reducing **arXiv:2507.06672** and **arXiv:2511.21208**. (task b)
5. Stub `nodes/l2-slack/` with `repairability(product_spec) →
   (score_0_1, breakdown)` reducing the DfR taxonomy from Discover
   Sustainability 2025 (**10.1007/s43621-024-00753-x**). (task b)
6. Stub `nodes/l3-priority/` reading-side: a callable
   `extended_exergy(node_state) → number` reducing Qi et al. 2025
   (Scientific Reports). (task b)
7. Stub `nodes/l3-priority/` schema side: a JSON schema for a
   per-resource DPP record, reducing the Tandfonline 2024 DPP review
   use-case list (**10.1080/13675567.2024.2374256**). (task b)
8. Draft candidate `PHYSICAL_LINK: sensor ↔ l1-reliability` with
   "signed-output-at-source" via TZ-LLM-style TEE construction,
   citing **arXiv:2511.13717** as the physical basis. Status:
   `proposed`. This is the link the routine's prior synthesis
   flagged as missing. (task c)
9. Draft candidate `PHYSICAL_LINK: l1-reliability ↔ l3-priority` via
   the (score, σ) → extended-exergy-weighted vote bridge.
   **Engineering basis incomplete** — combo-C's negative result
   stands: no published paper grounds a voting weight in a physical
   measurement. Status will enter as `blocked`, not `proposed`.
   (task c)
10. Re-run combo-A in ~6 months. Re-entry candidates already noted:
    2510.17846 (CARLE), 2504.19013 (Bayesian PINNs), 2510.03807 (6G
    DT). All are 2.0-borderline under v6 keyword strictness.
11. Re-run combo-D when window slides past Apr 2024 + 25d so that
    **arXiv:2404.12599 (QUTE)** falls inside. QUTE is the missing
    TinyML-UQ piece.

## Not yet explored

- Sociology / policy line of combo-B (post-growth, time-banking,
  non-market work). Captured in INDEX as ROADMAP-only signal; no
  engineering reduction. **Do not** create a node from these.
- Quadratic voting / mechanism-design literature with a physical
  measurement as vote weight. Negative result from combo-C; carry
  as the headline open problem rather than as future search.

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- v6 strict matching rule (≥2 keyword matches AND score ≥ 2.5)
  applied at adoption; do not retroactively loosen for an
  already-rejected paper.
