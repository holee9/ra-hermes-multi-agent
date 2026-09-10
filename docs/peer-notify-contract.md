# Peer Notify 계약 — T3610 ↔ raspi5p 기기간 댓글 알림 (SPEC-DEVCOMM-001 M4)

> 상태: 계약 문서 (T3610 수신 측 구현 기준, commit `d22ade0` 이후). raspi5p 측 구현은 **GATE-2**(n8n 변경 사전 보고·승인) 대상이며 이 문서는 그 인계 자료다.
> 원장: GitHub 이슈 댓글이 **유일한 영구 원장**이다. 이 채널은 "새 댓글이 있다"는 알림만 나른다(C7 — 본문을 싣지 않음).
> 이슈: #143

## 1. 두 계층

| 계층 | 방향 | 지연 | 실패 시 |
|---|---|---|---|
| ① 푸시 nudge | 댓글 작성 직후 → 상대 기기 `/v1/peer/notify` | < 1 s | 유실돼도 ②가 복구 |
| ② 폴링 백스톱 | 각 기기가 5분마다 GitHub 댓글 조회 → 자기 `/v1/peer/notify` | ≤ 5 min | 커서 미전진(fail-closed), 다음 주기 재시도 |

두 경로가 같은 댓글을 두 번 전달할 수 있으므로 수신기는 `comment_url`로 멱등 처리한다(§3).

## 2. 수신 엔드포인트 (T3610 구현 = 계약)

```
POST http://<T3610>:8643/v1/peer/notify
Authorization: Bearer <API_SERVER_KEY>
Content-Type: application/json
```

T3610 주소: 사내망 `192.168.100.200`, Tailscale `100.119.79.28`. 포트 8643은 T3610이 raspi5p에 여는 **유일한 표면**이다(C1).

### 2.1 요청 본문 — 4필드 고정

| 필드 | 타입 | 규칙 |
|---|---|---|
| `issue` | integer | 이슈 번호. bool 불가 |
| `comment_url` | string | 댓글 `html_url` (`…/issues/141#issuecomment-200` 형식). **멱등 키** |
| `author` | string | 댓글 작성자 GitHub login |
| `ts` | string | 댓글 `created_at` (ISO-8601 Z) |

본문·제목·첨부는 싣지 않는다. 필드 추가는 additive로만 허용하며 수신기는 모르는 필드를 무시한다.

### 2.2 응답

| 상태 | 본문 | 뜻 |
|---|---|---|
| 200 | `{"status":"accepted","comment_url":…}` | 처음 본 댓글. 이벤트 로그 기록 |
| 200 | `{"status":"duplicate","comment_url":…}` | 이미 처리한 댓글(푸시/폴링 중복). 아무것도 안 함 |
| 400 | `{"error":"issue must be an integer"}` 등 | 스키마 위반 |
| 401 | `{"error":"Unauthorized"}` | Bearer 불일치 |

수신기는 Honcho·OpenProject·자문 경로(`/v1/ra/advisory`)를 건드리지 않는다(C2, REQ-DC-007). 처리 결과는 `/var/log/peer-notify.jsonl`에 한 줄 이벤트로만 남는다:

```json
{"ts":"2026-09-10T00:00:00Z","type":"peer_comment","actor":"holee9",
 "payload":{"issue":143,"comment_url":"https://github.com/…#issuecomment-200","comment_ts":"2026-09-10T00:00:00Z"}}
```

## 3. 멱등성·내구성

