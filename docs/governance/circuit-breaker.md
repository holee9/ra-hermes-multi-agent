# 서킷 브레이커 — 조정 → 제약 → 정지

> 해결하는 결손: **D4 폭주 차단 사다리 부재** (기존 정책은 pause/resume 2단만)
> 원천: Munder Difflin `src/main/breaker.ts` — 정책 모듈 (MIT). 코드 주석에서 확인한 설계 원칙을 이식.
> 집행 주체: n8n (라우터와 별도 플로우, 동일 워킹카피). 판단 없음 — 신호 읽고 사다리 규칙 적용.
> 살의 역할: 레벨 표시(좌석 상태)만. 읽기 전용.

---

## 1. 왜 사다리인가

기존 §7 거버넌스는 예산 초과 시 `pause` 한 단계였다. 문제 둘:
- 예산에 닿기 전의 순환·오류 폭주를 잡지 못한다.
- 정지가 유일한 수단이면 정지가 너무 늦거나 너무 이르다.

MD breaker.ts의 원칙: **조정 우선, 한 비트에 한 단계씩, 절대 즉시 정지로 점프하지 않으며, 건강한 비트마다 한 단계 회복.** 그리고 `hardStop`은 기본 OFF — 없으면 사다리는 `constrained`에서 멈추고 절대 죽이지 않는다.

---

## 2. 레벨과 행동

```
healthy ──trip──▶ steering ──trip──▶ constrained ──trip(+hardStop)──▶ stopped
   ▲                 │                  │                                │
   └── 건강 비트 ────┴────── 건강 비트 ─┘                    사람 재개만
```

| 레벨 | 발생 행동 (레벨 **상승 시 1회**) | peer에게 | 살 표시 |
|---|---|---|---|
| `healthy` | 없음 | — | 정상 |
| `steering` | `policy(action:steer, target_actor, reason)` → 해당 peer inbox | "순환 중. 반복 멈추고 시도 요약 보고" | 좌석 앰버 |
| `constrained` | `policy(action:constrain, ...)` + 라우터가 해당 actor의 신규 `request`/`propose` 발신을 `.held/`에 보류 | "범위 축소. 진행 중 스레드만" | 좌석 앰버 점멸 |
| `stopped` | `policy(action:stop, ...)` + `escalation(reason:breaker)` → human | "정지. 재개는 사람" | 좌석 적색 |

행동은 **레벨이 오를 때만** 발화한다. 같은 레벨 유지 중 매 비트 재발송하지 않는다 (MD: *"durable steer message isn't re-sent every beat"*).

---

## 3. 트립 신호

세 원천을 집계한다. 값은 MD 기본값을 **참고값**으로 병기하되 우리 값은 미확정.

| 신호 | 측정 | MD 기본값 | 우리 초기값 |
|---|---|---|---|
| 반복 도구 호출 | 동일 도구+동일 입력 연속 횟수 | 8 | 미확정 — Hermes 도구 로그에서 실측 |
| 오류 폭주 | 진행 없는 연속 api_error/재시도 | 5 | 미확정 |
| 토큰 속도 | **연속 누적 샘플의 차분** Δout/Δt | 60,000 out tok/min | 미확정. GX10 Qwen3 처리량 기준으로 재산정 |
| 무진행 | 조율 파일 mtime + 작업 디렉토리 mtime 모두 정지, **연속 2비트** | 2비트 (300s 창) | 동일 채택 |

핵심 규율 셋 — 코드에서 확인:
1. **속도는 차분이다.** 단일 샘플을 증분으로 취급하지 않는다. 누적 스냅샷 두 개의 차이만 본다.
2. **무진행은 두 질문이다.** "조율 진행"(메시지 파일)과 "작업 진행"(작업 디렉토리)은 다르다. 20분간 파일 편집·빌드·커밋만 하고 hive 메시지를 안 보낸 peer는 무진행이 아니다. 두 신호 모두 정지일 때만 트립.
3. **1비트 블립은 트립이 아니다.** 무진행은 연속 2비트를 요구한다.

---

## 4. 예산 — 무엇을 셀 것인가

MD가 #189에서 배운 것: 캐시 읽기 토큰은 요청 횟수에 비례해 자라며 peer의 실제 작업량이 아니다. 두 peer가 4M 상한을 넘은 행에서 캐시 읽기가 98.6~99.2%였다.

| 용도 | 계산 |
|---|---|
| **예산 판정** | `work_tokens = in + out + cache_creation` (cache_read 제외) |
| **비용 표시** | `total_tokens = in + out + cache_read + cache_creation` |

계약 v2.1 `cost` 필드는 현재 `in_tokens`·`out_tokens`만 있다. **`cache_read`·`cache_creation` 추가 필요** — additive-only이므로 v2.1 내 추가 가능. Hermes가 이 값을 노출하는지 **확인 필요**.

---

## 5. 회복

건강한 비트(어떤 트립도 없음)마다 **한 단계 하강**. `stopped`는 예외 — 사람의 `policy(action:resume)` 정문 경유만.

`stopped` → `resume` 시 `healthy`로 직행하지 않고 `steering`에서 재시작한다. 재개 직후 재폭주를 한 단계 빨리 잡기 위함. (MD에 없는 우리 추가.)

---

## 6. hardStop

기본 **OFF.** OFF면 사다리는 `constrained`가 최고 단계이며 `stopped`에 도달하지 않는다.

ON으로 바꾸는 조건: 파일럿 기간 `constrained`가 발생했으나 peer가 제약 안에서 계속 폭주한 사례가 **관찰**된 뒤. 관찰 없이 ON 금지.

`stopped`의 집행은 **Hermes 프로세스 kill이 아니다.** 라우터가 해당 actor의 outbox를 읽지 않고 inbox에 넣지 않는 **격리**다. 프로세스 생사는 infra peer의 영역.

---

## 7. 비트

| 항목 | 값 |
|---|---|
| 비트 주기 | 60s (초기값) |
| 진행 창 | 300s |
| 대상 | registry `status:active` 전원 |
| 상태 저장 | `hive/.breaker/<actor>.json` — 라우터 관리, 커밋 대상 |

비트는 `log.jsonl`의 `cost` 필드와 Hermes 도구 로그를 읽는다. **`log.jsonl`에 `cost`가 없는 이벤트가 많으면 속도 트립은 작동하지 않는다** — Phase 1에서 cost 기록률을 먼저 확인.

---

## 8. 정문·창문과의 관계

- 브레이커는 뼈대 내부다. 살은 `policy` 이벤트를 `log.jsonl`에서 읽어 좌석 색만 바꾼다.
- 사람의 `resume`은 정문(n8n webhook / Telegram / 오피스 컴포저) 경유 → `policy(action:resume)` 이벤트 → 브레이커 상태 갱신. 살이 직접 상태를 쓰지 않는다.

---

## 9. 불변 원칙 정합

| 원칙 | 정합 |
|---|---|
| 3 중앙 두뇌 없음 | 브레이커는 판단하지 않는다. 임계와 사다리 규칙만 |
| 4 사람 = 최종 결정자 | `stopped` 해제는 사람만. `hardStop` 기본 OFF |
| 7 정직한 표현 | 살은 실제 레벨만 표시 |
| 9 config-as-code | 임계값은 `hive/.breaker/config.json`, PR로 변경 |
