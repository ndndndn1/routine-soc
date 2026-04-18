# ROADMAP — moneyless-stack

## Changelog
- 2026-04-18 (run 1): 빈 리포에서 출발 → 4 combo INDEX, 3+1 노드 격리
  스켈레톤, default-deny compose 구성. 매 노드는 독립 loop 로 자체 판단
  가능. 링크는 전부 `proposed` 상태.

## Directional axes (사회학 기반)

### A1. "측정값 직결" 을 행위 단위로 만들기
- 근거: combo-A §7 (Digital Twin AI survey), combo-C §1 (DAO sustainability
  KPIs), combo-D §8 (EconAgentic in DePIN)
- 방향: 모든 합의 입력은 검증 가능한 물리 측정값으로 환원되어야 한다.
  off-chain oracle 는 수용하지 않는다.

### A2. 잉여 자원은 재생 가능 범위 내에서만 비필수 욕구를 흡수한다
- 근거: combo-B §1 (CiRL), §4 (Industry 6.0), §5 (Jevons rebound)
- 방향: L2 는 absolute reserve floor 를 가진다. 최적화는 reserve 아래를
  건드리지 않는 제약 하에서만 이루어진다.

### A3. 토큰경제는 필요조건이 아니다
- 근거: combo-D §8, combo-C §8 (경계조건으로 수록)
- 방향: 인센티브 설계는 token/price 이전에 measurement attestation 과
  reputation-of-sensor 층에서 구성된다.

## Decomposition into engineering work items

| ID   | Item                                                      | Layer / Link | Backed by | Status |
| ---- | --------------------------------------------------------- | ------------ | --------- | ------ |
| W-01 | L1 노드 최소 구현: PHM tick + aleatoric/epistemic sigma 분리 출력 | L1 | combo-A §1, §3 | done (v0) |
| W-02 | L2 노드 최소 구현: reserve-floor 보호된 slack 할당기               | L2 | combo-B §1, §5 | done (v0) |
| W-03 | L3 노드 최소 구현: 단일노드 append-only commit log (분산 아님)     | L3 | combo-C §2 | done (v0) |
| W-04 | physical-bridge 스켈레톤 + 기본 disabled                       | bridge | default deny | done (v0) |
| W-05 | PHYSICAL_LINKS.md 등록부 형식 확정                             | links | 정책 | done |
| W-06 | L1→L3 link 제안 (status=proposed) + UQ-weighted commit 인터페이스 | link | combo-A §2, §3, §6 | proposed |
| W-07 | L2↔L3 link 제안: reserve 경고를 L3 의 hard-constraint 로       | link | combo-C §5 | proposed |
| W-08 | UQ-weighted voting 시뮬레이션 (가상 다중 L1 노드)                 | L3 | combo-A §1,§3 + combo-D §4 | backlog |
| W-09 | TPM attestation adapter 스텁 in `physical-bridge/`         | bridge | combo-D §1 | backlog |
| W-10 | CiRL 환경을 L2 뒷단으로 접합하는 어댑터                             | L2 | combo-B §1 | backlog |
| W-11 | greenwashing/ESG claim 검증기 off-ramp (optional)           | audit | combo-C §6 | backlog |
| W-12 | Bitcoin ASIC reservoir 가설 실증 feasibility note              | synthesis | combo-D §2,§3 | backlog |

## Next run entry conditions
- run 2 의 첫 과제: W-06 의 engineering ref 를 최소 1편 더 추가하고
  (예: UQ-weighted Byzantine agreement 직접 검색) PHYSICAL_LINKS 의 해당
  항목을 `proposed` → `validated-design` 으로 격상할 근거 확인.
- run 2 에서 W-09 스텁이 구현되면 처음으로 bridge 가 "boot 가능" 상태가 됨.

## Hard rules
- 사회학 논문만으로는 어떤 link 도 enable 되지 않는다.
- link enable 시에는 반드시 `PHYSICAL_LINKS.md` 항목과 compose network
  업데이트가 **같은 commit** 에 들어가야 한다.
