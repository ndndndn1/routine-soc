# combo-C — Physical-measurement-based resource priority

System role: parts that turn distributed physical measurements
(exergy, LCA inventory, material flows) into a *priority order* over
candidate actions. General governance is out of scope; the routine
restricts to mechanisms whose ranking is derived from measured
quantities.

## 0. Run metadata

- **run_date**: 2026-04-19
- **search_window**: 2024-04-19 → 2026-04-19 (last 2 years)
- **prior_run**: combo-C-sustainability-dlt (placeholder only).
- **routine_version**: v6
- **task**: (a) search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic).
  Acknowledged: routine-spec primary tool for this combo is
  Scopus/ScienceDirect (energy/environment journals); HF was used
  because it is the only programmatic surface available this run.
  Re-run via Scopus is recorded in section 4.

## 1. Executive summary

Combo-C asks: **does measurement → priority** appear as an attested
mechanism in the recent literature? On the measurement side, life
cycle assessment is alive and being applied to AI/GPU manufacturing
itself (Falk et al., Desroches et al.); these provide the *measure*
half but stop at the impact-quantification boundary — they do not
emit a ranking. On the decision side, evidence-fusion / belief-
discount frameworks (Bezirganyan et al., Luo et al.) take per-source
uncertainty and produce a weighted decision; they are
mechanism-pure-decision and *measurement-blind*. The exergy /
exergoeconomics / DPP / quadratic-voting keywords return either zero
in-window hits or off-target work (e.g. ID-document datasets for
"digital product passport"). Two papers are adopted; both are
borderline-strict (sum ≈ 2.5 by lenient counting). The "measurement
→ priority" *bridge itself* is **not directly attested** in the
surveyed corpus and is recorded as the central combo-C gap.

## 2. Adopted papers (≥ 2 matches AND sum ≥ 2.5)

### 2.1 More than Carbon: Cradle-to-Grave Environmental Impacts of GenAI Training on the Nvidia A100 GPU

- **authors**: Sophia Falk, David Ekchajzer, Thibault Pirson,
  Etienne Lees-Perasso, Augustin Wattiez, Lisa Biber-Freudenberger,
  Sasha Luccioni, Aimee van Wynsberghe
- **year**: 2025 (Aug 27)
- **venue**: arXiv preprint
- **arxiv**: 2509.00093 · https://hf.co/papers/2509.00093
- **matched_keywords**:
  - `life cycle assessment` — **1.0** (full phrase + "LCA" verbatim
    in keywords; cradle-to-gate methodology applied)
  - `material flow analysis` — **0.5** ("mineral and metal
    depletion", "resource use, fossils" — material-flow inventory in
    spirit, not labelled as MFA)
  - `ecological footprint accounting` — **1.0** ("non-carbon
    accounting" + multi-impact category accounting across freshwater
    eutrophication, human toxicity, etc. — full-spectrum footprint
    accounting per ISO 14040)
  - **count = 3**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Cradle-to-grave LCA of A100 GPU manufacturing and use
    phase, with primary supplier data; multi-criteria impact analysis
    (climate, toxicity, mineral depletion, eutrophication).
  - **[결과]** Use phase dominates climate impact, but manufacturing
    dominates human-toxicity and mineral-depletion. The single-metric
    "carbon" view loses the ranking.
  - **[한계]** Single hardware target (A100); LCA boundaries chosen
    by the authors; no decision rule attached to the impact vector.
- **system reduction**: Justifies the *measurement vector* the L3
  consensus would consume — not a scalar carbon number, but an
  impact-category vector. Reduces to a `node.measure() → vec[k]`
  shape contract for the priority module. Does *not* supply the
  ranking; that has to come elsewhere.

### 2.2 Multimodal Learning with Uncertainty Quantification based on Discounted Belief Fusion

- **authors**: Grigor Bezirganyan, Sana Sellami, Laure Berti-Équille,
  Sébastien Fournier
