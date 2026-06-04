# combo-A — Physics Reliability → Consensus Input

System role: produce, at each physical node, a calibrated health/lifetime
estimate (with uncertainty) that the upper layer can consume as a
consensus input. Components must measure → judge a physical residual.

## 0. Run metadata

- **run_date**: 2026-06-04
- **search_window**: 2024-06-04 → 2026-06-04 (last 2 years)
- **prior_run**: 2026-04-18 (v4 combo-A, three papers adopted under
  different scoring; this run re-keys to the v6 list and re-scores)
- **routine_version**: Research Routine v6
- **primary tool**: Hugging Face `paper_search` (semantic, ML-flavoured).
  Per-keyword calls, pooled, scored against the v6 keyword list.
- **fallback**: arXiv via WebSearch (used where HF index thin).

## 1. Executive summary

The v6 keyword list pushes harder on PHM with explicit uncertainty than
v4 did, and that filter selects for a different paper set: latent-health-
indicator models that emit aleatoric/epistemic uncertainty alongside the
RUL estimate now dominate. Three papers clear the ≥ 2 keyword AND ≥ 2.5
score threshold — all on turbofan / rolling-element bearing testbeds,
all 2025. The v4 flagship PINN-diesel-engine paper (2412.11967) drops
below threshold under v6 because PHM is no longer being credited as
partial via "engine health monitoring"; it remains a useful reference
but no longer counts as a v6 adoption. The recurring engineering shape
is "physics-prior or latent reconstruction model + heteroscedastic head"
— the head is the part that maps cleanly onto a consensus input.

## 2. Adopted papers (≥ 2 matches AND ≥ 2.5 score)

