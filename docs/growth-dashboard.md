# Growth Dashboard 운영 문서

> 목적: 사람 사용자가 Git checkout 또는 웹 브라우저에서 RA Hermes의 지속 성장 상태를 빠르게 확인한다.

## 현재 결론

`docs/growth-dashboard.html`은 정적 HTML snapshot이다. 서버, 빌드, 외부 JavaScript, 외부 CSS, JSON fetch 없이 열린다.

이 dashboard는 자동성장을 실행하지 않는다. 다음 상태를 사람이 검토하기 쉽게 보여주는 읽기 전용 보고서다.

- 자동성장 readiness radar chart
- 자동성장 timer 상태등
- 성장 지표 timer 상태등
- pending / wrong-peer / JSON envelope / hyphen peer cleanliness 상태등
- `ra_us`, `ra_eu`, `ra_kr` self-doc balance bar
- curriculum seed count
- 최신 growth metrics
- growth report trend sparkline

## 바로 보는 방법

README에서 [성장 대시보드 바로보기](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html)를 클릭하면 GitHub Pages로 렌더링된 HTML이 열린다.

로컬 checkout에서:

```bash
xdg-open docs/growth-dashboard.html
```

또는 파일 매니저/브라우저에서 `docs/growth-dashboard.html`을 직접 연다.

GitHub 웹 파일 화면에서 `docs/growth-dashboard.html`을 직접 클릭하면 HTML이 렌더링되지 않고 소스가 보일 수 있다. 실제 화면으로 보려면 다음 중 하나를 사용한다.

- repo를 checkout한 뒤 브라우저에서 파일 열기
- README의 GitHub Pages 링크 사용
- raw HTML viewer를 통해 raw 파일 URL 렌더링

GitHub Pages 경로:

```text
https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html
```

GitHub Pages는 `main` branch의 `/docs` path 기준으로 활성화되어 있다.

## 갱신 절차

최신 reports와 systemd 상태를 반영하려면 다음을 실행한다.

```bash
python3 scripts/render-growth-dashboard.py
python3 scripts/verify-growth-dashboard.py
```

dashboard HTML이 바뀌면 일반 문서 변경과 동일하게 커밋한다.

```bash
git add docs/growth-dashboard.html
git commit -m "docs(#62): refresh growth dashboard snapshot"
git push origin main
```

## 데이터 출처

| 표시 영역 | 출처 |
|---|---|
| Readiness | `reports/auto-growth-readiness/*.json` 중 최신 파일 |
| Growth metrics | `reports/growth-YYYY-MM-DD.json` 중 최신 파일 |
| Growth trend sparkline | 최근 `reports/growth-*.json` |
| Timer status | `systemctl is-active/is-enabled hermes-auto-growth.timer` |
| Metrics timer status | `systemctl is-active/is-enabled ra-growth-metrics.timer` |
| Cleanliness | readiness report 내부 DB snapshot |
| Agent balance | readiness report 내부 `self_docs`, `seed_counts` |

## 판정 기준

| 항목 | 정상 판정 |
|---|---|
| Readiness | `16/16` |
| Timer recommendation | `approval_review_required` |
| Auto growth timer | `inactive/disabled` until explicit approval |
| Metrics timer | `active/enabled` |
| Pending | total 0, RA 0 |
| Wrong peer | 0 |
| Active JSON envelope | 0 |
| Hyphen peer | 0 |
| `ra_kr` balance | `ra_kr >= int(ra_eu * 0.2)` |

`approval_review_required`는 자동성장 production timer를 켰다는 뜻이 아니다. 명시 승인 후 activation guard를 통과해 켤 수 있는 상태라는 뜻이다.

## 현재 한계

2026-06-16 기준 `ra-growth-metrics.timer`는 active/enabled이고 `reports/growth-2026-06-16.json`까지 생성했다. 그러나 최근 growth reports는 `sessions_scanned=0`, `messages_scanned=0`이다.

따라서 현재 dashboard는 다음에는 충분하다.

- readiness / safety 상태 확인
- timer on/off 상태 확인
- agent balance 확인
- reports 생성 여부 확인

하지만 다음에는 아직 부족하다.

- 실제 업무/학습 이벤트 기반 성장 추세 판단
- 7일/30일 moving average 판단
- trigger threshold 자동 알림 판단
- 실시간 자동 갱신 dashboard

이 잔여 작업은 #62에서 계속 추적한다.

## `virtual-office`와의 차이

| 항목 | `docs/growth-dashboard.html` | `virtual-office/` |
|---|---|---|
| 목적 | 성장/안전 상태 점검 | 활동 이벤트 시각화 |
| 데이터 | reports + systemd snapshot | activity event stream |
| 형태 | radar/status light/bar/sparkline 기반 정적 HTML snapshot | 파일럿 웹 대시보드 |
| 운영 영향 | 없음, 읽기 전용 | 없음, 읽기 전용 |
| 현재 상태 | 구현됨 | 구현됨, 별도 목적 |

두 화면은 합치지 않는다. 성장 판단 dashboard와 활동 재생 dashboard는 사용 목적이 다르다.
