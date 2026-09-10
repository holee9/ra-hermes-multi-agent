# 전달 게이트 — inbox 메시지가 peer의 턴이 되는 조건

> 원천: Munder Difflin `docs/message-queue.md` (MIT). MD가 실운영에서 겪은 사고를 규칙화한 문서.
> 적용 범위: 라우터가 inbox에 파일을 넣은 **이후**, peer가 그것을 처리하기 시작하는 시점의 통제.

---

## 1. MD가 겪은 사고

인박스 알림이 터미널에 직접 쓰였을 때, 두 번째 기록자가 "프롬프트가 비었나"를 각자 판단했고, 알림 텍스트가 사람이 반쯤 쓴 문장 위에 얹혀 **하나의 뒤섞인 프롬프트로 제출**되었다.

교훈: **"이 peer가 지금 받을 수 있는가"를 판단하는 곳은 한 곳이어야 한다.**

---

## 2. 우리 구조에서의 대응

Hermes peer는 PTY가 아니라 게이트웨이 경유 세션이므로 "사람의 타이핑과 충돌"은 없다. 그러나 동형 문제가 둘 있다:

| MD 문제 | 우리 동형 |
|---|---|
| 사람 초안 위에 알림이 얹힘 | peer가 턴 실행 중일 때 새 inbox 메시지가 컨텍스트 중간에 주입됨 |
| 연속 전송이 TUI를 막음 | 연속 메시지가 한 턴에 몰려 개별 답신 의무가 뒤섞임 |

---

## 3. 게이트 조건 — **전부** 충족 시에만 전달

| 조건 | 이유 | MD 원문 대응 |
|---|---|---|
| peer 상태 `idle` | 실행 중 턴을 방해하지 않음 | agent status is `idle` |
| 자동 전달 미정지 — **또는 사람이 수동 해제** | 층 전체 일시정지 스위치 | auto-delivery not paused / manual release |
| 시작 유예 경과 | Hermes 세션 초기화 중 | past the boot grace window |
| 브레이커 레벨 `< stopped` | 격리 중 peer에 전달 안 함 | (우리 추가) |
| 직전 전달 후 **최소 간격** 경과 | 연속 투입 방지 | 4.5 s since last delivery |

MD의 4.5s는 TUI 특성값. 우리 초기값은 **턴 단위** — 직전 메시지의 처리 결과(outbox 답신 또는 `.done` 이동)가 확인된 뒤 다음 메시지. 시간 간격보다 강한 조건.

### 3.1 상태 소스 계약 — `idle`은 authoritative 소스에서만 온다 (P3-1, codex 사전 리뷰 반영)

