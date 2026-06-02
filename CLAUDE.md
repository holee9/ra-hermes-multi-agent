# CLAUDE.md

이 파일은 이 저장소에서 작업할 때 Claude Code(claude.ai/code)에게 제공되는 안내 문서입니다.

## 언어 규칙

- 설명은 반드시 한국어로 작성합니다.
- 기술 용어(`git`, `gh`, `CLI`, `API`, `branch`, `commit`, `issue`, `PR` 등)와 명령어는 영어 그대로 사용합니다.
- 한국어와 영어 이외의 언어는 일체 사용하지 않습니다.

## Git / GitHub CLI 환경

`git`과 `gh` CLI가 모두 설치되어 있으며 별도 설치나 인증 작업이 필요하지 않습니다.

| 도구 | 경로 | 상태 |
|------|------|------|
| `git` | `/usr/bin/git` | 사용 가능 |
| `gh` | `/c/Users/drake/bin/gh` | `holee9` 계정으로 인증 완료 (`repo`, `workflow` scope) |

**중요**: `git`/`gh` 명령은 반드시 `Bash` 도구로 실행해야 합니다. `PowerShell` 도구는 `PATH`에 등록되지 않아 실패합니다.

### 주요 명령어

```bash
# 원격 push
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

# PR 병합
gh pr merge <번호>
```

## 저장소 정보

- **remote**: `https://github.com/holee9/ra-hermes-multi-agent.git`
- **기본 branch**: `main`
- **권한 설정**: `.claude/settings.json` 참고
