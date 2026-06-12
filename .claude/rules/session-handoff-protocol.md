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

## 관련 규칙

- CLAUDE.md `Issue History Protocol` — 이슈 코멘트/close 절차
- `.claude/rules/issue-history-protocol.md` — 코멘트 형식 상세