- dedup 키는 `comment_url`. 최근 500건을 `~/.hermes/peer-notify-seen.json`에 영속 → 서비스 재시작 후 폴러가 재전달해도 한 번만 처리.
- **지원 범위: 새 댓글만 알린다. 기존 댓글의 *수정*은 재알림하지 않는다** (#143, codex 재현). 이유는 계약 자체에 있다:
  `build_nudge`의 `ts`는 `created_at`이고 dedup 키는 `comment_url`이므로, 같은 댓글을 수정하면 **nudge 4필드가 원본과
  완전히 동일**해져 수신기가 중복으로 버린다. 커서(`compute_new_last_seen`)만 `updated_at`으로 전진하므로 폴러는
  다시 가져오지만 알림은 나가지 않는다. → **정정 내용을 상대에게 전달하려면 새 댓글로 남긴다.**
  이 동작을 바꾸려면 `ts` 의미 변경 또는 버전 필드 추가가 필요하고, 그것은 양쪽 소비자(T3610·raspi5p)의 외부
  인터페이스 변경이므로 **G2/G5 결정과 Pi 인계 경로**를 거친다. 승인 전 일방 변경 금지.
- **HTTP `accepted` ≠ 상대가 읽음.** 수락은 "알림이 도착해 기록됐다"는 뜻이다. 담당 에이전트가 실제로 댓글을 열람·업무를 재개했는지는 이 계약 밖이며, 그 소비자 연결은 별도 마일스톤(#143 결함 3)이다.

## 4. 폴링 백스톱 규칙 (양쪽 공통)

`scripts/peer-comment-poller.py` (T3610) 기준. raspi5p도 동일 규칙을 따른다.

| 항목 | 규칙 |
|---|---|
| 조회 | `GET repos/<repo>/issues/comments?since=<last_seen>&per_page=100&page=N` — 짧은 페이지까지 순회. 상한(기본 10페이지) 초과 시 커서를 올리지 않고 실패 |
| 자기 기기 댓글 제외 | **두 기기가 같은 GitHub 계정(holee9)을 쓴다.** login으로 거르면 상대 댓글도 사라지므로 login 필터는 기본 OFF. 대신 각 기기가 자기 댓글 본문 끝에 **기기 마커**를 넣고 자기 마커가 있는 댓글만 건너뛴다 |
| 기기 마커 | T3610: `<!-- peer:t3610 -->` / raspi5p: `<!-- peer:raspi5p -->` (HTML 주석이라 GitHub 화면에는 보이지 않음) |
| 커서 | 성공한 실행에서만 `last_seen = max(updated_at)`. POST 실패가 하나라도 있으면 전진 안 함 |
| 첫 실행 | 상태 파일이 없으면 1시간만 소급 |

## 5. raspi5p 측 인계 항목 (GATE-2 — n8n 변경은 사전 보고 후)

1. **발신(푸시)**: raspi5p가 댓글을 쓰는 지점(n8n 워크플로/스크립트) 직후 §2 요청을 T3610에 POST. 실패는 로그만 남기고 무시(②가 복구). 타임아웃 10 s, 재시도 최대 3회.
2. **수신**: raspi5p에도 같은 4필드 엔드포인트(또는 n8n webhook)를 두어 T3610 발신(M3)이 붙을 자리를 만든다. 멱등 키·응답 형식은 §2.2와 동일.
3. **폴링**: §4 규칙으로 5분 타이머. 자기 마커 `<!-- peer:raspi5p -->`.
4. **댓글 작성 규칙**: raspi5p가 남기는 모든 댓글 본문 끝에 `<!-- peer:raspi5p -->` 추가.

## 6. E2E 수락 기준 (AC-4)

| 기준 | 측정 |
|---|---|
| raspi5p 댓글 → T3610 `accepted` | 1 s 이내 (푸시). `/var/log/peer-notify.jsonl`에 이벤트 1건 |
| 푸시 유실 시 | 5 min 이내 폴링으로 동일 `comment_url` `accepted` 1건, 이후 `duplicate` |
| 같은 계정 | T3610 폴러가 raspi5p 댓글을 **제외하지 않음** (kept ≥ 1) |
| 자기 댓글 | 자기 마커 댓글은 nudge 0건 |

## 7. 환경 변수 (T3610 `scripts/.env`)

| 변수 | 뜻 | 기본 |
|---|---|---|
| `API_SERVER_KEY` | Bearer 키 (양쪽 동일 값) | 필수 |
| `PEER_POLL_REPO` | 폴링 대상 repo | `holee9/ra-hermes-multi-agent` |
| `PEER_POLL_SELF_MARKER` | 이 기기의 댓글 마커 | 빈 값 → **설정 필요** (`<!-- peer:t3610 -->`) |
| `PEER_POLL_SELF_LOGIN` | 기기별 계정이 다를 때만 | 빈 값 |
| `PEER_POLL_MAX_PAGES` | 페이지 상한 | 10 |
| `PEER_NOTIFY_LOCAL_URL` | 폴러가 POST할 자기 수신기 | `http://localhost:8643/v1/peer/notify` |
| `PEER_NOTIFY_STATE` / `PEER_NOTIFY_LOG` | dedup 상태 / 이벤트 로그 | `~/.hermes/peer-notify-seen.json` / `/var/log/peer-notify.jsonl` |
