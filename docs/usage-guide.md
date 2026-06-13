# RA Hermes 멀티 에이전트 — 사용 가이드

> 이 가이드는 RA Hermes 멀티 에이전트 시스템을 처음 사용하는 운영자와 개발자를 위한 실전 지침서입니다.
> 시스템 설계 철학은 [`docs/RA-multi-agent-master-design.md`](RA-multi-agent-master-design.md),
> 구현 경계는 [`docs/implementation-spec.md`](implementation-spec.md) 를 참조하세요.

---

## 목차

1. [시스템 구성 요약](#1-시스템-구성-요약)
2. [사전 조건 확인](#2-사전-조건-확인)
3. [Hermes 에이전트 실행](#3-hermes-에이전트-실행)
4. [에이전트별 역할과 페르소나](#4-에이전트별-역할과-페르소나)
5. [Honcho 연결 및 메모리 확인](#5-honcho-연결-및-메모리-확인)
6. [mail-triage 워크플로우 운영](#6-mail-triage-워크플로우-운영)
7. [Cold Start 검증](#7-cold-start-검증)
8. [운영 게이트 규칙](#8-운영-게이트-규칙)
9. [프로파일 재설정 (profiles/setup.sh)](#9-프로파일-재설정-profilessetupsh)
10. [undefined 피어 삭제](#10-undefined-피어-삭제)
11. [트러블슈팅](#11-트러블슈팅)

---

## 1. 시스템 구성 요약

```
T3610 (이 머신)
  └── Honcho API  :8000        ← 에이전트 메모리·세션 백엔드
  └── PostgreSQL  :5433        ← pgvector (4096차원)
  └── Redis       :6379        ← 세션 캐시
  └── Hermes RA 에이전트 8종   ← 이 가이드 주제

GX10 (원격 LAN)
  └── Qwen3 :11434             ← LLM 추론 엔진

Raspberry Pi 5+
  └── n8n  :5678               ← mail-triage / bridge / feedback 워크플로우
  └── OpenProject              ← WP(Work Package) 관리
```

### Honcho Workspace → Actor ID 매핑

| Workspace | Hermes 프로파일 | Honcho 피어 ID (frozen) | 인물 |
|-----------|----------------|------------------------|------|
| work | ra-us | `ra_us` | Mike — FDA 510(k) 전문 |
| work | ra-eu | `ra_eu` | Theo — EU MDR 전문 |
| work | ra-kr | `ra_kr` | Sam — MFDS/KGMP 전문 |
| work | op-manager | `op_manager` | Margot — WP 라이프사이클 |
| work | n8n-manager | `n8n_manager` | Olly — 워크플로우 관리 |
| infra | infra-t3610 | `infra_t3610` | Finn — T3610 SRE |
| infra | infra-gx10 | `infra_gx10` | Leo — GX10 SRE |
| infra | infra-rpi | `infra_rpi` | Gus — RPi SRE |

> **Actor ID는 변경 불가(frozen)**. n8n 워크플로우 JSON, 활동 로그, 피드백 레코드 모두 이 ID를 기준으로 합니다.

---

## 2. 사전 조건 확인

### 2.1 Honcho 스택 확인

```bash
docker ps --format "table {{.Names}}\t{{.Status}}" | grep honcho
```

정상 출력 예시:
```
honcho-api-1       Up X hours
honcho-postgres-1  Up X hours
honcho-redis-1     Up X hours
honcho-deriver-1   Up X hours
```

4개가 모두 Up 상태여야 합니다. 이상 시:
```bash
cd ~/path/to/ra-hermes-multi-agent
docker compose -f honcho/docker-compose.yml up -d
```

### 2.2 Honcho API 응답 확인

```bash
curl -s http://localhost:8000/health | python3 -m json.tool
```

### 2.3 Workspace 초기화 확인

```bash
curl -s http://localhost:8000/v3/workspaces | python3 -m json.tool
```

`work` 와 `infra` 두 workspace가 모두 있어야 합니다. 없으면:
```bash
bash honcho/init-workspaces.sh
```

### 2.4 Honcho 피어 등록 확인

```bash
# work workspace 피어 목록
curl -s "http://localhost:8000/v3/workspaces/work/peers" | python3 -m json.tool

# infra workspace 피어 목록
curl -s "http://localhost:8000/v3/workspaces/infra/peers" | python3 -m json.tool
```

등록된 피어: `ra_us`, `ra_eu`, `ra_kr`, `op_manager`, `n8n_manager` (work),
`infra_t3610`, `infra_gx10`, `infra_rpi` (infra).

### 2.5 Hermes 설치 확인

```bash
/home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes --version
# Hermes Agent v0.15.1 (2026.5.29)
```

### 2.6 GX10 LLM 연결 확인

```bash
source honcho/.env 2>/dev/null || true
curl -s "${GX10_BASE_URL:-http://192.168.100.1:11434/v1}/models" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('모델 수:', len(d.get('data', [])))
for m in d.get('data', [])[:5]:
    print(' -', m['id'])
"
```

---

## 3. Hermes 에이전트 실행

### 3.1 기본 실행 (대화형)

```bash
HERMES=/home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes

# RA US 전문가 (Mike)
HERMES_HOME=~/.hermes/profiles/ra-us $HERMES chat

# RA EU 전문가 (Theo)
HERMES_HOME=~/.hermes/profiles/ra-eu $HERMES chat

# RA KR 전문가 (Sam)
HERMES_HOME=~/.hermes/profiles/ra-kr $HERMES chat

# OP 매니저 (Margot)
HERMES_HOME=~/.hermes/profiles/op-manager $HERMES chat

# n8n 매니저 (Olly)
HERMES_HOME=~/.hermes/profiles/n8n-manager $HERMES chat

# 인프라 에이전트
HERMES_HOME=~/.hermes/profiles/infra-t3610 $HERMES chat
HERMES_HOME=~/.hermes/profiles/infra-gx10 $HERMES chat
HERMES_HOME=~/.hermes/profiles/infra-rpi $HERMES chat
```

> `HERMES_HOME` 은 각 프로파일 디렉터리를 가리킵니다. 기본 `~/.hermes` 가 아님을 주의하세요.

### 3.2 단발 쿼리 (비대화형)

```bash
HERMES_HOME=~/.hermes/profiles/ra-us \
  /home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes run \
  "HAD1717MC의 FDA 510(k) 분류 코드는 무엇인가?"
```

### 3.3 honcho.json 위치

전체 시스템 연결 설정은 `~/.hermes/honcho.json` 에 있습니다.

```json
{
  "baseUrl": "http://localhost:8000",
  "hosts": {
    "hermes_ra-us": { "aiPeer": "ra_us", "workspace": "work", "enabled": true },
    ...
  }
}
```

`aiPeer` 값은 Honcho 피어 ID(언더스코어 형식)와 반드시 일치해야 합니다.

---

## 4. 에이전트별 역할과 페르소나

### ra-us — Mike (FDA 510(k) 전문가)

**전문 도메인**: FDA 510(k) 실질적 동등성, predicate chain, QMSR (21 CFR Part 820)

- 510(k) 심사 전략 및 predicate 선정
- Traditional / Abbreviated / Special 510(k) 경로 판단
- 21 CFR Part 1020 방사선 기준 (HnX-P1/PB 필수)
- FDA 사이버보안 가이던스 (FD&C Act §524B)
- QMSR ISO 13485:2016 정합화 (2026-02-02 발효)

**페르소나**: 효율·전략형. "가장 빠른 신뢰할 수 있는 경로"를 찾는다. 단정 없이 정확히, 불확실하면 즉시 에스컬레이션.

### ra-eu — Theo (EU MDR 전문가)

**전문 도메인**: EU MDR 2017/745, CER(Clinical Evaluation Report), PMCF

- Class IIb/III 기기 임상 평가 전략
- Notified Body 심사 대응
- PMCF(Post-Market Clinical Follow-up) 계획
- EU MDR Article 120 전환 일정

**페르소나**: 철저·장기형. 임상 근거 문서화를 중시. "포괄 문서가 살아있는 문서여야 한다"는 철학.

### ra-kr — Sam (MFDS/KGMP 전문가)

**전문 도메인**: MFDS 인허가, KGMP, FDA·CE 근거의 한국 체계 연결

- 의료기기 품목 분류 및 허가 전략
- KGMP(제조·품질관리기준) 심사 대응
- FDA/CE 기허가 자료의 MFDS 활용 전략
- 한국어 의무 표기 요건

**페르소나**: 가교형. 해외 인허가 근거를 한국 규제 언어로 번역한다. 언어 의무 사항에 민감.

### op-manager — Margot (WP 라이프사이클 관리)

**전문 도메인**: OpenProject Work Package 상태 추적, 사안 분류·매칭

- WP 생성, 상태 전이(리뷰중 포함), 중복 탐지
- 기존 WP 매칭 vs 신규 WP 생성 판단
- **WP 완료·재오픈은 사람만** — Margot은 제안만 함

**페르소나**: 정밀 추적형. 같은 사안이 두 개의 WP로 분리되는 것을 가장 싫어한다.

### n8n-manager — Olly (n8n 워크플로우 관리)

**전문 도메인**: n8n 워크플로우 설계·개선·모니터링

- mail-triage·bridge·feedback 워크플로우 상태 감시
- 파싱 실패·라우팅 오류 진단 및 개선 제안
- **워크플로우 변경은 보고 후 진행** — 단독 실행 금지

**페르소나**: 신중형. 변경 전 영향 분석을 먼저 제출한다.

### infra-t3610 — Finn, infra-gx10 — Leo, infra-rpi — Gus

**전문 도메인**: 각 장비 SRE (Site Reliability Engineering)

| 에이전트 | 담당 | 주요 역할 |
|---------|-----|---------|
| infra-t3610 (Finn) | T3610 | Honcho·Docker 상태, pgvector 인덱스 건강도 |
| infra-gx10 (Leo) | GX10 | Qwen3 inference API 가용성, 모델 로딩 상태 |
| infra-rpi (Gus) | RPi | n8n·OpenProject 서비스 상태, 스토리지 여유 |

**게이트**: 모니터링·보고는 자율. **파괴적 조치(컨테이너 삭제, DB 리셋, 볼륨 초기화)는 사람 승인 필수**.

---

## 5. Honcho 연결 및 메모리 확인

### 5.1 피어 메모리 조회

에이전트가 Honcho에 기록한 메모리(결론·판단)를 조회합니다.

```bash
# ra_us 피어의 최근 메모리 10건
curl -s "http://localhost:8000/v3/workspaces/work/peers/ra_us/messages?limit=10" \
  | python3 -m json.tool
```

### 5.2 세션 목록 조회

```bash
curl -s "http://localhost:8000/v3/workspaces/work/peers/ra_us/sessions" \
  | python3 -m json.tool
```

### 5.3 피어 표상(AI 모델 메모리) 확인

에이전트의 학습 누적 상태(AI peer representation)를 조회합니다.

```bash
curl -s "http://localhost:8000/v3/workspaces/work/peers/ra_us" \
  | python3 -m json.tool
```

### 5.4 Hermes에서 Honcho 연결 상태 확인

```bash
HERMES_HOME=~/.hermes/profiles/ra-us \
  /home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes tools list 2>/dev/null \
  | grep -i honcho || echo "(honcho 도구 확인 필요)"
```

---

## 6. mail-triage 워크플로우 운영

### 6.1 워크플로우 구조

```
n8n (RPi)
  ↓ 재전송 메일 수신
  ↓ 파싱 (발신자·제목·본문)
  ↓ Hermes RA 에이전트 호출 (ra_us / ra_eu / ra_kr 중 라우팅)
  ↓ RA 분석 결과 JSON 수신
  ↓ OpenProject WP 처리 (신규 생성 or 기존 매칭)
  ↓ Honcho 활동 로그 기록
```

### 6.2 운영 환경변수

RPi n8n의 `.env`에는 최소한 아래 값이 있어야 합니다. 예시는 `n8n/.env.example`을 기준으로 유지합니다.

| 변수 | 필수 | 설명 |
|------|------|------|
| `HONCHO_API_URL` | 필수 | T3610 Honcho API base URL |
| `HONCHO_WORK_WORKSPACE` | 필수 | RA 업무 workspace 이름 |
| `OPENPROJECT_API_URL` | 필수 | OpenProject base URL. workflow에 URL 하드코딩 금지 |
| `OPENPROJECT_DEFAULT_PROJECT_ID` | 필수 | 신규 WP 생성 project ID |
| `YELLOW_CONFIDENCE_THRESHOLD` | 필수 | 이 값 미만의 분석은 사람 검토로 전환 |
| `HUMAN_ALERT_WEBHOOK_URL` | 선택 | Yellow payload를 받을 Webhook |
| `HUMAN_ALERT_EMAIL` | 선택 | 사람 알림 대상 메타데이터 |
| `BRIDGE_RELAY_CONFIG_JSON` | 선택 | infra→work bridge relay 조건 JSON |
| `WEIGHT_ADJUSTMENT_CONFIG_JSON` | 선택 | feedback 가중치 조정 공식 JSON |

`YELLOW_CONFIDENCE_THRESHOLD`가 비어 있거나 0~1 범위 숫자가 아니면 cold start로 간주하여 Yellow 게이트로 보냅니다.

### 6.3 RA 분석 결과 JSON (frozen 데이터 계약)

```json
{
  "actor": "ra_us",
  "wp": "WP-123|null",
  "match": "existing|new",
  "confidence": 0.0,
  "region": "US|EU|KR",
  "comment": "...",
  "transition_proposed": "리뷰중|null"
}
```

이 스키마는 변경 불가입니다. n8n 워크플로우·가상오피스·모든 컴포넌트가 이 형식을 기준으로 합니다.

### 6.4 Yellow 게이트 운영 기준

아래 상황은 자동 WP 반영을 멈추고 사람에게 올립니다.

| 상황 | 운영 판단 |
|------|-----------|
| 규제권 미판별 또는 복수 규제권 감지 | 담당 RA를 사람이 배정 |
| RA 응답 JSON 파싱 실패/필드 누락 | 모델 응답 또는 프롬프트를 점검 |
| confidence가 임계값 미만 | 근거 확인 후 기존 WP 코멘트/신규 WP 생성 결정 |
| 기존 WP가 완료/종결/닫힘 상태 | 재오픈, 신규 WP 생성, 무시 중 사람이 결정 |
| OpenProject 상태 조회 실패 | 인증/네트워크/권한 확인 후 재실행 |

Yellow payload에는 원 제목, 원 발신자, matching key, 본문 excerpt, 분석 결과, `yellow_reason`, OpenProject 상태 정보가 들어갑니다.

### 6.5 기존 WP 상태 검증

`match="existing"`이면 workflow는 바로 코멘트하지 않고 OpenProject에서 WP 상태를 조회합니다.

| 결과 | 처리 |
|------|------|
| open/new/progress/review/오픈/진행/리뷰/검토 | 기존 WP에 코멘트 추가 |
| closed/done/complete/완료/종결/닫힘 | Yellow 전환 |
| 상태 필드 없음, 인증 실패, 조회 실패 | Yellow 전환 |
| 상태명이 허용/차단 목록 어디에도 없음 | Yellow 전환 |

완료·재오픈은 영구적으로 사람 전용입니다.

### 6.6 n8n 활성화 확인 (RPi)

```bash
ssh raspi5p "curl -s -H 'X-N8N-API-KEY: \${N8N_API_KEY}' \
  http://localhost:5678/api/v1/workflows | python3 -m json.tool"
```

### 6.7 import 후 검증 시나리오

n8n의 webhook URL로 테스트 페이로드를 전송하여 전체 파이프라인을 확인합니다. 최소 시나리오는 아래 순서로 실행합니다.

1. 정상 신규 사안: `match="new"`, confidence 임계값 이상 → WP 생성.
2. 정상 기존 사안: `match="existing"`, OpenProject 상태 open/progress/review → 코멘트 추가.
3. 저신뢰 사안: confidence 임계값 미만 → Yellow payload, WP 반영 없음.
4. 완료 WP 매칭: OpenProject 상태 closed/done/완료/종결 → Yellow payload.
5. 알림 채널: `HUMAN_ALERT_WEBHOOK_URL` 설정 시 Webhook 수신 확인.

레포에서 먼저 돌릴 정적 검증:

```bash
npm run test:static
```

브라우저가 있는 개발/운영 점검 환경에서는 전체 게이트도 실행합니다.

```bash
npm test
```

---

## 7. Cold Start 검증

시스템 상태를 E2E로 자동 검증하는 스크립트입니다.

```bash
cd /home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent

# n8n API 키 설정 (선택 — AC1 검증에 필요)
export N8N_API_KEY="your-n8n-api-key"

bash scripts/cold-start-verify.sh
```

### 검증 항목 (7가지 인수 기준)

| AC | 항목 | 검증 내용 |
|----|-----|---------|
| AC1 | Honcho API 응답 | `/health` 엔드포인트 200 OK |
| AC2 | 활동 로그 형식 | 필수 필드(ts, type, actor, payload) 존재 확인 |
| AC3 | Honcho 피어 등록 | work·infra workspace 피어 8종 모두 등록 |
| AC4 | Hermes 프로파일 | ~/.hermes/profiles/ 8개 디렉터리 존재 |
| AC5 | Deriver 반영 | (설정으로 비활성화 가능: `ac5_deriver_reflection=false`) |
| AC6 | GX10 LLM 연결 | Qwen3 모델 API 응답 확인 |
| AC7 | honcho.json 피어 ID | aiPeer 값이 언더스코어 형식 준수 |

### 결과 리포트

실행 결과는 `reports/cold-start-<datetime>.json` 에 저장됩니다.

현재 상태: **6/7 PASS** (AC5 비활성화 — deriver 반영 주기 설정에 의한 skip)

---

## 8. 운영 게이트 규칙

이 규칙은 **절대 코드로 우회하지 않습니다**.

| 행위 | 권한 |
|-----|-----|
| WP 매칭·덧글 추가 | 에이전트 자율 (Green) |
| WP 상태 전이 (완료 제외) | 학습 성숙도에 따라 제안→자율 승급 |
| **WP 완료·재오픈** | **사람만 — 영구 불변** |
| n8n 워크플로우 변경 | 보고 후 사람 승인 |
| 인프라 파괴적 조치 | 사람 승인 필수 (DB 리셋·컨테이너 삭제·볼륨 초기화 등) |

---

## 9. 프로파일 재설정 (profiles/setup.sh)

기존 프로파일을 재생성하거나 새 머신에 설정할 때 사용합니다.

```bash
cd /home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent

# 드라이런 (변경 없이 동작 확인)
DRY_RUN=1 bash profiles/setup.sh

# 실제 실행
bash profiles/setup.sh
```

스크립트가 하는 일:
1. `~/.hermes/honcho.json` 에 `baseUrl` 및 각 프로파일 host 블록 작성
2. `hermes profile create <id> --no-skills` 실행 (SOUL.md 제외 — 다음 단계에서 이식)
3. 각 프로파일의 `config.yaml` 에 `memory.provider: honcho` 설정
4. `profiles/souls/` 의 SOUL.md를 각 프로파일 디렉터리에 복사

> `aiPeer` 값은 자동으로 언더스코어 형식으로 변환됩니다 (예: `ra-us` → `ra_us`).

---

## 10. spurious / wrong peer 처리

Honcho v0.15.1에는 피어 삭제 API 엔드포인트가 없습니다. DB 직접 조작은 프로덕션 데이터에 영향을 주므로, 먼저 피어가 참조 중인지 확인합니다.

```bash
docker exec honcho-postgres-1 psql -U honcho -d honcho -c "
SELECT name, workspace_name, id, created_at
FROM peers
WHERE name IN ('undefined', 'ra-us', 'ra-eu', 'ra-kr', 'ra_us', 'ra_eu', 'ra_kr')
ORDER BY workspace_name, name;
"
```

참조 여부 확인:

```bash
docker exec honcho-postgres-1 psql -U honcho -d honcho -c "
SELECT 'messages' AS kind, peer_name AS peer, COUNT(*) FROM messages
WHERE peer_name IN ('undefined', 'ra-us', 'ra-eu', 'ra-kr')
GROUP BY peer_name
UNION ALL
SELECT 'documents_observer', observer, COUNT(*) FROM documents
WHERE observer IN ('undefined', 'ra-us', 'ra-eu', 'ra-kr')
GROUP BY observer
UNION ALL
SELECT 'documents_observed', observed, COUNT(*) FROM documents
WHERE observed IN ('undefined', 'ra-us', 'ra-eu', 'ra-kr')
GROUP BY observed
UNION ALL
SELECT 'session_peers', peer_name, COUNT(*) FROM session_peers
WHERE peer_name IN ('undefined', 'ra-us', 'ra-eu', 'ra-kr')
GROUP BY peer_name
ORDER BY kind, peer;
"
```

### 10.1 `undefined`처럼 참조 없는 피어

참조가 0인 피어만 삭제 후보입니다. 삭제 전에는 반드시 `SELECT`로 대상이 1건인지 확인합니다.

```bash
docker exec honcho-postgres-1 psql -U honcho -d honcho -c "
SELECT id, name, workspace_name
FROM peers
WHERE name='undefined' AND workspace_name='work';
"
```

삭제가 필요하면 사람이 직접 승인 후 실행합니다.

```bash
docker exec honcho-postgres-1 psql -U honcho -d honcho -c "
DELETE FROM peers
WHERE name='undefined' AND workspace_name='work'
  AND NOT EXISTS (SELECT 1 FROM messages WHERE peer_name='undefined' AND workspace_name='work')
  AND NOT EXISTS (SELECT 1 FROM documents WHERE workspace_name='work' AND (observer='undefined' OR observed='undefined'))
  AND NOT EXISTS (SELECT 1 FROM session_peers WHERE peer_name='undefined' AND workspace_name='work');
"
```

### 10.2 `ra-us`/`ra-eu` 같은 wrong-peer 오염 (#49)

`ra-us`, `ra-eu`, `ra-kr` wrong peer는 단순 삭제하거나 `ra_us`, `ra_eu`, `ra_kr`로 직접 rename하면 안 됩니다. messages content 내부 actor, session name, embeddings, documents, queue가 서로 묶여 있어 정상 peer 메모리를 오염시킬 수 있습니다.

표준 처리:

1. wrong bootstrap 프로세스를 종료한다.
2. `honcho-deriver-1`를 중지한다.
3. affected rows를 JSONL로 백업한다.
4. wrong-peer pending queue를 quarantine한다.
5. wrong-peer derived documents를 soft-delete/quarantine한다.
6. raw `study_insight` payload를 clean text로 정상 peer에 replay한다.
7. deriver를 재시작한다.

복구 replay dry-run:

```bash
set -a && . scripts/.env && set +a
python3 scripts/replay-study-insights-issue49.py
```

실행:

```bash
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```

검증:

```bash
docker exec honcho-postgres-1 psql -U honcho -d honcho -c "
SELECT peer_name,
       COUNT(*) AS recovered,
       COUNT(*) FILTER (WHERE left(ltrim(content),1)='{') AS json_envelope,
       COUNT(*) FILTER (WHERE metadata->>'actor' IN ('ra_us','ra_eu')) AS correct_actor
FROM messages
WHERE metadata->>'recovered_from_issue'='49'
GROUP BY peer_name
ORDER BY peer_name;
"
```

정상 결과는 `json_envelope=0`이고, `correct_actor`가 `recovered`와 같아야 합니다.

---

## 11. 트러블슈팅

### Hermes가 Honcho에 연결되지 않을 때

```bash
# honcho.json baseUrl 확인
cat ~/.hermes/honcho.json | python3 -m json.tool

# Honcho API 직접 확인
curl -sv http://localhost:8000/health 2>&1 | tail -5
```

### 특정 에이전트가 응답하지 않을 때

```bash
# 프로파일 디렉터리 확인
ls -la ~/.hermes/profiles/<profile-id>/

# config.yaml 확인
cat ~/.hermes/profiles/<profile-id>/config.yaml

# SOUL.md 존재 확인
ls -la ~/.hermes/profiles/<profile-id>/SOUL.md
```

### GX10 연결 실패 시

```bash
# GX10 IP 확인 (detect-device.sh 활용)
bash scripts/detect-device.sh --print

# GX10_BASE_URL 수동 설정 후 재시도
export GX10_BASE_URL="http://192.168.100.1:11434/v1"
```

### cold-start-verify.sh 실패 시

```bash
# 상세 로그로 실행
bash -x scripts/cold-start-verify.sh 2>&1 | head -100
```

### Honcho 컨테이너 재시작 시 피어 사라짐

Honcho v0.15.1은 피어를 연결 시 자동 생성합니다. 에이전트를 한 번 실행하면 재등록됩니다.
또는 수동 등록:

```bash
# work 피어 재등록 예시
curl -s -X POST "http://localhost:8000/v3/workspaces/work/peers" \
  -H "Content-Type: application/json" \
  -d '{"id": "ra_us"}'
```

---

## 관련 문서

| 문서 | 내용 |
|-----|-----|
| [`docs/RA-multi-agent-master-design.md`](RA-multi-agent-master-design.md) | 전체 설계 철학·아키텍처 결정 |
| [`docs/implementation-spec.md`](implementation-spec.md) | 구현 경계 (`[구현]` vs `[IF]`) |
| [`docs/operations-guide.md`](operations-guide.md) | 학습 루프·성장 기준·게이트 운영 |
| [`CLAUDE.md`](../CLAUDE.md) | Claude Code 실행 지시 |
| [`scripts/cold-start-verify.sh`](../scripts/cold-start-verify.sh) | MVP E2E 자동 검증 스크립트 |
| [`profiles/setup.sh`](../profiles/setup.sh) | 프로파일 생성 자동화 |

---

*최종 갱신: 2026-06-13 | Hermes v0.15.1 / Honcho v0.15.1 기준*
