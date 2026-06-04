# combo-C — Resource Priority from Physical Measurement

System role: convert per-node physical measurements (exergy, mass flow,
LCA indicator, traceability event) into a *priority ordering* over
resource allocations. Not a generic governance survey — the surveyed
mechanism must map measurement → ranking.

## 0. Run metadata

- **run_date**: 2026-06-04
- **search_window**: 2024-06-04 → 2026-06-04
- **prior_run**: none (v6 first run for this combo)
- **routine_version**: Research Routine v6
- **primary tools attempted** (per v6 spec): Scopus / ScienceDirect (for
  energy/environmental journals) and arXiv cs.GT.
- **tools actually used**: Hugging Face `paper_search` for the
  voting/uncertainty side, WebSearch for exergy / DPP / LCA side
  (HF index thin on environmental engineering journals).

## 1. Executive summary

The combo splits cleanly into two halves. The *measurement* half
(exergy accounting, LCA, material flow, digital product passport,
traceability) has mature recent work in industrial-ecology and
production-engineering journals; two papers clear the threshold —
both around the Digital Product Passport, both 2025, one of them
explicitly *sensor-based* which is the system-relevant variant.
The *priority-formation* half (quadratic voting, uncertainty-weighted
decision making) is mature as theory but the surveyed in-window work
is generic — none of it consumes a physical measurement as input.
The bridge from "we measured X" to "X enters the vote weight" is
unattested in this run; that is the same gap combo-A surfaced from
the other side. Honest read: **measurement side strong, priority-
formation side present, bridge missing**.

## 2. Adopted papers (≥ 2 matches AND ≥ 2.5 score)

### 2.1 Design of a Sensor-Based Digital Product Passport for Low-Tech Manufacturing: Traceability and Environmental Monitoring in Bio-Block Production

- **authors**: Alessandro Pracucci, Matteo Giovanardi (Levery S.r.l.)
- **year**: 2025 (Sep 2025)
- **venue**: Sensors (MDPI), Vol. 25 No. 18
- **doi**: 10.3390/s25185653 ·
  https://www.mdpi.com/1424-8220/25/18/5653 (PMC12473943)
