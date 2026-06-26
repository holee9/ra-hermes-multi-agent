# RA 자문 연동 — 2차 점검 + DoD 잔여 검증 요청서 (#83)

- **대상**: raspi5p RA 자문 연동(e2e 실증) 잔여 DoD 검증
- **검토자**: T3610 자문 백엔드 측 (본 repo) / 2026-06-25
- **전제 문서**: `docs/ra-advisory-raspi5p-review.md`(1차 검토, 2026-06-24), `docs/ra-advisory-raspi5p-integration.md`(DoD 7종), CLAUDE.md Contract C
- **핵심**: 1차 검토 시점 "raspi5p 연동 0건" 이후 **상황 변화 확인됨** — raspi5p가 Contract C 자문 소비를 라이브로 시작함. 자문 수신 단계는 검증 완료, **실행 루프 클로즈가 잔여 병목**.

---

## 0. 3차 업데이트 (2026-06-25): 실행 루프 클로즈 실증 + DoD-4 게이트 결함 발견

raspi5p가 `ra-request-to-op_v6`를 Contract C로 정식 개편(`chat/completions`→`/v1/ra/advisory`, 게이트·feedback 2경로·audit marker 추가)하고, 독립 e2e harness(`scripts/e2e-t3610-advisory-op.js`)로 실행 루프를 실증함.

### 실증 결과 — 루프 클로즈 확인 (3축: T3610 서버 + Honcho + OP 실조작)
KST 06-25 07:00+ 구간, Honcho `ra_advisory` 8건 + `ra_advisory_feedback` 6건:
- `ra_eu` → WP 114 매칭 → **WP 435 댓글(comment 6034/6036)** → feedback `comment_added`
- `ra_kr` request_new → **WP 1414/1415 신규 검토** → feedback `review_requested`
- `system` 다중 Yellow → **"rejected: blocked without OP mutation"** (자동실행 0건)

→ feedback 3종(`comment_added`/`review_requested`/`rejected`)이 실제 OP WP 조작과 짝지어 도착. **DoD-1, 2, 5 실증.**

### 🔴 DoD-4 게이트 결함 발견 (안전 직결 — 최우선 수정 권고)
harness `gate()`(152~168줄)와 v6 "자문 실행 가능?" 노드가 `allowMutation`을 **yellow / confidence<0.5 / no-evidence / wp_candidate 존재 / decision** 으로만 결정. **WP 상태(closed/done)를 검사하지 않음.**

- **위험**: T3610 자문은 WP 상태를 모르므로 closed/done WP에도 `comment_existing_wp`를 반환할 수 있음. 그러면 raspi5p 게이트가 통과시켜 **종료된 WP에 댓글을 달음** = 게이트 규칙 위반 + 안전 결함.
- 현재 harness 케이스에 종료 WP가 없어 발견이 안 됐을 뿐 (숨은 결함).

**권고 수정**:
1. 게이트에서 `wp_candidate`의 OP `_status`를 조회해 `closed`/`done`이면 `allowMutation=false` (reason=`wp_closed_or_done`).
   - harness `gate()`에 WP 상태 인자 추가; v6 "자문 실행 가능?" 노드 앞 WP 조회 노드가 status를 포함해 `advisoryGate`로 전달.
2. harness에 **E4 케이스**(의도적 closed/done WP → 게이트 차단 검증) 추가.

### DoD-3 미검증 — timeout harness 케이스 누락
harness `gate()`는 `advisoryResult`가 존재함을 전제. **None(timeout/장애) 분기가 없음.** v6 워크플로우 error catch → rejected feedback 경로 존재 여부도 미확인.
- **권고**: harness에 **E5 케이스**(advisory URL 무효/차단 → `request_advisory` None → OP 자동실행 0건, rejected feedback) 추가.

