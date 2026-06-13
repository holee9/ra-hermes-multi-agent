# 운영 전략서 (Operations Guide)

> **대상: 사람(운영자) + Hermes.** 코딩이 아니라 *설정과 운영*. 코딩 산출물(구현 명세서)이 만든 그릇을 어떻게 채우고 키우는가.
> 핵심: 이 시스템은 *학습하며 성장*한다. 운영의 목표는 기능 추가가 아니라 **같은 골격을 성숙시키는 것**.

---

## 1. 운영 대 코딩 (경계 재확인)

- 코딩 산출물: n8n 워크플로우·파싱·연동·투표 자리·가상 오피스(구현 명세서).
- **운영 영역(이 문서)**: 프로파일 생성, SOUL.md 페르소나, Honcho 학습 루프 가동, 3점 평가, 성장 판단.

---

## 2. 프로파일·페르소나 운영

### 2.1 생성 순서 (자동화 스크립트 사용 권장)

`profiles/setup.sh` 로 전체 프로파일·honcho.json을 자동 생성합니다:

```bash
bash profiles/setup.sh
# DRY_RUN=1 bash profiles/setup.sh   # 드라이런
```

수동 생성 순서:
1. Honcho 서버 기동(T3610), workspace `work`·`infra` 생성.
2. 업무: `hermes profile create ra-us` → ra-eu·ra-kr → op-manager·n8n-manager.
3. 인프라: infra-t3610·infra-gx10·infra-rpi (workspace=infra).
4. 각 honcho.json host 블록에 workspace·aiPeer 지정.

### 2.1a Honcho 피어 ID 명명 규칙 (frozen)

`aiPeer` 값은 **언더스코어 형식**을 사용합니다. 이는 n8n 워크플로우·활동 로그·피드백 레코드의 `actor` 필드와 동일한 frozen 데이터 계약입니다.

| 프로파일 | aiPeer (정확한 값) | 오류 예시 (사용 금지) |
|---------|------------------|-------------------|
| ra-us | `ra_us` | ~~`ra-us`~~ |
| ra-eu | `ra_eu` | ~~`ra-eu`~~ |
| ra-kr | `ra_kr` | ~~`ra-kr`~~ |
| op-manager | `op_manager` | ~~`op-manager`~~ |
| infra-t3610 | `infra_t3610` | ~~`infra-t3610`~~ |

`profiles/setup.sh` 는 프로파일 ID(하이픈)를 자동으로 언더스코어로 변환합니다.

