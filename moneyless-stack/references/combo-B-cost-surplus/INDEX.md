# combo-B — Marginal Cost ↓ → Non-Essential Wants Absorbed

System role: produce the part of the stack that lets the system spend
its slack on "could-do" activities. Engineering bricks: repairable /
disassemblable product designs. Sociological scaffolding (ROADMAP-only):
non-market work, post-growth economics, time-banking.

## 0. Run metadata

- **run_date**: 2026-05-14
- **search_window**: 2024-05-14 → 2026-05-14 (last 2 years)
- **prior_run**: none under v6 naming (prior `combo-B-zmc-slack/` was
  a placeholder; this is the first substantive combo-B run).
- **routine version**: v6
- **task**: combo search + adoption + INDEX.md
- **primary tools**: WebSearch (Scopus / ScienceDirect / Springer Nature
  / SSRN / MDPI surfaced via search). HF `paper_search` used as a
  sanity check — it returned almost nothing in-domain because the HF
  index is ML-only. That is the expected behaviour for this combo and
  is recorded in the search log.
- **fallback tools (not used)**: Semantic Scholar direct, Google Scholar
  direct. Surfaced via WebSearch result links anyway.

## 1. Executive summary

Combo-B's keyword set splits cleanly: the design-engineering half
(right to repair, design for repair, design for disassembly, circular
economy product design, open source hardware, fab lab) is a mature,
publishing-active field; the social-economics half (time use survey,
non-market work, post-growth economics, time banking) is publishing
mostly as government reports, special-issue essays, and isolated
case studies — there is little intersection with the engineering
keywords. As a result, the cross-keyword filter (≥ 2 keywords, score ≥
2.5) catches engineering syntheses cleanly and catches almost no
sociology paper, which is consistent with the routine's prior
expectation. Two engineering reviews — both 2025, both on circular
electronics — are adopted. They turn "repairability" into measurable
design parameters (number of fasteners, modularity, spare-part
availability), which is exactly the slack-allocation primitive the
moneyless-stack needs at L2: a node should be able to *quantify*
how much slack it consumes when it chooses repair-vs-replace.
On the sociology side, post-growth and time-banking literatures exist
in window but never co-occur with the technical vocabulary; they
remain ROADMAP-only.

## 2. Adopted papers (matched_keywords ≥ 2 AND score ≥ 2.5)

### 2.1 Repairable electronic products for the circular economy: a review of design for repair features, practices and measures to contrast obsolescence

- **authors**: (Italian group, U. Brescia — see IRIS unibs.it
  preprint copy linked from search)
