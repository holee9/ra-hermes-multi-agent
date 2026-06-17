---
id: SPEC-ARCH-001
version: 1.0.0
status: Planned
created: 2025-01-21
updated: 2025-01-21
author: MoAI Orchestrator
priority: High
issue_number: TBD
---

# SPEC-ARCH-001: RA Hermes Multi-Agent Architecture Improvement

## HISTORY

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2025-01-21 | Initial SPEC creation | MoAI Orchestrator |

## 1. PURPOSE

This SPEC defines architectural improvements for the RA Hermes Multi-Agent system to enhance system integration, error handling, observability, growth loop stability, and documentation consolidation while maintaining the core philosophy: **"정확성·신뢰성 우선, 사람 보조 집중"** (Accuracy and reliability first, human-assisted focus).

## 2. ENVIRONMENT

### 2.1 Current System State

**Completed Milestones:**
- MVP deployed with growth loop implemented
- Safety/QA hardening complete
- Honcho v0.15.1 operational on T3610
- 3 RA agent profiles (ra_us, ra_eu, ra_kr) configured
- n8n workflows deployed on Raspberry Pi
- Layer 4 APIs integrated (openFDA, law.go.kr, data.go.kr)

**System Components:**
- 30+ modules across servers, scripts, workflows, and APIs
- Business Workspace: RA agents, op_manager, n8n_manager
- Infrastructure Workspace: infra_t3610, infra_gx10, infra_rpi
- Core Technologies: Honcho (FastAPI + pgvector + Redis), n8n, OpenProject, GX10 Qwen3

### 2.2 Assumptions

1. **Hardware Stability**: T3610, GX10, and Raspberry Pi maintain current network connectivity and service availability
2. **Hermes v0.15.1 Stability**: Current Hermes Agent version remains stable through implementation
3. **Knowledge Base Continuity**: ra_knowledge pgvector index remains accessible and properly maintained
4. **OpenProject API**: OpenProject API continues to provide work package management functionality
5. **Human Availability**: RA domain experts available for validation and feedback during implementation

## 3. REQUIREMENTS (EARS Format)

### 3.1 Module Integration Requirements

**REQ-ARCH-001: Integration Contract Standardization**
- The system SHALL define explicit integration contracts between Honcho server, RA agents, and n8n workflows
- WHEN a module boundary is crossed, the system SHALL validate data contracts before processing
- WHILE multiple modules interact, the system SHALL maintain transaction boundaries for rollback capability

**REQ-ARCH-002: Event-Driven Communication**
- WHEN Honcho records activity events, the system SHALL broadcast to virtual office via standardized activity log format
- WHEN n8n workflows complete triage, the system SHALL emit structured events to Honcho memory
- THE system SHALL maintain event ordering guarantees across all module communications

**REQ-ARCH-003: Peer ID Consistency**
- THE system SHALL enforce underscore peer_id format (ra_us, ra_eu, ra_kr) for all Honcho operations
- WHEN profile operations occur, the system SHALL separate profile_id (hyphen) from peer_id (underscore)
- IF a hyphenated peer_id is detected, the system SHALL reject the operation during preflight validation

### 3.2 Error Handling Requirements

**REQ-ARCH-004: Standardized Error Classification**
- THE system SHALL classify errors into: transient (retryable), permanent (human intervention), and degraded (fallback mode)
- WHEN a transient error occurs, the system SHALL retry with exponential backoff (max 3 attempts)
- WHEN a permanent error occurs, the system SHALL escalate to human review with diagnostic context

**REQ-ARCH-005: Error Recovery Patterns**
- WHEN Honcho API communication fails, the system SHALL attempt graceful degradation to cached responses
- WHEN OpenProject lookup fails, the system SHALL route to Yellow gate with explicit failure reason
- WHEN GX10 inference is unavailable, the system SHALL queue requests and notify operator

**REQ-ARCH-006: Error Observation**
- THE system SHALL log all error events with structured context (timestamp, module, error code, correlation ID)
- WHEN error rate exceeds threshold (10% of operations), the system SHALL trigger alert to operator
- THE system SHALL maintain error history for trend analysis over 30-day window

### 3.3 Observability Requirements

**REQ-ARCH-007: Distributed Tracing**
- WHEN a mail triage request is processed, the system SHALL maintain trace context across n8n → Honcho → OpenProject
- THE system SHALL expose trace IDs via response headers for cross-service correlation
- THE system SHALL support trace sampling (100% for critical paths, 10% for background tasks)

**REQ-ARCH-008: Metrics Collection**
- THE system SHALL collect metrics for: operation latency, error rates, queue depth, memory usage, and inference utilization
- WHEN metric thresholds are breached, the system SHALL generate alerts with affected component context
- THE system SHALL aggregate metrics at 1-minute resolution with 24-hour retention

**REQ-ARCH-009: Logging Standardization**
- THE system SHALL log in structured JSON format with consistent fields: timestamp, level, module, peer_id, event_type, context
- WHEN debugging mode is active, the system SHALL log LLM prompts/responses with sanitization
- THE system SHALL implement log rotation with 7-day retention for debug logs, 90-day for operational logs

### 3.4 Growth Loop Stability Requirements

**REQ-ARCH-010: Learning Loop Safety**
- WHEN autonomous study scheduler executes, the system SHALL verify peer_id format before any Honcho writes
- WHEN bootstrap process runs, the system SHALL validate source-hash idempotence before processing
- WHEN daily growth executes, the system SHALL default to dry-run mode until explicit human approval

**REQ-ARCH-011: Threshold Policy Enforcement**
- THE system SHALL require 30 days of valid metrics before auto-activation of growth timers
- WHEN threshold values are null, the system SHALL operate in conservative mode (escalate to human)
- IF threshold policies are modified, the system SHALL require audit log entry with rationale

