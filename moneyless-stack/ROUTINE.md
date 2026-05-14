# ROUTINE

This directory is driven by `Research & Build Routine`. Active routine
version: **v6**.

Each run performs exactly one of:

- (a) one combo search + paper adoption + INDEX.md update
- (b) a single adopted paper reduced into a node's code (CHANGELOG line)
- (c) one PHYSICAL_LINKS.md entry created or status-changed
- (d) ROADMAP.md / synthesis.md update

Run cadence is strict: **one task per run**, except for a full v6 pass
which performs (a) for all four combos and one (d) at the end. The
2026-05-14 run was such a full pass.

## v6 combos (current)

- **combo-A — Physics Reliability → Consensus Input**
  (`references/combo-A-physics-input/`)
- **combo-B — Marginal Cost ↓ → Non-Essential Wants Absorbed**
  (`references/combo-B-cost-surplus/`)
- **combo-C — Physical Measurement → Resource Priority**
  (`references/combo-C-priority-from-measurement/`)
- **combo-D — Near-Sensor Judgment**
  (`references/combo-D-near-sensor-judgment/`)

## v4 / pre-v6 directories (kept for prior-run traceability)

`combo-A-physics-consensus/`, `combo-B-zmc-slack/`,
`combo-C-sustainability-dlt/`, `combo-D-physical-ai-substrate/`.

Pre-v6 INDEX files record the looser keyword sets used in run 1. v6
INDEX files cite the pre-v6 INDEX as `prior_run` where applicable.

## Layer stack

- L1 Reliability Physics   — physically reliable production substrate
- L2 Entropy Buffer        — allocation of surplus to non-essential wants
- L3 Physical Consensus    — distributed consensus directly off measurements

## Default deny

All inter-node communication is **closed by default**. A link opens only
after a physical basis is justified in `PHYSICAL_LINKS.md` with ≥ 1
engineering reference. Sociology papers never justify a link.

## Adoption rule (v6)

A paper is adopted iff:
- publication date is within the run's 2-year window, AND
- it matches ≥ 2 combo keywords, AND
- summed match score is ≥ 2.5.

Match scoring: full phrase = 1.0, partial / core-word hit = 0.5.
Case, hyphen/space, and singular/plural are equivalent.
