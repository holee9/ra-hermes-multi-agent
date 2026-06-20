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

### B1. N8N_API_KEY 재발급 — `scripts/.env`
- **현재**: `scripts/.env`의 `N8N_API_KEY`가 길이 269(JWT)이나 **만료됨** (JWT_SECRET 변경으로 서명 검증 실패)
- **조치**:
  - [ ] n8n UI 접속: `http://192.168.100.200:5678` (또는 T3610 `localhost:5678`)
  - [ ] 로그인 후 Settings → API → **New API Key** 생성
  - [ ] `scripts/.env`의 `N8N_API_KEY` 값을 새 키로 교체
- **검증**: `curl -H "X-N8N-API-KEY:<새키>" http://localhost:5678/api/v1/workflows` 가 200 반환

### B2. honcho POSTGRES_PASSWORD 교체 — `honcho/.env`
- **현재**: `honcho/.env`의 `POSTGRES_PASSWORD`가 **길이 14** (placeholder `change_me_in_production` 또는 약한값 의심)
- **조치**:
  - [ ] `honcho/.env`에서 `POSTGRES_PASSWORD` 현재값 확인 (placeholder면 필수 교체)
  - [ ] 강력값으로 교체: `openssl rand -hex 24`
  - [ ] **주의**: honcho postgres 볼륨이 이미 초기화된 경우, 새값 적용하려면 볼륨 재초기화 또는 `ALTER USER` 필요. Hermes 런타임 영역이므로 교체 영향도 사전 확인 필수
- **검증**: 교체 후 `honcho-api-1` 헬스 정상 (`curl localhost:8000/health`)

### B3. honcho SECRET_KEY 확인 — `honcho/.env`
- **현재**: `honcho/.env.example`에 `SECRET_KEY=change_me_in_production` (placeholder). 실제 `honcho/.env` 값 확인 필요
- **조치**:
  - [ ] `honcho/.env`의 `SECRET_KEY` 값 확인
  - [ ] `change_me_in_production` 또는 약한값이면 `openssl rand -hex 32`로 교체
- **검증**: honcho 컨테이너 재기동 후 헬스 정상

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
