# 테스트케일 망 환경용 접속 설정 가이드

> **테스트케일 망 환경 특화**: 공용 와이파이에서 안전하게 접속하기 위한 설정 방법  
> **대상**: 원격지역(집/카페/공유 와이파이)에서 T3610 서버의 RA Hermes 시스템 접속  
> **기준일**: 2026-06-19

---

## 🎯 추천 접속 방식 (테스트케일 망 환경)

### 1. Tailscale VPN (가장 권장) ✅

**설치 이유:**
- 🏠 **가정 IP 활용**: T3610의 사내 IP(`192.168.100.200`)를 집에서도 사용 가능
- 🔒 **보안성 강화**: 엔드투트 암호화된 터널, 별도의 포트 노출 없음
- 📱 **모바일 친화적**: 스마트폰에서도 안전하게 접속 가능
- 🌐 **DNS 제공**: `hermes.tailnet.ts.net` 같은 도메인으로 접속 가능

**T3610 서버에 Tailscale 설치:**

1. Tailscale 계정 생성 (무료): https://tailscale.com/
2. T3610 서버에 Tailscale 설치:
```bash
# Debian/Ubuntu
curl -fsSL https://tailscale.com/install.sh | sh

# 설치 후 로그인
sudo tailscale up
```

3. Tailscale 관리 콘솔에서 T3610 머신 등록
4. Tailscale IP 확인:
```bash
# T3610에서 Tailscale IP 확인
tailscale ip -4
```

5. 테스트케일 망에서 Tailscale 앱 설치 후 로그인
6. T3610의 Tailscale IP로 접속:
```bash
# Honcho API
http://<tailscale-ip>:8000/v3/sessions/list

# 가상 오피스
http://<tailscale-ip>:3001
```

### 2. NGROK 터널 (개발용 중간) ⚠️

**사용 이유:**
- ⚡ **빠른 설정**: 설치 없이 외부 URL 즉시 제공
- 🔧 **개발 테스트용**: API 테스트, 웹훅 검증에 편리
- ⚠️ **보안 주의**: 도메인 노출, HTTPS 필요, 개발용으로만 사용

**T3610 서버에 NGROK 에이전트 설치:**

1. ngrok.com 계정 생성
2. T3610에 ngrok 설치:
```bash
# 다운로드
wget https://bin.equinoxio.com/c/bNyNGuJ0xNad/ngrok-v3-stable-linux-amd64.zip
unzip ngrok-v3-stable-linux-amd64.zip

# 설치 후 인증
./ngrok authtoken <your-auth-token>
```

3. Honcho API 터널링:
```bash
./ngrok http 8000
# 출력: https://xxxx-xxxx-xxxx.ngrok.io
```

4. 가상 오피스 터널링:
```bash
./ngrok http 3001
# 출력: https://xxxx-xxxx-xxxx.ngrok.io
```

5. 생성된 외부 URL을 테스트케일 망에서 사용

**주의사항:**
- ⚠️ ngrok URL은 임시적이며 재시작마다 변경됨
- 🔒 보안 상 중요한 데이터는 테스트용만 사용
- 📝 무료 플랜은 연결 제한이 있을 수 있음

### 3. SSH 터널링 (개발자용) 🔧

**테스트케일 망 환경에서 사용:**

```bash
# 테스트케일 망에서 T3610로 SSH 터널링 생성
ssh -R 8000:localhost:8000 -R 3001:localhost:3001 user@192.168.100.200

# 테스트케일 망에서 접속
http://localhost:8000
http://localhost:3001
```

**단순한 포트 포워딩으로는 부족함:**
- T3610는 현재 로컬 바인딩(127.0.0.1)만 허용
- 외부 접속을 위해서는 SSH 터널링이나 VPN 필요

---

## 🌐 테스트케일 망 환경에서의 접속 URL

### Tailscale 사용 경우 (권장)

**예시 설정 (T3610 Tailscale IP: 100.100.50.50):**
```bash
# Honcho API (Swagger UI)
https://100.100.50.50:8000/docs

# 가상 오피스
https://100.100.50.50:3001

# API 직접 호출
curl https://100.100.50.50:8000/v3/sessions/list
```

### NGROK 사용 경우 (개발용)

**예시 URL (ngrok 자동 생성):**
```bash
# Honcho API
https://random-id.ngrok.io/docs
https://random-id.ngrok.io/v3/sessions/list

# 가상 오피스
https://random-id.ngrok.io
```

---

## 📱 모바일 앱에서 접속 (테스트케일 망)

### Tailscale 앱 사용 (권장)

1. Tailscale 앱 설치 (iOS/Android)
2. 로그인 후 T3610 조인에 참여
3. Tailscale DNS 활성화 (설정 → Advanced → Use Tailscale DNS)
4. 브라우저에서 다음 URL 접속:
   - Honcho API: `http://<tailscale-ip>:8000/docs`
   - 가상 오피스: `http://<tailscale-ip>:3001`