> **P0 회귀 방지 (#49)**: 자율 학습·bootstrap·replay·Honcho 직접 기록 코드에서는 프로파일 ID와 Honcho peer ID를 반드시 분리한다. `peer_id`에 `ra-us`, `ra-eu`, `ra-kr`가 들어가는 순간 wrong peer가 생성되고, 메모리·문서·queue가 분리 오염된다. 이 경우 직접 rename하지 말고 raw payload를 clean text로 replay한다.

### 2.1b Honcho 피어 수동 등록

Honcho v0.15.1은 에이전트 첫 연결 시 피어를 자동 생성하지만, REST API로도 사전 등록할 수 있습니다:

```bash
# work 피어 등록 (ra_us 예시)
curl -s -X POST "http://localhost:8000/v3/workspaces/work/peers" \
  -H "Content-Type: application/json" \
  -d '{"id": "ra_us"}'

# infra 피어 등록 (infra_t3610 예시)
curl -s -X POST "http://localhost:8000/v3/workspaces/infra/peers" \
  -H "Content-Type: application/json" \
  -d '{"id": "infra_t3610"}'
```

> **피어 삭제 API 없음**: Honcho v0.15.1에는 피어 삭제 엔드포인트가 없습니다. spurious 피어 삭제는 DB 직접 접근 필요 (`docs/usage-guide.md` §10 참조).

### 2.2 SOUL.md (페르소나 = 지향점은 "지구 최고 전문가", 실제 실력은 학습으로)
- **공통 바탕**: 의료기기 인허가는 실수가 환자 안전과 직결 → "확실하지 않으면 단정 말고 사람에게 올린다"는 겸손을 모든 페르소나에 박는다. 최고 전문가 = 화려한 자신감이 아니라 정확함·정직함.
- **ra-us(Mike)**: substantial equivalence 논증·predicate 전략·신속(510k). 효율·전략형.
- **ra-eu(Theo)**: 기기별 임상 근거·포괄 문서·Notified Body. 철저·장기형.
- **ra-kr(Sam)**: KGMP·언어 의무 + 해외 근거를 한국 체계로 잇는 가교형.
- **op-manager(Margot)**: 사안 라이프사이클 추적. 완료는 절대 자기 처리 안 함(사람에게).
- **n8n-manager(Olly)**: 워크플로우 개선 안목. 변경은 보고 후 진행(신중).
- **infra 3종(Finn/Leo/Gus)**: 각 장비 SRE. 보수적(파괴적 조치는 사람 승인). 셋의 협업이 정체성.
- **T자형**: 모든 페르소나는 가로획(공통 지식 토대 = llm-wiki·ra-project·MD-process 단방향 참조) 위에 세로획(자기 전문성)을 쌓는다. SOUL.md에 "자기 영역을 깊이 판다"를 명시.

### 2.3 메모리 운영 (학습의 실제)
- `honcho_conclude`: 사안↔WP 매핑, 처리 판단 기록.
- `peer="ai"`: 자기 교정("내 판단이 이랬는데 사람이 다르게 갔다").
- `honcho_search/context`: 새 사안 처리 시 과거 맥락 warm start 주입.
- 학습 신호 핵심: 사람의 3점 평가 + 정정. 사람이 한 번 정정한 유형을 차회 정정 없이 맞히는가 = 성장 측정.

---

## 3. 학습 루프 가동

1. 사안(메일) 처리 → RA 전문가가 분석·판단(과거 맥락 주입된 상태).
2. 결정과 근거를 Honcho에 기록(자기 학습 교재).
3. 사람이 3점 평가 + 근거 한 줄.
4. 평가가 AI peer 표상에 누적 → 다음 판단이 사람 의도로 수렴.
5. 가중치는 평가가 사안 영역별로 사후 조정(앞에서 설계 안 함).

> 무평가 결정 = 중립(가중치 불변). 평가된 것만 학습에 사용.

### 3.1 자율 학습 bootstrap 운영 규칙 (#49 이후)

자율 학습 bootstrap은 대량 Honcho write와 deriver queue를 발생시키므로, 실행 전 반드시 아래 preflight를 통과해야 한다.

```bash
cd /home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent
python3 scripts/verify-study-scheduler.py

SCRIPT_DIR="$PWD/scripts"
set -a && . "$SCRIPT_DIR/.env" && set +a
STUDY_BOOTSTRAP_MAX=1 python3 "$SCRIPT_DIR/autonomous-study-scheduler.py" bootstrap --dry-run
```

정상 dry-run 로그는 `ra_us`, `ra_eu`, `ra_kr`처럼 언더스코어 peer ID를 보여야 한다. `ra-us`, `ra-eu`, `ra-kr`가 Honcho write 대상처럼 보이면 즉시 중단한다.

#### 실행 중 확인

프로덕션 T3610에서는 sandbox 안의 PID 조회가 실제 프로세스를 놓칠 수 있다. 반드시 host 기준으로 확인한다.

```bash
ps -eo pid,ppid,etime,args | rg 'autonomous-study-scheduler|claude -p'
tail -80 /tmp/hermes-bootstrap.log
```

#### 오염 발생 시 즉시 절차

1. wrong-peer bootstrap 프로세스와 child `claude -p`를 먼저 종료한다.
2. `honcho-deriver-1`를 중지해 pending queue가 더 이상 wrong-peer documents를 만들지 못하게 한다.
3. affected `messages`/`documents`/`queue`/`sessions`를 JSONL로 백업한다.
4. wrong-peer pending queue는 `processed=true`와 quarantine note로 격리한다.
5. wrong-peer derived documents는 soft-delete 또는 quarantine한다. 정상 peer로 직접 이동하지 않는다.
6. raw `study_insight` JSON payload에서 `topic`/`finding`/`relevance`/`source`/`chunk_id`만 추출해 clean text로 정상 peer에 replay한다.
7. `honcho-deriver-1`를 재시작하고 정상 peer queue 처리 상태를 모니터링한다.

복구 replay는 idempotent 스크립트를 사용한다.

```bash
set -a && . scripts/.env && set +a
python3 scripts/replay-study-insights-issue49.py          # dry-run
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```

직접 SQL로 `peer_name='ra-us'`를 `peer_name='ra_us'`로 바꾸는 방식은 금지한다. content 내부 actor, session name, embeddings, derived documents가 함께 오염되어 정상 peer에 meta-memory를 이식할 위험이 있다.

#### #49 실제 복구 상태

2026-06-13 기준 복구 결과:

| 항목 | 결과 |
|---|---:|
| wrong-peer source messages 백업 | 2,086 rows |
| wrong-peer queue 백업 | 1,573 rows |
| wrong-peer documents 백업 | 7,862 rows |
| clean replay to `ra_us` | 1,656 messages |
| clean replay to `ra_eu` | 429 messages |
| replay JSON envelope | 0 |
| wrong-peer active documents 최종 확인 | 0 |

`honcho-deriver-1`는 재시작되었고, `ra_us`/`ra_eu` 정상 peer queue를 처리한다. backlog 완료 전에는 #49를 닫지 않는다.

---

## 4. 게이트 운영 (고정 규칙)

| 행위 | 권한 |
|---|---|
| 매칭·덧글 추가 | 에이전트 자율(Green) |
| 상태 전이(완료 제외) | 학습 성숙도 따라 제안→자율 승급 |
| **완료·재오픈** | **사람 전용(불변)** — 에이전트는 제안만 |
| n8n 워크플로우 변경 | 보고 후 진행(사람 승인) |
| 인프라 파괴적 조치 | 사람 승인. 모니터링·보고는 자율 |

---

## 5. MVP → 프로덕션 성장 기준

**프로덕션은 새 기능이 아니라 성숙으로 도달한다.** 같은 골격이 학습·평가로 깊어진 상태. 아래는 "Hermes가 이만큼 성숙하면 무엇을 한다"는 성장 트리거 — 미리 일정으로 박지 않고, 조건이 충족되면 실행.

### 5.0 현재 로드맵 (2026-06-13 기준)

| 단계 | 상태 | 이슈 |
|------|------|------|
| Phase 1: MVP 골격 | ✅ 완료 | #3~#33 |
| Phase 2: T자형 가로획 구축 | ✅ 완료 | #34, #35, #36 |
| Phase 3: 성장 루프 계장화 | 🔄 부분 완료 | #38, #42 완료 / #37 후속 |
| Phase 4: 인프라 투표 활성화 | ⏳ 대기 | #39 |
| Phase 5: 프랙탈 확장 | ⏳ 조건부·일부 진행 | #40, #41 |
| Safety/QA 하드닝 | 🔄 레포 반영 | #43~#47 (#43~#45 운영 import/E2E 대기) |

### 5.1 성숙 지표 (이게 오르면 프로덕션에 가까워짐)
- 중복 WP 생성 빈도 ↓
- 사람 개입·정정 빈도 ↓ (가장 중요 — 성장 곡선)
- 사람 정정 유형의 차회 자동 적중 ↑
- 전이 제안이 사람 판단과 일치 ↑

**측정 도구**: `scripts/growth-metrics.py` (systemd 타이머 구현 완료, 운영 활성화 상태는 배포 환경에서 확인).

### 5.2 성장 트리거 (조건 → 실행)

**트리거 감지 자동화**: `feedback/config/growth-trigger-config.json` 임계값 + n8n 알림 (#38).  
트리거 달성 시 자동 실행이 아니라 **사람에게 알림** — 다음 단계 실행은 사람 판단.

| 트리거 조건 | 다음 단계 |
|------------|---------|
| 매칭이 안정화 (중복 WP 감소 지속) | 경계 케이스 Yellow 임계를 낮춰 자동 비중↑ |
| 전이 제안 정확도 특정 유형 누적 | 그 유형 전이를 제안→자율 승급(완료 제외) |
| 투표 결과가 평가로 충분히 수렴 | 3점 평가를 5점으로 상향(수렴 정밀화) |
| **부재가 패턴으로 확정** | 예약 자리를 채움 (스킬 또는 별도 에이전트, #41) |
| mail-triage 30일 안정 + 성숙 지표 달성 | form 워크플로우 이관 (#40) |
| 인프라 부하 패턴이 드러남 | 단순 규칙 브릿지를 지능형으로 보강 |

**부재 기반 확장 대상 (잠재)**:
- 임상 평가 전문가: CER/임상시험 WP가 월 N건 이상 + Yellow 게이트 비중 높음
- 품질/CAPA 전문가: QMS·CAPA 관련 WP 반복
- 시판후감시(PMS) 전문가: MDR/FSCA 보고서 WP 증가
- 사이버보안 전문가: §524B/MDCG 2021-6 WP 증가
- 팀장(coordinator): 업무량 증가로 RA 3종 간 조율 비용이 전문성 이득 초과

### 5.3 조직·사람 확장 (프랙탈)
- 업무량이 한 워크스페이스를 넘으면 → 팀 단위로 workspace 추가(같은 구조 복제).
- 사람 1인이 병목이 되면 → 팀/그룹별 담당 사람 배정(팀 담당→그룹 총괄→전체). workspace가 사람 책임 경계.
- **[미결]** 사람 다중화 시 사람 간 방향 정렬 — 그룹 총괄 또는 공통 헌장으로 해소.

### 5.4 n8n 하드닝 운영 기준 (#43~#45)

workflow 변경분은 레포에 반영된 것과 RPi n8n에 import된 것이 다를 수 있다. 아래 순서를 운영 기준으로 삼는다.

1. 변경 전 보고: 어떤 workflow와 env 값이 바뀌는지 사람에게 먼저 보고한다.
2. import 대상: `mail-triage.json`, `infra-to-work-bridge.json`, `feedback-recorder.json`.
3. env 적용: `OPENPROJECT_API_URL`, `HONCHO_WORK_WORKSPACE`, `YELLOW_CONFIDENCE_THRESHOLD`를 먼저 확인한다.
4. 선택 채널: `HUMAN_ALERT_WEBHOOK_URL`이 있으면 Yellow payload 수신지를 확인한다.
5. 검증 순서: 낮은 confidence, 완료 WP 매칭, OpenProject 조회 실패, bridge config parse, feedback config parse.
6. 이슈 이력: #43~#45에 import 일시, env 적용 여부, E2E 결과를 코멘트한다.

운영 판정 원칙:

| 상황 | 자동 처리 | 사람 처리 |
|------|-----------|-----------|
| confidence 임계값 이상 + 허용 WP 상태 | 코멘트/신규 생성 가능 | 사후 평가 |
| confidence 임계값 미만 | 중단 | 검토 후 처리 |
| 임계값 미설정/비정상 | 중단 | env 수정 또는 수동 처리 |
| 완료/종결 WP 매칭 | 중단 | 재오픈/신규/무시 결정 |
| OpenProject 상태 조회 실패 | 중단 | 인증·네트워크 확인 |

`BRIDGE_RELAY_CONFIG_JSON`과 `WEIGHT_ADJUSTMENT_CONFIG_JSON`은 [IF] 설정이다. 비워 두면 시스템은 안전한 초기 동작을 유지하되, 운영자가 값을 넣는 순간 그 JSON은 이슈에 기록한다.

---

## 6. 가상 오피스 운영

- MVP: 목업으로 프로토타입 확인.
- 연동: Honcho 활동 기록을 데이터 소스로 전환(`DATA_SOURCE`). 뼈대가 돌면 자동으로 채워짐(뼈대는 시각화 모름).
- 정교화: 필요 시 Kenney CC0 캐릭터로 교체. 일이 있을 때만 캐릭터가 움직이는 "기록 재생" — 비동기 시스템의 정직한 표현.

---

## 7. 운영 철학 (모든 판단의 나침반)

- **정확성·신뢰성 우선 (최우선 원칙)**: 의료기기 인허가에서 오류는 환자 안전 문제다. 속도는 정확성이 보장된 뒤의 부산물이다. 자동화 비중을 늘리는 것은 학습·성숙도 누적에 따른 결과이지, 목표 자체가 아니다. 에이전트가 불확실하다면 반드시 사람에게 올린다 — 이것은 실패가 아니라 올바른 동작이다.
- **중앙 두뇌 없음**: 종합·조율(팀장)은 두되 통제 아님. 판단 분산·집계 규칙·출력 배관.
- **사람 = 최종 결정자**: 규칙을 미리 못 박지 않고 평가로 수렴시킨다. 사람 개입이 줄어드는 게 성장.
- **프랙탈 + 벌집 지향**: 자기복제로 성장, 분산·상호지탱으로 견고. 구조 박제가 아니라 매 결정의 나침반.
- **부재 기반 성장**: 부재가 패턴으로 확정될 때만 채운다. 과잉 분할(조율 비용 > 전문성 이득) 경계.
