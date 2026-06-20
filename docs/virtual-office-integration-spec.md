# 가상 오피스 업무 플로우 시각화 통합 설계

> **기준일**: 2026-06-20  
> **대상 파일**: `virtual-office/virtual-office.html`  
> **목적**: 기존 가상 오피스에 규제권 라우팅 시각화 기능 통합

---

## 1. 기존 가상 오피스 구조 분석

### 1.1 현재 구조 (461 라인 단일 HTML)

```
[Layout]
├─ 헤더: h1 + sub (제목 + 상태 설명)
├─ 컨트롤: 재생/정지/리셋 + 속도 조절
├─ 스테이지 (760×440)
│  ├─ work 영역 (62%)
│  │  ├─ kanban (상단 74px)
│  │  └─ character 이동 영역
│  └─ infra 영역 (38%)
│     └─ voting zone + character 배치
└─ 이벤트 로그 (하단)
```

### 1.2 데이터 연동 상태

```javascript
// 현재 구현 (L439-457)
async function initDataSource(){
  const cfg = await fetch('/api/config').then(r => r.json());
  if (cfg?.data_source === 'honcho') {
    const evts = await fetch('/api/events').then(r => r.json());
    ACTIVE_EVENTS = evts;  // Honcho 실데이터 로드
    // 30초마다 폴링
  }
}
```

**연동 가능한 엔드포인트**:
- `/api/config` — 데이터 소스 설정
- `/api/events` — Honcho 활동 기록 스트림

---

## 2. 시각화 통합 방안

### 2.1 레이아웃 확장 (가로 분할)

```
[기존 스테이지] [시각화 패널]
  760×440        300×440
```

**변경 사항**:
```html
<!-- 기존 -->
<div class="stage" style="width:760px;height:440px;">
  <!-- work + infra 영역 -->
</div>

<!-- 변경 후 -->
<div class="main-container" style="display:flex;gap:8px;">
  <div class="stage" style="width:760px;height:440px;">
    <!-- 기존 work + infra 영역 (그대로 유지) -->
  </div>
  
  <div class="viz-panel" style="width:300px;height:440px;">
    <!-- 업무 플로우 시각화 영역 -->
  </div>
</div>
```

### 2.2 시각화 패널 구조

```
[viz-panel: 300×440]
├─ 탭 헤더 (3개)
│  ├─ Heat Map (활성)
│  ├─ Trend Line
│  └─ Gate Ratio
├─ 탭 컨텐츠 영역 (280×380)
│  ├─ #tab-heatmap (3x3 행렬)
│  ├─ #tab-trend (차트)
│  └─ #tab-gate (파이 차트)
└─ 데이터 갱신 표시 (우측 상단)
   "Last updated: HH:MM:SS"
```

---

## 3. 구현 상세

### 3.1 CSS 추가 (기존 <style> 태그 내)

```css
/* 메인 컨테이너 */
.main-container {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  justify-content: center;
}

/* 시각화 패널 */
.viz-panel {
  width: 300px;
  height: 440px;
  background: var(--card);
  border: 4px solid var(--wall);
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 0 4px var(--bg), 0 10px 30px rgba(0,0,0,.5);
}

/* 탭 헤더 */
.viz-tabs {
  display: flex;
  border-bottom: 2px solid var(--line);
  background: var(--kanban);
}
.viz-tab {
  flex: 1;
  padding: 8px 4px;
  font-family: 'Press Start 2P';
  font-size: 8px;
  color: #9aa5e0;
  background: transparent;
  border: none;
  cursor: pointer;
  border-right: 1px solid var(--line);
}
.viz-tab:last-child { border-right: none; }
.viz-tab.active {
  background: var(--accent);
  color: var(--ink);
}

/* 탭 컨텐츠 */
.viz-content {
  flex: 1;
  padding: 8px;
  overflow-y: auto;
}
.viz-tab-content {
  display: none;
  height: 100%;
}
.viz-tab-content.active {
  display: block;
}

/* Heat Map */
.heatmap-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}
.heatmap-table th {
  color: var(--accent);
  padding: 4px;
  border-bottom: 2px solid var(--line);
}
.heatmap-table td {
  text-align: center;
  padding: 6px;
  border-bottom: 1px dashed var(--line);
}
.heatmap-high { color: var(--green); }
.heatmap-mid { color: var(--accent); }
.heatmap-low { color: var(--red); }

/* 데이터 갱신 표시 */
.viz-updated {
  position: absolute;
  top: 4px;
  right: 6px;
  font-size: 10px;
  color: #8b8ba7;
}
```

### 3.2 HTML 구조 추가 (<body> 내)

