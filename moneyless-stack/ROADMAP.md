# ROADMAP

## Changelog — "since last run, the system can additionally do …"

- **2026-04-18 / run 1 (task a, combo-A)**: System now has a literature
  baseline for L1×L3 (physics-grounded maintenance consensus). Three
  papers adopted into `references/combo-A-physics-consensus/INDEX.md`.
  No code changes. No physical link opened.

## Open work queue (derived from run 1)

1. Stub `nodes/l1-reliability/` with a PHM skeleton reducing paper
   **arXiv:2412.11967** (PINN-based engine health monitoring) into a
   degradation-indicator function. (task b)
2. Stub `nodes/l3-consensus/` with a peer-ranked consensus skeleton
   reducing **arXiv:2510.24801** (Fortytwo). (task b)
3. Draft candidate `PHYSICAL_LINK: l1-reliability ↔ l3-consensus`
   citing **arXiv:2510.03807** (6G Digital Twin for industrial bearing
   fault detection) as physical basis. Status will enter as `proposed`. (task c)
4. Run combo-B search next. (task a)

## Not yet explored

- combo-B (Zero-Marginal Cost + Recoverable Slack)
- combo-C (Sustainability Constraints in DLT Governance)
- combo-D (Physical AI as Consensus Substrate)

## Invariants

- Sociology papers do not trigger code changes (ROADMAP only).
- Engineering paper : node code / link : 1-to-1.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top.
