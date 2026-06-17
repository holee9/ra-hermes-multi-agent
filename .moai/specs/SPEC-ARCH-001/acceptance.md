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

# SPEC-ARCH-001: Acceptance Criteria

## 1. ACCEPTANCE CRITERIA OVERVIEW

Each requirement from `spec.md` has corresponding acceptance criteria defined using Given-When-Then format. These criteria provide observable evidence of successful implementation.

## 2. MODULE INTEGRATION ACCEPTANCE CRITERIA

### AC-ARCH-001: Integration Contract Standardization

**Scenario 1: Contract Validation on Module Boundary**
```
GIVEN a module integration contract is defined for Honcho to n8n communication
WHEN n8n sends data to Honcho API
THEN the system SHALL validate the data against the contract schema
AND reject invalid data with specific error message
AND log the validation failure with contract reference
```

**Scenario 2: Transaction Boundary Maintenance**
```
GIVEN a multi-module operation involving n8n → Honcho → OpenProject
WHEN any step in the transaction fails
THEN the system SHALL rollback all completed steps
AND maintain system state consistency
AND notify operator of rollback with affected component context
```

**Scenario 3: Contract Schema Definition**
```
GIVEN the need to define integration contracts
WHEN creating contract schemas
THEN each schema SHALL include: provider, consumer, data_schema, error_handling, timeout, retry_policy, monitoring
AND schemas SHALL be stored in YAML format in `.moai/config/integration-contracts/`
AND contracts SHALL be version-controlled with change history
```

### AC-ARCH-002: Event-Driven Communication

**Scenario 1: Activity Log Broadcasting**
```
GIVEN Honcho records an activity event
WHEN the event is created
THEN the system SHALL broadcast the event in standardized activity log format
AND include required fields: ts (ISO8601), type, actor, payload
AND validate actor_id against allowed values (ra_us, ra_eu, ra_kr, op_manager, n8n_manager, infra_*, human, system)
```

**Scenario 2: Event Ordering**
```
GIVEN multiple events occurring in sequence
WHEN events are broadcast across modules
THEN the system SHALL maintain event ordering guarantees
AND process events in timestamp order
AND preserve causal relationships between events
```

**Scenario 3: Triage Event Emission**
```
GIVEN n8n mail-triage workflow completes processing
WHEN triage result is determined
THEN the system SHALL emit a structured event to Honcho memory
AND include triage metadata: actor, confidence, region, match, wp, transition_proposed
AND validate event format before transmission
```

### AC-ARCH-003: Peer ID Consistency

**Scenario 1: Peer ID Format Validation**
```
GIVEN a Honcho write operation is attempted
WHEN the operation includes a peer_id parameter
THEN the system SHALL validate the peer_id uses underscore format (ra_us, ra_eu, ra_kr)
AND reject hyphenated formats (ra-us, ra-eu, ra-kr) during preflight validation
AND return specific error message: "Invalid peer_id format: must use underscore (ra_us) not hyphen (ra-us)"
```

**Scenario 2: Profile ID Separation**
```
GIVEN profile operations are executed
WHEN profile_id and peer_id are both required
THEN the system SHALL maintain separate formats: profile_id (hyphen) for SOUL loading, peer_id (underscore) for Honcho operations
AND translate between formats when necessary
AND log format translations for audit purposes
```

**Scenario 3: Validation Script Execution**
```
GIVEN changes to autonomous-study-scheduler.py
WHEN the scheduler is modified
THEN the system SHALL execute `python3 scripts/verify-study-scheduler.py`
AND require the script to pass before committing changes
AND fail validation if peer_id inconsistencies are detected
```

## 3. ERROR HANDLING ACCEPTANCE CRITERIA

### AC-ARCH-004: Standardized Error Classification

**Scenario 1: Transient Error Classification**
```
GIVEN an operation encounters a network timeout error
WHEN the error is classified
THEN the system SHALL classify as transient (retryable)
AND initiate retry with exponential backoff
AND limit retries to maximum 3 attempts
AND log retry attempts with attempt number and backoff duration
```

