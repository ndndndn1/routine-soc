# combo-A — physical reliability → consensus input

## 0. Run metadata

- **run_date**: 2026-04-24
- **search_window**: 2024-04-24 → 2026-04-24 (strict 2-year)
- **prior_run**: run 1 (2026-04-18) under routine v4 keyword set
  (`physics-informed predictive maintenance`, `DePIN`, `verifiable
  computation`, …). That run adopted three papers: 2412.11967,
  2510.03807, 2510.24801.
- **routine**: v6 — combo keyword set reduced to 8 standard academic
  terms, adoption threshold ≥ 2 keyword matches and ≥ 2.5 sum.
- **task**: (a) re-survey under v6 keyword list.
- **primary tool**: Hugging Face `paper_search` (semantic), per-keyword
  calls, pooled, deduplicated by arXiv ID.

## 1. Executive summary

Under v6 the combo-A keyword list narrows to concrete PHM mechanisms
plus sensor-attestation. Five papers clear the ≥ 2.5 threshold, three
of them (I-GLIDE, CARLE, Thil et al. 2507.06672) new relative to run 1.
The recurring signal is the coupling of a Remaining-Useful-Life
estimator with aleatoric-uncertainty output, which is the shape of
signal the stack needs from the "L1 reliability" node: a
`(score, uncertainty)` tuple, not a point estimate. Of run 1's
adoptions, 2412.11967 clears again cleanly, 2510.03807 drops to 1.5
(it was adopted under v4's broader "digital twin" / "edge AI" pair —
v6 treats these more strictly), and 2510.24801 (Fortytwo) does not
match any combo-A keyword and is orphaned under v6 — noted in
synthesis.md. **No paper attests sensor-data attestation grounded in
physical measurement**; that keyword remains unfilled and the L1→L3
bridge remains a design gap.

## 2. Adopted papers (≥ 2 keywords, sum ≥ 2.5)

