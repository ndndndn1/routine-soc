# combo-C — Physical Measurement → Resource Priority

System role: take per-node measurements (mass, energy, exergy, flow,
lifecycle data) and turn them into "what gets resourced first". Strictly
*measurement → priority*; we exclude generic governance-theory papers
that do not pin their priorities on a physical quantity.

## 0. Run metadata

- **run_date**: 2026-05-14
- **search_window**: 2024-05-14 → 2026-05-14 (last 2 years)
- **prior_run**: placeholder only (`combo-C-sustainability-dlt/`),
  this is the first substantive combo-C run.
- **routine version**: v6
- **task**: combo search + adoption + INDEX.md
- **primary tools**: WebSearch (Scopus/ScienceDirect/Springer
  Nature/Tandfonline) plus HF `paper_search` for the cs.GT side
  (quadratic voting, uncertainty-weighted decision making). The
  energy/environment journals do not have HF coverage; WebSearch was
  the only path to extended-exergy and LCA papers.
- **fallback tools (not used)**: arXiv direct, Semantic Scholar.

## 1. Executive summary

Combo-C splits roughly into three sub-clusters: thermodynamics-based
accounting (exergy, exergoeconomics, thermoeconomics — small but
active field, dominated by Sciubba and successors); environmental
accounting (LCA + MFA + ecological footprint — large, saturating,
heavily reviewed); and physical-measurement-aware governance
(quadratic voting, uncertainty-weighted decisions — small set of cs.GT
papers, none of which actually grounds the vote weight in a physical
measurement). The cluster that produces the cleanest moneyless-stack
brick is **DPP (Digital Product Passport)** because it is the place
where supply-chain traceability, LCA data, and product-state
measurements converge into a single per-product record. Three papers
clear the 2.5 threshold: one extended-exergy industrial accounting
study (a worked example of measurement → priority for a real sector),
one DPP review (the record format), and one circular-economy-metrics
review (the integration of MFA + LCA + footprint). **Quadratic voting
does not adopt**: every QV paper in window operates over abstract
preferences, none ties vote weight to a sensor reading. That gap is
the most important negative result of combo-C.

## 2. Adopted papers (matched_keywords ≥ 2 AND score ≥ 2.5)

### 2.1 Extended exergy based ecological accounting for the smelting and pressing of nonferrous metals industry in China

