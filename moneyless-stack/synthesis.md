# synthesis.md

Cross-combo synthesis. Updated by task (d).

## State after v6 run 1 (2026-06-04 — all four combos surveyed)

### What is now attested in the literature

1. **Per-node calibrated health indicators with uncertainty** (combo-A):
   PHM models on the canonical turbofan / bearing benchmarks now emit
   `(score, aleatoric_var, epistemic_var)` natively, and the most
   recent (I-GLIDE, 2025-11) does it per sensor-group. This is the
   correct shape for the L1 → upper-layer interface.

2. **Repairability as a designed-in, measurable property** (combo-B):
   Design-for-Repair has consolidated into a feature/practice/measure
   taxonomy aimed at four distinct kinds of obsolescence. A
   *repairability measure* is itself a physical number — usable as a
   combo-C priority input.

3. **Sensor-grounded Digital Product Passport** (combo-C, 2.1):
   The DPP is no longer just a regulatory artefact; sensor-fed,
   per-stage-of-life environmental indicators are demonstrated end-to-
   end on a real (low-tech) manufacturing case. This is the
   measurement substrate a priority function consumes.

4. **Exergy as a candidate physical numeraire** (combo-C, 2.2):
   Extended exergy accounting reduces a heterogeneous resource flow
   to a single thermodynamic scalar; at industry scale 1992–2015 it
   gives a usable priority ordering.

5. **Judgment at the microcontroller, attested execution at the
   edge** (combo-D): TinyNav (2026-03) collapses sensor → action on
   an ESP32; GNNVault (2025-02) puts the privacy-critical portion of
   the same kind of inference inside Intel SGX. The two together
   sketch the L1 endpoint: lightweight local model + TEE for the
   parts that must be attested.

### What is *not* yet attested — the bridge

The four combos collide on the same gap: nothing in the surveyed set
binds the per-node uncertainty (combo-A) or the per-node measurement
(combo-C, combo-D) directly into a vote weight or priority weight.
Each side of the bridge exists; the bridge itself is absent.

The specific missing artefacts:

- An on-device uncertainty head on MCU-class hardware (combo-D × A).
  Surveyed UQ work is GPU/cloud; surveyed TinyML work is point
  predictions only.
- A remote-attestation envelope that carries `(decision, uncertainty,
  measurement_basis)` (combo-D × C). TPM-based attestation of
  binaries exists (2510.03219); attestation of the *decision* does
  not.
- A consensus protocol whose vote weight is bound to a physical
  scalar (e.g. node-local exergy budget or PHM confidence)
  (combo-A × C). The voting literature in window is mechanism-design-
  generic; no surveyed paper consumes a thermodynamic input.

### What is recorded as 근거 부족 rather than refuted

- The *absorption* half of combo-B (time use survey, non-market work,
  time banking, post-growth economics) — the tools available in this
  run do not cover the social-science indices well. Not a refutation,
  a coverage gap. Next combo-B re-entry should use Scopus / SSRN
  directly.
- On-device uncertainty estimation in combo-D — the search did reach
  the right shelf and there is no in-window paper. That's an
  evidence-of-absence finding inside the surveyed scope.

## Direction implied for next runs

- **Highest leverage**: build the missing bridge as code, since the
  parts are now individually well-attested. Concretely, prototype an
  L1 endpoint exposing `(score, var, attestation_quote)` on an MCU
  with a TEE. That is one task (b) per surveyed paper × link, with
  PHYSICAL_LINKS.md entries for each.
- **Cheapest fix**: re-run combo-B against Scopus / SSRN so the
  absorption side is no longer a 근거 부족.
- **Long shot**: search for an exergy-weighted consensus protocol
  outside the surveyed indices (likely industrial-ecology + cs.GT
  intersection). If found, it closes the bridge.

## Carry-forward open questions

- Can the I-GLIDE per-sensor-group uncertainty decomposition be
  preserved through a TEE boundary on an MCU-class device?
- Is there a node-local variant of extended exergy accounting, or
  does the numeraire only make sense at industry scale?
- Is the EU DPP schema rich enough to carry a per-decision
  uncertainty field, or does it need an extension?
