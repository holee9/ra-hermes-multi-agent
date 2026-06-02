# RA 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 학습하는 멀티 에이전트 시스템 설계 산출물.
> 사실 검증 기준일: 2026-05-28. Hermes Agent v0.14.0 / Honcho 기반.

---

## 파일 안내

### 메인 설계서

- **RA-multi-agent-master-design.md** — 마스터 설계서 (뼈대 전체)
  - 설계 철학(T자형·프랙탈·벌집), 기술 기반, 장비 배치, 조직 구조, 학습 루프, 고정 규칙, 1차 PoC 범위, 체크항목, 단계 요약, **MVP 구현 가이드(§14)**.
  - **가장 먼저 읽을 문서.** §14는 실제 착수용 구체(Honcho 환경변수·n8n 연동·최소 성공 기준).

### 생태계 차원

- **ECOSYSTEM.md** — RA 생태계 지도 (모든 레포에 동일 주입)
  - 헌장(공통 원칙 7개) + 조각 명세 매트릭스 + 관계 매트릭스 + 연계 프로젝트 색인.
  - 의료기기 인허가 생태계 안에서 본 시스템의 위치를 정의.

### 구현·운영 (AI 코딩 툴 + Hermes)

- **implementation-spec.md** — 구현 명세서 (**AI 코딩 툴용**, 툴 중립)
  - 전체 골격을 코딩 가능 깊이로. `[구현]`=코딩 / `[IF]`=인터페이스만(학습이 채움). Claude Code CLI / Codex CLI 등이 읽고 코딩.
- **operations-guide.md** — 운영 전략서 (**사람 + Hermes용**)
  - 프로파일·SOUL.md 페르소나, 학습 루프, 게이트, **MVP→프로덕션 성장 기준**.
  - 코딩 산출물이 만든 그릇을 어떻게 채워 키우는가.

> **코딩 vs 운영 경계**: implementation-spec가 만드는 건 *자라날 그릇*(n8n·연동·투표 자리·가상 오피스), operations-guide가 채우는 건 *내용물*(프로파일·학습·평가). 둘의 접점(데이터 계약)은 implementation-spec §3에 고정.

### 가상 오피스 (살)

- **virtual-office-mvp.md** — 살 MVP 설계 (목업 계약·캐릭터·동작 매핑·배포)
- **virtual-office-org-chart.md** — 살 전용 조직도 (actor ID ↔ 사람 이름 매핑, 파일럿 작명)
- **virtual-office.html** — 동작하는 프로토타입 (브라우저에서 바로 열림, 목업 이벤트 재생)
- **pixel-character-guide.md** — 캐릭터 정교화 가이드 (Kenney CC0 다운로드 위치·파일 배치·연결법)

---

## 읽는 순서

**전체 이해**:
1. **RA-multi-agent-master-design.md** — 전체 그림과 1차 PoC 범위, MVP 구현 가이드(§14)
2. **ECOSYSTEM.md** — 생태계 위치, 공통 헌장

**구현 착수**:
3. **implementation-spec.md** — AI 코딩 툴에 입력(코딩 대상·데이터 계약·수용 기준)
4. **operations-guide.md** — Hermes 프로파일·학습 루프·성장 기준

**가상 오피스**:
5. **virtual-office-mvp.md** → **virtual-office.html**(프로토타입) → **virtual-office-org-chart.md** + **pixel-character-guide.md**

---

## 핵심 원칙

- **T자형 성장**: 가로획(공통 지식 토대 = llm-wiki·ra-project·MD-process, 단방향 참조) × 세로획(자기 전문성, Honcho 누적).
- **프랙탈 + 벌집 지향**: 자기복제로 성장, 분산·상호지탱으로 견고. 구조 박제가 아니라 매 설계 결정의 나침반.
- **중앙 두뇌 없음**: 판단 분산, 집계 규칙, 출력 배관(n8n). 종합·조율 역할은 두되 통제 아님.
- **사람 = 최종 결정자**: 3점 사후 평가로 시스템을 사람 의도로 수렴. 완료 처리는 사람 전용(불변).
- **부재 기반 성장**: 부재가 패턴으로 확정될 때만 자리를 채움. 같은 철학이면 스킬, 독립 직능이면 에이전트.

---

## 현재 단계

설계 완료, 1차 PoC 착수 전. 다음 단계(마스터 설계서 §13):
1. 인프라 검증 — T3610 Honcho ↔ GX10 Qwen3 deriver 연결
2. mail-triage 이관 — 재전송 메일 → RA 전문가 3종, 규제권 라우팅
3. 학습 효과 측정 — 중복 WP 감소, 사람 개입 감소
4. 확장 — form 이관, 인프라 에이전트 + 투표·평가, 가상 오피스 MVP 연동

---

## 개발 환경

### Git / GitHub CLI

`git`과 `gh` CLI가 모두 설치되어 있으며 인증이 완료된 상태입니다.

- **git**: `Bash` 도구(`/usr/bin/bash`)를 통해 사용 가능. `PowerShell`에서는 인식되지 않으므로 반드시 `Bash` 도구로 실행할 것.
- **gh CLI**: `/c/Users/drake/bin/gh` 경로에 위치. `GitHub` 계정 `holee9`으로 인증됨 (`repo`, `workflow` scope 보유)
- **remote**: `https://github.com/holee9/ra-hermes-multi-agent.git`

`.claude/settings.json`에 허용 목록이 등록되어 있어 다음 작업을 바로 실행할 수 있습니다.

```bash
# push
git push origin main

# issue 생성
gh issue create --title "제목" --body "내용"

# issue comment 등록
gh issue comment <번호> --body "내용"

# issue 수정
gh issue edit <번호> --title "새 제목"

# issue 닫기
gh issue close <번호>

# PR 생성
gh pr create --title "제목" --body "내용"
```

> `git`/`gh` 명령은 항상 `Bash` 도구로 실행하세요. `PowerShell` 도구로 실행하면 `PATH` 미등록으로 실패합니다.
