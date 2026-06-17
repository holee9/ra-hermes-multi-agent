# Entry Points Catalog

## Server & Service Entry Points

### Honcho Server
- **Location**: `honcho-src/src/main.py`
- **Purpose**: FastAPI application entry point
- **Technology**: Python 3.13+, FastAPI 0.115+
- **Invocation**: `uv run fastapi dev src/main.py`
- **Port**: 8000 (default)
- **Responsibilities**:
  - Application initialization and middleware setup
  - Router registration (/v3 API endpoints)
  - Lifespan management (startup/shutdown hooks)
  - Global exception handlers
  - Telemetry and monitoring setup
- **Key Components**:
  - FastAPI app creation
  - CORS middleware configuration
  - Router inclusion: workspaces, peers, sessions, messages, conclusions, keys, webhooks
  - Sentry error tracking integration
  - Prometheus metrics endpoint
  - Database and cache initialization
- **Environment Variables**:
  - `DATABASE_URL`: PostgreSQL connection string
  - `REDIS_URL`: Redis connection string
  - `HONCHO_ENV`: Environment (development/production)
  - `EMBEDDING_MODEL_CONFIG`: Embedding provider configuration
  - `LLM_API_KEY`: LLM provider authentication

### Deriver Worker
- **Location**: `honcho-src/src/deriver/__main__.py`
- **Purpose**: Background queue consumer for memory formation
- **Technology**: Python 3.13+, uvloop
- **Invocation**: `uv run python -m src.deriver`
- **Responsibilities**:
  - Queue management and message processing
  - Deriver execution (memory formation)
  - Reconciler scheduling (embedding sync, queue cleanup)
  - Background task coordination
- **Key Components**:
  - QueueManager lifecycle
  - Representation task processing
  - Deriver batch processing
  - Reconciler scheduler integration
  - Error handling and retry logic
- **Scalability**: Multiple instances via `DERIVER_WORKERS` environment variable

## Python Script Entry Points

### Growth & Learning Automation

#### autonomous-study-scheduler.py
- **Location**: `scripts/autonomous-study-scheduler.py`
- **Purpose**: Bootstrap and delta study scheduling for RA agents
- **Technology**: Python 3.13+, FastAPI, Honcho SDK
- **Invocation**: `python scripts/autonomous-study-scheduler.py --mode [bootstrap|delta]`
- **Parameters**:
  - `--mode bootstrap`: Initial curriculum seeding from source materials
  - `--mode delta`: Incremental learning from new cases
  - `--peer_id`: Target peer (ra_us, ra_eu, ra_kr)
  - `--max_cases`: Maximum cases to process (default: 10)
- **Dependencies**: Honcho API, PostgreSQL/pgvector, Layer 4 APIs
- **Output**: Study insights recorded in Honcho peer memory

#### daily-growth-runner.py
- **Location**: `scripts/daily-growth-runner.py`
- **Purpose**: Daily growth loop automation for non-email cases
- **Technology**: Python 3.13+, Honcho SDK
- **Invocation**: `python scripts/daily-growth-runner.py`
- **Parameters**:
  - `--dry-run`: Simulate without execution
  - `--peer_id`: Target peer for growth
  - `--source`: Source type (non-email, qa, document)
- **Dependencies**: Honcho API, PostgreSQL/pgvector
- **Output**: Growth metrics and performance reports

#### growth-metrics.py
- **Location**: `scripts/growth-metrics.py`
-**Purpose**: Calculate and report growth performance metrics
- **Technology**: Python 3.13+, PostgreSQL
- **Invocation**: `python scripts/growth-metrics.py`
- **Metrics Calculated**:
  - Correction rate (human feedback / total decisions)
  - First-pass match accuracy (correct WP matching / total attempts)
  - Confidence calibration (prediction confidence vs actual accuracy)
  - Warmstart lift (improvement from cold start)
  - Escalation precision (appropriate human reviews)
- **Dependencies**: Honcho API, PostgreSQL
- **Output**: JSON report to `reports/growth-YYYY-MM-DD.json`

#### auto-growth-readiness-report.py
- **Location**: `scripts/auto-growth-readiness-report.py`
- **Purpose**: Generate 4x4 readiness matrix for auto-growth
- **Technology**: Python 3.13+, PostgreSQL
- **Invocation**: `python scripts/auto-growth-readiness-report.py`
- **Readiness Dimensions**:
  - Knowledge foundation (curriculum seeds, Layer 4 APIs)
  - Individual growth inputs (growth loops, timer status)
  - Growth proof data (sessions, messages, metrics)
  - Runtime safety gates (Yellow gates, validation)
  - Infrastructure consensus (vote rules, broadcast)
- **Output**: Readiness matrix JSON report

### Knowledge Management

#### index_ra_knowledge.py
- **Location**: `scripts/index_ra_knowledge.py`
- **Purpose**: Index regulatory knowledge into pgvector
- **Technology**: Python 3.13+, pgvector, Gitea API
- **Invocation**: `python scripts/index_ra_knowledge.py --source [github|local]`
- **Parameters**:
  - `--source github`: Index from GitHub repositories
  - `--source local`: Index from local files
  - `--repo`: Repository name (for GitHub source)
