# combo-A — Physics input → consensus input

System role: turn raw sensor streams into health / fault / RUL estimates
that the upstream layers can consume as inputs. This combo only catalogues
the *bottom* of the pipeline (sensor → calibrated indicator). It does not
yet wire the indicator into a vote.

## 0. Run metadata

- **run_date**: 2026-04-30
- **search_window**: 2024-04-30 → 2026-04-30 (last 2 years)
- **prior_run**: 2026-04-18 (v4, dir was `combo-A-physics-consensus`).
  Prior run mixed L1 (physics) and L3 (consensus) into a single combo;
  v6 splits them — consensus mechanics now live in combo C.
- **routine version**: v6
- **primary tool**: Hugging Face `paper_search` (semantic). Per-keyword
  calls, pooled, scored against the v6 keyword list.
- **fallback tools used**: none required at this stage. arXiv direct
  retained as backup.

## 1. Executive summary

The v6 split of combo A (sensor → calibrated indicator) is well populated
in arXiv literature from the last 2 years. PINN-based health monitors
remain the strongest "physics-prior" route to a labelled-data-light
indicator, while uncertainty-aware RUL prediction is converging on
aleatoric/epistemic decomposition as a standard reporting format. A new
result (I-GLIDE, Nov 2025) explicitly produces *grouped, uncertainty-tagged*
health indicators for multi-sensor systems — which is exactly the shape
the upper layers want to consume. **Federated-learning-for-prognostics**
returned no in-window hit specific to PHM (only healthcare FL); recorded
as 근거 부족. **Sensor data attestation** returned hits about TPM-attested
5G workloads but not sensor-stream attestation; also 근거 부족 — this is a
real gap and is deferred to combo D under `remote attestation edge`.

## 2. Adopted papers (≥ 2 keyword matches *or* ≥ 2.5 score)

### 2.1 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint (cs.LG)
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords** (v6):
  - `remaining useful life prediction` — full ("RUL prediction" in
    abstract; RUL is the standard PHM abbreviation) = **1.0**
  - `aleatoric uncertainty estimation` — full ("aleatoric uncertainty"
    + "epistemic uncertainty" + Monte Carlo dropout reported) = **1.0**
  - `prognostics and health management` — partial ("prognostics" used
    explicitly; framework positioned as a PHM tool) = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: A degradation-indicator framework combining Reconstruction
    along Projected Pathways (RaPP) with grouped sensor inputs and
    uncertainty quantification (aleatoric + epistemic via MC dropout)
    over probabilistic latent spaces.
  - **결과**: Improves both RUL prediction accuracy and interpretability
    on multi-sensor benchmarks; per-input-group health indicators are
    individually inspectable.
  - **한계**: Standard turbofan-class benchmarks; no online / streaming
    deployment study; group definition is a hyperparameter chosen by
    domain knowledge, not learned.
- **system reduction**: Justifies the *output contract* of the L1
  reliability node: `health_indicator(window) → (score_per_group,
  aleatoric_var, epistemic_var)`. The grouped form maps cleanly to
  per-subsystem confidence values, so a downstream aggregator can
  weight votes by epistemic variance instead of a flat reputation
  scalar.
- **[NEW]**: yes (v6).

### 2.2 CARLE: A Hybrid Deep-Shallow Learning Framework for Robust and Explainable RUL Estimation of Rolling Element Bearings

