# combo-D — Node-Internal Judgment / Near-Sensor

> v6 role: 노드 내부에서 자체 판단을 마치게 만들어 상위 통신을 줄이는 부품.
> 특정 하드웨어 방법론이 아니라 "판단을 센서 근처로 옮기는 기법"에 한정.

## 0. Run metadata

- **run_date**: 2026-05-21
- **search_window**: 2024-05-21 → 2026-05-21 (last 2 years)
- **prior_run**: none under v6 (placeholder existed under prior name
  `combo-D-physical-ai-substrate`; directory renamed; no prior adopted
  papers).
- **routine version**: v6
- **primary tool**: Hugging Face `paper_search` (semantic), 10 queries
  matching v6 keyword list, pooled and scored.
- **fallback tools used**: none required.

## 1. Executive summary

Combo-D v6 keyword list breaks into two clusters: a **TinyML / edge
inference** cluster (TinyML, on-device inference, edge inference,
in-sensor, near-sensor, sensor fusion, on-device uncertainty estimation,
energy-harvesting wireless sensor) and a **trust** cluster (trusted
execution environment, remote attestation). The search returns
saturated coverage on the inference cluster — many candidates, four of
which compound across ≥ 2 keywords — and borderline-strong hits on the
trust cluster (Arm TrustZone on-device LLMs; Intel SGX edge GNN). The
combination matters: combo-A produces calibrated (estimate, uncertainty)
tuples node-side; combo-D's role is to argue those tuples can be
computed and signed **inside** the sensor envelope. The adopted set
provides the inference half (QUTE, MMEdge) and the partition-and-protect
half (GNNVault, TZ-LLM). Pure remote-attestation papers exist (e.g.
TPM-IMA on Kubernetes) but did not compound enough keywords to be
adopted; the attestation primitive is real but its bridge to the PHM
tuple is not yet in the literature.

## 2. Adopted papers (≥ 2 keywords matched AND ≥ 2.5 score)

### 2.1 QUTE: Quantifying Uncertainty in TinyML models with Early-exit-assisted ensembles

- **authors**: Nikhil P. Ghanathe, Steve Wilton
- **year**: 2024 (Apr 19)
- **venue**: arXiv preprint
- **arxiv**: 2404.12599 · https://hf.co/papers/2404.12599
- **matched_keywords** (count 3, score 2.5):
  - `TinyML` — 1.0 (literal in title and keywords)
  - `on-device uncertainty estimation` — 1.0 (the entire paper is on-device
    UQ for TinyML; literal "uncertainty quantification" in resource-
    efficient deployment context)
  - `on-device inference` — 0.5 (partial via TinyML deployment context)
- **분류**: [공학]
- **방법**: Add early-exit branches to a TinyML backbone; treat the
  early-exit outputs as a cheap ensemble whose disagreement approximates
  predictive uncertainty without running multiple full passes.
- **결과**: Better OOD / covariate-shift detection than a single-pass
  baseline at the same memory budget; works at TinyML model sizes (KB
  range).
- **한계**: UQ quality bounded by how representative the early-exit
  branches are; no formal calibration guarantee; not tested on PHM-style
  regression workloads (the relevant target for combo-A).
- **system reduction**: Justifies a node-local `predict_with_uncertainty`
  callable inside `l1-reliability` that returns `(estimate, ood_flag,
  confidence)` without uploading to a fatter node. This is the
  *minimum-memory* version of the interface combo-A defined.
- **[NEW]**: yes.

### 2.2 MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding

