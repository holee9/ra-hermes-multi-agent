# RA Hermes Multi-Agent Architecture Overview

## System Purpose

RA Hermes is a learning multi-agent system for medical device regulatory affairs (RA) automation. It provides AI-powered assistance to human RA experts, prioritizing accuracy and reliability over speed.

## Design Philosophy

**정확성·신뢰성 우선, 사람 보조 집중** — This system handles medical device regulatory affairs where incorrect judgments impact patient safety.

- Accuracy always takes priority over speed
- Agents assist human RA experts, not replace them
- Human decision authority remains final
- Uncertain cases escalate to human review
- Human-in-the-loop is by design, not a weakness

## System Architecture

```
Business Workspace                    Infrastructure Workspace
├─ RA Agents (ra_us, ra_eu, ra_kr)      ├─ infra_t3610 (Honcho server)
├─ op_manager                          ├─ infra_gx10 (LLM inference)
└─ n8n_manager                         └─ infra_rpi (OpenProject + n8n)
       │                                          │
   [n8n workflows]                       [bridge]─────┘
       │
   [Honcho T3610] ──→ [GX10 Qwen3]
       │
   [OpenProject]
       │
   [Virtual Office] (read-only observer)
```

## Hardware Components

| Machine | Spec | Role |
|---------|------|------|
| T3610 | Xeon 12C/24T, 32GB, Linux | Honcho server (FastAPI + PostgreSQL/pgvector + Redis) + RA experts |
| GX10 | Grace Blackwell ARM, Qwen3 | LLM inference backend (tool-calling required) |
| Raspberry Pi 5+ | 16GB | OpenProject + n8n workflows |

## Core Technologies

- **Honcho**: FastAPI-based memory and social cognition layer (v0.15.1)
- **n8n**: Workflow automation for email triage and routing
- **OpenProject**: Work package management system
- **PostgreSQL/pgvector**: Vector database for knowledge and memories
- **Redis**: Cache layer for Honcho
- **Hermes Agents**: RA expert personas with learning capabilities

## Key Modules

### Business Workspace (ra-hermes-multi-agent)

#### Honcho Server (`honcho-src/`)
- **Purpose**: Infrastructure layer for AI agents with memory and social cognition
- **Technology**: FastAPI, SQLAlchemy 2.0, Pydantic v2
- **Entry Point**: `src/main.py`
- **Key Components**:
  - Dialectic Agent: Chat endpoint with personal context injection
  - Deriver: Background memory formation processor
  - Dreamer: Memory consolidation and self-improvement
  - Vector Store: pgvector-based knowledge management
  - Telemetry: Prometheus metrics + CloudEvents

#### RA Agent Profiles (`profiles/`)
- **ra_us**: US regulatory affairs expert
- **ra_eu**: EU regulatory affairs expert  
- **ra_kr**: Korea regulatory affairs expert
- **Structure**: Each profile contains SOUL.md persona definition and configuration

#### Python Scripts (`scripts/`)
- **Growth Automation**: `autonomous-study-scheduler.py`, `daily-growth-runner.py`
- **Knowledge Management**: `index_ra_knowledge.py`, `curriculum-seed.py`
- **Metrics & Reporting**: `growth-metrics.py`, `auto-growth-readiness-report.py`
- **Data Integration**: `extract_mail_qa.py`, `op_honcho_backfill.py`

#### n8n Workflows (`n8n/workflows/`)
- **mail-triage.json**: Email classification and routing
- **feedback-recorder.json**: Human feedback capture
- **wp-close-recorder.json**: Work package closure automation
- **infra-vote-broadcast.json**: Infrastructure consensus voting
- **infra-to-work-bridge.json**: Infrastructure-to-business communication

#### Integration Components
- **bridge/**: Infrastructure-to-business communication layer
- **voting/**: Vote-based consensus for infrastructure decisions
- **virtual-office/**: HTML-based read-only visualization

### External Dependencies

- **OpenProject API**: Work package and project management
- **Layer 4 APIs**: Real-time regulatory knowledge (law.go.kr, openFDA, data.go.kr)
- **GX10 Inference**: Remote LLM endpoint via OpenAI-compatible API
- **pgvector**: Vector similarity search for knowledge retrieval

## Data Flow Patterns

1. **Email Processing**: Email → n8n mail-triage → RA agents → OpenProject
2. **Memory Formation**: Interactions → Honcho deriver → pgvector → Dialectic recall
3. **Growth Loop**: Performance → growth-metrics → autonomous-study-scheduler → improved competence
4. **Infrastructure Consensus**: Infra decisions → voting system → broadcast to business workspace

## Architecture Patterns

- **Peer Paradigm**: Humans and AI agents unified as "Peers" in Honcho
- **Multi-Process**: API server + deriver worker + Dreamer specialist system
- **Event-Driven**: n8n workflows triggered by emails and webhooks
- **Vector Search**: pgvector HNSW indexes for semantic knowledge retrieval
- **Provider Agnostic**: LLM abstraction layer supporting multiple providers

## Safety & Quality

- **Yellow Gate**: Low-confidence decisions route to human review
- **State Verification**: Existing work package status validation before routing
- **Graceful Degradation**: Layer 4 API failures don't crash core operations
- **Immutable Data Contracts**: Fixed JSON schemas for RA analysis results
- **Human Supervision**: Final authority on all regulatory decisions

## Scalability Considerations

- **Horizontal Scaling**: Multiple deriver workers for memory processing
- **Caching**: Redis layer for frequently accessed peer representations
- **Batch Processing**: Up to 100 messages per batch in deriver
- **Connection Pooling**: PostgreSQL connection pool management
- **Async I/O**: Non-blocking operations for external API calls

---
Generated: 2026-06-17
System Status: MVP deployed, growth loop implemented, safety/QA hardening complete
