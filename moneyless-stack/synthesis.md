# synthesis.md

Cross-combo synthesis. Updated only by task (d) or after a full v6 pass.

## State after run 2 (v6 pass over all 4 combos)

The hypothesis is "money is a substitute for trust; if (a) production
infra is physically reliable, (b) surplus can be allocated to
non-essential wants, (c) priority is derived from physical
measurements, then the money layer is redundant". v6 surveyed all
four combos under tightened keyword discipline. The picture that
emerges:

- **L1 / per-node trust (combo-A + combo-D)** — load-bearing pieces
  are now anchored in the literature. We have:
  - a node-local `(score, σ_aleatoric, σ_epistemic)` health
    indicator (combo-A 2.1, 2.2),
  - a near-sensor judgement pattern that keeps raw sensor data
    inside the node (combo-D 2.1, 2.2),
  - a TEE construction that makes the node's output signable at
    source (combo-D 2.3).
  Net: the L1 "signed health indicator" construct that run 1 flagged
  as open is now buildable. The implementation is multi-component
  but each component has a 2025/2026 anchor.

- **L2 / slack allocation (combo-B)** — repairability has been
  reduced to a small set of measurable design parameters by the DfR
  / Repair-Oriented Design literature (combo-B 2.1, 2.2). This is
  the *measurement side* of slack. The *policy side* (what counts
  as a want, how much slack a node may consume on it) remains in
  post-growth / time-banking literature, which we have explicitly
  marked as ROADMAP-only (sociology). The split is deliberate.

- **L3 / priority from measurement (combo-C)** — Extended Exergy
  Accounting (combo-C 2.1) gives a worked example of "collapse
  heterogeneous physical inputs to one comparable number". DPP
  (combo-C 2.2) gives the record format that carries the inputs
  from sensor to accountant. CE Metrics review (combo-C 2.3) gives
  the catalogue from which a minimum measurement set is chosen.

- **L3 / aggregation across nodes** — the gap. Quadratic-voting
  literature exists (Benhaim/Falk/Tsoukalas 2025 Management Science,
  QV-net 2025 IACR), uncertainty-weighted decision literature
  exists, but none of the in-window papers binds a vote weight to a
  *physically measured* quantity. The bridge from combo-C's
  "comparable number" to a multi-node decision is not attested in
  the surveyed literature. This is now the routine's headline open
  problem.

## Net direction read

Direction is **strengthened, not changed**. v6 confirms run-1's
intuition that the moneyless stack is assembleable from existing
engineering primitives. The remaining genuine gap is small and well-
defined: a published voting / aggregation mechanism that takes
sensor-derived measurements as direct input. That gap is more
honest than what run 1 had — run 1 thought multiple pieces were
missing; v6 narrows the unsolved part to one specific construction.

## Open questions (carry forward)

- Can a published QV / mechanism-design paper be located (or
  written) that grounds vote weight in a physical exergy / footprint
  measurement? This is the only piece blocking the L3-aggregation
  story.
- Can on-device UQ (TinyML / QUTE-style) and TEE-attested output
  (TrustZone) be co-published as one pipeline? Not yet in the
  literature; possibly implementation work rather than a research
  gap.
- Empirical DPP rollout under EU ESPR (in force Jan 2025) will start
  producing operational data in late 2026. Worth re-entering
  combo-C then; the use-case review will date quickly.

## Score deltas vs run 1

| sub-hypothesis | run 1 | run 2 (v6) | reason for change |
|---|---|---|---|
| (a) reliable infra | 2 | 3 | +TEE-attested on-device inference; +UQ-split health indicator. |
| (b) surplus absorbs wants | — | 2 | first run scoring this axis; engineering side anchored, policy side ROADMAP-only. |
| (c) measurement-direct consensus | 2 | 3 | +EEA worked example, +DPP schema. *Decision* layer still 2. |
