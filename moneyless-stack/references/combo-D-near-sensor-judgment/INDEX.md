# combo-D — Near-Sensor Judgment

System role: pull as much of the judgement loop down to the node /
sensor itself, so the upstream link can be closed by default and the
output that *does* leave the node is small, signed, and self-justifying.

## 0. Run metadata

- **run_date**: 2026-05-14
- **search_window**: 2024-05-14 → 2026-05-14 (last 2 years)
- **prior_run**: placeholder only (`combo-D-physical-ai-substrate/`).
  This is the first substantive combo-D run.
- **routine version**: v6
- **task**: combo search + adoption + INDEX.md
- **primary tool**: HF `paper_search` (cs.AR / cs.LG / eess.SP are
  well-indexed). Per-keyword + bridge-style calls, scored.
- **fallback tools (not used)**: IEEE Xplore direct, arXiv API direct,
  Semantic Scholar.

## 1. Executive summary

Combo-D's keyword set is well-covered by HF's index — TinyML,
on-device inference, edge inference, sensor fusion, and TEE / remote
attestation are all active publishing fields, and several of the
2025-2026 papers explicitly try to bridge them. Three papers clear
the 2.5 threshold and they form a near-complete near-sensor
substrate: (1) MMEdge — multimodal sensor fusion *as* an on-device
pipeline; (2) Trivedi et al. — sensing-to-action loops where the
"action" is decided at the edge, no upstream call; (3) TZ-LLM —
the trusted-execution side, with the LLM (i.e. the judgment) kept
inside ARM TrustZone. The trio answers run-1's open question on
"can the L1 indicator be signable at the sensor?" with a qualified
**yes**: TEE + on-device inference is mature enough that the
"sensor → signed `(score, σ)`" pipeline is buildable. What still
does *not* show up in the literature is the *combination* — there is
no paper that signs a TinyML-derived uncertainty estimate inside a
TEE in one pipeline. That synthesis is the implementation work,
not a literature gap.

## 2. Adopted papers (matched_keywords ≥ 2 AND score ≥ 2.5)

### 2.1 MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding

