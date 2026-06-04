# combo-B — Marginal Cost Reduction → Non-essential Wants

System role: where production marginal cost is driven low (repair,
distributed manufacturing, open hardware), what part of the recovered
surplus is allocated to "could-do-or-not" activities. Need a
*mechanism*, not just an argument, for the absorption.

## 0. Run metadata

- **run_date**: 2026-06-04
- **search_window**: 2024-06-04 → 2026-06-04
- **prior_run**: none (v6 first run for this combo)
- **routine_version**: Research Routine v6
- **primary tools attempted** (per v6 spec): Scopus / ScienceDirect /
  SSRN / Google Scholar — none directly accessible from this
  environment.
- **tools actually used**: Hugging Face `paper_search` (very thin
  coverage of the social-side keywords), WebSearch (Google general index)
  for the remaining queries.

## 1. Executive summary

The v6 combo-B keyword list is half engineering (right-to-repair,
design-for-repair, design-for-disassembly, open-source hardware, fab
lab, circular economy product design) and half social-science (time use
survey, non-market work, post-growth economics, time banking). Neither
half is well-covered by Hugging Face; the social-side keywords return
≤ 2 papers each, none of which clear the threshold. The web-search
fallback surfaces the engineering side better: one strong systematic
review of design-for-repair features clears 2.5 with two full and one
partial keyword hit. The honest read is **partial signal on the supply
side, no signal on the absorption-mechanism side**. The hypothesis
that "surplus from low marginal cost is absorbed by non-essential
wants" cannot be advanced from this run beyond the structural claim
that design-for-repair literature is mature enough to specify *what*
makes the supply cheap; *how* the surplus is reallocated is not in the
returned literature. Recorded as **근거 부족** for the absorption
half — not a failure of the hypothesis, a coverage gap.

## 2. Adopted papers (≥ 2 matches AND ≥ 2.5 score)

### 2.1 Repairable electronic products for the circular economy: a review of design for repair features, practices and measures to contrast obsolescence

- **authors**: (full list per Discover Sustainability; first authors
  from Università degli Studi di Brescia — see DOI page for canonical
  list)
- **year**: 2024 (accepted Dec 2024, published in Discover Sustainability)
- **venue**: Discover Sustainability (Springer Nature), open access
- **doi**: 10.1007/s43621-024-00753-x ·
  https://link.springer.com/article/10.1007/s43621-024-00753-x
- **matched_keywords**:
  - design for repair (full — paper's central construct is "DfR
    features / practices / measures") = 1.0
  - circular economy product design (full — paper title and frame) = 1.0
  - right to repair (partial — paper situates DfR against
    obsolescence and EU R2R policy context) = 0.5
  - design for disassembly (partial — DfR practices include
    disassembly-for-repair) = 0.5
  - **Total = 3.0, matches = 4**
- **classification**: [공학] (engineering systematic review with
  policy framing)
- **summary**:
  - **방법**: Systematic literature review extracting product-design
    elements (DfR features), repair practices (DfR practices) and
    repairability indicators (DfR measures), categorised against four
    types of obsolescence — mechanical, technological, service,
    relative.
  - **결과**: DfR features that contrast mechanical, technological and
    service obsolescence are well-covered in the literature; DfR
    against *relative* (consumer-perception) obsolescence is the gap.
    Produces a usable taxonomy of DfR features and measures.
  - **한계**: Review, not empirical; no quantitative LCA-style
    repair-vs-replace numbers; no mechanism for cost-recovery beyond
    "lifetime extension".
- **system reduction**: Justifies a minimal `repair_inventory` per node
  exposing the three constructs as schema fields — `(feature_id,
  practice_id, measure_id)` triples. The measure_id is the part that
  matters for combo-C: a repairability measure is a *physical* number,
  and combo-C can consume it as a resource-priority input. The DfR
  taxonomy is also the natural schema for the EU Digital Product
  Passport, which is independently surfacing in combo-C.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | — | out of scope (combo-A). |
| (b) Surplus absorbs non-essential wants | 2 | The *supply* side (repair, DfR, OSH) is well-attested; the *absorption* side (time use, non-market work, time banking) returned essentially no in-window papers from the available tools. Score reflects half-coverage. |
| (c) Consensus from measurement | — | out of scope (combo-C). |

**Aggregate**: combo-B is half-confirmed. Repairability is a real,
measurable, designed-in property — the input to a marginal-cost
reduction is *not* hand-wave. The conversion of that recovered
marginal cost into a different time-allocation pattern is not
addressed by anything in the returned set.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- repairability index (used by EU and France — concrete metric)
- modular product architecture
- spare-parts logistics for repair
- repair café (community-scale repair, social-science)
- time allocation diary studies (the social-side keyword that may
  return more than "time use survey" did)

**Two under-explored adjacent fields:**
- Industrial ecology — sits between LCA and material-flow analysis,
  closer to combo-C but with a stronger "what is the supply price?"
  framing.
- Solidarity economy / mutual aid networks — the social-science
  literature where time banking actually lives; not on the indices
  used here.

## 5. Search log

Per-keyword calls to `paper_search` (HF), 10 results each, plus
WebSearch fallback for keywords where HF returned ≤ 2 in-window.

| keyword | HF results | in-window | WebSearch follow-up? |
|---|---|---|---|
| right to repair electronics | 1 | 0 | yes — surfaces 2.1 (Springer) and policy reviews |
| design for repair maintenance | 10 (mostly off-topic UI/CAD) | 1 | yes — confirms 2.1 |
| design for disassembly recycling | 10 (mostly robotics datasets) | 1 | none beyond 2.1 |
| circular economy product design | 10 | 3 | none new |
| open source hardware | 10 (mostly LLM-for-hardware) | 2 | yes — 2025 Fraunhofer/ScienceDirect review surfaced but did not clear threshold solo |
| fab lab distributed manufacturing | 6 | 1 | none |
| time use survey household labor | 1 | 0 | no useful additions |
| non-market work unpaid labor | 0 | 0 | no useful additions |
| post-growth economics degrowth | 6 (mostly off-topic) | 0 | no useful additions |
| time banking community currency | 2 | 1 (community currency network, single keyword only) | no useful additions |

- pooled in-window, pre-dedup: ~9
- after dedup: ~7
- candidates with ≥ 2 matches: 2
- adopted (≥ 2.5 score AND ≥ 2 matches): **1** (above)
- notable near-misses:
  - **Sustainability Through Open-Source Hardware: A Review**
    (ScienceDirect 2025, S2212827125008236) — open source hardware
    1.0 + design for repair 0.5 + circular economy 0.5 = 2.0.
    Borderline; record as candidate for a combo-B re-entry once we
    can hit ScienceDirect for the abstract.
  - **Topological Components in a Community Currency Network**
    (arXiv:2409.13674) — time banking 0.5 only. Single keyword.

**Search confidence**: low for the social-science half of the combo
(the absorption-mechanism side), medium for the engineering half (the
supply side). The keyword list itself is sound; the tool reach is the
constraint. Per routine: **추측 금지** — recording 근거 부족 for the
social half rather than inflating with weak matches.
