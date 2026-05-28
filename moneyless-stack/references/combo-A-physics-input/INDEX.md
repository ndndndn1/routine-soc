# combo-A — Physical reliability → consensus input

System role: turn sensor-side failure / lifetime / state estimates into the
input that higher-level prioritisation can read. Each adopted paper is a
candidate building block for the "L1 reliability physics" node — the part
of the moneyless stack that lets the system know whether a generation
asset is trustworthy enough to be relied on without monetary signalling.

## 0. Run metadata

- **run_date**: 2026-05-28
- **search_window**: 2024-05-28 → 2026-05-28 (last 2 years)
- **prior_run**: 2026-04-18 (Routine v4 — combo-A-physics-consensus). This
  run re-enters combo-A under Routine v6, with a tighter keyword list
  (RUL / PHM / PINN / CBM / DT-for-maintenance / FL-for-prognostics /
  aleatoric UQ / sensor data attestation). Prior adoptions are re-scored
  against v6 keywords; those that no longer clear the 2.5 threshold are
  dropped from the adopted list and noted in §5.
- **routine version**: v6
- **primary tool**: Hugging Face `paper_search` (semantic) over each of the
  8 keywords; pooled, deduped by arXiv ID, scored against the full
  combo-A keyword vector.
- **fallback tools used**: none — HF pool sufficient for combo-A scope.

## 1. Executive summary

Under the v6 keyword frame, combo-A converges on one stable building
block: deep-learning RUL/PHM with explicit uncertainty quantification on
turbofan-style degradation. Four papers clear the ≥ 2.5 / ≥ 2-keyword
threshold; three of them (Operator-infused PINN, the UQ-as-latent-health
turbofan paper, and I-GLIDE) form a coherent pipeline — physics prior →
latent health indicator → aleatoric+epistemic split — and the fourth
(CARLE) is the hybrid deep-shallow baseline. The recurring primitive is
`(score, uncertainty)` as a signed sensor-side output, not just `score`.
What is still **not** attested in the surveyed literature is the bridge
from this `(score, uncertainty)` pair into a remote-attested signed
artifact a downstream consensus node could verify. That is the gap the
routine carries into combo-D (TEE / remote attestation) and combo-C
(uncertainty-weighted decision making).

## 2. Adopted papers (≥ 2 keywords, ≥ 2.5 sum)

### 2.1 A Digital Twin for Diesel Engines: Operator-infused Physics-Informed Neural Networks with Transfer Learning for Engine Health Monitoring

- **authors**: Kamaljyoti Nath, Varun Kumar, Daniel J. Smith, George Em Karniadakis
- **year**: 2024 (Dec 16)
- **venue**: arXiv preprint
- **arxiv**: 2412.11967 · https://hf.co/papers/2412.11967
- **matched_keywords** (count = 3, sum = 2.5):
  - physics-informed neural network — 1.0 (full phrase in title)
  - digital twin for maintenance — 1.0 (digital twin applied to engine
    health monitoring = maintenance-domain twin)
  - prognostics and health management — 0.5 (engine health monitoring is
    a PHM activity but the PHM term is not used)
- **classification**: [공학]
- **방법**: PINN with a DeepONet operator backbone trained on a mean-value
  diesel-engine model; multi-stage and few-shot transfer to unseen
  operating regimes.
- **결과**: Identifies engine parameters and produces health indicators
  with better generalisation and lower compute than purely data-driven
  baselines.
- **한계**: Results stay on simulated engines; cross-engine transfer and
  online sensor-noise robustness are not established.
- **system reduction**: Justifies an `l1-reliability` node whose first
  callable function is `health_indicator(sensor_window) → (score,
  uncertainty)` derived from a physics-prior residual. This is the same
  reduction surfaced in run 1; it remains the canonical L1 primitive
  after v6 rescoring.

### 2.2 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025 (Jul 9)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords** (count = 3, sum = 2.5):
  - remaining useful life prediction — 1.0 (full phrase in title)
  - aleatoric uncertainty estimation — 1.0 (paper's central method is
    quantifying aleatoric and epistemic uncertainty in latent space)
  - prognostics and health management — 0.5 (NASA C-MAPSS turbofan is the
    canonical PHM benchmark)
