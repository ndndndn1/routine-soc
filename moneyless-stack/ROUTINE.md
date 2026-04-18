# Research & Build Routine v3

This file pins the operating contract of the repository. The routine spec
itself is stored under `references/` in each run only if it changes;
otherwise this file is the canonical copy.

## Purpose

점진적으로 자급자족 시스템을 구축한다. 최소 단위(노드)가
자체 판단하고, 노드 간 통신은 물리적으로 실제 구현 가능할 때만
연결된다. 기본값은 통신 불가 (default deny).

- 사회학 논문: 시스템의 방향성 (무엇을 만들 것인가) → `ROADMAP.md`
- 공학 논문: 실행안 (어떻게 만들 것인가) → `nodes/`, `PHYSICAL_LINKS.md`
- 리포지토리 루트: 매 실행마다 조금씩 동작하는 시스템 형상

## Core Hypothesis

화폐는 신뢰의 대용물이다. 따라서
(a) 생산 인프라 물리적 신뢰성이 충분히 높고
(b) 잉여 자원을 비필수 욕구에 회복 가능 범위 내에서 할당 가능하며
(c) 자원 우선순위 합의가 물리적 측정값에서 직접 도출되면
→ 화폐의 매개 기능은 잉여가 된다.

## 3-Layer Stack

| Layer | Name | Role |
| ----- | ---- | ---- |
| L1    | Reliability Physics | 고장 안 나는 생산 하부 |
| L2    | Entropy Buffer      | 잉여 자원의 욕구 할당 |
| L3    | Physical Consensus  | 측정값 직결 분산 합의 |

## Node Communication Model — default deny

- 모든 노드는 독립 docker container.
- `docker-compose.yml` 의 networks 는 기본 `internal: true` 로 격리.
- 두 노드가 통신하려면 다음을 모두 충족:
  1. `PHYSICAL_LINKS.md` 에 통신의 물리적 근거 기재
  2. 해당 link 가 최소 1편의 공학 논문으로 뒷받침됨
  3. compose 에 명시적 network 정의 + 양 노드 join
- 위 3개 중 하나라도 누락 시 통신 금지.
- 사회학 논문만으로는 link 를 열 수 없음 (방향성 자료일 뿐).

## Search Constraints

- 출판일 최근 2년
- 신조어 우회: PoPC ≈ DePIN/PoUW/verifiable physical computation;
  REA ≈ ludic economy / leisure as commons / slack theory
- 도구 우선순위: arXiv → Semantic Scholar → Google Scholar → IEEE Xplore
- 신뢰도 낮으면 "근거 부족" 으로 명시. 추측 금지.

## Per-Combo INDEX.md Structure

0. 실행 메타: run_date, search_window, prior_run
1. Executive Summary (5 문장)
2. 논문 5~10편 (메소드 신규성 > 인용수):
   - 제목 / 저자 / 연도 / venue / DOI or arXiv ID
   - 분류: [사회학=방향성] 또는 [공학=실행안]
   - 3~5 문장 요약: [방법] [결과] [한계]
   - L1/L2/L3 매핑 태그
   - 시스템 환원 (어느 노드/링크/코드)
   - [NEW] 태그 (직전 run 대비)
3. 가설 검증 점수 (1~5)
4. 후속 키워드 5개 + 인접 분야 2개

## Meta

- 공학 논문 1편 = 노드 1개 또는 link 1개 또는 코드 PR 1개.
- 사회학 논문만으로는 link 정당화 불가.
- ROADMAP.md 상단 changelog 에 "지난 실행 이후 무엇을 더 할 수 있게
  되었는가" 를 1줄로 기록.