### 방화벽 우회 (테스트용)

T3610 방화벽을 일시적으로 해제하려면:

```bash
# T3610 서버에서 방화벽 해제 (일시적, 권장하지 않음)
sudo ufw allow 8000/tcp
sudo ufw allow 3001/tcp

# 또는 특정 IP에서만 접속 허용
sudo ufw allow from <테스트케일-망-IP> to any port 8000
sudo ufw allow from <테스트케일-망-IP> to any port 3001
```

**⚠️ 경고**: 이는 보안상 권장하지 않습니다. 사용 후에는 반드시 다시 차단하세요:
```bash
sudo ufw delete allow 8000/tcp
sudo ufw delete allow 3001/tcp
```

---

## 🔧 실용 설정 스크립트

### 1단계: T3610에서 Tailscale 설치 (T3610 서버)

```bash
# T3610 서버에서 실행
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
# 화면에 안내에 따라 계정 로그인
tailscale ip -4  # Tailscale IP 확인
```

### 2단계: 테스트케일 망에서 Tailscale 앱 설치

테스트켈 망 기기에 맞는 Tailscale 앱 설치:
- **Android**: Play Store에서 "Tailscale"
- **iOS**: App Store에서 "Tailscale"
- 앱 설치 후 로그인

### 3단계: 접속 테스트

```bash
# Tailscale IP로 접속 테스트
# (T3610에서 확인한 Tailscale IP 사용)
curl http://<tailscale-ip>:8000/v3/sessions/list
xdg-open http://<tailscale-ip>:3001
```

---

## 📊 포트 접속 테스트

### Honcho API 테스트

```bash
# 세션 목록 확인
curl -X GET http://<tailscale-ip>:8000/v3/sessions/list \
  -H "Content-Type: application/json"

# 피어 목록 확인
curl -X GET http://<tailscale-ip>:8000/v3/peers/list \
  -H "Content-Type: application/json"
```

### 가상 오피스 테스트

웹 브라우저에서 다음 URL 접속:
```bash
http://<tailscale-ip>:3001
```

---

## 🚨 보안 주의사항

### 테스트케일 망 환경 특화 주의사항

1. **공용 와이파이 보안**: 
   - ✅ Tailscale VPN 사용: 암호화된 연결, 안전
   - ⚠️ NGROK 사용: 개발 테스트용으로만 사용, 보안 데이터 주의
   - ❌ 방화벽 해제: 권장하지 않음, 보안 위험

2. **데이터 보호**:
   - ⚠️ 테스트 데이터만 사용: 실제 환자 데이터 사용 금지
   - 🔒 API 테스트시 읽답匿명화: 실제 규제 정보 사용 주의
   - 📝 테스트 결과 기록: 테스트 케이스별 결과 기록 유지

3. **접속 제한**:
   - 🕐 근무 시간 외 접속 자제
   - 👥 접속 로그 모니터링 강화
   - 🔓 불필요한 접속 차단

---

## 📞 문제 해결

### Tailscale 연결 불가

```bash
# T36T3610에서 Tailscale 상태 확인
sudo systemctl status tailscale
sudo tailscale status

# Tailscale IP 재확인
tailscale ip -4
tailscale status
```

### 포트 연결 불가

```bash
# T3610에서 방화벽 상태 확인
sudo ufw status

# 필요시 포트 개방 (일시적)
sudo ufw allow 8000/tcp
sudo ufw allow 3001/tcp
```

### DNS 문제

```bash
# Tailscale DNS 설정 확인
# Tailscale 앱 → 설정 → Advanced → Use Tailscale DNS 확인

# 또는 로컬 DNS 설정에 Tailscale DNS 추가
# 100.100.x.x (Tailscale DNS 서버)
```

---

## 🎯 추천 테스트 시나리오

### 시나리오 1: API 기능 테스트

1. Tailscale VPN 연결
2. Honcho API Swagger UI 접속
3. `/v3/sessions/list` 엔드포인트 호출
4. 응답 확인 및 데이터 검증

### 시나리오 2: 가상 오피스 테스트

1. Tailscale VPN 연결
2. 가상 오피스 웹페이지 접속
3. 픽셀 캐릭터 배치 확인
4. 이벤트 재생 테스트

### 시나리오 3: RA 전문가 대화 테스트

1. Tailscale VPN 연결
2. SSH로 T3610 접속
3. Hermes CLI로 에이전트 실행:
   ```bash
   hermes profile run ra-us "테스트 질문"
   ```
4. 응답 확인

---

## 📚 추가 참고 자료

- **Tailscale 문서**: https://tailscale.com/kb/1019/switches/
- **NGROK 문서**: https://ngrok.com/docs
- **SSH 터널링**: `man ssh`, `man ssh-keygen`
- **운영 가이드**: `docs/operations-guide.md`

---

**📅 최종 업데이트**: 2026-06-19  
**🎯 테스트케일 망 환경 최적화**  
**🔒 보안 강화 버전**
