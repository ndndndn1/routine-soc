# synthesis.md

Cross-combo synthesis. Updated only by task (d).

## State after run 2 (v6, 2026-04-30)

All four combos have a v6 INDEX.md. The literature survey is now broad
enough to attempt a paper-level pipeline diagram for the moneyless
stack.

### Pipeline (paper-attested only)

```
[sensor] --raw-->  [L1 node]
                   ├── physics-prior residual          (combo A · 2412.11967)
                   ├── CWT/Res-CNN front-end           (combo A · 2510.17846)
                   ├── grouped UQ-tagged indicator     (combo A · 2511.21208)
                   └── attested emission               (combo D · 2511.13717)
                       on ESP32-class hardware         (combo D · 2603.11071)
                       via pipelined sense-encode      (combo D · 2510.25327)
                       in a sense→infer→act loop       (combo D · 2502.02692)
                              │
                              ▼
                  [DPP / blockchain substrate]         (combo C · 2025 IJPR DPP)
                              │
                              ▼
                  [priority aggregator]                 (combo C · EEA Sci Rep 2025
                                                         + MFA-LCA IJLCA 2024
                                                         + LCI availability 2024)
                              │
                              ▼  ← ⚠ collective-decision step UNATTESTED
                       [global ordering]
```

The dashed arrow at the bottom is the open gap: **measurement → vote
weight** is not attested by any in-window paper. The Benhaim et al.
quadratic-voting result (Mgmt Sci 2024) is the closest theory but was
strict-rejected in combo C at 1.5.

### What the four combos jointly attest

1. **(a) physical reliability of the substrate** is no longer a
   bottleneck on paper:
   - PHM with physics priors (combo A) gives calibrated indicators
     from low-data regimes.
   - ESP32-class hardware can carry the inference + attestation
     (combo D).
   - Open-source-hardware fab labs can replicate the node hardware at
     recoverable marginal cost (combo B · OLSK / HardwareX 2025).
2. **(b) recoverable surplus → discretionary wants**, only partially
   attested:
   - Engineering side (DfR, DfD, OSH) is solid.
   - Sociology side (post-growth empirical, time-banking, non-market
     work) does not match the v6 keyword list cleanly even though the
     direction-setting literature (Kallis et al. *Lancet Planetary
     Health* 2025) is strong.
3. **(c) measurement-direct priority** is half-attested:
   - Physical accounting (extended exergy, MFA + LCA) and a
     federated DPP substrate exist.
   - The collective-decision step that converts the per-node measured
     state into a global ordering is the remaining gap.

### Three load-bearing primitives (carry forward into code)

1. **L1 indicator output contract**:
   `health_indicator(window) → (score, group_score[], aleatoric_var,
   epistemic_var)`. Justified by I-GLIDE (combo A 2511.21208) and
   reinforced by UQ-Latent (combo A 2507.06672).
2. **Attested-emit envelope at the node**:
   the indicator is signed in a TEE (TrustZone class) before it
   leaves the L1 node. Justified by TZ-LLM (combo D 2511.13717).
3. **DPP-shaped persistence layer**:
   on-chain identity + commitments, off-chain bulky telemetry.
   Justified by Blockchain-DPP (combo C IJPR 2025).

### Three gaps that block end-to-end implementation

- **Sensor (not compute) attestation**: nothing surveyed signs the
  raw sensor reading at source. Sensing layer is the residual trust
  surface.
- **Measurement → vote-weight mapping**: no in-window paper directly
  derives a decision-weight from a physical quantity. Quadratic
  voting under uncertainty (Benhaim et al. 2024) is theory only.
- **Empirical sociology of non-market work measured at the node**:
  the closest evidence is large-scale time-use surveys, not sensor
  streams. The premise that *measurement replaces survey* is
  unattested.

## State after run 1 (v4, 2026-04-18) — historical

> Only combo-A (L1 × L3) had been surveyed. Two engineering primitives
> were flagged as recurring: PINN-driven health monitoring and
> peer-ranked / reputation-weighted consensus. Run 2 has supplanted
> both as primary lines, in favour of the wider v6 split.
