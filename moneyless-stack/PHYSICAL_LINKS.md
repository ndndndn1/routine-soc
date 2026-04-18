# PHYSICAL_LINKS

통신 허용 근거 등록부. 기본값: 모든 inter-node 통신은 금지.
링크 상태: `proposed` → `validated-design` → `enabled`.

현재 시점 run 1 기준으로 **enabled 링크는 없음**.

---

## link: l1-reliability ↔ l3-consensus
- physical_basis: **미확정**. 후보 1) 동일 industrial edge 기기 내
  on-board I2C/SPI 버스로 PHM 칩셋과 consensus MCU 가 연결되는 구성.
  후보 2) 동일 k3s 노드 내부 루프백 + TPM attested socket.
- engineering_refs:
  - `references/combo-A-physics-consensus/INDEX.md` §2 (2506.00499,
    Federated RUL, decentralized validation protocol)
  - `references/combo-A-physics-consensus/INDEX.md` §3 (2511.21208,
    I-GLIDE, aleatoric/epistemic UQ 분리)
  - `references/combo-A-physics-consensus/INDEX.md` §6 (2502.02692,
    Intelligent Sensing-to-Action)
  - `references/combo-D-physical-ai-substrate/INDEX.md` §1 (2510.03219,
    TPM 2.0 + Keylime continuous attestation)
- compose_network: (none yet; 지정 예정 net_phm_consensus)
- status: **proposed**
- reason_not_enabled: 물리 basis 가 아직 "동일 기기 vs 동일 클러스터"
  수준에서 택일되지 않았다. 엔지니어링 근거는 있으나 하나의 구체 경로로
  합의되지 않은 상태.
- last_verified: 2026-04-18

---

## link: l2-entropy-buffer ↔ l3-consensus
- physical_basis: **미확정**. 후보: L2 가 생산하는 reserve-level 값이
  L3 의 proposal constraint 로 주입되는 내부 링크.
- engineering_refs:
  - `references/combo-C-sustainability-dlt/INDEX.md` §5 (2512.01046,
    Shielded Controller Units for RL — hard-constraint enforcement)
  - `references/combo-C-sustainability-dlt/INDEX.md` §2 (2512.23618,
    Verifiable Off-Chain Governance — 계산 경계)
- compose_network: (none yet)
- status: **proposed**
- reason_not_enabled: SCU 논문은 단일 RL 에이전트 대상. 분산 shielding
  의 엔지니어링 확증이 부족.
- last_verified: 2026-04-18

---

## link: l1-reliability ↔ l2-entropy-buffer
- physical_basis: **미확정**. PHM 기반 health 하락을 L2 reserve floor
  상승 신호로 연결하는 내부 링크.
- engineering_refs:
  - `references/combo-B-zmc-slack/INDEX.md` §2 (2603.01548, self-healing
    tool routing — control plane pattern) — 소프트웨어 레벨, 물리 확증
    약함
  - `references/combo-B-zmc-slack/INDEX.md` §6 (COKE — manufacturing
    causal discovery) — 같은 제조 변수 공간 가정
- compose_network: (none yet)
- status: **proposed (weak backing)**
- reason_not_enabled: 공학 근거가 "소프트웨어 패턴" 수준. 물리 basis
  추가 근거 필요.
- last_verified: 2026-04-18

---

## link: physical-bridge ↔ *
- physical_basis: 어댑터 자체는 어떤 link 도 열지 않는다. 외부 세계
  (센서 fab, 실물 하드웨어) 와 위 링크들이 `enabled` 된 이후 endpoint
  역할을 한다.
- engineering_refs: n/a (shell adapter)
- compose_network: (없음; profile-gated)
- status: **disabled (structural)**
- last_verified: 2026-04-18

---

## 정책
- 위 중 하나라도 `enabled` 로 바뀌려면:
  1. 물리 basis 가 하나로 좁혀져야 한다.
  2. 공학 논문 레퍼런스가 최소 1편 더 보강되어야 한다.
  3. `docker-compose.yml` 에서 명시적 network 를 정의하고 양 노드가 join 한다.
  4. 해당 link 를 직접 구현한 코드가 각 노드에 merge 된다.
- 위 4개 모두 동일 commit 에 들어가야 한다.