**Scenario 2: Permanent Error Classification**
```
GIVEN an operation encounters an invalid peer_id error
WHEN the error is classified
THEN the system SHALL classify as permanent (requires human intervention)
AND escalate to human review with diagnostic context
AND include error classification and recommended action in notification
AND prevent automatic retry attempts
```

**Scenario 3: Degraded Mode Classification**
```
GIVEN GX10 inference service becomes unavailable
WHEN the error is classified
THEN the system SHALL classify as degraded (fallback mode available)
AND activate fallback behavior (queue requests, notify operator)
AND maintain system operation with reduced functionality
AND monitor service availability for recovery
```

### AC-ARCH-005: Error Recovery Patterns

**Scenario 1: Honcho API Communication Failure**
```
GIVEN Honcho API communication fails
WHEN the failure is detected
THEN the system SHALL attempt graceful degradation to cached responses
AND return cached data if available and within TTL
AND notify operator of cache usage with original error context
AND queue retry when API becomes available
```

**Scenario 2: OpenProject Lookup Failure**
```
GIVEN OpenProject API lookup fails during WP matching
WHEN the failure is detected
THEN the system SHALL route to Yellow gate (human review)
AND include explicit failure reason in notification
AND log lookup failure with WP reference
AND prevent automatic WP creation without human confirmation
```

**Scenario 3: GX10 Inference Unavailability**
```
GIVEN GX10 inference endpoint is unavailable
WHEN the unavailability is detected
THEN the system SHALL queue inference requests
AND notify operator of LLM service down status
AND monitor queue depth for backlog
AND process queued requests when service recovers
```

### AC-ARCH-006: Error Observation

**Scenario 1: Structured Error Logging**
```
GIVEN an error event occurs
WHEN the error is logged
THEN the system SHALL log in structured JSON format
AND include required fields: timestamp, level, module, error_code, correlation_id, context
AND ensure error_code is consistent across modules for same error type
AND include correlation_id for cross-service traceability
```

**Scenario 2: Error Rate Alerting**
```
GIVEN error monitoring is active
WHEN error rate exceeds 10% of operations
THEN the system SHALL generate alert to operator
AND include affected component context in alert
AND provide error breakdown by type and module
AND recommend investigation actions based on error patterns
```

**Scenario 3: Error History Maintenance**
```
GIVEN errors are being logged
WHEN error history is queried
THEN the system SHALL maintain error history for 30-day window
AND provide trend analysis for error rates by type
AND identify recurring error patterns
AND support filtering by module, error type, time range
```

## 4. OBSERVABILITY ACCEPTANCE CRITERIA

### AC-ARCH-007: Distributed Tracing

**Scenario 1: Mail Triage Trace Context**
```
GIVEN a mail triage request is received
WHEN the request is processed through n8n → Honcho → OpenProject
THEN the system SHALL maintain trace context across all services
AND propagate correlation ID via headers/logs
AND ensure trace completeness from receipt to recording
AND expose trace ID in response headers
```

**Scenario 2: Trace Sampling**
```
GIVEN tracing is enabled for operations
WHEN determining trace sampling rate
THEN the system SHALL apply 100% sampling for critical paths (mail triage, feedback capture)
AND apply 10% sampling for background tasks (metrics collection, cleanup)
AND adjust sampling rates based on system load
AND log sampling rate decisions for audit
```

**Scenario 3: Cross-Service Correlation**
```
GIVEN multiple services are involved in an operation
WHEN correlating events across services
THEN the system SHALL use correlation ID to link events
AND provide unified trace view across Honcho, n8n, OpenProject
AND support trace query by correlation ID
AND include trace context in all error notifications
```

### AC-ARCH-008: Metrics Collection

**Scenario 1: Required Metrics Collection**
```
GIVEN the system is operational
WHEN metrics are collected
THEN the system SHALL collect metrics for: operation latency, error rates, queue depth, memory usage, inference utilization
AND aggregate metrics at 1-minute resolution
AND retain metrics for 24-hour window
AND support metric query by time range and component
```

**Scenario 2: Threshold Breach Alerting**
```
GIVEN metric thresholds are defined
WHEN a threshold is breached
THEN the system SHALL generate alert with affected component
AND include current value, threshold, and breach duration
AND provide historical context for the metric
AND recommend actions based on severity level
```

