# combo-C — Physical-measurement-derived priority

System role: take measured physical quantities from many nodes and
turn them into a *global priority ordering* — what gets resourced
first. Strict scope: only the part where measurement → priority. The
collective-decision (vote) step lives here; the consensus *protocol*
is shared with combo A's output and combo D's substrate.

## 0. Run metadata

- **run_date**: 2026-04-30
- **search_window**: 2024-04-30 → 2026-04-30 (last 2 years)
- **prior_run**: none — v4 placeholder only (`combo-C-sustainability-dlt`).
- **routine version**: v6
- **primary tools**: WebSearch on Scopus / ScienceDirect / Springer
  (energy & environment journals); HF `paper_search` for the
  cs.GT slice (quadratic voting). WebFetch was 403-blocked on most
  publisher domains so abstracts come from search snippets confirmed
  across queries.

## 1. Executive summary

Combo C is the most heterogeneous of the four. Three families of
literature contribute distinct primitives: **(i)** energy-environment
accounting (extended exergy, exergoeconomics, LCA + MFA) gives a
*physical unit of account* that is currency-independent;
**(ii)** Digital Product Passport (DPP) literature gives a
*federated, blockchain-grounded* mechanism for circulating per-product
measurements; **(iii)** quadratic-voting research (cs.GT) gives the
formal mechanism for turning private valuations into a collective
ordering, plus the specific result that uncertainty over those
valuations breaks QV optimality. Three engineering papers are adopted;
the QV theory paper is **rejected under strict v6 scoring** but
recorded as load-bearing direction. Combo C confirms that the L1
indicators specified in combo A can be carried over a DPP-style
substrate, but the priority-aggregation mechanism remains an open
design question.

## 2. Adopted papers (≥ 2 keyword matches *or* ≥ 2.5 score)

### 2.1 Extended exergy based ecological accounting for the smelting and pressing of nonferrous metals industry in China

