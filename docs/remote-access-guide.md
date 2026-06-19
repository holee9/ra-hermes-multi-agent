# RA Hermes 시스템 접속 가이드 (원격지역용)

> **기준일**: 2026-06-19  
> **T3610 서버 IP**: 192.168.100.200 (LAN 내부)  
> **주의**: 외부 인터넷에서는 보안상 직접 접속이 권장되지 않습니다

---

## 🌐 원격지역에서 접속 가능한 서비스

### 1. Honcho API (RA 에이전트 백엔드)

**로컬 접속:**
```bash
# T3610 서버 내에서
curl http://localhost:8000/v3/sessions/list

# 또는 웹 브라우저
http://localhost:8000/docs
```

**LAN 접속 (같은 네트워크의 다른 머신에서):**
```bash
# T3610의 LAN IP 사용
curl http://192.168.100.200:8000/v3/sessions/list
http://192.168.100.200:8000/docs
```

**주요 엔드포인트:**
- `GET /v3/sessions/list` - 활성 세션 목록
- `POST /v3/messages/list` - 메시지 검색
- `GET /v3/peers/list` - 에이전트 피어 목록
- `/docs` - FastAPI 자동 문서 (Swagger UI)

### 2. 가상 오피스 (Virtual Office)

**로컬 접속:**
```bash
# T3610 서버 내에서
xdg-open http://localhost:3001

# 또는 웹 브라우저
http://localhost:3001
```

**LAN 접속:**
```bash
http://192.168.100.200:3001
```

**특징:**
- Honcho 활동 기록을 실시간 시각화
- 8종 RA 에이전트의 픽셀 캐릭터 배치
- 760×440 픽셀 아트 오피스 배경
- Docker 컨테이너로 구동 중

### 3. 성장 대시보드 (Growth Dashboard)

**웹 접속 (전 세계 어디서나 접속 가능):**
```bash
https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html
```

**특징:**
- GitHub Pages로 호스팅되어 외부 접속 가능
- RA 성장 지표 대시보드
- 에이전트별 성장 카드
- 시스템 건강 상태 모니터링

---

## 🔒 내부 전용 서비스 (로컬만 접속 가능)

### 4. n8n 워크플로우 자동화

**로컬 접속만 가능:**
```bash
# T3610 서버 내에서만 접속 가능
http://localhost:5678
```

**기본 인증 정보:**
- 사용자명: `admin`
- 비밀번호: `changeme_in_production` (운영 환경에서는 반드시 변경 필요)

**주요 워크플로우:**
- mail-triage: 이메일 트라이지 자동화
- infra-to-work-bridge: 인프라 투표 결과 전달
- feedback-recorder: 피드백 기록
- wp-close-recorder: WP 종료 기록

---

## 📱 모바일 앱 접속 방법

### Android (개인 핫스팟)

**Honcho API (내부 네트워크):**
```bash
# 핫스팟 설정 필요: LAN 고정 IP 또는 포트 포워딩
http://192.168.100.200:8000/v3/sessions/list
```

**가상 오피스:**
```bash
http://192.168.100.200:3001
```

**성장 대시보드:**
```bash
https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html
```

---

## 🛠️ 개발/테스트용 로컬 실행 방법

### Hermes 에이전트 직접 실행

```bash
# profiles/ 디렉토리에서
cd /home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent

# RA 전문가 에이전트 실행 (예: FDA 510(k) 질문)
hermes profile run ra-us "What are the FDA 510(k) requirements for Class II devices?"

# EU MDR 전문가 실행
hermes profile run ra-eu "What are the EU MDR requirements for medical devices?"

# MFDS 전문가 실행  
hermes profile run ra-kr "What are the MFDS requirements for medical device registration?"
```

### Honcho CLI 직접 사용

```bash
# 활성 세션 확인
honcho session list --peer ra_us

# 메시지 검색
honcho message search --peer ra_us "510(k)"

# 피어 목록 확인
honcho peer list
```

---

## 📊 서비스 포트 요약

| 서비스 | 포트 | 로컬 접속 | LAN 접속 | 외부 접속 |
|--------|------|----------|----------|----------|
| **Honcho API** | 8000 | ✅ `localhost:8000` | ✅ `192.168.100.200:8000` | ❌ 방화벽 |
| **가상 오피스** | 3001 | ✅ `localhost:3001` | ✅ `192.168.100.200:3001` | ❌ 방화벽 |
| **n8n** | 5678 | ✅ `localhost:5678` | ❌ 127.0.0.1 바인딩 | ❌ 방화벽 |
| **PostgreSQL** | 5432 | ✅ `localhost:5432` | ❌ 컨테이너 내부 | ❌ 방화벽 |
| **Redis** | 6379 | ✅ `localhost:6379` | ❌ 127.0.0.1 바인딩 | ❌ 방화벽 |
| **Qdrant** | 6333, 6334 | ✅ `localhost:6333` | ❌ 0.0.0.0 바인딩 | ❌ 방화벽 |

---

## 🔐 보안 주의사항

1. **외부 공개 금지**: Honcho API, 가상 오피스, n8n는 보안상 외부 인터넷에 공개하지 않습니다
2. **비밀번호 변경**: n8n 기본 비밀번호(`changeme_in_production`)는 운영 환경에서 반드시 변경하세요
3. **LAN 제약**: 원격지역 접속은 같은 LAN(로컬 네트워크) 내에서만 가능합니다
4. **방화벽 구성**: 현재 T3610 서버는 방화벽으로 구성되어 외부 접속이 제한됩니다

---

## 🚀 빠른 시작 가이드

### 1단계: 시스템 상태 확인
```bash
# 서비스 상태 확인
docker ps

# Honcho API 상태 확인
curl http://localhost:8000/v3/sessions/list
```

### 2단계: 가상 오피스 확인
```bash
# 웹 브라우저에서 가상 오피스 열기
xdg-open http://localhost:3001
# 또는
xdg-open http://192.168.100.200:3001
```

### 3단계: RA 에이전트와 대화
```bash
# RA 전문가에게 질문하기
hermes profile run ra-us "What are the key requirements for FDA 510(k) submission?"
```

### 4단계: 성장 대시보드 확인
```bash
# 웹 브라우저에서 성장 대시보드 열기
xdg-open https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html
```

---

## 📞 문제 해결

### 서비스 연결 불가
```bash
# 컨테이너 상태 확인
docker ps

# 컨테이너 로그 확인
docker logs honcho-api-1
docker logs virtual-office
```

### 포트 충돌
```bash
# 포트 사용 확인
netstat -tulpn | grep -E '8000|3001|5678'

# 프로세스 확인
ps aux | grep -E 'honcho|n8n|virtual'
```

---

**📅 최종 업데이트**: 2026-06-19  
**🎯 기준 환경**: T3610 서버, Ubuntu, Docker Compose  
**📧 문의**: GitHub Issue 또는 README.md 참조
