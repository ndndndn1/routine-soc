# synthesis.md

Cross-combo synthesis. Updated only by task (d).

## State after run 2 (Routine v6 rebaseline, 2026-04-19)

The v6 rebaseline ran all four combos at one date with sharper
keyword sets. The most useful change is that combo-A and combo-D
now exhibit a *coupled* pattern: combo-A papers all converge on the
output shape `(value, aleatoric, epistemic)`, and combo-D's QUTE
paper independently arrives at the same shape on a microcontroller.
This makes the L1 → L1-near-sensor port a small refactor, not a
research project.

### Recurring engineering primitives across combos

1. **Two-channel indicator output `(estimate, uncertainty)`**.
   Attested at server scale by combo-A (2507.06672, 2511.21208) and
   at microcontroller scale by combo-D (2404.12599 QUTE). This is
   now the routine's de-facto data shape across L1.
2. **Uncertainty-weighted fusion as a tokenless ranking rule**.
   Combo-C (2412.18024) gives the rule; combo-A papers give the
   per-source uncertainty; combo-D's TZ-LLM (2511.13717) gives the
   attestable execution envelope. Together these three pieces make
   "measurement → priority" implementable, not merely speculatable.
3. **Modular open hardware as the combo-B physical anchor**. Combo-B
   (2504.17249, Berkeley Humanoid Lite) is the only physical evidence
   in v6 that a non-trivial actuator stack can be field-rebuilt with
   consumer tooling. The social-science half of combo-B remains
   unattested in this corpus.

### The unattested bridge (still open)

Across all four combos, **no single surveyed paper signs a sensor
reading at the sensor**. Combo-D comes closest — TZ-LLM provides the
TEE envelope, QUTE provides the on-device indicator — but the *cryptographic
binding* of the indicator to a physical measurement (rather than to
the model that produced it) is unattested. This is now the most
concrete open research gap in the routine and is recorded for next
combo-D / cross-combo re-entry.

### Per-combo confidence (v6)

- **combo-A**: medium-high. Cluster is tight, three independent papers
  agree on indicator shape.
- **combo-B**: low. HF venue mismatch dominates; one engineering
  adoption + 근거 부족 for the social-science half.
- **combo-C**: low-medium. The two halves of the bridge exist
  separately, the bridge does not. Re-run via Scopus mandated.
- **combo-D**: medium-high. Three adoptions cover the three required
  sub-mechanisms.

### Carry-forward from run 1 (Routine v4)

The run-1 PINN-PHM and peer-ranked-consensus signals (2412.11967,
2510.03807, 2510.24801) are not invalidated by v6 — they were
adopted under wider keyword sets and remain valid for the
combo-A-physics-consensus / combo-D-physical-ai-substrate
historical INDEXes. v6 does not re-import them.

## Open questions (carry forward)

- Can the `(estimate, uncertainty)` pair be cryptographically bound
  to a *measurement* (not to the model)? combo-D close, combo-A and
  combo-C don't address.
- Is there a published empirical case study of cost-saved-→-allocated
  flow at community scale (combo-B sociology gap)?
- Does an exergy-weighted decision rule exist as code anywhere?
  (combo-C re-entry via Scopus)
- Tooling: HF is the wrong primary for combos B and C. Future runs
  must use SSRN / Scopus / ScienceDirect for those combos. Recorded
  here, not silently retried.