- **Dependencies**: PostgreSQL/pgvector, Gitea API
- **Output**: Vector embeddings in `ra_knowledge` table

#### curriculum-seed.py
- **Location**: `scripts/curriculum-seed.py`
- **Purpose**: Seed source-level curriculum for RA agents
- **Technology**: Python 3.13+, Honcho SDK
- **Invocation**: `python scripts/curriculum-seed.py --peer_id [ra_us|ra_eu|ra_kr]`
- **Parameters**:
  - `--peer_id`: Target peer for curriculum seeding
  - `--source`: Source directory or repository
  - `--max_cases`: Maximum cases to process
- **Dependencies**: Honcho API, PostgreSQL
- **Output**: Curriculum seeds in peer memory

#### knowledge_fetch.py
- **Location**: `scripts/knowledge_fetch.py`
- **Purpose**: Fetch real-time regulatory knowledge from Layer 4 APIs
- **Technology**: Python 3.13+, HTTP requests
- **Invocation**: `python scripts/knowledge_fetch.py --api [lawgokr|openFDA|datagokr]`
- **APIs**:
  - `lawgokr`: Korean legal framework search
  - `openFDA`: US regulatory database lookup
  - `datagokr`: Korean MFDS device information
- **Dependencies**: Layer 4 API endpoints
- **Output**: Structured knowledge data for LLM context

### Data Integration

#### op_honcho_backfill.py
- **Location**: `scripts/op_honcho_backfill.py`
- **Purpose**: Backfill Honcho memory from OpenProject historical data
- **Technology**: Python 3.13+, OpenProject API, Honcho SDK
- **Invocation**: `python scripts/op_honcho_backfill.py --days [N]`
- **Parameters**:
  - `--days`: Number of days to backfill
  - `--workspace`: Target Honcho workspace
  - `--peer_id`: Target peer for memory storage
- **Dependencies**: OpenProject API, Honcho API
- **Output**: Historical work packages as peer memories

#### extract_mail_qa.py
- **Location**: `scripts/extract_mail_qa.py`
- **Purpose**: Extract QA pairs from email history for training
- **Technology**: Python 3.13+, Email parsing
- **Invocation**: `python scripts/extract_mail_qa.py --source [mbox|eml]`
- **Parameters**:
  - `--source`: Email format (mbox or eml)
  - `--output`: Output directory for extracted data
- **Dependencies**: Email parsing libraries
- **Output**: Structured QA pairs for knowledge base

#### nas_indexer_v2.py
- **Location**: `scripts/nas_indexer_v2.py`
- **Purpose**: Index Gitea repositories from NAS storage
- **Technology**: Python 3.13+, Gitea API
- **Invocation**: `python scripts/nas_indexer_v2.py --repo [name]`
- **Dependencies**: Gitea API, PostgreSQL/pgvector
-**Output**: Vector embeddings in knowledge base

### Verification & Recovery

