# RA 자문 연동 — raspi5p "1차 구현 완료" 보고 교차 검토의견서 (#83)

- **대상**: raspi5p 보고 "RA 자문 연동 1차 구현 완료"
- **검토자**: T3610 자문 백엔드 측 (본 repo) / 2026-06-24
- **검토 방법**: raspi5p SSH 접속(`ssh raspi5p`) → 코드·n8n DB·실행이력 점검 + T3610 서버 로그·Honcho 점검
- **참조**: `docs/ra-advisory-api.md`, `docs/ra-advisory-raspi5p-integration.md`, CLAUDE.md Contract C

---

## 1. 핵심 결론

🔴 **raspi5p에 #83 자문 엔드포인트(`/v1/ra/advisory`) 연동 구현이 확인되지 않는다.** raspi5p의 활성 RA 워크플로우는 **구 엔드포인트 `/v1/chat/completions`(Contract A)**를 그대로 사용 중이며, 신규 자문 엔드포인트를 호출하는 코드·워크플로우·이력이 모두 0건이다.

→ **#83 자문 백엔드(T3610)는 raspi5p에 의해 아직 소비되지 않음.** 보고된 "1차 구현 완료"는 **범위(scope) 불일치**로, #83 Contract C 연동이 아니라 **기존 ra-request-to-op(v6, Contract A) 경로**를 가리키는 것으로 추정된다.

---

## 2. 교차 검토 근거 (3축, 모두 일치)

### ① raspi5p 코드 — `/v1/ra/advisory` 참조 0건
- `find /home/raspi5p -maxdepth 5` + `grep ra/advisory|/v1/ra/` → **파일 0건** (workspace/, .hermes/ 전수)
- 최근 2일 수정 코드 = op-taxonomy(OpenProject 분류)·lab_autonomous_check — 자문 연동과 무관

### ② n8n 워크플로우 — 활성 RA 경로 = 구 엔드포인트
raspi5p n8n(postgres)에서 RA 계열 워크플로우의 실제 호출 엔드포인트:
| 워크플로우 | active | 호출 엔드포인트 |
|-----------|--------|----------------|
| `ra-request-to-op_v6` | ✅ | **`/v1/chat/completions`** (Contract A) + `/v1/users/me/messages/` |
| `ra-mail-to-op` | ❌ | (비활성) |
| `infra-vote-broadcast` | ✅ | (#39, 별건) |
| advisory/자문 명칭 워크플로우 | — | **없음** |

→ `/v1/ra/advisory`를 호출하는 워크플로우 **0건**.

### ③ T3610 관측 — 신규 자문 엔드포인트 접근 0건
- 최근 2시간 `/v1/ra/advisory` 서버 접근 로그: **0건**
- Honcho `ra-advisory` / `ra_advisory_feedback` 레코드: **0건** (내 검증 데이터는 정리 완료 상태)

→ raspi5p가 live로 자문 엔드포인트를 호출한 적이 없다.

---

## 3. T3610 자문 백엔드(#83) 상태 — 계약 준수 양호 (재확인)

보고 불일치와 무관하게, T3610 측 자문 API는 정상 동작 중(본 세션 live 검증 완료):

| 검증 | 결과 |
|------|------|
| `POST /v1/ra/advisory` (8643, Bearer) | ✅ ra_kr/ra_us 단일 → 정상 JSON (evidence 포함) |
| 다중/불명확 → Yellow · 저신뢰/근거없음 → Yellow | ✅ |
| actor underscore 강제 (hyphen 차단) | ✅ |
| `POST /v1/ra/advisory/feedback` → Honcho 기록 | ✅ |
| `tests/test_advisory.py` 25 PASS | ✅ |

→ T3610 측 문제 아님. **대기 중인 자문 백엔드가 raspi5p에 의해 활성화되지 않은 상태.**

---

## 4. 해석 — 왜 보고가 불일치하는가

가장 유력한 해석: **raspi5p의 "RA 자문 연동 1차 구현" = 기존 `ra-request-to-op_v6` 워크플로우(구 `/v1/chat/completions`, Contract A `wp_comment` 기반)를 가리킨다.** 이는 #83에서 설계한 **Contract C(advisory) 자문 백엔드와 다른 계약**이다.

| 구분 | Contract A (기존, raspi5p 사용 중) | Contract C (#83, 미사용) |
|------|------------------------------------|--------------------------|
| 엔드포인트 | `/v1/chat/completions` | `/v1/ra/advisory` + `/feedback` |
| 응답 | `wp_comment` (email_type·matched_wp_id 등) | `advisory` (actor·decision·evidence·yellow_reason) |
| 라우팅 | caller가 `model`로 지정 | 서버측 키워드 라우팅 |
| 게이트 | n8n 내 | raspi5p 로컬 재검증(설계) |
| raspi5p 구현 | ✅ v6 활성 | ❌ 없음 |

즉 raspi5p는 **기존 A 경로를 다듬어 "완료"로 보고**했을 가능성이 높고, #83 C 경로로의 **마이그레이션은 착수 전**으로 판단된다.

---

## 5. 권고 (raspi5p에 요청)

1. **[최우선] 보고 범위 확인**: raspi5p가 "1차 구현 완료"로 보고한 것이 ① 기존 `ra-request-to-op`(Contract A)인지, ② #83 `/v1/ra/advisory`(Contract C) 신규 연동인지 명시할 것.
2. **#83 C 경로 연동이 목표라면** (본래 의도): `docs/ra-advisory-raspi5p-integration.md`의 DoD 7종(특히 로컬 게이트·금지위반 0건·fallback·feedback 회신)을 신규 구현해야 함. 현재 raspi5p 코드는 이 중 어느 것도 포함하지 않음.
3. **라이브 증빙**: 구현 후 raspi5p→T3610(`192.168.100.200:8643`, raspi5p는 Tailscale 미등록이므로 내부망 URL 사용) 실제 호출 1건 → T3610 서버 로그 + Honcho `ra_advisory` 기록으로 교차 검증 가능.

---

## 6. 결론

- 🔴 **#83 close 보류**. raspi5p에 #83 Contract C 자문 연동 구현이 확인되지 않음.
- T3610 자문 백엔드 자체는 완성·검증 완료. **병목은 raspi5p 측 실제 연동(또는 보고 범위 정합)에 있음.**
- 교훈: "보고된 완료"는 교차 검증 전까지 사실로 받아들이지 말 것 — 본 검토는 `feedback-live-test-catches-bugs`·`feedback-e2e-verify-before-report` 원칙의 교차 적용.

---

## 부록: 검토 접근 기록

- raspi5p SSH: `ssh raspi5p` (BatchMode, Tailscale 100.110.194.101) — 정상 접속
- 코드 탐색: `find`+`grep` (workspace/, .hermes/, maxdepth 5) → `/v1/ra/` 참조 0건
- n8n DB: `workflow_entity` 조회 → RA 워크플로우 실제 엔드포인트 = `/v1/chat/completions`
- T3610: 서버 journalctl + Honcho messages → `/v1/ra/advisory` 접근·기록 0건
