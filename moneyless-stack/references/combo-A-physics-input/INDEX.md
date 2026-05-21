# combo-A — Physics Reliability → Consensus Input

> v6 role: 센서에서 나온 고장/수명/상태 추정치를 상위 판단의 입력으로
> 쓰기 위한 부품.

## 0. Run metadata

- **run_date**: 2026-05-21
- **search_window**: 2024-05-21 → 2026-05-21 (last 2 years)
- **prior_run**: 2026-04-18 (combo-A-physics-consensus, v4). Directory
  renamed to `combo-A-physics-input` to match v6 spec. Two papers carry
  forward because they still match the v6 keyword list; the Fortytwo
  paper from v4 is dropped here because v6 combo-A does not include
  consensus keywords (it has migrated to combo-C/D territory).
- **routine version**: v6
- **primary tool**: Hugging Face `paper_search` (semantic), 8 queries
  matching v6 keyword list, pooled and scored.
- **fallback tools used**: none required.

## 1. Executive summary

The v6 combo-A keyword set — RUL prediction, PHM, PINN, condition-based
monitoring, digital twin for maintenance, federated learning for
prognostics, aleatoric uncertainty estimation, sensor data attestation —
intersects most densely on **uncertainty-aware prognostics**. The pool
returns one cluster (Thil et al.) producing two related papers that
combine RUL prediction with explicit aleatoric uncertainty estimation on
the NASA C-MAPSS turbofan dataset, and one PINN+digital-twin paper
(Nath/Karniadakis et al.) on diesel engines. None of the surveyed work
attempts the last keyword, **sensor data attestation** — there is no
in-window paper that wires a calibrated PHM output through a
cryptographic attestation primitive. That gap is the dependency that
combo-D must absorb (TEE / remote attestation literature). The honest
read: combo-A now confirms (a) physics-grounded RUL can be produced with
calibrated uncertainty at device level, but does **not** yet attest
(b) that the attested output can leave the device with provenance
intact. 근거 부족 on the attestation half of the combo.

## 2. Adopted papers (≥ 2 keywords matched AND ≥ 2.5 score)

