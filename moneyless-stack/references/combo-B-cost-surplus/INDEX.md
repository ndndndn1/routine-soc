# combo-B — Marginal Cost ↓ / Non-Essential Want Absorption

> v6 role: 생산 한계비용이 낮아진 만큼의 여유분을 "해도 되고 안 해도 되는
> 활동"에 배분하기 위한 부품.

## 0. Run metadata

- **run_date**: 2026-05-21
- **search_window**: 2024-05-21 → 2026-05-21 (last 2 years)
- **prior_run**: none (placeholder under prior name `combo-B-zmc-slack`,
  renamed; no prior adopted papers).
- **routine version**: v6
- **primary tools**: Google Scholar / Scopus equivalents via WebSearch
  (combo B is sociology + product-design heavy and not well-indexed by
  HF). HF `paper_search` used as supplement for `open source hardware`
  and `circular economy product design` only.
- **fallback tools used**: WebFetch attempted on Springer / Wiley /
  ScienceDirect for metadata verification — those publishers returned
  403; metadata reconstructed from Google Scholar / ResearchGate /
  PubMed mirrors.

## 1. Executive summary

Combo-B v6 has ten keywords spanning hardware (right to repair, design
for repair, design for disassembly, circular economy product design,
open source hardware, fab lab) and sociology / economics (time use
survey, non-market work, post-growth economics, time banking). The
hardware cluster compounds in two adopted papers: a 2024-2025 Discover
Sustainability review of design-for-repair features for circular
electronics (Roskladka et al.) and an ECIS 2024 paper analysing six
open-source hardware projects under a design-for-product-sustainability
lens (Brandenburger et al.). The sociology cluster does **not** compound
in the search window — each of {post-growth, time use, time banking}
returned a strong single-keyword paper (Kallis et al. 2025 Lancet
Planetary Health post-growth review; Lu et al. 2024 Innovation in Aging
timebanking quasi-experiment) but no in-window paper hits ≥ 2 sociology
keywords simultaneously. 근거 부족 on the sociology compound: adoption
threshold is honestly not met there, so those papers are listed as
*near-miss context* in §5 rather than adopted in §2. The combo's
contribution to the stack is therefore concrete (repair / disassembly /
OSHW patterns the L1 substrate must support) but does not yet supply a
measurable bridge from "low marginal cost" to "non-essential want
absorption".

## 2. Adopted papers (≥ 2 keywords matched AND ≥ 2.5 score)

### 2.1 Repairable electronic products for the circular economy: a review of design for repair features, practices and measures to contrast obsolescence

- **authors**: Nataliia Roskladka, Gianmarco Bressanelli, Nicola Saccani, Giovanni Miragliotta
- **year**: 2024 (received Jun 30, accepted Dec 09; published 2025 issue
  of Discover Sustainability)
