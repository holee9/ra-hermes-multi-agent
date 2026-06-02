# ra-hermes-multi-agent

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
