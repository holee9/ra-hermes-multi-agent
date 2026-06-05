# SPEC-RA-TOOL-001 인수 기준

**SPEC**: SPEC-RA-TOOL-001: MVP 자동화 브릿지 패키지
**Version**: 1.1.0 (교차검증 개정 2026-06-05 — SOUL.md 파일명 규칙 수정, 인프라 1:N 매핑 AC 추가, #6 반영)

---

## profiles/setup.sh 인수 기준

### AC-SETUP-01: 정상 실행 (#4 RA 3종 + #6 인프라 3종 + 매니저 2종)
- **Given**: `profiles/honcho-config-templates/` 디렉터리에 8종의 `.json.template`(ra-us/eu/kr, op-manager, n8n-manager, infra-t3610/gx10/rpi)이 존재하고 Honcho 서버가 기동 중
- **When**: `bash profiles/setup.sh` 실행
- **Then**: 8개 프로파일 모두 `hermes profile create` 완료, 표준 출력에 `[CREATE] ra-us: OK` 형식으로 결과 표시, exit code 0

### AC-SETUP-02: 멱등성
- **Given**: setup.sh를 이미 한 번 실행한 후 재실행
- **When**: `bash profiles/setup.sh` 두 번째 실행
- **Then**: 오류 없음, 각 프로파일에 `[SKIP] <name>: already exists` 출력, exit code 0

### AC-SETUP-03: SOUL.md 이식 (파일명 규칙 `<agent>-SOUL.md`)
- **Given**: `profiles/souls/ra-us-SOUL.md` 파일이 존재 (대문자 SOUL, 하이픈 구분 — 실측 파일명)
- **When**: `bash profiles/setup.sh`
- **Then**: ra-us 프로파일에 SOUL.md 내용이 반영됨 (`hermes profile update --soul` 성공)

### AC-SETUP-03b: 인프라 SOUL 공통 매핑 (1:N 폴백)
- **Given**: `profiles/souls/infra-SOUL.md` 1개가 존재하고 infra-t3610/gx10/rpi 3개 템플릿이 존재
- **When**: `bash profiles/setup.sh`
- **Then**: 3개 인프라 프로파일 모두에 `infra-SOUL.md` 내용이 이식됨, 각 프로파일에 `[SOUL] infra-<host>: infra-SOUL.md 적용` 형식 출력
- **Note**: `<agent>-SOUL.md` 정확 매칭이 우선, 없을 때만 `infra-*` 프로파일이 `infra-SOUL.md`로 폴백

### AC-SETUP-04: 부분 실패
- **Given**: 8종 중 1개 템플릿 파일이 손상됨
- **When**: `bash profiles/setup.sh`
- **Then**: 나머지 7개는 정상 처리, 손상된 1개는 `[FAIL] <name>: <error>` 출력, exit code 1

### AC-SETUP-05: 환경 변수 준수
- **When**: `HONCHO_URL=http://t3610:8000 bash profiles/setup.sh`
- **Then**: 지정된 URL로 hermes 연결 시도, localhost 사용 없음

---

## scripts/verify-honcho.sh 인수 기준

### AC-VERIFY-01: 전체 패스
- **Given**: T3610에서 Honcho, PostgreSQL(pgvector 4096차원), Redis, deriver가 모두 정상 가동 중이고 GX10이 응답 중
- **When**: `bash scripts/verify-honcho.sh`
- **Then**: 6개 검증 항목 모두 `[PASS]` 출력, exit code 0

### AC-VERIFY-02: pgvector 차원 불일치 감지
- **Given**: pgvector가 1536차원으로 초기화된 경우
- **When**: `bash scripts/verify-honcho.sh`
- **Then**: `[FAIL] pgvector dimensions: expected 4096, got 1536` 출력, exit code 1

### AC-VERIFY-03: 워크스페이스 존재 확인
- **Given**: `work` 워크스페이스만 생성되고 `infra` 는 미생성
- **When**: `bash scripts/verify-honcho.sh`
- **Then**: `[PASS] workspace: work`, `[FAIL] workspace: infra` 출력, exit code 1

### AC-VERIFY-04: GX10 모델 가용성 확인
- **Given**: GX10에서 `qwen3:latest`는 로드됐지만 `qwen3-embedding:latest`는 없음
- **When**: `bash scripts/verify-honcho.sh`
- **Then**: `[FAIL] GX10 model: qwen3-embedding:latest not found` 출력, exit code 1

### AC-VERIFY-05: 출력 형식
- **When**: `bash scripts/verify-honcho.sh`
- **Then**: 각 항목이 `[PASS]` 또는 `[FAIL]` 접두사와 함께 표시됨, 최종 줄에 `=== 6/6 checks passed ===` 또는 `=== N/6 checks failed ===` 출력

---

## scripts/cold-start-verify.sh 인수 기준

### AC-CS-01: 전체 E2E 사이클 완료
- **Given**: 모든 시스템(Honcho, n8n, OpenProject)이 정상 가동 중
- **When**: `bash scripts/cold-start-verify.sh`
- **Then**: 7개 검증 기준 모두 통과, `reports/cold-start-YYYY-MM-DD-HH-MM.json` 생성, exit code 0

### AC-CS-02: RA 분석 결과 스키마 검증
- **When**: cold-start-verify.sh 실행 중 RA 분석 결과 수신
- **Then**: 동결된 데이터 계약 7개 필드(actor, wp, match, confidence, region, comment, transition_proposed) 모두 존재하고 타입이 올바름, 필드 누락 시 오류 보고

### AC-CS-03: GATE-1 확인 (WP Close 차단)
- **When**: AC7 검증 단계에서 GATE-1 체크 실행
- **Then**: n8n mail-triage.json에서 WP Close API 경로(`/work-packages/:id/close`) 호출이 없음을 확인, 또는 차단 로직이 존재함을 확인, 실패 시 `[GATE-FAIL] WP Close 경로가 에이전트 코드에서 발견됨` 출력

### AC-CS-04: 테스트 데이터 격리
- **When**: cold-start-verify.sh 실행 후
- **Then**: 생성된 모든 OpenProject WP 제목에 `[TEST]` 접두사 존재, Honcho 세션 메타데이터에 `test: true` 태그 존재

### AC-CS-05: 타임아웃 처리
- **Given**: cold-start-config.json에 `"timeout_seconds": 60`으로 설정
- **When**: cold-start-verify.sh가 60초 내 완료되지 않음
- **Then**: `[TIMEOUT] Cold start exceeded 60s limit` 출력, exit code 2

### AC-CS-06: n8n 미가동 시 부분 실행
- **Given**: n8n 서비스가 중지 상태
- **When**: `bash scripts/cold-start-verify.sh`
- **Then**: AC1 (mail-triage) 건너뜀, 나머지 AC2-AC7 중 검증 가능한 항목 실행 계속, 결과에 `[SKIP] AC1: n8n unavailable` 표시

### AC-CS-07: 보고서 형식
- **When**: cold-start-verify.sh 완료
- **Then**: `reports/cold-start-*.json`에 다음 필드 포함:
  ```json
  {
    "timestamp": "ISO8601",
    "overall": "PASS|FAIL",
    "checks": [
      { "id": "AC1", "status": "PASS|FAIL|SKIP", "detail": "..." }
    ],
    "gate_rules_verified": ["GATE-1"],
    "duration_seconds": 42
  }
  ```

---

## 공통 인수 기준

### AC-COMMON-01: [IF] 패턴 준수
- **When**: 모든 스크립트를 소스 코드 검토
- **Then**: URL, 포트, 임계값이 환경 변수 또는 설정 파일에서 읽힘, 코드 내 하드코딩 없음

### AC-COMMON-02: 실행 권한
- **When**: `ls -la profiles/setup.sh scripts/verify-honcho.sh scripts/cold-start-verify.sh`
- **Then**: 3개 파일 모두 실행 권한(chmod +x) 설정됨

### AC-COMMON-03: 도움말
- **When**: `bash profiles/setup.sh --help` 또는 `bash scripts/verify-honcho.sh --help`
- **Then**: 사용법, 환경 변수 목록, 예시 명령 출력

---

Version: 1.1.0
Source: SPEC-RA-TOOL-001 (교차검증 개정 2026-06-05)