```html
<div class="main-container">
  <!-- 기존 stage (그대로 유지) -->
  <div class="stage" id="virtual-office-stage" style="width:760px;height:440px;">
    <!-- work + infra 영역 -->
  </div>
  
  <!-- 시각화 패널 (신규) -->
  <div class="viz-panel" style="position:relative;">
    <div class="viz-updated" id="viz-updated">Last updated: --:--:--</div>
    
    <div class="viz-tabs">
      <button class="viz-tab active" data-tab="heatmap">Heat Map</button>
      <button class="viz-tab" data-tab="trend">Trend</button>
      <button class="viz-tab" data-tab="gate">Gate</button>
    </div>
    
    <div class="viz-content">
      <div id="tab-heatmap" class="viz-tab-content active">
        <!-- Heat Map 렌더링 영역 -->
        <table class="heatmap-table" id="heatmap-table">
          <thead>
            <tr>
              <th>Region</th>
              <th>High</th>
              <th>Mid</th>
              <th>Low</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>FDA</th>
              <td class="heatmap-high" id="fda-high">-</td>
              <td class="heatmap-mid" id="fda-mid">-</td>
              <td class="heatmap-low" id="fda-low">-</td>
            </tr>
            <tr>
              <th>EU</th>
              <td class="heatmap-high" id="eu-high">-</td>
              <td class="heatmap-mid" id="eu-mid">-</td>
              <td class="heatmap-low" id="eu-low">-</td>
            </tr>
            <tr>
              <th>KR</th>
              <td class="heatmap-high" id="kr-high">-</td>
              <td class="heatmap-mid" id="kr-mid">-</td>
              <td class="heatmap-low" id="kr-low">-</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div id="tab-trend" class="viz-tab-content">
        <!-- Trend Line 차트 영역 -->
        <canvas id="trend-chart" width="270" height="340"></canvas>
      </div>
      
      <div id="tab-gate" class="viz-tab-content">
        <!-- Gate Ratio 파이 차트 영역 -->
        <canvas id="gate-chart" width="270" height="340"></canvas>
      </div>
    </div>
  </div>
</div>
```

### 3.3 JavaScript 기능 추가 (기존 <script> 태그 내)

```javascript
/* ===== 시각화 데이터 관리 ===== */
const VIZ_DATA = {
  heatMap: { FDA: { high: 0, mid: 0, low: 0 }, EU: { high: 0, mid: 0, low: 0 }, KR: { high: 0, mid: 0, low: 0 } },
  trend: [],
  gateRatio: { green: 0, yellow: 0, red: 0 },
  lastUpdated: null
};

/* 탭 전환 기능 */
document.querySelectorAll('.viz-tab').forEach(tab => {
  tab.onclick = () => {
    document.querySelectorAll('.viz-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.viz-tab-content').forEach(c => c.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(`tab-${tab.dataset.tab}`).classList.add('active');
    
    // 탭 전환 시 차트 렌더링
    if (tab.dataset.tab === 'trend') renderTrendChart();
    if (tab.dataset.tab === 'gate') renderGateChart();
  };
});

/* Heat Map 렌더링 */
function renderHeatMap() {
  const regions = ['FDA', 'EU', 'KR'];
  const levels = ['high', 'mid', 'low'];
  
  regions.forEach(region => {
    levels.forEach(level => {
      const cell = document.getElementById(`${region.toLowerCase()}-${level}`);
      if (cell) {
        cell.textContent = VIZ_DATA.heatMap[region][level] || 0;
      }
    });
  });
}

/* Trend Line 차트 렌더링 (Chart.js 라이브러리 필요) */
function renderTrendChart() {
  const ctx = document.getElementById('trend-chart').getContext('2d');
  
  // 데이터 포인트 추출
  const labels = VIZ_DATA.trend.map(d => d.date);
  const fdaData = VIZ_DATA.trend.map(d => d.FDA);
  const euData = VIZ_DATA.trend.map(d => d.EU);
  const krData = VIZ_DATA.trend.map(d => d.KR);
  
  // Chart.js 렌더링 (라이브러리 로드 필요)
  if (typeof Chart !== 'undefined') {
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          { label: 'FDA', data: fdaData, borderColor: '#41a6f6' },
          { label: 'EU', data: euData, borderColor: '#a7f070' },
          { label: 'KR', data: krData, borderColor: '#ffcd75' }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: { min: 0, max: 1.0, ticks: { color: '#8b8ba7' } },
          x: { ticks: { color: '#8b8ba7' } }
        },
        plugins: {
          legend: { labels: { color: '#e4e4ef' } }
        }
      }
    });
  } else {
    ctx.fillText('Chart.js 라이브러리 필요', 10, 50);
  }
}

/* Gate Ratio 파이 차트 렌더링 */
function renderGateChart() {
  const ctx = document.getElementById('gate-chart').getContext('2d');
  
  if (typeof Chart !== 'undefined') {
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Green', 'Yellow', 'Red'],
        datasets: [{
          data: [VIZ_DATA.gateRatio.green, VIZ_DATA.gateRatio.yellow, VIZ_DATA.gateRatio.red],
          backgroundColor: ['#a7f070', '#ffcd75', '#ef7d57']
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'bottom', labels: { color: '#e4e4ef' } }
        }
      }
    });
  } else {
    ctx.fillText('Chart.js 라이브러리 필요', 10, 50);
  }
}

/* 시각화 데이터 갱신 */
async function updateVisualization() {
  try {
    const response = await fetch('/api/analytics/routing-confidence');
    const data = await response.json();
    
    // 데이터 업데이트
    VIZ_DATA.heatMap = data.heat_map;
    VIZ_DATA.trend = data.trend;
    VIZ_DATA.gateRatio = data.gate_ratio;
    VIZ_DATA.lastUpdated = new Date();
    
    // 렌더링
    renderHeatMap();
    
    // 갱신 시각 표시
    document.getElementById('viz-updated').textContent = 
      `Last updated: ${VIZ_DATA.lastUpdated.toLocaleTimeString()}`;
  } catch (error) {
    console.error('시각화 데이터 갱신 실패:', error);
  }
}

/* 초기화 및 주기적 갱신 */
function initVisualization() {
  updateVisualization();
  setInterval(updateVisualization, 5 * 60 * 1000); // 5분마다 갱신
}

// 기존 initDataSource() 함수 내에서 호출
const originalInitDataSource = initDataSource;
initDataSource = async function() {
  await originalInitDataSource();
  initVisualization();
};
```

