# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-05-21 / run 2 (Research Routine v6, all 4 combos)**:
  - Routine upgraded v4 → v6. Combo directories renamed to mechanism-
    based names (combo-A-physics-input, combo-B-cost-surplus,
    combo-C-priority-from-measurement, combo-D-near-sensor-judgment).
  - **combo-A**: 3 papers adopted. Carries forward the PINN diesel-engine
    paper (arXiv:2412.11967) from run 1, re-scored against v6 keywords;
    adds two new RUL+UQ papers from the Thil et al. C-MAPSS cluster
    (arXiv:2507.06672, arXiv:2511.21208). Combo-A now delivers a clean
    `(estimate, uncertainty)` interface contract; the `sensor data
    attestation` half of the keyword list returned **no** compounding
    paper (근거 부족).
  - **combo-B**: 2 papers adopted (engineering side only). Roskladka
    et al. 2024 (Discover Sustainability, DOI 10.1007/s43621-024-00753-x)
    and Brandenburger et al. 2024 (ECIS Green IS). Sociology cluster
    (post-growth / time use / time banking) yielded canonical single-
    keyword papers but no compounds — **근거 부족** on premise (b).
  - **combo-C**: 4 papers adopted. Three DPP-LCA papers (Gieß & Möller
    2025 DOI 10.1111/jiec.13621; Procedia CIRP S2212827125002860;
    Tabata & Tsai 2025 DOI 10.1007/s43615-025-00552-0) and one extended
    exergy accounting paper (Qi et al. 2025 DOI 10.1038/s41598-025-
    29077-0). Combo-C now contributes the measurement schema (DPP) and
    the aggregation unit (exergy). The decision-rule bridge (exergy →
    vote) is still a literature gap.
  - **combo-D**: 4 papers adopted. Inference half (QUTE arXiv:2404.12599,
    MMEdge arXiv:2510.25327) and TEE half (GNNVault arXiv:2502.15012,
    TZ-LLM arXiv:2511.13717). Closes the attestation gap that combo-A
    flagged.
  - **synthesis.md** updated. Cross-combo seams identified:
    `attested PHM tuple` (combo-A × combo-D) and `exergy-denominated
    vote` (combo-A × combo-C, still open).
  - **No code changes**. **No PHYSICAL_LINKS entries opened**. Default-
    deny still in force.

- **2026-04-18 / run 1 (v4, combo-A only)**: System now has a literature
  baseline for L1×L3 (physics-grounded maintenance consensus). Three
  papers adopted into `references/combo-A-physics-consensus/INDEX.md`
  (directory subsequently renamed in run 2). No code changes. No
  physical link opened.

## Open work queue (derived from run 2)

1. **(task a, combo-A re-entry)** Re-search with the run-2 follow-up
   keyword `attested PHM output` to look for the combo-A × combo-D
   bridge paper. The attestation gap is structural to the architecture;
   a single missing paper would close it.
2. **(task a, combo-C re-entry)** Re-search with `exergy-weighted
   voting` / `multi-criteria decision-making exergy` to look for the
   decision-rule bridge (sustainability accounting → governance
   mechanism).
3. **(task b, combo-A)** Stub `nodes/l1-reliability/` with a PHM skeleton
   reducing **arXiv:2412.11967** (PINN-based engine health monitoring)
   into a `physics_residual(state, ode_form) → scalar` function.
   *Carried from run 1.*
4. **(task b, combo-A)** Extend the same stub with
   `rul_with_uncertainty(sensor_window) → (rul, aleatoric_var,
   epistemic_var)` reducing **arXiv:2507.06672** and **arXiv:2511.21208**.
5. **(task b, combo-D)** Stub `nodes/l1-reliability/secure/` with a
   TEE-partition skeleton reducing **arXiv:2502.15012** (GNNVault) /
   **arXiv:2511.13717** (TZ-LLM) into an `attested_indicator() →
   (tuple, attestation_blob)` interface.
6. **(task c)** Draft candidate `PHYSICAL_LINK: l1-reliability ↔
   l3-priority` citing **DOI:10.1111/jiec.13621** (DPP value ecosystem)
   as the data-schema basis. Status will enter as `proposed`.
7. **(task d, sociology)** Read Kallis et al. 2025 (Lancet PH post-
   growth review) end-to-end and update `ROADMAP.md` only — sociology
   papers do not trigger code or links.

## Not yet explored

- combo-A keyword `federated learning for prognostics` (returned no
  multi-keyword compound)
- combo-B keyword `fab lab` (returned only event recaps in-window)
- combo-C keyword `quadratic voting` × sustainability bridge (literature
  gap)
- combo-D keywords `in-sensor computing`, `energy-harvesting wireless
  sensor` (HF index thin in 2024-2026 window)

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link = 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- Default deny on inter-node links until PHYSICAL_LINKS entry is added.
