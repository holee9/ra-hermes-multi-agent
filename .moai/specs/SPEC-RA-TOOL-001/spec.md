# SPEC-RA-TOOL-001: MVP 자동화 브릿지 패키지

**Version**: 1.1.0
**Status**: APPROVED
**Created**: 2026-06-05
**Revised**: 2026-06-05 (코드베이스·문서·이슈 교차검증 개정 — SOUL.md 파일명/매핑 수정, #6 매핑 추가, 미결항목 갱신, 시퀀싱 노트 보강)
**Issues**: #3(SETUP-1), #4(PROFILE-1), #6(PROFILE-2), #11(MVP-VALIDATE) 지원
**Author**: MoAI Plan Workflow

---

## 1. 개요

### 1.1 목적

RA Hermes Multi-Agent MVP 골격 코드가 이미 완성된 상태에서, 하드웨어 배포(#3)가 완료된 직후 최소 인력으로 시스템을 구동할 수 있게 하는 **자동화 브릿지 레이어**를 구현한다.

현재 갭:
- `profiles/honcho-config-templates/` 8종이 존재하지만 `hermes profile create` 실행 스크립트가 없다
- Honcho 서버가 정상 가동된 후 연결 상태를 자동으로 검증하는 도구가 없다
- MVP Cold Start E2E 기준(7개 항목)을 자동으로 검증하는 하니스가 없다

### 1.2 범위

| 산출물 | 설명 | 관련 이슈 |
|--------|------|----------|
| `profiles/setup.sh` | honcho-config-templates 8종(RA 3 + 인프라 3 + 매니저 2)을 읽어 hermes profile create 자동 실행 | #4 PROFILE-1, #6 PROFILE-2 |
| `scripts/verify-honcho.sh` | Honcho API 헬스·pgvector 차원·deriver 상태 자동 검증 | #3 SETUP-1 |
| `scripts/cold-start-verify.sh` | MVP Cold Start E2E 7개 기준 자동 검증 하니스 | #11 MVP-VALIDATE |

### 1.3 범위 외

- n8n 환경변수 주입 도구 (별도 이슈화 가능)
- Hermes 기능 재구현 (메모리, 세션, 스킬, Kanban) — 절대 금지
- WP 완료/재오픈 자동화 — 영구적으로 사람 전용

---

## 2. 제약 조건

### 2.1 불변 게이트 규칙 (Hard, 코드로 보장)

```
GATE-1: WP 완료·재오픈은 사람 전용 — 자동화 스크립트에서 해당 API 경로 호출 금지
GATE-2: n8n 워크플로우 변경은 보고 후 진행
GATE-3: 인프라 파괴적 조치(컨테이너 삭제, 데이터 삭제)는 사람 승인 필요
```

cold-start-verify.sh는 WP Close/Reopen API 경로를 **호출하지 않고**, 해당 경로가 에이전트 코드 흐름에 없음을 검증하는 것으로 대체한다.

### 2.2 [IF] 패턴 준수

모든 스크립트의 임계값·URL·설정값은 **환경 변수 또는 외부 설정 파일**에서 읽어야 한다. 코드 내 하드코딩 금지.

### 2.3 동결된 데이터 계약

**RA 분석 결과 JSON** (mail-triage 출력, 변경 금지):
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

**활동 로그 형식** (Honcho 출력 = 가상오피스 입력, 변경 금지):
```json
{
  "ts": "ISO8601",
  "type": "mail_received|matched|comment_added|...",
  "actor": "<actor_id>",
  "payload": {}
}
```

---

## 3. 요구사항 (EARS 형식)

### 3.1 profiles/setup.sh

**REQ-TOOL-101** [SHALL]
시스템은 `profiles/honcho-config-templates/` 디렉터리에서 모든 `.json.template` 파일을 발견하고 각각에 대해 `hermes profile create` 명령을 실행해야 한다.

**REQ-TOOL-102** [SHALL]
시스템은 프로파일이 이미 존재하는 경우(idempotent 실행) 오류 없이 건너뛰고 결과를 "SKIP (already exists)"로 보고해야 한다.

**REQ-TOOL-103** [SHALL]
시스템은 각 프로파일의 처리 결과(CREATE/SKIP/FAIL)를 표준 출력에 명확히 표시해야 한다.

**REQ-TOOL-104** [SHALL]
시스템은 하나 이상의 프로파일 생성에 실패하면 비-0 exit code로 종료해야 한다.

**REQ-TOOL-105** [IF]
SOUL.md 경로 및 Honcho URL은 환경 변수 `HONCHO_URL`, `HERMES_PROFILES_DIR`에서 읽어야 한다. 기본값은 각각 `http://localhost:8000`, `profiles/honcho-config-templates/`이다.

**REQ-TOOL-106** [WHERE]
`profiles/souls/` 디렉터리에 해당 에이전트의 SOUL.md가 존재하는 경우, setup.sh는 해당 파일을 `hermes profile update --soul` 명령으로 이식해야 한다. **파일명 규칙은 `<agent>-SOUL.md`(대문자 SOUL, 하이픈 구분)이다.** (실측 확인: `ra-us-SOUL.md` 형식이며 `ra-us.soul.md` 형식이 아님 — 2026-06-05.)

**REQ-TOOL-106a** [WHERE]
SOUL 파일과 템플릿은 1:1이 아니다. 실제 매핑(실측 2026-06-05, SOUL 6종 ↔ 템플릿 8종):

| SOUL 파일 | 대상 프로파일 |
|-----------|--------------|
| `ra-us-SOUL.md` | ra-us |
| `ra-eu-SOUL.md` | ra-eu |
| `ra-kr-SOUL.md` | ra-kr |
| `op-manager-SOUL.md` | op-manager |
| `n8n-manager-SOUL.md` | n8n-manager |
| `infra-SOUL.md` | infra-t3610, infra-gx10, infra-rpi (1개 SOUL이 3개 인프라 프로파일 공통 담당) |

setup.sh는 각 프로파일에 대해 먼저 `<agent>-SOUL.md`를 정확히 탐색하고, 없으면 `infra-*` 프로파일에 한해 `infra-SOUL.md`로 폴백해야 한다. 이 매핑은 코드 내 상수 하드코딩이 아닌 파일명 규칙 기반 탐색으로 처리한다.

**REQ-TOOL-107** [ASSUMPTION]
hermes CLI의 `profile create`/`profile update` 서브커맨드 존재는 실측 확인됨(2026-06-05). 단 `--config`/`--soul` 정확한 플래그·인자 형식은 `hermes profile create --help`로 최종 확인 후 조정이 필요할 수 있다.

### 3.2 scripts/verify-honcho.sh

**REQ-TOOL-201** [SHALL]
시스템은 Honcho API 헬스체크 엔드포인트(`${HONCHO_URL}/health` 또는 루트 응답)가 200을 반환하는지 검증해야 한다.

**REQ-TOOL-202** [SHALL]
시스템은 `work` 및 `infra` 두 워크스페이스가 Honcho에 존재하는지 검증해야 한다.

**REQ-TOOL-203** [SHALL]
시스템은 PostgreSQL의 pgvector 익스텐션이 활성화되어 있고, **마이그레이션이 적용되었으며**(`alembic_version` 테이블 존재), **임베딩 컬럼 `documents.embedding`·`message_embeddings.embedding`이 존재하고 차원이 4096**임을 검증해야 한다.
(2026-06-05 실측 근거: 마이그레이션 미실행 시 api/deriver 크래시 루프, `EMBEDDING_VECTOR_DIMENSIONS` 미설정 시 컬럼이 1536으로 잘못 생성됨 — 두 실패 모두 이 검증으로 포착해야 한다. 이슈 #3 코멘트 참조.)

**REQ-TOOL-204** [SHALL]
시스템은 Honcho deriver 워커가 1개 이상 실행 중임을 검증해야 한다.

**REQ-TOOL-205** [SHALL]
시스템은 추론 엔드포인트(`${GX10_URL}/v1/models`)가 응답하고 채팅 모델 `qwen3.6:latest` 및 임베딩 모델 `qwen3-embedding:latest`가 사용 가능한지 검증해야 한다.
(2026-06-05 실측: 엔드포인트 `http://192.168.100.1:11434/v1` 응답 확인, `qwen3-embedding:latest` 출력 **4096차원** 직접 측정 확인. SPEC 초안의 `qwen3:latest`는 실재하지 않으며 채팅 모델은 `qwen3.6:latest`로 정정. 전체 모델: kqwen-coder, kqwen-rag, qwen3.6, qwen3-embedding, gemma4:26b, devstral-small-2.)

**REQ-TOOL-206** [SHALL]
시스템은 각 검증 항목에 대해 구조화된 패스/페일 보고서를 출력해야 한다:
```
[PASS] Honcho API health
[PASS] workspace: work
[PASS] workspace: infra
[FAIL] pgvector dimensions: expected 4096, got 1536
```

**REQ-TOOL-207** [SHALL]
시스템은 모든 검증을 통과하면 exit code 0, 하나라도 실패하면 exit code 1로 종료해야 한다.

**REQ-TOOL-208** [IF]
모든 URL과 포트는 환경 변수로 설정 가능해야 한다:
- `HONCHO_URL` (기본: `http://localhost:8000`)
- `GX10_URL` (기본: `http://gx10:11434`)
- `POSTGRES_URL` (기본: `postgresql://honcho:honcho@localhost:5433/honcho`)

### 3.3 scripts/cold-start-verify.sh

**REQ-TOOL-301** [SHALL]
시스템은 MVP 냉간 시동(Cold Start) E2E 검증 7개 기준을 자동으로 순서대로 검증해야 한다:
```
AC1: mail-triage 워크플로우가 테스트 이메일을 수신하고 처리한다
AC2: RA 분석 결과 JSON이 동결된 데이터 계약과 일치한다
AC3: 신규 WP 또는 기존 WP 매칭이 정확하다 (confidence >= 임계값)
AC4: Honcho에 활동 로그가 기록된다
AC5: 에이전트 피드백이 Honcho deriver를 통해 메모리에 반영된다
AC6: WP 완료/재오픈 경로가 에이전트 코드에서 차단된다 (GATE-1 검증)
AC7: 전체 사이클이 타임아웃(기본 300초) 내에 완료된다
```

**REQ-TOOL-302** [SHALL]
시스템은 RA 분석 결과 JSON의 스키마를 동결된 데이터 계약과 비교하고 필드 누락·타입 불일치를 보고해야 한다.

**REQ-TOOL-303** [SHALL]
시스템은 GATE-1을 검증할 때 실제 WP Close API를 호출하지 않고, n8n 워크플로우 코드에서 해당 경로의 부재 또는 차단 로직의 존재를 확인하는 방식으로 검증해야 한다.

**REQ-TOOL-304** [SHALL]
시스템은 테스트 실행 중 생성된 모든 테스트 데이터(WP, 세션, 메시지)에 `[TEST]` 접두사를 붙여 프로덕션 데이터와 명확히 구분해야 한다.

**REQ-TOOL-305** [SHALL]
시스템은 검증 결과를 `reports/cold-start-YYYY-MM-DD-HH-MM.json` 형식으로 저장해야 한다.

**REQ-TOOL-306** [IF]
타임아웃, confidence 임계값, 테스트 이메일 내용은 `scripts/cold-start-config.json`에서 읽어야 한다. 파일이 없으면 기본값을 사용해야 한다.

**REQ-TOOL-307** [WHERE]
n8n이 가동 중이지 않은 경우, 시스템은 mail-triage 단계를 건너뛰고 나머지 검증 가능한 단계(Honcho 기록 확인 등)를 계속 실행해야 한다.

---

### 3.4 공통: 장치 인식 (모든 스크립트)

**REQ-TOOL-108** [SHALL]
setup.sh·verify-honcho.sh·cold-start-verify.sh는 시작 시 `source scripts/detect-device.sh`로 현재 물리 장치를 인식하고 장치별 기본 URL(`HONCHO_URL`/`GX10_URL`/`POSTGRES_URL` 등)을 해소해야 한다. git 추적 파일은 모든 장치가 공유하므로, "현재 장치"는 git 밖 신호인 **라이브 hostname**으로 판별한다.

**REQ-TOOL-108a** [SHALL]
장치 판별 우선순위는 ① `RA_DEVICE` 환경변수 → ② `device-map.json`의 hostname 패턴 매칭 → ③ `unknown` 폴백이다. 개별 URL 환경변수가 이미 설정돼 있으면 그 값이 map 값보다 우선한다([IF] 패턴).

**REQ-TOOL-108b** [WHERE]
`RA_DESTRUCTIVE_IS_PROD=true`(T3610/GX10/RPi)인 장치에서 스크립트는 파괴적 조치(컨테이너 삭제, DB/볼륨 초기화)를 수행하지 않으며, 해당 경로 발생 시 GATE-3에 따라 사람 승인 메시지를 출력하고 중단해야 한다. `unknown` 장치는 서비스 원격·파괴 위험을 미확정으로 간주한다.

**REQ-TOOL-108c** [CONFIRMED 2026-06-05]
`device-map.json`의 모든 장치 정보가 실측으로 확정됨: T3610(honcho :8000, pgvector :5433, redis :6379), GX10(hostname `gx10-d74b`, 2.5G IP `192.168.100.1`, Ollama :11434), RPi(hostname `raspberrypi`, 2.5G IP `192.168.100.50`, OpenProject :8085, n8n :5678). 7장 미결 3·5 참조사항 해소됨.

---

## 4. 구현 지침

### 4.1 기술 스택

- **언어**: Bash (setup.sh, verify-honcho.sh) + Node.js(cold-start-verify.sh는 JSON 파싱 필요)
- **의존성**: curl, jq (Bash), node (v20+, cold-start-verify.sh)
- **hermes CLI**: hermes (NousResearch) — PATH 설치 확인됨(2026-06-05), `profile create`/`profile update` 서브커맨드 존재. v0.14.0 가정이나 PyPI 배포본은 v0.13.0일 수 있음(7장 미결 4 참조)

### 4.2 파일 구조

```
profiles/
  setup.sh                    ← 신규 생성
scripts/
  detect-device.sh            ← 신규 생성 (장치 인식, git 추적)
  device-map.json             ← 신규 생성 (hostname→장치/URL 매핑, git 추적)
  verify-honcho.sh            ← 신규 생성
  cold-start-verify.sh        ← 신규 생성
  cold-start-config.json      ← 신규 생성 (기본값 포함)
reports/
  .gitkeep                    ← 신규 생성 (cold-start 결과 저장 디렉터리)

(비추적 / git 밖 — 장치별 로컬)
CLAUDE.local.md               ← 장치별 에이전트 브리핑 (.gitignore 처리, 장치마다 다름)
```

`detect-device.sh`/`device-map.json`은 git 추적(모든 장치 공유)이지만 **선택은 라이브 hostname**(git 밖 신호)으로 이뤄진다. `CLAUDE.local.md`는 장치별 비추적 파일로 에이전트가 현재 장치(T3610 등)를 오판하지 않도록 매 세션 컨텍스트에 고정한다.

### 4.3 @MX 태그 계획

| 파일 | 위치 | 태그 | 이유 |
|------|------|------|------|
| `cold-start-verify.sh` | GATE-1 검증 블록 | `@MX:ANCHOR` | 에이전트 WP Close 차단 — 핵심 불변 계약 |
| `cold-start-verify.sh` | 타임아웃 설정 | `@MX:NOTE` | [IF] 패턴 — 외부 설정에서 읽음 |
| `verify-honcho.sh` | pgvector 차원 체크 | `@MX:ANCHOR` | 4096차원은 Qwen3 임베딩과 맞춤 — 변경 금지 |

---

## 5. 검증 기준

acceptance.md 참조.

---

## 6. 이슈 매핑

| SPEC 요구사항 | GitHub 이슈 | 이슈 작업 항목 |
|--------------|-------------|--------------|
| REQ-TOOL-101~107 | #4, #6 | PROFILE-1(RA 3종) + PROFILE-2(인프라 3종) — setup.sh가 8개 전 프로파일 생성하므로 두 이슈를 동시 충족 |
| REQ-TOOL-201~208 | #3 | SETUP-1: Honcho 서버·GX10 연결 검증 |
| REQ-TOOL-301~307 | #11 | MVP-VALIDATE: Cold Start E2E 전 사이클 |

---

## 7. 미결 항목

> 2026-06-05 코드베이스 실측으로 일부 항목 해소·세분화됨.

1. **hermes CLI 플래그형 확인**: `hermes profile create`/`profile update` 서브커맨드 존재는 실측 확인됨. `--config`/`--soul` 정확한 플래그·인자 형식만 `hermes profile create --help`로 최종 확인 후 조정 필요 (REQ-TOOL-107).
2. **Honcho workspace 조회 엔드포인트**: 생성 경로 `POST /v1/apps/{APP}/workspaces`는 `init-workspaces.sh`에서 실사용 확인됨(해소). verify-honcho.sh가 워크스페이스 **존재 여부를 조회**할 GET/LIST 엔드포인트 형식은 T3610 배포 후 OpenAPI 스키마로 확인 필요 (REQ-TOOL-202).
3. ~~**추론 엔드포인트 / GX10 정체**~~ → **해소(2026-06-05 gx10 진단)**: `192.168.100.1`은 GX10 장치의 실제 2.5G IP 확정 (`enx00e04c4728ca`, 2500Mbps, hostname `gx10-d74b`). 게이트웨이/프록시가 아님. `device-map.json` gx10 항목 실IP·실포트로 업데이트 완료. 모델 교체 진행 중(현재 `qwen3.6`+`qwen3-embedding`+`kqwen-coder`+`kqwen-rag`+`gemma4:26b`+`devstral-small-2`) — REQ-TOOL-205는 런타임 `${GX10_URL}/v1/models` 쿼리로 동적 검증하므로 교체 완료 후에도 자동 반영됨.
4. **hermes 버전 가용성**: v0.14.0("Foundation Release")은 PyPI 미배포(v0.13.0)일 수 있음. 배포 환경의 실제 버전과 `profile` 서브커맨드 호환성 확인 필요.
5. ~~**Qwen3 모델 ID 정확 명칭**~~ → **해소(2026-06-05)**: 임베딩 `qwen3-embedding:latest`(4096차원 실측), 채팅 `qwen3.6:latest`로 확정. REQ-TOOL-205 정정 반영됨.
6. **deriver 헬스체크 방법**: REQ-TOOL-204의 deriver 워커 가동 확인 방법(Honcho `/health` 응답 필드 vs 컨테이너 프로세스 점검 vs DB 큐)은 Honcho 헬스 스키마 확인 후 확정.
7. **AC5 관찰가능 정의**: cold-start AC5("deriver를 통한 메모리 반영")의 검증 가능한 증거(honcho conclude 엔트리·차회 판단 변화 등)는 배포 후 운영 정의 필요.
8. **[배포 결함·미해결] Honcho 임베딩 차원 1536→4096**: 2026-06-05 T3610 실측에서 마이그레이션은 적용됐으나(api/deriver Up 복구) `EMBEDDING_VECTOR_DIMENSIONS` 미설정으로 임베딩 컬럼이 1536으로 생성됨. qwen3-embedding(4096)과 불일치 → 차원 수정(파괴적·무손실 스키마 재생성) **사용자 보류 중**. 복구 절차는 이슈 #3 코멘트 참조. 이 결함은 #3(SETUP-1) 범위.

---

## 8. 시퀀싱·사전조건 노트

- **장치 인식 선행**: 모든 스크립트는 `source scripts/detect-device.sh`로 장치를 먼저 해소(REQ-TOOL-108). T3610에선 `HONCHO_URL=http://localhost:8000`(로컬), RPi/GX10에선 `http://192.168.100.200:8000`(2.5G LAN 실IP)으로 자동 전환. 에이전트는 `CLAUDE.local.md`로 현재 장치를 인식하여 localhost 오판·파괴적 명령 오발을 방지.
- **setup.sh 실행 시점**: #3(Honcho 배포) 완료 후 실행. #13(ABSORB-1, SOUL.md 심화 이식)과는 실행상 독립이나, REQ-TOOL-106의 SOUL 이식 효과는 #13 완료 후에 충분해진다. 권장 순서: **#13 → setup.sh → #11**.
- **verify-honcho.sh 사전조건**: `work`·`infra` 워크스페이스가 `init-workspaces.sh`(SPEC 범위 외, 기구현)로 사전 생성되어 있어야 한다. 미생성 시 REQ-TOOL-202가 FAIL 처리.
- **cold-start-verify.sh 사전조건**: #3·#4·#6 완료 + #5(mail-triage 배포) 필요. #7·#8·#9 워크플로우 가동 시 AC1~AC7 전체 실행되나, 미가동 시 REQ-TOOL-307/AC-CS-06 graceful fallback으로 AC1(및 피드백 의존 AC5)을 건너뛰고 검증 가능 항목을 계속 실행한다.

---

Version: 1.1.0
Source: SPEC-RA-TOOL-001 (moai plan 2026-06-05, 교차검증 개정 2026-06-05)
