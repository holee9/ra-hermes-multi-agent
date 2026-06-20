# 보안 유출 점검 체크리스트 — 2026-06-21

전수 점검 결과를 정리한 수작업 체크리스트. **이미 자동 조치된 항목**과 **사용자가 직접 처리해야 할 항목**을 구분.
수작업 세션에서 이 문서를 펼쳐놓고 `- [ ]` → `- [x]` 로 하나씩 처리.

---

## ✅ A. 이미 자동 조치 완료 (이번 세션, commit 75b953b)

| 항목 | 조치 | 검증 |
|------|------|------|
| n8n `N8N_USER_MANAGEMENT_JWT_SECRET` | 고정값(`ra-hermes-jwt-2026`) → `n8n/.env` 64hex 난수 | 컨테이너 env `12f1faee...` 확인 |
| n8n `N8N_BASIC_AUTH_PASSWORD` | `changeme_in_production` → `n8n/.env` 32byte 난수 | 컨테이너 env 확인 |
| n8n `POSTGRES_PASSWORD` | `n8n_ra_2026` → `n8n/.env` 48hex 난수 | 컨테이너 env 확인 |
| 보안 산물 git 분리 | `bootstrap-apikey.json`, `entities.zip`, `api-import/` → `n8n/.gitignore` | `git status`에 안 보임 |

> 이 항목들은 git에서 분리 + 새 난수 적용 완료. **아래 수작업 항목과 함께 검증만 하면 됨.**

---

## 🔧 B. 사용자 수작업 체크리스트 (한 번에 처리)

### B1. N8N_API_KEY 재발급 — `scripts/.env`  ✅ 완료 (2026-06-21, 키 ...5rH8)
- **완료**: 기존 무효 키(...7R4, 401) → 새 키(...5rH8) 교체. n8n UI에서 기존 auto-session 키 삭제 후 신규 1개 등록(cli-hermes)
- **검증 결과**: API 호출 **HTTP 200**, 워크플로우 4개 active 조회 성공, `cold-start-verify.sh` AC1 경로 도달 성공 (자동화 정상화)
- **조치**:
  - [ ] **발급**: n8n UI 로그인 → 좌측 하단 사용자 아이콘 → **Settings → API → "Add an API key"** → 키 복사(라벨 `cli`)
    - 접속 URL: `http://192.168.100.200:5678` (내부망) **또는** `http://100.119.79.28:5678` (Tailscale)
  - [ ] **적용**: T3610에서 `nano scripts/.env` → `N8N_API_KEY=` 뒤에 키 붙여넣기 → 저장
  - (원격 PC라면 SSH: `raspi5p`/T3610 접속 후 동일 편집, 또는 T3610 Claude 세션에서 "방금 발급한 키로 N8N_API_KEY 교체해줘" 요청)
- **검증** (적용 후 T3610에서):
  ```bash
  set -a && . scripts/.env && set +a
  curl -s -o /dev/null -w "%{http_code}\n" -H "X-N8N-API-KEY: $N8N_API_KEY" http://localhost:5678/api/v1/workflows
  # 200 이면 완료

### B2. honcho POSTGRES_PASSWORD — `honcho/.env`  ✅ 수용 결정 (2026-06-21)
- **현재**: 길이 14 짧은값이지만 **현재 동작 중인 실제 DB 비밀번호** (honcho 정상 가동 중)
- **결정**: **수용(유지)**. T3610 내부망 전용이고 외부 노출 아니면 위험도 낮음. 교체 시 DB `ALTER USER` + `.env` 동기화 + Hermes 재기동(일시 장애)이 수반되어 비용이 더 큼
- [x] 수용 완료 — 교체 불필요

### B3. honcho SECRET_KEY — `honcho/.env`  ✅ OK (조치 불필요)
- **현재**: 길이 27 강한값 확인 → `.env.example`의 `change_me_in_production` placeholder와 무관하게 실제값은 강함
- [x] 교체 불필요

### B4. DATA_GO_KR_API_KEY 발급 (선택) — `scripts/.env`
- **현재**: `DATA_GO_KR_API_KEY` 길이 2 (사실상 미설정)
- **조치** (공공데이터포털 연동 사용 시에만):
  - [ ] https://www.data.go.kr 에서 발급
  - [ ] `scripts/.env`에 설정
- 사용 안 하면 무시

---

## ⚖️ C. 결정 필요 — git history 정리 (rewrite)

**문제**: 아래 약한 기본값들이 GitHub `origin/main` 이력에 노출되어 있음.

| 값 | 최초 노출 커밋 | 위험 평가 |
|----|--------------|----------|
| `changeme_in_production` (n8n BASIC_AUTH) | `89ae25c` (#39) | **낮음** — 컨테이너는 이미 새 난수, n8n 최신 버전은 user-management 기반이라 BASIC_AUTH 무시 가능 |
| `n8n_ra_2026` (postgres) | `89ae25c` (#39) | **매우 낮음** — n8n은 현재 postgres 미사용(SQLite), 컨테이너는 새 난수 |

**옵션 (하나 선택)**:
- [ ] **C-a (권장) 수용** — 두 값 모두 placeholder성 약한값이고 이미 새값으로 무효화됨. 실제 강력 시크릿이 아니므로 rewrite의 비용(강제 푸시, 협업자 재클론)보다 위험이 낮음
- [ ] **C-b history rewrite** — `git filter-repo` 또는 BFG로 두 값을 이력에서 제거. **파괴적**: force-push + 모든 클론 재취득 필요. 레포 단독 작업자(holee9)면 부담 적음
- [ ] **C-c 보류** — 별도 보안 이슈로 등록 후 추진

> 추천: **C-a**. 두 값 모두 실제 운영 비밀번호로 사용된 흔적이 없고(컨테이너는 새 난수), 외부 서비스 키가 아님.

---

## 🔍 D. 점검에서 확인된 안전 항목 (조치 불필요)

- tracked `.env` 실제 파일 없음 (전부 untracked → git에 안 올라감)
- `scripts/*.py` 시크릿 참조 = `os.environ.get()` (하드코딩 아님)
- `scripts/configure-glm.sh` 시크릿 단어 = 안내 메시지 (실제값 아님)
- 알려진 토큰 패턴(`ghp_`, `sk-`, `AIza`, `glpat-`, `xox`) git history에 없음
- `ra-hermes-jwt-2026` (이번 세션 임시 고정값) git 이력에 노출된 적 없음
- `virtual-office/docker-compose.yml` 시크릿 없음
- n8n 워크플로우 4개 active 유지 (재게시 확인 완료)

---

## 완료 후

- [ ] 이 체크리스트의 `- [ ]` 를 전부 `- [x]` 로 전환 (또는 보류 사유 기록)
- [ ] `memory/next-session-entrypoint.md` 에 수작업 완료 내역 반영
- [ ] (선택) 결정한 C 옵션을 보안 이슈로 GitHub에 등록

---
점검자: Claude (GLM-5.2[1m]) | 점검일: 2026-06-21 | 기준 커밋: 75b953b
