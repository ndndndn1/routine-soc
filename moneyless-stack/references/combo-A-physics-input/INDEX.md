# combo-A — Physics Reliability → Consensus Input

System role: produce calibrated fault/RUL/health estimates from sensors
that the upper layer can ingest as a vote weight.

## 0. Run metadata

- **run_date**: 2026-04-19
- **search_window**: 2024-04-19 → 2026-04-19 (last 2 years)
- **prior_run**: combo-A-physics-consensus (run 1, 2026-04-18). v6
  rebaseline: keyword set narrowed to RUL / PHM / PINN / CBM / DT-for-
  maintenance / FL-for-prognostics / aleatoric UQ / sensor attestation.
- **routine_version**: v6
- **task**: (a) search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic). Per-keyword
  calls, pooled, dedup, scored.

## 1. Executive summary

The v6 rebaseline of combo-A produces a tighter cluster than run 1: the
strongest signal is the joint occurrence of **uncertainty-quantified
RUL prediction** with PHM-domain datasets (turbofan, bearings). Three
papers clear the ≥ 2.5 / ≥ 2 keyword threshold and they all converge
on the same interface: a learned health indicator that emits both a
point estimate and an aleatoric/epistemic uncertainty pair. None of
them targets sensor-level data attestation — that keyword returned
infrastructure-grade attestation work (TPM/Keylime) but no sensor-side
construction. The bridge from "calibrated indicator" to "signed
indicator" remains unattested and is now the most concrete L1→L3 gap.
Federated learning for prognostics produced no in-window adoptable
hits; condition-based monitoring matched only as background context.
PINN papers are abundant but mostly target PDE solving rather than
maintenance — adoptable PINN-for-PHM papers were not found in this run.

## 2. Adopted papers (≥ 2 matches AND sum ≥ 2.5)

