# synthesis.md

Cross-combo synthesis. Updated only by task (d).

## State after run 2 (Routine v6 reset, 2026-05-28)

All four combos have now been surveyed at least once under v6 keywords.
Combined adoption: 10 engineering papers + 1 sociology review. The
shape of the moneyless stack the literature can currently *justify* is:

```
   sensor ──► l1-tiny (TinyML)      ──► (control output, no UQ)        — combo-D, 2603.11071
   sensor ──► l1-reliability (PHM)  ──► (score, per-group-uncertainty) — combo-A, 2412.11967 / 2507.06672 / 2511.21208 / 2510.17846
   nodes  ──► l1-fusion (MMEdge)    ──► (multimodal score, low latency)— combo-D, 2510.25327
   asset  ──► FootprintPassport     ──► (multi-criteria impact record) — combo-C, 2509.00093 / 2601.21632
```

Note three of the four boxes terminate at "produces an output." The
*consumption* side — a vote rule that takes
`(per-asset health, per-asset footprint)` and outputs a priority — is
**not** attested by any adopted paper in any combo this run.

## Recurring primitives across combos

1. **`(score, uncertainty)` as the L1 output unit.** Surfaced in
   combo-A (RUL with aleatoric + epistemic UQ) and is the natural input
   shape combo-C's priority rule would consume. Combo-D papers
   currently produce *score only*; this is the cleanest near-term
   convergence target (give the TinyML and MMEdge outputs a calibrated
   UQ head).

2. **Per-asset *multi-criteria* impact record.** Combo-C's adoptions
   reject single-metric carbon reporting. The minimum viable footprint
   record is multi-dimensional and lifecycle-phase-keyed. This is the
   "what does a digital product passport carry" answer.

3. **Near-sensor judgment ≠ near-sensor trust.** Combo-D shows
   judgment can be moved to a $5 MCU. Combo-A's "sensor data
   attestation" keyword surfaces 5G-infrastructure attestation, not
   sensor-level attestation. The literature this routine can currently
   reach does **not** close the loop "judgment near the sensor + signed
   receipt near the sensor." This is the single most important gap.

4. **Repair-cycle absorption as the L2 substrate.** Combo-B's one
   robust adoption (Springer review of design-for-repair features for
   circular economy) reframes "surplus" as *time at the repair-replace
   interface* rather than additional production. This is sociology-only
   and updates ROADMAP, not code.

## Open questions (carry forward)

- **Vote rule that consumes uncertainty + footprint.** Not surfaced in
  combo-C this run. Next combo-C run should target arXiv cs.GT
  listings directly for measurement-weighted / uncertainty-weighted
  voting empirical work, *not* generic mechanism design.
- **TEE-attested sensor stream.** Not surfaced in combo-A or combo-D
  this run. The literature exists in IEEE Xplore (TIFS / TDSC), USENIX
  Security, NDSS — none of which the HF semantic search reaches.
  Flagged as the highest-priority cross-combo gap.
- **Sociology DB access.** Combo-B's evidence base lives in Springer /
  ScienceDirect / Lancet / Cambridge Core / SSRN. WebSearch can find
  titles but cannot programmatically retrieve abstracts for strict
  scoring. The "1 adoption + 2 near-miss high-quality candidates"
  outcome this run is the ceiling under the current toolchain; lifting
  it requires direct DB access.

## Direction change vs. run 1

Run 1's synthesis named two load-bearing primitives:

> (1) PINN-driven health monitoring as an L1 reduction.
> (2) Peer-ranked / reputation-weighted consensus as an L3 primitive.

Under v6 framing, **(1) survives** (it is the canonical
`l1-reliability` reduction). **(2) is dropped** — Fortytwo's
peer-ranked consensus is application-internal and does not consume a
physical measurement; it does not fit combo-C v6's
"measurement → priority" scope. The L3 layer is *renamed* `l3-priority`
(rather than `l3-consensus`) to reflect this shift: the moneyless stack
does not need consensus *about a ledger*; it needs a priority *over
physical quantities*.

## Honest read

Run 2 (v6) is partial confirmation of feasibility, no confirmation of
the full assertion that "money is unnecessary if reliability,
measurement, and surplus absorption are wired together." The pieces
exist; the wiring (vote rule + sensor-level attestation) is not yet
attested in the literature this routine can reach. The hypothesis is
**buildable in principle, unattested at the closing seam.**
