# synthesis.md

Cross-combo synthesis. Updated only by task (d).

## State after run 2 (2026-04-24, v6)

Four combos have been surveyed. Under the v6 keyword-and-threshold
rule the picture is asymmetric: combos A and D have adoptable
engineering literature, combos B and C do not (within HF's reach).
This asymmetry is **expected and load-bearing for routine planning**,
not a failure.

### What was adopted (10 papers total)

| combo | count | arXiv IDs |
|---|---|---|
| A (physics-input) | 5 | 2511.21208, 2510.17846, 2507.06672, 2412.11967, 2506.16095 |
| B (cost-surplus) | 0 | — (근거 부족) |
| C (priority-from-measurement) | 0 | — (근거 부족) |
| D (near-sensor-judgment) | 5 | 2510.25327, 2502.02692, 2405.07601, 2406.01655, 2603.11071 |

### What v6 retained and dropped from run 1

- **Retained**: 2412.11967 (Diesel PINN) still clears cleanly.
- **Dropped from adoption**: 2510.03807 (6G digital twin, 1.5 under
  v6's stricter combo-A keyword set) and 2510.24801 (Fortytwo —
  orphaned; doesn't match any v6 combo keyword). The papers remain
  referenced and remain interesting; they just no longer *justify
  stack components* under v6.

## Load-bearing observations

### 1. The HI-with-UQ primitive is now attested, replicably

Three independent 2025 papers (I-GLIDE, CARLE, Thil turbofan)
converge on the same signal shape: a health indicator accompanied by
*both* aleatoric and epistemic uncertainty, across at least three
physical domains (turbofan, rolling bearing, aero-engine parts).
This is the L1 `health_indicator` contract the routine has been
searching for since run 1. It is now safe to code `nodes/l1-reliability/`
against the signature
`sensor_window → (score: float, aleatoric: float, epistemic: float)`
— that contract is defensible regardless of which member of the
{PINN, RaPP, CARLE} family is plugged in behind it.

### 2. Node-local judgment closes part of the consensus-input gap

Combo-D's adopted set (MMEdge, Trivedi sensing-to-action, TinyNav,
TinySV, 2405.07601) establishes that judgment can terminate at the
sensor. The combo-A L1 output does not need to travel to a central
arbiter to be useful; it can already be *acted upon* locally. This
matters because it means the moneyless-stack's consensus layer
(L3) inherits a much narrower communication surface than a
classical blockchain consensus would — most decisions never leave
the node. This partially substitutes for measurement-direct priority
(combo-C's unfilled role): nodes don't need to negotiate over
priorities they can satisfy alone.

### 3. The attestation gap is now cross-combo, not combo-local

Both combo-A (sensor-data attestation) and combo-D (remote
attestation restricted to compute-node integrity, not sensor
output) flag the same void: **there is no adopted paper that
cryptographically attests the physics-derived output of a sensor**.
This is the single most important unfilled position in the stack
after run 2. The next runs should target this axis first.

### 4. Combos B and C are tool-mismatched, not content-empty

The v6 rule "채택 수 저조 시 키워드 확장 금지 — 근거 부족으로 기록"
has been followed for both B and C. This is an honest record, not a
dismissal: the sociology/environmental-accounting literature exists
but is not on HF. Next B/C runs should go to Scopus/ScienceDirect
(as v6 already designates in "주 도구"), not to a broader HF query.

## Open questions (carry forward)

- **Attestation/signing of a physics-derived indicator**: unfilled
  in both combo-A and combo-D. Candidate approaches to look for next
  run: PUF-backed signatures on sensor outputs, zkML proofs over
  PHM inference, TEE-enclosed HI computations with remote attestation.
- **Thermodynamic-to-priority mapping**: unfilled in combo-C.
  Candidate: exergy / emergy literature on Scopus, plus cs.GT
  quadratic-voting deployment reports.
- **Engineering-grade DfD artifacts**: unfilled in combo-B.
  Candidate: Scopus / J. of Cleaner Production / Circular Economy
  Journal for the 2025 DfD reviews; EN 45554 standard for the
  measurable-repairability axis.

## Direction (non-binding — routine decides)

The logical next-run is a **task (c) on combo-A's calibrated HI
contract**, opening a PHYSICAL_LINKS.md entry for
`l1-reliability ↔ l3-consensus` citing I-GLIDE (2511.21208) as the
"what travels" and Trivedi sensing-to-action (2502.02692) as the
"why it travels only on demand". The link should enter with
`status: proposed` until the attestation gap closes.
