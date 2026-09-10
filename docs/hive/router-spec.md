# 라우터 명세 (n8n)

> 역할: MD의 "메인 프로세스 라우터"에 해당. 판단 없는 기계. GOD 기능 중 **이송·집계·에스컬레이션**만 맡는다. 조정(adjudication)은 맡지 않는다 — 그것은 사람이다.
> 호스트: Raspi5P (n8n 기가동). 파일 접근은 Gitea 클론 워킹카피.
> 원천: Munder Difflin `src/main/hive.ts` `routeMessage()`·`deliver()`·`normalize()` (MIT)

---

## 1. 흐름

```
[감시]  agents/*/outbox/*.json  (폴링, .tmp-* 제외)
   │
   ▼
[정규화]  v · id · ts · actor · hops · requires_reply · conversation 채움
   │
   ▼
[검증]  schema v2.1 + 규칙 (§3)  ── 실패 → outbox/.rejected/ + log(kind:policy, action:refuse-invalid)
   │
   ▼
[홉 가드]  hops > HOP_CAP → escalation(hop-cap) → human inbox
   │
   ▼
[수신자 해석]  to → 대상 목록 (§4)
   │
   ▼
[전달]  각 대상 inbox/ 에 원자적 기록
   │
   ▼
[기록]  log.jsonl 에 append — **실제 전달된 대상만**
   │
   ▼
[이동]  outbox/<f> → outbox/.sent/<f>
   │
   ▼
[커밋]  git add <이번 배치가 만든 경로만> && git commit  (재시도 + 백오프, 단일 커미터, §8)
```

---

## 2. 정규화 규칙

| 필드 | 채우는 법 |
|---|---|
| `v` | `"2.1"` |
| `id` | `evt_<UTC YYYYMMDDTHHMMSS>_<4hex>`. 충돌 시 재발급(§2.1) |
| `ts` | 처리 시각, ISO-8601 +09:00 |
| `workspace` | `registry/actors.json`의 해당 actor `workspace`. peer 값 무시 |
| `actor` | outbox 디렉토리의 actor ID. peer가 쓴 값은 **덮어쓴다** (위장 방지) |
| `act` | 없으면 kind의 기본 act (계약 §2) |
| `requires_reply` | peer가 명시하면 **보존**, 생략하면 `act ∈ {request, query, propose}`로 파생. 명시값이 §3 규칙에 어긋나면 거부 (`hive/PROTOCOL.md` §2와 동일) |
| `hops` | `corr` 없으면 0. 있으면 `log.jsonl`에서 `corr` 이벤트를 찾아 `hops + 1`. **못 찾으면 거부** (§3 `unknown-corr`) — 0으로 재시작하면 홉 상한을 우회할 수 있다 |
| `conversation` | `corr` 있으면 원인의 값 상속. 없으면 `conv_<wp>_<kind>_<4hex>` |
| `null` 필드 | raw 메시지의 `"corr": null`, `"conversation": null` 등 null 값은 **필드 자체를 제거**한다. 스키마는 null을 허용하지 않는다 |

**raw ↔ 정규화 경계.** peer가 outbox에 쓰는 것은 *raw 메시지*(위 표의 필드가 비어 있어도 됨)이고, 스키마 v2.1은 **정규화 이후의 이벤트**에만 적용한다. `log.jsonl`과 inbox에는 정규화 이벤트만 기록된다. 정규화 책임은 라우터에 있다.

MD `normalize()`와 동일 논리. 차이: `to` 기본값이 MD는 `god`, 우리는 **없음** — `to` 없는 outbox 메시지는 관찰 이벤트로 log에만 기록하고 전달하지 않는다.

### 2.1 id 충돌

`id`의 4hex는 랜덤이므로 전역 유일을 가정하지 않는다. 발급 직후 `log.jsonl`·당일 inbox 파일명과 대조해 충돌이면 재발급한다. 전달 재시도 시에는 **처음 발급한 id를 보존**한다(수신자별 중복 전달 방지 키).

---

## 3. 검증 규칙 (스키마 외)

| 규칙 | 실패 시 |
|---|---|
| `to == actor` (자기 전달) | 거부 |
| 종결형 act에 `requires_reply: true` | 거부 |
| `broadcast`에 `requires_reply: true` | `false`로 강제 후 통과 + 경고 |
| `corr`가 가리키는 이벤트의 `act`가 종결형 | 거부 — 종결형에 답신 금지 |
| `corr`가 `log.jsonl`에 없음 (`unknown-corr`) | 거부 — 미확인 원인으로 hops를 0으로 재시작하지 않는다 |
| `corr`가 자신보다 뒤에 기록된 이벤트 | 거부 — 원인은 선행해야 한다 |
| `to`가 registry에 없음 | §4 undeliverable |
| `to`의 `status != active` | §4 undeliverable |

