# 활동 이벤트 계약 v2.1

> 상태: 제안 → 사람 승인 시 정본
> 변경 규칙: **additive-only.** 필드 추가만 허용. 삭제·의미 변경 금지. 위반 시 v3.
> 원천: 6월 확정 계약 v1(conclusion·투표·매칭·3점평가) → v2 봉투(2026-08 제안) → v2.1 화행·홉 추가(본 문서)
> 검증: `tools/validate_events.py` + `docs/contract/event-v2.1.schema.json`

---

## 0. 이 계약이 해결하는 결손

| # | v2까지의 결손 | v2.1 해법 | 출처 |
|---|---|---|---|
| D1 | 화행 부재 — 수신자가 응답 의무를 판정 못함 | `act` 7종 + `requires_reply` | Munder Difflin HIVE.md §4 (FIPA-lite) |
| D2 | 루프 방어 부재 — peer 간 무한 핑퐁 | `hops` + 상한 + 종결형 화행 | HIVE.md §4, hive.ts `HOP_CAP` |
| D3 | 동시 쓰기 규율 부재 | 계약 외 — `docs/hive/hive-layout.md` | HIVE.md §2·§3 |
| D4 | 폭주 차단 사다리 부재 | 계약 외 — `docs/governance/circuit-breaker.md` | breaker.ts |

D3·D4는 계약이 아니라 **구현 규율**이므로 별도 문서. 본 문서는 D1·D2만 다룬다.

---

## 1. 봉투 (envelope)

```json
{
  "v": "2.1",
  "id": "evt_20260909T091233_a1b2",
  "ts": "2026-09-09T09:12:33+09:00",
  "workspace": "work",
  "actor": "ra_us",
  "kind": "matching",
  "case": { "wp": 1042, "regime": "US" },
  "payload": {},
  "artifacts": [],
  "cost": { "model": "qwen3-gx10", "in_tokens": 1820, "out_tokens": 640 },
  "corr": "evt_20260909T091230_9f3e",

  "to": "ra_eu",
  "act": "request",
  "requires_reply": true,
  "hops": 0,
  "conversation": "conv_1042_matching"
}
```

### 1.1 v2 유지 필드 (변경 없음)

| 필드 | 타입 | 필수 | 규칙 |
|---|---|---|---|
| `v` | string | ✓ | `"2.1"` 고정 |
| `id` | string | ✓ | 시간순 정렬 가능. 형식 `evt_<YYYYMMDDTHHMMSS>_<4hex>`. **전역 유일** |
| `ts` | string | ✓ | ISO-8601, 타임존 포함 |
| `workspace` | string | ✓ | `work` \| `infra` \| (신규 workspace 슬러그) |
| `actor` | string | ✓ | 뼈대 actor ID만. 사람 이름 금지(원칙 9). 사람은 `human` |
| `kind` | string | ✓ | §2 목록 중 하나 |
| `case` | object | – | `{wp, regime?}`. 사안 무관 이벤트(infra·policy)는 생략 |
| `payload` | object | ✓ | kind별 §2. 빈 객체 허용 |
| `artifacts` | array | – | `[{type, name, ref}]`. `ref`는 `gitea://` 또는 `nas://` URI |
| `cost` | object | – | `{model, in_tokens, out_tokens}`. 모델 호출 이벤트만 |
| `corr` | string | – | 원인 이벤트 `id`. 스레딩·애니메이션 연결 |

### 1.2 v2.1 추가 필드

| 필드 | 타입 | 필수 | 규칙 |
|---|---|---|---|
| `to` | string | – | 수신자. actor ID \| `broadcast` \| `human`. **없으면 관찰 이벤트**(v2 동작 그대로), **있으면 대화 이벤트**(§3 규칙 적용) |
| `act` | string | `to` 있을 때 ✓ | `request` \| `inform` \| `propose` \| `query` \| `agree` \| `refuse` \| `done` |
| `requires_reply` | boolean | `to` 있을 때 ✓ | `act ∈ {request, query, propose}`일 때만 `true` 허용. 그 외 `true`는 **검증 오류** |
| `hops` | integer | `to` 있을 때 ✓ | 최초 발신 0. 답신(`corr` 있음)은 원인 이벤트 `hops + 1`. 상한 §3.3 |
| `conversation` | string | – | 스레드 식별자. 답신은 원인의 `conversation` 상속 |

---

## 2. kind 목록

v2와 동일. 각 kind의 기본 화행 매핑을 추가한다 — `to`가 있을 때 `act` 생략 시 이 값이 적용된다.

| kind | 의미 | payload 핵심 | 기본 act | v1 대응 |
|---|---|---|---|---|
| `case_open` | WP 생성 관찰 | `source`(mail/office/telegram/op), `title` | `inform` | — |
| `matching` | 사안-전문가 매칭 판단 | `decision`, `confidence`, `basis[]` | `propose` | 매칭 |
| `comment` | WP 코멘트 | `text_ref` | `inform` | conclusion |
| `handoff` | 규제권 간 이관 요청 | `to_actor`, `reason` | `request` | — |
| `vote_call` | 투표 소집 | `question`, `options[]` | `query` | 투표 |
| `vote_cast` | 투표 | `choice`, `weight` | `inform` | 투표 |
| `vote_result` | 집계 (n8n) | `tally`, `decision` | `inform` | 투표 |
| `eval3` | 사람 3점 사후 평가 | `score`(1–3), `target_evt` | `inform` | 3점평가 |
| `artifact` | 산출물 발생 | `artifacts[]` 채움 | `inform` | — |
| `absence` | 매칭 실패·직능 공백 | `gap_tag`, `case` | `inform` | — |
| `infra` | 호스트 상태 | `host`, `metric`, `level` | `inform` | — |
| `policy` | 정책 발화 | `action`(pause/resume/throttle/steer/constrain/stop/release/refuse-invalid), `reason`, `target_actor?`, `ref_evt?` | `inform` | — |
| `hire_proposal` | 부재 임계 도달 | `gap_tag`, `count`, `window` | `propose` | — |
| `escalation` | **신규** — 사람 호출 | `reason`(hop-cap/undeliverable/breaker/refuse-deadlock), `ref_evt` | `request` | — |

