# combo-B — Marginal-cost reduction → non-essential wants

System role: surface mechanisms by which a drop in production marginal
cost can be *absorbed* by activities that are "OK to do or not to do"
(reparability, reuse, distributed manufacturing, time-rich non-market
work, post-growth allocation). These are the parts of the moneyless
stack that justify the "L2 entropy buffer" — the surplus pool a node can
release into without endangering core needs.

## 0. Run metadata

- **run_date**: 2026-05-28
- **search_window**: 2024-05-28 → 2026-05-28 (last 2 years)
- **prior_run**: none (placeholder from v4 reset)
- **routine version**: v6
- **primary tool per routine**: Scopus / ScienceDirect, SSRN, Google
  Scholar — *not directly callable from this run*. Best-effort
  substitutes used: Hugging Face `paper_search` (semantic) on each
  keyword, plus targeted `WebSearch` for sociology/economics keywords
  (right to repair, time use survey, post-growth economics) to recover
  papers in Springer / ScienceDirect / Lancet / Cambridge venues.
- **search confidence**: low-to-medium. HF coverage is ML-biased and
  largely empty for the sociology end of combo-B; WebSearch surfaces
  paper *links* but the routine cannot programmatically extract their
  abstracts to score them strictly. One paper is adopted with high
  confidence (clear title-level keyword match); two more are logged as
  "near-miss high-quality, below the strict 2.5 threshold under
  abstract-unseen scoring."

## 1. Executive summary