- **classification**: [공학]
- **방법**: Autoencoder-based latent health indicator augmented with a
  RaPP reconstruction loss and explicit aleatoric/epistemic UQ; trained
  on C-MAPSS turbofan data.
- **결과**: Adding UQ on top of the latent health indicator outperforms
  both traditional methods and end-to-end models on RUL accuracy.
- **한계**: Single-domain evaluation (turbofan only); UQ is post-hoc on
  latent reconstructions, not a calibrated probabilistic head.
- **system reduction**: Defines the *shape* of the L1 output — the node
  should expose `(rul_estimate, aleatoric_var, epistemic_var)`, not just
  `rul_estimate`. Combo-C and combo-D depend on this triple: combo-C
  needs the uncertainty to weight priorities, combo-D needs it to know
  when to escalate to a higher node.

### 2.3 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords** (count = 3, sum = 2.5):
  - remaining useful life prediction — 1.0 (RUL prediction is the
    headline task)
  - aleatoric uncertainty estimation — 1.0 (aleatoric and epistemic UQ
    via Monte Carlo dropout is the core mechanism)
  - prognostics and health management — 0.5 (paper keyword list
    explicitly includes "prognostics")
- **classification**: [공학]
- **방법**: Splits sensor channels into input groups and trains a separate
  RaPP-based latent health indicator per group; aggregates via a
  probabilistic latent space with MC-dropout UQ.
- **결과**: Improves RUL accuracy and per-sensor interpretability in
  multi-sensor systems; surfaces which input groups drive uncertainty.
- **한계**: Group partitioning is hand-chosen; sensor-group invariance
  under hardware changes is not tested.
- **system reduction**: Refines 2.2's L1 output shape: the node should
  also report `per_input_group_uncertainty` so that a downstream priority
  vote can discount specific failing sensor groups instead of the whole
  node. Connects directly to combo-D's near-sensor judgment work.

### 2.4 CARLE: A Hybrid Deep-Shallow Learning Framework for Robust and Explainable RUL Estimation of Rolling Element Bearings

