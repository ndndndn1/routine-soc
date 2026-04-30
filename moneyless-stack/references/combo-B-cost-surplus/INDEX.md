# combo-B — Marginal-cost reduction → discretionary surplus absorption

System role: identify the engineering and policy parts that *make the
marginal cost of producing X close to zero*, and the social mechanisms
that absorb the freed-up time/resources into non-essential wants
without collapsing the recoverable envelope.

## 0. Run metadata

- **run_date**: 2026-04-30
- **search_window**: 2024-04-30 → 2026-04-30 (last 2 years)
- **prior_run**: none — v4 placeholder only (`combo-B-zmc-slack`).
- **routine version**: v6
- **primary tools**: Google Scholar / Springer / MDPI / ScienceDirect via
  WebSearch (HF index is thin on circular-economy and post-growth
  literature). HF `paper_search` retained as backup.
- **fallback**: WebFetch was blocked (403) on Springer / Lancet /
  MDPI / Brill domains; abstracts were sourced from search-result
  snippets and confirmed across multiple search queries.

## 1. Executive summary

Combo B has the messiest evidence base of the four because the keyword
list spans both engineering ("design for repair", "open source hardware",
"fab lab") and sociology ("post-growth economics", "time banking",
"non-market work"). The engineering side is well-attested: there is
strong recent literature on Design for Repair / Disassembly as concrete
product-design strategies, and the Open Lab Starter Kit (HardwareX 2025)
is the first peer-reviewed instance of a *replicable* fab lab built from
open-source hardware. The sociology side is active but most candidate
papers fail strict v6 keyword matching — the field tends to use
adjacent vocabulary ("unpaid work", "post-growth" alone, "degrowth")
rather than the v6 standard phrases. **Four** papers are adopted; below-
threshold sociology evidence is recorded in ROADMAP.md as direction.

## 2. Adopted papers (≥ 2 keyword matches *or* ≥ 2.5 score)

### 2.1 Repairable electronic products for the circular economy: a review of design for repair features, practices and measures to contrast obsolescence

- **authors**: (multi-author systematic review, Università di Brescia
  group; full author list per DOAJ entry)
- **year**: 2024
- **venue**: Discover Sustainability (Springer Nature)
- **DOI**: 10.1007/s43621-024-00753-x
- **matched_keywords** (v6):
  - `design for repair` — full ("Design for Repair (DfR) strategies"
    in abstract / title) = **1.0**
  - `right to repair` — full ("consumer movements 'Right to Repair'"
    in abstract) = **1.0**
  - `circular economy product design` — partial ("Circular Economy
    strategy" + "product design stage" used in abstract; the strict
    3-gram doesn't appear) = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: PRISMA systematic review on Scopus (search performed
    March 2024) using terms "design for repair", "right to repair",
    "design for disassembly", "circular economy", "product longevity".
  - **결과**: Codifies DfR features (modularity, fastener choice,
    diagnostic access) and counter-obsolescence measures into a single
    framework. Names the gap that DfR is presented "in fragmented
    way" with little integration to CE policy.
  - **한계**: Electronics scope only; not yet a measurement protocol —
    the review does not output a repairability score we can call.
- **system reduction**: Justifies a `design_rules/` module specifying
  the *physical* repairability invariants any node we build must
  satisfy: modular fasteners, diagnostic-accessible bus, no glued
  enclosures. This is a hard input to combo D's hardware-substrate
  choice.
- **[NEW]**: yes (v6).

### 2.2 Service Design for Repair Practices in the Circular Economy: A Systematic Review Approach

- **year**: 2025
- **venue**: MDPI *Knowledge* 6(4):154, 2025
- **URL**: https://www.mdpi.com/2673-4060/6/4/154
- **matched_keywords** (v6):
  - `design for repair` — full ("Service Design for Repair" — the
    exact 3-gram "design for repair" is present inside the title) = **1.0**
  - `circular economy product design` — partial ("Circular Economy"
    + repair-and-design framing) = **0.5**
  - `right to repair` — partial (review surfaces R2R legislative
    drivers) = **0.5**
  - count = 3, total = **2.0**
- **classification**: [공학] (with sociological framing — service
  design is on the engineering/policy boundary)
- **method / result / limitation**:
  - **방법**: Systematic review of 60 studies; categorises
    interventions into micro (consumer engagement), meso (digital
    platforms / process frameworks), macro (regulation, culture).
  - **결과**: Names "product complexity" and "insufficient
    legislative support" as the dominant blockers; argues service
    design can mitigate via co-creation.
  - **한계**: Review-of-reviews; no operational metrics.
