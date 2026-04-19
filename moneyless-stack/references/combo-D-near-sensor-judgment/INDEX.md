# combo-D — Move judgment to the sensor

System role: keep the judgment loop at or near the sensor so that
upward bandwidth, attestation surface, and energy budget all collapse.
Specific hardware methodologies are not the target — the target is
*locating judgment near sensing*.

## 0. Run metadata

- **run_date**: 2026-04-19
- **search_window**: 2024-04-19 → 2026-04-19 (last 2 years)
- **prior_run**: combo-D-physical-ai-substrate (placeholder only).
- **routine_version**: v6
- **task**: (a) search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic), per-keyword
  pooled and scored.

## 1. Executive summary

Combo-D returns a healthier pool than B/C: TinyML and on-device
learning are productive areas on HF, and the ≥ 2.5 / ≥ 2 keyword
threshold is met by **three papers** that together cover the three
sub-mechanisms the routine wants — (i) on-device uncertainty
quantification (QUTE), (ii) on-device LLM execution under a hardware
TEE (TZ-LLM), and (iii) a survey/programme paper that frames sensing
→ action as a single edge loop with neuromorphic fall-back
(Trivedi et al. "Sensing-to-Action"). Energy-harvesting wireless
sensors are present in the pool but mostly reduce to security /
clustering algorithm work — no paper that closes a *judgment loop on
harvested energy* is found. Remote-attestation papers are present
but live at the Kubernetes / TPM layer, not the sensor — same gap as
combo-A. The combo-D adoption set is the strongest of the four
combos in v6 and most directly enables an L1×L3-edge node.

## 2. Adopted papers (≥ 2 matches AND sum ≥ 2.5)

### 2.1 QUTE: Quantifying Uncertainty in TinyML models with Early-exit-assisted ensembles

- **authors**: Nikhil P Ghanathe, Steve Wilton
- **year**: 2024 (Apr 19) — boundary of search window, included
- **venue**: arXiv preprint
- **arxiv**: 2404.12599 · https://hf.co/papers/2404.12599
- **matched_keywords**:
  - `TinyML` — **1.0** (full phrase in title)
  - `on-device uncertainty estimation` — **1.0** ("Quantifying
    Uncertainty in TinyML" is exactly on-device UQ; OOD detection
    explicit)
  - `on-device inference` — **0.5** (early-exit ensembles run
    inference on-device, partial of the phrase)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Early-exit ensemble where each early exit serves as an
    ensemble member; the disagreement across exits is used as the
    uncertainty estimate. No additional model copies needed.
  - **[결과]** Calibrated uncertainty + OOD detection at TinyML scale
    with a single forward pass; lower model footprint than naïve
    ensembles.
  - **[한계]** Calibration on covariate-shifted OOD is partial;
    benchmarks are vision/audio TinyML tasks, not sensor-streaming
    tasks.
- **system reduction**: Justifies that an `l1-near-sensor` node can
  emit a calibrated `(prediction, uncertainty)` pair with a single
  micro-controller forward pass — exactly the shape combo-A papers
  asked for at the *upstream* PHM layer. Reduces to the in-sensor
  realisation of the same `(value, uncertainty)` contract.

### 2.2 TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

- **authors**: Xunjie Wang, Jiacheng Shi, Zihan Zhao, Yang Yu,
  Zhichao Hua, Jinyu Gu
