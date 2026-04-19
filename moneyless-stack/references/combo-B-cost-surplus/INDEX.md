# combo-B — Marginal-cost decline → non-essential want absorption

System role: ground the budget by which physically saved capacity
(repair, longer service life, shared tooling, leisure time) is
diverted to want-side activities without breaking the system.

## 0. Run metadata

- **run_date**: 2026-04-19
- **search_window**: 2024-04-19 → 2026-04-19 (last 2 years)
- **prior_run**: combo-B-zmc-slack (placeholder only — no adopted
  papers; v6 is the first real run of this combo).
- **routine_version**: v6
- **task**: (a) search + adoption + INDEX.md
- **primary tool**: Hugging Face `paper_search` (semantic).
  Acknowledged limitation: HF index is ML-centric, so the social-
  science keywords (`time use survey`, `non-market work`,
  `post-growth economics`, `time banking`) are intrinsically
  under-served. Per routine, no keyword expansion — under-served
  keywords are recorded as 근거 부족.

## 1. Executive summary

Combo-B asks for *physical and social* mechanisms that absorb saved
marginal cost. The HF pool returns one defensible engineering anchor
(open-source modular hardware) and several adjacent-but-thin signals
(circular-economy topic modelling, community-currency network
topology). The strict ≥2-keyword + ≥2.5-sum threshold is met by **one
paper only** (open-source 3D-printed humanoid, scored generously on
modularity). The remaining 9 keywords return either out-of-window or
sub-threshold material; this is not a failure of the keyword design,
it is a venue mismatch — the adopted-paper count is therefore low and
flagged as **근거 부족** for the social-science half of the combo. No
sociology paper is adopted in this run; ROADMAP gets no sociology
update from combo-B v6.

## 2. Adopted papers (≥ 2 matches AND sum ≥ 2.5)

### 2.1 Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot

- **authors**: Yufeng Chi, Qiayuan Liao, Junfeng Long, Xiaoyu Huang,
  Sophia Shao, Borivoje Nikolic, Zhongyu Li, Koushil Sreenath
- **year**: 2025 (Apr 24)
- **venue**: arXiv preprint
- **arxiv**: 2504.17249 · https://hf.co/papers/2504.17249
- **matched_keywords**:
  - `open source hardware` — **1.0** (full phrase: "Open-source ...
    3D-printed Humanoid Robot")
  - `design for repair` — **0.5** (modular cycloidal-gear design
    enables part replacement; partial of explicit "design for repair")
  - `design for disassembly` — **0.5** ("modular design", "3D-printed
    components" enable field disassembly; partial)
  - `circular economy product design` — **0.5** (3D-printed parts +
    modular replaceable joints satisfy CE-design heuristics in
    spirit; partial)
  - **count = 4**, **sum = 2.5**
- **classification**: [공학]
- **summary**:
  - **[방법]** Cycloidal-gear humanoid joints are 3D-printable on
    consumer printers; the full BOM, CAD, controller, and RL policy
    are open-sourced; zero-shot policy transfer to physical hardware
    demonstrated.
  - **[결과]** A bipedal research platform reproducible at fab-lab
    scale (~$5k order of magnitude); modular joint replacement
    without disassembling unrelated subsystems.
  - **[한계]** Robotics-domain only; no LCA on print-vs-machined
    parts; "open source" here is openness of files, not openness of
    the silicon.
- **system reduction**: Justifies, as physical evidence, the routine's
  premise that a non-trivial actuator stack can be field-rebuilt with
  consumer tooling. Reduces to a *capability assumption* the L2
  budget calculation is allowed to make: "joint replacement does not
  require external supply chain". No code yet — captured as a
  proposed assumption in `synthesis.md`.

## 3. Hypothesis score (1–5)

| sub-hypothesis | score | note |
|---|---|---|
| (a) physical reliability | — | out of combo-B scope. |
| (b) surplus absorbs non-essential wants | 1 | one engineering paper attests reproducibility-at-cost; nothing in the surveyed window attests the *allocation* mechanism (time banking / post-growth) at empirical scale. |
| (c) physical-measurement consensus | — | out of combo-B scope. |

**Aggregate**: combo-B v6 is **structurally under-supported** by the
HF index for the social-science half. The engineering half has one
solid attestation (open hardware + modular joints). Honest read: the
"surplus → wants" transfer remains unattested as a physical
mechanism in this surveyed corpus.

## 4. Follow-up keywords + adjacent fields

**Five follow-up keywords (next combo-B re-entry, possibly via
SSRN/Scopus rather than HF):**
- modular product architecture
- repair-time elasticity
- household time allocation diary
- maker-space throughput
- product-as-service decoupling

**Two under-explored adjacent fields:**
- Industrial symbiosis case studies (Kalundborg-style) — would
  empirically attest cost-saved-→-allocated flows.
- Computational social science of mutual-aid networks — would attest
  the demand-side absorption.

**Tooling note:** if combo-B is re-run, the *primary* tool should
shift away from HF to SSRN / Google Scholar / KCI / Scopus. HF is
diagnosed as wrong-venue for this combo's social-science keywords.
This is recorded in synthesis.md, not silently retried.

## 5. Search log

| keyword (query used) | results | in-window | notes |
|---|---|---|---|
| right to repair consumer electronics | 0 | 0 | HF index returned nothing |
| design for disassembly circular economy | 10 | 6 | mostly waste-sorting / e-waste vision |
| circular economy product design | 10 | 5 | overlap with prior; topic-modelling adjacent |
| open source hardware fab lab manufacturing | 10 | 5 | EDA / Verilog dominate; Berkeley-Humanoid-Lite is the one fit |
| time use survey non-market work | 0 | 0 | venue mismatch |
| post-growth economics degrowth | 6 | 4 | all are macro-econ / climate-econ, none on degrowth as such |
| time banking community currency | 2 | 1 | community-currency network paper only |

- **pooled after in-window filter, pre-dedup**: ~21
- **dedup**: removed 4 cross-keyword duplicates (mostly the
  circular-economy topic-modelling paper appearing thrice).
- **scored ≥ 2 keywords**: 4 candidates
- **scored ≥ 2.5 sum AND ≥ 2 keywords (adopted)**: **1** (Berkeley
  Humanoid Lite, above)
- **rejected at < 2.5 / not in window**: 2503.03998 (Robotic prying,
  sum 1.0), 2401.06528 (PCB-Vision, out of window), 2405.10452 (CE
  topic modelling, sum 1.0), 2510.18513 (DWaste, 0.5), 2409.13674
  (Community currency network topology, 0.5), 2506.11061 (Engineered
  timber reusability, 1.0).

**Search confidence**: low. HF venue mismatch dominates. Per routine
"신뢰도 낮으면 '근거 부족' 명시. 추측 금지." — the combo-B v6 run is
recorded as **partially supported (1 adoption) + 근거 부족 for the
social-science axis**.
