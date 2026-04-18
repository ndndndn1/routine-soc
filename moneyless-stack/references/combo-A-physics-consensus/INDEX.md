# combo-A — Physics-grounded Maintenance Consensus (L1 × L3)

## 0. Run metadata

- **run_date**: 2026-04-18
- **search_window**: 2024-04-18 → 2026-04-18 (last 2 years)
- **prior_run**: none (this is the first run for combo-A)
- **task**: (a) search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic). Per-keyword
  calls, pooled, scored.
- **fallback tools not used**: Firecrawl / arXiv direct / Semantic Scholar —
  not required, HF pool was sufficient.

## 1. Executive summary

Surveying the L1 × L3 intersection yields a consistent pattern: physics-
informed PHM is maturing into deployable engine/bearing health monitors,
while decentralized consensus is splitting off from token-weighted designs
toward reputation/peer-ranking schemes. Three papers clear the ≥ 3.0
keyword threshold — two on the L1 side (PINN-based digital twins and
6G-edge industrial fault detection) and one on the L3 side (Fortytwo's
peer-ranked swarm consensus). None of them wires PHM output directly into
a ledger commit — the "oracle-problem-free sensor-to-ledger" construct the
routine is searching for is not yet attested in the surveyed literature.
What *is* attested: (a) engine/bearing PHM indicators reproducible with
physics priors and small data, and (b) a consensus substrate that accepts
heterogeneous per-node confidences without requiring a native token.
The honest read is **partial confirmation of direction, no confirmation
of the full L1→L3 bridge**; the bridge remains an open design problem.

## 2. Adopted papers (≥ 3.0 matched)

### 2.1 A Digital Twin for Diesel Engines: Operator-infused Physics-Informed Neural Networks with Transfer Learning for Engine Health Monitoring

- **authors**: Kamaljyoti Nath, Varun Kumar, Daniel J. Smith, George Em Karniadakis
- **year**: 2024 (Dec 16)
- **venue**: arXiv preprint
- **arxiv**: 2412.11967 · https://hf.co/papers/2412.11967
- **matched_keywords**: physics-informed (1.0), digital twin (1.0),
  prognostics health management (0.5 — partial via "health monitoring"),
  predictive maintenance (0.5 — partial via engine health prediction
  context). **Total: 3.0**
- **classification**: [공학 = 실행안]
- **summary (3–5 sentences)**:
  - **[방법]** A PINN with a deep operator network (DeepONet) is trained
    on a mean-value diesel engine model, then adapted via multi-stage and
    few-shot transfer learning to unseen operating regimes.
  - **[결과]** The operator-infused PINN identifies engine parameters and
    produces health indicators with better generalisation and lower
    compute cost than pure data-driven baselines.
  - **[한계]** Results remain on a simulated diesel engine; cross-engine
    transferability and online operation under sensor noise are not
    established.
- **L-mapping**: L1 primary. Weak L3 adjacency (health indicator could
  feed a consensus vote, but paper does not implement this).
- **system reduction**: Justifies an `l1-reliability` node whose first
  callable function is `health_indicator(sensor_window) → (score, uncertainty)`
  grounded in a physics-prior residual. Candidate for a later task (b)
  reducing the paper to a ~30-line degradation-residual module.
- **[NEW]**: yes (first run).

### 2.2 6G-Enabled Digital Twin Framework for Real-Time Cyber-Physical Systems: An Experimental Validation with Industrial Bearing Fault Detection

- **authors**: Vaskar Chakma, Wooyeol Choi
- **year**: 2025 (Oct 04)
- **venue**: arXiv preprint
- **arxiv**: 2510.03807 · https://hf.co/papers/2510.03807
- **matched_keywords**: digital twin (1.0), edge AI (1.0),
  predictive maintenance (0.5 — partial, bearing fault detection task),
  fault tolerant (0.5 — partial via fault-detection/classification).
  **Total: 3.0**
- **classification**: [공학 = 실행안]
- **summary (3–5 sentences)**:
  - **[방법]** A 6G-terahertz + intelligent-reflecting-surface testbed
    streams sensor data from industrial bearings to an edge-AI digital
    twin that runs a Random Forest fault classifier.
  - **[결과]** Reports ultra-low end-to-end latency and high F1 scores
    for bearing fault classification, showing the twin can keep up with
    the physical asset in real time.
  - **[한계]** Depends on 6G infrastructure that is not deployed at
    scale; the classifier is shallow (Random Forest, not PINN); no
    uncertainty calibration reported.
- **L-mapping**: L1 × L3 — L1 for the on-edge fault classifier, L3
  candidate as the digital twin is the shared state between physical
  node and observer.
- **system reduction**: Justifies a *proposed* (not yet enabled)
  physical link between `l1-reliability` and `l3-consensus` —
  specifically, "the twin's classifier output, not the raw sensor
  stream, is what crosses the link". This is the first piece of
  evidence the routine will cite when it opens that link.
- **[NEW]**: yes.

### 2.3 Fortytwo: Swarm Inference with Peer-Ranked Consensus

