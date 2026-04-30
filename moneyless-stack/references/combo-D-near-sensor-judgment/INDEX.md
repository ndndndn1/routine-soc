# combo-D — Judgment near the sensor

System role: keep the per-node compute close enough to the sensor that
the node can finish its judgment locally and only emit a small
attested message upward. Strict scope: the judgment-locality and
substrate-trust pieces. Does not cover the consensus protocol itself
(combo C) or the indicator-physics (combo A).

## 0. Run metadata

- **run_date**: 2026-04-30
- **search_window**: 2024-04-30 → 2026-04-30 (last 2 years)
- **prior_run**: none — v4 placeholder only (`combo-D-physical-ai-substrate`).
- **routine version**: v6
- **primary tools**: HF `paper_search` (semantic) on cs.AR / cs.LG /
  eess.SP. WebSearch for cross-confirmation.

## 1. Executive summary

Combo D is the densest of the four. Three intersecting research
trajectories converge on the routine's premise that *judgment should
finish at the node*: (i) TinyML / on-device-inference papers now
target end-to-end tasks (autonomous navigation, depth estimation) on
microcontroller-class devices; (ii) edge-multimodal-fusion papers
treat sensing-and-encoding as a pipelined unit; (iii) trusted-execution
papers (Arm TrustZone, TPM-IMA) are converging on practical
attested-inference patterns. Four engineering papers are adopted.
The previously identified gap from combo A — **sensor-stream
attestation** — is partially closed by TZ-LLM (TrustZone for
on-device LLMs) and the TPM-IMA attestation work, although the latter
attests workloads, not sensor data per se.

## 2. Adopted papers (≥ 2 keyword matches *or* ≥ 2.5 score)

### 2.1 MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding

- **authors**: Runxi Huang, Mingxuan Yu, Mingyu Tsoi, Xiaomin Ouyang
- **year**: 2025 (Oct 29)
- **venue**: arXiv preprint
- **arxiv**: 2510.25327 · https://hf.co/papers/2510.25327
- **matched_keywords** (v6):
  - `on-device inference` — full ("on-device multimodal inference"
    in title) = **1.0**
  - `edge inference` — full ("edge devices" + inference framework
    explicitly framed for edge) = **1.0**
  - `sensor fusion` — partial ("pipelined sensing and encoding",
    multimodal fusion across modalities; not the strict 2-gram
    "sensor fusion") = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: A multi-modal inference framework that pipelines
    sensing and encoding stages, adds temporal aggregation, and
    uses an adaptive multimodal-configuration optimiser plus
    cross-modal speculative skipping.
  - **결과**: Reduces end-to-end latency on edge devices while
    maintaining accuracy across autonomous-driving, mobile-health,
    and UAV workloads.
  - **한계**: Requires hardware capable of pipelining (not the
    smallest MCU class); no on-device-uncertainty channel.
- **system reduction**: Justifies a **pipelined sense-encode-emit**
  pattern at the L1 node — sensing happens while the previous frame
  is still being encoded, so the link upward never carries unprocessed
  raw sensor data. This locks in the "judgment finishes at the node"
  invariant the routine wants.
- **[NEW]**: yes (v6).

### 2.2 TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers

- **authors**: Pooria Roy, Nourhan Jadallah, Tomer Lapid, Shahzaib
  Ahmad, Armita Afroushe, Mete Bayrak
- **year**: 2026 (Mar 10)
- **venue**: arXiv preprint
- **arxiv**: 2603.11071 · https://hf.co/papers/2603.11071
- **matched_keywords** (v6):
  - `TinyML` — full ("end-to-end TinyML" in title) = **1.0**
  - `on-device inference` — full ("inference latency" on ESP32 MCU,
    standard on-device usage) = **1.0**
  - `edge inference` — partial (microcontroller-class edge) = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Lightweight quantised 2D CNN deployed on ESP32 MCU,
    consumes depth data, outputs steering and throttle commands.
    Includes correlation analysis and Grad-CAM for interpretability.
  - **결과**: Demonstrates end-to-end autonomous navigation entirely
    on an ESP32-class device; full perception-to-action loop closes
    on-chip.
  - **한계**: Single-task (navigation); model is depth-only — no
    fusion; no uncertainty channel.
