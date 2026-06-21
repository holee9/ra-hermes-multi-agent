# RA Hermes Multi-Agent - Entry Points

## Python CLI Scripts

### Growth & Learning

**autonomous-study-scheduler.py**
```bash
# Bootstrap mode (first run, all chunks)
python3 scripts/autonomous-study-scheduler.py --mode bootstrap --agent ra-us
python3 scripts/autonomous-study-scheduler.py --mode bootstrap --agent ra-eu
python3 scripts/autonomous-study-scheduler.py --mode bootstrap --agent ra-kr

# Delta mode (incremental since last checkpoint)
python3 scripts/autonomous-study-scheduler.py --mode delta

# Dry-run (inspect what would be studied)
STUDY_MAX=1 python3 scripts/autonomous-study-scheduler.py --mode bootstrap --agent ra-us
```
Flags: `--mode` (bootstrap|delta), `--agent` (ra-us|ra-eu|ra-kr), `--dry-run`
Environment: `HONCHO_URL`, `HERMES_API_URL`, `API_SERVER_KEY`, `POSTGRES_URL`, `STUDY_BATCH_SIZE`, `STUDY_MAX_CHUNKS`

**daily-growth-runner.py**
```bash
# Plan mode (dry-run, inspect what would be generated)
python3 scripts/daily-growth-runner.py --plan --date 2026-06-20

# Execute mode (run actual growth cycles)
python3 scripts/daily-growth-runner.py --run --date 2026-06-20
```
Flags: `--plan`|`--run`, `--date` (YYYY-MM-DD), `--agent` (ra-us|ra-eu|ra-kr|all)
Environment: `HONCHO_URL`, `HONCHO_WS`, `POSTGRES_URL`

**growth-metrics.py**
```bash
python3 scripts/growth-metrics.py --date 2026-06-20
```
Flags: `--date` (YYYY-MM-DD), `--output` (JSON file path)
Environment: `HONCHO_URL`, `HONCHO_WS`, `POSTGRES_URL`

**curriculum-seed.py**
```bash
python3 scripts/curriculum-seed.py --source-dir /path/to/curriculum
```
Flags: `--source-dir`, `--batch-size`

**pre-auto-growth-loop.py**
```bash
python3 scripts/pre-auto-growth-loop.py --verify
```
Flags: `--verify`, `--check-activation-policy`

**non-email-growth-loop.py**
```bash
python3 scripts/non-email-growth-loop.py --dry-run
python3 scripts/non-email-growth-loop.py --execute
```
Flags: `--dry-run`, `--execute`, `--agent`

**ra-kr-growth-plan.py**
```bash
python3 scripts/ra-kr-growth-plan.py --plan
```
Flags: `--plan`, `--prioritize`

**growth-transition-readiness.py**
```bash
python3 scripts/growth-transition-readiness.py --assess
```
Flags: `--assess`, `--report`

**auto-growth-readiness-report.py**
```bash
python3 scripts/auto-growth-readiness-report.py --compile
```
Flags: `--compile`, `--evidence`

**render-growth-dashboard.py**
```bash
python3 scripts/render-growth-dashboard.py --input reports/metrics.json
```
Flags: `--input`, `--output` (HTML file)

**replay-study-insights-issue49.py**
```bash
# Dry-run (verify replay)
python3 scripts/replay-study-insights-issue49.py --backup /path/to/insights.jsonl

# Execute replay (batch size 50)
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```
Flags: `--backup`, `--execute`, `--batch-size`

### Knowledge Indexing

**index_ra_knowledge.py**
```bash
python3 scripts/index_ra_knowledge.py --source /path/to/llm-wiki
python3 scripts/index_ra_knowledge.py --source /path/to/ra-project
python3 scripts/index_ra_knowledge.py --source /path/to/MD-process
```
Flags: `--source` (path to markdown repo)
Environment: `POSTGRES_URL`
> **[HARD]** Read-only indexing: NEVER write to source repos

**index_github_repos.py**
```bash
python3 scripts/index_github_repos.py --repo https://github.com/user/repo
```
Flags: `--repo`, `--branch`

**knowledge_fetch.py**
```bash
# Called by hermes-api-server.py as subprocess
python3 scripts/knowledge_fetch.py --query "FDA 510(k) requirements" --profile ra-us --top 3
```
Flags: `--query`, `--profile` (ra-us|ra-eu|ra-kr), `--top`

**nas_indexer_v2.py**
```bash
python3 scripts/nas_indexer_v2.py --scan /path/to/nas/documents
```
Flags: `--scan`, `--embed`, `--upload`
Environment: `QDRANT_URL`, `OLLAMA_URL`, `EMBED_MODEL`