거부된 메시지는 `outbox/.rejected/`로 이동하고 `log.jsonl`에 `kind:"policy", payload.action:"refuse-invalid", payload.reason:<규칙>`을 기록한다. peer의 다음 인박스에 사유를 `inform`으로 넣는다.

---

## 4. 수신자 해석

```
to == "human"      → human inbox (별도: agents/human/inbox/, 사람은 살·Telegram·OpenProject로 읽음)
to == "broadcast"  → registry.actors 중 status==active, id != actor
to == <actor_id>   → [to] (자기 자신 제외는 §3에서 이미 거부)
```

**undeliverable** (수신자 없음·비활성): MD는 GOD으로 바운스한다. 우리는 **사람으로 바운스**한다 — `escalation(reason:"undeliverable", ref_evt:<id>)`을 human inbox에 넣고, 원 메시지는 `.rejected/`에 보존. **조용히 사라지는 메시지는 없다.**

---

## 5. 전달 기록 원칙

MD 코드 주석 그대로: *"의도가 아니라 실제 전달된 대상을 기록한다 — 바운스·폐기된 메시지가 전달된 것으로 읽히지 않도록."*

`log.jsonl` 항목의 `payload.delivered_to: [...]`에 실제 inbox 기록에 성공한 actor만 넣는다. `broadcast`가 5명 중 3명에게만 성공하면 3명만 기록하고 나머지는 `undeliverable` 에스컬레이션.