### 2.1 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025-11-26
- **venue**: arXiv preprint (under review)
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords**:
  - aleatoric uncertainty estimation (full) = 1.0
  - prognostics and health management (partial via "prognostics") = 0.5
  - remaining useful life prediction (partial via "RUL prediction") = 0.5
  - condition-based monitoring (partial via "degradation estimation
    in multi-sensor systems") = 0.5
  - **Total = 2.5, matches = 4**
- **classification**: [공학]
- **summary**:
  - **방법**: RaPP (Reconstruction along Projected Pathways) with input-
    group partitioning produces probabilistic latent spaces; Monte Carlo
    dropout separates aleatoric vs. epistemic uncertainty per sensor
    group.
  - **결과**: Improves RUL prediction accuracy and interpretability on
    multi-sensor degradation benchmarks; sensor-group-level uncertainty
    surfaces which subsystems drive the prediction.
  - **한계**: Demonstrated on CMAPSS-style simulated turbofan data; no
    online deployment under sensor noise or sensor dropout.
- **system reduction**: Justifies that `l1-reliability` node should
  expose `health_indicator(sensor_window) → (score, aleatoric_var,
  epistemic_var)` — not a scalar but a tuple. The per-sensor-group
  decomposition is also directly reducible: each subsystem can publish
  its own indicator with its own variance, which is exactly the shape a
  measurement-weighted consensus (combo-C) consumes.
- **[NEW]**: yes (v6 first adoption).

### 2.2 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025-07-09
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords**:
  - remaining useful life prediction (full) = 1.0
  - aleatoric uncertainty estimation (full — paper names both
    aleatoric and epistemic explicitly) = 1.0
  - prognostics and health management (partial via "prognostics on
    NASA C-MAPSS") = 0.5
  - **Total = 2.5, matches = 3**
- **classification**: [공학]
- **summary**:
  - **방법**: Autoencoder-derived latent health indicator (RaPP) +
    variational-autoencoder uncertainty head, evaluated on NASA C-MAPSS
    turbofan dataset.
  - **결과**: Adding uncertainty quantification to the latent health
    indicator improves RUL prediction accuracy over both classical
    autoencoder baselines and end-to-end RUL models.
  - **한계**: Same dataset family (C-MAPSS) as 2.1; cross-asset
    generalisation not shown; uncertainty calibration evaluated
    indirectly through downstream RUL error.
- **system reduction**: Earlier-stage companion of I-GLIDE from the
  same group. Justifies the *minimum viable* shape of the L1 callable:
  `(score, uncertainty)` is enough, group-decomposition is the upgrade.
- **[NEW]**: yes.

### 2.3 CARLE: A Hybrid Deep-Shallow Learning Framework for Robust and Explainable RUL Estimation of Rolling Element Bearings

- **authors**: Waleed Razzaq, Yun-Bo Zhao
- **year**: 2025-10-10
- **venue**: arXiv preprint
- **arxiv**: 2510.17846 · https://hf.co/papers/2510.17846
- **matched_keywords**:
  - remaining useful life prediction (full) = 1.0
  - prognostics and health management (full — paper title says
    "prognostic health management") = 1.0
  - condition-based monitoring (partial via bearing condition
    monitoring application) = 0.5
  - **Total = 2.5, matches = 3**
- **classification**: [공학]
- **summary**:
  - **방법**: Res-CNN + Res-LSTM with multi-head attention extracts deep
    features; a Random Forest regressor head produces the RUL estimate.
    Continuous Wavelet Transform + Gaussian filtering preprocess
    vibration.
  - **결과**: Robust RUL estimation across varying operating conditions
    on rolling-element bearing benchmarks; explanation is provided
    through feature-importance of the shallow head.
  - **한계**: No uncertainty estimate exposed; RF head gives point
    predictions only, which is a problem if this is to feed an
    uncertainty-weighted consensus.
- **system reduction**: Useful as a *baseline* for the L1 indicator on a
  different physical asset (bearings vs. turbofan). The lack of an
  uncertainty head is the gap — combining the CARLE feature extractor
  with the I-GLIDE-style uncertainty head is a candidate (task b)
  reduction for a later run.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | 3 | PHM models now reliably emit calibrated uncertainty on the canonical turbofan/bearing benchmarks; jump from 2 in v4 is driven by uncertainty being native, not bolted-on. |
| (b) Surplus absorbs non-essential wants | — | out of scope (combo-B). |
| (c) Consensus derivable from measurement | 2 | Calibrated per-node uncertainty is now available, but nothing in combo-A wires it into a vote weight. The gap is exactly the combo-C bridge. |

**Aggregate**: combo-A under v6 is stronger on (a) than v4 was, because
uncertainty is now a *native output* of the surveyed models rather than
a downstream concern. The (a)→(c) bridge is still the open design
problem and is correctly delegated to combo-C.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (to feed a later combo-A or combo-D run):**
- heteroscedastic regression for degradation
- calibration of RUL uncertainty
- cross-asset transfer of PHM models
- vibration signal foundation model
- physics-residual + uncertainty head

**Two under-explored adjacent fields:**
- Structural health monitoring (SHM) for civil assets — long-horizon
  physics priors, near-analog to PHM but with different sensor
  modalities.
- Battery state-of-health (SOH) estimation — uncertainty literature
  there is mature and worth cross-reading.

## 5. Search log

Per-keyword calls to `paper_search` (HF), 10 results each, then
in-window filter (2024-06-04 → 2026-06-04) applied post-hoc.

| keyword | results | in-window | notable |
|---|---|---|---|
| remaining useful life prediction | 10 | 6 | 2507.06672, 2511.21208, 2510.17846 |
| prognostics and health management deep learning | 10 | 1 | 2510.17846 (mostly medical false positives) |
| physics-informed neural network | 10 | 2 | 2506.00731, 2602.01176 (general PDE, no PHM application) |
| condition-based monitoring fault prognosis | 10 | 3 | 2511.21208, 2510.17846, 2511.22133 |
| digital twin for predictive maintenance | 10 | 2 | 2510.03807, 2601.01321 |
| federated learning for prognostics | 10 | 0 | search returned general FL, no PHM crossover in window |
| aleatoric uncertainty estimation | 10 | 6 | 2511.21208, 2509.13262, 2603.10745 |
| sensor data attestation | 10 | 3 | 2510.03219 (TPM/Keylime), 2511.17692, 2605.19233 — useful for combo-D, single-match for A |

- pooled in-window, pre-dedup: ~23
- after DOI/title dedup: ~17
- candidates with ≥ 2 matches: 5
- adopted (≥ 2.5 score AND ≥ 2 matches): **3** (above)
- notable rejections:
  - **arXiv:2412.11967** (PINN diesel-engine, v4 adoption) —
    physics-informed neural network 1.0 + digital twin 0.5 + PHM 0.5 =
    2.0. Below v6 threshold. Stays in `candidate-advisors.md` but no
    longer a v6-adopted paper.
  - **arXiv:2510.03807** (6G digital twin bearing fault) —
    digital twin 0.5 + condition-based 0.5 + PHM 0.5 = 1.5. Below.
    Demoted to "engineering reference" only.
  - **arXiv:2511.22133** (probabilistic digital twin with Bayesian NN)
    — digital twin 0.5 + aleatoric UQ 0.5 = 1.0. Below.

**Search confidence**: medium-high for the PHM+UQ subdomain (the HF
index covers it well). Low for `sensor data attestation` and `federated
learning for prognostics` as adopted-for-combo-A signals — those are
better pursued in combo-D and a future combo-A re-entry.