### Operations Tools

**extract_mail_qa.py**
```bash
python3 scripts/extract_mail_qa.py --input /path/to/emails.mbox
```
Flags: `--input`, `--output` (JSON pairs)

**meta_extractor.py**
```bash
python3 scripts/meta_extractor.py --file /path/to/document.pdf
```
Flags: `--file`, `--output`

**op_honcho_backfill.py**
```bash
python3 scripts/op_honcho_backfill.py --import /path/to/export.json
```
Flags: `--import`, `--workspace`

### Verification Suite

**verify-*.py** (all verify scripts)
```bash
python3 scripts/verify-auto-growth-activation-policy.py
python3 scripts/verify-daily-growth-runner.py
python3 scripts/verify-growth-metrics.py
python3 scripts/verify-growth-dashboard.py
python3 scripts/verify-curriculum-seed.py
python3 scripts/verify-non-email-growth-loop.py
python3 scripts/verify-pre-auto-growth-loop.py
python3 scripts/verify-ra-kr-growth-plan.py
python3 scripts/verify-study-scheduler.py
```

**scripts/tests/ (pytest)**
```bash
pytest scripts/tests/
pytest scripts/tests/test_growth_metrics_error_handling.py
```

## Shell Entry Points

**auto-growth-runner.sh**
```bash
bash scripts/auto-growth-runner.sh --start
bash scripts/auto-growth-runner.sh --stop
bash scripts/auto-growth-runner.sh --status
```

**daily-monitoring.sh**
```bash
bash scripts/daily-monitoring.sh
```

**growth-metrics-cron.sh**
```bash
bash scripts/growth-metrics-cron.sh
```

**cold-start-verify.sh**
```bash
bash scripts/cold-start-verify.sh
```

**deploy-local.sh**
```bash
bash scripts/deploy-local.sh --stack honcho
bash scripts/deploy-local.sh --stack virtual-office
```

**deploy-n8n-rpi.sh**
```bash
bash scripts/deploy-n8n-rpi.sh --host raspi5p
```

**detect-device.sh**
```bash
bash scripts/detect-device.sh --print
# Output: t3610 | gx10 | raspi5
```

**configure-glm.sh**
```bash
bash scripts/configure-glm.sh --backend gx10
```

**verify-honcho.sh**
```bash
bash scripts/verify-honcho.sh --quick
bash scripts/verify-honcho.sh --full
```

**install-auto-growth-timer.sh**
```bash
bash scripts/install-auto-growth-timer.sh
```

**install-study-scheduler.sh**
```bash
bash scripts/install-study-scheduler.sh
```

**day1-baseline-simple.sh**
```bash
bash scripts/day1-baseline-simple.sh
```

## systemd Services & Timers

**ra-growth-metrics.service + timer**
```bash
# Timer: Daily at 02:00
# Service: Oneshot → runs growth-metrics-cron.sh
systemctl status ra-growth-metrics.timer
systemctl start ra-growth-metrics.timer
systemctl enable ra-growth-metrics.timer
journalctl -u ra-growth-metrics.service -f
```
Schedule: `OnCalendar=*-*-* 02:00:00` (daily 2 AM)
Persistent: true (runs on boot if missed)

**hermes-auto-growth.service + timer**
```bash
systemctl status hermes-auto-growth.timer
systemctl start hermes-auto-growth.timer
systemctl enable hermes-auto-growth.timer
```
Schedule: Configurable interval (typically daily)

**hermes-study.service + timer**
```bash
systemctl status hermes-study.timer
systemctl start hermes-study.timer
systemctl enable hermes-study.timer
```
Schedule: Daily (configurable, typically late night)

**hermes-daily-monitoring.service + timer**
```bash
systemctl status hermes-daily-monitoring.timer
```
Schedule: Daily at configurable time

## n8n Webhook Triggers

**mail-triage.json**
```bash
# Manual test trigger
POST /webhook/mail-triage-test
Content-Type: application/json
{
  "subject": "Test FDA 510(k) inquiry",
  "from": "test@example.com",
  "body": "We need guidance on 510(k) submission..."
}
```
Full path: `POST /webhook/mail-triage-test`
Production: Gmail IMAP trigger (poll every minute, unread emails)

**feedback-recorder.json**
```bash
# Human feedback webhook
POST /webhook/feedback
Content-Type: application/json
{
  "target": "ra_us",
  "feedback_type": "correction",
  "original_response": "...",
  "corrected_response": "...",
  "human_note": "Missing predicate device analysis"
}
```
Full path: `POST /webhook/feedback`