### 3.4 Chart.js 라이브러리 로드 (<head> 내)

```html
<!-- 기존 스타일 시트 아래에 추가 -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

---

## 4. 백엔드 API 엔드포인트 구현

### 4.1 Honcho API 확장 (`/api/analytics/routing-confidence`)

```python
# Honcho FastAPI 백엔드에 추가
from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/api/analytics/routing-confidence")
async def get_routing_confidence(period: int = 7):
    """
    규제권 라우팅 confidence 집계 데이터 반환
    
    Args:
        period: 집계 기간 (일수), 기본값 7일
    
    Returns:
        heat_map: 규제권별 confidence 구간 집계
        trend: 일별 confidence 추이
        gate_ratio: Green/Yellow/Red 게이트 비율
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period)
    
    # PostgreSQL에서 confidence 집계 (구현 필요)
    heat_map = await db.fetch_routing_heat_map(start_date, end_date)
    trend = await db.fetch_confidence_trend(start_date, end_date)
    gate_ratio = await db.fetch_gate_ratio(start_date, end_date)
    
    return {
        "period": f"{period}d",
        "heat_map": heat_map,
        "trend": trend,
        "gate_ratio": gate_ratio
    }
```

---

## 5. 구현 우선순위

### Phase 1: 기본 Heat Map (2-3일)
- [ ] 가상 오피스 HTML 레이아웃 확장 (가로 분할)
- [ ] Heat Map CSS 구현
- [ ] `/api/analytics/routing-confidence` 엔드포인트 구현
- [ ] 5분 주기 데이터 갱신

### Phase 2: 차트 라이브러리 통합 (1-2일)
- [ ] Chart.js CDN 로드
- [ ] Trend Line 차트 구현
- [ ] Gate Ratio 파이 차트 구현
- [ ] 탭 전환 기능 구현

### Phase 3: T자형 성장 연계 (2-3일)
- [ ] 성장률 계산 로직 추가
- [ ] Confidence 상승률 시각화
- [ ] 프랙탈 확장 패턴 표현

---

## 6. 성공 기준

### 6.1 기능적 완성도
- [ ] Heat Map이 실시간 confidence 분포를 정확히 표시
- [ ] Trend Line이 7일간 추이를 시각화
- [ ] Gate Ratio가 Green/Yellow/Red 비율을 표현
- [ ] 5분마다 자동 갱신

### 6.2 UI/UX 품질
- [ ] 픽셀 아트 스타일과 시각화 패널의 조화
- [ ] 탭 전환이 매끄럽게 작동
- [ ] 차트가 가독성 있게 렌더링

### 6.3 T자형 성장 연계
- [ ] 사용자가 confidence 상승을 시각적으로 인지
- [ ] 에이전트별 성장 추이를 파악 가능

---

## 7. 기술적 제약사항

### 7.1 라이브러리 의존성
- **Chart.js 4.4.0**: CDN 로드 필요
- **Honcho API**: `/api/analytics/*` 엔드포인트 구현 필요

### 7.2 브라우저 호환성
- **모던 브라우저**: ES6+ 지원 필요
- **Canvas API**: 차트 렌더링 필수

### 7.3 성능 고려사항
- **폴링 주기**: 5분 (과도한 API 호출 방지)
- **차트 렌더링**: 탭 전환 시만 렌더링 (불필요한 리소스 소모 방지)

---

**📅 작성일**: 2026-06-20  
**🎯 다음 단계**: Phase 1 구현 시작 (레이아웃 확장 → Heat Map CSS)