- **authors**: Runxi Huang, Mingxuan Yu, Mingyu Tsoi, Xiaomin Ouyang
- **year**: 2025 (Oct 29)
- **venue**: arXiv preprint
- **arxiv**: 2510.25327 · https://hf.co/papers/2510.25327
- **matched_keywords**:
  - "on-device inference" (1.0 — title)
  - "edge inference" (1.0 — "multimodal inference framework for edge
    devices")
  - "sensor fusion" (0.5 — multimodal pipelined sensing across
    modalities = sensor fusion at the encoder)
  - **Total: 2.5** · 3 keywords matched
- **classification**: [공학]
- **방법**: Pipelines the sensing step with the encoding step on the
  edge device — instead of "sense everything, then encode" the
  encoder consumes partial sensor windows as they arrive.
  Cross-modal speculative skipping cuts redundant compute when one
  modality is informative enough.
- **결과**: Latency reduction at maintained accuracy on autonomous
  driving / mHealth / UAV workloads. Cross-modal skipping is the
  bit that makes the pipelining honest — it gives an *adaptive*
  per-event compute budget rather than worst-case sizing.
- **한계**: Application benchmarks rather than a clean low-level
  microbenchmark. The speculative skipping policy is dataset-tuned;
  generalisation across modality combinations is not characterised.
- **시스템 환원**: Justifies a `near-sensor` module pattern where
  the encoder is the only thing that sees raw sensor data. The
  module's outbound API is the encoded representation, not the raw
  stream — which is the right shape for the "default-deny" link
  policy in `PHYSICAL_LINKS.md`.
- **[NEW]**: yes.

### 2.2 Intelligent Sensing-to-Action for Robust Autonomy at the Edge: Opportunities and Challenges

- **authors**: Amit Ranjan Trivedi, Sina Tayebati, Hemant Kumawat,
  Nastaran Darabi, Divake Kumar, Adarsh Kumar Kosta, Yeshwanth
  Venkatesha, Dinithi Jayasuriya, + 4 others
- **year**: 2025 (Feb 04)
- **venue**: arXiv preprint
- **arxiv**: 2502.02692 · https://hf.co/papers/2502.02692
- **matched_keywords**:
  - "edge inference" (1.0 — "autonomous edge computing"; entire
    paper is edge-decision-loop framing)
  - "near-sensor computing" (0.5 — "sensing-to-action loops" closed
    near the sensor)
  - "in-sensor computing" (0.5 — same construct, slightly different
    keyword vocabulary)
  - "sensor fusion" (0.5 — multi-agent / multi-sensor coordination
    discussed as a substrate)
  - "on-device inference" (0.5 — implied by the framework)
  - **Total: 3.0** · 5 keywords matched
- **classification**: [공학]
- **방법**: Position / survey paper. Frames the edge-AI design
  problem as a sensing-to-action loop and argues that proactive,
  context-aware adaptation is the missing primitive. Surveys
  neuromorphic / event-driven processing and multi-agent
  coordination as enabling technologies.
- **결과**: Identifies hierarchical control and multi-agent
  sensing-action loops as the two co-design axes. The contribution
  is the framing, not a measurement.
- **한계**: Survey; no benchmark. The "challenges" half is more
  developed than the "opportunities" half — concrete protocols are
  thin.
- **시스템 환원**: Justifies the *shape* of the L1 node — it is a
  closed sensing-to-action loop with the upstream link only
  reporting *decisions*, not perceptions. Locks in the routine's
  default-deny posture from the engineering side. The neuromorphic
  / event-driven material also seeds combo-D's follow-up keywords.
- **[NEW]**: yes.

### 2.3 TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

- **authors**: Xunjie Wang, Jiacheng Shi, Zihan Zhao, Yang Yu,
  Zhichao Hua, Jinyu Gu
- **year**: 2025 (Nov 17)
- **venue**: arXiv preprint
- **arxiv**: 2511.13717 · https://hf.co/papers/2511.13717
- **matched_keywords**:
  - "trusted execution environment" (1.0 — Arm TrustZone is the
    canonical mobile TEE)
  - "on-device inference" (1.0 — "On-Device Large Language
    Models")
  - "remote attestation" (0.5 — TrustZone supports attestation;
    paper relies on it for model integrity)
  - **Total: 2.5** · 3 keywords matched
- **classification**: [공학]
- **방법**: Loads and runs an on-device LLM inside an Arm TrustZone
  secure world, with weights and the runtime isolated from the
  normal-world OS. Uses TrustZone's existing attestation
  primitives for integrity proofs.
- **결과**: A working secure-world LLM inference path on
  consumer-grade ARM hardware. The construction itself —
  weights-in-TEE + attestation primitives reachable from outside —
  is the result that matters for moneyless-stack.
- **한계**: Heavy on engineering, light on threat-model formalism.
  The performance hit of TEE memory isolation on LLM inference is
  real (paper reports it as the main cost).
- **시스템 환원**: Justifies the "signed-at-source" half of the
  near-sensor pattern. The same TEE construction generalises from
  LLM to PHM-indicator: a small model that produces `(score, σ)`
  can sit inside the TEE and emit a signed output. This is the
  first paper in the routine that physically allows the "signed
  health indicator" construct flagged as open by run 1.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | 3 | with TEE-attested on-device inference, the *per-node trust* part of "reliable enough to skip a money layer" now has a real engineering anchor. |
| (b) Surplus absorbs non-essential wants | — | not the combo-D axis. |
| (c) Consensus from physical measurement | 3 | the missing piece from combo-A — "signed indicator at source" — is now buildable. The aggregation layer (whose vote weight reads such a signed indicator) is still combo-C's open problem. |

**Aggregate**: combo-D substantially advances (a) and (c). Combined
with combo-A (indicator-with-uncertainty exists) and combo-C
(measurement→priority pipeline exists), the routine now has
literature anchors for every L1→L3 piece except the actual
voting-weight binding.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- neuromorphic event-driven inference (for low-power sensing loops)
- TEE-attested model output / verifiable inference
- on-device conformal prediction
- secure aggregation across edge nodes
- in-memory computing reliability (drift, retention)

**Two under-explored adjacent fields:**
- Energy-harvesting MCU literature — appeared at the margins of the
  pool but never co-occurred strongly with combo-D vocab. The
  intermittent-computing framing is the relevant one; carry it
  forward.
- Sensor calibration drift / model-update logistics at the edge —
  attestation of *what is being run* is solved (combo-D); attestation
  of *whether the model is up to date* is not.

## 5. Search log

`paper_search` (HF), 10 results per call.

| query | results | in-window | pooled |
|---|---|---|---|
| TinyML on-device inference microcontroller | 10 | 5 | 5 |
| in-sensor near-sensor computing edge inference | 10 | 4 | 4 |
| sensor fusion on-device uncertainty estimation | 10 | 3 | 3 |
| energy-harvesting wireless sensor TinyML | 10 | 4 | 4 |
| trusted execution environment edge attestation | 10 | 6 | 6 |
| TinyML uncertainty quantification edge devices | 10 | 5 | 5 |
| in-sensor computing analog processing | 10 | 3 | 3 |
| edge AI inference microcontroller sensor IoT | 10 | 5 | 5 |
| multi-sensor fusion edge device autonomous | 10 | 4 | 4 |

- **pooled after in-window filter, pre-dedup**: ~39
- **dedup (arXiv ID + title-normalised)**: ~28 unique
- **candidates scored ≥ 2.0**: 9
- **candidates scored ≥ 2.5 and adopted**: **3**
- **rejected at 2.0**:
  - 2603.11071 TinyNav — TinyML 1.0 + on-device 0.5 + edge 0.5 = 2.0.
  - 2604.19642 Micro Language Models — on-device 1.0 + edge 0.5 +
    TinyML partial 0.5 = 2.0.
  - 2407.19401 Towards Secure and Private AI — TEE 1.0 + edge 0.5 +
    remote attestation 0.5 = 2.0.
- **rejected just-outside-window**:
  - 2404.12599 QUTE (Apr 19 2024) — would score 2.5 (TinyML 1.0 +
    on-device uncertainty 1.0 + on-device inference 0.5) but
    publication date is 25 days before the 2024-05-14 cutoff. Strict
    rejection. Carry as the first re-entry candidate when the
    window slides forward.
- **rejected as out-of-window**: 1612.05974 Fulmine SoC (2016),
  2007.10319 MCUNet (2020), 2206.15472 On-Device Training Under 256KB
  (2022), 2305.08415 Marsellus (May 2023).

**Search confidence**: high. The keyword set is densely covered;
multiple independent queries surface the same top papers and
saturation is reached after ~9 calls. The negative results
(TEE+TinyML+UQ not yet co-published as one paper) are also confident
— they are not artefacts of insufficient search.

**근거 부족 (insufficient evidence)** flagged for:
- "energy-harvesting wireless sensor" as a joint keyword with the
  TinyML/edge cluster. The intermittent-computing literature
  exists (Maeng/Lucia line) but is mostly pre-window or in
  embedded-systems venues outside the HF index.
- A single paper that puts TinyML + on-device UQ + TEE attestation
  in one pipeline. The components exist; the integration is the
  implementation work, not a citation gap.