- **system reduction**: Justifies treating an ESP32-class MCU as a
  *complete* L1 node (sense + decide + emit) rather than a sensor
  satellite. The ESP32's modest cost and the demonstrated end-to-end
  loop set the **lower hardware envelope** for the moneyless-stack
  L1 node.
- **[NEW]**: yes (v6).

### 2.3 Intelligent Sensing-to-Action for Robust Autonomy at the Edge: Opportunities and Challenges

- **authors**: Amit Ranjan Trivedi, Sina Tayebati, Hemant Kumawat,
  Nastaran Darabi, Divake Kumar, Adarsh Kumar Kosta, Yeshwanth
  Venkatesha, Dinithi Jayasuriya, et al.
- **year**: 2025 (Feb 04)
- **venue**: arXiv preprint
- **arxiv**: 2502.02692 · https://hf.co/papers/2502.02692
- **matched_keywords** (v6):
  - `edge inference` — partial ("autonomous edge computing" + the
    paper is explicitly about edge) = **0.5**
  - `in-sensor computing` — partial ("sensing-to-action loops" with
    spike-based event-driven processing close to the sensor) = **0.5**
  - `near-sensor computing` — partial (same justification —
    judgment moves close to sensing) = **0.5**
  - `sensor fusion` — partial (multi-agent sensing-action coordination)
    = **0.5**
  - `on-device uncertainty estimation` — partial (paper discusses
    proactive context-aware adaptation under uncertainty) = **0.5**
  - count = 5 (all partial), total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Position / survey paper proposing proactive,
    context-aware sensing-to-action loops at the edge with
    neuromorphic and event-driven processing as substrate; argues
    for hierarchical control and multi-agent coordination.
  - **결과**: A taxonomy of design opportunities and the open
    challenges; not an empirical paper.
  - **한계**: Survey / agenda paper, not a measurable result.
- **system reduction**: Justifies the *architectural* choice that the
  L1 node should have a sense → infer → act loop with no upward
  communication required to act. This is the single best statement
  in the surveyed literature of the routine's "judgment near sensor"
  premise.
- **[NEW]**: yes (v6).

### 2.4 TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

- **authors**: Xunjie Wang, Jiacheng Shi, Zihan Zhao, Yang Yu,
  Zhichao Hua, Jinyu Gu
- **year**: 2025 (Nov 17)
- **venue**: arXiv preprint
- **arxiv**: 2511.13717 · https://hf.co/papers/2511.13717
- **matched_keywords** (v6):
  - `trusted execution environment` — full (Arm TrustZone is the
    canonical TEE on Arm; the paper is built on TrustZone) = **1.0**
  - `on-device inference` — full ("On-Device Large Language Models"
    in title; protects on-device inference) = **1.0**
  - `remote attestation` — partial (TrustZone offers attestation
    primitives that the paper's threat model relies on, even if the
    paper's contribution is the protection scheme not the attestation
    itself) = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Uses Arm TrustZone secure-world to protect on-device
    LLM weights and intermediate activations from a hostile rich-OS;
    enforces I/O boundaries between secure and normal worlds.
  - **결과**: Demonstrates feasibility of running LLM inference under
    TrustZone with workable performance overhead. (Detailed numbers
    not in our snippet pool — flagged as area to verify on next run.)
  - **한계**: TrustZone-specific; not portable to non-Arm parts; LLM
    scope (which is overkill for our PHM use case but the security
    construction generalises).
- **system reduction**: Justifies the **attested-emit** primitive at
  the L1 node: an indicator emitted by the node carries a
  TrustZone-backed signature that downstream nodes can verify.
  This closes (partially) the combo-A gap on `sensor data
  attestation`. Does not yet attest the *sensor*, only the
  computation — a residual gap recorded for follow-up.
- **[NEW]**: yes (v6).

## 3. Hypothesis sub-score (1–5)

| paper | sub-hyp it relates to | score | reason |
|---|---|---|---|
| MMEdge (2510.25327) | (a) reliability + (c) | 4 | pipelined sense-encode keeps raw data off the link |
| TinyNav (2603.11071) | (a) | 4 | sets the hardware floor — ESP32 is enough |
| Sensing-to-Action survey (2502.02692) | (a) + architectural | 4 | best literature statement of "judgment near sensor" |
| TZ-LLM (2511.13717) | (c) measurement-as-input + trust | 4 | gives us attested-emit; partially closes the combo-A attestation gap |

