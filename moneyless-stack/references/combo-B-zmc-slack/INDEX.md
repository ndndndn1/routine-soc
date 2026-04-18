# Combo B — L1 × L2 : Zero-Marginal Cost + Recoverable Slack

## Run meta
- run_date: 2026-04-18
- search_window: 2024-04 .. 2026-04
- prior_run: none
- tools used: HF paper_search, WebSearch

## Executive Summary
"한계비용 0" 담론은 서지적으로는 Industry 4.0 → 6.0 프레임 안에서
순환경제/자원회복으로 이어지고, 공학적으로는 self-healing
(LLM agent tool routing, robotic recovery) 과 RL 기반 순환자원 제어
환경(CiRL)으로 구체화된다. 그러나 "여유(slack)를 비필수 욕구에
회복가능 범위 내에서 할당" 을 정량화한 TEA(Techno-Economic Analysis)
는 아직 빈약하고, 대부분 서술/질적 수준에 머물러 있다. 본 combo의
공백은 **엔트로피/exergy 여유를 보존 제약으로 수식화한 할당기**의
부재이며, 이는 L2 노드의 핵심 알고리즘 과제이다.

## Papers

### 1. CiRL — Open-Source RL Environments for Circular Economy and Net Zero
- id: arXiv:2505.21536 · 2025
- 분류: [공학=실행안]
- 방법: 고체/유체 물질 순환 제어를 위한 deep RL benchmark suite
- 결과: 재사용 가능한 환경 + baseline 제공
- 한계: 경제주체 간 상호작용·화폐 비매개 가정은 미포함
- 매핑: L2 (자원순환 시뮬레이션)
- 환원: `nodes/l2-entropy-buffer/` 의 allocate/produce 모델을
  향후 CiRL env 로 대체할 때의 참조 구현
- [NEW]

### 2. Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents
- id: arXiv:2603.01548 · 2026
- 분류: [공학=실행안]
- 방법: parallel health monitor + cost-weighted tool graph 에서
  Dijkstra shortest-path 로 deterministic routing, silent failure
  자동 복구
- 결과: LLM 호출 의존 감소 + 높은 정확성
- 한계: 물리 장비가 아닌 소프트웨어 tool 레이어 한정
- 매핑: L1 (fault-tolerant control pattern) → L2 (자가 치유 scheduling)
- 환원: L1 노드의 `self_healing_router` 모듈 설계 패턴
- [NEW]

### 3. Adaptable Recovery Behaviors in Robotics (BTMG)
- id: arXiv:2404.06129 · 2024
- 분류: [공학=실행안]
- 방법: Behavior Trees + Motion Generators 에 RL 로 recovery 정책 학습
- 결과: dual-arm KUKA peg-in-hole 복구 성공률 향상
- 한계: factory-scale 일반화 미검증
- 매핑: L1 (물리 복구 절차)
- 환원: L1 의 "고장 시 자동 복구" 방향성 정당화
- [NEW]

### 4. Transforming Manufacturing from Industry 4.0 to Industry 6.0
- ref: ISGM-79 / AIS Academy preprint · 2025
- 분류: [사회학=방향성]
- 방법: consciousness / circularity / resilience 세 기둥 개념적 통합
- 결과: 제조가 인간번영·생태회복의 촉매라는 프레임
- 한계: 개념적. 정량 모델 없음
- 매핑: L1+L2 방향성
- 환원: ROADMAP 의 "비필수 욕구 흡수 = slack 회수" 문구 근거
- [NEW]

### 5. Jevons' Paradox in AI's Environmental Debate
- id: arXiv:2501.16548 · 2025
- 분류: [사회학=방향성]
- 방법: 효율성 향상이 절대 소비 증가로 이어지는 rebound 리뷰
- 결과: 한계비용 0 도 총량 경계 없이는 붕괴
- 한계: AI 에너지에 한정
- 매핑: L2 방향성 (reserve 유지가 왜 필수인가)
- 환원: L2 allocate 에서 "reserve floor" 10% 를 유지하는 선택 근거
- [NEW]

### 6. COKE — Causal Discovery in Manufacturing with High Missingness
- id: arXiv:2407.12254 · 2024
- 분류: [공학=실행안]
- 방법: 전문가 지식 + 시간순서 기반 인과 그래프, 결측 보간 없이
- 결과: F1 향상
- 한계: static dataset
- 매핑: L1/L2 (생산 변수 인과 관계)
- 환원: L2 이상 제어의 causal prior 준비
- [NEW]

### 7. Optimal Decision Making in Robotic Assembly (failure restart)
- id: arXiv:2301.10846 · 2023
- 분류: [공학=실행안] (window 경계 밖이지만 adjacent 비교용)
- 방법: Markov jump 기반 failure prediction 으로 preemptive restart
- 결과: task completion time 단축
- 한계: 2023 → [NEW] 아님
- 매핑: L1 (self-healing)
- 환원: baseline 비교

### 8. CiRL 보조 — RL + Resource Optimization surveys
- 일반 서베이 레퍼런스 (Huang 2025 BSE, Sciepublish 2025) —
  주로 [사회학=방향성], 참고용 INDEX 링크만 유지

## Hypothesis score
- ZMC/slack 기술적 타당성: **3/5**
  (정량 TEA + 엔트로피 보존 제약 기반 allocator 의 실증이 부족)

## Follow-up keywords
1. "exergy accounting allocator"
2. "recoverable slack budget"
3. "entropy-constrained scheduling"
4. "non-essential demand satisfaction index"
5. "planetary boundary manufacturing RL"

## Adjacent unexplored fields
- Thermoeconomics → 분산 시스템 가치척도
- Degrowth operations research
