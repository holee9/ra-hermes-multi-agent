# RA Hermes 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 **정확성·신뢰성 우선** 학습 멀티 에이전트 시스템. 에이전트는 사람 RA 전문가를 *보조*한다.
> Hermes Agent v0.15.1 / Honcho v0.15.1 기반. 사실 기준일: 2026-06-21.

**[사용 가이드 →](docs/usage-guide.md)** | [📘 인터랙티브 사용 매뉴얼](docs/user-guide-korean.html) | [마스터 설계서 (Hermes v0.15.1)](docs/RA-multi-agent-master-design.md) | [구현 명세](docs/implementation-spec.md) | [운영 전략](docs/operations-guide.md) | [🌐 원격 접속 가이드](docs/remote-access-guide.md) | [🔧 테스트케일 망 설정 가이드](docs/tailscale-setup-guide.md) | [성장 대시보드 바로보기](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html) | [대시보드 운영 문서](docs/growth-dashboard.md)

GLM-5.2/Z.ai 전환은 [GLM-5.2 설정 메모](docs/glm-5.2-setup.md)를 따른다. 기본 운영 경로는 GX10 `gpt-oss:120b`이며, `scripts/configure-glm.sh`로 필요한 프로파일만 OpenAI-compatible GLM endpoint로 바꿀 수 있다.

---

## 현재 상태

**✅ 구축 완료 · 인터랙티브 사용 매뉴얼 배포 · 상세 스크린샷 시스템 완료(19개) · 시스템 운영 가이드 제공** | 최종 갱신: 2026-07-24

**최신 완료 작업:**
- ✅ **#133 PSUR 템플릿 Art.86 KB 소스 오류(하위항 라벨 4/5 + IIb 주기) — 소스 교정 + pgvector 전파 + 검증, CLOSE** (2026-07-24, ra-project commit `3eb44ec`): 에이전트 날조 아닌 **KB 원본 데이터 오류**(#127/#128 클래스), #132 작업 중 발견. EUR-Lex CELEX:32017R0745 Art.86 원문으로 독립 재검증(2차 출처 eumdr.com이 "IIa도 매년"으로 오기 → 원문·다수 출처·문서 자체 L46 일치로 기각). `PSUR_템플릿_MDR_Article86.md`: (1) Art.86(1) 하위항 라벨 재매핑 — (a)=benefit-risk(Sec6)·(b)=PMCF(Sec7)·(c)=판매량(Sec2), 존재하지 않는 (d)/(e)와 오배치 (a)를 제거하고 Art.86(1) 본문 인용으로 교체(Sec3/4/5/8 + 체크리스트 3건); (2) Art.86(2) 주기 정정 — Class IIb·III=매년 / IIa=2년마다, L21-22 주기표 + L25/L36/L45 자기모순 정합화. GitHub push → pgvector `ra_knowledge` 재인덱싱(DELETE 19청크, 백업 `backups/ra_knowledge-PSUR_Article86-pre133-2026-07-24.jsonl` → 재삽입 19, new=1/skipped=135). **retrieval store 직접 검증**: 옛 (d)/(e)·`IIa/IIb 2년마다` 잔존 0, 정정 라벨·주기·v1.1 헤더 전부 존재. 라이브 Qdrant는 03:18 자동 동기화. #132가 "에이전트 발명"으로 오진했던 결함의 상당 부분이 실은 이 소스 오류 전파였음이 근본 해결됨.
- ✅ **#131 Rule↔Class 불일치 + Class↔Annex route 매핑, #130 라벨링/위험관리 Annex 오배치 — Class→Annex 경로 표 신설 + 재-eval 검증, 둘 다 CLOSE** (2026-07-21): "#131/#130(같은 패턴 신규 착수)" 요청으로 두 이슈를 한 세션에서 처리. 재조사 결과 #130의 라벨링(Annex I Ch.III §23)/위험관리(Annex I GSPR+ISO 14971) 항목과 #131의 Rule→Class 고정값 표는 #123 라운드3 positive framing 재작성 때 이미 반영돼 있었음 — 남은 진짜 작업은 #131의 **Class→Annex 적합성평가 경로 표 신설**뿐이었음. EUR-Lex MDR Art.52 원문(2개 출처 교차검증)으로 Class I 자기선언 / Is·Im·Ir→Annex IX Ch.I&III 또는 Annex XI Part A / IIa→Annex IX(+§4) 또는 Annex II&III+Annex XI §10·18 / IIb→Annex IX(+§4) 또는 Annex X+XI / III→Annex IX 또는 Annex X+XI 표를 `ra-eu` SOUL.md에 신설(백업 `SOUL.md.bak-pre-130-131`). 표본 재현 테스트 5건(Class IIa 경로·DoC 근거·Rule 17·라벨링·위험관리) 전부 정상 확인 후, 신규 배치(2026-07-24 dated, 45케이스, 캡처 실패 0건) ra_eu 15건 팩트체크: **Rule→Class 불일치 0/15, Class IIa→Annex X 오배치 0/15(직전 배치 4/15로 단일 최다빈발이었음), DoC→Annex IX §3 오인용 0/15, 라벨링 Annex VI/VII 오인용 0/15, 위험관리 Annex XVII 오인용 0/15** — 5개 결함 패턴 전부 소거 확인.
  - **잔여 관찰(신규 이슈 미등록, 헤지된 경계선 사례)**: `it02-ra_eu-003`에서 GUI Software 분류 근거를 Rule 11 대신 "MDR §22"로 인용(최종 Class 값 IIa 자체는 정확)했고, X-ray Detector에 "Rule 17→IIa; 능동 소스와 연결 시 IIb로 상향될 수 있음"이라는 헤지 표현이 관찰됨 — Rule 17 자체엔 상향 경로가 없으나 "복합기기 구성요소" 논리로 프레이밍돼 원 #131 결함(근거 없는 단정적 발명)과는 결이 다름. 확정 결함으로 보기 어려워 별도 이슈는 등록하지 않고 참고로만 기록.
- ✅ **#129 ra_kr 구체 규정번호 창작 — 식별자 원칙 일반화 + 재-eval 검증, CLOSE** (2026-07-23): #124가 OECD/CER 문장에만 국한돼 모델이 다른 주제에서 한국 고시번호 계속 발명(소스 대조로 전부 모델 발명 확인). 공유 Citation rule(`build_case_content`, 전 에이전트) case(2)를 device 번호 + 구체 dated 규정번호(고시/notice/decree) + 특정 조/항/호까지 확장 + ra-kr SOUL.md Fixed Rule 6(구체 규정번호는 소스에서, 발명 금지) + OECD MAD(비임상 GLP) vs 임상 CER 구분. positive framing(#123 R2 교훈). 신규 배치 45케이스(캡처 실패 0) ra_kr 15건 결정론적 측정: **소스에 없는 규정번호 발명 5→0, OECD MAD 혼용 1→0**. 규정번호 언급 2건은 둘 다 소스 실재 정당 인용, 헤징 9/15. daily-growth는 반영됨, 라이브는 서비스 재시작 대기.
- ✅ **#128 ra_kr 감사문서 뒤집기 — 근본원인은 KB 데이터+검색 거버넌스(프롬프트 아님), CLOSE** (2026-07-19, commit `87844`계열): 프롬프트 수정 2회 실패 후 실제 소스 정밀조사로 **2층 근본원인** 확인. (A) 자매 규제문서 5개가 stale 20722 인용 — GitHub 원본은 이미 2026-07-10 audit #947로 20139 정정됐으나 pgvector만 stale(인덱서 skip, #127과 동일) → 재인덱싱(백업 190청크). (B) `issue-drafts/`가 인덱싱 제외에 없어 947 감사문서(수정지시서)가 검색돼 모델이 "20722는 오류"를 "20722를 표준으로" 뒤집음 → **issue-drafts/(302문서·1310청크·전체 KB 19%, 프로세스 메타)를 3개 제외 지점에 추가**(#112 거버넌스 패턴, 삭제 아닌 검색 필터링=가역적). 정답 20139는 law.go.kr 3중 검증. **모델 재현 검증**: 20139(정답) 2회, 20722(오류) 0회. 프롬프트 2회 실패는 증상만 공격한 것 — 에이전트 탓 전에 KB 원본 확인 교훈. Qdrant 라이브는 서비스 재시작+03:18 동기화 대기.
- ✅ **#127 KB 소스 오류(FDA_QMSR_2026.md §820.30) 수정 + 프로덕션 전파 + 재-eval 검증, CLOSE** (2026-07-19): 에이전트 창작이 아닌 **KB 원본 데이터 오류** — eCFR/Cornell LII(89 FR 7523) 검증 후 `MD-process/FDA_QMSR_2026.md` 2.2 구조표 정정(§820.30만 아니라 §820.20/§820.25/§820.198 등 구 QSR 번호를 활성 조항처럼 서술한 행 전체를 검증 구조로 교정 — 실재 활성은 §820.1·3·7·10·35·45뿐, 설계관리=ISO 13485 §7.3). GitHub main 푸시 → pgvector `ra_knowledge` 재인덱싱. **인덱서 동작 발견**: 이미 DB에 있는 파일은 skip(`--force` CLI 없음) → 변경 파일은 백업(19청크) 후 삭제→재인덱싱으로 처리. 재-eval 검증(정정 소스 검색 재현): §820.30=설계관리 오단정 소멸, "reserved §820.20–820.30 → ISO 13485 §7.3" 정확 서술. Qdrant 라이브 서빙은 매일 03:18 자동 동기화.
- ✅ **#126 ra_us CFR Part 862/892 오분류 + §830.7·PCC 혼동 — positive framing 수정 + 재-eval 검증 완료, CLOSE** (2026-07-21): 전 사실 eCFR/Cornell LII 검증 후 `ra-us` SOUL.md에 "FDA Citation Reference" 섹션 신설(금지 문구 0건, positive framing — CFR part map, Part 892 영상 섹션표, Part 830 구조, PCCP 용어). 신규 배치 45케이스(캡처 실패 0건) ra_us 15건 결정론적 측정: **영상→862 오분류 3→0, §830.7 1→0, PCC 혼동 1→0** 전건 소거. 인용 조항 전수 검증(892.2050 / 830.10·60·300 전부 실재, 862 인용 0) — **창작 재이동 없음**. kb-eval는 SOUL.md 매 실행 로드로 반영, 라이브는 서비스 재시작 대기.
- ✅ **#135 허위 자기검증 + 방어 마커 오발화 — positive framing 수정 + 재-eval 검증 완료, CLOSE** (2026-07-20, commit `db2ceda`+`be112bc`): `daily-growth-runner.py` `build_case_content()` Citation rule 재작성(금지 문구 아닌 positive framing, #123 R2 교훈). 신규 배치 45케이스(캡처 실패 0건) ra_eu 15건 결정론적 측정:
  - **문제1 허위 자기검증**: baseline 1/15 → **0/15 완전 해소**("정확성은 사람 검토자가 확인, 규제 판단으로 마무리" 긍정 서술이 자기검증 문장 자리 제거).
  - **문제2 마커 오발화**: 마커 8개 **전부 케이스 레벨 식별자에 정상 발화, 확립된 참조(Rule/Annex/Art) 인접 오발화 0건**(baseline은 Rule 번호 옆 3회 스탬프). Rule 번호 79회 사실 서술. 개수(5→6케이스)가 아니라 성격이 "늑대소년→정상용도"로 전환됨 — 인용을 (1)확립된 참조=사실 서술 / (2)케이스 레벨 식별자=마커로 구분한 결과.
  - **보너스**: #134 C1 자동 감지 블록이 `it01-ra_eu-004`에서 Art.86(1)(d) 자동 감지(#133 KB 소스 오류 전파분) — 코드 레벨 검증기 실배치 실증.