| 항목 | 규칙 |
|---|---|
| 상태 소스 | 라우터 밖 설정(`RA_HIVE_GATE_SOURCE`, P3에서 확정)으로 주입되는 **Hermes 자체 상태 API/신호**만 authoritative. 라우터 코드에 소스 종류·주소를 하드코딩하지 않는다 |
| 상태 값 | `idle` · `busy` · `unknown`(소스가 답을 주지 않음/파싱 불가) · `stale`(마지막 확인이 `GATE_MAX_AGE`보다 오래됨) · `unavailable`(소스 미설정·미노출) |
| 전달 허용 | **`idle`일 때만.** `busy`·`unknown`·`stale`·`unavailable`은 모두 **보류** — 실패로 취급하지 않고 다음 배치에서 다시 조회한다. §4 수동 해제도 idle 조건은 우회하지 못한다(일시정지만 우회) |
| 대용 증거 금지 | outbox·도구·세션 로그의 잠잠함, inbox 파일 미소비, 시간 경과는 `idle`의 증거가 아니다(§7·§8). 긴 턴(모델 응답 대기·네트워크 대기·긴 도구 실행)은 기록 없이도 실행 중이다 |
| 조회↔전달 원자성 | 라우터 측 "조회 → inbox 기록 → 재조회"는 원자 수락이 **아니다**: 조회와 기록 사이에 턴이 시작되면 이미 진행 중인 턴에 입력이 주입되고, 사후 `busy` 확인으로는 막지 못한다. 수락은 **Hermes 수신측**에서 결정돼야 한다 — 수신측 큐가 입력을 받아 `accept`/`queued`/`reject-busy`를 반환하는 compare-and-accept 계약(P3-0 실측 대상: base.py의 active guard·`_pending_messages`·`on_processing_start`). 그 계약이 없으면 라우터는 `idle` 조회 후 **한 배치에 한 건만** 기록하고 `written`에 둔 채 `accepted`(§5.1) 확인을 기다린다. `written`은 파일 기록 단계일 뿐 수락이 아니다 |
| `accepted` 확인 | §5.1 — 세션 로그의 `id` 처리 개시 기록만. 라우터가 inbox 파일이 사라졌다는 것으로 `accepted`를 추정하지 않는다 |
| 실제 RA 진입점 (P3-0 경계, codex 확인) | 현재 RA peer는 게이트웨이 세션이 아니라 `scripts/hermes-api-server.py` `_invoke_hermes()`(770행)가 띄우는 **일회성 subprocess** `hermes -p <profile> -z <context> --skills ra-expert`(PID 3727243 서비스, `HERMES_BIN`, timeout 900)다. repo 안에서 hermes CLI를 호출하는 곳은 이 API 서버뿐이다(정적 grep). 따라서 `gateway/platforms/base.py`의 active guard·`_pending_messages`가 이 경로를 보호한다고 **가정할 수 없다**. P3-0에서 고정할 것: 실제 host/profile/entry/세션 유무, CLI `-p` 동시 실행 계약(같은 profile 동시 2건 시 세션 공유·격리 여부), 수락 주체. 이 경로가 유일한 호출자로 확인되면 API 서버 자신의 '해당 profile subprocess 실행 중' 상태가 그 경로의 authoritative 소스 후보다 |
| 한 배치 한 건의 뜻 | **속도 제한이지 원자성 보장이 아니다** — 조회 직후 턴 시작 경쟁(TOCTOU)은 수신측 직렬 수락만 없앤다. P2 참조 라우터의 inbox 파일 적재는 Hermes 입력이 **아니며** drain을 하지 않는다. 실제 입력 주입은 수신측 직렬 수락 계약 확인 전까지 보류(영구 수동 운영으로 목표를 축소하지 않고 진입점 계약 조사를 잇는다) |
| 회귀(P3-2) | `tools/hive_drain.py` + `tests/test_hive_drain.py`(16): 소스 미설정→`unavailable` 보류 · busy/unknown/garbage 보류 · 시각 없는 idle→unknown · GATE_MAX_AGE 초과→stale · 턴 간격(handled 전 보류) · 수동 해제=pause만 우회 · 유예·브레이커 · manual 선두/도착순 · 비정형 이름 무시 · accept 토큰 없으면 배치당 1건 · sink 거절은 written 아님 · CLI dry-run 무전달. 로그를 읽는 경로가 없으므로 '긴 턴 무로그'는 구조적으로 전달 불가 |

이 계약이 채워지기 전(P3-0 실측 전)에는 상태 소스가 없으므로 값은 항상 `unavailable`이고 자동 전달은 일어나지 않는다.