**Scenario 3: Metric Aggregation**
```
GIVEN raw metrics are being collected
WHEN metrics are aggregated
THEN the system SHALL calculate P50, P95, P99 percentiles for latency metrics
AND calculate error rates by error type
AND aggregate queue depth by service
AND support time-series analysis for trend detection
```

### AC-ARCH-009: Logging Standardization

**Scenario 1: Structured JSON Logging**
```
GIVEN a log event is generated
WHEN the log is written
THEN the system SHALL log in structured JSON format
AND include required fields: timestamp, level, module, peer_id, event_type, context
AND ensure consistent field naming across all modules
AND validate JSON schema before writing
```

**Scenario 2: Debug Mode Logging**
```
GIVEN debug mode is active
WHEN LLM prompts/responses occur
THEN the system SHALL log full prompts and responses with sanitization
AND sanitize sensitive information (API keys, personal data)
AND include model name, token count, and timing information
AND disable debug logging by default with explicit activation required
```

**Scenario 3: Log Rotation**
```
GIVEN logs are being written
WHEN log rotation occurs
THEN the system SHALL implement 7-day retention for debug logs
AND implement 90-day retention for operational logs
AND compress archived logs to save disk space
AND maintain log index for efficient querying
```

## 5. GROWTH LOOP STABILITY ACCEPTANCE CRITERIA

### AC-ARCH-010: Learning Loop Safety

**Scenario 1: Peer ID Validation in Scheduler**
```
GIVEN autonomous study scheduler executes
WHEN scheduler performs Honcho write operations
THEN the system SHALL verify peer_id format before writes
AND validate all peer_id values use underscore format
AND reject operations with invalid peer_id formats
AND log validation failures with scheduler context
```

**Scenario 2: Bootstrap Source Validation**
```
GIVEN bootstrap process is running
WHEN processing curriculum sources
THEN the system SHALL validate source-hash idempotence
AND skip already-processed sources based on hash
AND log idempotence validation results
AND prevent duplicate processing of same source
```

**Scenario 3: Daily Growth Dry-Run Default**
```
GIVEN daily growth runner is executed
WHEN explicit --execute flag is not provided
THEN the system SHALL default to dry-run mode
AND simulate all operations without Honcho writes
AND report what would be executed
AND require explicit --execute flag for real execution
```

### AC-ARCH-011: Threshold Policy Enforcement

**Scenario 1: 30-Day Validation Window**
```
GIVEN auto-activation of growth timers is requested
WHEN less than 30 days of valid metrics exist
THEN the system SHALL deny auto-activation
AND require manual approval for activation
AND report current valid metrics days (days/30)
AND log denial reason with policy reference
```

**Scenario 2: Null Threshold Policy**
```
GIVEN threshold values are null
WHEN growth operations require threshold comparison
THEN the system SHALL operate in conservative mode
AND escalate all decisions to human review
AND prevent automatic progression based on undefined thresholds
AND log conservative mode activation with null field reference
```

**Scenario 3: Policy Change Audit**
```
GIVEN threshold policies are modified
WHEN a policy change is committed
THEN the system SHALL require audit log entry
AND include: timestamp, changed field, old value, new value, rationale, operator
AND maintain policy change history
AND support policy rollback to previous version
```

### AC-ARCH-012: Memory Integrity

**Scenario 1: Wrong-Peer Detection**
```
GIVEN Honcho operations are executing
WHEN wrong-peer records are detected
THEN the system SHALL quarantine affected records
AND prevent automatic data migration
AND notify operator of quarantine with record count
AND maintain quarantine metadata for audit
```

**Scenario 2: Clean Text Replay**
```
GIVEN recovery operations are required
WHEN replaying study insights
THEN the system SHALL use only clean text content
AND avoid raw JSON envelope replay
AND reconstruct structured metadata from clean text
AND validate replay data format before Honcho writes
```

**Scenario 3: Integrity Validation**
```
GIVEN memory integrity checks are performed
WHEN validating peer assignments
THEN the system SHALL verify all messages use correct peer_id
AND verify all documents reference correct observer/observed peers
AND validate queue entries reference correct peer_id
AND report any integrity violations with detailed context
```

