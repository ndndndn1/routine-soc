# ROUTINE

This directory is driven by `Research Routine v6`. The routine lives in the
session instructions (not checked in verbatim).

## Goal

Build a self-sufficient stack with minimum maintenance cost, incrementally.
Sociology papers set direction. Engineering papers supply the executable
plan.

## Core hypothesis

Money is a proxy for trust. The mediating role of money becomes surplus when:

- (a) the physical reliability of the production substrate is high enough,
- (b) surplus resources can be allocated to non-essential wants within a
  recoverable envelope, and
- (c) priority-setting consensus is derivable directly from physical
  measurements.

## Combo map (v6)

| combo | role in the system | primary tool |
|---|---|---|
| A — physics-input | turn sensor → fault/RUL/health estimates that upper layers can consume | arXiv (cs.LG, eess.SP), IEEE Xplore |
| B — cost-surplus | absorb the marginal-cost surplus into discretionary activity | Scopus / SSRN / Google Scholar |
| C — priority-from-measurement | turn measured node states into a global priority ordering | Scopus (energy/env), arXiv (cs.GT) |
| D — near-sensor-judgment | move judgement near the sensor so the upstream link can stay closed | arXiv (cs.AR, cs.LG, eess.SP) |

## Selection rules

- **standard-only keywords**: must appear verbatim or near-verbatim in
  paper title/abstract usage. No coined terms.
- **multi-keyword match**: each candidate paper is scored against the
  keyword list of *its* combo. Adoption requires ≥ 2 keywords matched
  *or* a summed score ≥ 2.5 (full phrase = 1.0, partial = 0.5).
- **publication window**: last 2 years.
- **dedup**: by DOI / arXiv ID inside a combo and across combos.

## Sociology vs engineering

- Sociology paper: only ROADMAP.md is updated. No code is triggered.
- Engineering paper: may justify a node or a `PHYSICAL_LINKS.md`
  entry. One paper → at most one node / link reduction.

## Default deny on links

All inter-node communication is closed by default. A link opens only after
a physical basis is justified in `PHYSICAL_LINKS.md` with ≥ 1 engineering
reference.

## INDEX.md schema (per combo)

0. Run metadata: `run_date`, `search_window`, `prior_run`.
1. Executive summary (~5 sentences).
2. Adopted papers — title / authors / year / venue / DOI or arXiv ID;
   `matched_keywords` (count, list, summed score); 분류 [사회학]/[공학];
   method / result / limitation; system reduction (1–2 sentences).
3. Hypothesis score (1–5) — partial-support is fine.
4. 5 follow-up keywords + 2 unexplored adjacent fields.
5. Search log: per-keyword results, adopted / rejected / duplicate counts.

## Loop termination

Loop runs until all 4 combos have a v6 INDEX.md, then halts on the synthesis
update.
