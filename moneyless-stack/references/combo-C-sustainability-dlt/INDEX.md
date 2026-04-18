# Combo C — L2 × L3 : Sustainability Constraints in DLT Governance

## Run meta
- run_date: 2026-04-18
- search_window: 2024-04 .. 2026-04
- prior_run: none
- tools used: HF paper_search, WebSearch

## Executive Summary
DAO/스마트컨트랙트 연구는 on-chain governance KPI·토큰 집중도·
참여율·의결권 위임 등 "거버넌스 측정" 에서는 성숙하지만, **생태·
열역학적 hard constraint** 를 합의 자체에 주입한 사례는 거의 없다.
"ReFi (Regenerative Finance)" 는 정책 레이어에서는 존재하나,
verification layer 는 여전히 oracle/off-chain attestation 에 의존한다.
ESG 보고에 대한 greenwashing 검출 (EmeraldMind) 은 반대 방향 —
문서 검증이지 합의 제약은 아님. 따라서 측정 불확실성 → 의결권 가중치
매핑은 거의 공백으로 남아 있으며, 이것이 L3 × UQ 의 핵심 기회이다.

## Papers

### 1. Evaluating DAO Sustainability and Longevity Through On-Chain Governance Metrics
- id: arXiv:2504.11341 · 2025
- 분류: [사회학=방향성] (공학 컴포넌트 포함)
- 방법: governance efficiency / financial robustness / decentralization /
  community engagement 4축 KPI
- 결과: 참여 집중도 낮으면 장기 지속 안 됨
- 한계: 환경/생태 제약은 포함되지 않음
- 매핑: L3 (거버넌스 건강지표)
- 환원: ROADMAP 의 L3 health monitoring 방향성
- [NEW]

### 2. Verifiable Off-Chain Governance
- id: arXiv:2512.23618 · 2025
- 분류: [공학=실행안]
- 방법: on-chain 계산 한계를 off-chain 검증으로 보완 (16만+ 홀더 규모
  에서 on-chain exact 계산 비현실성 명시)
- 결과: 예산 제약 내 simplified model + verifiable 재증명
- 한계: 물리 센서와 무관
- 매핑: L3 (합의 내부 계산 비용 경계)
- 환원: L3 consensus 를 단순화하고 heavy 계산을 L1/bridge 에서
  검증가능하게 위임하는 패턴 정당화
- [NEW]

### 3. Decentralized Governance of AI Agents (ETHOS)
- id: arXiv:2412.17114 · 2024–2025
- 분류: [사회학=방향성]
- 방법: DAO + smart contract 로 AI agent 위험 분류 · 자동 compliance
- 결과: 동적 risk classification 프레임
- 한계: 생태 제약 미포함
- 매핑: L3 (규칙 enforcement 프레임)
- 환원: L3 규칙 집행 아키텍처의 구조적 참고
- [NEW]

### 4. Decentralized RAG with Source Reliabilities Secured on Blockchain
- id: arXiv:2511.07577 · 2025
- 분류: [공학=실행안]
- 방법: 블록체인 스마트컨트랙트에 source reliability score 저장 +
  batched update, LLM retrieval 에 반영
- 결과: 중앙화 대비 성능/비용 경쟁력
- 한계: 데이터 source 에 한정, 물리 측정 아님
- 매핑: L3 (reliability-weighted commit pattern)
- 환원: L3 의 UQ-weighted voting 에 선행하는 "출처 신뢰도 가중" 패턴
- [NEW]

### 5. Shielded Controller Units for RL with Operational Constraints
  (Remote Microgrids)
- id: arXiv:2512.01046 · 2025
- 분류: [공학=실행안]
- 방법: shielding 을 통해 hard constraint satisfaction 을 보장한 RL
- 결과: 연료 소비 감소, 배터리 열화 유지
- 한계: 단일 마이크로그리드, 분산 합의 미포함
- 매핑: L2 × L3 (hard constraint 를 decision 에 주입)
- 환원: L3 proposal 에 SCU 레이어 도입 근거
- [NEW]

### 6. EmeraldMind — Greenwashing Detection (KG + RAG)
- id: arXiv:2512.11506 · 2025
- 분류: [공학=실행안] (검증 도구로 사용 가능)
- 방법: 도메인 지식그래프 + RAG 로 ESG 보고 사실 검증
- 결과: 증거기반 판정
- 한계: 문서 중심, 실측 연결 없음
- 매핑: 보조 (ReFi 정직성 감사)
- 환원: 향후 ReFi claim 의 off-chain attest 로 검토
- [NEW]

### 7. CrowdMine — Proof of Crowdsourcing / Useful Work
- id: arXiv:2211.06669 · 2022–2023 (window 경계 밖이지만 baseline)
- 분류: [공학=실행안]
- 방법: 계산 자원을 유용한 task 로 돌리는 합의
- 결과: 에너지 효율 + 51% 공격 내성
- 한계: 2022년 논문
- 매핑: L3 PoUW baseline
- 환원: 비교 기준

### 8. Agent Economy — Blockchain Foundation for Autonomous AI Agents
- id: arXiv:2602.14219 · 2026
- 분류: [사회학=방향성] + 실행안
- 방법: W3C DID, DePIN, 평판자본, Agentic DAOs 통합 프레임
- 결과: M2M micropayments 가능성 정량화
- 한계: 여전히 토큰경제 기반 (본 스택은 화폐 비매개 지향이라 부분적 반례)
- 매핑: L3 반례 / 경계 조건
- 환원: synthesis.md 의 "가설 약화 증거" 섹션 수록
- [NEW]

## Hypothesis score
- 지속가능성 hard constraint 가 합의에 내장된 사례: **2/5**
  (대부분 off-chain oracle 의존; 진정한 physical consensus 희소)

## Follow-up keywords
1. "exergy-denominated voting"
2. "measurement uncertainty voting weight"
3. "ecological shielding RL"
4. "verifiable claim carbon"
5. "sustainability hard constraint smart contract"

## Adjacent unexplored fields
- Commons-based peer production formal models
- Bioregional DLT (지역 자원경계와 합의의 매칭)