#### replay-study-insights-issue49.py
- **Location**: `scripts/replay-study-insights-issue49.py`
- **Purpose**: Replay study insights after peer_id correction (Issue #49)
- **Technology**: Python 3.13+, PostgreSQL
- **Invocation**: `python scripts/replay-study-insights-issue49.py --execute --batch-size 50`
- **Parameters**:
  - `--execute`: Execute replay (default: dry-run)
  - `--batch-size`: Number of insights per batch
- **Dependencies**: PostgreSQL, Honcho API
- **Output**: Corrected peer memories with `ra_us`/`ra_eu` peer IDs

## n8n Workflow Entry Points

### Business Workflows

#### mail-triage.json
- **Location**: `n8n/workflows/mail-triage.json`
- **Purpose**: Email triage and routing to RA agents
- **Trigger**: Incoming email webhook
- **Key Processing Steps**:
  1. Email parsing and content extraction
  2. OpenProject work package lookup
  3. RA agent consultation via Honcho API
  4. Confidence threshold validation
  5. Yellow gate escalation if low confidence
  6. Work package routing/creation
- **Dependencies**: OpenProject API, Honcho API
- **Output**: RA analysis result JSON, routing decision

#### feedback-recorder.json
- **Location**: `n8n/workflows/feedback-recorder.json`
- **Purpose**: Capture human feedback on agent decisions
- **Trigger**: Human feedback submission
- **Key Processing Steps**:
  1. Feedback validation and normalization
  2. Agent judgment recording in Honcho
  3. Human correction storage
  4. Growth metrics calculation
- **Dependencies**: Honcho API
- **Output**: Feedback records in peer memory

#### wp-close-recorder.json
- **Location**: `n8n/workflows/wp-close-recorder.json`
- **Purpose**: Record work package closure events
- **Trigger**: OpenProject status webhook
- **Key Processing Steps**:
  1. Closure event detection
  2. Case digest generation
  3. Honcho memory storage
  4. Growth metrics update
- **Dependencies**: OpenProject API, Honcho API
- **Output**: Closure records and performance metrics

### Infrastructure Workflows

#### infra-vote-broadcast.json
- **Location**: `n8n/workflows/infra-vote-broadcast.json`
- **Purpose**: Aggregate and broadcast infrastructure votes
- **Trigger**: Vote submission from infrastructure agents
- **Key Processing Steps**:
  1. Vote collection (2/3 quorum rule)
  2. Result aggregation
  3. Broadcast to business workspace
  4. Consensus decision tracking
- **Dependencies**: Voting system APIs, bridge/
- **Output**: Consensus results broadcast

#### infra-to-work-bridge.json
- **Location**: `n8n/workflows/infra-to-work-bridge.json`
- **Purpose**: Translate infrastructure events to business workspace
- **Trigger**: Infrastructure events
- **Key Processing Steps**:
  1. Event receipt from infrastructure
  2. Event translation and routing
  3. Business workspace delivery
  4. Error handling and retry
- **Dependencies**: bridge/, Honcho API
- **Output**: Business-readable events

## Command-Line Interfaces

### Honcho CLI
- **Entry Point**: `honcho-src/honcho-cli/`
- **Purpose**: Command-line interface for Honcho workspace management
- **Technology**: Python 3.13+, Click
- **Commands**:
  - `honcho peers list`: List all peers
  - `honcho sessions create`: Create new session
  - `honcho messages send`: Send messages to peers
  - `honcho conclusions query`: Query peer conclusions
- **Dependencies**: Honcho API

### System Service Entry Points

#### systemd Services
- **Location**: `systemd/`
- **Services**:
  - `ra-growth-metrics.service`: Daily growth metrics timer
  - `ra-growth-metrics.timer`: Daily execution at 02:00 KST
  - `hermes-auto-growth.service`: Auto-growth scheduler
  - `hermes-auto-growth.timer`: Scheduled growth loop
- **Invocation**: `systemctl start/enable/disable [service]`
- **Dependencies**: Python scripts, Honcho API

## Web Interface Entry Points

### Virtual Office
- **Location**: `virtual-office/virtual-office.html`
- **Purpose**: Read-only visualization of Honcho activity
- **Technology**: Self-contained HTML (no build step)
- **Access**: Direct file open in browser
- **Features**:
  - Pixel-art character visualization
  - Real-time activity monitoring
  - Honcho event log display
- **Data Source**: Honcho Activity Log API (`GET /v1/activity`)
- **Dependencies**: Honcho server (read-only access)

### Growth Dashboard
- **Location**: GitHub Pages (published via `render-growth-dashboard.py`)
- **Purpose**: HTML-based growth operations dashboard
- **Technology**: Static HTML with embedded JSON data
- **Access**: `https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html`
- **Features**:
  - RA Growth Operations summary
  - Per-agent growth cards
  - Growth signal flow diagram
  - Growth measurement status
  - Coverage evidence
- **Data Source**: `reports/growth-*.json` files
- **Dependencies**: Growth metrics JSON reports

## API Entry Points (REST)

### Honcho API (`/v3/`)

#### Workspace Operations
- `POST /v3/workspaces`: Create workspace
- `POST /v3/workspaces/list`: List workspaces
- `POST /v3/workspaces/search`: Search workspaces
- `POST /v3/workspaces/{id}`: Get workspace details

#### Peer Operations
- `POST /v3/peers`: Create peer
- `POST /v3/peers/list`: List peers
- `POST /v3/peers/{peer_id}/chat`: Chat with peer (Dialectic)
- `POST /v3/peers/{peer_id}/messages`: List peer messages

#### Session Operations
- `POST /v3/sessions`: Create session
- `POST /v3/sessions/list`: List sessions
- `POST /v3/sessions/{session_id}/peers`: Manage session participants

#### Message Operations
- `POST /v3/messages`: Create messages (batch up to 100)
- `POST /v3/messages/list`: List messages
- `POST /v3/messages/{id}`: Get message details

#### Conclusion Operations
- `POST /v3/conclusions`: Create conclusions
- `POST /v3/conclusions/query`: Semantic search
- `POST /v3/conclusions/list`: List conclusions

#### Utility Operations
- `POST /v3/keys`: Create scoped JWT keys
- `POST /v3/webhooks`: Register webhook
- `GET /metrics`: Prometheus metrics

## Development Entry Points

### Testing
- **Unit Tests**: `pytest tests/`
- **Integration Tests**: `pytest tests/integration/`
- **Live LLM Tests**: `pytest tests/live_llm/` (requires `--live-llm` flag)
- **Benchmark Tests**: `pytest tests/bench/`

### Code Quality
- **Linting**: `uv run ruff check src/`
- **Formatting**: `uv run ruff format src/`
- **Type Checking**: `uv run basedpyright`

### Build & Package
- **Installation**: `uv sync`
- **Package Build**: `uv build`
- **Distribution**: `uv publish`

---
Generated: 2026-06-17
Total Entry Points: 30+ across servers, scripts, workflows, and APIs