### 갱신된 DoD 현황
| DoD | 상태 | 비고 |
|-----|------|------|
| 1 단일권 루프 | ✅ 실증 | EU→WP435, KR→WP1414/1415 |
| 2 Yellow 자동실행 금지 | ✅ 실증 | rejected without OP mutation |
| 3 timeout fallback | ❌ 미검증 | harness E5 추가 필요 |
| 4 closed/done WP 차단 | 🔴 **결함** | 게이트 WP 상태 검사 누락 — 수정+E4 필요 |
| 5 feedback 기록 | ✅ 실증 | 3종 전부 |
| 6 금지항목 위반 0건 | ✅ (현재) | 전이/완료/삭제 0건 |
| 7 키 유출 | ✅ | Bearer 정상 |

### 테스트 데이터 정리 권고
- harness가 **실제 OP WP 435(댓글 6034/6036)/1414/1415**를 조작함(개발/테스트 데이터). 실행 종료 후 표기/삭제 권고 (이전 #81 데모 데이터 정리 패턴과 일관).

### 구분 메모
- harness(`e2e-t3610-advisory-op.js`) = **독립 Node 스크립트**(OP_API_KEY로 OP 직접 호출). 위 실증은 harness 실행 결과.
- n8n v6 워크플로우 자체 = 코드 완성 + 22:00 trigger 1회 성공. **실제 메일/요청 → 자동 실행 루프는 아직 단기** (별개 과제).

---

## 0b. 4차 업데이트 (2026-06-25): 문서-코드 불일치 + timeout 자동실행 위반 발견

raspi5p가 3차 권고 적용 후 e2e 재실행(09:00~09:50 KST)한다고 보고했으나, **코드 검증 결과 두 안전 결함이 코드에 반영되지 않았음.**

### 사실관계 (문서 vs 코드 불일치)
- ✅ 문서(`T3610_RA_ADVISORY_ENDPOINT.md`, 09:13): "raspi5p revalidates WP existence, **WP status**, confidence..." 명시
- 🔴 코드: v6 `advisoryGate`("WP 본문 생성" 68~92줄) + harness `gate()` — **status 검사 0건**. status는 WP 생성 기본 할당용(162줄)일 뿐 게이트 조건 아님.

### 🔴 DoD-3 timeout 자동실행 위반 (최우선)
v6 "WP 본문 생성" 노드 69줄:
```js
if (!advisory) return { allowMutation: true, reason: null, contract: 'legacy' };
```
자문 누락(timeout/장애/파싱실패) 시 게이트 통과(allowMutation:true) = **자동실행 허용**. Contract C / DoD-3 "T3610 장애 시 자동실행 절대 금지, 사람 검토" 직접 위반. 의료기기 RA에서 자문 백엔드 장애 시 무조건 실행으로 빠지는 가장 위험 경로.

### 🔴 DoD-4 closed/done 미반영 (3차와 동일 상태)
v6 78~83줄 + harness `gate()`: `comment_existing_wp` 분기가 `resolvedCandidate` 존재만 검사. closed/done status 미검사.

### 증빙 부재
Honcho `ra_advisory_feedback`에 closed/done·timeout 사유 rejected **0건**. 09:00~09:50 실행도 EU/KR/MULTI 동일 3케이스 반복(harness 독립 스크립트, n8n v6 자동실행 아님).

### 권고 (raspi5p — 코드 수정)
1. **[최우선]** v6 69줄: `!advisory → allowMutation:false` (reason=`advisory_unavailable`) + rejected feedback 경로
2. v6 78~83줄 + harness `gate()`: `resolvedCandidate.status not in (closed, done)` 검사 추가 (reason=`wp_closed_or_done`)
3. harness **E4**(closed/done WP)/**E5**(advisory URL 차단→timeout) 실행 → Honcho에 `wp_closed_or_done`/`advisory_unavailable` rejected 증빙

→ **코드 수정 + E4/E5 증빙 전까지 #83 close 보류.**

---

## 1. 2차 점검 결론

🟡 **raspi5p가 #83 Contract C(`/v1/ra/advisory`) 자문을 실제로 소비하기 시작했음이 3축 교차 검증으로 확인됨.** 단, 자문 수신까지이고 **게이트→OP실행→feedback 루프는 아직 닫히지 않음.**

| 축 | 증거 | 결과 |
|----|------|------|
| T3610 서버 로그 | 23:52~23:55 raspi5p(192.168.100.50) → `POST /v1/ra/advisory` 4건 HTTP 200 | ✅ |
| Honcho 기록 | `ra_advisory` 4건 + `ra_advisory_feedback` 1건 (UTC 14:52~15:07) | ✅ |
| raspi5p Codex 세션 | `{"nodes":24,"advisory":"...8643/v1/ra/advisory","gate":true}` + v6 wire-in 인지("F-05") | ✅ |

→ 3축 일치. **"자문 백엔드 → raspi5p 자문 소비" 경로가 진짜로 살아남.**

---

## 2. 실증 케이스 4종 (라우팅 핵심 시나리오)

| 케이스 | actor | 내용 | 결과 |
|--------|-------|------|------|
| US | `ra_us` | FDA 510(k) 보완요청 | 정상 자문 (underscore 강제) |
| EU | `ra_eu` | MDR EUDAMED 등록 (Basic UDI-DI) | 정상 자문 |
| KR | `ra_kr` | MFDS 변경허가 / KGMP 영향평가 | 정상 자문 |
| 다중 규제권 | `system` | Yellow — "다중 규제권 감지, 단일 RA 자문 불가" | Yellow 자동 라우팅 |

> 추가: `ra_advisory_feedback` smoke test 1건("rejected") — feedback 엔드포인트 자체 동작은 확인.

---

## 3. DoD 잔여 검증 요청 (raspi5p 대상)

raspi5p는 현재 4건 자문을 **Codex 세션 수동 호출**로 검증함. `ra-request-to-op_v6`가 `active=true`·게이트 ON·advisory wire-in 까지는 됐지만, **n8n 워크플로우가 자동으로 advisory→게이트→OP실행→feedback을 수행한 live 실행 증거는 아직 없음.** 아래 3개 라이브 시나리오를 돌려 루프를 닫을 것.

### E1. 단일권 정상 루프 (DoD-1, 5) — 최우선
- **목표**: 단일 규제권 요청 → 자문 수신 → 게이트 통과 → OP 댓글 추가 → feedback 회신 → Honcho `ra_advisory_feedback` 기록
- **주의(US-510K 교훈)**: 이전 Codex 케이스 `US-510K`가 `yellow_review`(confidence 0.78, "WP 연계 문서 부족")로 떨어짐. **WP 매칭 컨텍스트(`wp_context.wp_list` / `wp_id`)를 충분히 제공**해야 정상 `comment_existing_wp`가 나옴. 컨텍스트 없으면 정상 통과 케이스를 검증할 수 없음.
- **검증 포인트**:
  - T3610 자문 `decision == "comment_existing_wp"` (Yellow 아님)
  - raspi5p 게이트 통과 → OpenProject WP에 **댓글만** 추가 (`recommended_comment` 사용)
  - **금지 위반 0건**: WP 상태 전이 / 완료 / 재오픈 / 삭제 시도 없음
  - `post_feedback(action="comment_added", gate_result="passed", wp_id=...)` 회신
- **T3610 관측**: 서버 로그 `/v1/ra/advisory/feedback` POST 1건 + Honcho `ra_advisory_feedback` +1

### E2. Fallback — T3610 장애 시뮬 (DoD-3)
- **목표**: T3610 자문 timeout/failure 시 **자동실행 절대 금지**, 사람 검토요청 생성
- **방법**: raspi5p에서 advisory URL 일시 차단(방화벽/잘못된 호스트) 또는 `API_SERVER_KEY` 의도적 무효화 → `request_advisory`가 `None` 반환
- **검증 포인트**:
  - raspi5p 자동실행(댓글/전이) **0건**
  - 사람 검토요청 생성
  - `post_feedback(action="review_requested", gate_result="blocked", note="advisory unavailable")`
- **T3610 관측**: 이 케이스는 T3610 도달 자체가 없으므로 **raspi5p 로컬 로그가 1차 증거**. feedback도 도달 불가(장애 상태)이므로, fallback 시엔 feedback 생략이 정상 — raspi5p가 로컬로 "자동실행 0건"을 증명하면 됨.

### E3. closed/done WP 게이트 차단 (DoD-4)
- **목표**: 종료된 WP에 대한 `comment_existing_wp` 자문 → raspi5p 게이트가 차단 → 사람 검토
- **방법**: 의도적으로 closed/done 상태인 WP를 대상으로 자문 요청(T3610은 WP 상태를 모르므로 정상 `comment_existing_wp` 반환)
- **검증 포인트**:
  - raspi5p가 WP 상태 재확인 → closed/done 감지 → **댓글 추가 안 함**
  - `post_feedback(action="review_requested", gate_result="blocked", note="WP closed/done")`

---

## 4. T3610 관측 포인트 (교차 검증 쿼리)

raspi5p가 E1/E2/E3를 돌릴 때, T3610은 아래로 교차 검증.

### 4.1 자문 호출 + feedback POST (서버 로그)
```bash
# 최근 자문 + feedback 접근
journalctl -u hermes-api-server --since "30 min ago" \
  | grep -E "ra/advisory"
# 기대: /v1/ra/advisory (200) + /v1/ra/advisory/feedback (200) 쌍
```

### 4.2 Honcho 자문/피드백 기록 (DoD-5 루프 클로즈)
```bash
docker exec honcho-postgres-1 sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c \
  "select session_name, metadata->>'"'"'record_type'"'"' rt, peer_name, left(content,50) c, created_at \
   from messages \
   where session_name in ('"'"'ra-advisory'"'"','"'"'ra-advisory-feedback'"'"') \
   order by created_at desc limit 15;"'

# 카운트 (ra_advisory_feedback 증가 = 루프 클로즈 증거)
docker exec honcho-postgres-1 sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -c \
  "select metadata->>'"'"'record_type'"'"' rt, count(*) from messages \
   where metadata->>'"'"'record_type'"'"' like '\''ra_advisory%'\'' group by 1;"'
```

### 4.3 통과 기준 (라이브 증빙 매칭)
| 케이스 | T3610 서버 | Honcho | OP 부작용 |
|--------|-----------|--------|----------|
| E1 | advisory 200 + feedback 200 | ra_advisory_feedback +1 (action=comment_added) | WP 댓글 1건, **상태 전이 0** |
| E2 | (도달 없음 — 정상) | (feedback 없음 — 정상) | 자동실행 0건 (raspi5p 로컬 증빙) |
| E3 | advisory 200 + feedback 200 | ra_advisory_feedback +1 (gate_result=blocked) | 댓글 0건 (차단) |

---

## 5. #83 close 조건 (갱신)

1차 review.md는 "#83 close 보류"였으나, 자문 소비가 확인된 만큼 조건부 close로 전환:

- [x] T3610 자문 백엔드 완성·검증 (1차)
- [x] raspi5p 자문 소비 라이브 확인 (2차, 본 문서)
- [ ] **E1 라이브**: 단일권 루프 클로즈 (게이트→OP댓글→feedback, 자동실행)
- [ ] **E2 라이브**: fallback 시 자동실행 0건 증명
- [ ] **E3 라이브**: closed/done WP 게이트 차단 증명
- [ ] 금지항목(전이/완료/재오픈/삭제) 위반 0건 — E1~E3 전체에서

→ E1~E3 라이브 증빙이 T3610 관측(4.3)과 정합하면 **#83 close**.

---

## 6. 교훈 (갱신)

- 1차 "0건" → 2차 "4건 라이브": 보고 시점과 점검 시점의 갭이 큼. **"보고된 상태"는 교차 검증 전까지 사실로 받아들이지 말 것** (1차 교훈 유지).
- 자문 수신(라우팅) 검증과 실행 루프(게이트·OP·feedback) 검증은 **별개 단계**. 전자 통과가 후자 통과를 의미하지 않음.
- US-510K yellow 사례: **WP 컨텍스트 제공 여부가 정상 통과 케이스 성패를 가름**. e2e 케이스 설계 시 입력 컨텍스트를 케이스 의도에 맞게 통제할 것.