**infra-vote-broadcast.json**
```bash
# Vote broadcast trigger
POST /webhook/infra-vote
Content-Type: application/json
{
  "topic": "Increase GX10 inference capacity",
  "context": "...",
  "options": ["approve", "reject", "defer"]
}
```
Full path: `POST /webhook/infra-vote`

**wp-close-recorder.json**
```bash
# WP close recording (human-only action)
POST /webhook/wp-close
Content-Type: application/json
{
  "wp_id": "WP-123",
  "close_reason": "Device approved, market authorization complete",
  "human_confirmed": true
}
```
Full path: `POST /webhook/wp-close`
> **[HARD]** WP close/reopen = human-only permanently

## Docker Compose Services

**honcho/docker-compose.yml**
```bash
# Start Honcho stack
docker-compose -f honcho/docker-compose.yml up -d

# Stop Honcho stack
docker-compose -f honcho/docker-compose.yml down

# View logs
docker-compose -f honcho/docker-compose.yml logs -f api
docker-compose -f honcho/docker-compose.yml logs -f deriver
```
Services:
- `api` - FastAPI on `0.0.0.0:8000` (host `:8000`)
- `deriver` - Background worker (no exposed ports)
- `postgres` - pgvector on `0.0.0.0:5433` (host `:5433`)
- `redis` - Redis on `127.0.0.1:6379`

**virtual-office/docker-compose.yml**
```bash
# Start virtual office adapter
docker-compose -f virtual-office/docker-compose.yml up -d

# Rebuild image (after HTML changes)
docker-compose -f virtual-office/docker-compose.yml up -d --build
```
Services:
- `adapter` - Node.js Express on `0.0.0.0:3000` (container internal)
- Host mapping: `:3001` (exposed to user)

**n8n/docker-compose.yml**
```bash
# Start n8n
docker-compose -f n8n/docker-compose.yml up -d

# Access n8n UI
http://raspi5p:5678
```
Services:
- `n8n` - n8n workflow engine on `:5678`

## Hermes API Server Endpoints

**hermes-api-server.py** (Flask on port 8643)

`POST /v1/chat/completions`
- Purpose: RA classification (OpenAI-compatible)
- Auth: `Authorization: Bearer <API_SERVER_KEY>`
- Request Body:
  ```json
  {
    "model": "ra_us",
    "messages": [{"role": "user", "content": "..."}],
    "mail_subject": "...",
    "mail_sender": "...",
    "mail_attachments": [],
    "wp_list": "WP-123, WP-456"
  }
  ```
- Response: OpenAI chat completion format with `wp_comment` in content

`POST /v1/knowledge/fetch`
- Purpose: Layer 4 real-time knowledge lookup (llm-wiki, openFDA, law.go.kr)
- Auth: `Authorization: Bearer <API_SERVER_KEY>`
- Request Body:
  ```json
  {
    "query": "FDA 510(k) predicate device requirements",
    "profile": "ra_us",
    "top": 3
  }
  ```
- Response:
  ```json
  {
    "status": "ok",
    "profile": "ra_us",
    "results": {
      "llm_wiki": [...],
      "openfda": [...],
      "law_kr": [...]
    }
  }
  ```

`GET /v1/models`
- Purpose: List available RA models
- Auth: `Authorization: Bearer <API_SERVER_KEY>`
- Response:
  ```json
  {
    "data": [
      {"id": "ra_us", "owned_by": "hermes"},
      {"id": "ra_eu", "owned_by": "hermes"},
      {"id": "ra_kr", "owned_by": "hermes"}
    ]
  }
  ```

`GET /health`
- Purpose: Health check
- Response: `{"status": true, "service": "hermes-api-server"}`

## Virtual Office Adapter Endpoints

**virtual-office-honcho-adapter.js** (Express on port 3000/3001)

`GET /api/events`
- Purpose: Server-Sent Events (SSE) or polling endpoint for activity log
- Query Params: `?poll=true` (polling mode, no SSE)
- Response: Event stream or JSON array
  ```json
  [
    {"ts": "2026-06-20T10:30:00Z", "type": "mail_received", "actor": "system", "target": "ra_us", "payload": {...}},
    {"ts": "2026-06-20T10:31:00Z", "type": "matched", "actor": "ra_us", "payload": {...}}
  ]
  ```

`GET /health`
- Purpose: Health check
- Response: `{"status": "ok", "data_source": "honcho|mock"}`