### 2.1 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords**:
  - `remaining useful life prediction` — 1.0 (explicit: "RUL prediction")
  - `aleatoric uncertainty estimation` — 1.0 (explicit: "aleatoric
    and epistemic uncertainty quantification (UQ) via Monte Carlo
    dropout")
  - `prognostics and health management` — 0.5 (partial: "bridges
    anomaly detection and prognostics")
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Reconstruction-along-Projected-Pathways (RaPP) as HI,
    augmented with MC-dropout aleatoric and probabilistic-latent
    epistemic UQ; "indicator groups" isolate sensor subsets per
    degradation mechanism.
  - 결과: Accuracy and generalisation gains on aerospace and
    manufacturing RUL datasets; mechanism-specific diagnostics.
  - 한계: Benchmarked on public RUL datasets; no wired link to any
    downstream consensus layer; UQ calibration vs. out-of-distribution
    bearings not reported.
- **시스템 환원**: Directly supports the L1 `health_indicator` function
  signature `sensor_window → (score, aleatoric, epistemic)`. Indicator
  groups give a sensor-subset ontology that can be carried through
  into a later physical-link manifest (each subset = an independent
  channel with its own uncertainty).
- **[NEW]**: yes.

### 2.2 CARLE: A Hybrid Deep-Shallow Learning Framework for Robust and Explainable RUL Estimation of Rolling Element Bearings

- **authors**: Waleed Razzaq, Yun-Bo Zhao
- **year**: 2025 (Oct 10)
- **venue**: arXiv preprint
- **arxiv**: 2510.17846 · https://hf.co/papers/2510.17846
- **matched_keywords**:
  - `remaining useful life prediction` — 1.0 (explicit)
  - `prognostics and health management` — 1.0 (explicit: "Prognostic
    Health Management (PHM) systems")
  - `condition-based monitoring` — 0.5 (partial: "PHM systems monitor
    and predict equipment health")
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Res-CNN + Res-LSTM + multi-head attention + RFR stacked;
    CWT + Gaussian-filter preprocessing.
  - 결과: Beats SOTA baselines on XJTU-SY and PRONOSTIA; LIME/SHAP
    interpretability.
  - 한계: Bearings only; no uncertainty output; supervised regression
    so failure-labelled data required.
- **시스템 환원**: Backup/ensemble member for the L1 `health_indicator`
  function when the physics-prior path (PINN / RaPP) is unavailable;
  SHAP output is a candidate explanation payload that could travel
  alongside the HI vote into L3.
- **[NEW]**: yes.

### 2.3 Uncertainty Quantification as a Complementary Latent Health Indicator for RUL Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Jul 9)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords**:
  - `remaining useful life prediction` — 1.0 (explicit)
  - `aleatoric uncertainty estimation` — 1.0 (explicit: "separating
    aleatoric from epistemic uncertainty")
  - `prognostics and health management` — 0.5 (partial: "predictive
    maintenance")
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Standard + variational autoencoders produce RaPP HIs;
    aleatoric and epistemic uncertainty are threaded into RUL model.
  - 결과: Competitive / SOTA on NASA C-MAPSS.
  - 한계: Simulated turbofan dataset; no demonstration on sensor
    streams under drift.
- **시스템 환원**: Precursor to 2.1. Specifies the minimum shape of
  calibrated UQ attached to an HI, usable as a reference for the
  L1 HI contract.
- **[NEW]**: yes.

### 2.4 A Digital Twin for Diesel Engines: Operator-infused PINNs with Transfer Learning

- **authors**: Nath, Kumar, Smith, Karniadakis
- **year**: 2024 (Dec 16)
- **venue**: arXiv preprint
- **arxiv**: 2412.11967 · https://hf.co/papers/2412.11967
- **matched_keywords**:
  - `physics-informed neural network` — 1.0 (explicit)
  - `digital twin for maintenance` — 1.0 (explicit: "Digital Twin
    for Diesel Engines ... Engine Health Monitoring")
  - `prognostics and health management` — 0.5 (partial via "engine
    health monitoring")
  - `condition-based monitoring` — 0.5 (partial: model consumes
    actuator + sensor signals for online health)
  - **sum**: 3.0
- **classification**: [공학]
- **system reduction**: Inherited from run 1 — `l1-reliability` node's
  degradation-residual module. Still the strongest candidate for a
  physics-prior HI source.
- **[NEW]**: no — re-adopted from run 1.

### 2.5 Intelligent O&M and Prediction Model Optimization for Wind Power Generation Efficiency

- **authors**: Liu, Wu, He, Gupta
- **year**: 2025 (Jun 19)
- **venue**: arXiv preprint
- **arxiv**: 2506.16095 · https://hf.co/papers/2506.16095
- **matched_keywords**:
  - `condition-based monitoring` — 1.0 (explicit: "condition
    monitoring have significantly enhanced turbine maintenance")
  - `digital twin for maintenance` — 1.0 (explicit: "digital twins ...
    turbine maintenance practices")
  - `prognostics and health management` — 0.5 (partial: "predictive
    maintenance models")
  - **sum**: 2.5
- **classification**: [공학] — qualitative / interview-based, low
  engineering-artifact density, but survives as a *ground-truth
  failure-mode inventory* rather than a method.
- **방법 / 결과 / 한계**:
  - 방법: Structured interviews with five wind-farm O&M engineers;
    thematic analysis.
  - 결과: Identifies failure modes current PHM misses: slow gradual
    faults, integration pain with legacy SCADA, sensor malfunctions,
    false positives.
  - 한계: Not an algorithm, not a dataset. Interview sample size 5.
- **시스템 환원**: Constrains the L1 HI API: must expose both a
  "detected-false-alarm" counter and a "slow-drift warning" channel,
  because these are the two named failure modes where current PHM is
  weak. Motivates aleatoric-only vs. epistemic-+-aleatoric split
  in the HI return type.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5, components-for-hypothesis basis)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability high enough that a node's output can be trusted as a consensus input | 3 | PINN + RaPP + UQ RUL stack is now reproducible across multiple domains (turbofan, bearing, engine). The HI → (score, uncertainty) contract is attested. |
| (b) surplus absorption | — | out of scope for combo-A. |
| (c) measurement-direct priority | 1 | None of the five papers signs or attests its HI output. The "sensor-data-attestation" keyword returned no in-combo matches. |

**Aggregate**: combo-A is moving from "plausible" (run 1) to
"demonstrable" for the calibrated-HI primitive, but **the gap between
a calibrated HI and a cryptographically trustable HI is unchanged from
run 1**.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (re-enter next combo-A run or combo-D):**
- signed health indicator
- attested RUL output
- hardware-root-of-trust for PHM
- OOD detection for PHM
- CMAPSS-to-field transfer

**Two under-explored adjacent fields:**
- Structural health monitoring (SHM) for civil assets — long-horizon
  physics priors, a near-analog to rotating-machinery PHM.
- Formal verification of neural degradation models — an inroad into
  the "can we attest an HI" gap.

## 5. Search log

| keyword (query used) | returned | in-window | pooled | ≥ 2.5 |
|---|---|---|---|---|
| remaining useful life prediction prognostics | 12 | 8 | 8 | 3 |
| physics-informed neural network condition monitoring | 12 | 4 | 4 | 1 |
| digital twin predictive maintenance industrial | 12 | 4 | 4 | 2 |
| condition-based monitoring machinery deep learning | 10 | 5 | 5 | 2 |
| federated learning prognostics health management | 10 | 3 | 3 | 0 (all drift to healthcare FL, not PHM) |
| aleatoric uncertainty estimation deep learning | 10 | 3 | 3 | 1 |
| sensor data attestation trusted integrity | 10 | 2 | 2 | 0 (papers target compute-node attestation, not sensor-to-HI) |

- pooled after in-window filter, pre-dedup: ~29
- dedup: removed ~5 cross-keyword duplicates (I-GLIDE, Thil 2507, CARLE
  and 2412.11967 all surfaced in 2+ queries — expected given the
  intentional overlap of combo-A keywords).
- adopted (≥ 2.5): **5**
- rejected at < 2.5 but ≥ 2.0: 2510.03807 (1.5, re-scored from run 1),
  2412.17823 (1.5, RUL wind turbine), 2510.24801 (0 under v6,
  Fortytwo — orphaned).

**Search confidence**: medium-high. HF index is strong on ML-flavoured
PHM; the "sensor-data-attestation" axis is sparse there and is the
correct place to escalate to IEEE Xplore / embedded-security venues
on the next combo-A run.
