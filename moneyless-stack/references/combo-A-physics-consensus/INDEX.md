# Combo A — L1 × L3 : Physics-grounded Maintenance Consensus

## Run meta
- run_date: 2026-04-18
- search_window: 2024-04 .. 2026-04
- prior_run: none (first run)
- tools used: HF paper_search, arXiv via WebSearch

## Executive Summary
최근 2년간 PHM(Prognostics and Health Management) 분야는 확률적
Digital Twin + 물리정보 베이지안 학습으로 UQ(불확실성 정량화) 내장
예측이 표준이 되고 있다. 합의(consensus) 측면에서는 연합학습이
분산 RUL 예측을 실현하며 중앙화 없이 검증 가능한 prognostics 모델을
생산한다. 그러나 PHM 출력 → 분산 원장 commit 경로는 대부분
"oracle 가정" 으로 처리되고, sensor-to-ledger 직결 구조는
아직 공백이다. 본 combo의 핵심 gap 은 UQ-weighted voting 을
실제 하드웨어 경로로 구현한 사례이다. 따라서 L1→L3 링크는
UQ 가중치를 입력으로 받는 합의 인터페이스 설계 문제로 환원된다.

## Papers

### 1. Bayesian Physics-Informed Neural Networks for Reliable Transformer Prognostics
- id: arXiv:2509.15933 · 2025
- 분류: [공학=실행안]
- 방법: B-PINN 프레임워크로 변압기 prognostics 에 확률적 RUL 예측
- 결과: uncertainty-aware 예측이 robust maintenance decision 을 지원
- 한계: 전력자산 1개 도메인 한정, 센서 → 원장 파이프라인 미포함
- 매핑: L1 (PHM 코어). 추후 L3 voting weight 로 사용
- 환원: `nodes/l1-reliability/` PHM 시뮬레이터의 UQ 출력 포맷 정당화
- [NEW]

### 2. Federated learning framework for collaborative RUL prognostics (aircraft engine)
- id: arXiv:2506.00499 · 2025
- 분류: [공학=실행안]
- 방법: 6개 항공사가 데이터 공유 없이 RUL 모델을 공동 학습,
  검증도 분산 프로토콜로 수행
- 결과: 5/6 참여자에서 단독 학습 대비 정확도 향상
- 한계: 검증은 여전히 off-chain; 물리 센서 ↔ 원장 직결 없음
- 매핑: L1 × L3 (분산 검증 프로토콜)
- 환원: `PHYSICAL_LINKS.md` 의 L1↔L3 link 후보 근거 논문
- [NEW]

### 3. I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation
- id: arXiv:2511.21208 · 2025
- 분류: [공학=실행안]
- 방법: RaPP 기반 aleatoric/epistemic UQ 분리, MC dropout,
  probabilistic latent space, indicator group decomposition
- 결과: RUL 정확도 + 해석성 동시 개선, 다중 센서 이상 탐지 강화
- 한계: 시뮬레이션 중심, field deployment 데이터 부족
- 매핑: L1 (UQ 분해) → L3 (가중 투표용 aleatoric/epistemic 구분)
- 환원: `nodes/l1-reliability/phm_tick` 의 sigma 출력을
  aleatoric/epistemic 두 값으로 확장할 근거
- [NEW]

### 4. Probabilistic Digital Twin via Latent Force Modeling + Bayesian NN
- id: arXiv:2511.22133 · 2025
- 분류: [공학=실행안]
- 방법: GPLFM + BNN 으로 모델 미지정 구조동역학계에서 latent
  입력력 추정, Kalman filter 기반 uncertainty-aware inference
- 결과: Bouc-Wen hysteretic system, Silverbox 데이터셋에서 robust
- 한계: 실시간성/엣지 배치 미검증
- 매핑: L1 (probabilistic digital twin 코어)
- 환원: `nodes/l1-reliability/` 다음 버전의 상태추정 엔진 blueprint
- [NEW]

### 5. 6G-Enabled Digital Twin Framework for Real-Time CPS (Industrial Bearing Fault)
- id: arXiv:2510.03807 · 2025
- 분류: [공학=실행안]
- 방법: THz 통신 + IRS + edge AI 로 bearing fault detection
- 결과: 초저지연, 높은 F1
- 한계: 통신 자체는 외부 인프라 (자급자족 원칙과 상충)
- 매핑: L1 (edge PHM) · 통신층은 PHYSICAL_LINKS 에 부적합
- 환원: edge PHM feasibility 레퍼런스로만 사용
- [NEW]

### 6. Intelligent Sensing-to-Action for Robust Autonomy at the Edge
- id: arXiv:2502.02692 · 2025
- 분류: [공학=실행안]
- 방법: 센싱-액션 루프 내 proactive/context-aware 적응, neuromorphic
  + multi-agent 계층적 제어
- 결과: 동적 환경 엣지 자율성 신뢰성 향상
- 한계: 구체 프로토콜은 architecture-level
- 매핑: L1 ↔ L3 (in-sensor compute → edge orchestration)
- 환원: 동일 PCB/센서버스 상에서 L1→L3 물리 링크의 개념적 근거
- [NEW]

### 7. Digital Twin AI — Opportunities and Challenges (survey)
- id: arXiv:2601.01321 · 2026
- 분류: [사회학=방향성] + [공학=실행안 hybrid survey]
- 방법: modeling → mirroring → intervention → autonomous mgmt 4단계
- 결과: 물리정보 AI + 생성 AI + foundation 모델 통합 lifecycle
- 한계: 서베이 (구현 제공 없음)
- 매핑: L1 전 레이어 방향성
- 환원: ROADMAP 의 L1 장기 방향성 bullet
- [NEW]

### 8. Survey of Predictive Maintenance Methods (classification/regression)
- id: arXiv:2506.20090 · 2025
- 분류: [공학=실행안 survey]
- 방법: PdM 방법론 분류와 데이터 불균형/고차원 이슈 정리
- 결과: hybrid + AI-enabled 접근이 지배적 트렌드
- 한계: 분산 합의와의 연결은 다루지 않음
- 매핑: L1 전반
- 환원: L1 구현 시 baseline 선택 근거
- [NEW]

## Hypothesis score
- 화폐 비매개 시스템 L1/L3 부분에 대한 기술적 타당성: **4/5**
  (UQ-weighted voting 의 하드웨어 직결 사례 부재가 −1)

## Follow-up keywords
1. "sensor-attested ledger commit"
2. "UQ-weighted Byzantine agreement"
3. "prognostics as oracle-free input"
4. "aleatoric epistemic voting weight"
5. "edge PHM with on-device signing"

## Adjacent unexplored fields
- Mechanical TRNG (reliability sensor noise as entropy source)
- Post-quantum signing in edge MCUs (for sensor-level attestation)
