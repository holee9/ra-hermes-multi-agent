# n8n Credential 유실 복구 (2026-06-21)

## 현상
n8n 워크플로우 4개(mail-triage, infra-to-work-bridge, feedback-recorder, wp-close-recorder)가
credential을 참조하지만 **DB에 credential이 0건**. 특히 mail-triage의 Gmail Trigger가
credential 부재로 폴링을 시작하지 못해 실행 기록 0건 → 모든 워크플로우 동작 불가.
가상 오피스도 최근 활동 0건으로 관측됨.

## 원인
- credential 레코드가 DB에 없음 (encryption key는 `/home/node/.n8n/config`에 영속 → key 문제 아님)
- 컨테이너 재생성 과정 또는 초기 설정 누락 추정 (정확한 유실 시점은 미확정)
- 부가: `n8n/.env`의 OP 자격증명이 placeholder(`your-openproject-api-key`) + 잘못된 주소(`10.20.6.140`)

## 복구 절차
1. **OP 토큰 확보**: `/opt/hermes-ra/.env`의 `OPENPROJECT_API_TOKEN` (유효, 64자) — `scripts/op_honcho_backfill.py` 참고
2. **OP 주소 교정**: `10.20.6.140` → `192.168.100.50:8080` (RPi 내부망 직접)
   - `plm.abyz-lab.work`는 Cloudflare 1010(봇 차단)/401(auth 헤더 깨짐) → 내부망 직접이 정답
3. **OP Admin Auth credential import** (id `S1K0DNp5LZmzpu4j` 재사용 → workflow 재매핑 불필요):
   ```
   type=httpBasicAuth, user=apikey, password=<OPENPROJECT_API_TOKEN>
   ```
   - n8n credential API(POST)는 allowedDomains/type 스키마로 거부 → `n8n import:credentials` CLI + 배열 + id 포함 형식으로 해결
4. **n8n 컨테이너 recreate** (env URL 적용): `cd n8n && docker compose up -d`
   - credential은 volume(`n8n_n8n_data`)에 유지 → recreate 후에도 보존 확인
5. **검증**: n8n 컨테이너 → `http://192.168.100.50:8080/api/v3` 접근 성공

## 남음 — Gmail OAuth (사용자 인증 필수)
- Gmail credential(id `g84TMmDST8pNER2l`, googleOAuth2Api) **뼈대 import 완료**(빈 client/secret)
- Google OAuth 연결 필요:
  1. n8n UI(`http://192.168.100.200:5678` 또는 Tailscale `100.119.79.28:5678`) 로그인
  2. Credentials → "Gmail account" 편집
  3. Google Cloud OAuth client ID/Secret 입력
     - Authorized redirect URI: `http://192.168.100.200:5678/rest/oauth2-credential/callback`
  4. "Sign in with Google" → Google 계정 인증 (브라우저 1회)
- Gmail 연결 전까지 mail-triage Gmail Trigger 미동작 (OP 경로는 이미 정상)

## 예방 조치
- `N8N_ENCRYPTION_KEY`는 config 파일에 영속 확인 → 컨테이너 재생성 시 credential 보존 (볼륨 `n8n_n8n_data` 유지 전제)
- credential/OP 자격증명은 정기 `n8n export:credentials` 백업 권장
- `.env` placeholder 사전 검증 필요 (`your-*` 패턴 체크)
- OP는 내부망 직접 주소(`192.168.100.50:8080`) 사용 — Cloudflare 도메인(`plm.abyz-lab.work`)은 n8n 자동화 경로 부적합
