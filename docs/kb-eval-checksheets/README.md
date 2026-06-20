# KB Eval Checksheets

이 폴더는 KB 기반 RA 평가 채점지를 날짜별로 보관한다.

목적:

- `ra_knowledge`에서 생성한 평가 케이스를 사람이 빠르게 체크한다.
- 체크된 Markdown을 git 이력으로 남긴다.
- 이후 `scripts/kb-eval-feedback-ingest.py`가 체크 결과를 Honcho `score_given` 피드백으로 변환한다.

운영 규칙:

1. 케이스마다 score는 하나만 체크한다.
2. 빠른 체크 항목은 사실인 것만 체크한다.
3. 수정이 필요할 때만 correction note를 짧게 남긴다.
4. production timer 30일 기준은 유지한다. 이 채점지는 controlled pilot 판단용 fast evidence다.

생성:

```bash
set -a && . scripts/.env && set +a
python3 scripts/kb-eval-checksheet.py --iterations 3 --cases-per-agent 5
```

체크 결과 확인:

```bash
set -a && . scripts/.env && set +a
python3 scripts/kb-eval-feedback-ingest.py --input docs/kb-eval-checksheets
```

Honcho에 피드백으로 반영:

```bash
set -a && . scripts/.env && set +a
python3 scripts/kb-eval-feedback-ingest.py --input docs/kb-eval-checksheets --execute
```

GitHub 평가 이슈에서 체크된 결과를 Honcho에 반영:

```bash
set -a && . scripts/.env && set +a
python3 scripts/kb-eval-feedback-ingest.py \
  --github-search '"[EVAL][평가] KB Eval 2026-06-20" in:title' \
  --execute
```

GitHub 평가 이슈 발행:

```bash
python3 scripts/kb-eval-publish-issues.py \
  --date-dir docs/kb-eval-checksheets/2026-06-20 \
  --execute
```

운영 기준:

- 채점지 하나는 GitHub issue 하나로 발행한다.
- 제목은 `[EVAL][평가]`로 시작해 일반 결함 이슈와 구분한다.
- GitHub issue 본문 체크박스는 클릭으로 상태를 저장할 수 있다.
- `docs/`의 Markdown은 원본/감사용 기준 파일로 유지한다.
