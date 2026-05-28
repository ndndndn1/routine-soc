# combo-D — Internal node judgment (push the decision close to the sensor)

System role: collect mechanisms that let a node *finish* its own
judgment before talking upstream — TinyML on a microcontroller,
sensor-fusion on edge SoC, conformal/UQ heads that run on-device,
TEEs / remote attestation as integrity envelopes. The point of combo-D
is to *reduce the bandwidth a higher consensus layer has to consume*;
if the node can already say "what I observed, how sure I am, and a
signed receipt for both," combo-C does less work.

## 0. Run metadata

- **run_date**: 2026-05-28
- **search_window**: 2024-05-28 → 2026-05-28 (last 2 years)
- **prior_run**: none (placeholder from v4 reset)
- **routine version**: v6
- **primary tool**: Hugging Face `paper_search` (semantic). Combo-D is
  the best HF-covered combo of the four (cs.AR / cs.LG / eess.SP).
- **fallback tools used**: none.
- **search confidence**: medium-high for TinyML / on-device / edge
  inference axis; medium for sensor fusion + UQ; low for TEE / remote
  attestation as applied to *sensors* specifically (the HF pool surfaces
  TEE-for-LLM-serving more than TEE-at-sensor, which is the combo-D
  intent — same limitation flagged in combo-A).

## 1. Executive summary

Combo-D yields four adoptions that together describe a near-sensor
inference stack: (i) end-to-end TinyML on an ESP32 microcontroller for
real-time autonomous navigation, (ii) TinyML with on-device learning
for speaker verification (a privacy-preserving, sensor-local
verification primitive), (iii) on-device multimodal inference with
pipelined sensing-and-encoding, and (iv) edge inference with real-time
contextual data fusion for V2X-connected vehicles. The recurring
pattern is *sensing → small model → calibrated output* without a
round-trip to the cloud. The TEE / remote-attestation axis surfaces
work, but mostly for *cloud LLM serving* (TZ-LLM, Trusted AI Agents in
the Cloud, BOLT) rather than for *sensor data attestation* — that gap
remains the single most important missing primitive for the combined
combo-A / combo-D pipeline.

## 2. Adopted papers (≥ 2 keywords, ≥ 2.5 sum)

### 2.1 TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers

- **authors**: Pooria Roy, Nourhan Jadallah, Tomer Lapid, Shahzaib Ahmad,
  Armita Afroushe, Mete Bayrak
- **year**: 2026 (Mar 10)
- **venue**: arXiv preprint
- **arxiv**: 2603.11071 · https://hf.co/papers/2603.11071
- **matched_keywords** (count = 3, sum = 2.5):
  - TinyML — 1.0 (full phrase in title)
  - on-device inference — 1.0 (ESP32 microcontroller real-time inference
    of steering / throttle from depth input — full on-device path)
  - edge inference — 0.5 (microcontroller deployment is canonical edge
    inference, but the paper does not use the "edge inference" term
    itself)
- **classification**: [공학]
- **방법**: A lightweight quantized 2D CNN runs on an ESP32-class
  microcontroller, consuming a depth stream and outputting steering and
  throttle commands. Correlation analysis and Grad-CAM are used to
  inspect what the on-MCU model is actually attending to.
- **결과**: Real-time control loop closes on the MCU with the depth-only
  input; latency budget is met without offloading.
- **한계**: Single-sensor (depth), single-platform; no calibrated UQ on
  the steering/throttle output.
- **system reduction**: This is the *thinnest possible* L1 node — the
  whole inference path fits on a $5 MCU. Justifies a `nodes/l1-tiny/`
  family separate from the heavier `l1-reliability` PINN/RUL path.
  Combo-D's role here is to prove that the *control* output of a node
  can be produced near the sensor; the *trust* output (signed receipt)
  is the next step that this paper does not address.

### 2.2 TinySV: Speaker Verification in TinyML with On-device Learning

- **authors**: Massimo Pavan, Gioele Mombelli, Francesco Sinacori,
  Manuel Roveri
- **year**: 2024 (Jun 3)
- **venue**: arXiv preprint
- **arxiv**: 2406.01655 · https://hf.co/papers/2406.01655
- **matched_keywords** (count = 3, sum = 2.5):
  - TinyML — 1.0 (full phrase in title)
  - on-device inference — 1.0 (on-device speaker verification *is*
    inference; the paper's adaptive variant adds on-device learning on
    top)
  - edge inference — 0.5 (TinyML on resource-constrained device =
    canonical edge inference, term not used explicitly)
