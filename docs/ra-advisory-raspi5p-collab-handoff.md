# RA 자문 연동 — T3610 → raspi5p 협업 전달 메모

- **작성**: T3610 자문 백엔드 측 (본 repo) / 2026-06-25 (5차)
- **대상**: raspi5p RA 자문 연동 담당
- **목적**: raspi5p 5차 개선을 교차 검증한 결과 + 함께 ra request 구조를 완성할 협업 과제 정리
- **참조**: `docs/ra-advisory-raspi5p-dod-verification.md`, `docs/ra-advisory-raspi5p-review.md`, CLAUDE.md Contract C

---

## 0. 먼저 — raspi5p 5차 개선, T3610이 교차 검증한 결과: 전부 확인됨 ✅

raspi5p가 보고한 개선(OP 권한 제거 · timeout 상향 · 재검증 pass)을 T3610 장비에서 직접 검증했습니다. **전부 사실이고 방향이 좋습니다.**

| raspi5p 보고 | T3610 검증 결과 |
|--------------|-----------------|
| OP `.env` 잔여 제거 (op_env_refs=0) | `/opt/hermes-ra/.env` OP 키워드 **0건** ✅ |
| hermes-api-server OP 코드 없음 | 매칭 11건은 전부 **Contract A `wp_comment` 스키마 파싱** (OP 직접 write/read 코드 아님) ✅ |
| timeout 220 상향 | `/opt/.env` = `ADVISORY_TIMEOUT=220` (코드 기본 180 → env 오버라이드) ✅ |
| 재검증 4case + E2E pass | Honcho 11:16~11:20(KST) ra_us / ra_eu(WP435 comment 6074) / ra_kr(WP1418) / Yellow 차단 + conclusion session 기록 ✅ |

특히 **T3610이 자문자임에도 OP 권한 잔여를 제거한 것**은 경계를 단단히 한 훌륭한 조치입니다.

---

## 1. 함께 닫아야 할 근본 갭 3 (raspi5p 역할)

### 🔴 1.1 [최우선] 69줄 timeout 자동실행 — root cause 수정

- **현 상태**: v6 "WP 본문 생성" 노드 69줄
  ```js
  if (!advisory) return { allowMutation: true, reason: null, contract: 'legacy' };
  ```
- **문제**: timeout 180→220 상향은 parse_or_hermes_failure Yellow의 **빈도를 줄일 뿐**, `advisory==null`(네트워크/GX10 장애·파싱실패)이면 **여전히 `allowMutation:true`로 통과**합니다.
- **요청**: 69줄을 `allowMutation:false`(`reason=advisory_unavailable`) + rejected feedback 경로로 수정.
- **이유**: 의료기기 RA에서 **자문 백엔드 장애 시 자동실행**이 가장 위험. raspi5p 보고의 "timeout 자동실행 금지" 주의사항과 코드가 일치해야 함.

### 🔴 1.2 closed/don WP 게이트 — status 검사 추가

- **현 상태**: v6 `advisoryGate`(68~92줄) + harness `gate()` 가 `wp_candidate` **존재**만 검사, **status 안 봄**.
- **위험**: T3610 자문은 WP 상태를 모름 → 종료 WP에도 `comment_existing_wp` 반환 → raspi 게이트 통과 → **종료 WP에 댓글**.
- **요청**: `comment_existing_wp` 분기에 `wp_candidate.status not in (closed, done)` 검사(`reason=wp_closed_or_done`); harness에 **E4 케이스**(의도적 종료 WP → 차단) 추가.

### 🟡 1.3 live → repo 소스 동기화 (가장 조용하지만 치명적)

- **현 상태**: T3610 백엔드 live(`/opt/hermes-ra/hermes-api-server.py`)와 이 repo 소스(`scripts/hermes-api-server.py`)가 **diff 39줄** 차이.
- raspi5p가 고친 것(`ADVISORY_TIMEOUT`, `ADVISORY_FALLBACK_ACTOR=ra_kr`, conclusion 기록 로직)이 **live에만** 있음.
- **위험**: T3610 재배포(repo → /opt) 시 raspi5p contract 보강이 **전부 유실**.
- **요청**: live 변경분을 `holee9/ra-hermes-multi-agent` 의 `scripts/hermes-api-server.py`로 **PR**. 이 repo가 자문 백엔드의 소스 오브 트루스입니다. live 고치면 반드시 repo로.

---

## 2. T3610이 할 것 (협업 관측)

- 1.1·1.2 수정 후 Honcho `ra-advisory-feedback` 에 `advisory_unavailable` / `wp_closed_or_done` 사유 rejected 가 찍히는지 교차 검증.
- raspi5p harness E4/E5 실행 결과를 T3610 서버 로그(`/v1/ra/advisory/feedback`) + Honcho로 관측·증빙.

---

## 3. 완성 조건 (#83 close)

- [ ] 1.1 69줄 root cause 수정 (`!advisory → false`)
- [ ] 1.2 closed/don 게이트 + harness E4
- [ ] 1.3 repo-live diff 0 (PR 동기화)
- [ ] harness E5(timeout → rejected) 증빙 → DoD-3
- [ ] DoD 7종 전부 (1,2,5,6,7 이미 ✅; 3·4가 위 항목)
- [ ] 테스트 데이터 정리: WP 435(댓글 6034/6036/6064/6066/6073/6074) · WP 1414~1418

---

## 4. 경계 재확인 (불변)

- **T3610 = 자문자** (판단·처리안 JSON만 반환). OpenProject write **영구 금지**. ← raspi5p OP `.env` 제거로 강화한 것 훌륭.
- **raspi5p = 실행주체** (게이트 · OP mutation · feedback 회신).
- **소스 창구**: `holee9/ra-hermes-multi-agent` 이 repo의 PR. 백엔드 live를 고치면 반드시 repo로 역동기화.
- 두 성장축(금일 daily-growth written=9 = KB 학습 / raspi5p e2e = 실전 자문)은 같은 완성의 양 날개 — 동시 진행 환영.

---

## 5. 한 줄 요약

raspi5p 5차 개선은 정확하고 방향도 좋음. **(1) 69줄 root cause, (2) closed/don 게이트, (3) live→repo PR 동기화** 이 세 개를 분담해서 닫으면 ra request 구조 완성 + #83 close.