**Combo D v6 aggregate**: hypothesis branch (a) — that the production
substrate can be made physically reliable enough to skip currency-as-
trust — is most strongly attested in this combo. The L1 node can be
small (ESP32-class), can finish judgment locally (TinyNav, MMEdge),
and can attest the result it emits (TZ-LLM). Combined with combo A
(physics-priors / UQ on the indicator) and combo C (DPP-substrate /
EEA-priority), the hardware story is now complete on paper. End-to-
end *sensor* attestation (not just computation attestation) remains
the residual gap.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
1. `attested sensor reading` — the residual gap above; "sensor data
   attestation" generalised.
2. `signed indicator emission` — combo A × combo D bridge keyword.
3. `event-driven inference MCU` — narrower than "edge inference",
   matches the spike-based half of the literature.
4. `over-the-air model update attested` — load-bearing for
   long-horizon node maintenance.
5. `fault-injection MCU resilience` — combines combo A's reliability
   physics with combo D's substrate.

**Two unexplored adjacent fields:**
- **Confidential computing on RISC-V** (Keystone / Sanctum lineage) —
  removes the Arm dependency of TZ-LLM.
- **Open-source secure elements** (Tropic Square TROPIC01, etc.) —
  attestable hardware built on OSH; ties combo D back to combo B's
  bootstrap claim.

## 5. Search log

| keyword query | tool | results | in-window | adopted |
|---|---|---|---|---|
| TinyML on-device inference microcontroller | HF | 12 | 4 | TinyNav (2603.11071) |
| in-sensor / near-sensor analog inference | HF | 12 | 2 | Sensing-to-Action (2502.02692) |
| edge inference uncertainty estimation device | HF | 12 | 5 | 0 net new |
| trusted execution environment remote attestation edge | HF | 12 | 4 | TZ-LLM (2511.13717) |
| energy harvesting wireless sensor network DL | HF | 10 | 2 | 0 net new (LAD-BNet 1.5; Reducing Inference Energy 1.0) |
| multimodal sensor fusion edge device DL | HF | 10 | 4 | MMEdge (2510.25327); also Multi-modal On-Device Learning for Depth (2512.00086) cross-listed below |

- **pooled in-window candidates (pre-dedup)**: ~21
- **dedup**: ~3 cross-query duplicates
- **scored ≥ 2 keywords**: 4
- **adopted (final)**: **4**
- **strict-rejected at < 2 keywords (notable)**:
  - QUTE — *Quantifying Uncertainty in TinyML models with Early-exit
    ensembles* (2404.12599) — 2.0 score (`TinyML` 1.0 + `on-device
    uncertainty estimation` 1.0) but **published 2024-04-19, 11 days
    before the v6 window**. Strict-rejected on date. Strong candidate
    for re-adoption if window is widened.
  - Multi-modal On-Device Learning for Monocular Depth Estimation on
    Ultra-low-power MCUs (2512.00086, Nov 26 2025) — partial-only
    matches across 4 keywords, score ~2.0; **adopted-equivalent on
    score** but rejected here in favour of MMEdge which has cleaner
    full matches. Recorded for follow-up.
  - TPM-Based Continuous Remote Attestation for 5G VNFs (2510.03219)
    — `remote attestation` full + TPM ≠ TEE (partial 0.5) — 1.5;
    below threshold. Note: this was the paper combo A flagged as a
    sensor-attestation candidate; under v6 it does not clear the
    combo D bar either.
  - SPIDEr (2412.09222) — TEE + attestation but de-identification
    pipeline, not on-device inference; partial fit only.
  - LAD-BNet (2511.10680) — `edge inference` full only; 1.0.
- **gaps recorded as 근거 부족**:
  - **energy-harvesting wireless sensor + ML**: HF index returned
    nothing in-window that combined the harvesting and the ML side at
    the strict-keyword level. This is a real gap in the literature
    surveyed, not just a search-tool limitation.
  - **sensor (not compute) attestation**: still open after combo D.

**Search confidence**: high on TinyML / on-device inference axis,
medium on TEE/attestation axis, low on energy-harvesting axis.