- **year**: 2025 (Nov 17)
- **venue**: arXiv preprint
- **arxiv**: 2511.13717 · https://hf.co/papers/2511.13717
- **matched_keywords**:
  - `trusted execution environment` — **1.0** (Arm TrustZone is the
    canonical mobile TEE; full-phrase coverage)
  - `on-device inference` — **1.0** ("On-Device Large Language
    Models" — inference is the explicit workload protected)
  - `remote attestation` — **0.5** (TrustZone deployment implies
    attestable measured boot; partial)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Partition an on-device LLM inference path so the
    weight-sensitive segments execute inside Arm TrustZone secure
    world; non-sensitive compute stays in the normal world.
  - **[결과]** Demonstrates that hardware-rooted protection of model
    state (and by extension, sensor-side judgment) can be retrofit
    onto consumer-class Arm hardware.
  - **[한계]** Targets LLMs specifically — sensor-fusion and PHM
    inference are out-of-scope for the paper but are the obvious next
    workloads to port.
- **system reduction**: Justifies the *attestable* leg of the
  near-sensor judgment construction. Reduces to: a node's
  `health_indicator(...)` call can run inside a TEE so that the
  output of L1 (per combo-A) carries a hardware-rooted signature, not
  just a number. This is the closest the v6 corpus comes to a
  "signed sensor reading".

### 2.3 Intelligent Sensing-to-Action for Robust Autonomy at the Edge: Opportunities and Challenges

- **authors**: Amit Ranjan Trivedi, Sina Tayebati, Hemant Kumawat,
  Nastaran Darabi, Divake Kumar, Adarsh Kumar Kosta, Yeshwanth
  Venkatesha, Dinithi Jayasuriya, et al.
- **year**: 2025 (Feb 4)
- **venue**: arXiv preprint
- **arxiv**: 2502.02692 · https://hf.co/papers/2502.02692
- **matched_keywords**:
  - `near-sensor computing` — **1.0** ("sensing-to-action loops" =
    near-sensor compute closure; survey covers in-sensor +
    near-sensor variants)
  - `sensor fusion` — **0.5** ("multi-agent sensing-action loops"
    + multimodal sensor coordination)
  - `edge inference` — **1.0** ("autonomous edge computing",
    "robust autonomy at the edge", "spike-based processing on edge")
  - `in-sensor computing` — **0.5** (paper explicitly frames in-
    sensor as a viable path; partial of phrase)
  - **count = 4**, **sum = 3.0**
- **classification**: [공학]
- **summary**:
  - **[방법]** Position-paper / survey from the same group as STARNet;
    frames the entire sensing-to-action loop as a target for
    proactive, context-aware adaptation, with neuromorphic and
    spike-based fall-back when the digital pipeline is over budget.
  - **[결과]** Catalogue of mechanisms (hierarchical control, multi-
    agent coordination, event-driven processing) that close the loop
    at edge time-scales without round-tripping to cloud.
  - **[한계]** Survey, not a system; no released code; vendor-
    specific neuromorphic targets would matter for any reduction.
- **system reduction**: Provides the *frame* the routine has been
  missing — that "judgment lives near the sensor" is a defensible
  research programme, not a personal preference. Justifies the
  routine's L1 + L3-edge collapsed node as a publishable architectural
  position.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | 2 | indirectly — TEE-rooted on-device compute means a node's failure mode is bounded by attested execution. |
| (b) surplus → wants | — | out of combo-D scope. |
| (c) consensus from physical measurement | 3 | combo-D is the first v6 combo where the two halves (calibrated indicator + attestable execution) are simultaneously attested; the *signing* of the indicator is now an engineering exercise, not an open research problem. |

**Aggregate**: combo-D is the **load-bearing combo of v6**. It is
the first run in this routine where the bridge gap from combo-A
(unsigned indicator) is at least architecturally answerable: QUTE
gives the indicator, TZ-LLM gives the attestation envelope, and
2502.02692 gives the architectural argument that the two should
co-locate at the sensor.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (next combo-D re-entry):**
- in-sensor analog inference
- TEE for embedded ML
- attested telemetry
- event-camera on-device
- spike-based fault detection

**Two under-explored adjacent fields:**
- Approximate computing for energy-harvested inference (overlap with
  PHM at very low duty cycle).
- Hardware root-of-trust for industrial-IO modules — combo-A's
  missing "signed health indicator" lives here.

## 5. Search log

| keyword (query used) | results | in-window | notes |
|---|---|---|---|
| TinyML on-device inference microcontroller | 12 | 8 | core hits cluster on TinyML + on-device learning |
| edge inference IoT efficient | 12 | 9 | abundant; many overlap with TinyML pool |
| in-sensor computing analog near-sensor | 12 | 6 | strong on neuromorphic / IMC |
| multimodal sensor fusion robotics | 10 | 7 | autonomous-driving dominated |
| on-device uncertainty estimation calibration | 10 | 6 | calibration generic, only QUTE explicitly TinyML |
| energy harvesting wireless sensor network | 10 | 4 | mostly security / clustering, no edge-judgment |
| trusted execution environment remote attestation TEE | 12 | 7 | TPM/Keylime + TZ-LLM dominate |

- **pooled after in-window filter, pre-dedup**: ~47
- **dedup**: ~10 cross-keyword duplicates removed
- **scored ≥ 2 keywords**: 9 candidates
- **scored ≥ 2.5 sum AND ≥ 2 keywords (adopted)**: **3** (above)
- **rejected at < 2.5**: 2405.07601 (TinyML semantic mgmt, 1.5),
  2406.01655 (TinySV, 1.5), 2603.11071 (TinyNav, 2.0),
  2510.03219 (TPM remote attestation Kubernetes, 1.5 — wrong layer),
  2412.18024 (Discounted belief fusion, 1.0 — adopted in combo-C
  instead), 2501.06878 (Online extrinsic calibration, 1.5),
  2603.13343 (V2X predictive maintenance, 1.0).

**Search confidence**: medium-high. HF index is well-aligned to this
combo's keyword set; the only missing piece is energy-harvested
edge-judgment, recorded as 근거 부족 for `energy-harvesting wireless
sensor` specifically.
