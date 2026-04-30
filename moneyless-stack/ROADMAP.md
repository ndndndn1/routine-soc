# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-30 / run 2 (v6, all four combos)**: All four combos now
  have v6 INDEX.md. The literature survey now jointly specifies a
  paper-level pipeline (see synthesis.md). 15 papers adopted across
  the four combos under strict v6 scoring. Sociology direction
  signals (Lancet Kallis et al.; time-banking Taiwan; Charmes et al.
  global time-use; Sahu unpaid-work India) recorded below as
  direction-only. No code changes. No physical link opened.
- **2026-04-18 / run 1 (v4, combo-A only)**: System had a literature
  baseline for L1×L3 (physics-grounded maintenance consensus).
  Three papers adopted into the v4 combo-A INDEX.md. Superseded by
  the v6 split.

## Sociology direction signals (no code trigger)

These papers do **not** trigger a code change but are recorded here
because they materially shape the routine's direction:

- **Kallis, Hickel, O'Neill, Jackson, Victor, Raworth, Schor,
  Steinberger, Ürge-Vorsatz** — *Post-growth: the science of wellbeing
  within planetary boundaries*, *Lancet Planetary Health* 9(1):e62–e78
  (Jan 2025). Strict-rejected from combo B INDEX (1.0–1.5 score), but
  is the canonical reference for the *direction* of hypothesis branch
  (b). Practical implication: the routine should not assume GDP-style
  growth as the surplus generator.
- **Lloveras, Pansera, Smith** — *On the Politics of Repair Beyond
  Repair*, *Journal of Business Ethics* (online Jan 2025). Adopted in
  combo B as [사회학]. Practical implication: do not gate node
  replaceability on Right-to-Repair legal status of components; build
  the affordances directly.
- **Charmes, Emandi, Buvinic, Encarnacion, Grum, Seck, Vaca Trigo**
  — *A global overview of time-use data: gendered uses and policy
  work* (Sage 2025). Strict-rejected, 1.5 score. Direction:
  measurement of non-market work is still survey-driven, not sensor-
  driven; the routine's "measurement replaces survey" premise is
  empirically unattested.
- **Sahu** — *Gender Conundrum and Unpaid Work in India: Empirical
  Evidence from India's First Large-scale Time Use Survey* (Sage
  2024). Strict-rejected, 1.5 score. Direction: same as above, with
  an empirical anchor point.
- **Brill ISS 2025 — Innovative Time Bank Practices in Taiwan**
  (Innovation in the Social Sciences, 2025). Strict-rejected, 1.5
  score. Direction: time-banking is the closest empirical mechanism
  to "non-market work as an exchange medium", but published evidence
  is small-N case studies.

## Open work queue (derived from run 2)

Engineering tasks that are now justified by the v6 literature pool:

1. Stub `nodes/l1-reliability/` with the v6 indicator interface
   `health_indicator(window) → (score, group_score[], aleatoric_var,
   epistemic_var)` reducing **arXiv:2511.21208 (I-GLIDE)** + the
   physics-prior residual line from **arXiv:2412.11967**. (task b)
2. Stub `nodes/l1-reliability/attest/` reducing **arXiv:2511.13717
   (TZ-LLM)** to a minimal attested-emit pattern: signed
   `(score, ε_a, ε_e)` envelope. Hardware target ESP32 / Cortex-M
   class with TrustZone-M. (task b)
3. Stub `substrate/dpp/` with the IJPR 2025 blockchain-DPP design
   principles: on-chain identity + commitments, off-chain
   bulky telemetry. (task b)
4. Draft candidate `PHYSICAL_LINK: l1-reliability ↔ substrate/dpp`
   citing **arXiv:2510.03807 (6G Digital Twin)** as physical basis
   for the link bandwidth/latency profile (carry-over from v4
   ROADMAP). Status will enter as `proposed`. (task c)
5. Re-enter combo A with widened keyword list once the **sensor
   data attestation** gap is closed by a published paper. (task a)
6. Re-enter combo C with the keyword `liquid democracy weighted by
   uncertainty` to test whether the measurement → vote-weight gap
   has been filled. (task a)

## Bootstrap claim status

The OLSK Small Laser V2 paper (HardwareX 2025) attests the **physical
reproducibility** of a node's hardware via OSH. Combined with TinyNav
(ESP32 end-to-end), the claim "a node can be replaced from open-source
hardware at recoverable marginal cost" is now backed by two peer-
reviewed papers. This claim was previously aspirational; it is now
direction-setting.

## Not yet explored

- Sensor-stream attestation (combined combo A × combo D follow-up).
- Measurement-grounded vote weighting (combo C re-entry).
- Empirical non-market-work data with sensor-level granularity (no
  current literature).

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- Strict v6 keyword scoring is applied without relaxation. When
  adoption count is low, the answer is `근거 부족`, never a softer
  scoring rule.