**P3-0 조사 지점(codex, 설치 Hermes `f8adefde` `gateway/platforms/base.py`, 수정 없음):** active-session guard·stale-owner 검사(3848~), busy 경로의 `_pending_messages` 큐잉과 `merge_pending_message_event(merge_text=True)`(3985~), `on_processing_start`(4085)·`on_processing_complete`(4388, `ProcessingOutcome`=응답 전달 결과이지 업무 완료가 아님). 설계 원칙(#2 G3): Hermes 큐·수명주기를 **재사용**하고 private dict를 외부에서 고치거나 큐를 재구현하지 않는다. 인수 항목: (a) RA peer의 실제 진입 adapter/버전 대조, (b) `accepted/started/completed` ↔ HIVE `id` 연결, (c) merge 경로에서 여러 HIVE 메시지가 개별 ack를 잃지 않음(잃으면 라우터가 한 배치에 한 건만 전달), (d) 외부 HTTP 상태 API·hook 확장 지원 여부 — 미확인이면 `unavailable`.

---

## 4. 수동 해제

층 전체 일시정지 중에도 사람이 특정 메시지를 **지금 전달**할 수 있다. 수동 해제는 **일시정지 조건만** 우회한다. idle·유예·브레이커·간격은 그대로 적용.

살에서: 정지 중 대기 메시지에 "지금 전달" 표시 → 정문 경유 `policy(action:release, ref_evt)` → 라우터가 해당 메시지에 `manual:true` 표시 후 큐 선두로.

---

## 5. 확인(ack) 규칙

전달 성공은 **peer가 메시지를 읽어 처리를 시작한 것이 확인된 뒤에만** 인정. 실패 시 메시지는 inbox에 그대로 남고 다음 비트에 재시도. 조용히 사라지지 않는다.

확인 신호: Hermes 세션 로그에 해당 `id` 처리 개시 기록, 또는 outbox에 `corr == id`인 답신 출현.

### 5.1 전달 상태는 다섯 개다 — 파일 전달 ≠ 처리 완료

| 상태 | 뜻 | 증거 | 기록 주체 |
|---|---|---|---|
| `written` | 라우터가 inbox에 파일을 썼다 | inbox 파일 존재, `log.jsonl` `delivered_to` | 라우터 |
| `accepted` | peer가 파일을 읽어 처리를 시작했다 | Hermes 세션 로그의 `id` 처리 개시 | 라우터가 세션 로그에서 확인 |
| `processing` | peer 턴 진행 중 | 세션 활동 | 라우터는 추론하지 않는다 (§7) |
| `handled` | peer가 이 메시지에 대한 의무를 마쳤다 | `requires_reply:true` → outbox 답신(`corr == id`) 출현; `inform` 등 답신 없는 메시지 → peer가 outbox에 `kind:comment, act:done, corr:id, payload.ack:true`를 **선택적으로** 남기거나, 라우터가 세션 로그의 턴 종료를 확인 | 라우터 |
| `outcome` | 업무 결과가 원장에 반영됐다 | OpenProject 코멘트/상태, `artifact` 이벤트 | OpenProject·이벤트 로그 |

- 라우터가 파일을 `inbox/.done/`으로 옮기는 것은 `handled` **확인 이후의 정리 동작**이지 완료의 증거가 아니다. 라우터 자신의 이동 기록으로 완료를 증명하지 않는다.
- 활동이 잠잠하다는 이유로 `handled`나 `idle`을 추정하지 않는다. 확인 신호가 없으면 상태는 `written`에 머문다.
- 답신 없는 `inform`의 `handled` 확인 방식(선택적 ack 이벤트 vs 세션 로그 턴 종료)은 P3에서 Hermes 실측 후 하나로 고정한다.

---

## 6. 처리 순서

inbox 내 파일명(`<ts>-<id>.json`)의 사전순 = 도착순. `manual:true`는 예외로 선두. 그 외 재정렬 없음.

---

## 7. 두 개의 큐 — 혼동 방지

| 큐 | 위치 | 내용 |
|---|---|---|
| **hive inbox** | `agents/<a>/inbox/` | 라우터가 전달했고 peer가 아직 처리 시작 안 한 메시지 |
| **Hermes 내부 큐** | Hermes 세션 | Hermes가 받았지만 아직 착수 안 한 입력 |

라우터는 **후자를 보지 못하고 추론하지 않는다.** MD 원문: *"The harness cannot see the Claude queue and never reasons about it."*

---

## 8. 미확인 사항

- Hermes 게이트웨이가 peer의 `idle` 상태를 외부에 노출하는지 — **Hermes 문서 확인 필요.** 노출하지 않으면 idle 조건을 **`unavailable`로 기록하고 자동 전달을 하지 않는다**(§3.1 — 수동 해제 §4도 idle 조건을 우회하지 못하므로, 이 상태에서는 사람이 peer에 직접 입력하는 것 외에 전달 경로가 없다). outbox·도구 로그가 잠잠하다는 것을 idle의 대용 증거로 쓰지 않는다 — 잠잠함은 실행 중 추론일 수도, 죽은 세션일 수도 있다.
- 시작 유예 시간 — Hermes 세션 기동 시간 실측 후.
