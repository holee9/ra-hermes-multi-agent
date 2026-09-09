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
[커밋]  git add -A && git commit  (재시도 + 백오프, 단일 커미터)
```

---

## 2. 정규화 규칙

| 필드 | 채우는 법 |
|---|---|
| `v` | `"2.1"` |
| `id` | `evt_<UTC YYYYMMDDTHHMMSS>_<4hex>` |
| `ts` | 처리 시각, ISO-8601 +09:00 |
| `actor` | outbox 디렉토리의 actor ID. peer가 쓴 값은 **덮어쓴다** (위장 방지) |
| `act` | 없으면 kind의 기본 act (계약 §2) |
| `requires_reply` | peer가 명시하지 않으면 `act ∈ {request, query, propose}` |
| `hops` | `corr` 없으면 0. 있으면 `log.jsonl`에서 `corr` 이벤트를 찾아 `hops + 1`. 못 찾으면 0 + `policy` 경고 |
| `conversation` | `corr` 있으면 원인의 값 상속. 없으면 `conv_<wp>_<kind>_<4hex>` |

MD `normalize()`와 동일 논리. 차이: `to` 기본값이 MD는 `god`, 우리는 **없음** — `to` 없는 outbox 메시지는 관찰 이벤트로 log에만 기록하고 전달하지 않는다.

---

## 3. 검증 규칙 (스키마 외)

| 규칙 | 실패 시 |
|---|---|
| `to == actor` (자기 전달) | 거부 |
| 종결형 act에 `requires_reply: true` | 거부 |
| `broadcast`에 `requires_reply: true` | `false`로 강제 후 통과 + 경고 |
| `corr`가 가리키는 이벤트의 `act`가 종결형 | 거부 — 종결형에 답신 금지 |
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

---

## 7. 거절 교착 감지

같은 `conversation`에서 `act:refuse`가 **서로 다른 두 actor**로부터 각 1회 이상 → `escalation(reason:"refuse-deadlock")`. 이후 그 conversation의 신규 메시지는 사람 응답 전까지 `.held/`에 보류.

---

## 8. 커밋

- 라우터 처리 배치 1회 = 커밋 1회. 메시지마다 커밋하지 않는다.
- 메시지: `hive: route <n> msgs (<actor>→<to> ...)` 
- `index.lock` 존재 시: 5초 대기 → 재시도 3회 → 실패 시 `policy(action:throttle, reason:"git-lock")` + 다음 배치에서 재시도. stale lock(>60s, 프로세스 없음) 정리.
- 이 라우터 외 어떤 프로세스도 `ra-hive`에 커밋하지 않는다. peer 컨테이너에는 git 바이너리를 두지 않는다.

---

## 9. 인박스 → peer 전달 (drain gate)

라우터가 inbox에 파일을 넣는 것과, peer가 그것을 **읽어 처리하기 시작하는 것**은 별개다. 후자는 `docs/governance/delivery-gate.md`.

---

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

폴링 주기 15s는 초기값. `log.jsonl` 지연 허용치는 살의 재생 특성상 수 초면 충분하다(원칙 7 — 실시간 아닌 기록 재생).

---

## 11. 관찰 항목 (Phase 1 실측)

| 항목 | 이유 |
|---|---|
| 정상 스레드 hops 분포 | `HOP_CAP` 설정 |
| 배치당 메시지 수 | 폴링 주기 조정 |
| git commit 소요·lock 충돌 빈도 | 단일 커미터 검증 |
| undeliverable 발생률 | registry 정합성 |
| Raspi5P CPU/메모리 증분 | 호스트 적합성 |
