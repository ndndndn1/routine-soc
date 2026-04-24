# combo-C — measurement-driven priority

## 0. Run metadata

- **run_date**: 2026-04-24
- **search_window**: 2024-04-24 → 2026-04-24
- **prior_run**: none (first combo-C run; v4's `combo-C-sustainability-dlt`
  directory has been renamed to this but never had content).
- **routine**: v6.
- **task**: (a) search + adoption.
- **primary tool**: HF `paper_search`. Combo-C's "주 도구" per v6 is
  Scopus/ScienceDirect for the environmental-accounting side and
  arXiv (cs.GT) for the mechanism side; HF straddles both imperfectly.

## 1. Executive summary

Combo-C asks whether a physical measurement can be turned directly
into a resource-priority ordering. The v6 keyword list mixes three
literatures: (i) thermodynamic accounting (`extended exergy
accounting`, `exergoeconomics`, `thermoeconomics`), (ii) environmental
footprint tracing (`LCA`, `MFA`, `ecological footprint accounting`,
`supply chain traceability`, `digital product passport`), and
(iii) social choice + UQ (`quadratic voting`,
`uncertainty-weighted decision making`).

Under strict v6 scoring, **no HF paper clears ≥ 2.5** across the
keyword set. Three papers approach but do not reach the threshold:
Falk et al. 2509.00093 (multi-criteria LCA of GPU training, 2.0),
Desroches et al. 2501.14334 (corporate AI LCA, 2.0), and Khorshidi &
Aickelin 2012.01569 (interval-data MCGDM, out of window). The
thermodynamic-accounting half of combo-C returned zero in-window HF
papers. Per v6 rule, combo-C is recorded as **근거 부족** on HF;
follow-up on Scopus/ScienceDirect is required and is explicitly noted
in ROADMAP as the next combo-C run's priority.

## 2. Adopted papers (≥ 2 keywords, sum ≥ 2.5)

**None.**

### 2.x Near-miss: More than Carbon — Cradle-to-Grave environmental impacts of GenAI training on Nvidia A100

- **arxiv**: 2509.00093 · https://hf.co/papers/2509.00093
- **year**: 2025 (Aug 27)
- **matched_keywords**:
  - `life cycle assessment` — 1.0 (explicit: "multi-criteria LCA")
  - `material flow analysis` — 0.5 (partial: "mineral and metal
    depletion 33% higher with primary data")
  - `ecological footprint accounting` — 0.5 (partial: 16 environmental
    impact categories)
  - **sum**: 2.0 → below threshold
- **note**: Strongest HF candidate. Demonstrates that a disciplined
  LCA can resolve *which stage* of a compute product drives each
  category of impact — the exact operation the stack needs for
  priority ordering. Fails adoption because no second distinct
  keyword reaches 1.0; if v6 added `primary-data LCA` as a standard
  keyword it would clear.

### 2.x Near-miss: Exploring the sustainable scaling of AI dilemma

- **arxiv**: 2501.14334 · https://hf.co/papers/2501.14334
- **year**: 2025 (Jan 24)
- **matched_keywords**:
  - `life cycle assessment` — 1.0 (explicit)
  - `supply chain traceability` — 0.5 (partial: "greater transparency
    from all actors of the value chain")
  - `material flow analysis` — 0.5 (partial: "end-of-life processes")
  - **sum**: 2.0 → below threshold

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | — | out of scope for combo-C. |
| (b) surplus absorption | — | out of scope for combo-C. |
| (c) priority derived from physical measurement | 1 | LCA is widely demonstrated as a measurement-to-category mapping, but the mapping-to-priority step (a rank or allocation over categories) is not attested inside the window on HF. Quadratic-voting literature (which is the mechanism that could close this gap) returned no in-window matches on HF either. |

**Aggregate**: combo-C is the combo whose two constituent literatures
(thermoeconomic accounting + physical-measurement-to-governance
mechanism design) most conspicuously live in venues outside HF's
reach. The current-run conclusion is **근거 부족**, which per v6
triggers a tool-change in the next combo-C run rather than a
keyword-set change.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (re-enter on Scopus / ScienceDirect next
run, per v6 "주 도구"):**
- emergy synthesis (Odum tradition, a close cousin of extended exergy)
- ecological-economic footprint accounting at product level
- exergoeconomic optimisation of industrial processes
- blockchain-based digital product passport pilot
- quadratic voting deployment (e.g. Colorado appropriations experiment)

**Two under-explored adjacent fields:**
- Material passports for the built environment (construction /
  demolition).
- Algorithmic mechanism design for commons governance (Ostrom +
  Weyl lineage).

## 5. Search log

| keyword (query used) | source | returned | in-window | pooled | ≥ 2.5 |
|---|---|---|---|---|---|
| life cycle assessment supply chain material flow | HF | 8 | 3 | 3 | 0 |
| digital product passport traceability supply chain | HF | 8 | 2 | 2 | 0 |
| quadratic voting mechanism design preferences | HF | 8 | 1 | 1 | 0 |
| exergy analysis thermoeconomics energy accounting | HF | 6 | 2 | 2 | 0 |
| uncertainty-weighted decision making multi-criteria | HF | 8 | 2 | 2 | 0 |
| digital product passport battery EU | HF | 5 | 2 | 2 | 0 |
| exergy accounting industrial process sustainability | HF | 6 | 2 | 2 | 0 |
| quadratic voting collective decision budget allocation | HF | 6 | 2 | 2 | 0 |

- pooled in-window unique candidates: ~12
- ≥ 2.0 but < 2.5: 2509.00093 (2.0), 2501.14334 (2.0)
- ≥ 2.5 adopted: **0**
- rejected at < 2.0: 2502.06874 (GREEN, 1.0), 2311.03124 (TAMPAR,
  out of window), 2404.05198 (participatory budgeting lotteries,
  0.5 — PB-adjacent but no QV / physical-measurement linkage),
  2410.15168 (electoral CDM for LLMs, 0.5).

**Search confidence**: low-medium on HF. Environmental-accounting
literature is strongly indexed in Scopus / ScienceDirect (Ecological
Economics, J. of Industrial Ecology, Resources Conservation &
Recycling) and not on HF. Mechanism-design literature is in arXiv
cs.GT which is partially in HF but this run's queries did not surface
in-window QV papers specifically. Correct escalation is Scopus for (i)
and direct arXiv cs.GT queries for (ii).