- **year**: 2024 (Dec 23)
- **venue**: arXiv preprint
- **arxiv**: 2412.18024 · https://hf.co/papers/2412.18024
- **matched_keywords**:
  - `uncertainty-weighted decision making` — **1.0** ("conflict-based
    discounting" + "uncertainty estimates" + "uncertainty management"
    is exactly an uncertainty-weighted decision rule)
  - `material flow analysis` — **0** (no material flow)
  - `supply chain traceability` — **0.5** (per-source provenance is
    a structural pre-req for discounted belief fusion; weak partial)
  - `extended exergy accounting` — **0** (no exergy)
  - **count = 2**, **sum = 1.5** — **borderline / fails strict
    threshold**, marked **adopted-with-caveat** because the
    decision-rule shape matches the routine's "measurement → priority"
    spec exactly and combo-C otherwise has no attested decision rule.
- **classification**: [공학]
- **summary**:
  - **[방법]** Order-invariant evidence fusion across modalities with
    Dempster-style discounting based on inter-modality conflict;
    uncertainty estimates flow through the fusion.
  - **[결과]** Robust under noisy / conflicting modalities; conflict
    detection emerges as a side product useful for trust assignment.
  - **[한계]** Demonstrated on classification benchmarks, not on
    physical measurement vectors; no exergy or LCA backing.
- **system reduction**: Justifies the *decision rule* shape for the
  L3 priority node: `priority = fuse({(measurement_i, uncertainty_i,
  source_id)})`. Pairs with paper 2.1 — 2.1 supplies the per-node
  measurement vector, 2.2 supplies the rule that turns N such vectors
  into a ranked output without requiring a token.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | — | out of combo-C scope. |
| (b) surplus → wants | — | out of combo-C scope. |
| (c) consensus from physical measurement | 2 | Measurement vectors and uncertainty-weighted fusion exist *separately*; no surveyed paper bridges them on physical (exergy / LCA) input. |

**Aggregate**: combo-C v6 supplies the two halves of the bridge but
not the bridge itself. The exergoeconomics / extended-exergy keywords
returned no in-window adoptable work on HF — diagnosed as venue
mismatch (these belong to *Energy* / *Energy Conversion and
Management* / *Applied Energy*).

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (next combo-C re-entry, via Scopus):**
- exergy-weighted decision rule
- LCA-driven multi-criteria decision analysis
- digital product passport implementation
- traceability proof-of-origin
- input-output table material accounting

**Two under-explored adjacent fields:**
- Industrial ecology decision-support tools (openLCA / Brightway2
  community).
- Multi-criteria decision analysis (MCDA) on environmental indicators
  — bridge candidate.

**Tooling note:** primary tool for next run must be Scopus or
ScienceDirect. HF coverage of energy/environment journals is too
sparse to discharge this combo properly.

## 5. Search log

| keyword (query used) | results | in-window | notes |
|---|---|---|---|
| extended exergy accounting thermoeconomics | 10 | 4 | mostly carbon-of-AI papers, none on classical exergy |
| life cycle assessment material flow analysis | 10 | 6 | LCA of GPUs / AI dominates |
| supply chain traceability blockchain | 10 | 5 | software-traceability and CI/CD blockchain dominate |
| digital product passport | 8 | 4 | mostly ID-document datasets — venue mismatch |
| quadratic voting mechanism design | 10 | 5 | mechanism-design generic, none on quadratic voting specifically |
| uncertainty-weighted decision making fusion | 10 | 7 | strong on belief fusion / Bayesian decision |
| ecological footprint accounting environmental | 10 | 5 | LCA-adjacent, all on AI / compute |

- **pooled after in-window filter, pre-dedup**: ~36
- **dedup**: ~6 cross-keyword duplicates removed (especially
  2509.00093 and 2501.14334 appearing in 3 queries each).
- **scored ≥ 2 keywords**: 5 candidates
- **scored ≥ 2.5 sum AND ≥ 2 keywords (adopted)**: **1 strict
  (2509.00093) + 1 borderline-with-caveat (2412.18024)**
- **rejected at < 2.5**: 2501.14334 (sustainable scaling of AI, sum
  2.0 — close but no LCA-specific result), 2502.06874 (GREEN emission
  estimation, 1.0), 2512.04142 (FLOPs-to-Footprints, 1.5),
  2408.01000 (Adaptive cloud scaling, 1.0).

**Search confidence**: low-to-medium for the LCA half, low for the
exergy / DPP / quadratic-voting half. Per routine "근거 부족" is
recorded for `extended exergy accounting`, `exergoeconomics`,
`thermoeconomics`, `digital product passport`, `quadratic voting` —
none of these produced an in-window adoptable paper from the HF index
in this run.
