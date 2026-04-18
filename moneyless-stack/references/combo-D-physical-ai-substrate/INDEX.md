# Combo D — L1 × L3 (Hardware Layer) : Physical AI as Consensus Substrate

## Run meta
- run_date: 2026-04-18
- search_window: 2024-04 .. 2026-04
- prior_run: none
- tools used: HF paper_search, WebSearch

## Executive Summary
뉴로모픽 SNN + on-chip learning 은 엣지에서 저전력/저지연을 확립했고,
TPM 기반 원격 증명 (TPM 2.0 + Linux IMA + Keylime) 은 컨테이너 런타임
무결성을 성숙 단계까지 끌어올렸다. zk-ML 검증 (DSperse, Equivariant
Encryption, TCME) 은 분산 추론의 신뢰 근거를 제공한다. 흥미로운
극단 사례로는 Bitcoin 채굴 ASIC 을 reservoir computing 물리 기질로
재활용한 연구 (Speaking to Silicon, Toward Thermodynamic Reservoir
Computing) 가 있으며, 이는 "기존 비합리적 에너지 싱크를 유용한 합의
기질로 회수" 라는 본 스택 방향과 직접 공명한다. 이 combo 는 "물리적
으로 위변조 불가능한 substrate 가 합의 비용을 낮춘다" 라는 가설에
가장 높은 엔지니어링 근거를 제공한다.

## Papers

### 1. TPM-Based Continuous Remote Attestation for 5G VNFs on Kubernetes
- id: arXiv:2510.03219 · 2025
- 분류: [공학=실행안]
- 방법: TPM 2.0 + Linux IMA + Keylime 기반 지속적 원격 증명,
  k3s 클러스터 배포
- 결과: 5G core VNF 런타임 무결성 보장
- 한계: 하드웨어 의존 (TPM 없는 노드 불가)
- 매핑: L3 substrate
- 환원: `nodes/physical-bridge/` 의 미래 attestation adapter 참조
- [NEW]

### 2. Speaking to Silicon — Neural Communication with Bitcoin Mining ASICs
- id: arXiv:2601.12032 · 2026
- 분류: [공학=실행안, radical]
- 방법: ASIC 을 reservoir 로 사용, Thermodynamic Probability Filter,
  Virtual Block Manager, Lean4 공식 증명, PUF, 계층적 수체계
- 결과: ASIC 하드웨어 보편성 + 에너지 감소
- 한계: 개념 증명 수준, 실 배포 부재
- 매핑: L1 × L3 (물리 substrate 를 합의 기질로 재활용)
- 환원: synthesis.md 의 "기존 인프라 회수" 가설 근거
- [NEW]

### 3. Toward Thermodynamic Reservoir Computing (SHA-256 ASIC)
- id: arXiv:2601.01916 · 2026
- 분류: [공학=실행안]
- 방법: SHA-256 hashing pipeline 내 thermal noise 를 reservoir 로,
  edge-of-stability 동작
- 결과: 뉴로모픽 응용 가능성 실증
- 한계: 위와 유사
- 매핑: L1 × L3
- 환원: 동일
- [NEW]

### 4. DSperse — Targeted Verification in zk-ML
- id: arXiv:2508.06972 · 2025
- 분류: [공학=실행안]
- 방법: 모델 subcomputation 만 zk 증명 (sliced inference)
- 결과: 비용 절감, 감사/복제 가능
- 한계: 아직 vision/small models 중심
- 매핑: L3 (verification layer)
- 환원: L3 consensus 가 채택할 경량 verification 인터페이스
- [NEW]

### 5. Towards Secure and Private AI — Decentralized Inference Framework
- id: arXiv:2407.19401 · 2024
- 분류: [공학=실행안]
- 방법: ZK proof + consensus check + split learning + TEE
- 결과: 다중 레이어 보안 + 신뢰 + 공정성
- 한계: 여전히 소프트웨어 레벨
- 매핑: L3
- 환원: L3 multi-mechanism verification 설계 청사진
- [NEW]

### 6. NeuEdge — Adaptive SNN for Edge AI (hardware-aware)
- id: arXiv:2602.02439 · 2026
- 분류: [공학=실행안]
- 방법: adaptive threshold SNN + hardware-aware training
- 결과: 뉴로모픽 엣지에서 높은 정확도 / 저전력
- 한계: 일반 deployment 플랫폼 제한
- 매핑: L1 (edge compute), 추후 L1↔L3
- 환원: 엣지 compute substrate 후보
- [NEW]

### 7. Edge Processing of SNNs with On-Chip Learning
- id: arXiv:2504.00957 · 2025
- 분류: [공학=실행안]
- 방법: 상용 뉴로모픽 프로세서에 SNN 매핑 + on-chip learning
- 결과: 저지연, 저전력
- 한계: 산업 파이프라인 통합은 별도
- 매핑: L1
- 환원: L1 미래 하드웨어 사양 후보
- [NEW]

### 8. EconAgentic in DePIN Markets
- id: arXiv:2508.21368 · 2025
- 분류: [사회학=방향성]
- 방법: LLM 에이전트로 DePIN 공유경제 시뮬레이션
- 결과: DePIN 시장 > $10B cap, 토큰 인센티브의 한계 식별
- 한계: 여전히 토큰경제 가정
- 매핑: L3 경계 조건
- 환원: 화폐 비매개 가설의 반례로 synthesis 에 수록
- [NEW]

## Hypothesis score
- 물리 substrate 가 합의비용을 낮출 수 있다는 가설: **4/5**
  (radical ASIC-reuse 가 feasibility 를 +1 끌어올렸지만 실증은 아직)

## Follow-up keywords
1. "sensor-rooted attestation"
2. "PUF-based consensus weight"
3. "thermodynamic reservoir DLT"
4. "neuromorphic verifier edge"
5. "oracle-free physical commit"

## Adjacent unexplored fields
- Photonic logic for consensus (nanophotonic)
- Mechanical/analog hash as light-weight attestation