### 2.1 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025 (Jul 9)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords**:
  - `remaining useful life prediction` — **1.0** (full phrase in title)
  - `aleatoric uncertainty estimation` — **1.0** (paper estimates
    aleatoric + epistemic uncertainty as the central contribution;
    "aleatoric uncertainty" present verbatim in keywords)
  - `prognostics and health management` — **0.5** (NASA C-MAPSS
    turbofan dataset is the canonical PHM benchmark; "health
    indicator" partial of PHM)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Autoencoder-based latent health indicator with
    Reconstruction-along-Projected-Pathways (RaPP); aleatoric and
    epistemic uncertainty propagated through a variational head into
    the RUL regressor.
  - **[결과]** On NASA C-MAPSS turbofan, the uncertainty-augmented
    indicator improves RUL accuracy over end-to-end baselines and
    yields a calibrated confidence band per prediction.
  - **[한계]** Single-domain (turbofan), no on-device evaluation, no
    discussion of how the uncertainty pair would be consumed downstream.
- **system reduction**: Justifies the `l1-reliability` node's primary
  output being a `(rul_estimate, aleatoric, epistemic)` tuple rather
  than a scalar. The split is what lets L3 weight the vote — this
  paper supplies the empirical case for "two-channel" output.

### 2.2 CARLE: A Hybrid Deep-Shallow Learning Framework for Robust and Explainable RUL Estimation of Rolling Element Bearings

- **authors**: Waleed Razzaq, Yun-Bo Zhao
- **year**: 2025 (Oct 10)
- **venue**: arXiv preprint
- **arxiv**: 2510.17846 · https://hf.co/papers/2510.17846
- **matched_keywords**:
  - `prognostics and health management` — **1.0** ("prognostic health
    management" in keywords; singular/plural equivalence per matching
    rule)
  - `remaining useful life prediction` — **1.0** ("RUL Estimation" in
    title; "remaining useful life" in keywords)
  - `condition-based monitoring` — **0.5** (rolling-element bearings
    under varying operating conditions; CBM is the implicit deployment
    context)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Res-CNN + Res-LSTM with multi-head attention extract
    deep features; a Random Forest regressor on those features
    produces the explainable RUL output. CWT preprocessing.
  - **[결과]** Higher robustness and generalisation across operating
    conditions than pure-deep baselines; explainability via the RF
    leaf attribution.
  - **[한계]** Bearings only; no uncertainty calibration; no edge
    deployment numbers.
- **system reduction**: Provides a fallback architecture for the
  `l1-reliability` node when training-set diversity is low — the
  deep-shallow split is implementable in <100 LoC and gives an
  interpretable indicator. Pairs with paper 2.1 by supplying the
  point estimate where 2.1 supplies the uncertainty pair.

### 2.3 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords**:
  - `aleatoric uncertainty estimation` — **1.0** (aleatoric +
    epistemic uncertainty are central; Monte-Carlo dropout used as
    estimator)
  - `remaining useful life prediction` — **1.0** ("RUL prediction"
    is the headline task)
  - `prognostics and health management` — **0.5** ("prognostics" in
    keywords; "anomaly detection" + multi-sensor systems)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Extends RaPP with input grouping ("indicator groups")
    so that latent health indicators are computed per sensor cluster;
    aleatoric/epistemic uncertainty estimated with MC-dropout per
    group.
  - **[결과]** Both RUL accuracy and interpretability improve over
    flat RaPP because failures are localised to specific input groups.
  - **[한계]** Group definition is hand-designed; no automatic
    grouping criterion; benchmarks limited to the same C-MAPSS family
    as 2.1.
- **system reduction**: Justifies the `l1-reliability` node carrying
  *per-subsystem* indicators rather than one scalar per node. Direct
  feed into L3: each subsystem indicator can vote with its own weight.
  This paper is the first to implement the "fan-out" the routine needs.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability of production infra is high enough | 2 | RUL/PHM literature gives device-scale calibrated estimators; system-scale MTBF still absent. |
| (b) surplus absorbed by non-essential wants | — | out of combo-A scope. |
| (c) consensus weights derive from physical measurements | 2 | A calibrated `(estimate, uncertainty)` pair is now well-attested at the *node* level; the link from there to a vote weight is *not* covered by any combo-A paper. |

**Aggregate**: combo-A (v6) confirms the L1 input-shape — every node
can produce `(value, uncertainty)` from sensors using PHM-grade
methods. Does not bridge to L3 by itself. Open: who signs the
indicator at the sensor.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (next combo-A re-entry):**
- conformal prediction RUL
- per-sensor uncertainty decomposition
- signed health indicator
- RUL distribution shift
- PINN-based bearing model

**Two under-explored adjacent fields:**
- Structural health monitoring (SHM) for civil assets — strong physics
  priors, long-horizon ground truth, currently sparse on HF index.
- Reliability-physics MTBF aggregation across heterogeneous nodes —
  needed for the (a) sub-hypothesis but absent in this run.

## 5. Search log

Per-keyword `paper_search` calls, ≤ 12 results each.

| keyword (query used) | results | in-window | notes |
|---|---|---|---|
| remaining useful life prediction | 12 | 7 | core hits cluster on C-MAPSS / battery / wind |
| prognostics and health management deep learning | 12 | 1 | most hits are *medical* PHM (off-topic), 1 industrial |
| physics-informed neural network | 12 | 9 | abundant but PDE-solving, none for maintenance |
| condition-based monitoring machinery | 12 | 7 | mostly anomaly detection / vibration |
| digital twin for maintenance industrial | 12 | 5 | covered already in run 1 (combo-A-physics-consensus 2510.03807) |
| federated learning prognostics fault diagnosis | 12 | 6 | all general FL, none on prognostics specifically |
| aleatoric uncertainty estimation | 12 | 5 | strong for vision / NeRF, weak for PHM |
| sensor data attestation integrity | 12 | 4 | TPM/Kubernetes/IMA — none at the *sensor* layer |

- **pooled after in-window filter, pre-dedup**: ~44
- **dedup by arXiv ID + title-normalised**: ~9 duplicates removed
  (2507.06672, 2510.17846, 2511.21208 each appeared in 2–3 queries;
  2510.03807 carried over from run 1 and excluded as already adopted)
- **scored ≥ 2 keywords**: 8 candidates
- **scored ≥ 2.5 sum AND ≥ 2 keywords (adopted)**: **3** (above)
- **rejected at < 2.5**: 2412.17823 (RUL wind turbine, sum 1.5),
  2410.23893 (DiffBatt battery, 1.0), 2504.11581 (vibration analysis
  dataset, 1.0), 2504.19013 ($PINN Bayesian, 1.5), 2509.13262
  (Split-Point UQ, 1.0), 2510.03219 (TPM remote attestation, 0.5).

**Search confidence**: medium. The HF index covers PHM-flavoured ML
well but is thin on the sensor-side attestation literature the routine
asked for; "근거 부족" recorded for `sensor data attestation` and
`federated learning for prognostics` — neither produced an adoptable
candidate this run.
