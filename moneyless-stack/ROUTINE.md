# ROUTINE

This directory is driven by `Research Routine v6`. The routine lives in
the session instructions (not checked in verbatim). The v6 framing
replaces v4's three-layer L1/L2/L3 stack with a four-combo "parts of a
moneyless system" search: each combo collects *components* that could
become a node, a link, or a calculation in the stack.

## Combo definitions (v6)

- **combo-A — Physical reliability → consensus input**
  Sensor-side RUL / PHM / PINN / condition-based monitoring / digital
  twin for maintenance / federated PHM / aleatoric UQ / sensor data
  attestation. Output shape: `(score, uncertainty)` from a node.

- **combo-B — Marginal-cost reduction → non-essential wants**
  Right to repair / design for repair / design for disassembly /
  circular economy product design / open source hardware / fab lab /
  time use survey / non-market work / post-growth economics / time
  banking. The "L2 entropy buffer" justification — what surplus can be
  spent on.

- **combo-C — Physical measurement → resource priority**
  Extended exergy accounting / exergoeconomics / LCA / material flow
  analysis / thermoeconomics / ecological footprint accounting / supply
  chain traceability / digital product passport / quadratic voting /
  uncertainty-weighted decision making. Excludes generic governance
  theory — combo-C is about *measurement → priority* mechanisms only.

- **combo-D — Internal node judgment (near-sensor)**
  TinyML / on-device inference / edge inference / in-sensor computing /
  near-sensor computing / sensor fusion / on-device uncertainty
  estimation / energy-harvesting wireless sensor / trusted execution
  environment / remote attestation. The "judgment close to the sensor"
  primitive.

## Per-run discipline

Each run performs exactly one of:

- (a) one combo search + paper adoption + INDEX.md update
- (b) a single adopted paper reduced into a node's code (CHANGELOG line)
- (c) one PHYSICAL_LINKS.md entry created or status-changed
- (d) ROADMAP.md / synthesis.md update

Run cadence is **one task per run**, except during a routine version
transition (this run, 2026-05-28, is the v4→v6 reset and therefore runs
combos B/C/D in addition to combo-A; future runs return to one-task
cadence).

## Adoption rule (v6)

For each combo:

1. Search every keyword on the combo's primary tool.
2. Pool, dedup by DOI / arXiv ID.
3. For each candidate, score `title + abstract` against the *full
   combo keyword vector*: full phrase = 1.0, core word partial = 0.5,
   hyphen / space / singular-plural normalised.
4. Adopt iff **≥ 2 keywords matched AND sum ≥ 2.5**.
5. If the pool is empty or no candidate clears the bar, log "근거 부족."
   *Do not expand keywords.*

## Default deny

All inter-node communication is closed by default. A link opens only
after a physical basis is justified in `PHYSICAL_LINKS.md` with ≥ 1
engineering reference. Sociology papers do not justify a link; they
update ROADMAP only.

## Classification

Every adopted paper is tagged `[공학]` (drives code / link work) or
`[사회학]` (drives direction / ROADMAP only). Hybrid papers default to
the more restrictive `[사회학]` tag for routine purposes.
