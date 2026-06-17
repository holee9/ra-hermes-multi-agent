# Dependency Graph

## Module Dependency Relationships

### Core System Dependencies

```
RA Hermes System
├─ Business Workspace
│  ├─ Honcho Server (honcho-src/)
│  │  ├─ FastAPI Framework
│  │  ├─ SQLAlchemy 2.0 (ORM)
│  │  ├─ Pydantic v2 (Validation)
│  │  ├─ PostgreSQL/pgvector (Database + Vector Store)
│  │  └─ Redis (Cache)
│  │
│  ├─ RA Agent Profiles (profiles/)
│  │  ├─ ra-us → Honcho Memory System
│  │  ├─ ra-eu → Honcho Memory System
│  │  └─ ra-kr → Honcho Memory System
│  │
│  ├─ Python Scripts (scripts/)
│  │  ├─ autonomous-study-scheduler.py → Honcho API
│  │  ├─ growth-metrics.py → Honcho API
│  │  ├─ index_ra_knowledge.py → PostgreSQL/pgvector
│  │  └─ daily-growth-runner.py → Honcho API
│  │
│  └─ n8n Workflows (n8n/workflows/)
│     ├─ mail-triage.json → OpenProject API, Honcho API
│     ├─ feedback-recorder.json → Honcho API
│     ├─ wp-close-recorder.json → OpenProject API
│     └─ infra-vote-broadcast.json → voting/
│
└─ Infrastructure Workspace
   ├─ bridge/ → n8n, Honcho API
   ├─ voting/ → n8n, infrastructure APIs
   └─ virtual-office/ → Honcho Activity Log API
```

## Internal Module Dependencies

### Honcho Server (`honcho-src/src/`)

```
main.py (Entry Point)
├─ config.py (Configuration)
├─ db.py (Database Engine)
├─ security.py (JWT Authentication)
│
├─ routers/ (API Endpoints)
│  ├─ workspaces.py → crud/workspace.py
│  ├─ peers.py → crud/peer.py
│  │  └─ dialectic/chat.py (Dialectic Agent)
│  ├─ sessions.py → crud/session.py
│  ├─ messages.py → crud/message.py
│  ├─ conclusions.py → crud/conclusion.py
│  ├─ keys.py → security.py
│  └─ webhooks.py → crud/webhook.py
│
├─ crud/ (Database Operations)
│  ├─ All CRUD modules → models.py, db.py
│  └─ representation.py → vector_store/
│
├─ dialectic/ (Dialectic Agent)
│  ├─ chat.py → utils/agent_tools.py
│  ├─ core.py → llm/, utils/agent_tools.py
│  └─ prompts.py
│
├─ deriver/ (Memory Formation)
│  ├─ queue_manager.py → deriver.py, reconciler/
│  ├─ deriver.py → llm/, prompts.py
│  └─ enqueue.py → models.py
│
├─ dreamer/ (Memory Consolidation)
│  ├─ orchestrator.py → specialists.py
│  ├─ specialists.py → llm/, utils/agent_tools.py
│  └─ surprisal.py → crud/
│
├─ llm/ (LLM Abstraction)
│  ├─ api.py → backends/, executor.py
│  ├─ backends/ (anthropic, gemini, openai)
│  ├─ tool_loop.py → api.py, backends/
│  └─ structured_output.py → api.py
│
├─ vector_store/ (Vector Stores)
│  ├─ lancedb.py (Alternative)
│  └─ turbopuffer.py (Alternative)
│
├─ cache/ (Redis Cache)
│  └─ client.py
│
├─ telemetry/ (Observability)
│  ├─ metrics_collector.py → prometheus/
│  ├─ events/ (Event Definitions)
│  └─ prometheus/ (Metrics)
│
└─ utils/ (Utilities)
   ├─ agent_tools.py (Tool Definitions)
   ├─ summarizer.py (Session Summarization)
   └─ representation.py (Representation Formatting)
```

### Python Scripts (`scripts/`)

```
Growth & Learning
├─ autonomous-study-scheduler.py
│  └─ → Honcho API, PostgreSQL/pgvector
├─ daily-growth-runner.py
│  └─ → Honcho API, PostgreSQL/pgvector
├─ growth-metrics.py
│  └─ → Honcho API, PostgreSQL/pgvector
└─ auto-growth-readiness-report.py
   └─ → Honcho API, PostgreSQL/pgvector

Knowledge Management
├─ index_ra_knowledge.py
│  └─ → PostgreSQL/pgvector, external APIs
├─ curriculum-seed.py
│  └─ → Honcho API, PostgreSQL/pgvector
├─ knowledge_fetch.py
│  └─ → Layer 4 APIs (external)
└─ meta_extractor.py
   └─ → PostgreSQL/pgvector

Data Integration
├─ extract_mail_qa.py
│  └─ → PostgreSQL/pgvector
├─ op_honcho_backfill.py
│  └─ → OpenProject API, Honcho API
└─ nas_indexer_v2.py
   └─ → Gitea API, PostgreSQL/pgvector

Specialized Growth
├─ ra-kr-growth-plan.py
│  └─ → Honcho API, PostgreSQL/pgvector
├─ non-email-growth-loop.py
│  └─ → Honcho API, PostgreSQL/pgvector
└─ pre-auto-growth-loop.py
   └─ → Honcho API, PostgreSQL/pgvector

Verification
└─ replay-study-insights-issue49.py
   └─ → PostgreSQL/pgvector, Honcho API
```

