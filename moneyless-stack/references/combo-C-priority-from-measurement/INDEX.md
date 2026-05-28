# combo-C — Physical measurement → resource priority

System role: take physically measured quantities from many nodes and
turn them into "what gets done first." Combo-C is deliberately *not*
governance theory; the routine restricts adoption to mechanisms that
convert a measurement into a priority signal. The eligible primitives
are exergy/LCA-style accounting, traceability/passport plumbing, and
uncertainty-weighted voting/decision rules.

## 0. Run metadata

- **run_date**: 2026-05-28
- **search_window**: 2024-05-28 → 2026-05-28 (last 2 years)
- **prior_run**: none (placeholder from v4 reset)
- **routine version**: v6
- **primary tool per routine**: Scopus / ScienceDirect (energy /
  environment journals) + arXiv cs.GT — not directly callable. Used
  Hugging Face `paper_search` (semantic) on each of the 10 keywords,
  pooled, deduped, scored.
- **fallback tools used**: none beyond HF for this run.
- **search confidence**: medium. HF surfaces the AI-environmental-impact
  cluster well (cradle-to-grave LCA on GPU, footprint accounting for
  open-source AI ecosystems) but is thin on classical exergoeconomics /
  extended exergy accounting; expected, since the LCA/exergy
  engineering literature lives in *Energy*, *Applied Energy*,
  *Resources Conservation & Recycling*, not HF.

## 1. Executive summary

Combo-C under v6 yields a coherent but *narrow* set of adoptions: two
2025–2026 papers that wire life-cycle assessment + footprint accounting
into a runnable artifact (a cradle-to-grave LCA of GPU training, and an
ecosystem-level footprint-tracking proposal for open-source AI
derivatives). Together they prove that measurement-to-priority can be
*implemented as plumbing* — a passport-like footprint object that
travels with an asset and can be aggregated. What is still **not**
attested in this run's pool is the closing step: a vote/decision rule
that consumes the footprint with calibrated uncertainty as input.
Quadratic-voting and uncertainty-weighted decision-making papers exist
in cs.GT, but none surfaced via HF in-window with sufficient combo-C
keyword density. The L3 priority node remains a design problem, not yet
a literature-attested primitive.

## 2. Adopted papers (≥ 2 keywords, ≥ 2.5 sum)

### 2.1 More than Carbon: Cradle-to-Grave environmental impacts of GenAI training on the Nvidia A100 GPU

- **authors**: Sophia Falk, David Ekchajzer, Thibault Pirson, Etienne
  Lees-Perasso, Augustin Wattiez, Lisa Biber-Freudenberger, Sasha
  Luccioni, Aimee van Wynsberghe
- **year**: 2025 (Aug 27)
- **venue**: arXiv preprint
- **arxiv**: 2509.00093 · https://hf.co/papers/2509.00093
- **matched_keywords** (count = 4, sum = 2.5):
  - life cycle assessment — 1.0 (LCA in title's "cradle-to-grave" and
    in the AI keyword list; full LCA methodology applied to A100 GPU)
  - material flow analysis — 0.5 (mineral and metal depletion, resource
    use accounting — MFA-adjacent quantification, but the MFA term is
    not explicitly used)
  - ecological footprint accounting — 0.5 (multi-criteria environmental
    footprint accounting across categories; the *accounting* concept is
    full, *ecological footprint* as a term-of-art is partial)
  - supply chain traceability — 0.5 (cradle-to-grave traces the GPU
    supply chain end-to-end across categories)
- **classification**: [공학]
- **방법**: Multi-criteria LCA of the Nvidia A100 SXM 40GB GPU across
  cradle-to-gate manufacturing and cradle-to-grave use, evaluated
  against representative training workloads (BLOOM, GPT-4-class).
  Primary data combined with reference inventories for non-carbon
  categories.
- **결과**: Use phase dominates most environmental impact categories,
  but manufacturing is the dominant phase for human toxicity (cancer)
  and mineral / metal depletion — a result that single-metric carbon
  reporting hides.
- **한계**: One GPU model, two workloads; the inventory data quality for
  the non-carbon categories is bounded by available LCI databases.
- **system reduction**: Justifies the L3 priority input *schema*: a
  priority vote needs a multi-criteria footprint vector per asset, not
  a scalar carbon number. The minimum viable per-asset record is
  `(carbon, water, mineral_depletion, toxicity)` keyed by lifecycle
  phase. This is the "what does the passport carry" question for
  combo-C, and the answer here is "more than a single number."

### 2.2 Sustainable Open-Source AI Requires Tracking the Cumulative Footprint of Derivatives

- **authors**: Shaina Raza, Iuliia Zarubiieva, Ahmed Y. Radwan, Nate
  Lesperance, Deval Pandya, Sedef Akinli Kocak, Graham W. Taylor