- **venue**: Discover Sustainability (Springer Nature, open access)
- **DOI**: 10.1007/s43621-024-00753-x
- **matched_keywords** (count 4, score 3.0):
  - `design for repair` — 1.0 (literal in title; "DfR features" is the
    paper's core organising concept)
  - `circular economy product design` — 1.0 (literal "circular economy"
    + "product design" both in title; the review's frame)
  - `right to repair` — 0.5 (partial — covered as policy context driving
    DfR adoption; not the paper's mechanism)
  - `design for disassembly` — 0.5 (partial — DfR practices include
    disassembly indices and modular re-assembly; sub-theme of the
    review)
- **분류**: [공학] (engineering review of design practices)
- **방법**: Systematic literature review of repair-oriented design
  features for consumer electronics, organised by lifecycle stage and
  by countermeasure to planned obsolescence.
- **결과**: A taxonomy of design-for-repair features (modular
  architecture, screwed vs. glued joints, standardised fasteners,
  documentation, spare-parts availability) and a mapping to obsolescence
  mechanisms.
- **한계**: Consumer electronics scope; does not quantify cost or
  willingness-to-pay; policy bridge to EU Right-to-Repair Directive
  (Directive (EU) 2024/1799) cited but not analysed.
- **system reduction**: Justifies a stack-level invariant for any L1
  node that aims to be locally repairable: the BOM and the firmware
  build must expose a `repairability_class` field, populated from this
  review's taxonomy. Concretely, a future PHYSICAL_LINKS entry between
  `l1-reliability` and a producer node must carry the DfR-class of the
  producing fab.
- **[NEW]**: yes.

### 2.2 Design for Product Sustainability in a Circular Economy — Using the Example of Six Open Source Hardware Projects

- **authors**: Bonny Brandenburger, Maximilian Voigt, Simon Borgel, Magnus Busch
- **year**: 2024 (Jun, ECIS proceedings)
- **venue**: European Conference on Information Systems 2024 Proceedings,
  Green IS track
- **URL**: https://aisel.aisnet.org/ecis2024/track17_greenis/track17_greenis/25/
- **matched_keywords** (count 3, score 2.5):
  - `open source hardware` — 1.0 (literal in title; "OSHW" is the
    case-study substrate)
  - `circular economy product design` — 1.0 (literal in title:
    "Design for Product Sustainability in a Circular Economy")
  - `design for disassembly` — 0.5 (partial — disassembly / modularity
    is one of the OSHW sustainability levers analysed)
- **분류**: [사회학 + 공학] (case-study analysis with engineering examples
  and a sustainability framing; treated as 공학 for system-reduction
  purposes because the case studies are physical hardware projects)
- **방법**: Cross-case analysis of six OSHW projects (prototype-phase
  focus) coded against design-for-product-sustainability dimensions.
- **결과**: OSHW projects most strongly support sustainability where
  modularity and documentation are explicit project goals from the
  prototype phase; weak where reliance on commodity COTS parts
  re-introduces opacity.
- **한계**: Six cases, qualitative coding; no quantitative footprint
  comparison vs. closed equivalents.
- **system reduction**: Justifies, for any node implemented in the
  stack, that the design-for-sustainability decision belongs at
  prototype-time, not at productisation-time. Translates to a
  CONTRIBUTING-rule for `nodes/*`: an L1 node's first commit must
  include its BOM and modularity diagram, not just code. (No
  PHYSICAL_LINKS entry derived directly.)
- **[NEW]**: yes.

## 3. Hypothesis score (1–5, 부품 가치 점수)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable | 2 | DfR review constrains how the infra can be built such that local repair stays possible; partial support. |
| (b) Surplus absorbs non-essential wants | 1 | Sociology compound did not clear the threshold — adopted papers do not measure how surplus flows into non-essential activity. The post-growth literature exists (Kallis et al. 2025 in §5) but is single-keyword. **근거 부족**. |
| (c) Consensus from measurement directly | — | out of scope for combo-B. |

**Aggregate**: combo-B supplies the **producer-side constraints** that
make a moneyless stack feasible (repair-able, disassemble-able,
open-documented hardware) but does **not** yet supply the
measurement-side argument that surplus reliably absorbs non-essential
wants. The premise of sub-hypothesis (b) is currently load-bearing on
ROADMAP-level argument, not on cited literature. Honest read.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords** (to re-enter later, especially on the
sociology axis):

- repair cafe network (concrete instance of time-bank-adjacent practice)
- universal basic services
- household production satellite account (a time-use-survey extension)
- commoning literature
- foundational economy

**Two under-explored adjacent fields**:

- Care-work economics — closest empirical evidence for "non-market work
  absorbing surplus time"; Kallis et al. 2025 cites this literature but
  it did not surface directly in our search.
- Repair-cafe / fixit-clinic ethnographies — qualitative evidence that
  time-banking-like arrangements actually pull in the surplus.

## 5. Search log (and near-miss notes)

| keyword query (v6) | tool | results | in-window | pooled |
|---|---|---|---|---|
| right to repair electronics policy 2024-2025 | WebSearch | 8 | 5 | mostly news/policy, 1 academic context |
| design for disassembly circular economy product | HF | 6 | 3 | 3 |
| open source hardware fab lab distributed manufacturing | HF | 10 | 4 | 4 |
| time use survey non-market work 2024-2025 | WebSearch | 8 | 6 | India/Latin-America national reports + 1 Hong Kong study |
| post-growth degrowth 2024-2025 journal | WebSearch | 9 | 7 | Lancet Planetary Health review + Ecological Economics reviews |
| time banking community currency mutual aid 2024-2025 | WebSearch | 9 | 6 | Hong Kong quasi-experimental study + Urumqi case |
| fab lab sustainability circular economy 2024-2025 | WebSearch | 8 | 4 | weak — fab-lab papers mostly are >2y old or are conference recaps |
| digital product passport EU regulation 2024-2025 | WebSearch | 10 | 8 | bridges to combo-C; one DPP paper compounds in combo-C, not here |
| design for repair design for disassembly 2024-2025 paper | WebSearch | 8 | 6 | Roskladka review surfaced + Sustainable Production and Consumption 2025 |
| open source hardware circular economy 2024-2025 | WebSearch | 9 | 5 | Brandenburger ECIS paper surfaced + supporting reviews |

- **pooled after in-window filter, pre-dedup**: ~50
- **candidates scored ≥ 2 keywords**: 4
  - 10.1007/s43621-024-00753-x (4 kw, 3.0) ✓ adopted
  - ECIS 2024 Brandenburger et al. (3 kw, 2.5) ✓ adopted
  - arXiv:2504.17249 Berkeley Humanoid Lite (2 kw, 1.5) — rejected
  - arXiv:2405.10452 Public Attention Circular Economy (2 kw, 1.0) — rejected
- **rejected at < 2.5**: 2 borderline (above) + ~15 single-keyword hits.

**Near-miss papers (cited as context, NOT adopted — single-keyword
matches only):**

- Kallis G, Hickel J, O'Neill DW, Jackson T, Victor PA, Raworth K,
  Schor JB, Steinberger JK, Ürge-Vorsatz D. (2025). "Post-growth: the
  science of wellbeing within planetary boundaries." Lancet Planetary
  Health, 9(1):e62-e78. DOI: 10.1016/S2542-5196(24)00310-3. Single-
  keyword match on `post-growth economics`. Synthesised review; relevant
  but not multi-keyword.
- Lu S, Chui C, Lum T, Liu T, Wong G, Chan W. (2024). "Promoting Late-
  Life Volunteering With Timebanking: A Quasi-Experimental Mixed-
  Methods Study in Hong Kong." Innovation in Aging, 8(7):igae056. DOI:
  10.1093/geroni/igae056. Strong on `time banking`; partial on `non-
  market work` (volunteering). Total 1.5 — does not clear adoption.
- Directive (EU) 2024/1799 on the Right to Repair (2024-06-13).
  Regulatory artifact, not a paper; cited as the policy context behind
  Roskladka et al.

**Search confidence**: medium on the hardware-engineering cluster
(saturated, repeated hits). **Low** on the sociology cluster — search
is finding the canonical recent papers but each cleanly maps to **one**
v6 keyword. The v6 keyword set as currently scoped under-counts
sociology compounds; per routine rule "키워드 확장 금지", we record this
as 근거 부족 rather than synthesise a workaround.
