# RA Advisory API — T3610 RA 자문 백엔드 (#83)

> **경계**: T3610 RA agent는 **자문자**. raspi5p Hermes가 **실행주체**. T3610은 OpenProject에 직접 write하지 않는다.

## 개요
raspi5p Hermes가 RA 관련 WP/메일/요청을 받으면 T3610의 RA 전문가(ra_us/ra_eu/ra_kr)에게 **처리안**을 질의하고, raspi5p가 로컬 안전 게이트를 통과한 뒤에만 OP 댓글/검토요청을 실행한다.

## 엔드포인트
| Method | Path | 용도 |
|--------|------|------|
| `POST` | `/v1/ra/advisory` | RA 처리안 질의 (raspi5p → T3610) |
| `POST` | `/v1/ra/advisory/feedback` | 실행 결과 회신 (raspi5p → T3610) |

- **Base URL**: `http://<t3610>:8643` — Tailscale `http://100.119.79.28:8643` / 내부망 `http://192.168.100.200:8643`
- **Auth**: `Authorization: Bearer <API_SERVER_KEY>` (gitignored `.env`에서 raspi5p에 안전 전달)
- **Timeout**: client 30s / server 35s (Hermes CLI + RAG 지연 고려)
- **Honcho**: T3610이 로컬 Honcho(8000)에만 기록. raspi5p는 8643만 호출 (8000 노출 안 함).

## Request — `/v1/ra/advisory`
```json
{"query": "510(k) 신청 관련 질의 본문", "wp_context": {"wp_list": "WP-101 ...", "wp_id": 101}, "region_hint": "US"}
```
- `query` (필수, ≤8000자) · `wp_context.wp_list` (≤50 WP) · `region_hint` (선택: US/EU/KR 해당 actor)

## Response (고정 계약)
```json
{
  "actor": "ra_us",
  "region": "US",
  "confidence": 0.82,
  "decision": "comment_existing_wp",
  "wp_candidate": 101,
  "summary": "...",
  "recommended_comment": "...",
  "evidence": ["source/path.md#section"],
  "yellow_reason": null,
  "request_ref": "adv-<ts>"
}
```
- `decision`: `comment_existing_wp` | `request_new_wp_review` | `yellow_review` | `no_action`
- Yellow(`decision=yellow_review`) 시 `yellow_reason` 필수, 자동실행 불가.

## 라우팅 (서버측 키워드)
| 키워드 | actor |
|--------|-------|
| FDA, 510(k), QMSR, De Novo, PMA | ra_us |
| MDR, CE, NB, EUDAMED, EU clinical | ra_eu |
| MFDS, KGMP, 식약처, 한국 허가, 국내 인증 | ra_kr |
| 다중 규제권 / 불명확 | Yellow (LLM 호출 생략, 사전 반환) |

## 필수 규칙 (서버 검증 → 위반 시 Yellow)
- `actor` ∈ {ra_us, ra_eu, ra_kr} (라우팅 결과로 고정, LLM 표기 무시)
- **peer ID underscore만** (`ra-us` 금지)
- `confidence` ∈ [0,1]
- **고신뢰(confidence≥0.7) 응답은 evidence 필수** — 없으면 Yellow 강제

## 예시 응답
**① 단일 규제권(KR) 정상**:
```json
{"actor":"ra_kr","region":"KR","confidence":0.82,"decision":"comment_existing_wp","wp_candidate":1234,"summary":"MFDS 심사 반려 사유 반영 필요","recommended_comment":"식약처 의견서 회신 일정 확인 요청","evidence":["ra-project/.../MFDS_기술문서가이드.md#section3"],"yellow_reason":null}
```
**② 다중 규제권 Yellow**:
```json
{"actor":"system","region":"","confidence":0.0,"decision":"yellow_review","wp_candidate":null,"summary":"[Yellow] 다중 규제권이 감지되어 단일 RA 전문가 자문 불가","recommended_comment":null,"evidence":[],"yellow_reason":"multi_region"}
```
**③ 고신뢰 evidence 없음 Yellow** (RA가 0.9로 응답했으나 evidence 미포함):
```json
{"actor":"ra_us","region":"US","confidence":0.0,"decision":"yellow_review",...,"yellow_reason":"high_confidence_without_evidence"}
```

## 실행 정책 (raspi5p)
- T3610은 처리안만 반환. raspi5p가 WP 존재·상태·confidence·evidence **재검증 후 실행**.
- **1차 PoC 허용**: OP 댓글 또는 사람 검토요청만. **금지**: 완료·재오픈·상태전이·파괴 변경.

## Fallback
- T3610 timeout/failure → raspi5p **자동 실행 금지**, 사람 검토요청만.
- Honcho 자체 장애 → Honcho 경유 보고 금지, 직접 OP/log/알림 우회 (순환의존 회피).

## Feedback — `/v1/ra/advisory/feedback`
raspi5p 실행 후 회신 → T3610이 `ra_advisory_feedback` Honcho 기록.
```json
{"request_ref":"adv-<ts>","actor":"ra_kr","action_taken":"comment_added","wp_id":1234,"gate_result":"passed","note":"WP-1234 댓글 반영"}
```
- `action_taken`: `comment_added` | `review_requested` | `rejected` | `no_action`

## raspi5p 최소 호출 예시 (curl)
```bash
# 자문 요청
curl -s -X http://100.119.79.28:8643/v1/ra/advisory \
  -H "Authorization: Bearer $API_SERVER_KEY" -H "Content-Type: application/json" \
  -d '{"query":"510(k) predicate device 분석 요청","region_hint":"US"}'

# 실행 결과 회신
curl -s -X http://100.119.79.28:8643/v1/ra/advisory/feedback \
  -H "Authorization: Bearer $API_SERVER_KEY" -H "Content-Type: application/json" \
  -d '{"request_ref":"adv-...","actor":"ra_us","action_taken":"comment_added","wp_id":101,"note":"반영"}'
```

## 대시보드 가시화 (#81 연계)
- `ra_advisory` → `advisory_returned` (RA 캐릭터 반응), `ra_advisory_feedback` → `advisory_executed` (raspi5p/Iris 반응)
- 기록창 행 클릭 → 상세 패널에 자문 전문(summary·evidence·confidence·decision) 표시. CLI 없이 자문 이력 실점검.
