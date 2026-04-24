# ROUTINE

This directory is driven by `Research Routine v6`. The routine lives in the
session instructions (not checked in verbatim). A run executes one or more
of:

- (a) one combo search + paper adoption + INDEX.md update
- (b) synthesis.md / candidate-advisors.md update
- (c) ROADMAP.md update (sociology-only runs stop here)
- (d) directory / metadata refactor to match current routine version

v6 replaces the L1/L2/L3 framing from v4 with a **component-oriented**
framing. Each combo is a bucket of mechanisms that plug into the larger
system as identifiable parts (sensor→input, surplus→slack, measurement→
priority, judgment-near-sensor).

## Core hypothesis (v6)

Money is a proxy for trust. Therefore, if (a) the physical reliability of
production infrastructure is sufficiently high, (b) surplus resources can
be allocated to non-essential wants within a recoverable range, and
(c) resource-priority consensus can be derived directly from physical
measurements, then the mediating function of money becomes surplus.

We do **not** expect papers to assert this hypothesis. We collect
*components* whose combination could make such a system. Each adopted
paper must reduce to a concrete part of the stack (a node, a function,
or a link).

## Combos

| combo | role in system                                | dir                                       |
|-------|-----------------------------------------------|-------------------------------------------|
| A     | physical reliability → consensus input        | `references/combo-A-physics-input/`       |
| B     | marginal-cost reduction → absorbs nonessential| `references/combo-B-cost-surplus/`        |
| C     | measurement-driven priority                   | `references/combo-C-priority-from-measurement/` |
| D     | judgment near the sensor                      | `references/combo-D-near-sensor-judgment/`|

## Keyword match rule (v6)

Per-combo keywords are searched individually, pooled, deduplicated by
DOI/arXiv ID. A paper is adopted iff its title+abstract matches ≥ 2
distinct combo keywords **and** the summed match score is ≥ 2.5
(full-phrase = 1.0, key-word partial = 0.5; case / hyphen / singular
insensitive).

Sociology papers only update ROADMAP.md. They do not trigger code
changes and do not justify PHYSICAL_LINKS.md entries.

## Default deny on inter-node links

All inter-node communication is closed by default. A link is opened only
after a physical basis is justified in `PHYSICAL_LINKS.md` with ≥ 1
engineering reference. This invariant survives the v4 → v6 transition.
