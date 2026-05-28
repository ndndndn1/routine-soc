# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-18 / run 1 (task a, combo-A, Routine v4)**: System gained a
  literature baseline for L1 × L3 (physics-grounded maintenance
  consensus) under v4 framing. Three papers adopted into
  `references/combo-A-physics-consensus/INDEX.md`. No code changes,
  no physical link opened.

- **2026-05-28 / run 2 (task a × 4, Routine v6 reset)**: Routine
  bumped from v4 to v6. Combo directories renamed:
  - combo-A-physics-consensus → combo-A-physics-input
  - combo-B-zmc-slack → combo-B-cost-surplus
  - combo-C-sustainability-dlt → combo-C-priority-from-measurement
  - combo-D-physical-ai-substrate → combo-D-near-sensor-judgment

  Combo-A v6: 4 papers adopted (Operator-infused PINN 2412.11967
  carried over; Uncertainty-Aware RUL Turbofan 2507.06672, I-GLIDE
  2511.21208, CARLE 2510.17846 newly adopted). The previously-adopted
  6G Digital Twin (2510.03807) and Fortytwo (2510.24801) no longer
  clear the v6 keyword threshold and are removed from the adopted list
  with explanatory notes in §5 of the combo-A INDEX.

  Combo-B v6: 1 paper adopted (Springer *Discover Sustainability* 2024
  review of design-for-repair features for the circular economy,
  doi:10.1007/s43621-024-00753-x). Classified `[사회학]`. Acknowledged
  tool gap: HF index does not cover Springer / ScienceDirect / Lancet
  venues that combo-B's keywords need; flagged for next run with
  direct DB access.

  Combo-C v6: 2 papers adopted (Cradle-to-Grave LCA of A100 GPU
  2509.00093; Sustainable Open-Source AI Footprint Tracking
  2601.21632). The L3 priority *plumbing* is now attested; the
  priority *rule* (vote/decision function) remains open.

  Combo-D v6: 4 papers adopted (TinyNav 2603.11071; TinySV 2406.01655;
  MMEdge 2510.25327; AI-Driven Predictive Maintenance with V2X Data
  Fusion 2603.13343). Near-sensor inference path is now well-attested;
  the TEE / remote-attestation-at-sensor gap remains.

  Total adopted this run: 11 engineering papers + 1 review (sociology).
  No code changes, no physical link opened.

## Open work queue

Carried from run 1 (still valid under v6):

1. (task b) Stub `nodes/l1-reliability/` with a PHM skeleton reducing
   **arXiv:2412.11967** (Operator-infused PINN for diesel engine
   health) into a degradation-indicator function returning
   `(score, uncertainty)`.
2. (task b) Stub `nodes/l3-consensus/` is **deprecated** under v6 —
   Fortytwo (arXiv:2510.24801) no longer meets the combo-A v6
   threshold and is not a measurement-grounded consensus primitive.
   Replace with `nodes/l3-priority/` stub once combo-C surfaces a
   vote rule (not yet attested in this run).
3. (task c) Draft candidate `PHYSICAL_LINK: l1-reliability ↔
   l1-tiny` citing **arXiv:2603.13343** (AI-Driven Predictive
   Maintenance with V2X Data Fusion) as physical basis — the link
   carries a *fused* sensor stream, not a raw sensor stream. Status
   will enter as `proposed`.

New from run 2 (v6):

4. (task b) Stub `nodes/l1-tiny/` with a TinyML skeleton reducing
   **arXiv:2603.11071** (TinyNav) into a sensor-to-control function
   that fits a $5 MCU budget. This is the cheap-node-many counterpart
   to the l1-reliability node.
5. (task b) Extend `nodes/l1-reliability/` output shape to
   `(score, aleatoric_var, epistemic_var, per_input_group_var)`
   following **arXiv:2507.06672** (UQ for RUL on Turbofan) and
   **arXiv:2511.21208** (I-GLIDE).
6. (task d) Add an `nodes/l2-entropy/` design-direction note citing
   the Springer review (10.1007/s43621-024-00753-x): surplus is
   absorbed by *extending the repair-replace cycle*, not by
   substitution-in-kind. Document only — does not open a link.
7. (task b) Stub `nodes/l3-priority/` with a footprint-passport
   data-class reducing **arXiv:2601.21632** (Footprint Tracking for
   Open-Source AI Derivatives) into a `FootprintPassport(asset_id,
   per_phase: dict[Phase, MultiCriteriaImpact])` record. The class
   carries the data; a vote rule that *consumes* it is still open.
8. (task a) Next combo run: **re-enter combo-C** with arXiv cs.GT
   listings (not HF) to find an attested measurement-weighted vote
   rule.
9. (task a) **Re-enter combo-B** with direct Springer / ScienceDirect
   / SSRN access to lift the "근거 부족" risk for the surplus-absorption
   side.
10. (task a) **Re-enter combo-A or combo-D** specifically to chase
    `TEE-attested sensor stream` — the single biggest cross-combo
    gap. Suggested venues: IEEE Xplore (TIFS / TDSC), USENIX Security,
    NDSS.

## Not yet explored (still)

- Direct DB access to Scopus / ScienceDirect / SSRN (combo-B / combo-C
  primary tools per the routine; unavailable in this run).
- Korean-language sources (KCI / RISS) — not entered in run 1 or run 2.

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- Routine version is part of every INDEX.md `run metadata` block; v4
  adoptions are *not* automatically grandfathered into v6 — they are
  re-scored each transition.
