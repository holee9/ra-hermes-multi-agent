# Module Catalog

## Core Business Modules

### RA Agent Profiles (`profiles/`)

#### ra-us (US Regulatory Affairs Expert)
- **Purpose**: US FDA regulatory compliance and device classification
- **Responsibilities**:
  - FDA 510(k) submission guidance
  - SaMD vs SiMD classification
  - US regulatory pathway analysis
  - FDA recall and alert monitoring
- **Dependencies**: Honcho memory system, Layer 4 APIs (openFDA)
- **Configuration**: `profiles/ra-us/SOUL.md` persona definition
- **Key Files**: SOUL.md, configuration templates

#### ra-eu (EU Regulatory Affairs Expert)
- **Purpose**: EU MDR compliance and CE marking guidance
- **Responsibilities**:
  - MDR classification and conformity assessment
  - CE marking requirements
  - EU regulatory pathway analysis
  - European competent authority interactions
- **Dependencies**: Honcho memory system, Layer 4 APIs (if applicable)
- **Configuration**: `profiles/ra-eu/SOUL.md` persona definition
- **Key Files**: SOUL.md, configuration templates

#### ra-kr (Korea Regulatory Affairs Expert)
- **Purpose**: MFDS approval and Korean regulatory compliance
- **Responsibilities**:
  - MFDS device licensing and approval
  - Korean regulatory pathway analysis
  - Post-market surveillance requirements
  - Korea-specific labeling and documentation
- **Dependencies**: Honcho memory system, Layer 4 APIs (data.go.kr MFDS)
- **Configuration**: `profiles/ra-kr/SOUL.md` persona definition
- **Key Files**: SOUL.md, configuration templates

## Honcho Server Modules (`honcho-src/`)

### Core API (`src/`)
- **main.py**: FastAPI application entry point
  - Middleware: CORS, validation, error handlers
  - Router registration: /v3 API endpoints
  - Lifespan: Startup/shutdown hooks
- **config.py**: Hierarchical configuration (env > .env > config.toml > defaults)
- **db.py**: Database engine and session management
- **models.py**: SQLAlchemy ORM models (Workspace, Peer, Session, Message, etc.)
- **security.py**: JWT authentication and authorization

### Routers (`src/routers/`)
- **workspaces.py**: Workspace CRUD operations
- **peers.py**: Peer management and chat endpoint (Dialectic agent)
- **sessions.py**: Session management and multi-peer coordination
- **messages.py**: Message creation and batch operations
- **conclusions.py**: Conclusion (observation) API endpoints
- **keys.py**: Scoped JWT key generation
- **webhooks.py**: Webhook registration and delivery

### CRUD Operations (`src/crud/`)
- **representation.py**: Peer representation management
- **peer.py**: Peer profile and card operations
- **message.py**: Message CRUD with batch support
- **session.py**: Session lifecycle and participant management
- **workspace.py**: Workspace configuration and operations

### Agent Systems (`src/dialectic/`, `src/deriver/`, `src/dreamer/`)
- **dialectic/chat.py**: Agentic chat with tool-using Dialectic
- **dialectic/core.py**: DialecticAgent tool loop implementation
- **deriver/deriver.py**: Minimal deriver for memory formation
- **deriver/queue_manager.py**: Background queue consumer
- **dreamer/orchestrator.py**: Dream coordination and specialist management
- **dreamer/specialists.py**: Deduction/Induction specialists