`policy.action`에 `steer/constrain/stop`이 추가되었다(서킷 브레이커 연동). 기존 `pause/resume/throttle` 유지.
`release`(전달 게이트 수동 해제, `docs/governance/delivery-gate.md` §4)와 `refuse-invalid`(라우터 검증 거부 기록, `docs/hive/router-spec.md` §3)는 **계약 확장(additive)** 으로 enum에 포함한다 — 기존 action에 매핑하지 않는다. 두 값 모두 `payload.ref_evt`로 대상 메시지를 가리킨다.

**완료·재오픈에는 kind가 없다.** 사람 전용 행위는 OpenProject에서만 일어난다(원칙 4).

---

## 3. 대화 규칙 (`to`가 있는 이벤트)

### 3.1 화행 의미

| act | 의미 | 답신 의무 | 종결 |
|---|---|---|---|
| `request` | 행위 요청 | 수신자 → `agree` \| `refuse` \| `done` | ✗ |
| `query` | 정보 질의 | 수신자 → `inform` | ✗ |
| `propose` | 제안 | 수신자 → `agree` \| `refuse` | ✗ |
| `inform` | 통지 | 없음 | ✓ |
| `agree` | 수락 | 없음 (이후 `done`은 별도) | ✓ |
| `refuse` | 거절 | 없음 | ✓ |
| `done` | 완료 보고 | 없음 | ✓ |

**종결형(`inform`·`agree`·`refuse`·`done`)에 답신하면 검증 오류.** 이것이 핑퐁을 끊는 1차 방어선이다.

### 3.2 답신 규칙

- 답신은 `corr = 원인 id`, `conversation = 원인 conversation`, `hops = 원인 hops + 1`.
- 자기 자신에게 발신 금지 (`to == actor` → 라우터 거부).
- `broadcast`는 발신자 제외 활성 actor 전체. `requires_reply`는 `broadcast`에서 `false` 강제.

### 3.3 홉 상한

- `HOP_CAP` 값은 **운영 실측 후 설정**. 초기 관찰값으로 MD의 12를 참고하되 우리 값은 미확정.
- `hops > HOP_CAP` 도달 시 라우터는 메시지를 **폐기하지 않는다.** `kind:"escalation"`, `to:"human"`, `payload.reason:"hop-cap"`으로 변환해 사람에게 전달한다.
- MD 코드는 폐기(`kind:'drop'`)를 선택했다. 우리는 원칙 4에 따라 **사람 호출**을 선택한다 — 12번 오간 논의는 버릴 것이 아니라 사람이 봐야 할 것이다.

### 3.4 거절 교착

- 동일 `conversation`에서 `refuse`가 양방향으로 2회 이상 발생 → 라우터가 `escalation(reason:"refuse-deadlock")` 발화.

---

## 4. 관찰 이벤트 vs 대화 이벤트

```
to 없음  →  관찰 이벤트. v2와 100% 동일. 살은 이것만 읽어도 v2 동작 유지.
to 있음  →  대화 이벤트. §3 규칙 적용. 라우터가 inbox로 이송.
```

살은 두 종류를 구분 없이 `log.jsonl`에서 읽는다. 대화 이벤트는 회의실 애니메이션(`vote_call`)·봉투 비행(`to` 있음)의 원천이 된다.

---

## 5. 하위 호환

- v2 이벤트(`to`·`act`·`hops` 없음)는 v2.1 검증기를 **통과**한다.
- v2.1 이벤트는 v2 소비자가 추가 필드를 무시하면 그대로 읽힌다.
- `v` 필드로 소비자가 분기할 수 있으나, 분기 없이도 동작해야 한다.

---

## 6. 매핑 — MD hive 메시지 ↔ 우리 이벤트

| MD `HiveMessage` | 우리 v2.1 | 비고 |
|---|---|---|
| `id` | `id` | 형식만 다름 |
| `conversation` | `conversation` | 동일 |
| `in_reply_to` | `corr` | 동일 의미 |
| `from` | `actor` | 우리는 관찰 이벤트와 통합 |
| `to` | `to` | `god` 없음 — 우리는 `human`만 |
| `act` | `act` | 7종 동일 |
| `subject` / `body` | `payload` | 구조화 |
| `hops` | `hops` | 동일 |
| `requires_reply` | `requires_reply` | 동일. 파생 규칙 동일 |
| `needs_human` | `to:"human"` 또는 `kind:"escalation"` | 플래그 대신 수신자로 표현 |
| `created_at` | `ts` | 동일 |

MD와의 차이는 셋: (1) GOD 부재 — `to:"god"`이 없다, (2) 관찰·대화 이벤트 통합, (3) 홉 초과 시 폐기 대신 에스컬레이션.

---

## 7. 출처

- 6월 확정: 목업=계약(conclusion·투표·매칭·3점평가), 명명 이원화, 사람=최종 결정자
- 2026-08 제안: 계약 v2 봉투 (virtual-office-v2-proposal)
- Munder Difflin HIVE.md §4 메시지 스키마, §2 확정 결정 (MIT)
- Munder Difflin `src/main/hive.ts` — `HOP_CAP=12`, `normalize()` requires_reply 파생, `routeMessage()` 자기전달 차단·폐기 동작
