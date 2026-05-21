# combo-C — Physical Measurement → Resource Priority

> v6 role: 여러 노드의 물리 측정값을 종합해 "무엇을 먼저 할 것인가"를
> 결정하는 부품. 거버넌스 일반론이 아니라 "측정값이 우선순위로 바뀌는
> 메커니즘"에 한정.

## 0. Run metadata

- **run_date**: 2026-05-21
- **search_window**: 2024-05-21 → 2026-05-21 (last 2 years)
- **prior_run**: none (placeholder under prior name
  `combo-C-sustainability-dlt`, renamed; no prior adopted papers).
- **routine version**: v6
- **primary tools**: WebSearch (Google Scholar / Wiley / Springer
  surfaces) for sustainability accounting + DPP literature; HF
  `paper_search` for the quadratic-voting and uncertainty-weighted
  decision-making queries.
- **fallback tools used**: WebFetch attempted on Wiley / Springer /
  ScienceDirect — 403; metadata reconstructed from Google Scholar /
  ResearchGate citation pages.

## 1. Executive summary

Combo-C compounds best on the **Digital Product Passport (DPP) cluster**
under the EU Ecodesign for Sustainable Products Regulation (Reg. (EU)
2024/1781) and the **extended exergy accounting** cluster as applied to
heavy industry. Three DPP-LCA papers from 2025 each compound a digital
product passport + life cycle assessment match (plus partial supply-
chain-traceability or material-flow-analysis matches); one Scientific
Reports 2025 paper applies extended exergy accounting to the Chinese
nonferrous-metals industry, compounding with ecological footprint
accounting and thermoeconomics. The **quadratic-voting** and
**uncertainty-weighted decision-making** keywords return strong single-
keyword papers (arXiv:2504.12859 on QV for blockchain governance;
Khorshidi & Aickelin on MCGDM under uncertainty) but do **not** compound
with the sustainability cluster — the two halves of combo-C live in
separate literatures. The honest read: combo-C provides a **measurement
ontology** (exergy + LCA + DPP) that can be plugged into the L1→L2 hand-
off, but the **decision aggregation** half (how those measurements get
turned into a vote) is not yet attested in the surveyed pool. That gap
mirrors combo-A's attestation gap, and is the routine's largest
remaining open question.

## 2. Adopted papers (≥ 2 keywords matched AND ≥ 2.5 score)

### 2.1 Exploring the value ecosystem of digital product passports