- **classification**: [공학]
- **방법**: TinyML pipeline for speaker verification with an adaptive
  on-device learning stage that operates on limited unlabelled data; a
  keyword-spotting-style front-end feeds the verification head.
- **결과**: Memory and compute footprint sit within sub-keyword-spotting
  budgets while maintaining usable verification accuracy.
- **한계**: Single biometric modality; the trust model assumes the MCU
  itself is honest (no attestation).
- **system reduction**: This paper is the *identity* counterpart to
  TinyNav's *control* output. Together they suggest the L1 node has
  two near-sensor outputs — "what I observed" and "who I am" — both
  produced before any upstream call. In combo-C terms, this is what
  gives the priority vote a *speaker* without a centralised KMS.

### 2.3 MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding

- **authors**: Runxi Huang, Mingxuan Yu, Mingyu Tsoi, Xiaomin Ouyang
- **year**: 2025 (Oct 29)
- **venue**: arXiv preprint
- **arxiv**: 2510.25327 · https://hf.co/papers/2510.25327
- **matched_keywords** (count = 3, sum = 2.5):
  - on-device inference — 1.0 (full phrase in title; explicit on-device
    multimodal framework)
  - sensor fusion — 1.0 (multimodal pipelined sensing-and-encoding *is*
    sensor fusion at the edge — the paper's "cross-modal speculative
    skipping" is a fusion-time scheduling primitive)
  - edge inference — 0.5 (edge-devices deployment; the paper uses
    "edge devices" not "edge inference" as the term)
- **classification**: [공학]
- **방법**: Pipelines sensing and encoding units so encoders start
  consuming partial sensor streams before the full frame arrives;
  temporal aggregation buffers cross-modal misalignment; an adaptive
  optimizer chooses configurations at runtime; speculative skipping
  drops a modality when the others already agree.
- **결과**: Reduces end-to-end multimodal inference latency on edge
  devices without measurable accuracy loss across autonomous-driving,
  HCI, mobile-health, and UAV workloads.
- **한계**: Latency-accuracy trade is workload-dependent; the
  speculative skip relies on cross-modal agreement signals whose
  calibration is not characterised.
- **system reduction**: This is the *scheduling* primitive for an L1
  node that has more than one sensor. Combo-A's I-GLIDE wants
  per-input-group uncertainty; MMEdge says you can compute those
  groups *in parallel with sensing* rather than sequentially after.
  The implication for the moneyless stack is direct: a node can ship
  its `(score, per_group_uncertainty)` triple within the sensor frame
  budget, not after it.

### 2.4 AI-Driven Predictive Maintenance with Real-Time Contextual Data Fusion for Connected Vehicles: A Multi-Dataset Evaluation

- **authors**: Kushal Khemani, Anjum Nazir Qureshi
- **year**: 2026 (Mar 7)
- **venue**: arXiv preprint
- **arxiv**: 2603.13343 · https://hf.co/papers/2603.13343
- **matched_keywords** (count = 3, sum = 2.5):
  - edge inference — 1.0 (explicit "edge inference" in the paper's
    keyword list — full phrase)
  - sensor fusion — 1.0 (real-time fusion of in-vehicle sensor data
    with V2X external contextual signals; the paper's contribution is
    a fusion-augmented predictive maintenance baseline)
  - on-device inference — 0.5 (edge inference on connected vehicles
    implies on-device but the term is not used)
- **classification**: [공학]
- **방법**: Couples vehicle-side sensor streams with V2X-delivered
  contextual signals through a LightGBM-based fault classifier; uses
  SMOTE for class imbalance and SHAP for per-prediction attribution;
  evaluates across multiple vehicle datasets.
- **결과**: Feature-ablation shows the V2X contextual signals
  materially improve AUC-ROC / macro-F1 over vehicle-only baselines;
  edge inference latency is within real-time bounds.
- **한계**: Tabular fusion via LightGBM, not deep multi-modal; no
  signed-output / TEE story; benchmarks are heterogeneous.
- **system reduction**: This paper is the *combo-A × combo-D bridge in
  one artifact*: predictive maintenance (combo-A's PHM territory) done
  with sensor + V2X fusion (combo-D's edge-inference + sensor-fusion
  territory). It is the cleanest single-paper justification for a
  PHYSICAL_LINK between `l1-reliability` and `l1-tiny` (the
  near-sensor neighbour) — the link carries a *contextually-fused*
  rather than *raw-sensor* stream. Status will enter as `proposed`.

## 3. Hypothesis score (1–5)

- **(a) physical reliability** — combo-D score: **3/5**. Near-sensor
  TinyML proves the cheap-hardware-many-nodes posture is buildable
  *today*; the missing piece for hypothesis (a) at the system level is
  attested redundancy (multiple cheap nodes voting), which combo-D
  enables but does not prove.
- **(b) surplus absorption** — out of scope.
- **(c) priority from measurement** — combo-D score: **2/5**. The
  edge-inference + sensor-fusion adoptions show the *measurement-side*
  of (c) can be produced cheaply and locally. Bridging that into a
  vote weight remains the combo-C gap.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords**:
- conformal prediction on microcontroller
- signed TinyML output / remote attestation MCU
- per-channel uncertainty calibration edge
- TEE-attested sensor stream (IEEE Xplore / USENIX Security)
- ESP32 TFLite-micro on-device learning

**Two under-explored adjacent fields**:
- on-MCU cryptographic identity (Microchip ATECC608, OPTIGA Trust M,
  TPM 2.0 for microcontrollers) — the *trust* output that this
  combo-D pool consistently lacks
- event-camera / neuromorphic-sensor near-sensor inference — combo-D
  surfaced neuromorphic processors (2504.00957) but none with
  in-window keyword density; revisit with "event-based vision" as a
  follow-up

## 5. Search log

Per-keyword calls to `paper_search` (HF), `results_limit = 10`,
`concise_only = true`.

| keyword (query used) | results | in-window | useful |
|---|---|---|---|
| TinyML microcontroller | 120 | 10 | 3 (papers 2.1, 2.2; TinyAC 2509.19350 below) |
| on-device inference mobile | 120 | 10 | 1 (paper 2.3) |
| edge inference low latency | 120 | 10 | 1 (paper 2.4 surfaced via dedup) |
| in-sensor computing analog | 120 | 8 | 0 (analog-circuit synthesis surfaces, not in-sensor) |
| near-sensor computing accelerator | 120 | 8 | 0 (Fulmine SoC 1612.05974 out of window) |
| sensor fusion autonomous robotic | 120 | 10 | 2 (papers 2.3, 2.4) |
| on-device uncertainty estimation edge | 120 | 9 | 1 (2.4 dupe; UA-OEC 2501.06878 below threshold) |
| energy-harvesting wireless sensor network | 120 | 6 | 0 (WakeMod 2505.21529 0.5 sum) |
| trusted execution environment confidential computing | 120 | 10 | 0 (cloud TEE / LLM serving; no sensor-side TEE) |
| remote attestation IoT device | 45 | 6 | 0 (TPM-5G 2510.03219 1.5 sum) |

- **pooled in-window, pre-dedup**: ~87
- **deduped by arXiv ID**: ~40 unique
- **candidates with ≥ 2 keywords matched**: 9
- **adopted (sum ≥ 2.5)**: **4**
- **rejected at < 2.5 sum but ≥ 2 keywords** (logged):
  - TinyAC: Autonomic Computing for Resource-Constrained Systems
    (arXiv:2509.19350) — 2 keywords, 1.5 sum.
  - TZ-LLM: Protecting On-Device LLMs with Arm TrustZone
    (arXiv:2511.13717) — 2 keywords, 2.0 sum. *Close miss.* Best
    candidate for "TEE at the on-device LLM tier" but its target is
    not sensor data; revisit when LLM-on-MCU keyword is added.
  - SPIDEr: Secure Pipeline for Information De-Identification
    (arXiv:2412.09222) — 2 keywords, 2.0 sum. TEE + attestation but
    not sensor-bound.
  - Trusted AI Agents in the Cloud (arXiv:2512.05951) — 2 keywords,
    2.0 sum. TEE + differential attestation but cloud-scale, not
    edge.
  - Uncertainty-Aware Online Extrinsic Calibration (arXiv:2501.06878)
    — 2 keywords, 2.0 sum. Conformal-prediction UQ for sensor
    calibration; the strongest "on-device UQ for sensors" candidate
    but does not deploy to MCU.
  - Availability-aware Sensor Fusion (arXiv:2503.07029) — 1 keyword,
    1.0 sum.

**Search confidence**: medium-high for TinyML / on-device / sensor
fusion (HF index is strong); low for sensor-attached TEE (the literature
lives in IEEE Xplore, USENIX Security, NDSS).