- 🛠️ **#134 옵션 B(코드 레벨 인용 검증기) 구현 — C1 배포, C2는 측정 후 폐기** (2026-07-18, commit `c33d17e`): 4회 연속 관측된 "창작 재이동"에 대한 코드 레벨 대응. `scripts/ra_citation_lint.py` 신규(EUR-Lex 검증 레지스트리, 무의존·무네트워크 순수 모듈).
  - **C1(존재하지 않는 Article 하위항, 예: Art.86(1)(d)) → 배포**: 순수 구조 검사라 표 안전·결정론적. 2026-07-19 실배치 오프라인 측정 **2건 적발 전부 true, 오탐 0**. `validate_advisory`에 계층형 hard-gate(신규 `yellow_reason "citation_error"`) + kb-eval 자동 감지 블록.
  - **C2(주제↔인용 의미적 모순, 예: SSCP→Art.66) → 배포 안 함**: 근접성 기반. 실배치 측정 **107→76→10건 전부 오탐**(규제 문서 표·리스트 밀집으로 문자 근접성 짝짓기 불가). 배포 시 검토자가 모든 경고를 무시하게 됨(#135 문제) → `@MX:DEBT`로 코드 보존, 구조 파싱 재설계 시 재검토.
  - **전략 결론(#134 질문에 대한 답)**: 코드 레벨 검증은 **구조적 하위클래스(존재 불가 식별자)만** 깨끗이 해결, **의미적 하위클래스(맞는 식별자·틀린 주제)는 미해결** → A(페르소나 표)+C(사람 검토)가 여전히 담당. B는 대체가 아니라 보완.
  - 검증: 신규 `test_citation_lint.py` 16종 + `test_advisory.py` 게이트 3종, **전체 63 passed**. 회귀 없음. 라이브 게이트는 서비스 재시작 블로커로 실배포 보류(코드만).
- ✅ **#132 ra_eu 하위 식별자 창작 — 표적 결함 5종 전건 해소, #123 close** (2026-07-19, commit `d0a0a91`): EUR-Lex 원문·IEC webstore로 전 사실 검증 후 positive framing으로 Post-market Article 표(Art.83-88 + Art.86(1) 3개항 + 주기)·Annex I 구조(23 GSPR)·X-ray IEC 표준표·하위 식별자 인용 원칙 추가. 신규 배치 45케이스(**캡처 실패 0건**) ra_eu 15건 전수 팩트체크 결과: **IEC 표준 오용 6→0 · Art.87 혼동 4→0 · Art.86(1) 하위구조 발명 1→0 · PSUR 주기 날조 1→0 · GSPR § 라벨 3→0** 전건 해소. **페르소나 참조표가 나쁜 소스를 이긴 사례 확인**(it02-004가 #133 오류 소스의 뒤바뀐 (a)/(b) 라벨을 따르지 않고 규정 원문대로 정정).
  - **⚠️ 작업 중 자기 오진 발견·정정**: #132 본문에 "Art.86(1) 하위구조를 에이전트가 발명"이라 진단했으나, KB 원본을 직접 열람하니 **소스 문서가 그렇게 적어놓은 것**이었음(`PSUR_템플릿_MDR_Article86.md`가 Art.86(1)을 (a)~(e) 5개항으로 표기, 실제는 (a)(b)(c) 3개뿐이며 (a)/(b) 내용도 뒤바뀜 — **5개 라벨 중 4개 오류**). PSUR 주기표도 `IIa/IIb→2년마다`(실제 IIb는 매년)로 오류이며 같은 문서 내 자기모순. → **[#133](https://github.com/holee9/ra-hermes-multi-agent/issues/133) 신규 등록**(#127과 동일 KB 데이터품질 클래스), 이슈 본문 진단도 코멘트로 정정.
  - **⚠️ 4회 연속 관측 — 창작이 참조표 미커버 영역으로 재이동**: RMF 근거 §를 `Annex I §§16-22`로 오배치 6/15(실제 Ch.I §§1-9; **제 수정이 § 번호를 안 준 공백**), `SSCP→Art.66(3)`(실제 Art.32)·`DoC→Art.37`(실제 Art.19)·`ISO 14971 §5.6` 등 참조표 밖 도메인 창작. **"표가 커버하면 방어, 커버 안 하면 이동"이 #123 R1→R3→#132까지 4회 반복** — 표 열거 방식의 구조적 한계 → **[#134](https://github.com/holee9/ra-hermes-multi-agent/issues/134) 전략 이슈 등록**(표 확장 / 코드 레벨 검증(#118 Part B 패턴) / 수용 중 선택 필요).
  - **별도 축**: 허위 자기검증 주장(`"No invented identifiers have been inserted"`라고 써놓고 같은 응답에서 창작) + 방어 마커 오발화(참조표에 있는 Rule 17/10/11에도 "verify separately" 스탬프) → **[#135](https://github.com/holee9/ra-hermes-multi-agent/issues/135) 등록**.
- ✅ **#123 라운드3(positive framing) — 6개 명시 패턴 전건 해소** (2026-07-18, commit `7e65c70`): 신규 배치 45케이스(**캡처 실패 0건**)로 ra_eu 15건 전수 팩트체크.
  - **결과**: pattern 5(Module/Annex 혼합) **6/15 → 0/15 완전 해소** — 15건 전체에서 module letter 0회 등장, 라운드2의 날조("MDR도 module letter를 쓴다") 재발 없음. pattern 1-4 퇴행도 **2/15 → 0/15 복구**. pattern 5 또는 6 보유 케이스: 라운드1 33%(4/12) → 라운드2 60%(9/15) → **라운드3 13%(2/15)**.
  - **🔑 검증된 교훈 — 금지 문구 vs 정답 제시**: 라운드2(금지 강화) 악화 → 라운드3(금지 전면 삭제 + 정답만 서술) 해소. `"Not this"` 컬럼을 통째로 제거하고, Module을 *금지*하는 대신 **"MDR은 Annex 번호로 경로를 부르며 이것이 전부다. Module 표기는 Decision 768/2008/EC 소관이고 MDR은 그 체계를 채택하지 않는다"** 는 **사실 서술로 오답을 존재하지 않게** 만든 것이 결정적. Rule 문언·Class 값은 EUR-Lex 원문 대조 검증.
  - **잔존 2건 판정**: rule *선택* 오류(원래 pattern 6 정의)는 0/15이고, 잔존 2건은 Rule→*Class 값* 오류로 [#131](https://github.com/holee9/ra-hermes-multi-agent/issues/131) 스코프 — 이 재분류는 자기 수정을 유리하게 볼 여지가 있어 이슈 코멘트에 근거를 명시하고 사람 판단을 요청함(현재 OPEN 유지).
  - **날조 무게중심 이동**: 라벨 오배치가 정리되자 conformity route 세부·IEC 표준번호·Article 하위구조로 날조가 옮겨감(근본 성향 미해결) → **[#132](https://github.com/holee9/ra-hermes-multi-agent/issues/132) 신규 등록**(IEC 60601-2-33 MRI 표준을 X-ray에 적용, Art.86(1) 하위구조 발명 등), [#131](https://github.com/holee9/ra-hermes-multi-agent/issues/131) 재확인(Class IIa에 Annex X 제시가 4/15로 단일 최다 빈발).
- ⚠️ **#123 라운드2 수정 재검증 — 실패 확인, 오히려 악화 (OPEN 유지)** (2026-07-17, commit `fce66f4`): 신규 배치 45케이스(iteration 01-03, **캡처 실패 0건** — iter01은 GX10 부하로 13/15 타임아웃 발생해 타임아웃 90s→180s 상향 후 재실행, 15/15 전건 성공)로 ra_eu 15건 전수 팩트체크.
  - **결과**: pattern 5(Module/Annex 혼합 라벨) **2/12 → 6/15로 악화**, pattern 6(Rule 9/10/17) 4/15, 라운드1에서 해결됐던 pattern 1-4도 2/15 퇴행. 두 패턴 중 하나 이상 범한 케이스 33%(4/12) → **60%(9/15)**.
  - **근본 원인 — 금지 문구(prohibition)가 역효과**: it03-ra_eu-005가 라운드2 금지 문구("Do not mix module letters with Annex numbers")를 응답에 그대로 복창해놓고 같은 답변에서 스스로 위반(`Annex IX – QMS assessment (module B)`), 나아가 **"MDR references the same letters but ties them to the specific annexes"라는 새로운 거짓 주장까지 생성**(MDR은 module letter 체계를 전혀 사용하지 않음). "NEVER write X" 방식은 규칙을 행동으로 내면화시키지 못하고 표층 복창만 유발함이 실증됨.
  - **대조 검증**: #130 대응 행(금지가 아닌 **정답 제시** 방식 — labeling→Annex I Ch.III §23, risk mgmt→Annex I+ISO 14971)은 **15/15 전건 정확** → 라운드3은 positive framing으로 전환 권고.
  - **신규 오류형 → [#131](https://github.com/holee9/ra-hermes-multi-agent/issues/131) 등록**: Rule↔Class 불일치(`Class IIb under Rule 17` — Rule 17은 항상 IIa), Class↔Annex route 매핑 오류(DoC→`Annex IX §3`, Class IIa→`Annex X`, `Annex VIII`를 design-dossier route로 오용).
- ⚠️ **#128 ra_kr 감사(audit) 오독 — 프롬프트 수정 시도, 재현 테스트 2건 모두 미해결 확인 (OPEN 유지)** (2026-07-16): `ra-kr` SOUL.md에 Fixed Rule 5(감사/오류보고서는 결함 서술이지 표준이 아님) 신설·강화 2차 시도했으나, 원래 트리거 케이스(it02-ra_kr-005) 재현 테스트에서 여전히 감사 대상 법률번호(20722)를 기준값으로 놓고 판단하는 동일 오류 재현. 원인: 이 케이스는 서로 다른 두 발췌 청크에 흩어진 정보(추상적 오류 서술 + 구체 번호)를 연결하는 교차청크 추론이 필요해 프롬프트 지시만으로는 안정적으로 해결되지 않는 것으로 판단됨 — #118 Part B 방식의 결정론적 코드 레벨 후처리가 대안으로 제안됨(사람 판단 필요, 미착수).
- ✅ **#123/#124/#125 전체 배치 재-eval 검증 완료 — #124/#125 CLOSE, #123 2차 수정 후 OPEN 유지** (2026-07-16, commit `995f6db`): 신규 45케이스(`kb-eval-checksheet.py --capture-responses`, iteration 01-03) 생성 후 딥리서치 팩트체크(3개 병렬 에이전트, agent-type별).
  - **#124 CLOSE**: 핵심 패턴(OECD/CER 고시번호 창작) 재발 0/15건 확인.
  - **#125 CLOSE**: 핵심 패턴(가짜 기기 카테고리) 재발 0/15건. 잔여 스타일 흔적("Daily Growth" 응답 제목 노출) 5건 발견 → 프롬프트 안내문 2차 보완 후 재현 테스트로 해소 확인.
  - **#123 OPEN 유지**: 6개 명시 패턴 중 4개(CER/PMCF/PMS/DoC) 완전 해결(12건 전건 정확), 2개(NLF Module 혼동/Rule 9-10 역전) 4/12건 잔존 → SOUL.md 참조표 2차 강화(EUR-Lex 재검증: Rule 9=치료용/10=진단용/17=X-ray 영상기록 전용) + 표본 2건 재현 테스트로 개선 확인, 단 전체 재-eval 미실시로 이슈는 열어둠.
  - **신규 이슈 5건 등록**(Issue-First Protocol): [#126](https://github.com/holee9/ra-hermes-multi-agent/issues/126)(ra_us Part 862/892 영상기기 분류 오배치), [#127](https://github.com/holee9/ra-hermes-multi-agent/issues/127)(KB 소스 `FDA_QMSR_2026.md` 자체 노후화), [#128](https://github.com/holee9/ra-hermes-multi-agent/issues/128)(ra_kr 감사 지시 반대 해석, High), [#129](https://github.com/holee9/ra-hermes-multi-agent/issues/129)(ra_kr OECD 외 주제 고시번호 창작 잔존), [#130](https://github.com/holee9/ra-hermes-multi-agent/issues/130)(ra_eu 라벨링/위험관리 Annex 오배치).
- 🔧 **#123/#124/#125 근본원인 조사 + 수정 적용 완료 (이슈는 OPEN 유지, 전체 재-eval 대기)** (2026-07-16, commit `84b9e0d`): 우선순위 순 3건 순차 적용.
  - **#124(재우선순위 확인 결과 원 가설 정정)**: 등록 당시 가설("`_fetch_learning_history` 경유 전파")은 코드 확인 결과 틀림 — kb-eval 응답 캡처 경로는 학습이력 재주입을 아예 하지 않음. 실제 원인은 `ra-kr` SOUL.md 페르소나 파일이 "OECD mutual recognition, CER acceptance since Jan 2026"을 출처 없이 단정해 매 호출마다 창작을 유발("전파"가 아니라 "공통 오염원 반복 자극"). 구체 고시번호/날짜는 KB 출처 인용 또는 미검증 명시로 수정.
  - **#123**: EUR-Lex 웹검증 기반 MDR Annex/Article 매핑 참조표(CER=Annex XIV Part A, PMCF=Annex XIV Part B, PMS/PSUR=Art.83-86, 적합성평가=Annex IX/X/XI vs NLF Module 구분, EUDAMED=Art.33-39)를 `ra-eu` SOUL.md에 추가.
  - **#125**: `daily-growth-runner.py` `build_case_content()`의 내부 추적 필드(Growth version 등)에 "기기 속성 아님" 명시 태그 추가, 회귀 테스트(`verify-daily-growth-runner.py`/`verify-kb-eval-checksheet.py`) PASS.
  - 각 이슈당 1건 재현 테스트로 개선 확인(전건 fabrication 없이 정상 응답). **제약**: SOUL.md 2건은 `hermes-api-server.service` 재시작이 권한 정책에 막혀 라이브 advisory 미반영(사용자 확인 대기) — `daily-growth-runner.py`는 코드 커밋이라 다음 실행부터 자동 반영. 전체 배치 재-eval은 미실시로 이슈 OPEN 유지.
- ✅ **#119~122 KB Eval iteration 14-17 사람 채점 완료, 전건 CLOSED** (2026-07-16, [#119](https://github.com/holee9/ra-hermes-multi-agent/issues/119)~[#122](https://github.com/holee9/ra-hermes-multi-agent/issues/122) CLOSED, commit `4ae516f`): 딥리서치 팩트체크(4개 병렬 에이전트, source + 외부 규제자료(FDA eCFR/EUR-Lex MDR/MFDS 국가법령정보센터) 대조)로 60케이스 전건을 사람 채점 형식(Reviewer Score + Fast Checks 6종 + 보정 노트)에 반영. 사용자 코멘트 검토 후 승인 → 체크박스 기계적 반영(스크립트 검증: 60건 전건 score/fast-check/note 불일치 0건). **채점 분포**: Score 3(fabrication 없음) 8건 · Score 2(경미한 정정 필요) 27건 · Score 1(정정 필수/캡처 실패) 25건(응답 캡처 타임아웃 8건 포함). **발견된 반복 패턴 → 신규 이슈 등록**: [#123](https://github.com/holee9/ra-hermes-multi-agent/issues/123)(MDR Annex/Article 체계적 오배치), [#124](https://github.com/holee9/ra-hermes-multi-agent/issues/124)(존재하지 않는 OECD-CER 상호인정 조항 창작 확산, High priority), [#125](https://github.com/holee9/ra-hermes-multi-agent/issues/125)(Daily Growth 실행 라벨을 기기 카테고리로 오독). #118에서 발견된 `K123456` predicate 창작 패턴이 iteration-16에서 재확인됨.
- 🛡️ **#118 근거 없는 구체 식별자 fabrication — 검증+로깅+정규식 버그 수정 + 배포·라이브 검증 완료, CLOSED** (2026-07-16, [#118](https://github.com/holee9/ra-hermes-multi-agent/issues/118) CLOSED, commit `d3db662`+`2f88408`): evidence 필드까지 커버하는 Part A(프롬프트)+Part B(결정론적 사후검증, `validate_advisory()`에 `_shown_source_text()`+`_cited_identifier_status()` 추가, 신규 `yellow_reason="unverified_identifier"`) 구현. **후속**: `_log_adv_request`에 `cited_identifier_status`(식별자별 검증 여부) 기록 추가로 향후 유사 분쟁 사후 진단 가능화. **부수 발견(테스트 작성 중)**: `\bK\d{6}\b`가 "K222222도 확인"류 **한글 조사 결합 문장에서 매칭 실패**(Python `re`의 `\b`가 유니코드 모드에서 한글을 단어문자로 취급) — 식별자가 추출조차 안 돼 검증을 조용히 우회하는 가장 위험한 실패 형태였음. negative lookaround로 경계 재정의해 수정. **검증**: `tests/test_advisory.py` 신규 9종 포함 44 passed. **`/opt` 배포 완료**(백업 `.bak-pre-118c`, 재시작) + **라이브 검증**: 실제 advisory 호출에서 `cited_identifier_status: {"K213497": true}`가 프로덕션 로그에 정확히 기록됨을 확인.
- 🔬 **#69~72 재-eval — 응답 캡처 포함 재생성, 신규 hallucination 패턴 발견(#118)** (2026-07-15): #110/#111/#112 retrieval 개선 + #113 응답 캡처 기능으로 원본 iteration 03-06(2026-06-20, 60케이스)과 동일 규모를 iteration 14-17로 재생성. 캡처 52/60(86.7%, 8건 타임아웃은 fail-safe 처리) · README-sourced 8.3%(5/60) · mismatch-flagged 5.0%(3/60) — 대규모 배치에서도 #110/#111 개선 효과 유지 확인. **신규 발견**: ra_us 3케이스(iteration-16)가 동일한 가상 510(k) 번호 `K123456`을 반복 인용(#113 파일럿의 `K123456`/`K234567`과도 일치) — source에 근거 없는 구체 식별자를 fabricate하는 재현 가능한 패턴 → **[#118](https://github.com/holee9/ra-hermes-multi-agent/issues/118)** 등록. GitHub 이슈 본문 크기 한도(65KB) 초과로(응답 포함 후 iteration당 ~200KB) 체크시트 파일 링크 방식으로 **[#119](https://github.com/holee9/ra-hermes-multi-agent/issues/119)~[#122](https://github.com/holee9/ra-hermes-multi-agent/issues/122)** 신규 게시, 구 자료(#69~72)는 supersede 사유 명시 후 CLOSED.
- 🧪 **#113 KB eval 체크시트 — 실제 에이전트 응답 캡처 추가, CLOSED** (2026-07-15, [#113](https://github.com/holee9/ra-hermes-multi-agent/issues/113) CLOSED, commit `7716171`): 체크시트 케이스에 source/매칭 키워드만 있고 실제 응답이 없어 `no_hallucination`/`escalation_appropriate`를 판정할 수 없던 갭 해결. `capture_agent_response()`(hermes-api-server.py `_invoke_llm_direct`와 동일 방식, 도구 없는 단발 completion) + `--capture-responses` opt-in 플래그 추가, `render_case()`에 **Agent Response** 섹션 신설(판정 기준 문구도 응답 기준으로 정합). 검증: `verify-kb-eval-checksheet.py` 신규(4종) PASS. **파일럿(iteration-13, 3케이스)에서 실제 hallucination 발견** — ra_us 응답이 존재하지 않는 가상 510(k) predicate 번호(K123456 등)를 구체 인용, 응답 캡처 없이는 식별 불가능했던 결함을 정확히 재현.
- 🔒 **#112 저신호·PII 소스(QA 이메일 로그) 인덱싱 배제 — 4단계 정리 완료, CLOSED** (2026-07-15, [#112](https://github.com/holee9/ra-hermes-multi-agent/issues/112) CLOSED): `06_심사_QA이력`/`11_일일_리서치로그` 저신호·PII 소스를 인덱싱·동기화·라이브 검색·원본 저장 4개 층위에서 순차 정리.
  1. **인덱싱 배제 규칙**(commit `02c7a24`): `scripts/index_github_repos.py`에 `INDEX_EXCLUDED_PATH_PATTERNS`+`is_excluded_path()` — fetch·embed 이전 단계에서 차단. `/opt` 배포 + 라이브 실행 검증(신규 유입 0건).
  2. **딥싱크로 발견한 라이브 노출 경로**: `sync_ra_knowledge_to_qdrant.py`(매일 03:18 KST)가 `llm-wiki`만 제외하고 QA이력/리서치로그는 필터 없이 Qdrant `ra_kb_markdown`(`hermes-api-server.py _run_rag_search()`의 **실제 라이브 advisory 서빙 컬렉션**)로 복사 중이었음 확인 — 실제 이메일·직원 실명·회사 주소 포함 812+620건 존재. advisory 로그+Honcho 세션 메시지 4,789건 검색 결과 실제 인용 사고 0건(잠재 위험이었지 발생한 사고는 아님).
  3. **sync 필터 추가 + Qdrant 정리**(commit `9403f9d`): `EXCLUDED_SOURCE_PATTERNS` 추가(구현 중 psycopg2 `%`-이스케이프 버그 재현+수정). Qdrant 기존 1,432건 백업(`~/hermes-backups/qdrant-ra_kb_markdown-qa-research-log-20260715.jsonl`) 후 삭제(8209→6777).
  4. **pgvector 원본 격리**(quarantine, 삭제 아님): 백업(`~/hermes-backups/ra_knowledge-quarantine-112-20260715.jsonl`) → 신규 `ra_knowledge_quarantine` 테이블(동일 스키마+`quarantined_at`/`quarantine_reason`) 생성 → 트랜잭션으로 1,432건 이동(건수 불일치 시 자동 롤백 가드) → `ra_knowledge` 8238→6806, 해당 패턴 0건.
  검증: 각 단계 회귀 테스트 3종 + 실제 advisory 쿼리 재확인(confidence 0.88~0.94, 매 단계 정상). 상세: `docs/specs/kb-rag-sync-spec.md` Annex D.
  **DoD 전체 충족**: 인덱싱 배제 정의 ✅ / 재-eval 오매칭 소거 확인 ✅ / 기존 PII 소스 격리(삭제 아닌 quarantine, 감사 보존) ✅.
- 🛠️ **#111 README 목차(manifest) 청크 필터 보강 — 재-eval로 개선 실측 후 CLOSED** (2026-07-15, [#111](https://github.com/holee9/ra-hermes-multi-agent/issues/111) CLOSED, commit `fb6a41c`): `is_substantive_chunk()`가 하이퍼링크 없는 불릿/번호 목차를 걸러내지 못하던 갭 수정 — heading 제외 라인 중 목록형이 60% 이상이면서 80자 넘는 실질 문장이 없으면 비실질로 판정하는 조건 추가. 회귀 테스트 3종 추가, `verify-daily-growth-runner.py` PASS. **재-eval 실측(iteration 10-12 vs 07-09)**: README-sourced TOC성 excerpt **13.3%(6/45) → 4.4%(2/45)**. 잔여 2건은 필터 결함이 아니라 `MDR_2017_745/README.md` 자체가 인덱싱된 청크 3개 전부 목차성이라 대체할 실질 청크가 없는 문서-콘텐츠 한계.
- 🔎 **#110 광의 키워드 라우팅 오매칭 — 재-eval로 개선 확인, CLOSED** (2026-07-15, [#110](https://github.com/holee9/ra-hermes-multi-agent/issues/110) CLOSED): PR #114(84ffed5, FOCUS_ROUTING negative-token 필터) 반영 후 신규 checksheet 45케이스(iteration 07-09, `docs/kb-eval-checksheets/2026-07-15/`, 프로덕션과 동일한 `assemble_cases`)로 재검증 — focus=`510(k) predicate strategy`+FDA 키워드 매칭 시 이전엔 cybersecurity/threat-model 문서였으나 이번엔 510(k)/RTA 계열로 정합, 직접 재현 테스트로 이전 오매칭 미재현 확인. 전체 mismatch 3/45(6.7%, 전부 경계 케이스).
- 🚀 **#109 RA Advisory 프롬프트 — summary 본문분석 강제 프로덕션 배포, CLOSED** (2026-07-15, [#109](https://github.com/holee9/ra-hermes-multi-agent/issues/109) CLOSED): 2026-07-11 커밋(`16cdf91`, summary는 `Subject:` 라인 복사/변형 금지 + 본문 분석 기반 + 100자 이내 가드)이 `/opt` 배포본과 7줄 차이로 미반영 상태였던 것을 사용자 승인(GATE-3) 받아 동기화(백업 `.bak-pre-109` 보존) + `hermes-api-server.service` 재시작. **라이브 검증**: `Subject:` 라인을 본문 앞에 삽입한 유도 쿼리로 실 advisory 호출 → 응답 summary가 Subject를 복사하지 않고 본문 기반 85자 요약으로 정상 생성 확인.
- 🧹 **#27 llm-wiki pgvector 잔존 정리 — Karpathy on-demand 정책 일관 적용** (2026-07-11): 사용자 승인(전체 정리 3단위). ra_knowledge llm-wiki 레거시 2,636건(06-11 정체) 백업(JSONL) 후 DELETE → ra_knowledge 10,795→8,159(MD-process+ra-project만). `index_github_repos` GITEA_REPOS=[](llm-wiki 재인제스트 영구 차단, /opt 배포). `autonomous-study-scheduler`+`curriculum-seed` ra_knowledge 쿼리 llm-wiki 제외 필터(agent study/curriculum에서 llm-wiki 배제 — 이전에 섞여 있었음). 검증: verify 2종 PASS, ra_kb_markdown 8,159 변화 없음. Layer 4 `fetch_llm_wiki`(Gitea realtime) 별도 경로—무영향. 백업 `~/hermes-backups/ra_knowledge-llm-wiki-20260711.jsonl`(롤백 가능). **정책 일관**: llm-wiki = on-demand Layer 4, pgvector/RAG/study 대상 아님.
- 🔗 **#107 Phase 2 (c1) 역방향 동기화 — ra-project/MD-process markdown → 에이전트 RAG 도달 (변화 C 단절 해소)** (2026-07-11, [#107](https://github.com/holee9/ra-hermes-multi-agent/issues/107) CLOSED): 사용자 "제대로 점검해서 승인받아" → 임베딩 호환 실측(pgvector `ra_knowledge` 4096/Cosine/qwen3 == Qdrant `nas_ra_docs`)으로 **(c1) 역방향이 (a)전량이관/(b)하이브리드 대비 최적** 입증. `sync_ra_knowledge_to_qdrant.py` 신규 — ra_knowledge(pgvector, 임베딩 이미 계산) → Qdrant `ra_kb_markdown` 역방향 복사, **GX10 임베딩 0건·데이터 손실 0**(NAS 2.09M 유지 + markdown 8,159 추가, llm-wiki 제외). `_run_rag_search` nas_ra_docs + ra_kb_markdown 하이브리드(Hermes `rag_search.py` 스킬 미수정). `build_advisory_context` rag_results[:5]→[:8](markdown 잘림 버그 수정). cron 18:03 증분. **라이브 검증**: AC-P2-1 RAG 도달(`_run_rag_search` NAS 5 + markdown 5 = 10건, markdown score 0.80 > NAS 0.72, LLM 무관 확정) · AC-P2-2 NAS 회귀 보존 · AC-P2-3 SPEC REQ-KBS-004a (c1) 문서화. 이전 보고에서 "사람 결정 대기"로 미룬 것은 점검 부족이었음(정정).
- 🚀 **#106 maturity-capability Phase 1+2 구현 + 라이브 배포 — KB 갭 탐지 루프 + 별 다축(coverage) 진화** (2026-07-10, [#106](https://github.com/holee9/ra-hermes-multi-agent/issues/106) CLOSED): 사용자 승인 Run. **Phase 1** — `hermes-api-server.py` `_log_kb_gap()` + `/v1/ra/advisory` 두 반환 지점 훅(advisory 추론 로직 미접촉, #105 회귀 방지), `adapter.js` `/api/kb-gaps` 엔드포인트(`readKbGaps`: JSONL 읽기+topic dedup+집계), VO "KB 보완 후보" 패널(DOM 기반 XSS safe). OD-1=(b) JSONL `reports/kb-gaps/`. **Phase 2** — `computeAgentLevels` coverage 축 추가(`coverage_sources`+`coverage_pct`, [IF] `KB_TOTAL_SOURCES` 기본 1493). DB 실측: ra_us 22/ra_eu 17/ra_kr 17 고유 source(volume 59/59/64와 직교). volume 별 `levelFromCount` 유지(REQ-MC-006 회귀=0), accuracy 축은 #69~72 pending(이관). OD-2=source 단위 정규화, OD-3=축별 다중 표시. **라이브 배포 완료(GATE-3 승인)**: hermes-api-server `/opt` 배포 + VO docker-compose 갭 로그 bind mount → **AC-P1-1~5 + AC-P2-1/3/4 전부 라이브 PASS**(chromium DOM 별 title "커버리지 22 source(1.5%)" + 갭 패널, `/v1/ra/advisory` 30s 회귀 무). accuracy 축(AC-P2-2)은 #69~72로 이관. 커밋 `bcd3c05`+`5b598de`.
- 📐 **#106 maturity-capability SPEC 수립 — 별 역량 다축 진화 + (c) KB 갭 탐지 루프 통합** (2026-07-10, [#106](https://github.com/holee9/ra-hermes-multi-agent/issues/106)): `docs/specs/maturity-capability-spec.md` 신규(294줄, 설계 PLAN 전용). 별이 volume 단일 축이라 KB 점프 시 퇴색하는 문제(3 경로) 해결을 위한 2-phase 설계 — **Phase 1** (c) KB 갭 탐지 루프 / **Phase 2** 별 다축(학습량·정확도·커버리지). **핵심 통찰**: 갭 탐지 신호가 `validate_advisory`(hermes-api-server.py:411)에 이미 존재(yellow_reason + evidence 부재) → Phase 1은 로깅·서피스·승인 루프만 추가, advisory 추론 로직 미접촉(#105 회귀 방지). REQ-MC-001~015(EARS), 3 OD Run phase 연기, plan-auditor self-audit 통과. **정확성 우선**: 별5 = "많이 학습"이지 "판단 신뢰" 아님 → 자동화 근거 사용 금지(REQ-MC-012), ra-advisory confidence 영구 제외(REQ-MC-015 raspi5p 오염). **구현은 GATE-3**(kb-rag-sync `4068d90`와 동일 패턴). 커밋 `52ea662`.
- 🧠 **"진짜 RA 전문 agent" (a)+(b) 둘 다 해결 — 학습 이력 주입 + 지식 query 행 근본 fix** (2026-07-07, [#104](https://github.com/holee9/ra-hermes-multi-agent/issues/104)·[#105](https://github.com/holee9/ra-hermes-multi-agent/issues/105)): **(a) REQ-AC-002b 학습 이력 주입** — `build_advisory_context`에 Honcho `daily_growth_case` 최근 7일 학습 주제 주입(`_fetch_learning_history`, date 기반 직접 probe, fail-safe 50-75ms). 에이전트가 과거 학습 반영 회고/자문 가능(SOUL.md 재진술 한계 해소). **(b) #105 지식 query 300s+ 행 근본 fix** — advisory를 Hermes agentic mode(도구+루프가 원인)에서 **직접 LLM 호출**(`_invoke_llm_direct`: SOUL.md persona + context를 GX10 `gpt-oss:120b`에 단발 완성, **도구 미노출→루프 구조적 불가**)로 전환. Contract A(이메일 triage)는 `_invoke_hermes` 유지. **라이브 e2e(실서버 `/v1/ra/advisory`)**: 지식 query 300s+행→**47s** 유효 자문(conf 0.92), email/action 자문 68s→**42s**(conf 0.87, 회귀 없음 오히려 개선). pytest 34 passed. 커밋 `518be4d`→`187a892`(1차 시도 롤백)→`b21b47c`(근본 해결). production 배포 완료. (중간 교훈: 1차 스킬 제거 fix는 단발 테스트만 믿었다가 라이브에서 email 자문 회귀 → 롤백; 2차는 직접 LLM으로 근본 해결 + 실서버 양쪽 query e2e로 검증.)
- ✨ **가상 오피스 RA 전문가 성숙도 별 표시** (2026-06-30): RA 3종(Mike/Theo/Sam) 캐릭터 이름 아래 학습량 기반 **별 1~5** 표시 — 현재 전부 ★★★☆☆(ra_us/eu 29 case, ra_kr 34 case). 별 5개=지구 최강 전문가 장기 목표. 정확도는 사람 KB-eval(#69~72) 도입 시 별도 활성(ra-advisory confidence는 raspi5p 루프 오염으로 제외). 구현 중 두 버그 포착·수정: ① `sessions/list` pagination 누락(page 1만 cap 50 → 전체 page 순회, #95 `messages/list`와 동일 패턴) ② `/api/events` 1.7MB/8511건 폭증(raspi5p 무한 루프 advisory가 98%) → 동일 이벤트 5분 윈도우 dedup로 **268KB/1117건(85%↓)**로 압축(growth/score 등 고유 활동은 보존, DB 변경 없이 표시 정책만). 별 count는 전체 기반이라 정확도 유지.
- ✨ **가상 오피스 세부내용(detail) 창 확대** (2026-06-30): 기록창 하단 세부내용 창(`.detail-panel`) max-height 220→440px(+220). 행 클릭 시 상세 하단이 잘려 스크롤해야 하던 문제 해결. `max-height` 기반이라 **내용 양에 따라 0~440px 동적 높이**(내용 적으면 그만큼 축소) — 이 동작으로 확정(사용자 확인 완료). `.log` 220px는 유지. Docker rebuild 반영(포트 3001). 커밋 `ed0c20a`.
- 🐛 **가상 오피스 최신 activity 미표시 버그 수정** (2026-06-28, [#95](https://github.com/holee9/ra-hermes-multi-agent/issues/95)): adapter `postJson`이 `path`에 query string(search)을 버려 항상 page 1(oldest 50)만 조회 → RA 전문가 자문·raspi5p 실행 최신이 대시보드에 누락되고 page 재호출로 중복 수집. `pathname + search` + `?page=N` 순회로 수정. 검증: advisory_returned 50→114건, latest 14:02 KST(기존 06-26). 커밋 `ce9cad0`. (#96 회귀 의심은 오판 정정 — ra_advisory 정상 기록 중)
- 🛡️ **raspi5p 자문 실행 게이트 안전 강화 + unclear_region 해소** (2026-06-27, [#91](https://github.com/holee9/ra-hermes-multi-agent/issues/91)·[#88](https://github.com/holee9/ra-hermes-multi-agent/issues/88)): raspi5p `hermes_fallback`이 T3610 yellow(사람 승격)을 우회 실행하던 결함 수정 — advisoryGate에 `yellow_review`/`no_action` → `allowMutation:false` 분기 추가(hermes_fallback 경로 전, fail-closed 보장). raspi5p `region_hint` 프로덕션 v6 적용 + caller timeout `620000ms`(T3610 `ADVISORY_TIMEOUT=600`+20s). T3610은 advisory 요청 query+region_hint 로깅 추가([#92](https://github.com/holee9/ra-hermes-multi-agent/issues/92)). 교차검증: raspi5p n8n DB 배포 v6 + 런타임(region_hint 적용 후 unclear 0건·우회 0건).
- 🩺 **T3610 RA 자문 백엔드 → raspi5p Hermes 연동 기반** (2026-06-24, [#83](https://github.com/holee9/ra-hermes-multi-agent/issues/83)): T3610 RA agent를 raspi5p의 **RA 자문 backend**로(실행권한 이동 없음). `POST /v1/ra/advisory`·`/feedback`(8643 Bearer) — 서버측 키워드 라우팅·검증(actor underscore·저신뢰/근거없음→Yellow)·Honcho 기록(로컬만). raspi5p(Iris) 캐릭터 + advisory 이벤트 대시보드 가시화. live 전 검증(단위 25 PASS + live 단일/다중/Yellow/feedback/옵저버). 커밋 `b564156`(+review 수정). 상세: [docs/ra-advisory-api.md](docs/ra-advisory-api.md).
- 🏢 **가상 오피스 → 실제업무 대시보드 전환** (2026-06-24, [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81)): 옵저버가 메일(activity_log)만 보던 한계 해소 — `metadata.record_type` 기반 매핑으로 RA 일일 학습(growth_case)·사람 KB-eval 평가(score_given)까지 표시. 하단 기록창 확대·폭 정렬 + 클릭 상세 패널(소스·도메인·점수·차원). 새 이벤트 실시간 애니메이션 사용자 브라우저로 검증. 커밋 `0f28c50`·`3b50e0e`.
- 🛡️ **RA 본질 견고성 개선** (2026-06-23, [#80](https://github.com/holee9/ra-hermes-multi-agent/issues/80)): Contract A confidence 타입 위반 수정·knowledge_fetch 에러 분류+로깅·openFDA 429 감지·growth-metrics 타임존 KST 보정. 회귀 테스트 추가(`verify-growth-metrics` H1·`verify-knowledge-fetch` 신규 H2/H3). py_compile + verify PASS. peer_id 하이픈 감별 위반 0건. 픽셀 아트(WCAG 팔레트+안경/수염) 시각 확인 완료.
- 🧭 **생태계 의사결정 원칙 전면 개정** (2026-06-21, `ECOSYSTEM-DECISION.md`): ECOSYSTEM 헌장(1·3·8) 기반 매 작업 전 4문 자문 훅. mail-triage/Gmail ⬇ 보류(Low), RA 자율 학습/지식/사람-에이전트 협업 ⬆ High.
- ✉️ **Gmail OAuth RPi→T3610 이전** (2026-06-21, [#75](https://github.com/holee9/ra-hermes-multi-agent/issues/75)): credential 이전(연결 test 200). 단 n8n 2.26.7 폴링 호환 에러로 **메일 처리 미동작 — mail-triage 보류**(채널 중 하나). **2026-06-23 정정: 이전 취소, n8n=RPi 정위치 복귀** (아래 "n8n 운영 위치" 참조).
- 🎮 **가상 오피스 재생→관측 모델 전환** (2026-06-21, [#74](https://github.com/holee9/ra-hermes-multi-agent/issues/74)): 관측 전용(read-only)으로 전환 — 재생 메타포 폐지, 과거는 정적 로그, 새 활동만 실시간 애니메이션, Heat Map 실데이터. chromium 렌더링 e2e 검증 완료.
- 🔧 **n8n credential 유실 복구** (2026-06-21, [#75](https://github.com/holee9/ra-hermes-multi-agent/issues/75)): DB credential 0건 → OP credential+URL(192.168.100.50:8080) 복구. OP 경로 e2e 4종 PASS.
- 🔍 **구현 전수 점검 완료** (2026-06-21): `[구현]` 30개 마커 ↔ 산물 대응, n8n 워크플로우 10개·SAFETY 게이트 검증(13/13 PASS)·growth snapshot 12개 전부 확인. **구현층 완결** — 남은 작업은 전부 외부 의존(30일 metrics·사람 승인·POC 평가). 시스템 🟢 NORMAL.
- 🔒 **n8n 보안 강화** (2026-06-21): 시크릿(JWT/BASIC_AUTH/POSTGRES) env화 + 강력 난수화, N8N_API_KEY 재발급(API 200), 보안 산물 gitignore 분리 — `reports/security-audit-2026-06-21.md`
- 📘 **상세 스크린샷 시스템**: 19개 포괄적인 시스템 캡쳐 자동 생성 (마스터 인덱스 포함)
- 📊 **E2E 검증 완료**: 모든 캡쳐가 실제 시스템 데이터와 상태 정보 포함
- 🔧 ~~**T3610 단일 n8n 운영**: 4개 워크플로우 import 및 활성화 완료~~ → **2026-06-23 철회** (반쪽짜리 이전, n8n=RPi 복귀)
- 📖 **문서 최신화**: 주요 문서 2026-06-21 기준

## 🏗️ 구축된 시스템 구성요소 상세

### 🤖 RA 에이전트 (8종 AI 전문가)

**모두 실제 작동 중** - 각 에이전트는 독립 SOUL.md와 전문 분야를 보유:

| 에이전트 | 역할 | SOUL.md | Honcho Peer ID | 작동 상태 |
|---------|------|---------|---------------|----------|
| **Mike (ra-us)** | FDA 510(k) 전문가 | ✅ 구축 완료 | `ra_us` | ✅ 활성 |
| **Theo (ra-eu)** | EU MDR 전문가 | ✅ 구축 완료 | `ra_eu` | ✅ 활성 |
| **Sam (ra-kr)** | MFDS/KGMP 전문가 | ✅ 구축 완료 | `ra_kr` | ✅ 활성 |
| **Margot (op-manager)** | OpenProject 사안 담당 | ✅ 구축 완료 | `op_manager` | ✅ 활성 |
| **Olly (n8n-manager)** | n8n 자동화 담당 | ✅ 구축 완료 | `n8n_manager` | ✅ 활성 |
| **Finn (infra-t3610)** | T3610 인프라 모니터링 | ✅ 구축 완료 | `infra_t3610` | ✅ 활성 |
| **Leo (infra-gx10)** | GX10 LLM 추론 관리 | ✅ 구축 완료 | `infra_gx10` | ✅ 활성 |
| **Gus (infra-rpi)** | RPi 인프라 관리 | ✅ 구축 완료 | `infra_rpi` | ✅ 활성 |

**특징**: 규제권별 철학이 다른 3종 RA 전문가, 실제 업무 경험과 피드백으로 성장

---

### 🏢 가상 오피스 (픽셀 아트 실제업무 대시보드)

**구축 완료: RA 조직의 실제 업무(학습·평가·메일 처리)를 실시간으로 비추는 관측 대시보드 + 사람→RA 자문 입력 창구([#104](https://github.com/holee9/ra-hermes-multi-agent/issues/104))**

> **관측 + 단방향 자문**. Hermes 활동은 읽기 전용으로 관측하되, 하단 채팅창으로 사람→RA 자문을 받는다. 어댑터가 `/v1/ra/advisory`를 호출하므로 **Hermes는 VO의 존재를 모른다(단방향 유지)**. 에이전트는 자문만 반환하고 실행·결정은 사람.

메일 트리아지뿐 아니라 **RA 일일 학습(daily-growth)·사람 KB-eval 평가**까지 표시한다. 메일이 들어오지 않아도 학습 루프가 살아 있으면 오피스가 움직인다 — CLI 없이도 프로젝트 활동 이력을 파악하는 것이 목적이다.

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **virtual-office.html** | ✅ 구축 완료 | 픽셀 오피스(760×440) + 하단 기록창(상단 폭 정렬·확대) + 클릭 상세 패널 |
| **캐릭터 시각화** | ✅ 구축 완료 | 코드 기반 픽셀 캐릭터 (Kenney CC0 교체 가능), WCAG 팔레트 |
| **캐릭터-에이전트 매핑** | ✅ 구축 완료 | actor ID ↔ 캐릭터 자동 매핑 (ra_us/eu/kr·op/n8n manager·infra 3종·human·system) |
| **실제 업무 매핑** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) | `metadata.record_type` 기반 — daily_growth_case→학습, score_given→평가, activity_log→메일 |
| **Honcho 실데이터 연동** | ✅ 구축 완료 | 어댑터가 Honcho 세션/메시지 폴링 → 이벤트로 변환·렌더링 |
| **이벤트 시각화** | ✅ 구축 완료 | mail_received·matched·comment_added·transition_proposed·vote_*·score_given·growth_case |
| **클릭 상세 이력** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) | 기록 행 클릭 → 하단 패널에 소스·도메인·점수·평가차원 등 상세 표시 |
| **실시간 애니메이션** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) 검증 | 새 이벤트만 캐릭터 반응, 과거는 정적 로그 (활동 없으면 조용함 = 정상 신호) |
| **Docker 컨테이너 배포** | ✅ 구축 완료 | 단일 컨테이너, `DATA_SOURCE=mock\|honcho` 전환 |
| **E2E 테스트** | ✅ 구축 완료 | 11개 Playwright 테스트 케이스 |

**작동 모드**: 관측 중심(단방향). Hermes 활동은 읽기 전용으로 관측하고, 하단 채팅창([#104](https://github.com/holee9/ra-hermes-multi-agent/issues/104))으로 사람→RA 자문을 받는다(어댑터가 `/v1/ra/advisory`를 호출 → **Hermes는 VO를 모름**). 에이전트는 자문만 반환, 실행·결정은 사람. `DATA_SOURCE`로 목업/Honcho 전환. 폴링(기본 30초) 중 새 이벤트가 오면 해당 캐릭터가 반응한다. 접속: `http://192.168.100.200:3001` / Tailscale `http://100.119.79.28:3001`.

---

### 📊 성장 대시보드 (Growth Dashboard)

**구축 완료: GitHub Pages 기반 정적 HTML 대시보드**

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **growth-dashboard.html** | ✅ 구축 완료 | standalone HTML snapshot (외부 의존 없음) |
| **RA Growth Operations 요약** | ✅ 구축 완료 | 전체 시스템 성장 현황 한눈에 파악 |
| **담당자별 성장 카드** | ✅ 구축 완료 | ra_us/ra_eu/ra_kr 개별 성장 추적 |
| **Growth Signal Flow** | ✅ 구축 완료 | 성장 신호 흐름 시각화 |
| **성장 측정 상태** | ✅ 구축 완료 | Trend Verdict, Evidence Radar 차트 |
| **커버리지 근거** | ✅ 구축 완료 | coverage-guards.json 기반 판정 |
| **inline SVG/CSS** | ✅ 구축 완료 | 독립 렌더링 (외부 fetch 없음) |

**데이터 소스**: reports/growth-YYYY-MM-DD.json, systemd 상태(`ra-growth-metrics.timer` active/enabled), readiness matrix 16/16. 집계 로직은 정상 작동한다(06-17~19 snapshot: 27 sessions / 302 messages). 06-20 snapshot은 timer 실행 시점의 Honcho 500 오류(`POST /v3/workspaces/work/sessions/list`)로 0건으로 회귀했고 현재는 복구됨 — `scripts/check-growth-metrics-health.py`로 매일 회귀를 감지한다(건강도 85/100). 행동/사람 피드백 metric 값이 아직 없어 Growth Trend Verdict는 warning을 유지한다.

---

### 🔧 Honcho 백엔드 시스템

**구축 완료: FastAPI + PostgreSQL + Redis + Deriver**

| 컴포넌트 | 상태 | 포트/구성 |
|----------|------|----------|
| **Honcho API** | ✅ 구축 완료 | :8000 (LAN 오픈) |
| **Deriver 워커** | ✅ 구축 완료 | 2 worker, flush 활성화 |
| **PostgreSQL/pgvector** | ✅ 구축 완료 | :5433 (4096차원, 1493 sources) |
| **Redis** | ✅ 구축 완료 | :6379 (루프백크) |
| **Workspace 2개** | ✅ 구축 완료 | work (업무), infra (인프라) 격리 |
| **Docker Compose** | ✅ 구축 완료 | 일관 기동 가능, T3610 운영 |

**환경**: T3610 단일 운영, GX10 Qwen3 연동 (tool calling 지원)

---

### ⚙️ n8n 워크플로우 자동화

**구축 완료: 4개 핵심 워크플로우 활성화**

| 워크플로우 | 상태 | 기능 |
|-----------|------|------|
| **mail-triage.json** | ✅ 구축 완료 | Gmail → RA 분석 → OpenProject 자동화 |
| **infra-vote-broadcast.json** | ✅ 구축 완료 | 인프라 3종 투표 브로드캐스트 |
| **feedback-recorder.json** | ✅ 구축 완료 | 3점 평가 → Honcho 기록 |
| **infra-to-work-bridge.json** | ✅ 구축 완료 | 인프라 → 업무 workspace 단방향 전달 |
| **form-triage-draft.json** | ✅ 구축 완료 | 폼 입력 처리 (gate 닫힘, 30일 metrics 미달) |

**안전 게이트**: Yellow 게이트 (low confidence → 사람 검토), WP 상태 검증, 환경변수 외부화 완료

---

### 💬 대화하는 칸반 (Interactive Components)

**구축 완료: RA 에이전트와 실제 대화하는 시스템**

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **Hermes Chat Completions API** | ✅ 구축 완료 | `/v1/chat/completions` 실시간 응답 |
| **세션 기반 대화** | ✅ 구축 완료 | SQLite 세션 히스토리, 문맥 유지 |
| **자기개선 루프** | ✅ 구축 완료 | 성공 워크플로우 → 스킬 자동 변환 |
| **Kanban 보드** | ✅ 구축 완료 | v0.13.0 (heartbeat, reclaim, zombie detection) |
| **메모리 시스템** | ✅ 구축 완료 | honcho_search, honcho_context, honcho_conclude |
| **Layer 4 RAG** | ✅ 구축 완료 | 실시간 규제 DB 조회 (openFDA, law.go.kr, data.go.kr) |

---

### 📚 지식 인프라 (Knowledge Infrastructure)

**구축 완료: pgvector 기반 지식베이스**

| 컴포넌트 | 상태 | 데이터 |
|----------|------|------|
| **pgvector ra_knowledge** | ✅ 구축 완료 | 1493 sources 인덱싱 완료 |
| **RA 프로젝트 레포** | ✅ 구축 완료 | ra-project + MD-process 마크다운 |
| **llm-wiki (NAS Gitea)** | ✅ 구축 완료 | DR_RnD/ra-llm-wiki 990 sources |
| **source curriculum seed** | ✅ 구축 완료 | ra_us 48, ra_eu 31, ra_kr 48 sources |
| **Layer 4 API 서버** | ✅ 구축 완료 | `/v1/knowledge/fetch` 실시간 조회 |

---

## 📸 실제 구동 현황 (E2E 검증 완료)

| 컴포넌트 | 상태 | 검증 상태 | 문서화 |
|----------|------|----------|--------|
| Honcho 서버 | ✅ 운영 중 | API :8000 정상 응답 확인 | ✅ 상세 캡쳐 완료 |
| 가상 오피스 | ✅ 구동 중 | 실제업무 대시보드 (학습/평가/메일 record_type 매핑) + 클릭 상세 패널 (#81, 재생→관측 전환 #74) | ✅ 상세 캡쳐 완료 |
| 성장 대시보드 | ✅ 배포 중 | GitHub Pages 렌더링, 16/16 readiness 확인 | ✅ 상세 캡쳐 완료 |
| n8n 워크플로우 | ✅ 활성 | 4개 workflow import/activate 상태 확인 | ✅ 상세 캡쳐 완료 |
| RA 에이전트 | ✅ 응답 중 | Hermes API 통해 실제 대화 가능 | ✅ 상세 캡쳐 완료 |
| Honcho 세션 관리 | ✅ 운영 중 | 142 활성 세션, 302 메시지 처리 | ✅ 상세 캡캡 완료 |
| 지식 베이스 | ✅ 운영 중 | pgvector 1493 sources 인덱싱, 검색 정상 | ✅ 상세 캡쳐 완료 |
| 인프라 투표 시스템 | ✅ 구동 중 | 3개 인프라 에이전트 투표 활성 | ✅ 상세 캡쳐 완료 |

**E2E 검증**: 모든 컴포넌트가 실제 환경(T3610)에서 구동 중임을 확인

### 🎯 상세 스크린샷 시스템 (2026-06-19 완료)

총 **19개**의 포괄적인 시스템 캡쳐가 생성되었습니다. 각 캡쳐는 실제 시스템 데이터와 E2E 검증 상태를 포함합니다.

**📘 마스터 인덱스**: [docs/screenshots/00-master-index.html](docs/screenshots/00-master-index.html)

**카테고리별 캡쳐 개요:**
- **시스템 개요 및 아키텍처** (4개): 기본 + 상세 아키텍처, Honcho API
- **에이전트 및 인터페이스** (4개): 가상 오피스, 대화 시스템  
- **모니터링 및 자동화** (4개): 성장 대시보드, n8n 워크플로우
- **전문 기능 분석** (6개): 세션, 지식, 트라이지, 투표, 성과, 통합
- **기능 플로우 및 시나리오** (6개): 이메일 E2E, 협업, 검색, 결정, 학습, 모니터링

---

| 단계 | 상태 | 이슈 |
|---|---|---|
| 설계 | ✅ 완료 | [#12 ADR-001](https://github.com/holee9/ra-hermes-multi-agent/issues/12) (closed) |
| 골격 코드 구현 | ✅ 완료 | — |
| Honcho T3610 배포 | ✅ 완료 | [#3](https://github.com/holee9/ra-hermes-multi-agent/issues/3) |
| MVP 자동화 스크립트 (SPEC-RA-TOOL-001) | ✅ 완료 | [#16](https://github.com/holee9/ra-hermes-multi-agent/issues/16) |
| RA 프로파일 생성 (PROFILE-1, PROFILE-2) | ✅ 완료 | [#4](https://github.com/holee9/ra-hermes-multi-agent/issues/4), [#6](https://github.com/holee9/ra-hermes-multi-agent/issues/6) |
| SKILL.md 심화 이식 | ✅ 완료 | [#13](https://github.com/holee9/ra-hermes-multi-agent/issues/13) |
| 지식베이스 연결 | ✅ 완료 | [#15](https://github.com/holee9/ra-hermes-multi-agent/issues/15) |
| hermes-ra 스크립트 이전 | ✅ 완료 (아카이브는 #11 게이트) | [#14](https://github.com/holee9/ra-hermes-multi-agent/issues/14) |
| n8n mail-triage 배포 (WORKFLOW-1) | ✅ 완료 | [#5](https://github.com/holee9/ra-hermes-multi-agent/issues/5) |
| 가상오피스 Honcho v3 API 연결 | ✅ 완료 (mail-triage 데이터 대기) | [#10](https://github.com/holee9/ra-hermes-multi-agent/issues/10) |
| MVP Cold Start 검증 | ✅ 완료 | [#11](https://github.com/holee9/ra-hermes-multi-agent/issues/11) (closed) |
| 인덱싱 스크립트 Qdrant → pgvector (MIGRATE-1) | ✅ 완료 | [#17](https://github.com/holee9/ra-hermes-multi-agent/issues/17) (closed) |
| extract_mail_qa.py Qdrant → pgvector (MIGRATE-2) | ✅ 완료 | [#19](https://github.com/holee9/ra-hermes-multi-agent/issues/19) (closed) |
| OpenProject → Honcho backfill (SEED-1) | ✅ 완료 (OP 토큰 갱신 + backfill 스크립트) | [#18](https://github.com/holee9/ra-hermes-multi-agent/issues/18) |
| warm-start 학습 루프 구축 (GROWTH-1,2) | ✅ 완료 (Honcho 컨텍스트 조회 + 프롬프트 주입 + deriver 활성화) | [#20](https://github.com/holee9/ra-hermes-multi-agent/issues/20), [#21](https://github.com/holee9/ra-hermes-multi-agent/issues/21) (closed) |
| feedback-recorder delta 페어링 (GROWTH-3) | ✅ 완료 (agent_judgment/human_correction/dimensions 기록) | [#22](https://github.com/holee9/ra-hermes-multi-agent/issues/22) (closed) |
| WP 종결 → case digest 자동 기록 (GROWTH-4) | ✅ 완료 (wp-close-recorder.json — OP webhook → Honcho AI peer) | [#23](https://github.com/holee9/ra-hermes-multi-agent/issues/23) (closed) |
| 일일 성장 지표 측정 인프라 (GROWTH-5) | ✅ 완료 (growth-metrics.py 5개 지표 + systemd timer 가이드) | [#24](https://github.com/holee9/ra-hermes-multi-agent/issues/24) (closed) |
| Layer 4 실시간 지식 통합 (llm-wiki/openFDA/law.go.kr) | ✅ 완료 (law.go.kr HTTP 수정, openFDA/law.go.kr E2E 검증 완료, graceful degradation 확인) | [#30](https://github.com/holee9/ra-hermes-multi-agent/issues/30) (closed) |
| Layer 4d data.go.kr MFDS DB 통합 (제조수입업허가/추적관리) | ✅ 완료 (DATA_GO_KR_API_KEY 통일, 2/3 서비스 E2E 검증) | [#31](https://github.com/holee9/ra-hermes-multi-agent/issues/31) (closed) |
| Layer 4d data.go.kr 품목허가(15057456) 3/3 서비스 완성 | ✅ 완료 (MdlpPrdlstPrmisnInfoService05, nested item 처리, 6건 E2E 검증) | [#33](https://github.com/holee9/ra-hermes-multi-agent/issues/33) (closed) |
| 정확성·신뢰성 우선 철학 전사 이식 | ✅ 완료 (CLAUDE.md·마스터설계·구현명세·운영전략·ra-us SOUL 전 문서 반영, cold start Yellow 게이트 기본값 명시) | [#32](https://github.com/holee9/ra-hermes-multi-agent/issues/32) (closed) |
| SaMD/SiMD 분류 보정 (ra-us/eu/kr SOUL.md) | ✅ 완료 (HnVUE=SaMD, Retrofit=SiMD 명시, SOUL.md 3종 테이블 갱신) | — |
| Phase 2~5 로드맵 문서화 | ✅ 완료 (master-design §12-§13, implementation-spec P2-P4, operations-guide §5 갱신) | [#34](https://github.com/holee9/ra-hermes-multi-agent/issues/34)~[#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| Gitea API 인덱싱 지원 추가 (DR_RnD/ra-llm-wiki) | ✅ 완료 (Gitea 990 소스 pgvector 인덱싱 완료, ra_knowledge 총 1493 sources) | [#35](https://github.com/holee9/ra-hermes-multi-agent/issues/35) (closed) |
| hermes-api-server.py 버전 관리 편입 + deploy-local.sh | ✅ 완료 (Layer 4 API 서버 git 편입, /opt/hermes-ra/ 동기화 스크립트, .env.example GITEA_URL 등 추가) | [#37](https://github.com/holee9/ra-hermes-multi-agent/issues/37) (연관) |
| doc-converter NAS→pgvector 인덱싱 | ✅ 완료 (llm-wiki + #35 인덱싱으로 목적 충족, 별도 구현 불필요, scripts/doc-converter/ 삭제) | [#36](https://github.com/holee9/ra-hermes-multi-agent/issues/36) (closed) |
| growth-metrics systemd 타이머 + 트리거 알림 자동화 | ✅ 완료 (check_and_notify_triggers 추가, systemd/ra-growth-metrics.{service,timer} 생성, T3610 배포 명령 이슈 기록) | [#38](https://github.com/holee9/ra-hermes-multi-agent/issues/38) (closed) |
| 팀장 에이전트 자리 예약 + 확장 가이드 초안 | 🔄 진행 중 (coordinator-SOUL.md 미활성 초안, agent-expansion-guide.md 작성 완료, growth-metrics 카테고리 분류는 운영 데이터 필요) | [#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| 에이전트 자율 학습 루프 (GROWTH-7) | ✅ 완료 (Layer 4 7소스, autonomous-study-scheduler.py Bootstrap/Delta 모드, 피어 교환, systemd 타이머, growth-metrics 지표 2개 추가) | [#42](https://github.com/holee9/ra-hermes-multi-agent/issues/42) (closed) |
| 자율 학습 peer_id 오염 복구 | ✅ 완료 (wrong-peer live messages/embeddings/queue refs/session peers 0, raw payload 2,085건 `ra_us`/`ra_eu` clean replay, JSONL 감사 백업 보존) | [#48](https://github.com/holee9/ra-hermes-multi-agent/issues/48), [#49](https://github.com/holee9/ra-hermes-multi-agent/issues/49), [#56](https://github.com/holee9/ra-hermes-multi-agent/issues/56) (closed) |
| source-level curriculum seed fast-track | ✅ 완료 (`ra_us` 48개, `ra_eu` 31개, `ra_kr` 48개 source seed processed, `curriculum_seed` JSON envelope 0, `ra_kr` all-scope idempotence `to_seed=0`) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| 비메일 성장 cadence loop | ✅ 구현 완료·운영 timer off (`hermes-auto-growth.timer` inactive/disabled, RA pending 0, 수동 readiness 16/16 확인, activation은 명시 승인 필요) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed), [#51](https://github.com/holee9/ra-hermes-multi-agent/issues/51) (closed), [#52](https://github.com/holee9/ra-hermes-multi-agent/issues/52) (closed), [#53](https://github.com/holee9/ra-hermes-multi-agent/issues/53) (closed), [#54](https://github.com/holee9/ra-hermes-multi-agent/issues/54) (closed), [#55](https://github.com/holee9/ra-hermes-multi-agent/issues/55) (closed), [#57](https://github.com/holee9/ra-hermes-multi-agent/issues/57) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| 자동성장 pre-production hardening | ✅ 목표치 완료 (`auto-growth-readiness-report.py` 4x4 matrix 16/16, timer OFF 유지, `ra_kr` self-doc 638로 legacy pre-activation floor 통과. 이 20% floor는 전문가 성숙도 기준이 아님) | [#58](https://github.com/holee9/ra-hermes-multi-agent/issues/58) (closed), [#59](https://github.com/holee9/ra-hermes-multi-agent/issues/59) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| mail-triage Yellow 게이트·사람 알림 강화 | ✅ RPi n8n import/activate, mail-triage Yellow smoke 완료 | [#43](https://github.com/holee9/ra-hermes-multi-agent/issues/43) |
| 기존 WP 매칭 시 OpenProject 상태 검증 | ✅ RPi n8n import/activate 완료 (통제된 closed-WP side-effect E2E는 별도 테스트 WP에서 수행) | [#44](https://github.com/holee9/ra-hermes-multi-agent/issues/44) |
| n8n 워크플로우 env/config 외부화 | ✅ RPi n8n env/compose 반영, workflow import/activate 완료 | [#45](https://github.com/holee9/ra-hermes-multi-agent/issues/45) |
| npm test 품질 게이트 복구 | ✅ 완료 (`test:static` + Playwright E2E 11건) | [#46](https://github.com/holee9/ra-hermes-multi-agent/issues/46) |
| 문서 상태 불일치 정리 | ✅ 완료 (README·설계·운영·생태계·상태 문서 동기화) | [#47](https://github.com/holee9/ra-hermes-multi-agent/issues/47) |
| 아키텍처 문서화 (Codemaps + SPEC-ARCH-001) | ✅ 완료 (전체 시스템 아키텍처 분석, 4개 codemaps + SPEC-ARCH-001 생성) | Codemaps 완료 |
| 제로 베이스 프로젝트 상태 재정렬 | ✅ 완료 (목표·현황·잔여 작업을 대시보드가 아니라 RA 전문가 성장 운영 기준으로 재정렬) | [#63](https://github.com/holee9/ra-hermes-multi-agent/issues/63) |
| 성장 지표 ingestion/data contract 보정 | ✅ 완료 (Honcho v0.15.1 `POST /sessions/list`·`POST /sessions/{id}/messages/list` 계약 반영, 2026-06-19 report 27 sessions/302 messages scanned) | [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64) |
| 자동성장 threshold/notification 정책 | ✅ 완료 (threshold null 정책·검증 추가, 30일 유효 metrics 전까지 자동 알림 비활성, error handling/dashboard/auto-copy/day15-checklist 구현) | [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65) |

> **README 갱신 규칙**: 이슈 close 시마다 위 표 상태를 갱신한다. `⏸ 대기 → 🔄 진행 중 → ✅ 완료` 순서로 전환.

### 제로 베이스 프로젝트 현황 (2026-06-16)

이 프로젝트의 목표는 대시보드 구축이 아니라 **H&ABYZ의 의료기기 인허가 업무를 보조하는 학습형 RA 전문가 조직**을 만드는 것이다. 에이전트는 사람 RA 전문가를 대체하지 않고, 지식베이스와 실제 업무 피드백을 통해 정확성·신뢰성 우선으로 성장한다.

| 축 | 현재 사실 | 판정 |
|---|---|---|
| 지식 토대 | `ra_knowledge` source curriculum seed와 Layer 4 API가 구축됨. `ra_us` 48, `ra_eu` 31, `ra_kr` 48 source seed 처리 완료 | ✅ foundation 존재 |
| 개별 성장 입력 | 메일 비의존 daily/weekly/monthly/quarterly growth loop 구현, timer는 승인 전 OFF | ✅ 구현 완료·운영 보류 |
| 성장 증명 데이터 | `growth-2026-06-19.json` 기준 27 sessions, 302 messages scanned. 행동/사람 피드백 metric은 N/A 또는 denominator 0. 2026-06-20 KB 평가 채점지 6회차/90건을 `docs/kb-eval-checksheets/`에 생성해 사람 체크 기반 denominator 확보를 시작 | ⚠️ 입력 수집됨·pilot evidence 확보 중 |
| 런타임 안전 게이트 | Yellow gate, WP 상태 검증, env/config 외부화 workflow를 RPi n8n에 import/activate. feedback + mail-triage Yellow smoke 완료 | ✅ 운영 반영 |
| 실시간 규제 활용 | `/v1/knowledge/fetch` 추가, T3610 runtime 배포/restart, RPi → Layer 4 smoke 200 OK | ✅ 운영 반영 |
| 인프라 의사결정 | `vote-rules.json` 초기값 + `infra-vote-broadcast` workflow 추가/import/activate, webhook smoke 완료 | ✅ skeleton 운영 반영 |
| 확장 | absence signal metric과 transition readiness report 추가. 현재 specialist/form 전환은 운영 데이터 부족으로 blocked | 🔄 데이터 대기 |
| 아키텍처 문서화 | 전체 시스템에 대한 codemaps (4개 파일)과 SPEC-ARCH-001 (3개 파일) 생성 완료 | ✅ 문서화 완료 |

### 남은 작업 우선순위

| 우선순위 | 작업 | 왜 필요한가 | 이슈 |
|---|---|---|---|
| P0 | 성장 metrics ingestion/data contract 보정 | 완료. 2026-06-19 daily report가 새 collector 계약으로 27 sessions / 302 messages를 스캔 | [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64) |
| P0 | #43~#45 RPi n8n import 및 smoke | 완료. 4개 workflow import/activate, env 반영, feedback webhook + mail-triage Yellow smoke 완료 | [#43](https://github.com/holee9/ra-hermes-multi-agent/issues/43), [#44](https://github.com/holee9/ra-hermes-multi-agent/issues/44), [#45](https://github.com/holee9/ra-hermes-multi-agent/issues/45) |
| P1 | Layer 4 API → mail-triage 실시간 연결 | 완료. n8n Layer 4 lookup node + prompt injection + runtime endpoint smoke 완료 | [#37](https://github.com/holee9/ra-hermes-multi-agent/issues/37) |
| P1 | 유효 metrics 기반 threshold/notification 정책 | policy/validator 구현. 임계값은 30일 valid metrics 전까지 null 유지 | [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65) |
| P1 | KB 기반 human-scored evidence 확보 | `ra_knowledge`에서 RA별 평가 채점지를 생성하고 체크 결과를 `score_given`으로 ingest하는 pilot evidence 루프 추가. 30일 production 기준은 유지 | 운영 |
| P2 | infra vote-rules와 n8n broadcast | 완료. 초기 2/3 quorum rule + broadcast workflow + webhook smoke | [#39](https://github.com/holee9/ra-hermes-multi-agent/issues/39) |
| P2 | 세부 전문가 확장 조건 데이터화 | 완료. `absence_pattern_signals` metric 추가. 현재 review signal 없음 | [#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| P3 | form workflow 이관 | draft workflow/enable gate 구현. 현재 30일 valid metrics 미달로 `FORM_TRIAGE_ENABLED=false` 유지 | [#40](https://github.com/holee9/ra-hermes-multi-agent/issues/40) |

### 지속 성장 모니터링 현황 (2026-06-19)

| 구분 | 현재 상태 | 판정 |
|---|---|---|
| 자동성장 readiness | `scripts/auto-growth-readiness-report.py` 기준 4x4 matrix 16/16, `approval_review_required` | ✅ 승인 검토 가능 |
| 자동성장 timer | `hermes-auto-growth.timer` inactive/disabled, 명시 승인 전 자동 실행 없음 | ✅ 안전 |
| 일일 성장 지표 timer | `ra-growth-metrics.timer` active/enabled, 매일 02:00 KST 실행 | ✅ 스케줄러 존재 |
| 성장 지표 산출물 | `reports/growth-YYYY-MM-DD.json` 생성 (`correction_rate`, `first_pass_match_accuracy`, `confidence_calibration`, `warmstart_lift`, `escalation_precision`, `autonomous_study_sessions`, `study_insights_count`) | ⚠️ 파일 기반 |
| 최근 지표 유효성 | `growth-2026-06-19.json`: `sessions_scanned=27`, `messages_scanned=302`, 행동/사람 피드백 metric denominator 0 | ⚠️ 입력 수집됨·성장 판정 보류 |
| KB 평가 채점지 | `docs/kb-eval-checksheets/2026-06-20/`에 6 iterations / 90 cases 생성. 체크 후 `scripts/kb-eval-feedback-ingest.py`로 `score_given` 반영 가능 | 🔄 사람 채점 대기 |
| 웹 대시보드 | GitHub Pages `growth-dashboard.html` 바로보기 활성화. RA Growth Operations 요약, 담당자별 성장 카드, growth signal flow, 성장 측정 warning, 커버리지 근거 포함 | ✅ README 클릭 렌더링 |
| 트리거 알림 | `feedback/config/growth-trigger-config.json` 구조는 있으나 threshold/webhook은 null | ⚠️ 운영 기준 미정 |

현재 존재하는 것은 **자동 리포트와 정적 HTML snapshot 기반 모니터링**이다. [성장 대시보드 바로보기](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html)는 README에서 클릭하면 렌더링된 HTML로 열린다. 2026-06-16 #64에서 Honcho v0.15.1 list API 계약을 `POST /sessions/list`, `POST /sessions/{id}/messages/list`로 보정했고, 2026-06-19 daily report는 27 sessions / 302 messages를 스캔한다. 다만 행동/사람 피드백 지표가 N/A 또는 denominator 0이므로 Growth Trend Verdict는 `측정 불충분` warning 상태가 맞다. 하단 readiness/coverage/raw metrics는 매일 볼 필수 현황이 아니라 기본 접힘 상태의 검증/감사 상세다. 열람·갱신·판정 기준은 [growth-dashboard.md](docs/growth-dashboard.md)에 정리했다. `virtual-office`는 Honcho 활동 이벤트를 시각화하는 관측 파일럿으로 분리한다(사람→RA 자문 입력 채널 [#104](https://github.com/holee9/ra-hermes-multi-agent/issues/104) 포함 — 어댑터가 API caller이므로 단방향 유지, Hermes는 VO를 모름). dashboard 표시 유지·보정은 [#62](https://github.com/holee9/ra-hermes-multi-agent/issues/62), metrics ingestion 보정 이력은 [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64), threshold/webhook 운영 기준은 [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65)에서 각각 추적한다.

### Hermes 프로파일 & Honcho 피어 현황 (2026-06-16 기준)

| 프로파일 | Honcho 피어 ID | Workspace | 인물 | 상태 |
|---------|--------------|-----------|-----|-----|
| ra-us | `ra_us` | work | Mike (FDA) | ✅ 등록·SOUL.md 이식 완료 |
| ra-eu | `ra_eu` | work | Theo (EU MDR) | ✅ 등록·SOUL.md 이식 완료 |
| ra-kr | `ra_kr` | work | Sam (MFDS) | ✅ 등록·SOUL.md 이식 완료 |
| op-manager | `op_manager` | work | Margot (WP) | ✅ 등록·SOUL.md 이식 완료 |
| n8n-manager | `n8n_manager` | work | Olly (n8n) | ✅ 등록·SOUL.md 이식 완료 |
| infra-t3610 | `infra_t3610` | infra | Finn (T3610) | ✅ 등록·SOUL.md 이식 완료 |
| infra-gx10 | `infra_gx10` | infra | Leo (GX10) | ✅ 등록·SOUL.md 이식 완료 |
| infra-rpi | `infra_rpi` | infra | Gus (RPi) | ✅ 등록·SOUL.md 이식 완료 |

> `honcho.json` `aiPeer` 값은 모두 언더스코어 형식(frozen 데이터 계약 준수). #49에서 `ra-us`/`ra-eu` wrong-peer bootstrap 오염을 복구했으며, 이후 자율 학습은 `scripts/verify-study-scheduler.py`와 dry-run을 통과한 뒤만 재시작한다. wrong-peer records는 직접 rename하지 않고 raw payload replay 방식만 허용한다.

### n8n 운영 위치 — RPi 단일 (2026-06-23 정정)

> **정정 (2026-06-23)**: 2026-06-19 "T3610 단일 n8n 운영" 선언은 **철회**. 조사 결과 (1) RPi 핵심 RA 워크플로우 32개(ra-reg-monitor·규제기관 스크래핑·Gitea 연동 등)가 이관 대상에서 누락, (2) 외부 도메인 `n8n.abyz-lab.work`가 RPi cloudflared에 묶인 채 T3610으로 전환 안 됨, (3) 4개만 부분 이전된 반쪽짜리 상태. **CLAUDE.md 원 설계(n8n=RPi 정위치)로 복귀**.

**현재 구성 (정정 후):**
- **RPi**: n8n + OpenProject (n8n 정위치, 36개 워크플로우 운영)
- **T3610**: Honcho server 전담 (n8n rollback/제거)

**이후 과제 — 이식성 개편 (별도 SPEC):**
- 현재 구조는 하드코딩 내부 IP(`172.18.0.1:*` 등)·도메인-인스턴스 결합으로 **머신 종속 → 이전 불가**
- 모든 서비스 주소를 env/논리 이름화, 도메인-인스턴스 분리, IaC화하여 **어느 머신에서든 운영 가능** 구조로 개편 선행 필요

**워크플로우 구현 현황:**
- `mail-triage`: Gmail 트리거 → 본문 파싱 → 규제권 라우팅 → Yellow 게이트 → RA 호출 → OpenProject 연동
- `infra-vote-broadcast`: Webhook 수신 → 투표 표준화 → 투표 집계 → 브릿지 전달
- `feedback-recorder`: 피드백 Webhook → 평가 검증 → Honcho 기록
- `infra-to-work-bridge`: 인프라 투표 결과 → 업무 workspace 전달

### 주요 구현 항목

| 컴포넌트 | 파일 | 상태 |
|---|---|---|
| Honcho 서버 설정 | `honcho/docker-compose.yml`, `init-vector-dim.sql`, `init-workspaces.sh` | 완료, T3610 배포 완료 |
| n8n 워크플로우 (T3610) | `n8n/workflows/mail-triage.json`, `infra-vote-broadcast.json`, `feedback-recorder.json`, `infra-to-work-bridge.json` | 완료, T3610 단일 운영 전환 |
| RA 프로파일 템플릿 | `profiles/honcho-config-templates/` 8종 | 완료 |
| SOUL.md 페르소나 | `profiles/souls/` 6종 (ra-us/eu/kr, op/n8n-manager, infra) | 완료 |
| mail-triage 워크플로우 | `n8n/workflows/mail-triage.json` | 완료, #43/#44/#45 안전 게이트 레포 반영 — RPi n8n 재import 필요 |
| 브릿지 워크플로우 | `n8n/workflows/infra-to-work-bridge.json` | 완료, relay 조건 env/config 외부화(#45) |
| 피드백 워크플로우 | `n8n/workflows/feedback-recorder.json` | 완료, 가중치 공식 env/config 외부화(#45) |
| 투표 집계 인터페이스 | `voting/vote-aggregator.js`, `voting/config/vote-rules.json`, `n8n/workflows/infra-vote-broadcast.json` | 완료 — 초기 2/3 quorum rule, RPi n8n import/activate, webhook smoke 완료 |
| 가상오피스 | `virtual-office/virtual-office.html` + 어댑터 + Dockerfile | 완료, Playwright 11건 `npm test` 통합(#46) |
| 자율 학습 scheduler guard | `scripts/verify-study-scheduler.py`, `scripts/replay-study-insights-issue49.py` | #49 peer_id 계약 검증·오염 payload clean replay 완료 |
| source curriculum seed | `scripts/curriculum-seed.py`, `scripts/verify-curriculum-seed.py` | #50/#60 기존 `ra_knowledge` source를 clean text curriculum seed로 빠르게 이식 (`ra_us` 48, `ra_eu` 31, `ra_kr` 48 processed) |
| non-email growth loop | `scripts/non-email-growth-loop.py`, `scripts/verify-non-email-growth-loop.py`, `scripts/pre-auto-growth-loop.py`, `scripts/auto-growth-readiness-report.py`, `scripts/auto-growth-runner.sh`, `scripts/systemd/hermes-auto-growth.{service,timer}`, `scripts/verify-auto-growth-activation-policy.py` | #51/#53/#54 메일 수신 없이 KB/source curriculum/autonomous study/coverage audit cadence 실행, #57 이후 timer 활성화는 명시 승인 게이트 필요, #58 pre-production readiness loop로 지속 개선 |
| KB eval checksheets | `scripts/kb-eval-checksheet.py`, `scripts/kb-eval-feedback-ingest.py`, `docs/kb-eval-checksheets/` | KB source를 평가 채점지로 변환해 git 이력으로 보관하고, 체크된 결과를 Honcho `score_given` feedback으로 ingest하는 controlled pilot evidence 루프 |
| static growth dashboard | `docs/growth-dashboard.html`, `docs/growth-dashboard.md`, `scripts/render-growth-dashboard.py`, `scripts/verify-growth-dashboard.py`, `scripts/coverage-guards.json` | #62 GitHub Pages에서 바로 보는 standalone HTML snapshot. RA Growth Operations 요약, 담당자별 성장 카드, growth signal flow, trend/evidence 시각화 |
| 아키텍처 Codemaps | `.moai/project/codemaps/` (overview.md, modules.md, dependencies.md, entry-points.md) | 전체 시스템 아키텍처 분석 완료. 30+ 모듈, 50+ 진입점, 내외부 의존성 그래프 문서화 |
| 아키텍처 개선 SPEC | `.moai/specs/SPEC-ARCH-001/` (spec.md, plan.md, acceptance.md) | SPEC-ARCH-001 생성 완료. EARS 형식 요구사항 15개, 5단계 구현 계획, Given-When-Then 수용 기준 |

> [IF] 표시 항목은 의도적 공백 — 운영·학습으로 채워지는 설계. 하드코딩 금지.

### n8n 운영 적용 체크리스트 (#43~#45)

RPi n8n에는 레포 변경을 import해야 실제 운영에 반영된다.

| 순서 | 확인 항목 |
|------|-----------|
| 1 | `n8n/.env.example` 기준으로 `OPENPROJECT_API_URL`, `HONCHO_WORK_WORKSPACE`, `YELLOW_CONFIDENCE_THRESHOLD` 확인 |
| 2 | 선택 알림 채널 `HUMAN_ALERT_WEBHOOK_URL` 설정 여부 결정 |
| 3 | `mail-triage.json`, `infra-to-work-bridge.json`, `feedback-recorder.json` import |
| 4 | 낮은 confidence, 완료 WP 매칭, OpenProject 조회 실패, bridge/feedback config parse 시나리오 E2E |
| 5 | 결과를 #43~#45 이슈에 코멘트 후 운영 기준값 변경 시 문서 동기화 |

레포 검증 명령:

```bash
npm run test:static
npm test
```

---

## 🖼️ 시스템 운영 및 E2E 검증

### 스크린샷 캡쳐 가이드

각 구성요소의 실제 운영 상태를 시각적으로 확인하고 E2E 검증을 수행하려면:

1. **캡쳐 가이드 참조**: `docs/screenshots/capture-guide.md` 
   - Honcho 대시보드, 가상 오피스, 성장 대시보드 등 6개 구성요소 캡쳐 방법
   - E2E 검증 체크리스트 포함

2. **주요 서비스 접속**:
   - Honcho API: `http://localhost:8000` 
   - n8n 워크플로우: `http://localhost:5678`
   - 가상 오피스: `virtual-office/virtual-office.html`
   - 성장 대시보드: [GitHub Pages](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html)

3. **인터랙티브 사용 매뉴얼**: 탭 기반 상세 가이드 제공
   - 시스템 개요, RA 에이전트, 가상 오피스, 성장 모니터링, n8n 워크플로우

### 시스템 상태 확인

```bash
# Honcho API 상태 확인
curl http://localhost:8000/health

# Docker 컨테이너 상태 확인  
docker ps | grep -E "honcho|postgres|redis"

# n8n 워크플로우 상태 확인
curl http://localhost:5678 | grep -o "<title>.*</title>"
```

---

## 장비별 역할

| 장비 | 역할 | 이 레포에서 할 일 |
|---|---|---|
| **T3610** | Honcho 서버 + Hermes 에이전트 | `git clone` 후 `honcho/` 기동, 프로파일 생성 |
| **GX10** | LLM 추론 엔진 (`gpt-oss:120b`, tool calling 확인) | 별도 작업 없음 (T3610이 API 호출) |
| **Raspberry Pi 5+** | n8n + OpenProject | `n8n/workflows/*.json` 3개 import만 |

---

## T3610 빠른 시작

```bash
git clone https://github.com/holee9/ra-hermes-multi-agent.git
cd ra-hermes-multi-agent

# 1. 환경변수 설정
cp honcho/.env.example honcho/.env
# .env 필수 편집 항목:
#   GX10_BASE_URL=http://GX10_실제IP:11434/v1
#   GX10_MODEL=gpt-oss:120b
#   EMBEDDING_MODEL_CONFIG__MODEL=qwen3-embedding:latest   ← __OVERRIDES__MODEL 아님
#   POSTGRES_PASSWORD=안전한_비밀번호
#   SECRET_KEY=안전한_시크릿

# 2. Honcho 서버 기동 (pgvector 4096차원 자동 초기화 포함)
docker-compose -f honcho/docker-compose.yml up -d

# 3. Workspace 초기화 (work + infra)
bash honcho/init-workspaces.sh
```

> **이후 작업은 [GitHub Issues](https://github.com/holee9/ra-hermes-multi-agent/issues) 순서대로 진행.**
> 이슈 #2 RULE을 먼저 읽고 시작할 것.

---

## 디렉터리 구조

```
ra-hermes-multi-agent/
│
├── .moai/                           # MoAI 프로젝트 관리
│   ├── project/                      # 프로젝트 산출물
│   │   └── codemaps/                # 아키텍처 Codemaps
│   │       ├── overview.md           # 시스템 개요
│   │       ├── modules.md            # 모듈 카탈로그 (30+ 모듈)
│   │       ├── dependencies.md       # 의존성 그래프
│   │       └── entry-points.md       # 진입점 매뉴얼 (50+ 진입점)
│   └── specs/                        # SPEC 문서
│       └── SPEC-ARCH-001/            # 전체 시스템 아키텍처 개선 SPEC
│           ├── spec.md               # EARS 형식 요구사항 (15개)
│           ├── plan.md               # 5단계 구현 계획
│           └── acceptance.md        # Given-When-Then 수용 기준
│
├── docs/                            # 설계·운영 문서
│   ├── RA-multi-agent-master-design.md  # 마스터 설계서 (전체 그림·철학)
│   ├── implementation-spec.md           # 구현 명세 ([구현]/[IF] 구분)
│   └── operations-guide.md              # 운영 전략 (프로파일·학습·게이트)
│
├── honcho/                          # T3610: Honcho 서버
│   ├── docker-compose.yml           # API + deriver + PostgreSQL(pgvector) + Redis
│   ├── .env.example                 # 환경변수 템플릿 → .env로 복사 후 편집
│   ├── init-workspaces.sh           # work/infra workspace 초기화 스크립트
│   └── init-vector-dim.sql          # pgvector 4096차원 초기화 (첫 기동 시 자동 실행)
│
├── profiles/                        # Hermes 프로파일 템플릿
│   ├── honcho-config-templates/     # ra-us, ra-eu, ra-kr, op-manager, n8n-manager, infra-* 8종
│   └── souls/                       # SOUL.md 페르소나 (ra-us/eu/kr, op-manager, n8n-manager, infra)
│
├── n8n/                             # Raspberry Pi: n8n에 import
│   ├── .env.example                 # n8n 환경변수 템플릿
│   └── workflows/
│       ├── mail-triage.json         # 핵심: 재전송 메일 → RA 분석 → WP 처리
│       ├── infra-to-work-bridge.json # 인프라→업무 단방향 브릿지
│       ├── infra-vote-broadcast.json # 인프라 투표 브로드캐스트 skeleton
│       ├── feedback-recorder.json   # 3점 평가 → Honcho 기록
│       └── form-triage-draft.json   # #40 form 이관 draft (FORM_TRIAGE_ENABLED=false)
│
├── voting/                          # 인프라 투표 자리 [IF]
│   ├── vote-aggregator.js           # 집계 인터페이스 (규칙은 외부 설정)
│   └── config/vote-rules.json       # 집계 규칙 (초기 운영값: quorum 2, threshold 0.66)
│
├── bridge/
│   └── config/bridge-config.json   # 브릿지 전달 임계 조건 [IF]
│
├── feedback/
│   └── config/weight-adjustment-config.json  # 가중치 설정 [IF]
│
├── scripts/                         # T3610 운영 스크립트
│   ├── hermes-api-server.py         # Layer 4 규제 API 서버 (openFDA/law.go.kr/data.go.kr) — 버전 관리 편입
│   ├── deploy-local.sh              # git scripts/ → /opt/hermes-ra/ 동기화 (--dry-run 지원)
│   ├── index_github_repos.py        # GitHub + Gitea 레포 → pgvector 인덱싱 (DR_RnD/ra-llm-wiki 포함)
│   ├── curriculum-seed.py           # ra_knowledge source-level curriculum seed → Honcho peer
│   ├── daily-growth-runner.py       # 메일 비의존 KB 기반 daily growth case planner/runner
│   ├── kb-eval-checksheet.py        # KB 기반 human review 채점지 생성
│   ├── kb-eval-feedback-ingest.py   # 체크된 채점지를 score_given feedback으로 반영
│   ├── verify-workflows.js          # n8n JSON/Code node 정적 검증
│   └── ...                          # 기타 자동화 17종
│
├── e2e/                             # Playwright E2E 테스트 (virtual-office)
│   └── virtual-office.spec.js       # 4 Suite 11 테스트 케이스
│
├── virtual-office/                  # 가상오피스 (자기완결)
│   ├── Dockerfile                   # Docker 단일 컨테이너 빌드
│   ├── virtual-office-honcho-adapter.js  # Honcho 실데이터 연결 어댑터
│   ├── virtual-office.html          # 픽셀아트 프로토타입 (브라우저 직접 열기)
│   ├── virtual-office-mvp.md        # 가상오피스 MVP 설계
│   ├── virtual-office-org-chart.md  # actor ID ↔ 캐릭터 매핑
│   └── pixel-character-guide.md     # 스프라이트 교체 가이드 (Kenney CC0)
│
├── README.md                        # 이 파일
├── CLAUDE.md                        # Claude Code 프로젝트 지시
└── ECOSYSTEM.md                     # RA 생태계 지도 (전 레포 공유)
```

---

## 실행 순서 (이슈 번호 아님 — 의존관계 기준)

> GitHub 이슈 번호는 등록 순서일 뿐이다. **실제 작업 순서는 아래 표를 따른다.**
> 이슈 목록: https://github.com/holee9/ra-hermes-multi-agent/issues

### 상시 참조 (닫지 않음)

| 이슈 | 내용 |
|---|---|
| [#2 RULE](https://github.com/holee9/ra-hermes-multi-agent/issues/2) | 절대 위반 금지 규칙 — 모든 작업 전 필독 |
| [#12 ADR-001](https://github.com/holee9/ra-hermes-multi-agent/issues/12) | 생태계 운영 결정 기록 — 레이어 모델, 개발 주력 확정 |

### Phase 1 — Foundation (T3610)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 1 | [#3 SETUP-1](https://github.com/holee9/ra-hermes-multi-agent/issues/3) | Honcho 서버 배포 · GX10 Qwen3 연결 검증 | T3610 | ✅ |

### Phase 2 — Profiles + Knowledge (T3610, #3 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 2a | [#4 PROFILE-1](https://github.com/holee9/ra-hermes-multi-agent/issues/4) | RA 프로파일 생성 (ra-kr/ra-us/ra-eu/op-manager) | T3610 | ✅ |
| 2b | [#13 ABSORB-1](https://github.com/holee9/ra-hermes-multi-agent/issues/13) | hermes-ra SKILL.md → SOUL.md 3종 심화 이식 | T3610 | ✅ |
| 2c | [#6 PROFILE-2](https://github.com/holee9/ra-hermes-multi-agent/issues/6) | 인프라 프로파일 생성 (infra-t3610/gx10/rpi) | T3610 | ✅ |
| 2d | [#15 CONNECT-1](https://github.com/holee9/ra-hermes-multi-agent/issues/15) | ra-project + MD-process → Honcho 지식 연결 | T3610 | ✅ |

> 2a·2b는 병행 가능. 2a 완료 후 2b 시작 권장 (프로파일 디렉토리 확정 후 이식).

### Phase 3 — Workflows (RPi, #4 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 3a | [#5 WORKFLOW-1](https://github.com/holee9/ra-hermes-multi-agent/issues/5) | mail-triage n8n 배포 · E2E 검증 | RPi | ✅ |
| 3b | [#10 SETUP-2](https://github.com/holee9/ra-hermes-multi-agent/issues/10) | 가상오피스 Docker 빌드 · Honcho 실데이터 연결 | T3610 | ✅ |

### Phase 4 — IF 구현 (선택적, #5 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 4a | [#7 WORKFLOW-2](https://github.com/holee9/ra-hermes-multi-agent/issues/7) | 투표 집계 자리 동작 확인 [IF] | T3610 | ✅ |
| 4b | [#8 WORKFLOW-3](https://github.com/holee9/ra-hermes-multi-agent/issues/8) | 브릿지 n8n 배포 · 단방향 검증 [IF] | RPi | ✅ |
| 4c | [#9 WORKFLOW-4](https://github.com/holee9/ra-hermes-multi-agent/issues/9) | 3점 평가 루프 n8n 배포 [IF] | RPi | ✅ |

### Phase 5 — Validate + Archive (전체 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 5a | [#11 MVP-VALIDATE](https://github.com/holee9/ra-hermes-multi-agent/issues/11) | Cold Start E2E 검증 — **hermes-ra 종료 게이트** | 전체 | ✅ |
| 5b | [#14 ABSORB-2](https://github.com/holee9/ra-hermes-multi-agent/issues/14) | hermes-ra 스크립트 이전 + 아카이브 (#11 PASS 후) | T3610 | ✅ |

```
#3 → #4 + #13(병행) + #6 + #15 → #5 + #10 → #7 + #8 + #9 → #11 → #14
```

---

## 핵심 원칙

- **정확성·신뢰성 우선** (최우선): 의료기기 인허가에서 오류는 환자 안전 문제다. 속도는 정확성이 확보된 뒤의 부산물. 불확실하면 반드시 사람에게 올린다. Cold start 상태에서 기본값은 Yellow 게이트(사람 확인).
- **학습하며 성장**: 골격 고정, 내용물(판단·기억·평가)이 성숙해지는 구조. 자동화 비중은 학습·성숙도 누적 후 점진적으로 확대.
- **T자형**: 공통 지식(llm-wiki·ra-project·MD-process 단방향 참조) + 개별 전문성(Honcho 누적)
- **사람 = 최종 결정자**: WP 완료·재오픈은 사람 전용(불변). 에이전트는 보조하고 제안만. 사람이 검토 루프에 있는 것은 약점이 아니라 설계.
- **[IF] = 의도적 공백**: 투표 규칙·가중치·임계값은 운영하며 채움. 코드 하드코딩 금지.

---

## 문서 읽는 순서

1. `docs/RA-multi-agent-master-design.md` — 전체 그림, 설계 철학
2. `docs/implementation-spec.md` — 구현 경계 (`[구현]` vs `[IF]`)
3. `docs/operations-guide.md` — 프로파일·학습 루프·게이트·성장 기준
4. `virtual-office/virtual-office-mvp.md` — 가상오피스 설계