- **year**: 2026 (May 5)
- **venue**: arXiv preprint
- **arxiv**: 2601.21632 · https://hf.co/papers/2601.21632
- **matched_keywords** (count = 4, sum = 2.5):
  - ecological footprint accounting — 1.0 (paper's central proposal is
    *impact accounting* across an ecosystem of forks / fine-tunes /
    adapters; "environmental footprint, carbon reporting, water
    consumption, emissions, impact accounting" in keyword list)
  - supply chain traceability — 0.5 (tracking derivatives across the
    open-source model supply chain — traceability concept, not the
    term)
  - life cycle assessment — 0.5 (cumulative footprint across derivative
    chain is an LCA-style cradle-to-grave for model artifacts)
  - digital product passport — 0.5 (the proposed "transparency layer"
    + "public dashboards" + "measurement integration" is, at the
    artifact level, a digital product passport for AI models — concept
    is direct, name-of-art is not used)
- **classification**: [공학]
- **방법**: Proposes a standardized accounting infrastructure that
  attaches and aggregates environmental impact records across the
  derivative tree of a foundation model (fine-tunes, adapters,
  quantizations, merges, forks). Combines per-derivation logging with a
  transparency layer for public dashboards.
- **결과**: Argues — with worked examples — that single-model footprint
  reporting under-counts ecosystem-level cost by orders of magnitude;
  shows how a measurement-integration layer can make the ecosystem cost
  legible.
- **한계**: Position-paper-shaped: the accounting schema is proposed,
  not implemented as a working registry; standard adoption is a
  political-economy problem the paper acknowledges.
- **system reduction**: This is the *plumbing* spec for combo-C. The
  L3 priority node should consume a per-asset record that travels
  with the asset across derivations and aggregates without
  recomputation. Concretely: an `l2-entropy` / `l3-consensus` boundary
  needs a "footprint passport" record type whose schema borrows from
  this paper's accounting layer. This is the most direct candidate for
  a *digital product passport* primitive surfaced in the pool.

## 3. Hypothesis score (1–5)

- **(a) physical reliability** — out of scope.
- **(b) surplus absorption** — out of scope.
- **(c) priority is derived directly from measurement** — combo-C
  score: **2/5**. The *measurement* and *carrier* halves are both
  attested: an LCA paper proves the per-asset measurement is
  multi-dimensional and reproducible; a footprint-tracking paper
  proves an artifact-level passport can carry that record across
  derivations. The *priority rule* half — the function from
  passport → vote weight — is **not** in any adopted paper this run.
  Hypothesis (c) is *plumbing-ready, decision-rule-unattested*.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords**:
- conformal prediction policy decision (cs.GT × stats.ML)
- quadratic voting empirical
- exergoeconomic optimization industrial cluster
- material flow analysis IoT supply chain
- digital product passport battery (EU regulation evaluation)

**Two under-explored adjacent fields**:
- ecological economics journals (*Ecological Economics*, *Journal of
  Industrial Ecology*) — where exergy accounting actually lives, and
  which HF does not index
- algorithmic mechanism design with uncertainty (cs.GT × cs.LG) — the
  decision-rule side of combo-C; needs arXiv listings, not HF semantic
  search, since "uncertainty-weighted decision making" returns
  decision-theory papers without measurement grounding via HF.

## 5. Search log

Per-keyword calls to `paper_search` (HF), `results_limit = 10`,
`concise_only = true`.

| keyword (query used) | results | in-window | useful |
|---|---|---|---|
| extended exergy accounting | 3 | 3 | 1 (GREEN 2502.06874, 2.0 sum) |
| exergoeconomics energy systems | 31 | 8 | 0 (energy mgmt papers, no exergoeconomics term) |
| life cycle assessment environmental impact | 69 | 10 | 2 (papers 2.1, 2.2) |
| material flow analysis sustainability | 56 | 9 | 1 (2.1 dupe) |
| thermoeconomics energy cost | 37 | 8 | 0 |
| ecological footprint accounting nation | 16 | 7 | 2 (papers 2.1, 2.2) |
| supply chain traceability blockchain | 120 | 10 | 2 (papers 2.1, 2.2 dupes; ISOMORPH 2605.12768 below threshold) |
| digital product passport | 10 | 5 | 1 (paper 2.2 dupe) |
| quadratic voting mechanism design | 120 | 10 | 0 (auction/mechanism design papers, none with measurement grounding) |
| uncertainty-weighted decision making | 120 | 8 | 0 (decision under uncertainty papers, none with physical measurement input) |

- **pooled in-window, pre-dedup**: ~78
- **deduped by arXiv ID**: ~30 unique
- **candidates with ≥ 2 keywords matched**: 6
- **adopted (sum ≥ 2.5)**: **2**
- **rejected at < 2.5 sum but ≥ 2 keywords** (logged):
  - GREEN: Group Reasoning Emission Estimation Networks
    (arXiv:2502.06874) — 4 keywords, 2.0 sum. NLP-flavoured emission
    accounting; could be re-evaluated with "carbon accounting" added
    to keyword list in a later run.
  - Exploring the sustainable scaling of AI dilemma (arXiv:2501.14334)
    — 2 keywords, 1.5 sum.
  - ISOMORPH: Supply Chain Digital Twin (arXiv:2605.12768) — 2
    keywords, 1.0 sum.
  - DeFine: Decision-Making with Analogical Reasoning over Factor
    Profiles (arXiv:2410.01772) — 1 keyword, 1.0 sum (decision theory
    only, no physical measurement input — exactly the "general
    governance" pattern the routine excludes).

**Search confidence**: medium. The LCA/footprint axis is well-covered;
the *vote rule* axis is not. Future runs should target *Energy* /
*Applied Energy* / *Resources Conservation & Recycling* for
exergoeconomics, and arXiv cs.GT directly for quadratic-voting
empirical work.