### 2.1 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025 (Jul 09)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords** (count 3, score 2.5):
  - `remaining useful life prediction` — 1.0 (literal: "Remaining Useful
    Life Prediction" in title)
  - `aleatoric uncertainty estimation` — 1.0 (literal: "aleatoric
    uncertainty" + "epistemic uncertainty" in abstract keywords)
  - `prognostics and health management` — 0.5 (partial via "health
    indicator" + RUL context — PHM domain by construction, term not
    spelled out)
- **분류**: [공학]
- **방법**: RaPP-style reconstruction-along-projected-pathways autoencoder
  on C-MAPSS sensor windows; per-step variational posterior produces both
  aleatoric and epistemic components, fed as auxiliary latent health
  indicator to an RUL regressor.
- **결과**: Adds the UQ-derived health indicator to the RUL input feature
  set; reports improved RUL accuracy over end-to-end baselines that do
  not separate UQ from the regression target.
- **한계**: All evaluation on NASA C-MAPSS (turbofan, simulated). No
  field deployment, no statement on calibration drift under sensor noise,
  no provision for signing/attesting the produced indicator.
- **system reduction**: Justifies `nodes/l1-reliability` exposing
  `rul_with_uncertainty(sensor_window) → (rul_estimate, aleatoric_var,
  epistemic_var)` — three-tuple, not scalar. The `aleatoric_var` slot is
  what combo-C will need to weight votes by physical noise floor.
- **[NEW]**: yes (first appearance under v6).

### 2.2 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords** (count 3, score 2.5):
  - `prognostics and health management` — 1.0 (literal: "prognostics"
    listed in AI-Keywords)
  - `aleatoric uncertainty estimation` — 1.0 (literal: "aleatoric
    uncertainty" + Monte Carlo dropout in keywords)
  - `remaining useful life prediction` — 0.5 (partial via "RUL prediction
    accuracy" in abstract)
- **분류**: [공학]
- **방법**: Extends RaPP by grouping sensor inputs into semantic clusters
  ("indicator groups"); each group runs its own probabilistic latent
  space with Monte Carlo dropout for epistemic UQ; aleatoric handled
  through the reconstruction term.
- **결과**: Better-calibrated per-group degradation signals; improves
  interpretability over the single-latent-space variant 2.1.
- **한계**: Same dataset family (C-MAPSS); grouping is hand-defined per
  sensor topology and does not generalise without engineering input.
- **system reduction**: Lets the `l1-reliability` node expose **per-
  subsystem** indicators instead of a single scalar — i.e. a vector
  `{group_id → (score, uncertainty)}`. This is what an `l3` (consensus)
  layer would consume if it needs to weight votes by which subsystem
  produced the evidence.
- **[NEW]**: yes.

### 2.3 A Digital Twin for Diesel Engines: Operator-infused Physics-Informed Neural Networks with Transfer Learning for Engine Health Monitoring

- **authors**: Kamaljyoti Nath, Varun Kumar, Daniel J. Smith, George Em Karniadakis
- **year**: 2024 (Dec 16) — within v6 window (2024-05-21 onward)
- **venue**: arXiv preprint
- **arxiv**: 2412.11967 · https://hf.co/papers/2412.11967
- **matched_keywords** (count 4, score 3.0):
  - `physics-informed neural network` — 1.0 (literal in title)
  - `digital twin for maintenance` — 1.0 (literal "Digital Twin for
    Diesel Engines" in title; maintenance context via engine health
    monitoring)
  - `prognostics and health management` — 0.5 (partial via "Engine Health
    Monitoring")
  - `remaining useful life prediction` — 0.5 (partial via parameter
    identification + degradation modelling, not RUL per se)
- **분류**: [공학]
- **방법**: PINN with DeepONet (operator-network) prior on a mean-value
  diesel engine model; transfer-learning (multi-stage + few-shot) to
  unseen operating regimes.
- **결과**: Better generalisation than pure data-driven baselines; lower
  inference compute via the operator decomposition; parameter
  identification stable across regimes.
- **한계**: Simulated diesel engine throughout; no real-engine
  validation; transfer across different engines not characterised.
- **system reduction**: Justifies `physics_residual(state, ode_form) →
  scalar` as the canonical degradation indicator inside
  `l1-reliability` — one node-internal function whose output is a
  physics-prior residual, no labels required. Carries forward from v4
  run 1.
- **[NEW]**: no (carried; re-scored against v6 keywords).

## 3. Hypothesis score (1–5, 부품 가치 점수)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra can be made physically reliable enough | 3 | RUL + UQ at device-level is operational; PINN-based DT shrinks the labelled-data requirement. System-scale MTBF arguments still absent. |
| (b) Surplus can absorb non-essential wants | — | out of scope for combo-A. |
| (c) Consensus from measurement directly | 2 | The papers produce numerical outputs (score + uncertainty) but stop there. No paper in the pool wires the output through a cryptographic attestation primitive — that bridge is the unmet dependency. |

**Aggregate**: combo-A v6 cleanly delivers the **upstream half** of the
required interface — a tuple `(estimate, uncertainty)` grounded in
physics. The **downstream half** (transport this tuple as an attested
artifact) is not in this combo's literature; it is a combo-D
responsibility. Treat as partial confirmation.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords** (to re-enter at a later run):

- calibrated remaining useful life
- per-subsystem degradation indicator
- conformal prediction prognostics
- federated PHM aggregation
- attested health indicator (bridge to combo-D)

**Two under-explored adjacent fields**:

- Structural health monitoring (SHM) for civil infrastructure — same
  PINN-plus-UQ pattern with much longer time horizons; useful as a
  stress-test domain for the (estimate, uncertainty) interface.
- Battery state-of-health estimation as a separate vertical — its
  cycle-aware uncertainty literature is more developed than turbomachinery.

## 5. Search log

Per-keyword calls to `paper_search` (HF), 8-12 results each, in-window
filter applied post-hoc by publication date.

| keyword query (v6) | returned | in-window | pooled |
|---|---|---|---|
| remaining useful life prediction | 12 | 7 | 7 |
| prognostics and health management deep learning | 12 | 4 | 4 |
| physics-informed neural network prognostics | 12 | 4 | 4 |
| condition-based monitoring machinery | 12 | 6 | 6 |
| digital twin predictive maintenance | 12 | 7 | 7 |
| federated learning prognostics fault diagnosis | 12 | 5 | 5 |
| aleatoric uncertainty estimation regression | 12 | 4 | 4 |
| sensor data attestation provenance trust | 12 | 5 | 5 |
| physics-informed neural network digital twin engine health (refine) | 8 | 3 | 3 |
| remote attestation IoT edge device integrity (refine) | 8 | 4 | 4 |

- **pooled after in-window filter, pre-dedup**: ~49
- **dedup (arXiv ID + title-normalised)**: ~11 duplicates removed (2507.06672
  appeared in 2 queries; 2511.21208 in 2; 2412.11967 in 2).
- **candidates scored ≥ 2 keywords**: 6
  - 2507.06672 (3 kw, 2.5) ✓ adopted
  - 2511.21208 (3 kw, 2.5) ✓ adopted
  - 2412.11967 (4 kw, 3.0) ✓ adopted (carried)
  - 2510.17846 CARLE (3 kw, 2.0) — rejected, just under
  - 2412.17823 RUL wind turbine (3 kw, 2.0) — rejected, just under
  - 2410.23893 DiffBatt (2 kw, 1.5) — rejected
- **rejected at < 2.5**: 3 borderline (above) + ~10 single-keyword hits.

**Search confidence**: medium-high on RUL/PHM/PINN/UQ axes (saturated —
the same author cluster recurs across queries). **Low** on `sensor data
attestation`, `federated learning for prognostics`, and `condition-based
monitoring` (none of these alone surfaced a paper that compounded with
the rest). The attestation gap is structural, not a search miss — it is
the v6 architectural seam between combo-A and combo-D.
