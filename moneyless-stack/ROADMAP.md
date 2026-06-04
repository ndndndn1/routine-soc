# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-18 / run 1 (v4, task a, combo-A)**: literature baseline for
  L1 × L3 (physics-grounded maintenance consensus). Three papers
  adopted into `references/combo-A-physics-consensus/INDEX.md`. No
  code changes. No physical link opened.

- **2026-06-04 / run 2 (v6 bootstrap — four combos in one run)**:
  routine upgraded to v6; combo directories renamed
  (`combo-A-physics-input`, `combo-B-cost-surplus`,
  `combo-C-priority-from-measurement`, `combo-D-near-sensor-judgment`);
  all four INDEX.md files filled.
  - **combo-A** re-scored under v6 keywords → 3 papers adopted
    (I-GLIDE, RUL-Turbofan UQ, CARLE). v4 flagship 2412.11967 falls
    below the v6 threshold and is demoted to engineering reference.
  - **combo-B** → 1 paper adopted (Springer "Repairable electronic
    products" review); the social-science half of the keyword list
    recorded as **근거 부족** (sociology references update this file
    only, none cleared the threshold).
  - **combo-C** → 2 papers adopted (Sensor-Based DPP for low-tech
    manufacturing, Extended Exergy for Chinese nonferrous metals).
  - **combo-D** → 2 papers adopted (TinyNav end-to-end on MCU,
    GNNVault TEE-protected edge inference). In-sensor analog
    computing returned no in-window new work.
  - No code changes. No physical link opened. `synthesis.md` updated
    to reflect the shared open bridge across all four combos.

## Open work queue (derived from v6 run 1)

Engineering-paper-driven (task b, one-to-one with adopted paper):

1. Stub `nodes/l1-reliability/` with a PHM skeleton that exposes
   `health_indicator(window) → (score, aleatoric_var, epistemic_var)`,
   reducing **arXiv:2511.21208 (I-GLIDE)**. Per-sensor-group decomposition
   deferred to a v2.
2. Stub `nodes/l1-reliability/` baseline `bearing_health()` reducing
   **arXiv:2510.17846 (CARLE)** — point prediction only, marked as
   "no UQ" until merged with the I-GLIDE head.
3. Stub `nodes/l2-priority/dpp/` with a schema that holds
   `(stage, sensor_id, indicator_value, lca_attribution)` tuples,
   reducing **MDPI Sensors 25(18) 5653 (Sensor-Based DPP)**. No
   priority-formation logic yet — schema only.
4. Stub `nodes/l2-priority/exergy/` with a node-local exergy budget
   function, reducing **Sci Rep 15:44816 (Extended Exergy nonferrous
   metals)**. Macro→node transposition explicit in code.
5. Stub `nodes/l1-reliability/edge/tiny_decision.py` reducing
   **arXiv:2603.11071 (TinyNav)** to a `decision(sensor_window) → action`
   inference that targets MCU constraints. Quantisation deferred.
6. Stub `nodes/l1-reliability/edge/tee_partition.py` reducing
   **arXiv:2502.15012 (GNNVault)** to a "split inference at the trust
   boundary" pattern, even if the trusted side runs as a normal
   process in stub form.
7. Sociology-side trigger (Springer DfR review): **does NOT** create a
   node. Add a `repairability_measure` *field* to whatever DPP schema
   is built by item 3 — that is the only system reduction allowed for
   a DfR-side paper, since the paper itself is policy + review.
   (Edge case: paper is engineering-systematic-review, not pure
   sociology — kept as task b but scope-limited to schema only.)

Link-justification (task c):

8. Draft candidate `PHYSICAL_LINK: l1-reliability ↔ l2-priority`
   citing the Sensor-Based DPP paper as physical basis (sensor stream
   → DPP record is a measurable bits-from-physics link). Status will
   enter as `proposed`.
9. Draft candidate `PHYSICAL_LINK: l1-reliability-edge ↔
   l1-reliability-cloud` citing GNNVault as physical basis (TEE
   quote crossing the link is the bits-from-physics evidence).
   Status will enter as `proposed`.

Synthesis (task d, queued, not blocking):

10. Re-run combo-B against Scopus / SSRN once a credentialed path
    is available, to convert "근거 부족" on the absorption half into
    either signal or refutation.
11. Search the bridge — measurement-bound consensus / exergy-weighted
    voting / attested-decision DPP — as a synthesis search (does not
    fit a single combo).

## Not yet explored

- The bridge keyword cluster: "attested decision", "uncertainty-weighted
  consensus protocol with physical input", "node-local exergy budget".
- The non-HF social-science indices (Scopus, SSRN) for combo-B.

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link — 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
- v6 adoption rule: ≥ 2 keyword matches AND ≥ 2.5 score. No
  exceptions, no inflation.
