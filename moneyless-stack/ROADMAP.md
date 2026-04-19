# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-19 / run 2 (Routine v6 rebaseline, all four combos)**:
  System has a v6 literature baseline across all four combos at the
  same date. Adopted papers per combo are stored under
  `references/combo-{A,B,C,D}-*-/INDEX.md` with the v6 directory
  naming convention (`combo-A-physics-input`,
  `combo-B-cost-surplus`, `combo-C-priority-from-measurement`,
  `combo-D-near-sensor-judgment`). The previous run-1 directories
  (`combo-A-physics-consensus`, `combo-B-zmc-slack`,
  `combo-C-sustainability-dlt`, `combo-D-physical-ai-substrate`) are
  retained as run-1 history and are not deleted. No code changes. No
  physical link opened.
  - Combo A: 3 adoptions (RUL/aleatoric UQ/PHM cluster).
  - Combo B: 1 adoption (open-source modular hardware) + 근거 부족
    flagged for the social-science axis.
  - Combo C: 1 strict + 1 borderline-with-caveat adoption; 근거 부족
    flagged for exergy/DPP/quadratic-voting axes.
  - Combo D: 3 adoptions (TinyML UQ + on-device TEE + sensing-to-
    action survey). **Combo D is the load-bearing combo of v6**.

- **2026-04-18 / run 1 (task a, combo-A — Routine v4)**: System had a
  literature baseline for L1×L3 (physics-grounded maintenance
  consensus). Three papers adopted into
  `references/combo-A-physics-consensus/INDEX.md`. No code changes.
  No physical link opened.

## Open work queue (derived from run 2)

1. Stub `nodes/l1-near-sensor/` reducing **arXiv:2404.12599 (QUTE)**
   into a `(prediction, uncertainty)` early-exit ensemble skeleton.
   This is the smallest module that bridges combo-A's calibrated-
   indicator requirement and combo-D's on-device locality
   requirement. (task b)
2. Draft candidate `PHYSICAL_LINK: l1-near-sensor ↔ l3-priority` with
   physical basis cited from **arXiv:2511.13717 (TZ-LLM)** for the
   TEE-rooted execution envelope. Status will enter as `proposed`.
   (task c)
3. Stub `nodes/l3-priority/` reducing **arXiv:2412.18024 (Discounted
   Belief Fusion)** into a fuse-with-uncertainty-discount aggregator.
   Pairs with item 1 — together they implement the
   measurement-to-priority pipeline that combo-C identified as the
   missing bridge. (task b)
4. Run combo-C re-entry **via Scopus/ScienceDirect**, not HF, to
   discharge the exergy / DPP / quadratic-voting backlog. (task a)
5. Carry-forward from run 1: previous queue items referencing
   2412.11967 / 2510.24801 / 2510.03807 are *not* superseded by v6;
   they remain valid and are tracked under the run-1 INDEX.

## Not yet explored

- Sensor-side hardware root-of-trust (signed health indicator) — not
  attested in any combo of v6.
- Energy-harvested edge judgment loops — null result in combo-D.
- Empirical attestation of "saved cost → allocated to wants" in
  combo-B's social-science half (recorded as 근거 부족).

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- Routine v6 directory naming is authoritative for future runs;
  v4 directories are kept as historical read-only.