**REQ-ARCH-012: Memory Integrity**
- THE system SHALL prevent wrong-peer data pollution through strict peer_id validation
- WHEN replay operations occur for recovery, the system SHALL use only clean text content, not raw JSON envelopes
- IF wrong-peer records are detected, the system SHALL quarantine without automatic data migration

### 3.5 Documentation Requirements

**REQ-ARCH-013: Codemap Integration**
- THE system SHALL maintain codemap files synchronized with actual codebase structure
- WHEN new modules are added, the system SHALL update corresponding codemap documentation
- THE system SHALL validate codemap accuracy via automated checks on each deployment

**REQ-ARCH-014: Operational Documentation**
- THE system SHALL maintain operation procedures for all critical workflows (mail triage, feedback capture, WP closure)
- WHEN procedures are modified, the system SHALL require human validation before deployment
- THE system shall document all emergency procedures with decision trees for operator reference

**REQ-ARCH-015: API Documentation**
- THE system SHALL maintain OpenAPI specifications for all Honcho endpoints
- WHEN API contracts change, the system SHALL update documentation and notify dependent services
- THE system SHALL provide example requests/responses for all API operations

## 4. SPECIFICATIONS

### 4.1 Module Integration Patterns

**Integration Contract Schema:**
```yaml
contract:
  provider: string
  consumer: string
  data_schema: json_schema
  error_handling: retry_policy | escalate | fallback
  timeout_ms: integer
  retry_policy:
    max_attempts: integer
    backoff_ms: integer
  monitoring:
    trace: boolean
    metrics: boolean
```

**Activity Log Format (Fixed Contract):**
```json
{
  "ts": "ISO8601",
  "type": "mail_received|matched|comment_added|...",
  "actor": "<actor_id>",
  "payload": {...}
}
```

Valid Actor IDs: `ra_us`, `ra_eu`, `ra_kr`, `op_manager`, `n8n_manager`, `infra_*`, `human`, `system`

### 4.2 Error Handling Framework

**Error Classification Matrix:**

| Error Type | Classification | Recovery Strategy | Human Notification |
|------------|----------------|-------------------|-------------------|
| Network timeout | Transient | Retry with backoff | No (auto-recover) |
| Invalid peer_id | Permanent | Reject operation | Yes (validation error) |
| OpenProject API down | Degraded | Queue + alert | Yes (service degraded) |
| GX10 unavailable | Degraded | Queue + fallback | Yes (LLM down) |
| Confidence < threshold | Permanent | Yellow gate | Yes (low confidence) |

### 4.3 Monitoring Thresholds

**Operational Thresholds (Default Conservative):**

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Error rate | 5% | 10% | Alert operator |
| Queue depth | 100 | 500 | Scale notification |
| Latency P95 | 2s | 5s | Performance alert |
| Memory usage | 80% | 90% | Resource warning |
| Inference failures | 1% | 5% | LLM service alert |

### 4.4 Growth Loop Operational Policies

**Bootstrap Safety Requirements:**
- Verify scheduler config separates `profile_id` and `peer_id`
- Confirm all Honcho writes use underscore `peer_id` values
- Run `python3 scripts/verify-study-scheduler.py` after scheduler changes
- Execute bootstrap `--dry-run` with `STUDY_BOOTSTRAP_MAX=1` before real restart

**Daily Growth Requirements:**
- Default to dry-run while manual growth/backlog active
- Require explicit manual-completion gate before `--execute`
- Write `daily_growth_case` content as clean memory-derivable text, not JSON
- Avoid overly broad routing keywords that select administrative sources

## 5. EXCLUSIONS (What NOT to Build)

The following items are explicitly OUT OF SCOPE for this SPEC:

1. **New Feature Development**: This SPEC focuses on architectural improvements to existing functionality, not new features like additional RA regions or new workflow types

2. **Hermes Core Modifications**: Changes to Hermes Agent core functionality (memory, sessions, skills) are outside scope - these are managed by upstream Hermes project

3. **Database Migration**: Major database schema migrations or data model changes are not included - these require separate SPEC with detailed migration planning

4. **Performance Optimization**: While performance monitoring is included, active optimization work (query tuning, caching strategies) is deferred to a performance-focused SPEC

5. **UI/UX Changes**: Virtual office visualization improvements and user interface enhancements are not part of this architectural SPEC

6. **Hardware Scaling**: New hardware deployment, scaling strategies, or infrastructure provisioning are excluded - these belong to infrastructure-focused SPECs

7. **Regulatory Content Updates**: Changes to RA knowledge base content, regulation interpretations, or compliance requirements are operational activities, not architectural changes

8. **Third-Party Integrations**: New external service integrations beyond currently defined Layer 4 APIs are excluded

## 6. ACCEPTANCE CRITERIA SUMMARY

Each requirement includes detailed acceptance criteria in `acceptance.md`. Success is measured by:

- All EARS requirements implementable with test scenarios
- Integration contracts defined and validated
- Error handling patterns consistent across all modules
- Observability stack collecting required metrics
- Growth loop safety mechanisms operational
- Documentation synchronized with codebase changes

## 7. REFERENCES

- `.moai/project/codemaps/overview.md` - System architecture overview
- `.moai/project/codemaps/modules.md` - Module catalog
- `.moai/project/codemaps/dependencies.md` - Dependency mapping
- `.moai/project/status.md` - Current operational status
- `docs/RA-multi-agent-master-design.md` - Master design document
- `docs/implementation-spec.md` - Implementation specifications
- `docs/operations-guide.md` - Operational procedures
- `.claude/rules/autonomous-study-bootstrap-safety.md` - Bootstrap safety rules
