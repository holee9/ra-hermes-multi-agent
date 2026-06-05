# SPEC-RA-TOOL-001 Compact (Agent Context)

**목표**: MVP 자동화 브릿지 3종 스크립트 구현
**이슈**: #3(verify), #4+#6(setup — RA 3 + 인프라 3 프로파일), #11(cold-start)
**언어**: Bash + Node.js
**버전**: 1.1.0 (교차검증 개정 2026-06-05)

## 산출물

1. `scripts/detect-device.sh` + `scripts/device-map.json` — 장치 인식(라이브 hostname→장치/URL). 모든 스크립트가 `source`로 선행 호출 (REQ-TOOL-108)
2. `profiles/setup.sh` — honcho-config-templates/*.json.template → `hermes profile create` 자동화
3. `scripts/verify-honcho.sh` — Honcho API + pgvector(4096) + GX10 + workspace 검증
4. `scripts/cold-start-verify.sh` — MVP E2E 7기준 자동 검증
5. `scripts/cold-start-config.json` — 타임아웃·임계값 외부 설정
6. `reports/.gitkeep` — 결과 저장 디렉터리
(비추적) `CLAUDE.local.md` — 장치별 에이전트 브리핑(T3610 등), 매 세션 자동 로드

## 절대 제약 (위반 시 즉시 중단)

- WP Close/Reopen API를 스크립트에서 호출하지 말 것 (GATE-1)
- hermes 기능(메모리·세션·스킬)을 재구현하지 말 것
- URL·포트·임계값을 코드에 하드코딩하지 말 것 ([IF] 패턴)
- 가상오피스에 쓰기 작업 없음 (읽기 전용)

## 검증 체크리스트

- [ ] profiles/setup.sh: 8종 템플릿 처리, 멱등성 보장
- [ ] SOUL 이식: 파일명 규칙 `<agent>-SOUL.md` (대문자, 하이픈 — `.soul.md` 아님!), infra-SOUL.md 1개가 infra-t3610/gx10/rpi 3개에 폴백 적용
- [ ] verify-honcho.sh: 6체크 pass/fail, exit code 0/1
- [ ] cold-start-verify.sh: 7기준 E2E, reports/ JSON 저장
- [ ] 모든 스크립트: chmod +x, --help 지원
- [ ] [IF] 패턴: 환경 변수로 설정 가능

## 동결된 데이터 계약

RA 분석 결과: `{actor, wp, match, confidence, region, comment, transition_proposed}`
활동 로그: `{ts, type, actor, payload}`
→ cold-start-verify.sh는 이 스키마로 수신 데이터를 검증

## 가정 사항 (확인 필요 — 2026-06-05 실측 반영)

- hermes CLI: `profile create`/`update` 서브커맨드 존재 확인됨. `--config`/`--soul` 플래그형만 `hermes profile create --help`로 최종 확인
- Honcho workspace **생성** `POST /v1/apps/{APP}/workspaces` 확인됨(init-workspaces.sh). verify용 **조회** GET/LIST 형식만 배포 후 확인
- GX10 URL: `http://gx10:11434` (LAN 호스트명 확정 필요)
- hermes 버전: v0.14.0 가정이나 PyPI는 v0.13.0일 수 있음 — 배포 환경 버전 확인
- Qwen3 모델 ID: `qwen3:latest`/`qwen3-embedding:latest` 정확 명칭은 `${GX10_URL}/v1/models` 실응답 확인 (REQ-TOOL-205)
- 사전조건: verify-honcho는 init-workspaces.sh 선행 필요, cold-start는 #5 mail-triage 배포 필요(미가동 시 AC-CS-06 fallback)

## 구현 순서 (의존성)

1. `scripts/detect-device.sh` + `device-map.json` (장치 인식, 나머지가 source)
2. `scripts/cold-start-config.json` (기본값 정의)
3. `scripts/verify-honcho.sh` (독립, 즉시 구현 가능)
4. `profiles/setup.sh` (verify-honcho 통과 후 더 유용)
5. `scripts/cold-start-verify.sh` (verify + setup 이후 풀 테스트)
6. `reports/.gitkeep`

---
Version: 1.1.0