- **authors**: Vladyslav Larin, Ihor Naumenko, Aleksei Ivashov, Ivan Nikitin, Alexander Firsov
- **year**: 2025 (Oct 27)
- **venue**: arXiv preprint
- **arxiv**: 2510.24801 · https://hf.co/papers/2510.24801
- **matched_keywords**: decentralized (1.0),
  consensus protocol (0.5 — partial via "consensus"),
  distributed ledger (0.5 — partial via on-chain reputation),
  proof of useful work (0.5 — partial via proof-of-capability),
  verifiable computation (0.5 — partial via consensus verification).
  **Total: 3.0**
- **classification**: [공학 = 실행안]
- **summary (3–5 sentences)**:
  - **[방법]** Peers perform inference in parallel; a Bradley-Terry
    style pairwise-ranking aggregator forms consensus, weighted by
    on-chain reputation rather than a fungible token.
  - **[결과]** Outperforms majority voting on GPQA Diamond,
    LiveCodeBench, and AIME; demonstrates resilience to Sybil and
    prompt-injection style degradation.
  - **[한계]** Specific to LLM inference tasks (not sensor streams);
    the reputation signal is application-internal, not tied to a
    measured physical quantity; ledger integration is sketched, not
    formalised.
- **L-mapping**: L3 primary. L1 adjacency is only *potential* —
  nothing in the protocol today takes a physical measurement as a
  direct input.
- **system reduction**: Justifies an `l3-consensus` node whose first
  callable function is a reputation-weighted pairwise-ranking
  aggregator over `(peer_id, opinion, self_confidence)` tuples. No
  link is opened yet because the aggregator runs locally against a
  simulated peer set.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra can be made physically reliable enough | 2 | PINN/PHM papers show plausibility at device scale; system-scale MTBF arguments absent. |
| (b) Surplus resources can absorb non-essential wants | — | out of scope for combo-A; deferred to combo-B. |
| (c) Consensus can be derived from measurements directly | 2 | Peer-ranked consensus exists (Fortytwo), but none of the adopted papers wires a physical measurement straight into the vote weight. |

**Aggregate**: combo-A partially supports the premise that an L1→L3
pipeline is technically assembleable from existing building blocks,
but does **not** attest an end-to-end measurement-direct consensus.
The gap is exactly the "oracle problem": even Fortytwo's weights are
not grounded in a physical constant.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (to re-enter at a later combo-A run or combo-D):**
- sensor attestation
- remote attestation edge
- reputation grounded in error rate
- certified PHM output
- signed health indicator

**Two under-explored adjacent fields:**
- Control-theoretic MTBF aggregation for distributed systems
  (ties combo-A to combo-D hardware UQ).
- Structural health monitoring (SHM) for civil assets as a near-analog
  domain with long-horizon physics priors.

## 5. Search log

Per-keyword calls to `paper_search` (HF), 10 results each, last-2-years
filter applied post-hoc by publication date.

| keyword (query used) | results returned | in-window | pooled |
|---|---|---|---|
| physics-informed predictive maintenance | 10 | 5 | 5 |
| predictive maintenance industrial | 10 | 7 | 7 |
| federated learning edge devices | 10 | 3 | 3 |
| decentralized consensus protocol blockchain | 10 | 1 | 1 |
| prognostics health management PHM deep learning | 10 | 3 | 3 |
| edge AI sensor inference | 10 | 7 | 7 |
| reliability physics degradation model | 10 | 2 | 2 |
| digital twin industrial system | 10 | 5 | 5 |
| in-sensor computing near-sensor analog | 10 | 2 | 2 |
| stochastic computing low power hardware | 10 | 6 | 6 |
| fault tolerant distributed system | 10 | 5 | 5 |
| MTBF reliability engineering neural networks | 10 | 2 | 2 |
| distributed ledger IoT sensor trust | 10 | 3 | 3 |
| DePIN decentralized physical infrastructure networks | 10 | 6 | 6 |
| proof of useful work blockchain | 10 | 3 | 3 |
| verifiable computation machine learning zero knowledge | 10 | 6 | 6 |
| physics-informed neural network anomaly | 10 | 3 | 3 |

- **pooled after in-window filter, pre-dedup**: ~69
- **dedup (DOI/arXiv-ID + title-normalised)**: removed ~11 duplicates
  (many papers appeared in 2–3 keyword queries, e.g. 2412.11967,
  2510.03807, 2510.24801).
- **candidates scored with ≥ 2.0 keywords**: 7
- **candidates scored ≥ 3.0 and adopted**: **3** (listed above)
- **rejected at < 3.0**: included MAD-PINN (2509.23960, 2.5),
  CARLE (2510.17846, 1.5), AI-Driven Predictive Maintenance with V2X
  (2603.13343, 1.5), 6G Digital Twin for V2X Corridor (2410.00356, 2.5),
  Byzantine multi-agent reliability (2511.10400, 1.5–2.0),
  Secure decentralized inference (2407.19401, 2.0), JSTprove (2510.21024,
  1.5). Not recorded per-paper to keep this log tight; re-check in a
  later run if combo-A is re-entered.

**Search confidence**: medium. The HF index is strong on ML-flavoured
engineering but thin on pure reliability-physics and hardware-root-of-trust
literature; those keywords (MTBF, reliability physics, DePIN) returned
few in-window hits. Combo-D run is the correct place to follow up.
