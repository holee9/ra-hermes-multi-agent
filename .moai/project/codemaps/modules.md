# RA Hermes Multi-Agent - Module Catalog

## scripts/ Directory

### Growth & Learning Loop

**autonomous-study-scheduler.py** (Python 3.13)
- Purpose: Bootstrap and delta modes for autonomous RA agent learning from pgvector ra_knowledge
- Key Functions: `bootstrap_mode()`, `delta_mode()`, `study_chunks()`, `record_insights()`, `peer_exchange()`
- Dependencies: Honcho API (:8000), Hermes API (:8643), PostgreSQL pgvector
- Profile/Peer Mapping: ra-us/ra_us, ra-eu/ra_eu, ra-kr/ra_kr (underscore for Honcho, hyphen for Hermes)
- Entry Point: `python3 scripts/autonomous-study-scheduler.py --mode bootstrap|delta --agent ra-us`
- High fan-in: Called by systemd timer, manual growth runs

**daily-growth-runner.py** (Python 3.13)
- Purpose: Plan or run daily KB-driven growth routines (dry-run first, execute gated)
- Key Functions: `plan_growth()`, `run_growth()`, `generate_source_cases()`
- Dependencies: PostgreSQL pgvector, Honcho API
- Entry Point: `python3 scripts/daily-growth-runner.py --plan|--run --date YYYY-MM-DD`
- Output: Growth metrics JSON to reports/

**growth-metrics.py** (Python 3.13)
- Purpose: Calculate growth metrics (correction_rate, first_pass_match_accuracy, confidence_calibration, warmstart_lift)
- Key Functions: `calculate_metrics()`, `generate_report()`
- Dependencies: Honcho API (sessions/messages), PostgreSQL
- Entry Point: `python3 scripts/growth-metrics.py`
- Output: Metrics JSON for dashboard rendering

**curriculum-seed.py** (Python 3.13)
- Purpose: Seed initial curriculum source chunks to pgvector for autonomous study
- Key Functions: `seed_sources()`, `load_source_files()`
- Dependencies: PostgreSQL pgvector, local file system
- Entry Point: `python3 scripts/curriculum-seed.py`

**pre-auto-growth-loop.py** (Python 3.13)
- Purpose: Pre-activation validation and readiness checks for auto-growth
- Key Functions: `verify_readiness()`, `check_activation_policy()`
- Dependencies: Honcho API, PostgreSQL
- Entry Point: `python3 scripts/pre-auto-growth-loop.py`

**non-email-growth-loop.py** (Python 3.13)
- Purpose: Growth loop for non-email-dependent RA knowledge building
- Key Functions: `run_growth_cycle()`, `build_context()`
- Dependencies: Honcho API, Hermes API, PostgreSQL
- Entry Point: `python3 scripts/non-email-growth-loop.py`

**ra-kr-growth-plan.py** (Python 3.13)
- Purpose: KR-specific growth planning and MFDS-focused knowledge building
- Key Functions: `plan_kr_growth()`, `prioritize_mfds_topics()`
- Dependencies: PostgreSQL, Honcho API
- Entry Point: `python3 scripts/ra-kr-growth-plan.py`

**growth-transition-readiness.py** (Python 3.13)
- Purpose: Evaluate readiness to transition from manual to autonomous growth
- Key Functions: `assess_readiness()`, `generate_readiness_report()`
- Dependencies: Honcho API, growth metrics history
- Entry Point: `python3 scripts/growth-transition-readiness.py`

**auto-growth-readiness-report.py** (Python 3.13)
- Purpose: Generate comprehensive readiness report with evidence
- Key Functions: `compile_report()`, `gather_evidence()`
- Dependencies: All growth scripts, metrics history
- Entry Point: `python3 scripts/auto-growth-readiness-report.py`

**render-growth-dashboard.py** (Python 3.13)
- Purpose: Render HTML growth dashboard from metrics JSON
- Key Functions: `render_dashboard()`, `load_metrics()`
- Dependencies: Metrics JSON files, Jinja2 templates
- Entry Point: `python3 scripts/render-growth-dashboard.py`
- Output: docs/growth-dashboard.html

