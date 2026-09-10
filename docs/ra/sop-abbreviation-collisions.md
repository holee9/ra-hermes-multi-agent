# 사내 SOP 파일명 약어 ↔ FDA/규제 제도 약어 충돌 목록 (#146 DoD 2)

> 근거: pgvector `ra_knowledge`의 `source_path` 실측(2026-09-10, `SOP-<CODE>-NNN` 패턴 34종, MD-process 원본 125개 소스). 원본 KB(MD-process / ra-project / llm-wiki)는 이 레포에서 **읽기 전용**이며 파일명을 바꾸지 않는다 — 충돌은 **프롬프트/응답 측에서 문맥으로 해소**한다.
> 관측된 오독(#146): `SOP-PMA-001`의 PMA를 Premarket Approval로 읽어 Class III/PMA 경로를 구성(케이스 04·24), `RTA`를 "real-time analysis"로 읽어 존재하지 않는 무선 센서 기기를 창작(32), `PCCP`를 "Pre-Certification Collaborative Program"으로 확장(07·19).

## 1. 판정 규칙 (positive framing — 금지 문구 아님)

1. **파일명의 `SOP-<CODE>-NNN`에서 `<CODE>`는 사내 절차 식별자다.** 그 뜻은 아래 표의 "사내 의미" 열과 파일명 뒤 한글 제목이 결정한다. FDA/EU 제도 약어로 읽는 것은 본문에 그 제도가 실제로 등장할 때만이다.
2. FDA 제도 약어(PMA, RTA, PCCP, AI, De Novo, HDE 등)는 **21 CFR 파트·FDA 가이던스 제목이 함께 있을 때** 그 의미다. 파일명만으로 제도를 추정하지 않는다.
3. 같은 약어가 양쪽에 있으면 답변에서 **풀네임을 한 번 명시**한다: "SOP-PMA-001(프로세스 모니터링·분석 절차)". 풀네임을 정할 수 없으면 "약어 의미 확인 필요"로 남긴다.

## 2. 충돌 목록 (사내 SOP 코드 기준)

| 사내 코드 | 사내 의미 (파일명 제목) | 충돌하는 규제/일반 약어 | 위험 | 해소 단서 |
|---|---|---|---|---|
| **PMA** | 프로세스 모니터링·KPI 매트릭스 (ISO 13485 8.1/8.2.5/8.5.1) | FDA **Premarket Approval** (21 CFR 814) | **높음** — 케이스 04·24 오독 실증 | 파일명 제목이 "프로세스모니터링", 본문에 Part 814·Class III 언급 없음 |
| **RA** | 책임권한 및 내부소통 (ISO 13485 5.5) | **Regulatory Affairs** / 이 시스템의 RA 에이전트 명칭 | 높음 — 시스템 전반에서 RA=규제업무로 쓰임 | `SOP-RA-002`는 조직 책임·권한 절차 |
| **QP** | 품질정책 및 목표관리 (5.3/5.4) | EU **Qualified Person**(의약품) / MDR PRRC와 혼동 가능 | 중 | 의료기기 MDR에는 QP 제도 없음(PRRC, Art.15) |
| **CA** | 고객자산 관리 (7.5.10) | **Corrective Action**(CAPA의 CA), Competent Authority(EU) | 중 | 시정조치는 별도 `SOP-CAPA-001` |
| **IA** | 내부감사 (Internal Audit) | Information Assurance / Impact Assessment | 낮음 | 제목 "내부감사" |
| **MR** | 경영검토 (Management Review) | Medical Record / Magnetic Resonance / FDA **MDR**(Medical Device Reporting)과 한 글자 차이 | 중 | `SOP-MR-001`은 경영검토; 유해사례 보고는 `SOP-PMS-001` |
| **DT** | 설계이관 (Design Transfer) | Digital Twin / Drug Trial | 낮음 | 제목 "설계이관" |
| **CC** | 변경통제 (Change Control) | Clinical Chemistry(Part 862) / Common Criteria | 낮음 | 제목 "변경통제" |
| **CVD** | 조정된 취약점 공개 정책 (Coordinated Vulnerability Disclosure) | Cardiovascular Disease | 중 — 순환기 기기 문맥에서 오독 가능 | 제목·본문이 사이버보안 |
| **NC** | 부적합제품 관리 (Nonconformance) | Non-Clinical / National Competent (Authority) | 낮음 | 제목 "부적합제품" |
| **SUP** | 공급자 감사·재평가 (Supplier) | PMA **Supplement** | 낮음 | 510(k)에는 supplement 제도가 없음(#146 인접 결함) |
| **AIDATA / AIGOV** | AI 데이터셋 관리 / AI 공정성·설명성·드리프트 거버넌스 (Artificial Intelligence) | FDA **AI = Additional Information** request (510(k) 심사 중 추가자료 요청) | **높음** — 케이스 16·31에서 AI 응답 기한을 30일로 창작 | "Additional Information"은 심사 절차, "AI"가 기기 기술이면 AI/ML |
| **PMS / PSUR / FSCA / UDI / CAPA / RM / DHF / SBOM** | 시판후감시 / 정기안전성보고 / 현장안전시정조치 / UDI / 시정예방조치 / 위험관리 / 설계이력파일 / SBOM | 동일 의미 (충돌 없음) | 없음 | 그대로 사용 |

비-SOP 소스에서 관측된 약어:

| 약어 | 실제 의미 (KB 소스) | 오독 사례 | 해소 단서 |
|---|---|---|---|
| **RTA** | FDA 510(k) **Refuse to Accept** 체크리스트 (`13_규제평가_체크리스트/FDA_510k_RTA.md`) | "real-time analysis" → 무선 센서 기기 창작(케이스 32) | RTA는 접수 심사 절차. 기기 기능이 아님 |
| **PCCP** | FDA **Predetermined Change Control Plan** (2024-12 최종 가이던스) | "Pre-Certification Collaborative Program"으로 확장(07·19) | ra-us SOUL §Change-control terminology에 이미 풀네임 명시 — 문맥 무시가 원인이므로 규칙 1·2로 보강 |
| **AI** | 510(k) 심사 중 **Additional Information** 요청 | 응답 기한 30일 창작(16·31) — FDA 절차상 formal AI 요청의 완전한 답변은 180 calendar days | 절차 약어와 기술 약어 구분 |

## 3. 제안 — ra-us SOUL 추가 문단 (positive framing, 승인 후 반영)

> ### Document-name abbreviations vs FDA programs
> An in-house procedure file is named `SOP-<CODE>-NNN_<Korean title>`; `<CODE>` identifies the procedure, and its meaning is given by the Korean title (e.g. `SOP-PMA-001` is the *process monitoring & KPI matrix* procedure under ISO 13485 8.1/8.2.5/8.5.1; `SOP-RA-002` is *responsibility, authority & internal communication*; `SOP-CA-001` is *customer property*). An FDA program abbreviation — PMA (Part 814), RTA (510(k) Refuse-to-Accept checklist), PCCP, AI (Additional Information request during 510(k) review) — applies when the source text discusses that program. When both readings are possible, state the full name once in the answer and, if the source does not settle it, say the abbreviation needs confirmation.
>
> 510(k) submissions have no "supplement"; supplements belong to PMA (Part 814). FDA's formal Additional Information request gives 180 calendar days for a complete response. Class IIb and Field Safety Notice are EU (MDR) terms and do not belong in a US pathway table.

반영 순서(#146 DoD 3·4): SOUL 개정 → 배포(`profiles/setup.sh` 경로) → 캐시 반영 확인 → 해당 12건 **재질의**로 해소 확인. 사전 추가만으로 완료 선언하지 않는다(리뷰 지적).
