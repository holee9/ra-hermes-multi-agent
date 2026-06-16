# Growth Dashboard 운영 문서

> 목적: 사람 사용자가 Git checkout 또는 웹 브라우저에서 RA Hermes의 지속 성장 상태를 빠르게 확인한다.

## 현재 결론

`docs/growth-dashboard.html`은 정적 HTML snapshot이다. 서버, 빌드, 외부 JavaScript, 외부 CSS, JSON fetch 없이 열린다.

이 dashboard는 자동성장을 실행하지 않는다. 첫 화면의 우선순위는 실제 운영 중 각 RA 담당자가 성장하고 있는지, 성장 신호가 어디서 끊겼는지, 사용자가 다음에 무엇을 확인해야 하는지를 보여주는 것이다.

- RA Growth Operations 요약
- 담당자별 성장 카드: foundation, KB depth, source coverage, operational evidence
- Growth Signal Flow: Knowledge Base → Operational Input → Feedback Signal → Expert Growth
- Growth Trend Verdict
- Growth Evidence Radar
- Coverage Guard Basis
- 자동성장 readiness matrix
- 성장 지표 timer 상태등
- pending / wrong-peer / JSON envelope / hyphen peer cleanliness 상태등
- 최신 growth metrics
- growth report trend sparkline

첫 화면에서 매일 확인할 필수 현황은 RA Growth Operations 요약, 담당자별 성장 카드, Growth Signal Flow 3개다. 그 아래의 readiness, coverage guard, raw metrics, trend table은 기본 접힘 상태의 "검증/감사 상세"이며, 결론을 검산하거나 이슈 기록에 근거가 필요할 때만 펼친다.

검증/감사 상세가 필요한 이유:

- 결론 검산: 상단의 성장 추세 문구가 latest report의 `sessions_with_messages`, `messages_scanned`, `ingestion_diagnostics.empty_cause`와 일치하는지 확인한다.
- 병목 위치 확인: Operational Input이 막힌 것인지, 피드백/정확도 지표가 부족한 것인지 구분한다.
- 커버리지 오판 방지: KB/source floor 통과를 전문가 성숙도와 혼동하지 않도록 근거를 확인한다.
- 이슈 기록 근거: GitHub issue에 남길 수치, 파일명, readiness/cleanliness 상태를 확인한다.

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
| Depth Proxy / Source Coverage | readiness report 내부 `self_docs`, `seed_counts` + `scripts/coverage-guards.json` |
| Coverage Guard Basis | `scripts/coverage-guards.json` |
| Expert maturity targets | `scripts/growth-targets.json` |

## 판정 기준

| 항목 | 정상 판정 |
|---|---|
| RA Growth Operations | 최근 보고서의 `sessions_scanned`, `messages_scanned`, 14-report 누적 input/insight를 첫 화면에 표시 |
| 담당자별 성장 카드 | `ra_us`, `ra_eu`, `ra_kr` 각각 foundation, source, operational evidence를 분리 표시 |
| Growth Trend Verdict | `sessions_scanned > 0` 및 `messages_scanned > 0`이고 행동/피드백 지표가 target range에 들어와야 판정 가능 |
| Growth Evidence Radar | Depth/Source/Safety는 foundation proxy, Behavior/Feedback은 실제 행동/사람 평가 데이터 기반 |
| Readiness | `16/16` |
| Timer recommendation | `approval_review_required` |
| Auto growth timer | `inactive/disabled` until explicit approval |
| Metrics timer | `active/enabled` |
| Pending | total 0, RA 0 |
| Wrong peer | 0 |
| Active JSON envelope | 0 |
| Hyphen peer | 0 |
| Source Coverage | `scripts/coverage-guards.json`의 담당자별 expected explicit sources 이상 |
| Depth Proxy | `scripts/coverage-guards.json`의 담당자별 self-doc floor 이상 |
| Legacy KR/EU guard | `ra_kr >= int(ra_eu * 0.2)`는 legacy_pre_activation_floor일 뿐 전문가 성숙도 기준이 아님 |

`approval_review_required`는 자동성장 production timer를 켰다는 뜻이 아니다. 명시 승인 후 activation guard를 통과해 켤 수 있는 상태라는 뜻이다.

`scripts/coverage-guards.json`의 20% KR/EU relative guard는 #60에서 KR corpus가 EU 대비 거의 비어 있는 상태로 남지 않게 막기 위한 임시 pre-activation floor였다. 이 값은 규제 전문성, 업무 정확도, 사람 평가 통과율을 의미하지 않는다. 전문가 성숙도는 `correction_rate`, `first_pass_match_accuracy`, `warmstart_lift`, `confidence_calibration`, `escalation_precision`, human feedback coverage 같은 행동 지표와 사람 평가 데이터로만 판단한다.

## 현재 한계

2026-06-16 #64 보정 전에는 `reports/growth-2026-06-16.json`까지 생성됐지만 `sessions_scanned=0`, `messages_scanned=0`이었다. 원인은 collector가 Honcho v0.15.1 list API를 `GET /sessions`로 호출한 것이다. 실제 API 계약은 `POST /sessions/list`, `POST /sessions/{id}/messages/list`다.

보정 후 `reports/growth-diagnostic-2026-06-16.json`은 `sessions_listed=32`, `sessions_with_messages=27`, `messages_scanned=302`, `empty_cause=metrics_input_available`을 기록한다. scheduled daily report는 다음 `ra-growth-metrics.timer` 실행부터 같은 collector 계약을 따른다.

따라서 현재 dashboard는 다음에는 충분하다.

- 담당자별 KB foundation과 source coverage 확인
- 운영 성장 데이터가 실제로 들어오고 있는지 확인
- 성장 신호가 Knowledge Base 이후 Operational Input에서 끊겼는지 확인
- KR/EU legacy pre-activation floor가 전문가 성숙도 기준이 아님을 확인
- reports 생성 여부 확인

현재 결론은 "metrics ingestion은 복구됐지만, 30일 유효 metrics와 충분한 사람 평가 coverage가 없어 자동성장 threshold나 form 이관을 아직 확정할 수 없다"이다.

하지만 다음에는 아직 부족하다.

- 30일 유효 metrics 기반 성장 추세 판단
- RA 담당자별 "지구 최강 전문가" 근접도 판정
- 7일/30일 moving average 판단
- trigger threshold 자동 알림 판단
- 실시간 자동 갱신 dashboard

dashboard 표시 잔여 작업은 #62에서, threshold/webhook 정책은 #65에서 계속 추적한다.

## `virtual-office`와의 차이

| 항목 | `docs/growth-dashboard.html` | `virtual-office/` |
|---|---|---|
| 목적 | 성장/안전 상태 점검 | 활동 이벤트 시각화 |
| 데이터 | reports + systemd snapshot | activity event stream |
| 형태 | radar/status light/bar/sparkline 기반 정적 HTML snapshot | 파일럿 웹 대시보드 |
| 운영 영향 | 없음, 읽기 전용 | 없음, 읽기 전용 |
| 현재 상태 | 구현됨 | 구현됨, 별도 목적 |

두 화면은 합치지 않는다. 성장 판단 dashboard와 활동 재생 dashboard는 사용 목적이 다르다.
