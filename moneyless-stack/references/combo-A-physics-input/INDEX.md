# combo-A — Physics Reliability → Consensus Input

System role: take sensor-derived fault / RUL / health estimates and make
them usable as an input to a higher consensus layer. The bricks we want
are the ones that produce a calibrated `(score, uncertainty)` from a
sensor window.

## 0. Run metadata

- **run_date**: 2026-05-14
- **search_window**: 2024-05-14 → 2026-05-14 (last 2 years)
- **prior_run**: 2026-04-18, recorded under
  `combo-A-physics-consensus/INDEX.md`. That run used a wider, more
  ML-flavoured keyword set ("digital twin industrial system",
  "DePIN…"). v6 narrows combo-A to the strictly standard PHM/PINN/UQ
  vocabulary; that re-scoping changes which papers clear the threshold.
- **routine version**: v6
- **task**: combo search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic). Per-keyword
  calls, pooled, deduplicated by arXiv ID, scored by phrase match.
- **fallback tools (not used)**: arXiv direct, Semantic Scholar,
  Google Scholar. HF pool was sufficient to saturate the v6 keyword
  set; further calls would not have changed the adoption decisions.

## 1. Executive summary

The v6 combo-A keyword set ("remaining useful life prediction",
"prognostics and health management", "physics-informed neural network",
"condition-based monitoring", "digital twin for maintenance", "federated
learning for prognostics", "aleatoric uncertainty estimation", "sensor
data attestation") was searched against the HF paper index. Pool after
dedup: ~22 unique papers in window. The dominant pattern is that
RUL / PHM and aleatoric-uncertainty literatures have started to merge:
"latent health indicator + UQ" is now treated as one technique, not
two. That convergence is exactly what the routine wants for the
sensor→consensus bridge — a node should expose `(score, σ)` rather than
a bare classification. Two papers clear the 2.5 threshold; both are
from the same group (Thil et al.) and they explicitly couple RUL
prediction with aleatoric/epistemic uncertainty on standard PHM
benchmarks. **None** of the surveyed papers attests sensor output at
the source — `sensor data attestation` returned only generic TPM /
TEE work without a measurement binding. The "signed health indicator"
construct flagged as open by run 1 is still open.

## 2. Adopted papers (matched_keywords ≥ 2 AND score ≥ 2.5)

### 2.1 Uncertainty Quantification as a Complementary Latent Health Indicator for Remaining Useful Life Prediction on Turbofan Engines

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Florent Doquet
- **year**: 2025 (Jul 09)
- **venue**: arXiv preprint
- **arxiv**: 2507.06672 · https://hf.co/papers/2507.06672
- **matched_keywords**:
  - "remaining useful life prediction" (1.0 — exact phrase in title)
  - "aleatoric uncertainty estimation" (1.0 — "aleatoric uncertainty"
    listed as core keyword; "estimation" implied by the UQ task)
  - "prognostics and health management" (0.5 — health indicator on
    NASA C-MAPSS, the canonical PHM benchmark, but the literal phrase
    "PHM" is not used)
  - **Total: 2.5** · 3 keywords matched
- **classification**: [공학]
- **방법**: An autoencoder produces a latent health-indicator on the
  NASA C-MAPSS turbofan dataset. The reconstruction error is enriched
  with explicit aleatoric and epistemic UQ via a variational
  autoencoder backbone, and the resulting two-channel `(health, σ)`
  signal feeds a downstream RUL regressor.
- **결과**: Adding the UQ channel beats both classical autoencoder
  health indicators and end-to-end RUL networks on C-MAPSS metrics,
  with the uncertainty channel itself carrying predictive signal
  rather than acting as noise.
- **한계**: Single benchmark (turbofan), single failure mode.
  Uncertainty is well-calibrated on the test split but no operational
  drift test. UQ is on the indicator, not on the eventual RUL number
  delivered to a downstream system.
- **시스템 환원**: Justifies the `l1-reliability` node exposing
  `health_indicator(sensor_window) → (score, uncertainty)` as its
  *only* outbound API. The aleatoric/epistemic split is what the
  consensus layer needs in order to down-weight a noisy node without
  silencing it. Same primitive flagged in run 1's open-work item #1,
  now with a second, independent literature anchor.
- **[NEW]**: yes (within v6 combo-A; conceptually adjacent to run 1's
  2412.11967 but lower in the stack — operates on the *indicator*,
  not the physics prior).

### 2.2 I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation

- **authors**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **year**: 2025 (Nov 26)
- **venue**: arXiv preprint
- **arxiv**: 2511.21208 · https://hf.co/papers/2511.21208
- **matched_keywords**:
  - "remaining useful life prediction" (1.0 — "RUL prediction" in AI
    keywords; singular/plural and abbreviation tolerated)
  - "aleatoric uncertainty estimation" (1.0 — "aleatoric uncertainty,
    epistemic uncertainty, Monte Carlo dropout")
  - "prognostics and health management" (0.5 — explicit "prognostics"
    keyword, missing the "and health management" tail)
  - "condition-based monitoring" (0.5 partial — multi-sensor
    degradation monitoring context, not the literal phrase)
  - **Total: 3.0** · 4 keywords matched
- **classification**: [공학]
- **방법**: Extends the Thil group's RaPP / autoencoder line by
  splitting input sensors into groups, producing per-group latent
  health indicators, and aggregating them with MC-dropout-derived
  uncertainty. Sensors that disagree across groups raise epistemic
  uncertainty; sensors with internal noise raise aleatoric.
- **결과**: Improves RUL prediction accuracy *and* interpretability
  (per-group attribution) over the monolithic latent-indicator
  baseline. Importantly, the multi-group structure is what gives the
  paper its interpretability claim — the consensus question
  "which sensor is lying" can be read off directly.
- **한계**: Still benchmark-only (multi-sensor PHM datasets, no field
  data). Sensor-group decomposition is hand-designed, not learned.
  Group attribution is a per-window snapshot, not a temporal claim.
- **시스템 환원**: Directly maps onto a future `l1-reliability` node
  that emits per-sensor confidence in addition to a fused score —
  exactly the input the routine wants to feed a measurement-weighted
  consensus (open question carried forward from run 1's synthesis).
  Suggests the consensus layer can receive a *vector* of grouped
  `(score_g, σ_g)` rather than a scalar, which is a stronger signal.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5) — partial-credit for parts

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | 2 | PHM+UQ papers show a defensible per-node `(score, σ)` is achievable on benchmarks; system-MTBF claims still absent. Same level as run 1. |
| (b) Surplus absorbs non-essential wants | — | combo-B territory, not scored here. |
| (c) Consensus derived from physical measurement | 2 | UQ-grounded health indicators are the *input* to such a consensus, not the consensus itself. The "uncertainty-weighted vote" link is plausible but unbuilt. Same level as run 1. |

**Aggregate**: combo-A v6 nudges the L1 side from "indicator exists" to
"indicator-with-uncertainty exists", which is a real step but not a
threshold crossing. The bridge into L3 remains an open construction.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (carry into a later combo-A re-entry or combo-D):**
- conformal prediction prognostics
- physics-informed RUL (cross-keyword that returned 0 strong hits
  this run — interesting in itself)
- per-sensor attribution PHM
- calibrated health indicator
- signed sensor output (still open from run 1)

**Two under-explored adjacent fields:**
- Survival analysis for PHM (RULSurv 2405.01614 was a near-miss at
  1.5; the survival-analysis framing of RUL is a different statistical
  basis worth its own pass).
- Structural Health Monitoring (SHM) for civil assets — long-horizon
  physics priors, different sensor modality, surfaced repeatedly in
  the pool but never with enough combo-A overlap to adopt.

## 5. Search log

Per-keyword calls to `paper_search` (HF), 10 results each, in-window
filter (≥ 2024-05-14) applied post-hoc by publication date.

| keyword (query used) | results | in-window | pooled |
|---|---|---|---|
| remaining useful life prediction | 10 | 6 | 6 |
| prognostics and health management deep learning | 10 | 2 | 2 |
| physics-informed neural network fault diagnosis | 10 | 2 | 2 |
| condition-based monitoring machinery | 10 | 3 | 3 |
| digital twin for maintenance industrial | 10 | 4 | 4 |
| federated learning for prognostics | 10 | 3 | 3 |
| aleatoric uncertainty estimation deep learning | 10 | 2 | 2 |
| sensor data attestation authenticity | 10 | 3 | 3 |
| physics-informed remaining useful life uncertainty | 10 | 4 | 4 |
| federated prognostics health management privacy | 10 | 4 | 4 |
| digital twin condition monitoring bearing | 10 | 3 | 3 |
| remote attestation IoT sensor edge | 10 | 5 | 5 |
| condition-based maintenance machine learning sensor | 10 | 4 | 4 |
| prognostics deep learning bearing degradation | 10 | 2 | 2 |
| uncertainty quantification remaining useful life turbofan | 10 | 4 | 4 |
| digital twin predictive maintenance bearing fault | 10 | 3 | 3 |
| physics informed neural network prognostics RUL | 10 | 2 | 2 |

- **pooled after in-window filter, pre-dedup**: ~56
- **dedup (arXiv ID + title-normalised)**: ~22 unique
- **candidates scored ≥ 2.0**: 6
- **candidates scored ≥ 2.5 and adopted**: **2**
- **rejected at 2.0 (recorded so a later run can re-enter)**:
  - 2510.17846 (CARLE) — RUL + PHM both at 1.0, but no third
    standard-vocabulary hit (CBM not explicit).
  - 2504.19013 (Bayesian PINNs with domain decomposition) — PINN +
    aleatoric both 1.0, but the paper is methodological (PDEs), not
    prognostics; the third match is unconvincing.
  - 2510.03807 (6G Digital Twin for Bearing Fault Detection) — three
    partial 0.5s but no full match (digital twin "for maintenance"
    is implied, not literal). Was adopted in run 1 under the looser
    "digital twin industrial system" keyword; v6 is stricter.
  - 2412.17823 (RUL forecasting for wind turbine) — RUL 1.0 +
    predictive-maintenance partial; only 1.5.
  - 2405.01614 (RULSurv) — RUL 1.0 + PHM partial; 1.5.
  - 2602.01176 (Multi-Fidelity PINNs) — PINN 1.0 + aleatoric partial;
    1.5; same methodological-not-prognostic issue as 2504.19013.

- **dropped as out-of-window**: 2211.02842 (Nov 2022), 2310.14949
  (Oct 2023), 2311.18547 (Nov 2023), 2401.01172 (Jan 2024), 2403.00177
  (Feb 2024).

**Search confidence**: medium-high on the PHM/UQ axis (literature is
saturated, same names recurring), low on the `sensor data attestation`
axis (only generic TPM / TEE / remote-attestation work surfaced; the
specific "attest the measurement, not the host" construction the
routine wants is not present in HF's index for this window). Combo-D
is the correct place to follow up on attestation.

**근거 부족 (insufficient evidence)** flagged for:
- "federated learning for prognostics" as a *combined* keyword — most
  results were either pure FL theory or pure PHM, with very little
  in the intersection. Carry forward as a re-scoping note rather than
  an adoption.
