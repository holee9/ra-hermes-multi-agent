# 가상 오피스 (살) — MVP 설계 계획

> RA 전문가 시스템(뼈대)의 활동 기록을 픽셀 캐릭터 동작으로 시각화하는 웹 대시보드.
> 뼈대와 독립 개발하며, 접점은 단방향 데이터 계약 하나. 뼈대는 시각화의 존재를 모른다.

---

## 1. 원칙

- **관찰자 구조**: 살은 뼈대 활동을 읽기만 한다. 운영에 개입하지 않는다.
- **기록 재생**: 실시간 시뮬레이션이 아니라, 쌓인 활동 이벤트를 시간순 재생하는 플레이어. (라이브는 후속 — 같은 배열을 폴링 갱신)
- **[2026-06-21 갱신] 관측 모델 전환 완료**: 재생 메타포(플레이어) 폐지 → read-only 관측. 과거는 정적 로그(시간순, 애니메이션 없음), 새 이벤트만 실시간 애니메이션. Heat Map 목업→실데이터(`matched` 이벤트 region×confidence 집계). 모니터링 시스템은 있는 그대로 관측 — 활동 없으면 조용한 게 정상 신호.
- **[2026-06-24 갱신] 실제업무 대시보드 전환 ([#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81))**: 어댑터가 `metadata.record_type` 기반 매핑 추가 — `daily_growth_case`→`growth_case`(RA 일일 학습), `score_given`(사람 KB-eval 평가)을 기존 `activity_log`(메일)와 함께 표시. 메일 의존성 탈피 — 메일이 안 와도 학습 루프가 살아 있으면 오피스가 움직인다. 하단 기록창 확대(상단 폭 정렬·높이 96→220px) + **클릭 상세 패널**(행 클릭 시 소스·도메인·점수·평가차원 표시)로 CLI 없이 이력 파악. 새 이벤트 실시간 반응은 사용자 브라우저로 검증 완료.
- **목업 = 계약**: 뼈대 출력 형태를 목업으로 미리 고정. 연동 시 데이터 소스만 목업→Honcho 교체.
- **독립 배포**: 비설치형 웹앱. Docker 단일 컨테이너. 배포 PC는 추후 지정.

---

## 2. 데이터 계약 (목업 스펙)

살이 읽는 단위 = **활동 이벤트**. 이벤트 1개 → 캐릭터 동작 1개.

```json
{
  "events": [
    {"ts":"2026-05-28T10:32:00+09:00","type":"mail_received","actor":"system","payload":{"region":"US","subject":"510(k) follow-up"}},
    {"ts":"2026-05-28T10:32:05+09:00","type":"matched","actor":"ra_us","payload":{"wp":"WP-123","confidence":0.91,"existing":true}},
    {"ts":"2026-05-28T10:32:40+09:00","type":"comment_added","actor":"ra_us","payload":{"wp":"WP-123","note":"진행현황 반영"}},
    {"ts":"2026-05-28T10:33:00+09:00","type":"transition_proposed","actor":"ra_us","payload":{"wp":"WP-123","to":"review"}},
    {"ts":"2026-05-28T14:00:00+09:00","type":"vote_opened","actor":"infra_gx10","payload":{"topic":"load_high"}},
    {"ts":"2026-05-28T14:00:30+09:00","type":"vote_cast","actor":"infra_t3610","payload":{"topic":"load_high","vote":"defer"}},
    {"ts":"2026-05-28T14:01:00+09:00","type":"vote_result","actor":"system","payload":{"topic":"load_high","result":"defer"}},
    {"ts":"2026-05-28T15:00:00+09:00","type":"score_given","actor":"human","payload":{"target_event":"matched","score":3}}
  ]
}
```

**필드 의미**: `ts`=재생 순서, `actor`=캐릭터, `type`=동작, `payload`=말풍선/상태 내용.
이 형태가 뼈대 출력 명세이자 살 입력 명세다. 양쪽이 이 형태를 기준으로 만든다.

> **[2026-06-24] 데이터 소스 매핑 ([#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81))**: 살의 어댑터(`virtual-office-honcho-adapter.js`)는 Honcho 메시지를 위 이벤트 형태로 변환한다. 매핑 기준 = `metadata.record_type` / `metadata.type`:
> - `daily_growth_case` → `growth_case` 이벤트 (구조는 `metadata`에서 조립 — content는 사람이 읽는 텍스트)
> - `score_given` → `score_given` 이벤트 (자기서술적 content JSON 파싱)
> - `activity_log` → content JSON의 `type` 그대로 (mail_received·matched·comment_added·...)
>
> 이벤트 형태 자체는 불변(목업=계약). 변한 것은 어댑터의 소스 매핑뿐이다.

---

## 3. 캐릭터(actor) 목록 — 뼈대 구성과 동일 + 살 전용 이름

뼈대는 기계적 actor ID(불변·시스템 전용), 살은 사람 이름 + 직책(사람이 보는 조직도). 이름은 살의 매핑에만 존재하고 뼈대는 모른다(단방향). 이름 변경 시 이 매핑만 수정. **파일럿 작명** — 불편하면 교체.

상세 조직도·확장 규칙은 `virtual-office-org-chart.md` 참조.

| actor ID | 애칭(오피스 호칭) | 직책 | 구역 |
|---|---|---|---|
| ra_us | **Mike** (Michael) | 미국 RA 전문가 (FDA 510(k)) | 업무 |
| ra_eu | **Theo** (Theodore) | 유럽 RA 전문가 (CE MDR) | 업무 |
| ra_kr | **Sam** (Samuel) | 한국 RA 전문가 (MFDS/KGMP) | 업무 |
| op_manager | **Margot** | 사안 담당 (OpenProject WP 추적·반영) | 업무 |
| n8n_manager | **Olly** (Oliver) | 자동화 담당 (n8n 워크플로우) | 업무 |
| infra_t3610 | **Finn** | 인프라 (T3610) | 인프라 |
| infra_gx10 | **Leo** | 인프라 (GX10) | 인프라 |
| infra_rpi | **Gus** | 인프라 (라즈베리파이) | 인프라 |
| human | (사용자) | 최종 결정자 | 관리자 시점 |
| system | — | 시스템 이벤트 | — |

> 업무 구역 / 인프라 구역 분리 = 두 Honcho workspace 격리의 시각적 표현.
> 정식/애칭 짝: 정식은 공식 리포트, 애칭은 오피스 캐릭터 라벨.

---

## 4. 동작 매핑 (type → 캐릭터 동작)

| type | 동작 |
|---|---|
| mail_received | 봉투가 region의 RA 책상에 떨어짐 |
| matched | 해당 RA 읽기 애니메이션 + 신뢰도 말풍선 |
| comment_added | op_manager에게 걸어가 쪽지 전달 → 칸반 카드 부착 |
| transition_proposed | 카드 위 "리뷰?" 말풍선 (사람 승인 대기) |
| vote_opened | 인프라 구역 회의종 → 셋 테이블에 모임 |
| vote_cast | 각 인프라 캐릭터 표 카드 제출 |
| vote_result | 인프라→업무 구역으로 알림 종이 이동 (브릿지 시각화) |
| score_given | human이 대상 이벤트에 3점 도장 |
| growth_case | 해당 RA 학습 애니메이션 + "📖 도메인" 말풍선 (규제 문서 학습, daily-growth) |
| (완료, 후속) | human 전용 도장. 그전엔 카드가 완료구역 못 넘어감 (고정 규칙의 시각적 강제) |

---

## 5. MVP 최소 장면

풀 세트가 아니라 **한 줄기**부터: `mail_received → matched → comment_added`.
= "메일 들어와 미국 RA가 매칭해 칸반에 반영"하는 단일 흐름.
이 흐름이 재생되면 "뼈대 활동 → 캐릭터 동작" 연결이 증명된다.
이후 확장: 투표 장면(vote_*) → 평가 장면(score_given) → 완료 게이트.

---

## 6. 기술·배포

- **렌더링**: 브라우저 2D(Phaser류) + 이벤트 타임라인 재생 플레이어. (검증된 기존 패턴)
- **구조**: 정적 웹 + 목업 JSON. 본질은 이벤트 배열 시간순 재생기.
- **배포**: Docker 단일 컨테이너. `DATA_SOURCE` 환경변수로 목업/Honcho 전환.
- **배포 PC 조건**: 상시 가동 + (연동 시) Honcho(T3610) 네트워크 접근. 충족하면 추후 지정. MVP 동안은 개발 PC = 배포 PC 가능.
- **개발 위치**: 목업으로만 도는 독립 웹앱이라 어느 PC에서 개발해도 동일. 컨테이너로 배포 장비 이동 자유.

---

## 7. 연동 경로 (후속)

1. 뼈대가 2부 계약 형태로 활동 기록을 Honcho에 남김 (뼈대는 시각화를 모르고 운영 기록만 남김).
2. 살의 `DATA_SOURCE`를 목업 → Honcho 엔드포인트로 교체.
3. 형태가 동일하므로 살 렌더링 로직 무변경. 연동 = 소스 교체 + 네트워크 경로 주입.
