# raspi5p 통합 구현 지시서 — T3610 RA 자문 백엔드 연동 (#83)

> **경계(불변)**: 이 작업은 raspi5p Hermes를 **실행주체**로, T3610 RA agent를 **자문자**로 연동한다. raspi5p가 최종 실행권자이며, **T3610은 OpenProject에 직접 write하지 않는다** (이미 T3610 측 `/v1/ra/advisory`로 자문만 반환하도록 구현 완료).

---

## 0. 배경 · 현재 상태

- **T3610 측(완료, #83)**: `POST /v1/ra/advisory` + `POST /v1/ra/advisory/feedback` 가 동작 중(port 8643). RA 처리안을 JSON으로 반환하고, Honcho에 기록까지 마침.
- **raspi5p 측(본 과제)**: RA 관련 WP/메일/요청 수신 → T3610 자문 호출 → **로컬 안전 게이트** → (통과 시) OpenProject 댓글/검토요청 실행 → 실행 결과를 T3610에 feedback.
- 계약·라우팅·fallback 상세: `docs/ra-advisory-api.md` (T3610 repo). 본 문서는 raspi5p가 **구현해야 할 것**에 집중.

---

## 1. 사전 준비

1. **API_SERVER_KEY 확보**: T3610의 gitignored `.env`(`/opt/hermes-ra/.env` 또는 `scripts/.env`)에 있는 `API_SERVER_KEY` 값을 **안전한 경로로 전달받아** raspi5p 환경변수에 등록. (절대 커밋 금지)
2. **접속 주소**:
   - Tailscale: `http://100.119.79.28:8643` (권장)
   - 내부망: `http://192.168.100.200:8643`
3. **연결 확인** (raspi5p에서):
   ```bash
   curl -s http://100.119.79.28:8643/health
   # {"service":"hermes-api-server","status":true}
   curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $API_SERVER_KEY" \
     http://100.119.79.28:8643/v1/models   # 200
   ```

---

## 2. 구현 항목 (raspi5p 측)

### 2.1 Advisory 클라이언트 (필수)
하나의 함수/모듈로 T3610 자문을 호출.

```python
# 예시(Python). raspi5p 환경에 맞게 언어/런타임 적용.
import os, requests

ADVISORY_URL = os.environ["ADVISORY_URL"]            # http://100.119.79.28:8643
API_SERVER_KEY = os.environ["API_SERVER_KEY"]

def request_advisory(query: str, wp_context: dict | None = None,
                     region_hint: str | None = None) -> dict | None:
    """T3610 RA 자문 요청. 실패/timeout → None(=fallback)."""
    try:
        r = requests.post(
            f"{ADVISORY_URL}/v1/ra/advisory",
            headers={"Authorization": f"Bearer {API_SERVER_KEY}",
                     "Content-Type": "application/json"},
            json={"query": query, "wp_context": wp_context or {},
                  "region_hint": region_hint},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except Exception:
        return None   # ★ 반드시 None 처리 → 자동실행 금지, 사람 검토로
```

- `wp_context`: `{"wp_list": "...", "wp_id": 123}` (선택). `region_hint`: `US`/`EU`/`KR` 또는 `ra_us`/`ra_eu`/`ra_kr` (선택).

### 2.2 로컬 안전 게이트 (필수 — raspi5p가 재검증)
**T3610의 자문을 무조건 신뢰하지 말 것.** raspi5p가 아래를 재확인 후에만 실행.

| 검증 | 불통 시 |
|------|--------|
| `decision == "yellow_review"` 또는 `yellow_reason` 존재 | **사람 검토요청** (자동실행 금지) |
| `decision` not in {`comment_existing_wp`, `request_new_wp_review`} | 사람 검토요청 |
| `confidence < 0.5` 또는 `evidence` 없음 | 사람 검토요청 (T3610이 Yellow로 보냈겠지만 이중확인) |
| `wp_candidate` WP가 OpenProject에 **존재**하는가 | 아니면 → `request_new_wp_review` 경로(신규 검토) |
| 해당 WP 상태가 `closed`/`done`이 아닌가 | closed/done이면 → 사람 검토요청 (게이트 위반) |
| T3610 응답 None(timeout/장애) | **자동실행 절대 금지** → 사람 검토요청 |

### 2.3 실행 (1차 PoC 범위 — 반드시 준수)
게이트 통과 시에만 아래 **둘 중 하나**만 수행:
- `comment_existing_wp` → OpenProject WP에 **댓글 추가** (`recommended_comment` 사용)
- `request_new_wp_review` → **사람 검토요청 생성** (댓글/알림으로 사람에게 회신, 자동 전이 아님)

**금지 (PoC)**: WP 상태 전이(진행중→리뷰중 등), 완료 처리, 재오픈, 삭제, 기타 파괴적 변경.

### 2.4 Feedback 회신 (필수 — 루프 클로즈)
실행(또는 거부/검토) 후 반드시 T3610에 결과 회신 → RA 학습 루프로 환류.

```python
def post_feedback(request_ref, actor, action_taken, wp_id=None, gate_result="passed", note=""):
    requests.post(
        f"{ADVISORY_URL}/v1/ra/advisory/feedback",
        headers={"Authorization": f"Bearer {API_SERVER_KEY}",
                 "Content-Type": "application/json"},
        json={"request_ref": request_ref, "actor": actor,
              "action_taken": action_taken, "wp_id": wp_id,
              "gate_result": gate_result, "note": note},
        timeout=10,
    )
```
- `action_taken` ∈ {`comment_added`, `review_requested`, `rejected`, `no_action`}
- `gate_result`: `passed` | `blocked` | `yellow`

---

## 3. 전체 흐름 (의사코드)

```
on RA 관련 요청 수신 (WP/메일/요청):
    query, wp_context, region_hint = 추출()
    adv = request_advisory(query, wp_context, region_hint)
    request_ref = adv["request_ref"] if adv else f"local-{ts}"

    # --- fallback: T3610 장애 ---
    if adv is None:
        create_human_review(query, reason="T3610 자문 timeout/장애")
        post_feedback(request_ref, actor="system", action_taken="review_requested",
                      gate_result="blocked", note="advisory unavailable")
        return

    # --- Yellow: 자동실행 금지 ---
    if adv["decision"] == "yellow_review" or adv.get("yellow_reason"):
        create_human_review(query, adv)
        post_feedback(request_ref, adv["actor"], action_taken="review_requested",
                      gate_result="yellow", note=adv.get("yellow_reason"))
        return

    # --- 로컬 게이트: WP 재확인 ---
    wp_id = adv.get("wp_candidate")
    op = fetch_wp(wp_id) if wp_id else None
    if adv["decision"] == "comment_existing_wp":
        if not op or op.state in ("closed", "done"):
            create_human_review(query, adv, reason="WP 없음/종료")
            post_feedback(request_ref, adv["actor"], "review_requested", gate_result="blocked")
            return
        op.add_comment(wp_id, adv["recommended_comment"])      # ★ 댓글만
        post_feedback(request_ref, adv["actor"], "comment_added", wp_id=wp_id,
                      gate_result="passed", note="댓글 반영")
    elif adv["decision"] == "request_new_wp_review":
        create_human_review(query, adv)                        # 신규 → 사람
        post_feedback(request_ref, adv["actor"], "review_requested", gate_result="passed")
    else:
        create_human_review(query, adv, reason="알 수 없는 decision")
        post_feedback(request_ref, adv["actor"], "review_requested", gate_result="blocked")
```

---

## 4. 응답 계약 (T3610이 반환, 재확인용)

```json
{"actor":"ra_kr","region":"KR","confidence":0.82,
 "decision":"comment_existing_wp","wp_candidate":1234,
 "summary":"...","recommended_comment":"...",
 "evidence":["source/path.md#section"],"yellow_reason":null,
 "request_ref":"adv-<ts>"}
```
- `actor`는 항상 underscore(`ra_us`/`ra_eu`/`ra_kr`). hyphen이 오면 **비정상** → 사람 검토.
- Yellow 예: `{"decision":"yellow_review","yellow_reason":"multi_region","actor":"system",...}`

---

## 5. Fallback 정책 (불변)

- **T3610 timeout/failure → raspi5p 자동실행 절대 금지**. 사람 검토요청만 생성.
- **Honcho 자체 장애**: 본 연동과 무관 (T3610이 Honcho 기록 담당). raspi5p는 Honcho 직접 접근 안 함 (8643만 호출).
- raspi5p 로컬 장애 시에도 자동 전이/파괴 금지.

---

## 6. 완료 기준 (raspi5p 측 DoD)

1. RA 단일 규제권 요청 → T3610 자문 수신 → 게이트 통과 → OP 댓글 반영 → feedback 회신 (end-to-end)
2. Yellow 자문 → 자동실행 안 함, 사람 검토요청 생성 → feedback(`review_requested`)
3. T3610 timeout 시뮬레이션(네트워크 차단 등) → 자동실행 안 함, 사람 검토요청 → feedback(`blocked`)
4. closed/done WP에 대한 `comment_existing_wp` → 게이트 차단, 사람 검토
5. `post_feedback` 호출로 T3610 Honcho `ra_advisory_feedback` 기록 확인 (T3610에서 `record_type` 조회)
6. **금지 항목 위반 없음**: 상태 전이/완료/재오픈/삭제 시도 0건 (로직·테스트로 증명)
7. 키 유출 없음 (`API_SERVER_KEY` 커밋/로그 미포함)

---

## 7. 산출물 (raspi5p)

- [ ] advisory 클라이언트 모듈 (`request_advisory`)
- [ ] 로컬 게이트 로직 (`verify_and_decide`)
- [ ] 실행: OP 댓글 추가 + 사람 검토요청 생성
- [ ] feedback 회신 (`post_feedback`)
- [ ] 위 흐름을 엮은 오케스트레이션 (n8n 워크플로우 또는 Hermes 스크립트)
- [ ] DoD 7종 검증 (특히 fallback·금지위반 0건)
- [ ] 연동 완료 시 T3610 측 #83 close 요청

---

## 8. 참조

- T3610 자문 API 전문: `docs/ra-advisory-api.md` (ra-hermes repo)
- 계약·라우팅: CLAUDE.md "Contract C — RA Advisory" (ra-hermes repo)
- 접속: Tailscale `http://100.119.79.28:8643` / 내부망 `http://192.168.100.200:8643`
- 문의/이슈: `holee9/ra-hermes-multi-agent#83`