## 6. DOCUMENTATION ACCEPTANCE CRITERIA

### AC-ARCH-013: Codemap Integration

**Scenario 1: Codemap Synchronization**
```
GIVEN new modules are added to codebase
WHEN codemap generation runs
THEN the system SHALL update corresponding codemap documentation
AND validate codemap accuracy against actual file structure
AND report discrepancies between codemap and code
AND require manual review for structural changes
```

**Scenario 2: Automated Codemap Validation**
```
GIVEN codemap files exist
WHEN deployment is executed
THEN the system SHALL validate codemap accuracy
AND compare codemap entries against actual files
AND fail deployment if significant discrepancies exist
AND report validation results in deployment logs
```

### AC-ARCH-014: Operational Documentation

**Scenario 1: Procedure Documentation**
```
GIVEN a critical workflow is operational
WHEN operational documentation is reviewed
THEN the system SHALL document procedure with step-by-step instructions
AND include decision trees for error scenarios
AND provide example commands and expected outputs
AND validate documentation against actual workflow execution
```

**Scenario 2: Documentation Modification Validation**
```
GIVEN operational procedures are modified
WHEN procedures are deployed
THEN the system SHALL require human validation before deployment
AND document modification rationale and approval
AND maintain procedure version history
AND support procedure rollback to previous version
```

### AC-ARCH-015: API Documentation

**Scenario 1: OpenAPI Specification Generation**
```
GIVEN Honcho API endpoints are modified
WHEN API documentation is generated
THEN the system SHALL generate OpenAPI specifications from code annotations
AND include all endpoints with request/response schemas
AND provide example requests and responses
AND validate specification against actual API behavior
```

**Scenario 2: API Change Notification**
```
GIVEN API contracts are changed
WHEN changes are deployed
THEN the system SHALL update API documentation
AND notify dependent services of changes
AND document breaking changes with migration guide
AND maintain API version history
```

## 7. QUALITY GATE CRITERIA

### General Quality Gates

**G1: Implementation Completeness**
- All EARS requirements from spec.md have corresponding implementation
- All acceptance criteria have passing test scenarios
- No requirements marked as TBD or deferred without explicit rationale

**G2: Testing Coverage**
- Unit test coverage >= 85% for new modules
- Integration tests cover all critical paths
- Validation tests cover all error scenarios

**G3: Documentation Completeness**
- All new modules have documentation
- All API changes are reflected in OpenAPI specs
- All operational procedures are documented

**G4: Safety Validation**
- All peer_id validations passing
- All error recovery mechanisms tested
- All growth loop safety measures operational

**G5: Observability Validation**
- All required metrics collected and visible
- All critical paths have trace coverage
- All modules emit structured logs

## 8. EDGE CASES AND EXCEPTIONS

### Edge Case 1: Concurrent Module Updates
```
GIVEN multiple modules are updated simultaneously
WHEN integration contracts are affected
THEN the system SHALL validate all affected contracts
AND prevent deployment if contract validation fails
AND require sequential deployment with verification between updates
```

### Edge Case 2: Burst Error Conditions
```
GIVEN burst error conditions occur (>100 errors/minute)
WHEN error rate monitoring is active
THEN the system SHALL trigger immediate alert
AND implement rate limiting for error notifications
AND maintain error history for post-incident analysis
```

### Edge Case 3: Long-Running Operations
```
GIVEN long-running operations are executing (>5 minutes)
WHEN operation monitoring is active
THEN the system SHALL provide progress updates
AND maintain operation context across service restarts
AND support operation cancellation with cleanup
```

### Edge Case 4: Missing Configuration
```
GIVEN required configuration is missing
WHEN system initialization occurs
THEN the system SHALL fail fast with specific error message
AND identify missing configuration parameters
AND provide configuration examples in error message
AND prevent operation with incomplete configuration
```

### Edge Case 5: External Service Degradation
```
GIVEN multiple external services are degraded simultaneously
WHEN degradation is detected
THEN the system SHALL prioritize critical operations
AND implement graceful degradation for non-critical operations
AND notify operator of degraded services and impact
AND maintain core functionality despite service issues
```
