# synthesis.md — 4 combo 교차 인사이트 (run 1)

## 1. 교차 인사이트

### I-1. UQ 는 모든 레이어의 공통 통화이다
combo-A 의 aleatoric/epistemic 분해 (I-GLIDE, B-PINN) 와 combo-C 의
reliability-weighted RAG (2511.07577), combo-D 의 sliced zk-ML
(DSperse) 는 서로 독립적으로 "확률 구간을 의사결정의 가중치로"
사용한다. 이는 화폐 비매개 스택이 채택해야 할 공통 인터페이스가
price/token 이 아니라 **measurement uncertainty** 임을 시사한다.

### I-2. 기존 에너지 싱크의 재활용 가능성
combo-D §2 §3 의 Bitcoin ASIC reservoir computing 은, 화폐경제가 만든
거대한 에너지 싱크를 합의 기질로 재활용할 수 있다는 radical 가설을
제시한다. 반대로 combo-C §8 과 combo-D §8 은 여전히 토큰 인센티브
기반 DePIN 이 지배적 패러다임임을 보여준다. 둘의 공존은 "가설 약화
증거 = 강화 증거" 라는 이중 신호.

### I-3. default-deny 는 비용이 아니라 기능이다
combo-C §2 (Verifiable Off-Chain Governance) 가 지적한 on-chain 계산
한계 (16만+ 홀더 에서 exact resolution 비현실적) 는, 기본 격리된
노드 → 물리적으로 근거 있는 단일 link 만 선택 활성화 라는 본 스택의
정책과 동일 결론에 도달한다.

### I-4. slack 의 정량화가 가장 약하다
combo-B 는 순환/회복의 질적 비전은 풍부하나 정량 TEA (엔트로피/exergy
보존 제약) 가 부재. 이는 현 스택의 L2 가 가장 약한 레이어라는 증거.

---

## 2. 화폐 비매개 시스템의 현재 기술적 gap 5가지

1. **Sensor-to-ledger 직결 경로의 공백**: UQ 출력이 합의 weight 로
   물리적으로 전달되는 HW/SW 공동 구현이 publication 수준에서 희소.
2. **분산 shielding 부재**: SCU (2512.01046) 는 단일 RL 에이전트.
   다수 노드 간 hard constraint 공동 enforcement 는 아직.
3. **exergy/엔트로피 denominated 가치척도의 실측 부재**: 이론은 많으나
   실제 원장에 기록된 사례가 없음.
4. **PUF 기반 합의 가중치**: PUF 는 인증에 쓰이지만, "센서의 물리
   고유성 → voting weight" 로 환원된 프로토콜이 없음.
5. **비필수 욕구 지표**: REA (Recreational Entropy Allocation) 를
   정량화할 공인 지표가 없음. 현 L2 의 `request` 는 난수 샘플로
   대체되어 있음.

---

## 3. 5년 내 실증 가능한 minimal viable system 스케치

- 단일 산업 edge 클러스터 (예: 소규모 CNC + HVAC + 태양광 + 배터리).
- L1: 각 장비에 B-PINN 또는 GPLFM + BNN 기반 on-device PHM, TPM 서명.
- L2: 전체 에너지/자원 예산에서 "회복가능 slack" 을 실시간 측정,
  reserve floor 위에서만 비필수 작업 (재료 recycle run, 학습 실험)
  에 할당.
- L3: 3~5개 edge 노드가 sliced zk-proof + aleatoric/epistemic 가중으로
  "다음 작업 순위" 를 committee agreement.
- 화폐 교환은 없음. 외부 세계와의 접점은 물리적 원자재 입·출고에만.

스케일: 한 공장 한 동. 관찰 기간 12~24개월.

---

## 4. PhD 연구주제 후보 3안

### T-1. UQ-weighted Byzantine agreement for physical sensors (low risk, high feasibility)
- combo-A × combo-D 교집합.
- 컨트리뷰션: aleatoric/epistemic 분해를 가중치로 쓰는 BFT variant
  + attestation-pinned sensor identity.
- 위험: 기존 BFT 문헌이 두꺼워 novelty 확보가 어려움.

### T-2. Exergy-denominated smart contract for local commons (medium risk)
- combo-C × combo-B 교집합.
- 컨트리뷰션: 스마트컨트랙트 state variable 자체가 exergy 단위. 제출
  되는 claim 은 exergy balance 를 깨뜨리면 reject.
- 위험: 실측 exergy 계측 인프라 필요 (hardware-heavy).

### T-3. Retired-ASIC reservoir as a common compute substrate (high risk)
- combo-D 중심 + combo-B 의 "기존 싱크 회수" 비전.
- 컨트리뷰션: 폐기된 mining ASIC 을 reservoir computing 으로 재활용
  하여 합의 비용 낮추기. PUF 기반 ID + 열적 안정성 분석.
- 위험: 수명·노이즈 모델 불확실성이 큼.

---

## 5. 가설 약화 증거 (기록 원칙)

- combo-C §8 (Agent Economy, 2602.14219) 과 combo-D §8 (EconAgentic in
  DePIN) 은 여전히 토큰·가격 매개 경제가 지배적 설계임을 보여준다.
  이는 본 스택 가설 "화폐 비매개 가능" 의 강한 반례이며, 꾸준히 모니터
  링해야 한다. 관찰 지표: 대체 측정 기반 인센티브 연구 건수 / 토큰
  기반 인센티브 연구 건수 비율.
