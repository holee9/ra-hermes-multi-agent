# ra-hermes-multi-agent

## 개발 환경

### Git / GitHub CLI

`git`과 `gh` CLI가 모두 설치되어 있으며 인증 완료된 상태입니다.

- **git**: Bash 도구(`/usr/bin/bash`)를 통해 사용 가능. PowerShell에서는 인식 안 됨 — 반드시 `Bash` 도구로 실행할 것.
- **gh CLI**: `/c/Users/drake/bin/gh` — GitHub 계정 `holee9`으로 인증됨 (`repo`, `workflow` 스코프 보유)
- **원격**: `https://github.com/holee9/ra-hermes-multi-agent.git`

사용 가능한 작업 (`.claude/settings.json`에 허용 등록됨):

```bash
git push origin main           # 원격 푸시
gh issue create --title "..." --body "..."   # 이슈 생성
gh issue comment <번호> --body "..."        # 코멘트
gh issue edit <번호> --title "..."          # 이슈 수정
gh issue close <번호>                       # 이슈 닫기
gh pr create --title "..." --body "..."     # PR 생성
gh pr merge <번호>                          # PR 병합
```

> **주의**: PowerShell 도구에서는 `git`/`gh` 명령이 PATH에 없어 실패합니다.
> git/gh 작업은 항상 `Bash` 도구로 실행하세요.
