# 살 — 아바타 상태 기계와 이벤트 매핑

> 원천: Munder Difflin `SPEC.md` §4 (Sims 메타포 — 이벤트를 행동으로), `MEMORY_GRAPH_SPEC.md` §4 (화행 색상)
> 적용: 살은 `log.jsonl`만 읽는다(원칙 6). 아래 매핑은 **읽은 이벤트 → 화면 상태** 변환 규칙이며, 살은 어떤 상태도 뼈대에 쓰지 않는다.

---

## 1. 지배 원칙 — SPEC.md에서

> *"Every animation should actually tell you something you didn't know. If walking-to-the-shelf doesn't convey 'is reading a file' faster than a text label, we built a toy."*

우리 원칙 7(정직한 표현)과 같은 결론이다. 규칙: **이벤트 없는 애니메이션 없음. 정보 없는 애니메이션 없음.**

---

## 2. 상태

```
idle ─────case_open/handoff(to=나)─────▶ alert
alert ────matching/comment/vote_cast───▶ working(station)
working ──artifact────────────────────▶ carrying(→desk) ──▶ idle
working ──vote_call───────────────────▶ meeting(회의실)
meeting ──vote_result─────────────────▶ idle
any ──────to=human 발신───────────────▶ waiting(우편함)
any ──────policy(steer)───────────────▶ working (좌석 앰버)
any ──────policy(constrain)───────────▶ working (좌석 앰버 점멸)
any ──────policy(stop)────────────────▶ blocked (좌석 적색, 정지)
any ──────infra(level=down, host=내 host)▶ ghost ──30s──▶ 반투명
idle ─────absence(gap=내 역할 근접)────▶ (빈 좌석 카운터 +1)
```

MD와의 차이: MD는 Claude Code 훅(`PreToolUse` 등)이 원천. 우리는 **계약 v2.1 이벤트**가 원천. 훅 수준 도구 이벤트는 우리 계약에 없으므로 "파일 선반·터미널 스테이션" 같은 도구별 스테이션은 채택하지 않는다.

---

## 3. 스테이션 — kind → 위치

| kind (관찰) | 스테이션 | 정보 |
|---|---|---|
| `matching`, `comment` | 자기 책상 | 판단 중 |
| `handoff` (발신) | 수신자 책상으로 걸어감 → 봉투 전달 → 복귀 | 이관 |
| `vote_call` | 관련 actor 전원 회의실 이동 | 투표 소집 |
| `vote_result` | 회의실 → 각자 책상 | 종결 |
| `artifact` | 자기 책상 → 파일 캐비닛 → 복귀 | 산출물 발생 |
| `to == human` | 우편함 앞 대기 (손 흔듦) | 사람 입력 필요 |
| `escalation` | 우편함 + 배지 | 긴급 |
| `infra` | 2F 해당 호스트 좌석 카드 갱신 | 헬스 |
| `absence` | 빈 좌석 카운터 | 부재 누적 |
| `hire_proposal` | 빈 좌석에 제안 카드 | 채용 제안 |

---

## 4. 봉투 — 대화 이벤트의 시각화

`to`가 있는 모든 이벤트 = 봉투 1개가 `actor` 책상에서 `to` 책상으로 비행. `broadcast`는 발신자에서 전원으로 팬아웃(가늘게).

**봉투 색 = `act`.** MEMORY_GRAPH_SPEC §4.1의 원칙 — 그래프 엣지와 바닥의 봉투가 같은 시각 언어.

| act | 색 (제안) | 의미 |
|---|---|---|
| `request` | 앰버 | 행위 요청 |
| `query` | 하늘 | 질의 |
| `propose` | 보라 | 제안 |
| `inform` | 회백 | 통지 (종결) |
| `agree` | 청록 | 수락 (종결) |
| `refuse` | 적갈 | 거절 (종결) |
| `done` | 녹색 | 완료 (종결) |

종결형 4종은 채도를 낮춰 "이 스레드는 여기서 끝난다"가 색으로 읽히게 한다.

`hops` 표시: 봉투에 작은 숫자. 상한 근접(예: 상한의 80%)에서 봉투 테두리 점멸 — 사람이 개입 시점을 미리 안다.

---

## 5. 관계 그래프 뷰 (타임라인 뷰 보강)

MEMORY_GRAPH_SPEC를 축소 이식:
- 노드 = actor (좌석 색), `human`·`broadcast`는 의사 노드.
- 엣지 = 정렬된 (actor, to) 쌍당 1개, 굵기 = 메시지 수, 색 = 최근 `act`.
- 레이아웃: 힘 기반, 결정적 시드, 드래그 고정. **의존성 추가 없이** 50줄 시뮬레이션.
- 렌더: **SVG.** MEMORY_GRAPH_SPEC §7의 판정 그대로 — 100노드 미만 정적 데이터 뷰는 SVG가 맞다. Pixi는 바닥에만.
- 우리 추가: `escalation` 엣지는 `human`으로 향하는 굵은 적색 — 사람이 어디서 호출됐는지 한눈에.

이 뷰는 **감사 리플레이(§11)의 구조적 보조**다. 시간축이 "언제"를, 그래프가 "누가 누구와"를 답한다.

---

## 6. 사람 아바타

- 좌석 앞에서 Space → 해당 actor 지정 컴포저. 발신은 정문(n8n webhook) 경유만.
- 우편함에 대기 봉투 있으면 사람 아바타 머리 위 배지 수 표시.
- 사람의 `eval3` 발화 = 사람 아바타가 대상 actor 책상으로 걸어가 별점 부착. 실제 이벤트이므로 정직.

---

## 7. 채택하지 않은 MD 시각 요소

| 요소 | 사유 |
|---|---|
| 도구별 스테이션(파일 선반·터미널·웹 포털·MCP 코너) | 우리 계약에 도구 수준 이벤트 없음. 추가하면 계약 팽창 |
| GOD 좌석 확대(1.4×)·이중 테두리 | GOD 없음 |
| 라이브 터미널 패널 | 뼈대는 살의 존재를 모른다. PTY 노출은 관찰자 원칙 위반 |
| LimeZu 타일셋 | 별도 라이선스. Kenney CC0 경로 유지 |

---

## 8. 목업 데이터

`mock/events-v2.1.jsonl` — 계약 v2.1 준수 샘플 40건. `DATA_SOURCE=mock`에서 재생해 위 상태 기계를 검증한다. 원칙 8(목업=계약)의 v2.1 갱신.
