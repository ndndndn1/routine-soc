# combo-D — In-Node Judgment (Move Judgment to the Sensor)

System role: keep the decision local — finish the inference, the
uncertainty estimate, and the attestation inside or next to the sensor
so the link upward is a *decision*, not a sensor stream. Reduces
bandwidth, reduces the trust surface, makes the per-node output
something the upper layer can ratify rather than re-derive.

## 0. Run metadata

- **run_date**: 2026-06-04
- **search_window**: 2024-06-04 → 2026-06-04
- **prior_run**: none (v6 first run for this combo)
- **routine_version**: Research Routine v6
- **primary tool**: Hugging Face `paper_search` (HF index is strong on
  TinyML / on-device inference / TEE; weaker on in-sensor analog).

## 1. Executive summary

TinyML and on-device inference are the loud half of this combo's
literature, and they have stabilised into deployable artefacts on
microcontroller-class hardware (TinyNav 2026 is end-to-end). The TEE
literature is also maturing toward edge-AI use cases (GNNVault 2025
puts a GNN inside an SGX enclave on the edge device). Two papers
clear the threshold; both are concretely about *moving judgment to
the device* — one by making the model fit, one by making the model's
execution attestable. In-sensor / near-sensor analog computing
remains a 2022-vintage literature with little new published in the
two-year window. The bandwidth-reduction case (TinyML) and the
trust-surface case (TEE-on-edge) are both made; what is *not* made
is the on-device *uncertainty* case — surveyed UQ work targets cloud
or GPU deployment, not microcontroller deployment. That is the open
problem this combo carries forward.

## 2. Adopted papers (≥ 2 matches AND ≥ 2.5 score)

### 2.1 TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers

- **authors**: Pooria Roy, Nourhan Jadallah, Tomer Lapid, Shahzaib Ahmad,
  Armita Afroushe, Mete Bayrak
- **year**: 2026-03-10
- **venue**: arXiv preprint
- **arxiv**: 2603.11071 · https://hf.co/papers/2603.11071
- **matched_keywords**:
  - TinyML (full — title and frame) = 1.0
  - on-device inference (full — entire pipeline runs on ESP32) = 1.0
  - edge inference (partial — microcontroller is the extreme-edge
    case of edge inference) = 0.5
  - sensor fusion (partial — depth-data input fused with control
    output, paper handles the sensor → action loop) = 0.5
  - **Total = 3.0, matches = 4**
- **classification**: [공학]
- **summary**:
  - **방법**: Lightweight quantised 2D CNN runs on an ESP32-class MCU,
    taking depth-camera input and producing steering + throttle
    commands as the *only* outputs.
  - **결과**: Achieves real-time latency on the MCU; correlation
    analysis and Grad-CAM show the model is using physically plausible
    depth features.
  - **한계**: Single-task (navigation); no uncertainty estimate on the
    control output; no attestation of the model running on the device.
- **system reduction**: Justifies that an `l1-reliability` node can
  collapse a sensor stream all the way to a decision *on the
  microcontroller itself*. The link upward then needs to carry only the
  decision, which is the bandwidth-saving precondition the combo set
  out to confirm. Add an uncertainty head (combo-A) and an attestation
  (2.2 below) and the L1 endpoint is the full triple
  `(decision, uncertainty, attestation)`.
- **[NEW]**: yes.

### 2.2 Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment

- **authors**: Ruyi Ding, Tianhong Xu, Aidong Adam Ding, Yunsi Fei
- **year**: 2025-02-20
- **venue**: arXiv preprint
- **arxiv**: 2502.15012 · https://hf.co/papers/2502.15012
- **matched_keywords**:
  - trusted execution environment (full — Intel SGX, partition-
    before-training inside a TEE) = 1.0
  - edge inference (full — paper title: "Edge GNN Inference") = 1.0
  - on-device inference (partial — the protected portion runs on
    the edge device) = 0.5
  - **Total = 2.5, matches = 3**
- **classification**: [공학]
- **summary**:
  - **방법**: GNNVault partitions a GNN before training into a public
    backbone and a private rectifier; the rectifier and the private
    graph stay inside an Intel SGX enclave on the edge device.
  - **결과**: Defends against link-stealing attacks without significant
    accuracy loss; demonstrates that TEE-protected partial inference
    on the edge is practical for GNN workloads.
  - **한계**: Specific to GNN architectures; SGX assumption restricts
    hardware support; no remote attestation protocol specified, only
    local enclave execution.