- **authors**: Waleed Razzaq, Yun-Bo Zhao
- **year**: 2025 (Oct 10)
- **venue**: arXiv preprint
- **arxiv**: 2510.17846 · https://hf.co/papers/2510.17846
- **matched_keywords** (v6):
  - `prognostics and health management` — full ("prognostic health
    management" in keywords, "PHM" framing) = **1.0**
  - `remaining useful life prediction` — full ("RUL estimation" — RUL =
    remaining useful life; estimation/prediction interchangeable in
    PHM literature) = **1.0**
  - `condition-based monitoring` — partial ("robustness… under varying
    operating conditions" — adjacent but not the standard CBM phrase)
    = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Hybrid pipeline: Continuous Wavelet Transform + Gaussian
    filtering for signal cleaning; Res-CNN/Res-LSTM + multi-head
    attention as the deep stage; Random Forest Regressor as the shallow
    head; residual connections throughout.
  - **결과**: Reports robustness and explainability gains for RUL
    estimation of rolling-element bearings under varying operating
    conditions, vs. pure deep baselines.
  - **한계**: Bearings only; no transfer to dissimilar machinery; no
    uncertainty quantification (so combines weakly with I-GLIDE).
- **system reduction**: Justifies a CBM front-end module —
  `cwt_features(raw_vibration) → tensor` — as the first compute step in
  the L1 node. The Random-Forest tail is a small ablation point: lets
  us swap a noisy LSTM regressor for a calibrated, low-variance head
  on resource-constrained hardware.
- **[NEW]**: yes (v6).

### 2.3 A Digital Twin for Diesel Engines: Operator-infused Physics-Informed Neural Networks with Transfer Learning for Engine Health Monitoring

- **authors**: Kamaljyoti Nath, Varun Kumar, Daniel J. Smith, George Em Karniadakis
- **year**: 2024 (Dec 16)
- **venue**: arXiv preprint
- **arxiv**: 2412.11967 · https://hf.co/papers/2412.11967
- **matched_keywords** (v6):
  - `physics-informed neural network` — full = **1.0**
  - `digital twin for maintenance` — partial ("Digital Twin for Diesel
    Engines… Engine Health Monitoring" — maintenance is the application
    framing; the standard phrase "for maintenance" is not present)
    = **0.5**
  - `prognostics and health management` — partial ("engine health
    monitoring" maps to PHM application; abstract does not use term
    PHM) = **0.5**
  - count = 3, total = **2.0**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Operator-infused PINN (uses DeepONet) trained on a
    mean-value diesel engine model; multi-stage and few-shot transfer
    learning to unseen operating regimes.
  - **결과**: Engine parameter identification and health indicators
    generalise better than data-driven baselines, at lower compute.
  - **한계**: Simulated engine; cross-engine transfer and noisy-sensor
    online operation not yet established.
- **system reduction**: Justifies the **physics-prior residual** as the
  first callable inside the L1 node. Concretely, the indicator is a
  residual against a known mean-value engine model, so the L1 node only
  needs O(10²) parameters to store the prior — not a full data-driven
  model. Carry-over from v4.
- **[NEW]**: no (carry-over from v4 run 1; matches the v6 keyword list
  with score 2.0 ≥ 2 keywords).

### 2.4 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025 (Jul 09)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords** (v6):
  - `remaining useful life prediction` — full ("Remaining Useful Life
    Prediction" in title) = **1.0**
  - `aleatoric uncertainty estimation` — partial ("aleatoric uncertainty"
    used as a latent indicator, but the paper doesn't use the strict
    phrase "estimation") = **0.5**
  - `prognostics and health management` — partial ("health indicator"
    used in title) = **0.5**
  - count = 3, total = **2.0**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Variational autoencoder + RaPP latent reconstruction;
    aleatoric and epistemic uncertainty extracted from the latent space
    are themselves used as additional features for the RUL head.
  - **결과**: On NASA C-MAPSS turbofan, uncertainty-as-feature improves
    RUL accuracy over both classical autoencoder baselines and direct
    end-to-end models.
  - **한계**: Single dataset; no real-time / on-edge ablation.
- **system reduction**: Justifies a *non-trivial* design choice for the
  L1 → L3 link: the L1 node should expose the *uncertainty itself* as a
  field, not just `(score, std)`. This is a different output than I-GLIDE
  uses and gives the upper layer richer signal for vote weighting.
- **[NEW]**: yes (v6).

## 3. Hypothesis sub-score (1–5)

Per-paper "system part value" (not direct hypothesis support):

| paper | sub-hyp it relates to | score | reason |
|---|---|---|---|
| I-GLIDE (2511.21208) | (a) reliability + (c) measurement-as-input | 4 | exposes per-group uncertainty — the cleanest input format for the consensus layer |
| CARLE (2510.17846) | (a) reliability | 3 | strong CBM front-end, no UQ |
| PINN engine (2412.11967) | (a) reliability | 3 | physics-prior + small data — minimum-training-cost route |
| UQ-Latent (2507.06672) | (a) reliability + (c) | 4 | proposes that uncertainty *is* a feature — exactly the format the upper layer needs |

**Combo A v6 aggregate**: the L1 indicator interface is now well-attested
as a 4-tuple `(score, group_score[], aleatoric_var, epistemic_var)`. This
is enough to specify the L1 → L3 contract on paper. End-to-end
attestation (sensor authenticity) remains absent in the surveyed
literature — recorded as gap, deferred to combo D.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (next combo-A run or for combo D pickup):**
1. `remote attestation edge` — covers the gap that "sensor data attestation" left.
2. `signed health indicator` — combo D / combo A bridge.
3. `online RUL streaming` — closes "no real-time deployment" gap on the adopted papers.
4. `cross-engine transfer prognostics` — tests whether PINN-engine indicators generalise.
5. `concept drift PHM` — when the physical asset itself shifts mode.

**Two unexplored adjacent fields:**
- **Structural Health Monitoring (SHM) for civil assets** — long-horizon
  physics priors, near-analog to PHM at different sampling cadence.
- **Battery RUL with electrochemical priors** — distinct physics-prior
  family from mechanical PHM; tests whether the `(score, ε_a, ε_e)`
  contract survives a different domain.

## 5. Search log

| keyword (query used) | results | in-window | adopted from this query |
|---|---|---|---|
| remaining useful life prediction prognostics deep learning | 12 | 4 | I-GLIDE, CARLE, UQ-Latent (cross-listed) |
| physics-informed neural network fault detection condition monitoring | 12 | 1 | (PINN engine via separate query) |
| digital twin predictive maintenance industrial | 12 | 4 | PINN-engine 2412.11967 |
| federated learning prognostics health management | 12 | 0 in-PHM | none — 근거 부족 |
| aleatoric epistemic uncertainty estimation regression | 12 | 6 | 0 net new |
| sensor data attestation remote attestation IoT | 12 | 1 | none — 근거 부족 (TPM/VNF only) |
| condition-based monitoring vibration bearing fault | 10 | 2 | 0 net new |

- **pooled in-window (pre-dedup)**: ~18
- **dedup by arXiv ID**: 4 cross-query duplicates removed
- **scored ≥ 2 keywords**: 4
- **adopted (final)**: **4**
- **rejected at < 2 keywords**:
  - 2412.17823 RUL wind turbine — 1.0 only (no other v6 keyword)
  - 2504.11581 Universal Vibration Dataset — 1.0 only ("predictive
    maintenance" is not a v6 keyword)
  - 2510.03807 6G Digital Twin (v4-adopted) — under v6 only partial
    matches on `digital twin for maintenance` and `condition-based
    monitoring`; total 1.0; excluded under v6 strictness, recommended
    re-evaluation under combo D
  - 2403.13602 Bayesian PINN power — out of window (2024-03 < 2024-04-30)
- **gaps recorded as 근거 부족**:
  - federated learning for prognostics: no in-window arXiv hit specific
    to PHM in the HF index
  - sensor data attestation: TPM/VNF attestation hits are at the
    infrastructure layer, not sensor-stream

**Search confidence**: medium-high on RUL/PHM side, low on attestation
side. The two gaps are genuine and motivate a deliberate combo D
follow-up rather than a wider combo A re-run.