### n8n Workflows (`n8n/workflows/`)

```
Business Workflows
├─ mail-triage.json
│  ├─ → OpenProject API (WP Lookup)
│  ├─ → Honcho API (Agent Consultation)
│  └─ → feedback-recorder.json
│
├─ feedback-recorder.json
│  └─ → Honcho API (Feedback Storage)
│
└─ wp-close-recorder.json
   └─ → OpenProject API (Status Monitoring)

Infrastructure Workflows
├─ infra-vote-broadcast.json
│  ├─ → voting/ (Vote Aggregation)
│  └─ → bridge/ (Broadcast)
│
├─ infra-to-work-bridge.json
│  └─ → Honcho API (Event Translation)
│
└─ form-triage-draft.json
   └─ → OpenProject API (Draft)
```

## External Service Dependencies

### Database & Cache
```
PostgreSQL/pgvector
├─ Honcho Server (Primary DB + Vector Store)
├─ Knowledge Base (ra_knowledge)
└─ Analytics (Growth Metrics)
   ↑
Redis (Cache Layer)
└─ Honcho Server (Peer Representations)
```

### API Integrations
```
OpenProject API
├─ mail-triage.json (WP Lookup & Status)
├─ wp-close-recorder.json (Status Monitoring)
└─ op_honcho_backfill.py (Historical Data)

Layer 4 APIs
├─ knowledge_fetch.py (Real-time Regulatory Knowledge)
│  ├─ law.go.kr (Korean Legal Framework)
│  ├─ openFDA (US Regulatory Database)
│  └─ data.go.kr (Korean MFDS Database)
└─ ra-us/ra-eu/ra-kr (Domain-Specific Knowledge)

GX10 Inference Backend
└─ Honcho Server (LLM Tool Execution)
   ↑
n8n Workflow Automation
├─ Honcho API (Agent Consultation)
├─ OpenProject API (WP Operations)
└─ Internal Webhooks (Feedback Recording)
```

## Data Flow Dependencies

### Email Processing Pipeline
```
Email Input
  → n8n mail-triage.json
    → OpenProject API (WP Lookup)
    → Honcho API (RA Agent Analysis)
    → Yellow Gate (Human Review if low confidence)
    → OpenProject API (WP Update/Creation)
```

### Memory Formation Pipeline
```
Human/Agent Interactions
  → Honcho API (Message Creation)
    → PostgreSQL (Message Storage)
    → Redis Cache (Temporary Queue)
    → Deriver Process (Background)
      → LLM Backend (Memory Extraction)
      → PostgreSQL (Vector Embeddings)
      → Dialectic Agent (Context Retrieval)
```

### Growth Loop Pipeline
```
Daily Schedule
  → daily-growth-runner.py
    → PostgreSQL (New Cases)
    → Honcho API (Agent Processing)
      → LLM Backend (Analysis)
      → PostgreSQL (Results Storage)
    → growth-metrics.py (Performance Calculation)
      → PostgreSQL (Metrics Aggregation)
      → Report Generation
```

## Technology Stack Dependencies

### Backend Framework
```
FastAPI 0.115+
├─ Pydantic v2.9 (Data Validation)
├─ SQLAlchemy 2.0 (ORM)
├─ Python 3.13+ (Runtime)
└─ uv (Package Management)
```

### Database & Storage
```
PostgreSQL 16+
├─ pgvector Extension (Vector Similarity)
├─ HNSW Indexes (High-Dimensional Search)
└─ JSONB Metadata (Flexible Schema)

Redis 7+
└─ Cashews (Python Cache Client)
```

### LLM & AI
```
Provider-Agnostic LLM Layer
├─ Anthropic (Claude Models)
├─ Gemini (Google Models)
└─ OpenAI (GPT Models)
  ↑
Tool Loop Framework
├─ Dialectic Agent (Chat & Recall)
├─ Deriver (Memory Formation)
└─ Dreamer (Memory Consolidation)
```

### Workflow Automation
```
n8n Platform
├─ Webhook Integration (Email, OP Events)
├─ HTTP Request Nodes (API Calls)
├─ Function Nodes (Data Processing)
└─ Workflow Scheduling (Timer-based)
```

## Security & Authentication Dependencies

```
JWT Authentication
├─ security.py (Token Generation)
├─ keys.py (Scoped JWT Creation)
└─ routers/ (Token Validation)

Workspace Isolation
├─ Composite Foreign Keys (Multi-Tenancy)
└─ Peer Observation Rules (Access Control)

API Security
├─ CORS Middleware (Cross-Origin Control)
├─ Request Validation (Pydantic Models)
└─ Error Handling (Custom Exceptions)
```

## Configuration Dependencies

```
Hierarchical Configuration
.env (Environment Variables)
  ↓
config.toml (Workspace Settings)
  ↓
settings.py (Default Values)
  ↓
Individual Module Configs
```

---
Generated: 2026-06-17
Dependency Graph: 50+ modules with clear separation of concerns