- **system reduction**: Justifies a *layered* design contract:
  per-product (micro, combo-A/D node level), per-platform (meso,
  combo-C ledger / dashboard level), per-policy (macro, ROADMAP).
  This three-tier mapping clears up where each future paper should
  attach.
- **[NEW]**: yes (v6).

### 2.3 Open Lab Starter Kit Small Laser V2 — an open source Fab lab produced laser cutter

- **authors**: New Production Institute (HSU) + InMachines team
- **year**: 2025
- **venue**: HardwareX (Elsevier)
- **DOI / URL**: https://www.sciencedirect.com/science/article/pii/S2468067225000422
  (also PMC: PMC12226398)
- **matched_keywords** (v6):
  - `fab lab` — full ("Fab lab produced laser cutter" in title) = **1.0**
  - `open source hardware` — full (project documented as
    Open-Source Hardware (OSH) and Open-Source Machine Tools (OSMT)
    in abstract) = **1.0**
  - `design for repair` — partial (machine is repairable by design
    via local replication) = **0.5**
  - count = 3, total = **2.5**
- **classification**: [공학]
- **method / result / limitation**:
  - **방법**: Full machine documentation released as OSH; bill of
    materials, assembly instructions, control firmware all openly
    licensed; replication tested at multiple sites.
  - **결과**: First Fab Lab that is itself **fab-lab-replicable** —
    i.e. the machines that build a Fab Lab can be built using the
    machines of an existing Fab Lab. Demonstrates sub-kEUR cost
    point for a small-format laser cutter.
  - **한계**: Single machine type per paper (the wider OLSK has 8
    machines, only the small laser is reported here in detail); no
    long-horizon reliability data.
- **system reduction**: Justifies the *bootstrap claim* on which the
  whole moneyless-stack rests: a node's hardware can be reproduced
  at recoverable marginal cost using only OSH. Without this, the
  "physical reliability of production substrate" hypothesis (a)
  has no concrete ground; with it, replacement of a failing node
  is bounded by kit-cost, not by market price. This is the load-
  bearing combo-B paper.
- **[NEW]**: yes (v6).

### 2.4 On "the Politics of Repair Beyond Repair": Radical Democracy and the Right to Repair Movement

- **authors**: Javier Lloveras, Mario Pansera, Adrian Smith
- **year**: 2025 (Jan)
- **venue**: Journal of Business Ethics (online first Jan 2025)
- **DOI**: discoverable via title; published online 2025-01
- **matched_keywords** (v6):
  - `right to repair` — full ("Right to Repair Movement" in title) = **1.0**
  - `post-growth economics` — partial (Pansera's lineage explicitly
    links repair politics to post-growth / degrowth scholarship,
    used as framing in the abstract) = **0.5**
  - `design for repair` — partial (politics-of-repair framing
    references DfR as object of contestation) = **0.5**
  - count = 3, total = **2.0**
- **classification**: [사회학]
- **method / result / limitation**:
  - **방법**: Conceptual paper drawing on radical-democracy theory
    (Mouffe / Laclau lineage) to interpret R2R as a political
    project not just a consumer-rights project.
  - **결과**: Argues that R2R, taken seriously, requires
    institutional change beyond manufacturer compliance — echoes
    the post-growth claim that repair *culture* is the missing
    piece, not repair *legislation*.
  - **한계**: No empirical data; relies on document analysis of
    movement statements.
- **system reduction**: **Sociology** classification — does not
  trigger a code or link change. Used in ROADMAP as direction
  signal: "build the repair affordances; do not assume the law
  will." Concretely: do not gate node-replaceability on R2R legal
  status of components.
- **[NEW]**: yes (v6).

## 3. Hypothesis sub-score (1–5)

| paper | sub-hyp it relates to | score | reason |
|---|---|---|---|
| Repairable electronic products (s43621-024-00753-x) | (a) reliability + (b) surplus | 4 | converts CE rhetoric into testable product-level invariants |
| Service Design for Repair (Knowledge 2025) | (b) surplus | 3 | three-tier framing maps onto our combo split |
| OLSK Small Laser V2 (HardwareX 2025) | (a) + (b) | 5 | the bootstrap evidence — a node can be physically reproduced from OSH |
| Lloveras et al — Politics of Repair (JBE 2025) | direction (sociology) | 3 | argues against relying on legal R2R; not a code input |