- **system reduction**: Justifies that the same node which holds the
  TinyML decision head can run the privacy-critical portion of that
  head inside a TEE. The pairing with TinyNav gives the architectural
  template for the L1 endpoint: lightweight CNN on the MCU for the
  open part, TEE-protected partition for the part that must be
  attested. The next step (remote attestation across nodes) is the
  open piece that combo-D could not close in this run.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra reliable | — | out of scope (combo-A). |
| (b) Surplus absorption | — | out of scope (combo-B). |
| (c) Consensus from measurement | 3 | Moving the *decision* to the sensor is now demonstrable end-to-end (TinyNav) and the *trust surface* can be reduced via TEE (GNNVault). The remaining piece — attestable decision-with-uncertainty *across* nodes — is unattested in this run. |

**Aggregate**: combo-D is the most mature of the four combos for
producing real, deployable per-node artefacts. The bottleneck is no
longer "can we run this on a microcontroller" — it is "can the
microcontroller speak a per-decision uncertainty that survives a
remote attestation". Neither was shown end-to-end in the surveyed set.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- TinyML uncertainty estimation (the explicit cross of combo-A and
  combo-D — almost nothing in the surveyed set)
- remote attestation of ML model output (vs. of binary)
- TPM-based per-decision signing (2510.03219 hints at this for 5G
  VNFs; sensor-stream variant absent)
- DICE / RIoT-style identity on MCUs
- in-sensor event camera (the 2022 in-sensor lineage updated to
  spiking / event-driven, which the v6 keyword "in-sensor computing"
  misses)

**Two under-explored adjacent fields:**
- Confidential computing for IoT (the systems-research half of TEE,
  separate from the ML-systems half this run surfaced).
- Distributed UQ — Bayesian filters across multiple low-power nodes,
  the wireless-sensor-network lineage of uncertainty-aware fusion.

## 5. Search log

| keyword | HF results | in-window | notable |
|---|---|---|---|
| TinyML | 10 | 4 | 2603.11071, 2509.19350 |
| on-device inference | 10 | 7 | 2511.13717 (TZ-LLM), 2503.23748 (THEMIS), 2502.15012 (GNNVault), 2504.15299 (D²MoE) |
| edge inference neural network | 10 | 5 | 2502.15012, 2601.08025, 2602.02439 |
| in-sensor computing | 10 | 0 | lineage is 2022 (2212.10881, 2312.10343); no in-window new work |
| near-sensor computing analog | 10 | 0 | same — 2016 / 2022 lineage |
| sensor fusion deep learning IMU | 10 | 3 | 2503.07259, 2502.05086 — useful but single-keyword for D |
| on-device uncertainty estimation | 10 | 2 | 2511.10282 (Torch-Uncertainty — not on-device) |
| energy-harvesting wireless sensor | 10 | 2 | 2505.21529 (WakeMod — wake-up radio) |
| trusted execution environment | 10 | 6 | 2502.15012, 2511.13717, 2503.23748, 2412.09222 |
| remote attestation IoT | 10 | 4 | 2510.03219 (TPM-based 5G VNF) |

- pooled in-window, pre-dedup: ~33
- after dedup: ~21
- candidates with ≥ 2 matches: 6
- adopted (≥ 2.5 score AND ≥ 2 matches): **2** (above)
- notable near-misses:
  - **arXiv:2511.13717 TZ-LLM** — TEE (1.0) + on-device (1.0) = 2.0.
    Two-match but score < 2.5; would clear if remote attestation can
    be confirmed in the body, deferred.
  - **arXiv:2503.23748 THEMIS** — TEE (1.0) + on-device (1.0) = 2.0.
    Same threshold issue.
  - **arXiv:2510.03219 TPM-Based Continuous Remote Attestation** —
    remote attestation (1.0) + sensor attestation (0.5) = 1.5.
    Single concept covered.
  - **arXiv:2505.21529 WakeMod** — energy-harvesting (1.0) +
    on-device (0.5) = 1.5. Single-domain.
  - **arXiv:2509.19350 TinyAC** — TinyML (1.0) + on-device (1.0) =
    2.0. Borderline.

**Search confidence**: medium-high. TinyML and TEE-on-edge are
well-covered in HF; in-sensor computing literature has not produced
new work in the search window (the lineage is 2016 / 2022); on-device
uncertainty estimation specifically is a genuine gap, not a tool-reach
gap.