- **authors**: A. Gieß, F. Möller
- **year**: 2025
- **venue**: Journal of Industrial Ecology, 29:561-573
- **DOI**: 10.1111/jiec.13621
- **matched_keywords** (count 3, score 2.5):
  - `digital product passport` — 1.0 (literal in title; e3-value
    modelling of the DPP ecosystem)
  - `supply chain traceability` — 0.5 (partial — DPP-as-boundary-object
    spans manufacturer ↔ supplier ↔ EOL actor; traceability mechanism
    but term not literal)
  - `life cycle assessment` — 0.5 (partial — life-cycle product data is
    the DPP's payload; LCA term used in the literature review section)
  - `circular economy product design` — 0.5 (partial — DPP is positioned
    as a CE enabler; not the design focus)
- **분류**: [공학 + 사회학] (information systems analysis of an
  inter-organizational artifact; treated as 공학 for stack-reduction)
- **방법**: e3-value modelling of the DPP value ecosystem; identifies
  actors (manufacturer, supplier, consumer, EOL actor, regulator), their
  value exchanges, and the boundary-object role of the passport itself.
  Battery passport (under EU Battery Regulation) used as concrete
  application.
- **결과**: A schematic of which actor needs which DPP field at which
  lifecycle stage; identifies the data-quality gradient (manufacturer
  has rich data; EOL actor has degraded data).
- **한계**: Conceptual; no field deployment; battery passport scope
  only.
- **system reduction**: Justifies a `data_schema` constraint for any
  inter-node link that carries product-state data: the schema must align
  with the DPP boundary-object structure (5 actor classes, lifecycle-
  stage indexed). Concretely, a future `l2-entropy-buffer` ↔
  `l3-priority` link will inherit this schema.
- **[NEW]**: yes.

### 2.2 Development of a Decentralized Digital Product Passport for Enhanced Lifecycle Management of Electrical and Electronic Equipment

- **authors**: (ScienceDirect S2212827125002860 — Procedia CIRP 2025)
- **year**: 2025
- **venue**: Procedia CIRP (ScienceDirect)
- **identifier**: ScienceDirect PII S2212827125002860
- **matched_keywords** (count 3, score 2.5):
  - `digital product passport` — 1.0 (literal in title)
  - `life cycle assessment` — 1.0 (literal — abstract states the DPP is
    designed to feed LCA: "conducting a life cycle assessment still
    necessitates acquiring additional data...this gap" is the paper's
    target)
  - `supply chain traceability` — 0.5 (partial — blockchain-based data
    sharing IS supply-chain traceability mechanism; term not literal)
- **분류**: [공학]
- **방법**: Tree-structured hierarchical XML schema for EEE-class
  products; data digitisation via XML; blockchain (unspecified L1) for
  secure decentralised storage and sharing across the supply chain.
- **결과**: A prototype DPP for one EEE class with LCA-ready data
  granularity.
- **한계**: Single product class; XML/blockchain choices not justified
  against alternatives; performance / cost not measured.
- **system reduction**: Demonstrates that a DPP can be implemented
  without a centralised registrar — relevant because the moneyless
  stack's `l3-priority` cannot assume one. Justifies a **decentralised
  schema-registry** pattern for inter-node measurement exchange.
- **[NEW]**: yes.

### 2.3 The Role of Life Cycle Assessments in Digital Product Passport Implementation for Building a Plastic Circular Economy

- **authors**: T. Tabata, P. Tsai
- **year**: 2025
- **venue**: Circular Economy and Sustainability, 5:3145-3157
- **DOI**: 10.1007/s43615-025-00552-0
- **matched_keywords** (count 3, score 2.5):
  - `life cycle assessment` — 1.0 (literal in title)
  - `digital product passport` — 1.0 (literal in title)
  - `material flow analysis` — 0.5 (partial — plastic-CE flow analysis
    is the implicit substrate; "various combinations of methodologies"
    for each circular-economy stage)
- **분류**: [공학]
- **방법**: Maps each circular-economy stage for plastics to its required
  LCA inputs; identifies which inputs a DPP can supply directly vs.
  which must be reconstructed.
- **결과**: A gap-analysis matrix (stage × LCA-input) showing where DPPs
  are most leverageable for plastic circularity.
- **한계**: Plastics-specific; LCA methodology comparison left
  qualitative.
- **system reduction**: Provides the concrete mechanism by which
  measurement (DPP field) is turned into priority (LCA-driven recovery
  pathway). Justifies an interface contract for `l3-priority`:
  `dpp_field → lca_input → recovery_priority_score`.
- **[NEW]**: yes.

### 2.4 Extended exergy based ecological accounting for the smelting and pressing of nonferrous metals industry in China

- **authors**: H. Qi, Z. Dong, X. You, et al.
- **year**: 2025
- **venue**: Scientific Reports, 15:44816
- **DOI**: 10.1038/s41598-025-29077-0
- **matched_keywords** (count 4, score 2.5):
  - `extended exergy accounting` — 1.0 (literal in title; "EEA" applied
    longitudinally 1992-2015 to the industry)
  - `ecological footprint accounting` — 0.5 (partial — "ecological
    accounting" framing; exergy-based variant of footprint accounting)
  - `thermoeconomics` — 0.5 (partial — exergy-based industrial
    sustainability indicators sit in thermoeconomics; not the paper's
    title term)
  - `exergoeconomics` — 0.5 (partial — adjacent concept; the paper does
    not invoke it directly but EEA is its lineage)
- **분류**: [공학]
- **방법**: Apply EEA to time-series industry data; convert non-energy
  inputs (labour, environmental remediation) into equivalent exergy;
  derive industry-level sustainability indicators.
- **결과**: A trajectory of nonferrous-metals industry "ecological cost"
  in exergy units; identifies which sub-sectors are improving and which
  are not.
- **한계**: Historical data (1992-2015); single national industry;
  assumes EEA conversion factors are stable.
- **system reduction**: Justifies an exergy-denominated unit for the
  L3 priority computation — i.e. "measure value in exergy, not in
  currency, not in CO₂-equivalent only". Provides the canonical example
  the routine's premise (c) needs: a single physical quantity (exergy)
  that aggregates labour, materials, and environmental cost.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5, 부품 가치 점수)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable | 2 | LCA / exergy literature lets you measure reliability cost; not a reliability mechanism itself. |
| (b) Surplus absorbs non-essential wants | 2 | DPP work hints at a data substrate for measuring surplus, but combo-B owns the absorption side. |
| (c) Consensus from measurement directly | 4 | Combo-C is **the** load-bearing combo for premise (c). DPP-LCA papers supply the measurement transport; the Qi et al. EEA paper supplies the aggregation unit. What is **missing**: a paper that puts the aggregated exergy value into a voting / prioritisation mechanism. The quadratic-voting literature does not bridge to exergy. |

**Aggregate**: combo-C gets two-thirds of the premise (c) machinery:
**measurement schema** (DPP) + **aggregation unit** (extended exergy).
The third piece — **vote / decision rule** — is currently a literature
gap. The closest published candidates (QV-style mechanisms, MCGDM under
uncertainty) live in computer-science and management-science
literatures that have not yet absorbed exergy accounting.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords**:

- exergy-weighted voting (bridge term — does not currently exist as a
  search-results phrase; check arXiv cs.GT in 6 months)
- multi-criteria decision-making exergy
- non-monetary scarcity index
- battery passport ledger (concrete sub-instance of DPP)
- LCA-driven prioritisation algorithm

**Two under-explored adjacent fields**:

- Ecological-economics empirical literature (the Lancet PH 2025 review's
  citation list contains exergy/material-flow papers our HF index
  missed).
- Cooperative-game theory on commons allocation — the formalism that
  could absorb an exergy-denominated payoff.

## 5. Search log

| keyword query (v6) | tool | results | in-window | pooled |
|---|---|---|---|---|
| extended exergy accounting industrial | HF | 5 | 3 | 3 |
| exergoeconomics thermoeconomics energy systems | HF | 10 | 6 | 6 |
| life cycle assessment supply chain emissions | HF | 10 | 7 | 7 |
| material flow analysis resource circularity | HF | 10 | 4 | 4 |
| ecological footprint planetary boundary accounting | HF | 10 | 5 | 5 |
| supply chain traceability blockchain | HF | 10 | 6 | 6 |
| digital product passport traceability circular | HF | 4 | 1 | 1 (HF index thin on DPP) |
| digital product passport life cycle assessment 2024-2025 | WebSearch | 10 | 8 | 8 |
| extended exergy 2024-2025 | WebSearch | 7 | 4 | 4 |
| quadratic voting mechanism public goods | HF | 10 | 4 | 4 |
| uncertainty-weighted decision making prioritization | HF | 10 | 6 | 6 |
| quadratic voting experiment governance 2024-2025 | WebSearch | 9 | 6 | 6 |

- **pooled after in-window filter, pre-dedup**: ~62
- **dedup**: ~14 duplicates (DPP papers in 3-4 queries each).
- **candidates scored ≥ 2 keywords**: 6
  - jiec.13621 Gieß & Möller DPP value ecosystem (3-4 kw, 2.5) ✓ adopted
  - S2212827125002860 Decentralized DPP for EEE (3 kw, 2.5) ✓ adopted
  - s43615-025-00552-0 Tabata & Tsai LCA in DPP for plastic CE (3 kw, 2.5) ✓ adopted
  - s41598-025-29077-0 Qi et al. EEA nonferrous metals (4 kw, 2.5) ✓ adopted
  - arXiv:2509.00093 More than Carbon (3 kw, 2.0) — rejected, just under
  - arXiv:2512.04142 From FLOPs to Footprints (2 kw, 1.0) — rejected
- **rejected at < 2.5**: 2 borderline + ~15 single-keyword hits.

**Near-miss papers (single-keyword, NOT adopted):**

- arXiv:2504.12859 "Enhancing Decentralization in Blockchain Decision-
  Making Through Quadratic Voting and Its Generalization" (2025).
  Strong `quadratic voting` (1.0); 0.0 on the sustainability cluster.
- Khorshidi & Aickelin (2020), MCGDM under interval-data uncertainty —
  out of window but the canonical reference for the
  `uncertainty-weighted decision making` keyword.

**Search confidence**: high on DPP / LCA / extended exergy axes
(saturated, multiple compounding hits). **Medium** on `material flow
analysis` and `ecological footprint accounting` — these are textbook
terms whose practitioners publish in ecological-economics journals not
well-covered by HF; the WebSearch supplements were sparse on direct
hits. **Low** on the bridge from sustainability accounting to voting
mechanisms — this combination does not appear in literature.
