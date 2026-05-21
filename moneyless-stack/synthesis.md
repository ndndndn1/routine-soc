# synthesis.md

Cross-combo synthesis. Updated only by task (d) or by a run that
changes any combo's adoption set.

## State after run 2 (2026-05-21, Research Routine v6)

All four combos have been surveyed once under v6. The literature now
supports a partial system sketch.

### What the literature gives us

```
                ┌─────────────────────────────────────────┐
                │           node-internal pipeline        │
                │                                         │
  sensor ──►   physics residual    ──►   RUL + UQ       │
   (raw)       (combo-A: PINN)            (combo-A: RaPP) │
                                                  │      │
                                                  ▼      │
                                          ┌──────────────┴──┐
                                          │ attested tuple  │
                                          │  (combo-D: TEE) │
                                          └────────┬────────┘
                ┌─────────────────────────────────┼────────┐
                │           inter-node protocol   │        │
                │                                  ▼        │
                │      DPP schema   ◄────  attestation_blob │
                │      (combo-C)                            │
                │           │                               │
                │           ▼                               │
                │   exergy aggregation                      │
                │   (combo-C: EEA)                          │
                │           │                               │
                │           ▼                               │
                │   priority / vote                         │
                │   *** LITERATURE GAP ***                  │
                └───────────────────────────────────────────┘
```

### Three load-bearing primitives now attested in literature

1. **(combo-A)** `rul_with_uncertainty(sensor_window) → (estimate,
   aleatoric_var, epistemic_var)` — RaPP-style autoencoder + variational
   posterior. Reproducible from C-MAPSS, plausible from PINN priors.
2. **(combo-D)** `attested_*(payload) → (payload, signature)` inside a
   commodity TEE (Intel SGX in GNNVault; Arm TrustZone in TZ-LLM). The
   attestation primitive transfers from LLM / GNN workloads to PHM
   workloads with engineering effort, not new research.
3. **(combo-C)** `exergy_aggregate(measurements[]) → scalar` via
   Extended Exergy Accounting; longitudinally applied to industrial
   sectors. Provides the canonical non-monetary unit of comparison the
   premise (c) requires.

### Two seams still open

- **Seam A↔D** (`attested PHM output`): no in-window paper wires
  combo-A's `(estimate, uncertainty)` tuple **through** combo-D's TEE
  pattern. The engineering pattern is obvious (run RaPP inside the
  secure world, sign the tuple); the literature gap is that nobody has
  published the combination. ROADMAP item #1.
- **Seam C↔C** (`measurement → decision`): combo-C's measurement half
  (DPP + EEA) does not yet connect to its decision half (QV / MCGDM).
  The two literatures don't cite each other. ROADMAP item #2.

### What is *not* yet attested (premise check)

- **Premise (a)** "production infra physically reliable": attested at
  *device scale* (PHM literature). Not at *system scale* (MTBF
  arguments for distributed substrates absent from all 4 combos).
- **Premise (b)** "surplus absorbs non-essential wants": **근거 부족**.
  Combo-B's sociology cluster (post-growth / time-banking / time-use)
  did not compound. The premise is currently load-bearing on argument,
  not on literature.
- **Premise (c)** "consensus from measurement directly": **half-
  attested**. Measurement transport (DPP) and aggregation unit (exergy)
  are real; vote / decision rule denominated in exergy is not.

## Open questions (carry forward)

- Is there a published TEE + PHM combination paper outside the window
  we searched, or in a venue HF doesn't index? (combo-A × combo-D)
- Is there an exergy-denominated voting mechanism in any cs.GT,
  ecological-economics, or political-economy venue? (combo-C internal)
- Can the sociology evidence (Lu 2024 timebanking, Kallis 2025 post-
  growth) be re-cast against a richer keyword set that compounds with
  combo-B's engineering side? (combo-B re-entry)

## Open questions (resolved since run 1)

- ✓ "Can a PHM indicator output be made directly signable / verifiable
  at the sensor, without trusted middleware?" — combo-D 2.3 (GNNVault)
  and 2.4 (TZ-LLM) show this is engineering-feasible on commodity TEE
  hardware. The remaining question is whether the PHM output specifically
  has been wired through, which is the Seam A↔D gap above.
- ✗ "Is there a published consensus protocol whose vote weight is bound
  to a measured physical quantity (exergy, error rate, MTBF)?" — still
  not observed. Seam C↔C above.