**replay-study-insights-issue49.py** (Python 3.13)
- Purpose: Idempotent replay of study insights from raw payloads (issue #49 recovery)
- Key Functions: `replay_payloads()`, `verify_replay()`
- Dependencies: PostgreSQL, Honcho API, raw insight JSONL backup
- Entry Point: `python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50`

### Knowledge Indexing

**index_ra_knowledge.py** (Python 3.13)
- Purpose: Index llm-wiki, ra-project, MD-process into pgvector ra_knowledge
- Key Functions: `index_markdown_sources()`, `chunk_and_embed()`, `store_chunks()`
- Dependencies: PostgreSQL pgvector, local markdown repos
- Entry Point: `python3 scripts/index_ra_knowledge.py`
- [HARD] Read-only knowledge bases: NEVER write to llm-wiki/ra-project/MD-process repos

**index_github_repos.py** (Python 3.13)
- Purpose: Index GitHub repositories into pgvector
- Key Functions: `clone_and_index()`, `process_repo()`
- Dependencies: git, PostgreSQL pgvector
- Entry Point: `python3 scripts/index_github_repos.py --repo URL`

**knowledge_fetch.py** (Python 3.13)
- Purpose: Layer 4 real-time knowledge fetch (llm-wiki, openFDA, law.go.kr)
- Key Functions: `fetch_llm_wiki()`, `fetch_openfda()`, `fetch_law_kr()`
- Dependencies: HTTP APIs, Qdrant search
- Entry Point: Called by hermes-api-server.py (subprocess)

**nas_indexer_v2.py** (Python 3.13)
- Purpose: Index NAS company documents into Qdrant for RAG
- Key Functions: `scan_nas()`, `embed_and_upload()`
- Dependencies: Qdrant API, Ollama embeddings
- Entry Point: `python3 scripts/nas_indexer_v2.py`

### Operations Tools

**extract_mail_qa.py** (Python 3.13)
- Purpose: Extract QA pairs from historical email conversations
- Key Functions: `extract_qa()`, `format_pairs()`
- Dependencies: Email source files
- Entry Point: `python3 scripts/extract_mail_qa.py`

**meta_extractor.py** (Python 3.13)
- Purpose: Extract metadata from documents for indexing
- Key Functions: `extract_metadata()`, `normalize_fields()`
- Dependencies: Document files
- Entry Point: `python3 scripts/meta_extractor.py`

**op_honcho_backfill.py** (Python 3.13)
- Purpose: Backfill Honcho sessions from historical data
- Key Functions: `backfill_sessions()`, `import_messages()`
- Dependencies: Historical data exports, Honcho API
- Entry Point: `python3 scripts/op_honcho_backfill.py`

### Verification Suite

**verify-*.py** (~12 files)
- Purpose: Targeted verification for each growth component
- Entry Points: `python3 scripts/verify-[component].py`
- Coverage: auto-growth, daily-growth-runner, growth-metrics, growth-dashboard, curriculum-seed, non-email-growth-loop, study-scheduler

**scripts/tests/** (Python pytest)
- Purpose: Unit tests for growth metrics error handling
- Entry Point: `pytest scripts/tests/`

### Shell Scripts

**auto-growth-runner.sh**
- Purpose: Wrapper for auto-growth activation
- Dependencies: Python scripts
- Entry Point: `bash scripts/auto-growth-runner.sh`

**daily-monitoring.sh**
- Purpose: Daily system health checks
- Dependencies: Honcho API health endpoints
- Entry Point: `bash scripts/daily-monitoring.sh` (cron/systemd)

**growth-metrics-cron.sh**
- Purpose: Cron wrapper for growth-metrics.py
- Dependencies: Python 3.13
- Entry Point: `bash scripts/growth-metrics-cron.sh` (systemd timer)

**cold-start-verify.sh**
- Purpose: Verify cold start configuration
- Dependencies: All core services
- Entry Point: `bash scripts/cold-start-verify.sh`

**deploy-local.sh**
- Purpose: Deploy to local environment
- Dependencies: Docker Compose, honcho stack
- Entry Point: `bash scripts/deploy-local.sh`

**deploy-n8n-rpi.sh**
- Purpose: Deploy n8n to Raspberry Pi
- Dependencies: SSH, Docker
- Entry Point: `bash scripts/deploy-n8n-rpi.sh`

**detect-device.sh**
- Purpose: Detect current device (T3610/GX10/RPi)
- Output: Device identifier for conditional logic
- Entry Point: `bash scripts/detect-device.sh --print`

**configure-glm.sh**
- Purpose: Configure GLM inference backend
- Dependencies: GLM binary
- Entry Point: `bash scripts/configure-glm.sh`

**verify-honcho.sh**
- Purpose: Verify Honcho stack health
- Dependencies: Docker Compose
- Entry Point: `bash scripts/verify-honcho.sh`

**install-auto-growth-timer.sh**
- Purpose: Install systemd timer for auto-growth
- Dependencies: systemd
- Entry Point: `bash scripts/install-auto-growth-timer.sh`

**install-study-scheduler.sh**
- Purpose: Install systemd timer for study scheduler
- Dependencies: systemd
- Entry Point: `bash scripts/install-study-scheduler.sh`

**day1-baseline-simple.sh**
- Purpose: Day 1 baseline verification
- Dependencies: Core services
- Entry Point: `bash scripts/day1-baseline-simple.sh`

### JavaScript Verification

**verify-mail-triage-gates.js**
- Purpose: Verify n8n mail-triage workflow gates
- Dependencies: n8n workflow JSON
- Entry Point: `node scripts/verify-mail-triage-gates.js`

**verify-workflows.js**
- Purpose: Verify all n8n workflow syntax
- Dependencies: n8n workflow JSON files
- Entry Point: `node scripts/verify-workflows.js`

### systemd Units

**scripts/systemd/hermes-auto-growth.{service,timer}**
- Purpose: Auto-growth loop activation
- Schedule: Configurable interval
- Activation: `systemctl enable --now hermes-auto-growth.timer`

**scripts/systemd/hermes-daily-monitoring.{service,timer}**
- Purpose: Daily health monitoring
- Schedule: Daily at configurable time
- Activation: `systemctl enable --now hermes-daily-monitoring.timer`

**scripts/systemd/hermes-study.{service,timer}**
- Purpose: Autonomous study scheduler
- Schedule: Daily (configurable)
- Activation: `systemctl enable --now hermes-study.timer`

## n8n/workflows/ Directory

**mail-triage.json** (n8n workflow)
- Purpose: Gmail → RA classification → WP operations
- Trigger: Gmail IMAP poll (unread emails)
- Key Nodes:
  - Gmail Trigger (poll every minute)
  - 본문 파싱 및 규제권 라우팅 (JS code)
  - 라우팅 게이트 (IF: green vs yellow)
  - RA 에이전트 호출 (HTTP POST to Hermes API :8643)
  - RA 응답 파싱 (JS code: validate confidence, parse wp_comment)
  - 파싱 성공 게이트 (IF: parse_error vs yellow_required)
  - 신규 vs 기존 WP 분기 (IF: match existing vs new)
  - Honcho 활동 기록 (HTTP POST to Honcho :8000)
  - OpenProject WP 코멘트 기록 (HTTP POST to OpenProject API)
- External Calls: Gmail IMAP, Hermes API, Honcho API, OpenProject API
- Webhook: Manual test trigger (POST /webhook/mail-triage-test)
- > **⚠️ Drift Warning:** CLAUDE.md declares RA result JSON as `{actor, wp, match, confidence, region, comment, transition_proposed}`. Actual `hermes-api-server.py parse_wp_comment()` emits `{wp_comment: {email_type, wp_title, summary, recommendation, confidence, deadline, product, org, matched_wp_id, source_docs[], market_analysis{mfds,ce_mdr,fda}, flags[]}}`. The workflow parses both formats (Hermes format + flat format).

**mail-triage-fixed.json** (n8n workflow)
- Purpose: Fixed version of mail-triage with bug fixes
- Differences: Addressed parsing edge cases, improved error handling
- Status: Production-ready

**bootstrap-apikey.json** (n8n workflow)
- Purpose: Bootstrap API key for Hermes API server
- Trigger: Manual execution
- Key Nodes: API key generation, storage

**feedback-recorder.json** (n8n workflow)
- Purpose: Record human feedback to Honcho
- Trigger: Webhook (human feedback button)
- Key Nodes:
  - Feedback webhook (POST /webhook/feedback)
  - Honcho message recording (activity_log type)
- External Calls: Honcho API

**feedback-recorder-fixed.json** (n8n workflow)
- Purpose: Fixed version of feedback-recorder
- Status: Production-ready

**infra-to-work-bridge.json** (n8n workflow)
- Purpose: Bridge infra votes to work workspace
- Trigger: Infra vote completion
- Key Nodes:
  - Vote result polling
  - Bridge condition check (bridge-config.json)
  - Relay decision to work workspace
- External Calls: Vote aggregator, Honcho API
- [IF] Bridge conditions intentionally empty per CLAUDE.md principle

**infra-to-work-bridge-fixed.json** (n8n workflow)
- Purpose: Fixed version of infra-to-work-bridge
- Status: Production-ready

**infra-vote-broadcast.json** (n8n workflow)
- Purpose: Broadcast infra voting requests to all infra agents
- Trigger: Manual or scheduled
- Key Nodes:
  - Vote request broadcast
  - Vote collection (wait for responses)
  - Vote aggregation (vote-aggregator.js)
  - Result broadcast
- External Calls: Infra agents (HX11 endpoints), vote-aggregator.js

**wp-close-recorder.json** (n8n workflow)
- Purpose: Record WP close events (human-only action)
- Trigger: Webhook (WP close button)
- Key Nodes:
  - Close webhook (POST /webhook/wp-close)
  - Honcho activity recording (type=wp_closed)
  - Validation: Human approval required
- Gate Rules: [HARD] WP close/reopen = human-only permanently

**wp-close-recorder-fixed.json** (n8n workflow)
- Purpose: Fixed version of wp-close-recorder
- Status: Production-ready

**form-triage-draft.json** (n8n workflow)
- Purpose: Draft form triage workflow
- Status: In development

## virtual-office/ Directory

**virtual-office.html** (HTML + embedded JS/CSS)
- Purpose: Pixel-art real-time activity observer (read-only)
- Characters: 3 RA agents (Mike=ra_us, Theo=ra_eu, Sam=ra_kr)
- Features:
  - Animated pixel-art characters (8-bit style)
  - Real-time activity log rendering
  - Time-ordered event display
  - Static log for past events, live animation for new events
- Data Source: `/api/events` endpoint (virtual-office-honcho-adapter.js)
- Tech: Vanilla HTML/CSS/JS (no frameworks)

**virtual-office-honcho-adapter.js** (Node.js / Express)
- Purpose: Serve `/api/events` from Honcho activity logs
- Port: 3000 (container), 3001 (host via Docker Compose)
- Endpoints:
  - `GET /api/events` - SSE or polling endpoint
  - `GET /health` - Health check
- Key Functions:
  - `adaptHonchoMessage(msg)` - Convert Honcho message to virtual-office event format
  - `postJson(apiUrl, payload)` - HTTP POST helper
- Dependencies: Honcho API (:8000), Express.js
- Environment: `DATA_SOURCE=honcho|mock`, `HONCHO_API_URL`, `PORT=3000`
- Docker: `virtual-office/docker-compose.yml`

**virtual-office-org-chart.md**
- Purpose: Character-to-agent mapping
- Mapping: Mike→ra_us, Theo→ra_eu, Sam→ra_kr

**pixel-character-guide.md**
- Purpose: Sprite swap guide (code-drawn → Kenney CC0 PNG)
- Status: Reference for future asset upgrades

**virtual-office-mvp.md**
- Purpose: Virtual office MVP design spec
- Content: Requirements, feature set, implementation status

**docker-compose.yml**
- Purpose: Containerize virtual-office adapter
- Services: adapter (Node.js), depends_on honcho-api
- Ports: 3000:3000 (internal), mapped to 3001 on host

## voting/ Directory

**vote-aggregator.js** (Node.js ES2024+)
- Purpose: Aggregate infra agent votes with configurable rules
- [IF] Interface only — rules loaded from config/vote-rules.json
- Key Functions:
  - `loadRules()` - Load vote-rules.json
  - `aggregate(votes)` - Compute result from votes
- Input: `[{actor, vote: "approve"|"reject"|"abstain", topic}]`
- Output: `{topic, result: "approved"|"rejected"|"pending", method, tally, weighted, approve_ratio}`
- Config-Driven Behavior:
  - `quorum` - Minimum votes required (default: null)
  - `weights` - Per-actor voting weight (default: all 1)
  - `majority_threshold` - Approval ratio threshold (default: null → simple majority)
  - `fallback_method` - Fallback when rules unset (default: simple_majority)
- Dependencies: fs, path (Node.js built-in)
- Usage: n8n Function node `require('./vote-aggregator')`

**config/vote-rules.json**
- Purpose: Configurable voting rules (infra only, NOT RA judgments)
- Structure:
  - `quorum: 2` - Minimum 2 of 3 infra agents
  - `weights: {infra_t3610: 1, infra_gx10: 1, infra_rpi: 1}` - Equal weights initially
  - `majority_threshold: 0.66` - 2/3 supermajority
  - `fallback_method: "configured_supermajority"` - Named fallback
  - `timeout_seconds: 900` - 15-minute vote collection window
  - `abstain_policy: "exclude_from_decisive_ratio"` - Abstentions don't count toward ratio
- [HARD] These rules apply ONLY to infra votes, NOT RA regulatory decisions

## bridge/ Directory

**config/bridge-config.json**
- Purpose: [IF] Bridge relay conditions — intentionally empty
- Structure:
  - `relay_threshold: null` - No minimum threshold
  - `relay_conditions: []` - Empty array = relay all decisions
- Notes:
  - "초기 운영: 모든 infra 결정을 업무 workspace로 전달" (Initial ops: relay all infra decisions)
  - Conditions populated from observed patterns over time
- [IF] Principle: Config-driven, not hardcoded

## e2e/ Directory

**growth-dashboard.spec.js** (Playwright)
- Purpose: E2E test for growth dashboard rendering
- Framework: @playwright/test
- Test Cases:
  - Renders static growth dashboard snapshot
  - Shows current growth measurement and readiness status
  - Renders visual charts and status indicators
- Entry Point: `npm run test:e2e` or `playwright test`
- Coverage: KPI metrics, growth signals, coverage guards, readiness matrix

**virtual-office.spec.js** (Playwright)
- Purpose: E2E test for virtual office activity observer
- Framework: @playwright/test
- Test Cases:
  - Renders pixel-art characters
  - Displays activity log
  - Updates in real-time
- Entry Point: `npm run test:e2e`

## honcho/ Directory

**docker-compose.yml**
- Purpose: Honcho stack (api + deriver + postgres + redis)
- Services:
  - `api` - FastAPI app (`plasticlabs/honcho:latest`) on :8000
  - `deriver` - Python deriver worker (processes queue)
  - `postgres` - `pgvector/pgvector:pg15` on :5433
  - `redis` - `redis:7-alpine` on :6379
- Dependencies:
  - api depends_on postgres/redis (healthcheck)
  - deriver depends_on postgres/redis (healthcheck)
- Volumes: `postgres_data` (persistent)
- Environment: `.env` file with `POSTGRES_*`, `DB_CONNECTION_URI`, `CACHE_URL`

**init-workspaces.sh**
- Purpose: Initialize Honcho workspaces (work, ra-hermes)
- Entry Point: `bash honcho/init-workspaces.sh`

## systemd/ Directory

**ra-growth-metrics.service** (systemd unit)
- Purpose: Run growth metrics collection
- Type: oneshot
- User: abyz-lab
- WorkingDirectory: `/home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent`
- ExecStart: `/usr/bin/bash scripts/growth-metrics-cron.sh`
- StandardOutput/Error: append to `/var/log/ra-growth-metrics.log`

**ra-growth-metrics.timer** (systemd timer)
- Purpose: Daily trigger at 02:00
- OnCalendar: `*-*-* 02:00:00`
- Persistent: true (runs on boot if missed)
- WantedBy: timers.target

## feedback/config/ Directory

**growth-trigger-config.json**
- Purpose: [IF] Metric-gated growth trigger conditions — intentionally empty
- Structure:
  - `correction_rate_threshold: null`
  - `first_pass_match_accuracy_threshold: null`
  - `confidence_calibration_threshold: null`
  - `warmstart_lift_threshold: null`
- [IF] Principle: Triggers populated from growth metrics observation

**weight-adjustment-config.json**
- Purpose: Configurable weight adjustment rules
- Structure:
  - `performance_weight_adjustment: {}`
  - `quality_weight_adjustment: {}`
  - `consistency_weight_adjustment: {}`
- Usage: Future agent performance tuning

## Root Configuration

**package.json**
- Purpose: Root package.json for npm scripts and Playwright
- Scripts:
  - `test` - Run static + E2E tests
  - `test:static` - Verify workflows, compile Python, check shell scripts
  - `test:e2e` - Run Playwright tests
- DevDependencies: `@playwright/test@^1.60.0`

**playwright.config.js**
- Purpose: Playwright configuration for E2E tests
- Framework: @playwright/test
- Test Directory: `e2e/`
- Timeout: 30s (default)
