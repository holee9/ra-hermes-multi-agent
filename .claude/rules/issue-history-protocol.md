# Issue History Protocol

## 목적

모든 구현·배포 작업은 GitHub 이슈에 이력을 남긴다. 나중에 "언제 무엇을 왜 했는가"를 이슈 타임라인만 봐도 알 수 있어야 한다.

## 적용 시점

다음 작업에 반드시 적용한다:
- 배포·설정 변경 (컨테이너 재기동, .env 수정 등)
- 코드 구현 (새 파일, 기존 파일 변경)
- 인프라 조작 (포트 바인딩, 서비스 재시작)
- DoD 항목 달성

## 작업 흐름

### 1. 착수 전 — 관련 이슈 확인

```bash
gh issue list --repo holee9/ra-hermes-multi-agent --state open
```

- 작업과 관련된 이슈 번호를 확인한다
- 없으면 이슈를 먼저 등록하고 시작한다 (Issue-First Protocol)
- 착수 코멘트는 생략 가능 (짧은 작업은 완료 코멘트만 남겨도 됨)

### 2. 주요 변경 완료 시 — 이슈 코멘트 추가

```bash
gh issue comment <번호> --repo holee9/ra-hermes-multi-agent --body "..."
```

코멘트에 포함할 내용:
- 변경 전/후 (테이블 형식 권장)
- 검증 결과 (✅ / ⚠️ / ❌)
- 알려진 제약 또는 미결 항목

### 3. DoD 달성 시 — 이슈 close + README 갱신

```bash
gh issue close <번호> --repo holee9/ra-hermes-multi-agent --comment "완료 사유"
```

README.md 상태 표도 동시에 갱신한다:
- `🔄 진행 중` → `✅ 완료`

### 4. 미결 항목 — 이슈 open 유지

DoD 항목 중 일부가 남아 있으면 이슈를 닫지 말고 코멘트만 추가한다.

## 코멘트 형식 권장안

```markdown
## 작업명 — 완료/부분완료 (날짜)

### 변경 내용
| 항목 | 이전 | 이후 |
|------|------|------|
| ... | ... | ... |

### 검증 결과
- 항목 A: ✅
- 항목 B: ⚠️ 미검증 — 사유

### DoD 현황 (해당하는 경우)
| 항목 | 상태 |
|------|------|
| ... | ✅ / ⚠️ / ❌ |
```

## 관련 규칙

- CLAUDE.md `Issue-First Protocol` — 분석·발견 후 이슈 없으면 먼저 등록
- CLAUDE.md `Issue-History Protocol` — 이 파일 (상세)
- README.md 상태 표 — 이슈 close 시 동시 갱신
