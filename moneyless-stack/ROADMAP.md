# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-18 / run 1 (task a, combo-A, routine v4)**: Literature
  baseline for L1×L3 (physics-grounded maintenance consensus).
  Three papers adopted. No code changes. No physical link opened.

- **2026-04-24 / run 2 (task a+b+d, all four combos, routine v6)**:
  Routine migrates to v6. Combo directories renamed to v6 names.
  Combo keyword lists tightened to standard academic terms.
  Adoption threshold enforced at ≥ 2 keywords AND sum ≥ 2.5.
  Ten papers adopted across combos A and D. Combos B and C record
  **근거 부족** pending Scopus / ScienceDirect access per v6's
  "주 도구" guidance. synthesis.md reframed around the
  calibrated-HI contract, node-local judgment, and the cross-combo
  attestation gap.

## Open work queue (derived from run 2)

1. **task (c)** — open `PHYSICAL_LINK: l1-reliability ↔ l3-consensus`
   with `status: proposed`, citing combo-A 2511.21208 (I-GLIDE) as
   "what travels" (an HI with aleatoric + epistemic UQ) and
   combo-D 2502.02692 (Trivedi sensing-to-action) as "why it
   travels only on demand". Link stays `proposed` until the
   attestation gap closes.
2. **task (b)** — stub `nodes/l1-reliability/` against the v6 HI
   contract
   `sensor_window → (score: float, aleatoric: float, epistemic: float)`.
   Reduce paper 2511.21208 into a ~30-line indicator-group HI with
   MC-dropout UQ.
3. **task (b)** — stub `nodes/d-near-sensor/` as an MCU-target
   placeholder reducing 2603.11071 (TinyNav) into a minimum
   local-judgment loop.
4. **task (a) combo-A re-run** — targeted Scholar / IEEE Xplore
   search for the five follow-up keywords specifically about
   signing/attesting a PHM output.
5. **task (a) combo-B re-run on Scopus / SSRN** — per v6 "주 도구"
   guidance; the HF pool is content-sparse for this combo.
6. **task (a) combo-C re-run on Scopus / ScienceDirect** — same
   reason.

## Sociology signposts (combo-B, no code trigger per v6)

These are policy / social-science references surfaced by WebSearch
during the combo-B run. By v6 invariant (sociology papers update
ROADMAP, not code) they are not adoptable as stack components but
are tracked as context:

- **2025 Lancet Planetary Health** review of 201 post-growth studies
  — frames ecological macroeconomic models under post-growth.
- **ScienceDirect 2025** "Post-growth economics as a guide for
  systemic change: Theoretical and methodological foundations".
- **Journal of Supply Chain Management 60(4) 2024** "Rethinking
  Supply Chain Management in a Post-Growth Era".
- **EU Right-to-Repair Directive**, adopted July 2024, effective
  July 2026 — mandates manufacturer-supplied parts, tools,
  documentation.
- **Oregon SB 1596** Right-to-Repair, effective 2025-01-01; similar
  acts passed in CA, CO, MN, NY, MA.
- **Oxford Innovation in Aging 2024** Hong Kong quasi-experimental
  timebanking study — 116 treatment / 114 comparison; reward-based
  time-bank significantly increases late-life volunteering.
- **IKEA Circular Product Design Guide 2024** (industry, not
  academic) — codifies design-for-disassembly at a household-
  consumer scale.
- **ScienceDirect 2025** "A review of disassembly systems for
  circular product design".

## Not yet explored

- Scopus / ScienceDirect runs for combos B and C (required for
  fair signal on those combos).
- arXiv cs.GT direct queries on quadratic voting + deployed
  mechanism design.
- IEEE Xplore / embedded-security venues on sensor attestation.
- KCI / RISS for Korean-language secondary literature.

## Invariants (unchanged under v4 → v6 transition)

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any
  feature is added on top.
- `PHYSICAL_LINKS.md` default-deny remains in effect.