- **matched_keywords**:
  - digital product passport (full) = 1.0
  - supply chain traceability (full — "traceability and information
    accessibility across the entire product life cycle") = 1.0
  - life cycle assessment (partial — sensor data feeds LCA-style
    environmental indicators across stages A1–A5) = 0.5
  - material flow analysis (partial — bio-block production traces
    physical material flows from raw to install) = 0.5
  - **Total = 3.0, matches = 4**
- **classification**: [공학]
- **summary**:
  - **방법**: Conceptual architecture for a sensor-network-backed DPP
    in low-tech (construction) manufacturing, validated on a real
    bio-block production case. Sensors feed environmental indicators
    that populate the DPP record across product life-cycle stages.
  - **결과**: Lightweight, interoperable sensing solutions can deliver
    the data backbone that a DPP needs; environmental indicators
    derivable directly from sensor flows; barriers in low-tech sectors
    identified.
  - **한계**: Single case study; no priority-formation mechanism —
    the DPP holds data, but ranking resources by that data is out of
    scope of the paper.
- **system reduction**: Directly justifies the link
  `l1-reliability → l2-priority`: a node's sensor stream feeds an LCA-
  shaped record, which is the substrate any later priority function
  consumes. This is the closest paper in the run to the "measurement
  in, priority out" pipeline, with the priority step itself missing.
- **[NEW]**: yes.

### 2.2 Extended exergy based ecological accounting for the smelting and pressing of nonferrous metals industry in China

- **authors**: H. Qi, Z. Dong, X. You, et al.
- **year**: 2025
- **venue**: Scientific Reports (Nature Portfolio), Vol. 15 art. 44816
- **doi**: 10.1038/s41598-025-29077-0 ·
  https://www.nature.com/articles/s41598-025-29077-0
- **matched_keywords**:
  - extended exergy accounting (full) = 1.0
  - ecological footprint accounting (partial — "ecological accounting
    … based on thermodynamics law") = 0.5
  - material flow analysis (partial — applied to a metals supply
    chain at industry scale 1992–2015) = 0.5
  - thermoeconomics (partial — extended exergy framework is
    thermoeconomic in lineage) = 0.5
  - **Total = 2.5, matches = 4**
- **classification**: [공학]
- **summary**:
  - **방법**: Extended exergy accounting (EEA) applied to the Chinese
    nonferrous metals smelting/pressing sector, with exergy-based
    indicators for resource depletion, yields and emissions, time
    series 1992–2015.
  - **결과**: Quantifies industry-scale sustainability through a single
    thermodynamic numeraire; identifies which sub-flows dominate
    exergy destruction and where intervention has highest leverage.
  - **한계**: Macro-scale, retrospective; the numeraire is real but
    no real-time / node-local variant is given.
- **system reduction**: Justifies *exergy* as the candidate physical
  numeraire for a priority function. Exergy collapses heterogeneous
  resource flows to a single thermodynamic scalar — which is exactly
  what a measurement-weighted priority needs. The macro-scale of this
  paper is the gap to a node-local exergy budget; that's the next
  reduction.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra reliable | — | out of scope (combo-A). |
| (b) Surplus absorption | — | out of scope (combo-B). |
| (c) Consensus from measurement | 3 | The measurement substrate (DPP + exergy) is real and 2025-vintage; the ranking mechanism that consumes it is not in the adopted set. Score reflects substrate confirmed, mechanism deferred. |

**Aggregate**: combo-C confirms that a node-local measurement can be
encoded in a form (DPP record / exergy scalar) that a priority
function *could* consume. No surveyed work closes the loop; the loop
is the design gap shared with combo-A.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- node-local exergy budget
- DPP-driven procurement / allocation
- multi-criteria decision analysis with thermodynamic indicators
- futarchy with physical-resource oracles
- conformal prediction for resource-allocation decisions
  (links combo-A uncertainty to combo-C priority)

**Two under-explored adjacent fields:**
- Industrial symbiosis literature (where one node's waste is another
  node's input) — natural source of measurement-grounded priority
  algorithms.
- Mechanism-design with verifiable inputs (cs.GT × oracle problem) —
  the formal frame for "vote weight bound to a measurement", which
  none of the run-3 voting papers actually instantiated.

## 5. Search log

| keyword | HF results | in-window | WebSearch follow-up? |
|---|---|---|---|
| extended exergy accounting | 3 (all off-topic AI emissions) | 0 | yes — surfaces 2.2 |
| exergoeconomics | 0 | 0 | yes — confirms 2.2 lineage |
| life cycle assessment machine learning | 10 (AI-LCA only) | 4 | none of the AI-LCA papers are L2/L3 mechanisms |
| material flow analysis sustainability | 10 (AI sustainability) | 4 | yes — confirms 2.1/2.2 |
| thermoeconomics energy systems | 10 (microgrid / EMS) | 4 | none clear ≥ 2 matches |
| ecological footprint accounting | 10 (AI carbon footprint) | 4 | yes — confirms 2.2 |
| supply chain traceability blockchain | 10 | 4 | yes — surfaces 2.1 and a near-miss DPP paper |
| digital product passport | 10 | 4 | yes — 2.1 confirmed; 2.4 near-miss |
| quadratic voting mechanism design | 10 (general mechanism design) | 4 | none consumes physical measurement |
| uncertainty-weighted decision making | 10 (DeLLMa, MCGDM, etc.) | 4 | generic; not measurement-grounded |

- pooled in-window, pre-dedup: ~32
- after dedup: ~22
- candidates with ≥ 2 matches: 4
- adopted (≥ 2.5 score AND ≥ 2 matches): **2** (above)
- notable near-misses:
  - **Blockchain-based digital product passport: design principles
    and demonstration** (Int. J. Production Research, 2025,
    10.1080/00207543.2025.2464161) — DPP 1.0 + supply chain
    traceability 1.0 = 2.0. Two matches but score < 2.5. Record as
    candidate for a combo-C re-entry; the design-principles list is
    a near-direct contributor to the priority schema.
  - **Extended exergy accounting of agricultural resources in
    China's four provinces** (Sci Rep 2025, 10.1038/s41598-025-06828-7)
    — extended exergy 1.0 + material flow 0.5 = 1.5. Adjacent.

**Search confidence**: medium-high on the measurement substrate
(industrial ecology journals have stabilised on EEA / DPP /
traceability vocabulary). Low on the priority-formation half:
quadratic-voting literature is mature but the in-window work does
not bind votes to physical measurements, and the per-routine rule
**추측 금지** prevents inflating it.