Combo-B's evidence base is *not in the indices this routine can reach
directly*. Right-to-repair, post-growth economics, time-use surveys and
non-market work live in Springer, ScienceDirect, Lancet, Cambridge Core
and SSRN; the Hugging Face index returns essentially no relevant hits
for these terms. With that caveat, one paper clears the v6 threshold by
title alone: a 2024 Springer *Discover Sustainability* review of
"design for repair features, practices and measures to contrast
obsolescence" in electronic products for the circular economy. It hits
**design for repair, circular economy product design, right to repair,
and design for disassembly** simultaneously and is the canonical
adoption for combo-B v6. Two further high-quality 2024–2025 candidates
(Lancet Planetary Health on post-growth, Tandfonline on "slowing down
the loop" / smart-device RTR) are flagged as "below threshold under
strict scoring but worth manual review in the next combo-B run with
direct DB access." Combo-B status overall: **partial signal +
acknowledged tool gap; not yet 근거 부족, but on the line.**

## 2. Adopted papers (≥ 2 keywords, ≥ 2.5 sum)

### 2.1 Repairable electronic products for the circular economy: a review of design for repair features, practices and measures to contrast obsolescence

- **authors**: Andrea Tornese et al. (review article; full author list
  per DOI page)
- **year**: 2024
- **venue**: Discover Sustainability (Springer Nature)
- **doi**: 10.1007/s43621-024-00753-x
- **matched_keywords** (count = 4, sum = 3.0; scoring by title since
  this run cannot fetch the full abstract):
  - design for repair — 1.0 (full phrase in title)
  - circular economy product design — 1.0 (electronic products + circular
    economy + design features = full concept match in title)
  - right to repair — 0.5 (review of repair features and measures against
    obsolescence is the canonical RTR research topic)
  - design for disassembly — 0.5 (repair features for electronic products
    require disassembly affordances; concept-adjacent to the title)
- **classification**: [공학 + 사회학 hybrid] — engineering content
  (design features, obsolescence-contrast measures) embedded in a
  policy/sociology framing (circular economy review). Treated as **사회학**
  for routine purposes because it is a review, not a buildable
  reduction; ROADMAP-only update, no PHYSICAL_LINK trigger.
- **방법 (inferred from venue / title — verify on next combo-B run with
  full-text access)**: Systematic literature review of design-for-repair
  features and obsolescence-mitigation measures across electronic
  product categories.
- **결과 (inferred)**: A catalogue / taxonomy of design-for-repair
  features and a mapping to circular-economy outcomes; identifies which
  measures most reliably extend product life.
- **한계**: This adoption is title-and-venue based. The full abstract was
  not fetched in this run. *To be re-verified in the next combo-B run
  with direct ScienceDirect/Springer access.*
- **system reduction (sociology track — does not open a link)**: This
  paper does not create a node or a link. It enters ROADMAP as
  justification for the **L2 entropy-buffer direction**: surplus can be
  absorbed by lengthening the repair-replace cycle of physical assets
  rather than by monetary consumption. Concretely, it backs the design
  invariant "an L1 reliability indicator should expose repair-relevant
  state (which sub-component is degrading) not just an aggregate RUL,"
  which feeds combo-A's `per_input_group_uncertainty` direction (I-GLIDE).

## 3. Hypothesis score (1–5)

- **(a) production-side physical reliability** — out of scope.
- **(b) surplus can absorb non-essential wants** — combo-B score:
  **2/5**. One review-level paper exists that frames repair / circular
  design as the absorption channel. No measurement or modelling paper in
  the surveyed pool ties marginal-cost drop to a measured shift toward
  non-market or repair-time consumption. The L2 direction is *named*,
  not *measured*.
- **(c) priority from measurement** — out of scope.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords** (carry into next combo-B run with direct DB
access):
- repairability index (EU regulation evaluation)
- planned obsolescence empirical
- non-market work measurement methodology
- ecological macroeconomic model post-growth
- distributed manufacturing fab lab capability

**Two under-explored adjacent fields**:
- household-level time-use econometrics (US ATUS, OECD Time Use DB,
  India TUS 2024 — government-collected micro-data, not pre-prints)
- repair-café / commons-based peer production ethnography (Bauwens
  lineage, P2P Foundation outputs)

## 5. Search log

Per-keyword calls to `paper_search` (HF), `results_limit = 10`,
`concise_only = true`. Web supplements via `WebSearch` for three terms.

| keyword (query used) | tool | results | in-window | useful |
|---|---|---|---|---|
| right to repair policy electronics | HF | 0 | 0 | 0 |
| design for repair product | HF | 13 | ~5 | 0 (CAD/UI repair papers, off-topic) |
| design for disassembly circular economy | HF | 20 | 6 | 1 (PCB-Vision, off-topic) |
| circular economy product design | HF | 29 | 10 | 0 |
| open source hardware | HF | 120 | 10 | 1 (Berkeley Humanoid Lite 2504.17249, 2.0 sum — below threshold) |
| fab lab distributed manufacturing | HF | 6 | 3 | 0 |
| time use survey labor | HF | 0 | 0 | 0 |
| non-market work household production | HF | 0 | 0 | 0 |
| post-growth economics degrowth | HF | 6 | 3 | 0 |
| time banking community currency | HF | 2 | 1 | 0 (Community Currency Network 2409.13674, 0.5 sum) |
| right to repair 2024 2025 design | WebSearch | 8 links | n/a | 1 (Springer review 10.1007/s43621-024-00753-x) |
| time use survey 2024 2025 academic | WebSearch | 8 links | n/a | 0 peer-reviewed in window |
| post-growth economics 2024 2025 | WebSearch | 8 links | n/a | 2 candidate (below strict threshold; see §5 near-miss) |

- **pooled in-window, pre-dedup**: ~25
- **deduped by DOI / arXiv ID**: ~22
- **candidates with ≥ 2 keywords matched**: 3 (Springer review;
  Tandfonline RTR; Lancet post-growth)
- **adopted (sum ≥ 2.5)**: **1**
- **near-miss high-quality (below strict threshold, logged for next
  combo-B run with direct DB access)**:
  - **"'Slowing down the loop': smart devices and the right to repair"**
    — Intl. Review of Law, Computers & Technology, 2024,
    doi:10.1080/13600869.2024.2324535. Title-level matches: right to
    repair (1.0), circular economy product design (0.5 via "loop"),
    design for repair (0.5). Sum 2.0 — below threshold under strict
    title-only scoring. Likely 2.5+ with full abstract.
  - **"Post-growth: the science of wellbeing within planetary
    boundaries"** — Lancet Planetary Health, 2024,
    doi:10.1016/S2542-5196(24)00310-3. Single keyword (post-growth
    economics = 1.0) — below the ≥ 2 keyword *count* requirement, even
    though it is the canonical post-growth review of 2024. Reserved
    for ROADMAP-only mention.
  - **"Post-growth economics as a guide for systemic change: Theoretical
    and methodological foundations"** — Ecological Economics
    (ScienceDirect), 2025, S0921800925000047. Single keyword (post-growth
    economics = 1.0). Same status as the Lancet paper.

**Search confidence**: low-to-medium overall. The strict adoption
machinery requires title + abstract scoring; sociology/economics
venues are reachable by title via WebSearch but full abstracts were not
fetched in this run. The "근거 부족" label is *not yet* applied because
one paper does clear the bar by title alone; the rest is flagged as
"requires DB access" rather than "no evidence."
