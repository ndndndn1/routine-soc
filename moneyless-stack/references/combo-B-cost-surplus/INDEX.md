# combo-B — marginal-cost reduction → absorbs non-essential wants

## 0. Run metadata

- **run_date**: 2026-04-24
- **search_window**: 2024-04-24 → 2026-04-24
- **prior_run**: none (first combo-B run).
- **routine**: v6.
- **task**: (a) search + adoption.
- **primary tool**: HF `paper_search` for engineering angle; WebSearch
  (Google Scholar surface) for sociology / policy angle.
  Engineering is the tool on the "production" side of the combo; the
  sociology side (time banking, post-growth) is collected as ROADMAP
  signposts only per v6 rule.

## 1. Executive summary

Under v6, combo-B keywords straddle two fields the HF index does not
cover well: (i) product-design / repair-economy engineering keywords
(`right to repair`, `design for disassembly`, `open source hardware`,
`fab lab`), and (ii) pure social-science keywords (`time use survey`,
`non-market work`, `post-growth economics`, `time banking`).
Six HF candidates surfaced, the strongest being Berkeley Humanoid Lite
(2504.17249) at **2.0** — below the ≥ 2.5 threshold. **No paper
clears v6 adoption.** Per v6 rule "keyword expansion is disallowed when
adoption is low; record as 근거 부족". WebSearch confirms the
sociology-side literature exists (Lancet 2025 post-growth review;
Hong Kong 2024 timebanking quasi-experiment; EU Right-to-Repair
directive 2024; 2025 ScienceDirect review of disassembly systems for
circular product design) but none of these are engineering artifacts,
so per v6 invariant they feed ROADMAP.md only.

## 2. Adopted papers (≥ 2 keywords, sum ≥ 2.5)

**None.**

### 2.x Near-miss: Berkeley Humanoid Lite (2504.17249)

- **authors**: Chi, Liao, Long, Huang, Shao, Nikolic, Li, Sreenath
- **year**: 2025 (Apr 24)
- **venue**: arXiv
- **matched_keywords**:
  - `open source hardware` — 1.0 (explicit: "fully open-sourcing the
    hardware design")
  - `fab lab` — 0.5 (partial: "standard desktop 3D printers",
    "widely available e-commerce platforms" — a fab-lab workflow but
    not named)
  - `design for disassembly` — 0.5 (partial: "modular 3D-printed
    gearbox", "modularity and ease of fabrication" — modularity
    implies disassemblability but not framed as DfD)
  - **sum**: 2.0 → **below threshold**
- **note**: This is exactly the class of artifact the routine is
  looking for on the production side — a demonstrable, community-
  reproducible, low-capex hardware platform. v6 keyword strictness
  prevents it from being adopted on this run. Re-evaluation on next
  combo-B run if a new query explicitly picks up "design for repair"
  or "modular mechatronics" is warranted.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | — | out of scope for combo-B. |
| (b) surplus absorbs non-essential wants | 1 | Engineering-side literature that is both rigorous and combo-B-specific is sparse in HF. The existence of high-profile policy (EU DPP, U.S. state RtR laws, EU RtR directive taking effect 2026) does not constitute adoptable engineering evidence under v6. |
| (c) measurement-direct priority | — | out of scope for combo-B. |

**Aggregate**: **근거 부족 (insufficient evidence)** for combo-B under
v6 within HF's index. The routine's invariant against sociology
triggering code changes means this is a recognised-and-honored gap,
not a failure — the sociology signposts feed ROADMAP, not code.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (for next combo-B run — run on Scopus /
SSRN per v6 "주 도구" guidance, not HF):**
- circular economy product design standards (e.g. EN 45554)
- digital product passport (cross-combo with combo-C)
- modular mechatronics
- repair index (France "indice de réparabilité")
- open-source appropriate technology

**Two under-explored adjacent fields:**
- Participatory maintenance / commons-managed infrastructure
  literature (overlaps combo-C on governance).
- Computer-aided design for disassembly (CAD-DfD) metrics and tools —
  has engineering artifacts but not indexed on HF.

## 5. Search log

| keyword (query used) | source | returned | in-window | pooled | ≥ 2.5 |
|---|---|---|---|---|---|
| right to repair legislation consumer electronics | HF | 0 | 0 | 0 | 0 |
| design for disassembly circular economy product | HF | 6 | 3 | 3 | 0 |
| open source hardware fab lab maker | HF | 82 | ~5 | 5 | 0 |
| time use survey non-market work | HF | 0 | 0 | 0 | 0 |
| post-growth economics degrowth time banking | HF | 4 | 2 | 2 | 0 |
| modular robot 3D printed repairable | HF | 120 | 3 | 3 | 0 |
| reparable open hardware IoT low-cost | HF | 120 | ~3 | 3 | 0 |
| right to repair legislation 2024 2025 review article | WebSearch | — | — | 8 policy sources | 0 (policy, not papers) |
| post-growth economics 2024 2025 peer-reviewed | WebSearch | — | — | Lancet 2025 + ScienceDirect 2025 | 0 (not engineering) |
| design for disassembly product design 2024 2025 circular | WebSearch | — | — | ScienceDirect 2025 review | 0 (not HF-retrievable; logged in ROADMAP) |
| time banking community currency 2024 2025 empirical study | WebSearch | — | — | Oxford 2024 quasi-experiment | 0 (sociology) |

- pooled unique engineering candidates in-window: ~15
- ≥ 2.0 but < 2.5: 2504.17249 (Berkeley Humanoid Lite, 2.0)
- ≥ 2.5 adopted: **0**
- rejected at < 2.0: 2503.03998 (battery prying, 1.5),
  2405.10452 (CE topic modelling, 1.0), 2401.06528 (PCB-Vision, 1.5 —
  also borderline out of window at Jan 2024).

**Search confidence**: low on HF — the engineering literature that
does exist (product-design journals, circular-economy journals, IJCCR
for time banks) is not in the HF paper index. v6 "주 도구" guidance
for combo-B is explicitly Scopus / SSRN, which this run could not
interrogate. Next combo-B run should go there first.

**Sociology signposts (feed ROADMAP.md, not code)**:
- 2025 Lancet Planetary Health review of 201 post-growth studies.
- "Post-growth economics as a guide for systemic change", ScienceDirect 2025.
- "Rethinking Supply Chain Management in a Post-Growth Era",
  J. Supply Chain Management 60(4), 2024.
- EU Right to Repair Directive, adopted July 2024, effective July 2026.
- Oregon SB 1596 (Right to Repair), effective 2025-01-01.
- Oxford Innovation in Aging 2024 timebanking quasi-experiment.