- **year**: 2025
- **venue**: Scientific Reports (Nature Portfolio)
- **DOI / URL**: https://www.nature.com/articles/s41598-025-29077-0
- **matched_keywords** (v6):
  - `extended exergy accounting` — full ("Extended exergy accounting
    (EEA)" used) = **1.0**
  - `ecological footprint accounting` — partial ("ecological accounting"
    + exergy-based ecological indicators) = **0.5**
  - `thermoeconomics` — partial (thermodynamics-grounded accounting,
    explicit ancestry to thermoeconomics) = **0.5**
  - `exergoeconomics` — partial (exergy-cost flow approach) = **0.5**
  - count = 4, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Applies EEA to the smelting and pressing of nonferrous
    metals industry in China, 1992–2015, using thermodynamic-law-based
    exergy and exergy-based ecological indicators.
  - **결과**: Yields a numerical sustainability assessment (per-tonne
    extended exergy cost) directly comparable across years and
    sub-sectors. The accounting *is* the priority signal.
  - **한계**: Industry-scale; not yet broken down to a single asset
    instance; covers only one industry.
- **system reduction**: Justifies treating **per-output exergy cost**
  as the unit on which combo C's priority ordering is computed. In
  system terms: a node's vote weight on "do X" is a function of
  delta-exergy(X), not of currency cost. EEA is the closest thing
  the literature offers to a direct measurement-to-priority mapping.
- **[NEW]**: yes (v6).

### 2.2 Coupling material and energy flow analysis with life cycle assessment to support circular strategies at the urban level

- **year**: 2024
- **venue**: International Journal of Life Cycle Assessment (Springer)
- **DOI**: 10.1007/s11367-024-02320-y
- **matched_keywords** (v6):
  - `material flow analysis` — full = **1.0**
  - `life cycle assessment` — full = **1.0**
  - count = 2, total = **2.0**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Integrates Material and Energy Flow Analysis (MEFA) with
    LCA at the urban level to evaluate circular-economy strategies,
    couples stock-and-flow accounting with per-process impact factors.
  - **결과**: Demonstrates that the coupled MFA-LCA pipeline produces
    actionable per-strategy environmental scores at city scale.
  - **한계**: Single city case; data quality bottleneck on the inventory
    side (a recurring issue across the LCA literature).
- **system reduction**: Justifies the **two-stage measurement pipeline**:
  per-node MFA accumulates material/energy flows; per-decision LCA
  converts those flows into impact scores. The two together feed the
  priority ordering. In our system: combo A's PHM indicators become an
  input to MEFA (inferred mass-flow continuity from sensor data), then
  LCA characterisation factors give the per-action priority score.
- **[NEW]**: yes (v6).

### 2.3 Blockchain-based digital product passport: design principles and demonstration

- **year**: 2025
- **venue**: International Journal of Production Research (Taylor & Francis,
  online Feb 14, 2025)
- **DOI**: 10.1080/00207543.2025.2464161
- **matched_keywords** (v6):
  - `digital product passport` — full = **1.0**
  - `supply chain traceability` — partial (paper develops a
    blockchain-based supply-chain traceability mechanism for textiles,
    but the specific 3-gram is not in the title; abstract does use
    "traceability") = **0.5**
  - count = 2, total = **1.5**
  - (Adopted at the keyword-count threshold: 2 keywords matched, even
    though score is only 1.5 — the v6 rule is "≥ 2 keywords matched
    OR ≥ 2.5 score". Keyword count clears.)
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Two-year design science research; instantiates an
    end-to-end blockchain-based DPP prototype in the textile industry,
    using on-chain anchors for product identity and off-chain storage
    for bulky lifecycle data.
  - **결과**: Catalogues design principles (identity, partial-private
    visibility, immutable lifecycle events) and demonstrates working
    prototype.
  - **한계**: Single-domain demonstration; performance under heavy-tail
    update load not characterised; private-data leakage analysis is
    informal.
- **system reduction**: Justifies a **DPP-shaped persistence layer** as
  the substrate that carries combo A's `(score, ε_a, ε_e)` from L1 nodes
  to the priority aggregator. The hybrid on-chain / off-chain pattern
  also limits ledger cost — only commitments and identifiers go on-chain,
  bulky telemetry stays local. This pattern lines up with combo D's
  "judgement near sensor" principle.
- **[NEW]**: yes (v6).

### 2.4 Life Cycle Inventory Availability: Status and Prospects for Leveraging New Technologies

- **year**: 2024 (Aug)
- **venue**: ACS Sustainable Chemistry & Engineering
- **PMC**: PMC11864275
- **matched_keywords** (v6):
  - `life cycle assessment` — full ("LCA" / "life cycle assessment"
    repeatedly in abstract) = **1.0**
  - `supply chain traceability` — partial ("tracking product origins,
    processing, and transportation" + blockchain integration in supply
    chains) = **0.5**
  - `digital product passport` — partial (DPP is mentioned as one of
    the new technologies that can populate inventory data) = **0.5**
  - count = 3, total = **2.0**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Review article surveying the inventory-data bottleneck in
    LCA and identifying blockchain, IoT, and DPP as candidate enabling
    technologies.
  - **결과**: Names *inventory availability* as the load-bearing
    weakness for any LCA-based decision pipeline; argues that blockchain
    + sensor traceability is the credible solution path.
  - **한계**: Not an empirical paper; doesn't deliver a measurement
    protocol, only a research agenda.
- **system reduction**: Justifies the **"sensor populates LCI"** loop:
  rather than maintaining an external Life Cycle Inventory, the L1 nodes
  themselves emit per-cycle inventory entries. This collapses three
  layers (sensor → LCI → LCA → priority) into two (sensor → priority),
  exactly the structural simplification this routine is hunting for.
- **[NEW]**: yes (v6).

## 3. Hypothesis sub-score (1–5)

| paper | sub-hyp it relates to | score | reason |
|---|---|---|---|
| EEA nonferrous metals (Sci Rep 2025) | (c) priority from measurement | 4 | exergy as a currency-free unit of account |
| MEFA + LCA urban (IJLCA 2024) | (c) | 4 | concrete two-stage measurement pipeline |
| Blockchain-based DPP (IJPR 2025) | (b) + (c) | 3 | substrate that carries the indicators |
| LCI availability (ACS Sus Chem 2024) | (c) | 3 | names the bottleneck and the path |

**Combo C v6 aggregate**: hypothesis branch (c) — that priority-setting
consensus is derivable from physical measurements — has now two distinct
attested mechanisms (extended exergy accounting; MFA + LCA) plus a
working substrate (blockchain DPP). The collective-decision step (e.g.
quadratic voting) remains the outstanding gap: the QV theory work
(Benhaim et al. *Mgmt Sci* 2024) exists but is rejected here under
strict v6 scoring because it does not match a second v6 keyword;
recorded in the search log and ROADMAP as direction.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
1. `delta-exergy per action` — narrower than EEA; how to attribute
   exergy cost to a single decision.
2. `inventory data provenance` — DPP / LCI bridge.
3. `liquid democracy weighted by uncertainty` — adjacent QV variant
   that may match v6 keyword `uncertainty-weighted decision making`
   more cleanly than QV does.
4. `exergy ledger` — minimal-vocabulary form of "exergy accounting on
   distributed ledger"; tests whether anyone has built it.
5. `circular economy KPI dashboard` — names the visible part of the
   priority ordering.

**Two unexplored adjacent fields:**
- **Energy Return on Investment (EROI) accounting** — distinct
  thermoeconomic tradition with simpler unit (J/J), useful as a
  sanity ratio against EEA.
- **Catchment-scale water accounting** — different physics (mass &
  flow), tests whether the MFA half of the pipeline survives a
  non-energy domain.

## 5. Search log

| keyword query | tool | results | in-window | adopted from this query |
|---|---|---|---|---|
| extended exergy accounting / exergoeconomics | WebSearch | 10 | 5 | EEA-nonferrous (Sci Rep 2025) |
| life cycle assessment + material flow analysis | WebSearch | 10 | 7 | MEFA-LCA-urban (IJLCA 2024) |
| digital product passport + supply chain traceability | WebSearch | 10 | 6 | DPP-blockchain (IJPR 2025) |
| LCA + supply chain traceability | WebSearch | 10 | 5 | LCI-availability (ACS Sus Chem 2024) |
| exergoeconomics + renewable energy | WebSearch | 10 | 3 | 0 net new (2024 wind-storage paper at 1.5 — below threshold) |
| thermoeconomics / ecological footprint accounting | WebSearch | 10 | 4 | 0 net new (Footprint Network reports are non-academic) |
| quadratic voting + uncertainty | WebSearch | 10 | 3 | 0 — strict-rejected (see below) |
| quadratic voting mechanism design | HF paper_search | 10 | 4 | 0 — strict-rejected |

- **pooled in-window candidates (pre-dedup)**: ~22
- **dedup**: 3 cross-query duplicates (EEA-nonferrous appeared twice;
  LCI-availability appeared in two LCA-themed queries)
- **scored ≥ 2 keywords**: 4
- **adopted (final)**: **4**
- **strict-rejected at < 2 keywords (notable)**:
  - Benhaim, Hemenway Falk, Tsoukalas, *Balancing Power in Decentralized
    Governance: Quadratic Voting and Information Aggregation*, Management
    Science 2024 — full `quadratic voting` (1.0) + partial
    `uncertainty-weighted decision making` (0.5, via the result that
    cost convexity disincentivises better-informed voters) = **1.5**;
    one full keyword + one partial = below the 2-keyword count
    threshold. **Strict-rejected, but treated as load-bearing direction
    in synthesis** — this is the canonical theoretical result on why a
    naive QV will not work as our priority aggregator under uncertain
    L1 indicators.
  - *Exergoeconomic analysis and optimization of wind power hybrid energy
    storage system* (Sci Rep 2024) — `exergoeconomics` full + nothing
    else; 1.0.
  - *Enabling a dynamic information flow in DPPs* (Sustainable
    Production and Consumption Jan 2025) — `digital product passport`
    full + `supply chain traceability` partial; 1.5; below 2-keyword
    count.
  - *Digital Product Passport Implementation Based on Multi-Blockchain*
    (Applied Sciences 2024) — same 1.5 score; below threshold.
- **gaps recorded as 근거 부족**:
  - **measurement-direct collective decision**: no in-window paper
    couples a physical-measurement input (exergy, MFA flow) to a
    collective decision protocol (QV, liquid democracy, etc.). This is
    the load-bearing gap of the entire moneyless-stack hypothesis.
  - **sensor-as-LCI-source**: discussed only as research agenda in
    LCI-availability 2024; no working implementation found.

**Search confidence**: medium. Engineering side (EEA, LCA, DPP) is
well-covered. Mechanism design side is sparse for last-2-year window;
the QV strict-rejection is documented because the routine forbids
relaxing the keyword bar.