- **year**: 2025 (Jan; the journal also lists a 2024 acceptance date)
- **venue**: Discover Sustainability (Springer Nature)
- **DOI**: 10.1007/s43621-024-00753-x
- **matched_keywords**:
  - "design for repair" (1.0 — explicit title phrase, then
    operationalised as "DfR features" / "DfR practices")
  - "circular economy product design" (1.0 — "for the circular
    economy" + "at the product design stage" used together in the
    abstract)
  - "right to repair" (1.0 — abstract explicitly cites "Right to
    Repair" consumer movement + EU Circular Economy Action Plan)
  - "design for disassembly" (0.5 — DfD listed among the DfR
    practices the paper systematises)
  - **Total: 3.5** · 4 keywords matched
- **classification**: [공학] primarily, with sociology context.
- **방법**: Systematic literature review. Classifies Design-for-Repair
  features by the type of obsolescence they tackle (absolute:
  mechanical / technological / service; or relative). Extracts
  practices and measures and maps them onto product categories.
- **결과**: A taxonomy of DfR features (e.g. fastener choice, modular
  boards, replaceable batteries, available spare parts, documented
  diagnostic flows) tied to measurable obsolescence outcomes. The
  taxonomy itself is the contribution.
- **한계**: Review, not a primary study; metrics are normative
  ("should be measurable"), and there is no single agreed
  repairability index across product classes. Policy-coupled (EU
  framing) which may not transfer cleanly to non-EU contexts.
- **시스템 환원**: Justifies an `l2-slack` (or `l1-reliability`-side)
  callable `repairability(product_spec) → (score_0_1, breakdown)`
  whose breakdown enumerates the DfR features actually present. This
  is the first concrete numeric input the slack layer can consume
  from an engineering source — without it, "how much could-do
  activity is allocated to repair" stays qualitative.
- **[NEW]**: yes.

### 2.2 Repair-oriented design and manufacturing strategies for circular electronic products, from mass customization/standardization to scalable repair economy

- **authors**: ScienceDirect 2025 (see article PII)
- **year**: 2025 (Jan; Sustainable Materials and Technologies)
- **venue**: Sustainable Materials and Technologies (Elsevier)
- **DOI / PII**: S2590123025002579
- **matched_keywords**:
  - "design for repair" (1.0 — "Repair-Oriented Design" = RoD is
    the paper's coined term, explicitly equivalent to DfR)
  - "circular economy product design" (1.0 — "circular electronic
    products" + product-design framing)
  - "right to repair" (0.5 — referenced as the policy driver
    behind RoD, not the main subject)
  - **Total: 2.5** · 3 keywords matched
- **classification**: [공학]
- **방법**: Conceptual + AHP/QFD analysis. Defines Repair-Oriented
  Design (RoD) as an extension of DfR that explicitly accounts for
  repeated repair cycles, diagnostics, repair-skill heterogeneity,
  and post-sale services. Pairs RoD with mass-customization (MC) and
  mass-standardization (MS) to align manufacturer incentives.
- **결과**: 28 barriers and 56 drivers extracted and weighted;
  manufacturer-side incentives can be aligned with consumer-side
  repair value when MC/MS is paired with RoD.
- **한계**: Methodologically a structured opinion synthesis (AHP/QFD
  on expert input), not an empirical product study. Business-model
  framing is normative.
- **시스템 환원**: Adds a *temporal* dimension to repairability —
  the system should track repair cycles per product, not just
  one-shot repair feasibility. This pushes `repairability(...)` to
  `repair_state(product_id, history) → next_action` with history as
  an explicit input. The slack accounting layer can use repair count
  as a budgeted resource.
- **[NEW]**: yes.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) Production infra physically reliable enough | 2 | DfR/RoD show repairability is operationalisable but real MTBF arguments remain unattested by this combo. |
| (b) Surplus absorbs non-essential wants | 3 | The two adopted papers give the *measurement side* of slack ("how much of the could-do is going into repair"). The "want" side is still only in policy / advocacy literature. |
| (c) Consensus from physical measurement | — | out of scope for combo-B. |

**Aggregate**: combo-B confirms that a numeric repairability layer is
buildable from existing engineering literature. It does not
substantiate the larger post-growth / time-banking layer at a code
level — that remains a ROADMAP-only direction.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords:**
- repairability index / iFixit score formalisation
- digital product passport repair section (links into combo-C)
- spare part availability metric
- modular electronics standard (e.g. Framework laptop literature)
- reuse-rate vs recycle-rate empirical comparison

**Two under-explored adjacent fields:**
- Working-time reduction literature (post-growth-adjacent;
  appeared at the margins of search but never co-occurred with
  engineering keywords).
- Library-of-things / tool-library empirical studies — directly
  relevant to "slack as shared access" but absent from this run's
  pool.

## 5. Search log

`paper_search` (HF) calls — included to confirm the negative result.

| query | results | in-window | usable |
|---|---|---|---|
| right to repair electronics policy | 0 | 0 | 0 |
| design for disassembly circular economy | 10 | 4 | 1 useful (2405.10452 topic-modelling, low overlap) |
| open source hardware fab lab manufacturing | 10 | 4 | 0 with combo-B hit ≥ 2 |
| post-growth economics time use non-market work | 0 | 0 | 0 |

WebSearch (queries → relevant in-window hits surfaced):

| query | relevant hits in window |
|---|---|
| "right to repair" peer reviewed 2024-2026 | Ozturkcan 2024 (Convergence), Kramer & Lechner 2024 (Antitrust Bull.), "Slowing down the loop" 2024, Yang/Zhu/Jin 2024 (SSRN 4854543) |
| "design for repair" / DfD circular economy 2024-2025 | Discover Sustainability 2025 ✓, Sustainable Materials & Tech 2025 ✓, MDPI Sustainability (Service Design for Repair) Nov 2025, IDEA League 2025 |
| "open source hardware" "fab lab" 2024 | OLSK chapter 2024, Makerspaces / FabCity chapter 2024 |
| "time use survey" "non-market work" 2024 | UN Guide to Producing Statistics on Time Use 2024 (report, not paper), India NSO TUS 2024 (report) |
| "post-growth economics" 2024-2025 | Lancet Planetary Health post-growth review (Hickel et al. group, 2024), ScienceDirect post-growth systemic-change 2025 |
| "time banking" 2024-2025 | Springer "Scope and challenges of Time Bank in India" 2024, Hong Kong timebanking quasi-experimental studies 2024-25 |
| "circular economy" "design for repair" 2025 | Confirms 2.1 + 2.2 + Cogent Business 2025 lit review |
| "Whose circular repair economy counts" 2024 | Apr 2024, outside the 2024-05-14 cutoff by ~2 weeks; recorded but rejected as out-of-window |
| "open source hardware" "fab city" 2024-2025 | Designing a Greener Future / OSH publishing platform 2025 chapter; Interfacer / FabCityOS project material (not peer-reviewed) |

- **pooled (HF + Web), in-window**: ~22 papers/reports
- **dedup**: ~18 unique
- **candidates scored ≥ 2.0**: 6
- **candidates scored ≥ 2.5 and adopted**: **2**
- **rejected at 2.0**:
  - OLSK chapter (OSH 1.0 + fab lab 1.0; no third match in standard
    vocab).
  - Sustainable Design and Repair (ML-aided) ScienceDirect 2025 —
    DfR 1.0 + circular-economy 1.0; ML angle adds nothing in
    combo-B vocab.
- **rejected at out-of-window**:
  - "Whose circular repair economy counts" (Apr 2024).
  - "Service Design for Repair Practices in CE" (Nov 2025) — in
    window but DfR 1.0 + circular 0.5 + service-design 0 = 1.5.

**Search confidence**: medium. The engineering DfR/RoD branch is
saturating — same 2025 reviews recur across queries with the same
author clusters. The post-growth / time-banking branch is **근거 부족**
for combo-B's adoption purpose (it exists, it is publishing, but it
does not generate engineering bricks).

**근거 부족 (insufficient evidence)** flagged for:
- "non-market work" as a *combo-B* keyword tying to engineering
  output. Most hits are statistical-office reports, not papers.
  Carry forward into ROADMAP as a sociology-only signal.
- "fab lab" as a peer-reviewed keyword — most authoritative
  material is in proceedings / book chapters (Fab City Foundation,
  Springer Global Collaboration volume) rather than journals; the
  score-2.5 threshold is hard to clear with current 2-year window.