- **authors**: Runxi Huang, Mingxuan Yu, Mingyu Tsoi, Xiaomin Ouyang
- **year**: 2025 (Oct 29)
- **venue**: arXiv preprint
- **arxiv**: 2510.25327 · https://hf.co/papers/2510.25327
- **matched_keywords** (count 3, score 2.5):
  - `on-device inference` — 1.0 (literal "On-device Multimodal
    Inference" in title)
  - `edge inference` — 1.0 (literal "edge devices" in abstract; entire
    framework targets edge)
  - `sensor fusion` — 0.5 (partial via "multi-modal sensing" and
    pipelined sensor encoding; sensor fusion is the substrate but term
    not used directly)
- **분류**: [공학]
- **방법**: Pipeline sensor sampling and per-modality encoding so that
  inference overlaps with subsequent sample acquisition; add a
  temporal aggregator and a runtime-adaptive modality configurator with
  cross-modal speculative skipping.
- **결과**: Lower end-to-end latency on multi-modal edge tasks at
  comparable accuracy; concrete results on autonomous driving / mobile
  health / UAV.
- **한계**: Targets latency, not energy or attestation; relies on
  predictable sensor cadence; speculative skip can degrade tail accuracy
  under modality drop-out.
- **system reduction**: Justifies a *fusion-and-decide-locally* pattern
  for `l1-reliability` nodes that take multiple physical channels (e.g.
  vibration + thermal + acoustic for a bearing). Concretely:
  `decide_locally(streams[]) → (action_or_null, latency_ms)` with the
  contract that no upstream message is emitted on the no-action path.
  This is the architectural reason a moneyless node can stay quiet most
  of the time.
- **[NEW]**: yes.

### 2.3 Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment

- **authors**: Ruyi Ding, Tianhong Xu, Aidong Adam Ding, Yunsi Fei
- **year**: 2025 (Feb 20)
- **venue**: arXiv preprint
- **arxiv**: 2502.15012 · https://hf.co/papers/2502.15012
- **matched_keywords** (count 3, score 2.5):
  - `trusted execution environment` — 1.0 (literal in title)
  - `edge inference` — 1.0 (literal "Edge GNN Inference" in title)
  - `on-device inference` — 0.5 (partial — TEE on edge devices is a
    proper subset, but the paper does not use the phrase)
- **분류**: [공학]
- **방법**: Split a GNN into a public backbone (runs outside TEE) and a
  small private rectifier (runs inside Intel SGX); partition-before-
  training so the private cut is information-bottleneck enough to
  protect the graph topology while keeping accuracy.
- **결과**: Defeats published link-stealing attacks on edge GNN
  deployments at small accuracy cost and small TEE residency.
- **한계**: Intel SGX specifically (not Arm TrustZone, not RISC-V
  Keystone); GNN-shaped, not directly portable to PHM regression heads.
- **system reduction**: Provides the engineering pattern by which an
  `l1-reliability` node can compute and **sign** its
  `(estimate, uncertainty)` tuple inside a TEE — i.e. the cryptographic
  half of the combo-A attestation gap. Concretely: justifies a future
  `attested_health_indicator() → (tuple, attestation_blob)` function
  whose blob is verifiable by any consumer.
- **[NEW]**: yes.

### 2.4 TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

- **authors**: Xunjie Wang, Jiacheng Shi, Zihan Zhao, Yang Yu, Zhichao Hua, Jinyu Gu
- **year**: 2025 (Nov 17)
- **venue**: arXiv preprint
- **arxiv**: 2511.13717 · https://hf.co/papers/2511.13717
- **matched_keywords** (count 3, score 2.5):
  - `trusted execution environment` — 1.0 (Arm TrustZone is a TEE; the
    paper's mechanism IS a TEE deployment)
  - `on-device inference` — 1.0 (literal "On-Device Large Language
    Models")
  - `edge inference` — 0.5 (partial; on-device implies edge but term not
    spelled out)
- **분류**: [공학]
- **방법**: Run an on-device LLM partially inside the Arm TrustZone
  secure world to protect model weights and intermediate activations
  from the rich-OS attack surface; engineering work to keep latency
  acceptable despite the secure-non-secure crossings.
- **결과**: Demonstrates protected on-device LLM inference with a
  workable latency budget on commodity Arm SoCs.
- **한계**: TrustZone-specific; threat model assumes secure world itself
  is uncompromised; LLM-shaped (not PHM-shaped), but engineering
  patterns transfer.
- **system reduction**: Reinforces 2.3: on commodity ARM hardware
  (which is where most plausible PHM nodes sit), the TEE primitive is
  already deployable for non-trivial workloads. Justifies that the
  `attested_health_indicator()` callable from 2.3 is **not** restricted
  to Intel-class hardware — a Raspberry Pi or industrial ARM gateway
  can host the secure-world half.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5, 부품 가치 점수)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable | 3 | Strongly indirect: node-internal UQ + TEE means a node can self-certify its own degradation state. Doesn't argue *that* the production is reliable, but argues the *reporting* of reliability is itself attestable. |
| (b) Surplus absorbs non-essential wants | — | out of scope. |
| (c) Consensus from measurement directly | 4 | This is combo-D's strongest contribution. QUTE + MMEdge produce the (estimate, uncertainty) at the sensor; GNNVault + TZ-LLM bind that output to hardware identity. The remaining mile is a protocol layer (combo-C). |

**Aggregate**: combo-D closes the attestation gap that combo-A flagged.
The pair (combo-A + combo-D) now describes a **complete node-internal
pipeline**: sensor → physics residual → UQ → TEE-signed tuple. The
*inter-node* protocol that consumes those tuples is combo-C's job.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords**:

- attested PHM output (bridge term, combo-A ↔ combo-D)
- conformal prediction on-device
- in-sensor analog uncertainty
- RISC-V Keystone enclave (alternative to SGX/TrustZone)
- continuous remote attestation embedded

**Two under-explored adjacent fields**:

- Energy-harvesting / batteryless intermittent computing — the
  energy-harvesting keyword returned weak hits (only WakeMod scored
  meaningfully); a focused re-entry on batteryless TinyML would tighten
  the "node stays quiet by default" argument.
- DICE/RIoT-style hardware-rooted identity for cheap MCUs — relevant
  for attestation in nodes too small for full TrustZone.

## 5. Search log

| keyword query (v6) | returned | in-window | pooled |
|---|---|---|---|
| TinyML on-device inference microcontroller | 12 | 6 | 6 |
| in-sensor computing analog neural network | 12 | 5 | 5 |
| near-sensor computing edge AI low power | 12 | 5 | 5 |
| sensor fusion multimodal embedded systems | 12 | 6 | 6 |
| on-device uncertainty estimation edge inference | 12 | 6 | 6 |
| energy-harvesting wireless sensor network intermittent computing | 12 | 5 | 5 |
| trusted execution environment machine learning inference | 12 | 7 | 7 |
| remote attestation IoT edge device integrity | 8 | 3 | 3 |

- **pooled after in-window filter, pre-dedup**: ~43
- **dedup**: ~8 duplicates (e.g. 2502.02692, 2510.03219 each in 2 queries).
- **candidates scored ≥ 2 keywords**: 7
  - 2404.12599 QUTE (3 kw, 2.5) ✓ adopted
  - 2510.25327 MMEdge (3 kw, 2.5) ✓ adopted
  - 2502.15012 GNNVault (3 kw, 2.5) ✓ adopted
  - 2511.13717 TZ-LLM (3 kw, 2.5) ✓ adopted
  - 2502.02692 Sensing-to-Action edge (4 kw weak, 2.0) — rejected, all partials
  - 2510.03219 TPM-IMA remote attestation (2 kw, 1.5) — rejected
  - 2501.06878 UQ for extrinsic calibration (2 kw, 1.5) — rejected
- **rejected at < 2.5**: 3 above + ~15 single-keyword hits.

**Search confidence**: high on TinyML / TEE axes (recent, active, many
hits). **Low** on `in-sensor computing` and `near-sensor computing` —
these terms are used in older (pre-2024) literature; in-window hits are
sparse and tend to be neuromorphic-survey papers, not deployable
mechanisms. `energy-harvesting wireless sensor` returned only WakeMod
and infrastructure-flavoured papers; the batteryless-TinyML literature
exists but is not surfacing on HF's index.