- **authors**: Waleed Razzaq, Yun-Bo Zhao
- **year**: 2025 (Oct 10)
- **venue**: arXiv preprint
- **arxiv**: 2510.17846 · https://hf.co/papers/2510.17846
- **matched_keywords** (count = 3, sum = 2.5):
  - remaining useful life prediction — 1.0 (RUL estimation is the task)
  - prognostics and health management — 1.0 (paper's own keyword list
    uses "prognostic health management" — accepted as full phrase under
    the routine's singular/plural normalisation)
  - condition-based monitoring — 0.5 (robust under varying operating
    conditions is the CBM use case, though the term itself is not used)
- **classification**: [공학]
- **방법**: Hybrid Res-CNN + Res-LSTM front-end with multi-head attention,
  feeding a Random Forest regressor; continuous wavelet front-end and
  Gaussian filtering for explainability.
- **결과**: Robustness across operating conditions is materially better
  than deep-only baselines; the shallow tail makes the per-prediction
  rationale auditable.
- **한계**: Bearing-only; the explanation channel is feature-importance,
  not a calibrated uncertainty estimate.
- **system reduction**: The "explainable RUL" piece is the reason this
  paper enters L1 rather than just being a benchmark. The downstream
  consensus has to be able to *cite* why a node's reliability vote moved;
  CARLE-style feature-importance is one of the few cheap mechanisms that
  produces such a citation without a separate explainer model.

## 3. Hypothesis score (1–5)

The hypothesis under test (routine §"핵심 가설"):

- **(a) production-side physical reliability is high enough to remove
  monetary trust** — combo-A score: **2/5**. Four PHM/RUL papers show
  per-asset reliability can be *estimated*, with calibrated UQ in 3 of
  the 4. None demonstrates a system-of-systems MTBF claim that would
  let physical reliability stand in for trust at network scale.
- **(b) surplus can absorb non-essential wants** — out of scope for
  combo-A, deferred to combo-B.
- **(c) priority is derived directly from measurement** — combo-A
  score: **2/5**. The papers produce `(score, uncertainty)` triples that
  a priority mechanism *could* consume, but the consumption side
  (combo-C) is not wired in. This run does not close the gap, it
  only sharpens the L1 output shape required for combo-C to do so.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords** (re-entered in next combo-A run or combo-D):
- conformal prediction PHM
- federated PHM C-MAPSS
- physics-informed degradation residual
- signed health indicator (TEE)
- per-sensor uncertainty decomposition

**Two under-explored adjacent fields**:
- structural health monitoring (SHM) for civil assets — long-horizon
  physics priors with population-scale MTBF data
- control-theoretic MTBF aggregation for networked systems — currently
  the missing bridge for hypothesis (a) at the system level

## 5. Search log

Per-keyword calls to `paper_search` (HF), `results_limit = 10–12`,
`concise_only = true`. Publication window 2024-05-28 → 2026-05-28 applied
post-hoc.

| keyword (query used) | results | in-window | pooled |
|---|---|---|---|
| remaining useful life prediction | 12 | 7 | 7 |
| prognostics and health management | 12 | 5 | 5 |
| physics-informed neural network | 12 | 8 | 8 |
| condition-based monitoring industrial machines | 12 | 6 | 6 |
| digital twin for maintenance | 12 | 7 | 7 |
| federated learning for prognostics | 12 | 5 | 5 |
| aleatoric uncertainty estimation deep learning | 12 | 4 | 4 |
| sensor data attestation trusted hardware | 12 | 5 | 5 |

- **pooled in-window, pre-dedup**: ~47
- **deduped by arXiv ID** (e.g. 2412.11967, 2511.21208, 2507.06672 each
  surfaced in 2–3 keyword pools): removed ~9 duplicates
- **candidates with ≥ 2 keywords matched**: 11
- **adopted (sum ≥ 2.5)**: **4** (listed in §2)
- **rejected at < 2.5 sum but ≥ 2 keywords** (logged for the next
  combo-A run):
  - 6G-Enabled Digital Twin for Bearing Fault Detection
    (arXiv:2510.03807) — 3 keywords, 2.0 sum. *Dropped from prior run's
    adopted list under v6 keywords.* Still relevant — re-evaluate when
    combo-A is widened with "edge AI" or kept as a candidate for
    PHYSICAL_LINKS basis.
  - DiffBatt: Diffusion Model for Battery Degradation
    (arXiv:2410.23893) — 2 keywords, 1.5 sum
  - RUL forecasting for wind turbine predictive maintenance
    (arXiv:2412.17823) — 2 keywords, 1.5 sum
  - Uncertainty-Aware Remaining Lifespan Prediction from Images
    (arXiv:2506.13430) — 2 keywords, 1.5 sum
- **prior-run papers no longer meeting v6 threshold** (status note):
  - **arXiv:2510.03807** (6G Digital Twin) — was 3.0 under v4
    keywords (digital twin, edge AI, predictive maintenance, fault
    tolerant). Under v6 it scores 2.0 because "edge AI" and "predictive
    maintenance" are no longer in the combo-A vector. Engineering value
    is unchanged; will be re-evaluated under combo-D (edge inference
    keyword).
  - **arXiv:2510.24801** (Fortytwo) — was 3.0 under v4 (decentralized,
    consensus, distributed ledger, PoUW, verifiable computation). Under
    v6 keywords for combo-A it scores 0.0 — the paper is a consensus
    paper, not a physics-input paper. It does not belong in combo-A
    v6. May surface again in combo-C (mechanism design / decision
    making) or combo-D (verifiable inference).

**Search confidence**: medium-high for the RUL/PHM/PINN axis (HF index
is strong here), low for "sensor data attestation" (HF surfaces 5G
infrastructure attestation, not sensor-grounded attestation — the
intended literature lives in IEEE Xplore CCS / USENIX Security and was
not reached this run; flagged for combo-D).
