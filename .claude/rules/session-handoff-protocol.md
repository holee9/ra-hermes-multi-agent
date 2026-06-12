# Session Handoff Protocol

## 목적

작업 세션이 끝날 때 다음 세션에서 문맥 없이도 즉시 이어서 작업할 수 있도록 상태를 기록한다.

## 적용 시점

다음 중 하나라도 해당하면 핸드오프 기록을 수행한다:
- 1개 이상의 이슈 작업 완료 또는 부분 완료
- 새 파일/구조 생성 또는 배포 수행
- 다음 작업이 명확히 식별된 경우
- 블로커(사람 승인 필요, 외부 의존)가 새로 발생한 경우

## 핸드오프 체크리스트

### 1. GitHub 이슈 동기화 (Issue-History Protocol 연계)

```bash
gh issue list --repo holee9/ra-hermes-multi-agent --state open
```

- DoD 달성 이슈: `gh issue close <번호>` + README 상태 표 갱신
- 부분 완료 이슈: 코멘트 추가 (완료 항목 / 미결 항목)

### 2. README.md 상태 표 갱신

- 이슈 close 시: `🔄 진행 중` → `✅ 완료`
- 최종 갱신 날짜 업데이트 (헤더 라인 12)
- 신규 항목 추가 시 표 하단에 행 추가

### 3. memory/next-session-entrypoint.md 갱신

`~/.claude/projects/-home-abyz-lab-work-workspace-github-holee9-ra-hermes-multi-agent/memory/next-session-entrypoint.md` 파일을 반드시 갱신한다.

포함 내용:
- 이번 세션에 완료된 이슈 목록 (커밋 해시 포함)
- 부분 완료 이슈와 남은 작업
- 블로킹 이슈와 블로커 이유
- 조건부 이슈와 충족 조건
- 다음 즉시 실행 가능한 작업

### 4. Git 커밋

```bash
git add <변경 파일들>
git commit -m "type(#이슈번호): 작업 내용"
```

미커밋 변경사항이 없는 상태로 세션을 마친다.

## next-session-entrypoint 갱신 형식

```markdown
## 마지막 완료 작업 (YYYY-MM-DD)

### 완료된 이슈 (closed)
- **#N** [TAG]: 작업명 ✅ (commit abc1234)

### 부분 완료된 이슈 (open)
- **#N** [TAG]: 작업명 — 완료: X / 미완료: Y

### 블로킹 이슈 (open, 사람 승인 필요)
- **#N** [TAG]: 이유

### 조건부 이슈 (open, 조건 미충족)
- **#N** [TAG]: 조건

## 현재 오픈 이슈 요약
| # | 이슈 | 상태 |
|---|------|------|
| #N | ... | 즉시 진행 가능 / BLOCKED / 조건부 |

## 다음 즉시 실행 가능한 작업
1. ...
```

## 완료 보고 순서 [HARD]

**완료 보고는 반드시 핸드오프 완료 후에만 허용한다.**

순서:
1. 작업 완료
2. memory/next-session-entrypoint.md 갱신 (체크리스트 3번)
3. 이슈 코멘트/close (체크리스트 1번)
4. README 갱신 (체크리스트 2번)
5. git 커밋 — 미커밋 변경사항 없는 상태 확인 (체크리스트 4번)
6. **이 모든 단계 완료 후에만 사용자에게 완료 보고**

금지: 작업이 끝났다고 사용자에게 완료를 보고한 뒤 핸드오프를 처리하는 것.
이유: 핸드오프 전에 세션이 종료되거나 컨텍스트 손실이 발생하면 다음 세션이 어디서 이어야 할지 불명확해진다.

## 관련 규칙

- CLAUDE.md `Session Handoff Protocol` — 완료 순서 HARD 규칙
- CLAUDE.md `Issue History Protocol` — 이슈 코멘트/close 절차
- `.claude/rules/issue-history-protocol.md` — 코멘트 형식 상세
