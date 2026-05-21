# ROUTINE

This directory is driven by `Research Routine v6`. The routine spec
lives in the session instructions (not checked in verbatim); this file
records the version, the loop semantics, and the structural invariants.

## Loop semantics

Each run executes the loop **across all 4 combos** (A → D), then writes
or updates:

- `references/combo-X-*/INDEX.md` per the §-structure below
- `ROADMAP.md` changelog entry per combo
- `synthesis.md` cross-combo synthesis (only if a combo's adoption set
  changed)
- `candidate-advisors.md` for new recurring authors

Sociology papers update **ROADMAP only** — they do not justify physical
links or code changes.

## Combos (v6)

- **combo-A — physics-input** : 센서 → (estimate, uncertainty) at L1
- **combo-B — cost-surplus**  : low marginal cost → non-essential want
  absorption
- **combo-C — priority-from-measurement** : physical measurement →
  cross-node priority (exergy / LCA / DPP)
- **combo-D — near-sensor-judgment** : node-internal judgment + TEE /
  attestation

## INDEX.md structure (v6)

```
0. Run metadata (run_date, search_window, prior_run, routine version,
   primary tool, fallback tools)
1. Executive summary (5 sentences)
2. Adopted papers (≥ 2 keywords matched AND ≥ 2.5 score)
   - title / authors / year / venue / DOI or arXiv ID
   - matched_keywords: [...] with per-keyword score and total
   - 분류: [사회학] or [공학] or both
   - 방법 / 결과 / 한계
   - system reduction (1-2 sentences: which node / link / function)
   - [NEW] flag
3. Hypothesis score (1-5, 부품 가치 점수) — direct-support not required
4. Follow-up: 5 keywords + 2 adjacent fields
5. Search log (per-keyword pool sizes, dedup, adopted/rejected counts)
```

## Default deny (still in force)

All inter-node communication is **closed by default**. A link opens only
after a physical basis is justified in `PHYSICAL_LINKS.md` with ≥ 1
engineering reference. Sociology papers never justify a link.

## Routine invariants

- 가설 직접 지지 논문은 드물다. 부품을 모은다.
- 채택 수 저조 시 키워드 확장 금지. "근거 부족"으로 기록.
- 검색 도구 우선순위는 combo별 "주 도구" (§ in routine spec) 따름.
- Stub containers must `docker compose up` cleanly before any feature
  is added on top of a node.

## Version history

- **v4** (run 1, 2026-04-18): one-task-per-run, 3-layer L1/L2/L3 framing,
  4 combos with consensus-centric naming.
- **v6** (run 2, 2026-05-21): all-4-combos-per-run loop; combo names
  re-scoped around mechanism rather than layer; explicit ≥ 2-keyword
  adoption rule; sociology vs. engineering classification.