**확정 시점.** 원본 메시지의 log 항목은 **모든 대상이 전달 성공 또는 human escalation으로 확정된 뒤 한 번만** 쓴다. 그 전까지 진행 상태(성공 대상·실패 대상·발급된 파생 이벤트)는 `.router/journal/<id>.json`에만 있다. 이유: 부분 성공 시점에 log를 먼저 쓰면, escalation 실패로 원본이 보류됐다가 복구 후 재실행에서 추가 전달된 결과가 감사 로그에 반영되지 않는다(PR #151 리뷰). 확정된 항목은 `payload.delivered_to`(성공)와, 사람에게 넘긴 대상이 있으면 `payload.undeliverable`(escalation의 `ref_evt`로 연결)을 함께 가진다. log는 append-only이며 항목을 갱신하지 않는다.

**영속 순서(리뷰 4차).** 확정된 결정과 기록할 log 항목 자체를 먼저 저널에 쓴다(`step=finalizing`, `final={archive, event, delivered, undeliverable}`). 그 다음 log에 멱등 append(`step=audited`) → outbox 이동 → cursor 갱신 → `step=archived`. 어느 지점에서 죽어도 재시작은 `finalizing`/`audited` 저널을 **route 평가보다 먼저** 읽어 그 final만으로 완결하며, route·deliver·escalate를 다시 평가하지 않는다(복구된 대상에게 재전달하지 않음). outbox 파일이 이미 옮겨졌는데 cursor 전에 죽은 저널(orphan)은 `run()` 시작 시 스윕으로 완결한다. 파생 이벤트(policy/comment/escalation)의 전달 결과(`payload.delivered_to`)도 log append 전에 저널의 `derived`에 고정한다 — 재실행은 고정된 결과를 그대로 기록하며 복구된 inbox에 재전달하지 않는다. 확정 저널의 마무리는 `HOP_CAP` 미설정(held) 재평가보다 먼저 처리한다: 신규 전달만 보류된다.

---

## 6. 홉 가드

```
if hops > HOP_CAP:
    write escalation {
      kind: "escalation", to: "human", act: "request", requires_reply: true, hops: 0,
      payload: { reason: "hop-cap", ref_evt: <id>, conversation: <conv>, hops_reached: <hops> }
    } → human inbox
    move original → outbox/.rejected/
    log both
```

**폐기하지 않는다.** MD `routeMessage()`는 `kind:'drop'`으로 폐기하지만, 우리는 12번 오간 스레드를 사람이 봐야 할 것으로 취급한다(원칙 4).

`HOP_CAP` 초기값: **미확정.** n8n 환경변수 `RA_HIVE_HOP_CAP`으로 주입. 운영 첫 2주 관찰 후 설정. 관찰 항목: 정상 종결 스레드의 최대 hops 분포.

**미설정 시 동작:** `RA_HIVE_HOP_CAP`이 없으면 라우터는 `to`가 있는 대화 이벤트를 **전달하지 않는다** (관찰 이벤트만 `log.jsonl`에 기록). 상한 없는 자동 대화는 열지 않는다. P1·P2 테스트는 테스트 전용 값을 명시 주입한다.

---

## 7. 거절 교착 감지

같은 `conversation`에서 `act:refuse`가 **서로 다른 두 actor**로부터 각 1회 이상 → `escalation(reason:"refuse-deadlock")`. 이후 그 conversation의 신규 메시지는 사람 응답 전까지 `.held/`에 보류.

참조 구현 동작(P2): 교착을 확정한 두 번째 refuse는 **전달하고** 같은 배치에서 escalation(`payload.refusers`)을 사람 inbox에 기록한다(escalation 실패 시 원본 보류·재시도, 중복 전달 없음). 같은 actor의 반복 refuse는 교착이 아니다. 보류 판단은 `log.jsonl`을 conversation 순서로 읽어 결정한다: refuse-deadlock escalation 이후 그 conversation의 non-human 메시지는 `outbox/.held/`로 이동, `actor:human` 이벤트가 기록되면 보류 해제 + refuse 집계 초기화. 해제된 conversation의 `.held/` 파일은 다음 배치 시작 시 outbox로 되돌려 정상 처리한다.

---

## 8. 커밋

- 라우터 처리 배치 1회 = 커밋 1회. 메시지마다 커밋하지 않는다.
- **stage는 경로 지정으로만.** `git add -A`는 금지 — 신규 peer의 미처리 outbox, 사람이 편집 중인 `registry/*`·`identity.md`까지 라우터 커밋에 섞인다. 이번 배치가 만든 파일(inbox 기록, `.sent/`·`.rejected/` 이동, `log.jsonl`, `cursor.json`)만 `git add <path>`로 stage한다.
- 메시지: `hive: route <n> msgs (<actor>→<to> ...)` 
- `index.lock` 존재 시: 5초 대기 → 재시도 3회 → 실패 시 `policy(action:throttle, reason:"git-lock")` + 다음 배치에서 재시도. stale lock(>60s, 프로세스 없음) 정리.
- 이 라우터 외 어떤 프로세스도 `ra-hive`에 커밋하지 않는다. peer 컨테이너에는 git 바이너리를 두지 않는다.

---

## 9. 인박스 → peer 전달 (drain gate)

라우터가 inbox에 파일을 넣는 것과, peer가 그것을 **읽어 처리하기 시작하는 것**은 별개다. 후자는 `docs/governance/delivery-gate.md`.

---

## 9.1 참조 구현 (P2)

`tools/hive_router.py` — 이 명세의 §1~§8을 Python으로 옮긴 **격리 참조 구현**. n8n Code 노드로 이식(P4)할 때 동작 기준이 된다. dry-run이 기본(`--execute` 없이는 무쓰기), `.router/journal/<id>.json`에 단계별 진행을 먼저 기록해 재시작 시 중복 없이 이어가며, git 커밋은 하지 않고 stage 경로 목록만 반환한다. 검증: `python3 -m pytest tests/test_hive_router.py`.

## 10. n8n 노드 구성 (제안)

| 순번 | 노드 | 역할 |
|---|---|---|
| 1 | Schedule Trigger (15s) | 폴링 시작 |
| 2 | Execute Command `find agents/*/outbox -maxdepth 1 -name '*.json' ! -name '.tmp-*'` | 대기 메시지 수집 |
| 3 | Code (JS) — normalize + validate | §2·§3 |
| 4 | IF hops > cap | §6 분기 |
| 5 | Code — resolve targets | §4 |
| 6 | Execute Command — atomic write to inbox | 전달 |
| 7 | Code — build log entries (delivered_to 실측) | §5 |
| 8 | Execute Command — append log.jsonl, mv .sent, git commit | §8 |
| 9 | IF escalation exists → Telegram send | 사람 알림 |

폴링 주기 15s는 **테스트 전용 기본값**이며 운영값은 미확정이다(이슈 #150 "미확정" 항목과 동일 취급). `log.jsonl` 지연 허용치는 살의 재생 특성상 수 초면 충분하다(원칙 7 — 실시간 아닌 기록 재생). 운영 상수(`HOP_CAP`·폴링·브레이커 임계)는 P3/P4에서 사람이 승인한 값으로만 주입한다.

---

## 11. 관찰 항목 (Phase 1 실측)

| 항목 | 이유 |
|---|---|
| 정상 스레드 hops 분포 | `HOP_CAP` 설정 |
| 배치당 메시지 수 | 폴링 주기 조정 |
| git commit 소요·lock 충돌 빈도 | 단일 커미터 검증 |
| undeliverable 발생률 | registry 정합성 |
| Raspi5P CPU/메모리 증분 | 호스트 적합성 |