### LLM Subsystem (`src/llm/`)
- **api.py**: Provider-agnostic LLM API abstraction
- **backends/**: Provider implementations (anthropic, gemini, openai)
- **tool_loop.py**: Agentic tool execution framework
- **structured_output.py**: Structured output handling
- **caching.py**: LLM response caching

### Vector & Knowledge (`src/vector_store/`)
- **PostgreSQL/pgvector**: Default vector store (via MessageEmbedding model)
- **LanceDB**: Alternative vector store option
- **Turbopuffer**: Alternative vector store option

### Telemetry (`src/telemetry/`)
- **metrics_collector.py**: Prometheus metrics collection
- **events/**: CloudEvents type definitions
- **prometheus/**: Prometheus metric definitions
- **sentry.py**: Error tracking integration

## Automation Scripts (`scripts/`)

### Growth & Learning
- **autonomous-study-scheduler.py**: Bootstrap and delta study scheduling
- **daily-growth-runner.py**: Daily growth loop automation
- **growth-metrics.py**: Performance metrics calculation and reporting
- **auto-growth-readiness-report.py**: 4x4 matrix readiness assessment

### Knowledge Management
- **index_ra_knowledge.py**: Vector database indexing
- **curriculum-seed.py**: Source-level curriculum seeding
- **knowledge_fetch.py**: Layer 4 API integration
- **meta_extractor.py**: Knowledge metadata extraction

### Data Integration
- **extract_mail_qa.py**: Email QA dataset extraction
- **op_honcho_backfill.py**: OpenProject historical data import
- **nas_indexer_v2.py**: NAS Gitea repository indexing

### Specialized Growth
- **ra-kr-growth-plan.py**: Korea-specific growth planning
- **non-email-growth-loop.py**: Non-email growth automation
- **pre-auto-growth-loop.py**: Pre-growth automation scripts

### Verification & Validation
- **verify-*.py**: Test suites for each growth component
- **replay-study-insights-issue49.py**: Issue #49 recovery tool

## n8n Workflow Modules (`n8n/workflows/`)

### Core Business Workflows
- **mail-triage.json**: Email classification and routing to RA agents
  - Email parsing and analysis
  - Confidence threshold checking
  - Work package lookup and routing
  - Yellow gate escalation

### Feedback & Recording
- **feedback-recorder.json**: Human feedback capture
  - Feedback webhook handling
  - Agent judgment recording
  - Human correction storage

- **wp-close-recorder.json**: Work package closure automation
  - OpenProject status monitoring
  - Closure event recording
  - Case digest generation

### Infrastructure Integration
- **infra-vote-broadcast.json**: Infrastructure voting broadcast
  - Vote aggregation (2/3 quorum)
  - Result distribution to business workspace
  - Consensus decision tracking

- **infra-to-work-bridge.json**: Infrastructure-to-business communication
  - Unidirectional data flow (infra → business)
  - Event translation and routing
  - Error handling and retry logic

### Draft/Experimental
- **form-triage-draft.json**: Form-based triage workflow (draft status)

## Integration Modules

### Bridge System (`bridge/`)
- **Purpose**: Infrastructure-to-business communication layer
- **Components**: Configuration, message translation, error handling
- **Dependencies**: n8n, Honcho API

### Voting System (`voting/`)
- **Purpose**: Vote-based consensus for infrastructure decisions
- **Components**: Vote rules, aggregation, broadcasting
- **Dependencies**: n8n, infrastructure APIs

### Virtual Office (`virtual-office/`)
- **Purpose**: Read-only visualization of Honcho activity
- **Technology**: Self-contained HTML (no build step required)
- **Data Source**: Honcho activity log API
- **Features**: Pixel-art character visualization, activity monitoring

## Documentation Modules (`docs/`)

### Design & Architecture
- **RA-multi-agent-master-design.md**: System architecture and design decisions
- **implementation-spec.md**: Detailed implementation specifications
- **operations-guide.md**: Operational procedures and runbooks

### Project Documentation
- **ADR/**: Architecture Decision Records
- **incidents/**: Incident reports and resolutions
- **growth-dashboard.md**: Dashboard documentation and metrics

## External Dependencies

### APIs & Services
- **OpenProject API**: Work package and project management
- **Layer 4 APIs**: Real-time regulatory knowledge
  - law.go.kr: Korean legal framework
  - openFDA: US regulatory information
  - data.go.kr: Korean MFDS database

### Infrastructure Services
- **PostgreSQL/pgvector**: Primary database and vector store
- **Redis**: Caching layer for Honcho
- **n8n**: Workflow automation platform
- **Docker**: Container orchestration

---
Generated: 2026-06-17
Total Modules: 30+ core modules across business, infrastructure, and integration layers
