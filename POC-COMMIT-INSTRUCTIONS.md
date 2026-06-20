# POC 구현 변경사항 Git 커밋 가이드

> **생성일**: 2026-06-20  
> **목적**: 원격 작업 모드에서 POC 구현 변경사항을 git으로 관리

---

## 📋 변경사항 요약

### 신규 파일 (2개)
1. `docs/routing-visualization-spec.md` — 규제권 라우팅 시각화 명세서
2. `docs/virtual-office-integration-spec.md` — 가상 오피스 통합 설계

### 수정 파일 (1개)
3. `virtual-office/virtual-office.html` — 가상 오피스 POC 구현

---

## 🔄 Git 커밋 순서

### Step 1: 변경사항 스테이징

```bash
cd /home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent

# 모든 변경사항 스테이징
git add docs/routing-visualization-spec.md
git add docs/virtual-office-integration-spec.md  
git add virtual-office/virtual-office.html
```

### Step 2: 커밋 메시지

```bash
git commit -m "feat(#poc): 가상 오피스 Heat Map 시각화 POC 구현

## 변경사항
- docs/routing-visualization-spec.md: 규제권 라우팅 시각화 명세서
- docs/virtual-office-integration-spec.md: 가상 오픈스 통합 설계
- virtual-office/virtual-office.html: Heat Map POC 구현

## 주요 기능
- 3×3 Heat Map (FDA/EU/KR × High/Mid/Low confidence)
- Mock 데이터로 실시간 confidence 분포 표시
- 5분마다 자동 갱신 (랜덤 변화)
- 픽셀 아트 스타일 유지

## 기술 구현
- 메인 컨테이너 가로 분할 (760px + 300px)
- CSS 13개 규칙 추가
- HTML 40+ 라인 구조 추가
- JavaScript Mock 데이터 + 렌더링 + 갱신 타이머

## 테스트 방법
python3 -m http.server 8080
# 브라우저: http://localhost:8080/virtual-office/virtual-office.html

## 다음 단계
- 사용성 평가 후 MVP 진입
- Honcho API 실데이터 연동
- Trend Line + Gate Ratio 추가"
```

### Step 3: 원격지에서 적용 (T3610 서버)

```bash
# T3610 서버에서
cd /path/to/ra-hermes-multi-agent
git pull

# Docker 컨테이너 재시작 (POC 반영)
docker restart virtual-office

# 브라우저에서 확인
# http://localhost:3001 또는 http://192.168.100.200:3001
```

---

## 🧪 POC 테스트 체크리스트

### UI/UX 확인
- [ ] 가로 분할 레이아웃이 자연스러운지
- [ ] Heat Map 테이블이 가독성 있게 표시
- [ ] 색상 구분 (Green/Yellow/Red)이 명확한지
- [ ] "Last updated" 시각이 표시되는지

### 기능 동작 확인
- [ ] 초기값이 정확히 표시되는지 (FDA High=42, EU High=35, KR High=28)
- [ ] 5분 후 숫자가 변화하는지
- [ ] 기존 가상 오픈스 기능에 영향 없는지
- [ ] 캐릭터 이동, Kanban, 투표 연출이 정상 작동

### 브라우저 호환성
- [ ] Chrome/Edge 최신 버전
- [ ] Firefox 최신 버전
- [ ] Safari (Mac/iOS)

---

## 📊 MVP 진입 조건

POC 사용성 평가 후 아래 조건이 충족되면 MVP 진입:

1. **사용성 평가 완료**
   - UI 레이아웃 직관성 확인
   - 숫자 가독성 확보
   - 색상 구분 명확성 검증

2. **기술적 검증 완료**
   - 레이아웃 확장 기술 문제 없음
   - 데이터 갱신 메커니즘 안정적
   - 브라우저 호환성 확인

3. **이해관계자 피드백** (옵션)
   - 실제 RA 전문가 사용 의견
   - 개선 필요 사항 파악

---

## 🚀 일정

**POC 완료**: 2026-06-20
**MVP 시작**: POC 사용성 평가 완료 후
**MVP 기간**: 1-2주 예상 (Honcho API 연동 + Trend Line + Gate Ratio)

---

**📧 문의**: GitHub Issue 또는 README.md 참조