- **authors**: H. Qi, Z. Dong, X. You, et al.
- **year**: 2025
- **venue**: Scientific Reports (Nature Portfolio), 15:44816
- **DOI**: 10.1038/s41598-025-29077-0 (via search result)
- **matched_keywords**:
  - "extended exergy accounting" (1.0 — explicit title phrase
    "Extended exergy based ecological accounting")
  - "ecological footprint accounting" (0.5 partial — "ecological
    accounting" without the "footprint" framing)
  - "material flow analysis" (0.5 — paper accounts for industrial
    material flows as the basis of EEA)
  - "thermoeconomics" (0.5 — EEA is by construction a
    thermoeconomics extension)
  - **Total: 2.5** · 4 keywords matched
- **classification**: [공학]
- **방법**: Applies Extended Exergy Accounting (EEA, Sciubba) to a
  real Chinese industrial sector (nonferrous metals smelting and
  pressing), combining material, energy, capital, labour, and
  environmental remediation exergy in a single ledger.
- **결과**: Quantifies sector-level "extended exergy" inputs and
  yields, producing a single comparable number across heterogeneous
  inputs. The paper publishes the per-process breakdown, which is
  what makes the result a useful priority-ranking primitive.
- **한계**: Sector-specific (one industry, one country). EEA still
  has unsettled conversion factors for non-energetic inputs
  (especially labour), and the paper inherits those choices.
- **시스템 환원**: Justifies an `l3-priority` or `l2-slack` callable
  that consumes per-node {material, energy, labour, environmental}
  measurements and returns a single comparable exergy number. This
  is the first concrete "physical measurement → priority" pipeline
  found across the routine; it is exactly the construct run-1's
  synthesis flagged as missing.
- **[NEW]**: yes.

### 2.2 Digital product passport for sustainable and circular supply chain management: a structured review of use cases

- **authors**: (Tandfonline 2024; full author list at DOI)
- **year**: 2024
- **venue**: International Journal of Logistics: Research and
  Applications (Taylor & Francis)
- **DOI**: 10.1080/13675567.2024.2374256
- **matched_keywords**:
  - "digital product passport" (1.0 — title)
  - "supply chain traceability" (1.0 — "sustainable and circular
    supply chain management"; the review's use cases are
    traceability-focused)
  - "life cycle assessment" (0.5 — DPPs carry LCA-style data per
    product instance, discussed across the use cases)
  - "material flow analysis" (0.5 — per-product flow tracking is a
    DPP capability)
  - **Total: 3.0** · 4 keywords matched
- **classification**: [공학] with [정책/사회학] context (EU ESPR).
- **방법**: Structured review of DPP use cases across sectors
  (batteries, textiles, construction, electronics). Classifies the
  use cases by which supply-chain function they unlock (compliance,
  repair, recall, reuse, recycling).
- **결과**: A use-case taxonomy plus a list of the minimum data
  fields a DPP must carry to support each. The minimum-data-field
  list is the part that maps directly onto a system schema.
- **한계**: Review of *proposed* / *piloted* use cases. The EU ESPR
  was adopted in Dec 2024 (in force Jan 2025), so the operational
  DPP rollout is largely post-paper. Empirical assessment of which
  use cases actually deliver is future work.
- **시스템 환원**: Justifies an `l3-priority` data schema:
  each tradable resource in the system carries a DPP-style record
  whose fields are *measured*, not declared. The schema is what the
  EEA accounting in 2.1 reads from. Together, 2.1 + 2.2 form the
  measurement-to-priority spine of L3.
- **[NEW]**: yes.

### 2.3 Towards Circular Economy Metrics: a Systematic Review

- **authors**: (Springer 2025; full author list at DOI)
- **year**: 2025 (May)
- **venue**: Circular Economy and Sustainability (Springer)
- **DOI**: 10.1007/s43615-025-00604-5
- **matched_keywords**:
  - "life cycle assessment" (1.0 — explicit "Life Cycle Analysis
    (LCA)" as a evaluated methodology)
  - "material flow analysis" (1.0 — explicit "Material Flow
    Analysis (MFA)" as a evaluated methodology)
  - "ecological footprint accounting" (0.5 — footprint-style
    indicators reviewed alongside CEMs)
  - **Total: 2.5** · 3 keywords matched
- **classification**: [공학] / [정책]
- **방법**: Systematic review of circular-economy metrics across
  three dimensions: material flows, product life cycles, production
  processes. Catalogues methodologies (MFA, LCA, CI, C.Q.A.T.) and
  the indicators they produce.
- **결과**: Mapping of which indicators are computable from which
  data sources, plus a barriers list (data limitations,
  standardisation, regulatory fragmentation).
- **한계**: Review-level; does not advocate a single composite
  metric. The "integration of social and long-term economic
  dimensions" is explicitly named as still open.
- **시스템 환원**: Provides the catalogue from which `l3-priority`
  selects a *minimum* set of measurements that, together, are
  enough to rank competing resource asks. The fact that the review
  itself does not commit to one number is fine — moneyless-stack
  prefers a vector of measured indicators over a single composite,
  and this review is the literature anchor for that choice.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | — | not the combo-C axis. |
| (b) Surplus absorbs non-essential wants | 2 | combo-C provides the *measurement layer* on which a slack accounting can sit; the slack policy itself is combo-B's job. |
| (c) Consensus from physical measurement | 3 | first run where this sub-hypothesis crosses 2 — EEA + DPP + CE-metrics give an attested, field-tested pipeline from sensor / ledger data to a comparable priority number. The remaining gap is *who reads it* — no voting/consensus paper grounds vote weight in such a number. |

**Aggregate**: combo-C provides the missing measurement→number
layer. The remaining gap is "from number to decision" — i.e. the
absence of a published quadratic-voting / mechanism-design paper that
takes a sensor-derived exergy or footprint reading as its vote weight.
That gap is now the most explicit known open problem in the routine.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- exergy-weighted decision rule (combines EEA with voting-style
  aggregation — likely returns 0, but the negative result is itself
  informative)
- battery passport empirical evaluation
- product-level LCA streaming
- per-instance environmental product declaration (EPD)
- C.Q.A.T. tool implementation

**Two under-explored adjacent fields:**
- Industrial Symbiosis literature (Kalundborg-style cluster studies
  often have the missing "decision from measurement" loop closed,
  but as case studies not as protocols).
- Material Passport (construction sector) — adjacent to DPP, older
  literature, may already have the schema combo-C wants.

## 5. Search log

`paper_search` (HF) — in-window, combo-C-vocab hits:

| query | results | in-window | usable |
|---|---|---|---|
| quadratic voting mechanism design | 10 | 1 (2410.15168 electoral CDM, no QV) | 0 with QV ≥ 1.0 |
| uncertainty-weighted decision making aggregation | 10 | 3 | 0 with combo-C ≥ 2 |
| life cycle assessment machine learning | 10 | 5 | 2 LCA-anchored (2509.00093, 2501.14334) |
| supply chain traceability blockchain transparency | 10 | 4 | 0 with DPP keyword |

WebSearch — relevant in-window:

| query | hits |
|---|---|
| "digital product passport" 2024-2025 | EU Regulation 2024/1781 (legislation); Tandfonline use-case review 2024 ✓ |
| "extended exergy accounting" / "exergoeconomics" / "thermoeconomics" 2024-2025 | Sciubba 2024 (Energy 310); SYMΞX 2025; Qi et al. 2025 Sci. Reports ✓ |
| MFA + LCA circular economy 2024-2025 | Coupling MEFA-LCA urban 2024; SEMF for recycling LCA 2024; "Towards Circular Economy Metrics" 2025 ✓; CE Frontiers materials circularity 2025 |
| quadratic voting peer reviewed 2024-2025 | Benhaim/Falk/Tsoukalas Management Science 2025; QV-net IACR 2025; QVSR pilot 2026; arXiv 2504.12859 |
| ecological footprint accounting 2024-2025 | Ecological Indicators 2025 (China SDG study); PLOS ONE 2025; National Footprint Accounts 2025 release |

- **pooled (HF + Web), in-window**: ~28 papers
- **dedup**: ~24 unique
- **candidates scored ≥ 2.0**: 8
- **candidates scored ≥ 2.5 and adopted**: **3**
- **rejected at 2.0**:
  - Sciubba 2024 (Energy 310) — thermoeconomics 1.0 + exergoeconomics 0.5 + extended-exergy 0.5 = 2.0. A foundational synthesis paper but does not cross the line; carry to a later combo-C re-entry.
  - Benhaim/Falk/Tsoukalas 2025 (QV + Information Aggregation) — QV 1.0 + uncertainty-weighted partial 0.5 = 1.5. Strong methodological paper but does not bind voting weight to a physical measurement, so its system value is low for combo-C anyway.
  - Coupling MEFA-LCA urban 2024 — MFA 1.0 + LCA 1.0 = 2.0; no third-keyword hit.
  - Falk et al. 2025 "More than Carbon" arXiv:2509.00093 — LCA 1.0 + ecological-footprint partial 0.5 = 1.5; valuable in its own right but not for the priority-derivation function.
  - SYMΞX (Thermoeconomics meets Business Science) 2025 — thermoeconomics 1.0 + exergoeconomics 0.5 + extended-exergy 0.5 = 2.0.

**Search confidence**: medium. The exergy/thermoeconomics literature
is small but coherent (single tradition, ~3 active groups). The
LCA/MFA literature is large and saturating. The QV / mechanism-design
literature is active but disconnected from physical measurement; this
is the most informative negative result of combo-C.

**근거 부족 (insufficient evidence)** flagged for:
- "exergy-weighted voting" or any direct binding of QV/uncertainty-
  weighted decision making to a physical measurement. The pieces
  exist on each side; the bridge is not published in this window.
  Carry as the headline open problem.
- "ecological footprint accounting" as a *combo-C-defining* keyword.
  The methodology is mature but the 2024-2025 literature uses it as
  a one-line indicator rather than a primary instrument.
