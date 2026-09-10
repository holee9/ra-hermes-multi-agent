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

- Hermes 게이트웨이가 peer의 `idle` 상태를 외부에 노출하는지 — **Hermes 문서 확인 필요.** 노출하지 않으면 idle 조건을 **`unavailable`로 기록하고 자동 전달을 하지 않는다**(수동 해제 §4만 가능). outbox·도구 로그가 잠잠하다는 것을 idle의 대용 증거로 쓰지 않는다 — 잠잠함은 실행 중 추론일 수도, 죽은 세션일 수도 있다.
- 시작 유예 시간 — Hermes 세션 기동 시간 실측 후.
