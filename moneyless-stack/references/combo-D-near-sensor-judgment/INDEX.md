# combo-D — judgment near the sensor

## 0. Run metadata

- **run_date**: 2026-04-24
- **search_window**: 2024-04-24 → 2026-04-24
- **prior_run**: none (first combo-D run under v6).
- **routine**: v6.
- **task**: (a) search + adoption.
- **primary tool**: HF `paper_search`. HF is strong for combo-D
  (cs.AR / cs.LG / eess.SP) and 5 papers clear the ≥ 2.5 threshold.

## 1. Executive summary

Combo-D is the combo whose keyword list (`TinyML`, `on-device
inference`, `edge inference`, `in-sensor computing`, `near-sensor
computing`, `sensor fusion`, `on-device uncertainty estimation`,
`energy-harvesting wireless sensor`, `trusted execution environment`,
`remote attestation`) maps most cleanly onto HF-indexed literature.
Five papers clear the threshold. The strongest adoption is MMEdge
(2510.25327), which gives a concrete multi-modal on-device inference
pipeline — directly reducible to the "node-internal judgment" part
the stack needs. The Trivedi-et-al survey on sensing-to-action at the
edge (2502.02692) is adopted as a framing paper. Two TinyML papers
(TinySV, On-device Online TinyML) and TinyNav (2603.11071) fill out
the deployment envelope. **Remote-attestation and on-device-UQ
literature exists but cleared the threshold only via the
sensing-to-action survey (2502.02692) — meaning the tight
attestation-of-a-specific-sensor-HI paper is still not in the
adopted set, same gap flagged in combo-A.**

## 2. Adopted papers (≥ 2 keywords, sum ≥ 2.5)

### 2.1 MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding

- **authors**: Huang, Yu, Tsoi, Ouyang
- **year**: 2025 (Oct 29)
- **arxiv**: 2510.25327 · https://hf.co/papers/2510.25327
- **matched_keywords**:
  - `on-device inference` — 1.0 (explicit: "on-device multi-modal
    inference framework")
  - `sensor fusion` — 1.0 (explicit: "multimodal inference",
    "inter-modality dependencies")
  - `edge inference` — 0.5 (partial: "resource-constrained edge
    devices")
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Decomposes inference into fine-grained sensing+encoding
    units so computation proceeds as data arrive; lightweight
    temporal aggregation; cross-modal speculative skipping.
  - 결과: End-to-end latency reduction while preserving accuracy on
    two public multimodal datasets and a UAV testbed.
  - 한계: Multimodal assumption; requires tight integration with
    sensing pipeline; no attestation of what the on-device output
    represents cryptographically.
- **시스템 환원**: Defines the contract of a node's local "already
  judged" output: a fused multi-modal verdict that exits the node on
  a latency budget tighter than any upstream poll would allow. This
  is what L1 `health_indicator` should look like when the node has
  more than one sensor. Links downstream to combo-A 2.1 I-GLIDE's
  indicator-group concept.

### 2.2 Intelligent Sensing-to-Action for Robust Autonomy at the Edge

- **authors**: Trivedi, Tayebati, Kumawat, Darabi, Kumar, Kosta,
  Venkatesha, Jayasuriya, et al.
- **year**: 2025 (Feb 4)
- **arxiv**: 2502.02692 · https://hf.co/papers/2502.02692
- **matched_keywords**:
  - `sensor fusion` — 1.0 (explicit: "multi-modal data fusion")
  - `near-sensor computing` — 1.0 (explicit: "sensing-to-action
    loops", "action-to-sensing pathways")
  - `edge inference` — 0.5 (partial: "autonomous edge computing")
  - `on-device inference` — 0.5 (partial)
  - `in-sensor computing` — 0.5 (partial via sensing-integrated
    hierarchical control)
  - **sum**: 3.5
- **classification**: [공학] (survey / position paper).
- **방법 / 결과 / 한계**:
  - 방법: Surveys proactive context-aware sensing-to-action loops,
    multi-agent sensing-action coordination, neuromorphic substrate.
  - 결과: Articulates a control-loop frame within which every node
    knows both *what it sensed* and *what to sense next*.
  - 한계: Survey — no single benchmark, no shared codebase.
- **시스템 환원**: Provides the L1 node's behavioural model: a local
  closed loop that terminates most decisions without upstream
  communication. This justifies the default-deny inter-node policy
  in PHYSICAL_LINKS.md.

### 2.3 On-device Online Learning and Semantic Management of TinyML Systems

- **authors**: Ren, Li, Anicic, Runkler
- **year**: 2024 (May 13)
- **arxiv**: 2405.07601 · https://hf.co/papers/2405.07601
- **matched_keywords**:
  - `TinyML` — 1.0 (explicit, title)
  - `on-device inference` — 1.0 (explicit: "real-time on-device ML")
  - `edge inference` — 0.5 (partial)
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Online learning + federated meta-learning for TinyML
    deployment at scale, plus a semantic-management layer for
    device + model heterogeneity.
  - 결과: Three real-world TinyML apps (handwritten char, keyword
    audio, smart-building presence) improved via the framework.
  - 한계: Infrastructure paper — no formal guarantees on drift.
- **시스템 환원**: Gives the heterogeneous-node registry shape for
  the future `nodes/` inventory. Ties into combo-A's multi-model
  HI approach: each tiny node can advertise which HI variant it
  runs via the semantic layer.

### 2.4 TinySV: Speaker Verification in TinyML with On-device Learning

- **authors**: Pavan, Mombelli, Sinacori, Roveri
- **year**: 2024 (Jun 3)
- **arxiv**: 2406.01655 · https://hf.co/papers/2406.01655
- **matched_keywords**:
  - `TinyML` — 1.0 (explicit)
  - `on-device inference` — 1.0 (explicit: "on-device learning
    algorithm")
  - `edge inference` — 0.5 (partial via IoT deployment)
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: Two-layer KWS + adaptive speaker verification on Infineon
    PSoC 62S2; reduces memory/compute for on-device adaptation.
  - 결과: Demonstrated real-world IoT deployment.
  - 한계: Task-specific (speaker verification); still operates on
    unlabelled but single-modality data.
- **시스템 환원**: Concrete template for *identity / authenticity*
  decisions at the sensor, one of the two judgments the routine
  cares about (the other being HI). Potential fallback if sensor-
  data-attestation cryptographic solutions remain absent — a node
  may be able to authenticate *what is speaking to it* even
  without attesting *its own output*.

### 2.5 TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers

- **authors**: Roy, Jadallah, Lapid, Ahmad, Afroushe, Bayrak
- **year**: 2026 (Mar 10)
- **arxiv**: 2603.11071 · https://hf.co/papers/2603.11071
- **matched_keywords**:
  - `TinyML` — 1.0 (explicit)
  - `on-device inference` — 1.0 (explicit: deployed on ESP32)
  - `edge inference` — 0.5 (partial)
  - **sum**: 2.5
- **classification**: [공학]
- **방법 / 결과 / 한계**:
  - 방법: 23k-param quantised 2D CNN on ESP32; 20-frame depth window
    → steer/throttle.
  - 결과: 30 ms inference latency; Grad-CAM validates obstacle-
    avoidance spatial awareness.
  - 한계: Depth-only input; supervised training; no UQ.
- **시스템 환원**: Shows feasibility of a full sensing-to-action loop
  on a single microcontroller — i.e. a node that completes its
  judgment without *any* upstream communication. This is the
  extreme case the default-deny policy optimises for.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | 2 | Combo-D gives bodies to carry the combo-A HI. But nothing in the adopted combo-D set signs the HI. |
| (b) surplus absorption | — | out of scope for combo-D. |
| (c) measurement-direct priority | 2 | Local closed-loop inference reduces the need for upstream priority arbitration, which is a partial substitute for measurement-direct priority. Not a full solution. |

**Aggregate**: combo-D has the most adoptable engineering literature
of the four combos. The attestation gap is the same gap combo-A
flagged — cross-combo synthesis.md follows up.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- intermittent computing (canonical concept adjacent to energy-harvesting)
- PUF-backed attestation
- secure aggregation at the edge
- trusted execution environment on RISC-V (Keystone / CCA)
- in-sensor analog classifier

**Two under-explored adjacent fields:**
- Neuromorphic sensor co-processors (event cameras + SNNs).
- Formal verification of on-device inference results.

## 5. Search log

| keyword (query used) | returned | in-window | pooled | ≥ 2.5 |
|---|---|---|---|---|
| TinyML on-device inference microcontroller | 10 | 5 | 5 | 3 |
| edge inference efficient neural network deployment | 10 | 6 | 6 | 1 (survey) |
| in-sensor computing near-sensor processing analog | 8 | 2 | 2 | 0 |
| sensor fusion multi-modal edge IoT | 8 | 5 | 5 | 2 |
| energy-harvesting wireless sensor intermittent | 8 | 3 | 3 | 0 |
| trusted execution environment remote attestation embedded | 8 | 5 | 5 | 0 (all are compute-node attestation) |
| on-device uncertainty quantification edge | 8 | 3 | 3 | 0 (QUTE 5 days before window) |

- pooled in-window unique: ~24
- dedup: 4 cross-keyword duplicates (Intelligent Sensing-to-Action
  surfaces in 3 queries; MMEdge in 2).
- ≥ 2.5 adopted: **5**
- rejected at 2.0 ≤ score < 2.5: 2510.03219 (TPM 5G VNFs, 1.5 on
  combo-D axis; compute-node attestation not sensor attestation),
  2411.18271 (analog IMC RNN, 1.5), 2505.21529 (WakeMod, 1.0 —
  wake-up radio, not energy-harvesting per se),
  2504.00957 (SNN neuromorphic edge, 1.5).
- rejected < 2.0: 2212.10881 (In-sensor Neuromorphic, out of window),
  2404.12599 (QUTE on-device UQ, 5 days before window).

**Search confidence**: high. The adopted set covers deployment
(TinySV, TinyNav), scale management (2405.07601), multi-modal
judgment (MMEdge), and the behavioural frame (2502.02692). The
attestation sub-axis remains the weak spot and is cross-referenced
with combo-A's identical gap in synthesis.md.