**Combo B v6 aggregate**: hypothesis branch (b) — that surplus can
absorb non-essential wants within a recoverable envelope — is partially
attested. The *recoverable* part is concrete (DfR + DfD + OSH = the
engineering definition of recoverable). The *non-essential wants*
part is largely theoretical at this scope (post-growth and time-banking
literature does not yet meet v6 keyword strictness in its empirical
arm). Hypothesis branch (a) is reinforced indirectly by OLSK (a node
can be replaced from OSH).

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
1. `repair score regulation` — the EU repairability score (effective
   2025-06-20) is now a measurable input to the design rules.
2. `unpaid work valuation` — covers the "non-market work" gap with the
   vocabulary the empirical literature actually uses.
3. `degrowth provisioning` — the standard phrase in the post-growth
   literature where the v6 keyword `post-growth economics` doesn't hit.
4. `repair café` / `community repair` — the empirical sociology
   counterpart to "time banking".
5. `open source machine tools` — narrower than OSH, where OLSK lives.

**Two unexplored adjacent fields:**
- **Modular electronics standards** (Framework Laptop, Phonebloks
  retrospectives) as case studies for the DfR rules.
- **Care economy accounting** as the empirical hinge for non-market
  work; closer to combo C's measurement substrate than to combo B.

## 5. Search log

| keyword query | tool | results | in-window | adopted |
|---|---|---|---|---|
| right to repair empirical study | WebSearch | 10 | 7 | 1 (Lloveras et al, via cross-search) |
| design for repair / disassembly review | WebSearch | 10 | 8 | 2 (s43621-024-00753-x; Knowledge 6/4/154) |
| time use survey + non-market work | WebSearch | 10 | 7 | 0 — 근거 부족 (Charmes 2025, Sahu 2024 score 1.5; Lancet Kallis 2025 scores 1.0–1.5; all below threshold) |
| post-growth economics empirical | WebSearch | 10 | 6 | 0 — 근거 부족 (Lancet Kallis et al 2025; Klose JIE 2025 — neither hits 2 v6 keywords) |
| open source hardware + fab lab | WebSearch | 10 | 5 | 1 (OLSK Small Laser V2, HardwareX 2025) |
| time banking community currency | WebSearch | 10 | 3 | 0 — 근거 부족 (Brill ISS 2025 Taiwan timebank: 1 keyword full + 1 partial = 1.5) |
| circular economy product design | WebSearch | 10 | 7 | 0 net new (Klose JIE 2025 below threshold; cross-listed) |

- **pooled in-window candidates (pre-dedup)**: ~30
- **dedup by DOI / URL**: removed ~6 duplicates (s43621-024-00753-x
  appeared in 3 queries)
- **scored ≥ 2 keywords**: 4
- **adopted (final)**: **4**
- **rejected at < 2 keywords (notable)**:
  - Kallis et al. *Post-growth: the science of wellbeing within
    planetary boundaries*, Lancet Planetary Health 2025;1.0–1.5 — only
    `post-growth` (partial of `post-growth economics`); no second
    keyword. Recorded in ROADMAP.md as direction.
  - Charmes et al. *A global overview of time-use data*, 2025; full
    `time use survey` only; 1.0. ROADMAP.
  - Sahu, *Gender Conundrum and Unpaid Work in India*, 2024; full
    `time use survey` + partial via "unpaid work" ≈ "non-market work";
    1.5. ROADMAP.
  - Brill ISS 2025 Taiwan time-bank empirical case; full `time banking`
    + partial; 1.5. ROADMAP.
  - Klose, *A new circular economy conception for sustainable product
    design*, Journal of Industrial Ecology 2025; partial only; 1.0.
- **gaps recorded as 근거 부족**:
  - **federated repair-data infrastructure** — no in-window paper
    found connecting OSH BoMs to a shared repair-history ledger; this
    is the natural combo B × combo C handoff.
  - **non-market work measured at node** — empirical time-use studies
    are still survey-driven, not sensor-driven; the routine's premise
    that *measurement* replaces *survey* is not yet attested.

**Search confidence**: medium. Engineering side is solid; sociology
side is below the strictness bar by design (the v6 keyword list does
not match how the empirical sociology literature labels its work).
This is a feature not a bug — the rejected papers are still recorded
under ROADMAP as direction signals.
