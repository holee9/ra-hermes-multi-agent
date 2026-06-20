# 규제권 라우팅 시각화 명세서

> **기준일**: 2026-06-20  
> **목적**: T자형 성장 메커니즘의 시각화 핵심인 규제권 라우팅 confidence 추이를 실시간으로 모니터링

---

## 1. 시각화 구성 요소

### 1.1 Confidence Heat Map (3x3 행렬)

```
규제권: FDA | EU | KR
Confidence 구간별 라우팅 결과 집계
```

| Confidence 구간 | FDA | EU | KR |
|----------------|-----|----|----|
| High (0.8-1.0) | 🟢 N건 | 🟢 N건 | 🟢 N건 |
| Mid (0.5-0.8)  | 🟡 N건 | 🟡 N건 | 🟡 N건 |
| Low (0.0-0.5)  | 🔴 N건 | 🔴 N건 | 🔴 N건 |

**색상 의미**:
- 🟢 Green: 자동 라우팅 (Yellow 게이트 통과)
- 🟡 Yellow: 수동 검토 (Yellow 게이트 부분 통과)
- 🔴 Red: 사람 확인 (Yellow 게이트 전체 차단)

### 1.2 Confidence Trend Line (일별/주간/월간)

```
Y축: Average Confidence per Region
X축: Time (Daily/Weekly/Monthly)
선종: FDA (파랑), EU (녹색), KR (주황)
```

**데이터 포인트**:
```json
{
  "date": "2026-06-20",
  "regions": {
    "FDA": {"avg": 0.85, "count": 42},
    "EU": {"avg": 0.78, "count": 35},
    "KR": {"avg": 0.72, "count": 28}
  }
}
```

### 1.3 Gate Ratio Pie Chart

```
Green (자동): N건 (X%)
Yellow (수동): N건 (Y%)
Red (사람): N건 (Z%)
```

**자동화 성숙도 지표**:
- 1단계 (초기): Red ≥ 70%
- 2단계 (성장): Yellow ≥ 50%
- 3단계 (성숙): Green ≥ 60%

---

## 2. 데이터 소스 연동

### 2.1 Honcho API 엔드포인트

```bash
# confidence 분포 데이터 가져오기
GET /v3/analytics/routing-confidence?period=7d

# 응답 형식
{
  "period": "7d",
  "heat_map": {
    "FDA": {"high": 120, "mid": 45, "low": 12},
    "EU": {"high": 98, "mid": 52, "low": 18},
    "KR": {"high": 75, "mid": 38, "low": 22}
  },
  "trend": [
    {"date": "2026-06-14", "FDA": 0.82, "EU": 0.75, "KR": 0.70},
    {"date": "2026-06-15", "FDA": 0.83, "EU": 0.76, "KR": 0.71},
    ...
  ],
  "gate_ratio": {
    "green": 293, "yellow": 135, "red": 52
  }
}
```

### 2.2 가상 오피스 통합

```
가상 오피스 우측 패널에 "업무 플로우 모드" 추가
├─ Heat Map 탭
├─ Trend Line 탭
└─ Gate Ratio 탭
```

---

## 3. T자형 성장 시각화 연계

### 3.1 성장 지표 계산

**에이전트별 전문성 성장 = Confidence 상승률**

```javascript
// 예시: ra_us 에이전트 FDA 전문성 성장
const growthRate = (currentAvgConfidence - initialAvgConfidence) / initialAvgConfidence;

// 초기 baseline (bootstrap 직후)
const initial = 0.65;  // Yellow-heavy
// 현재 (일주일 후)
const current = 0.85;  // Green-dominant
// 성장률 = (0.85 - 0.65) / 0.65 = +30.8%
```

### 3.2 프랙탈 확장 시각화

```
[단계 1: 단일 규제권 성장]
ra_us: FDA confidence 0.65 → 0.85 (+30.8%)
ra_eu: EU confidence 0.62 → 0.78 (+25.8%)
ra_kr: KR confidence 0.58 → 0.72 (+24.1%)

[단계 2: 규제권 간 프랙탈 확장]
FDA 전문성 → EU 하위 영향력 분석
EU MDR → FDA 인정도 교차 검증
KR MFDS → 글로벌 harmonization 추이
```

---

## 4. 구현 우선순위

### Phase 1: 기본 Heat Map (1주일)
- [ ] Honcho API `/v3/analytics/routing-confidence` 엔드포인트 구현
- [ ] 3x3 Heat Map UI 구현 (가상 오피스 우측 패널)
- [ ] 실시간 데이터 갱신 (5분 interval)

### Phase 2: Trend Line 추가 (1주일)
- [ ] 일별/주간/월간 집계 쿼리 구현
- [ ] Trend Line 차트 라이브러리 통합 (Chart.js 또는 D3.js)
- [ ] 기간 선택기 UI 추가

### Phase 3: Gate Ratio와 성장 지표 (1주일)
- [ ] Gate Ratio Pie Chart 구현
- [ ] 에이전트별 성장률 계산 로직 추가
- [ ] T자형 성장 대시보드 연동

---

## 5. 기술 스택

### Frontend
- **가상 오피스 확장**: React + TypeScript
- **차트 라이브러리**: Chart.js (가볍고 확장 가능)
- **실시간 갱신**: Server-Sent Events (SSE) 또는 WebSocket

### Backend
- **Honcho API**: FastAPI + PostgreSQL
- **집계 쿼리**: pgvector로 미계산된 confidence 매트릭스 활용
- **캐싱**: Redis (5분 TTL)

---

## 6. 성공 기준

### 6.1 기능적 완성도
- [ ] Heat Map이 실시간 confidence 분포를 정확히 반영
- [ ] Trend Line이 최소 7일간 추이를 표시
- [ ] Gate Ratio가 Green/Yellow/Red 비율을 시각화

### 6.2 T자형 성장 연계
- [ ] 에이전트별 성장률이 confidence 상승으로 정량화
- [ ] 프랙탈 확장 패턴이 규제권 간 상관관계로 표현
- [ ] 사용자가 성장 단계를 시각적으로 인지

---

## 7. 향후 확장 가능성

### 7.1 예측 모델 연동
- **과거 confidence 추이** → **미래 성장 예측**
- ARIMA 또는 Prophet 시계열 모델로 다음 달 confidence 예측

### 7.2 이상 탐지
- **Confidence 급락** → **에이전트 퇴보 또는 이슈 알림**
- **Gate Ratio 불균형** → **특정 규제권에 편중 경고**

### 7.3 A/B 테스트 시각화
- **학습 전/후 confidence 비교**
- **커리큘럼 변경 효과 측정**

---

**📅 작성일**: 2026-06-20  
**🎯 다음 단계**: Phase 1 구현 시작 (Honcho API 엔드포인트 → Heat Map UI)
