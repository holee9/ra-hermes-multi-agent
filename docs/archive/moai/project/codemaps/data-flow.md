# RA Hermes Multi-Agent - Data Flow & Contracts

## Sequence Diagram: Mail Triage Flow

```mermaid
sequenceDiagram
    participant Gmail as Gmail IMAP
    participant n8n as n8n mail-triage
    participant Hermes as Hermes API :8643
    participant Qdrant as Qdrant :6333
    participant NAS as NAS RAG
    participant GX10 as GX10 Qwen3
    participant Honcho as Honcho :8000
    participant OP as OpenProject
    participant VO as Virtual Office

    Gmail->>n8n: New unread email (poll every minute)
    n8n->>n8n: Parse body, extract original subject/from
    n8n->>n8n: Detect regulatory region (US/EU/KR keywords)
    n8n->>n8n: Route to green (single region) or yellow (multi/no region)
    
    alt Green route (single region)
        n8n->>Hermes: POST /v1/chat/completions<br/>{model: ra_us, messages, subject}
        Hermes->>Qdrant: Layer 1 RAG search (subject-based query)
        Qdrant-->>NAS: Qdrant queries NAS docs
        NAS-->>Qdrant: Returns top 5 relevant chunks
        Qdrant-->>Hermes: RAG results (source_file, score, text)
        
        Hermes->>Hermes: Layer 4 knowledge fetch (llm-wiki, openFDA, law.go.kr)
        Hermes->>GX10: Invoke hermes binary with context<br/>hermes -p ra-us -z <context> --skills ra-expert
        GX10-->>Hermes: RA classification result
        
        alt Result parse successful
            Hermes-->>n8n: {wp_comment: {wp_title, summary, recommendation, confidence, matched_wp_id, ...}}
        else Error/timeout
            Hermes-->>n8n: Error fallback JSON (low confidence, hermes_failed flag)
        end
        
        n8n->>n8n: Parse wp_comment, validate confidence
        n8n->>n8n: Check YELLOW_CONFIDENCE_THRESHOLD (default 0.75)
        
        alt Confidence >= threshold (Green gate pass)
            n8n->>Honcho: POST activity_log<br/>{type: matched, actor: ra_us, payload: {wp, confidence, existing}}
            n8n->>OP: POST comment to OpenProject WP
            Honcho->>VO: Activity log broadcast (SSE)
            VO-->>Human: Real-time pixel-art update
        else Confidence < threshold (Yellow gate fail)
            n8n->>Honcho: POST activity_log<br/>{type: yellow_route, actor: system, payload: {reason: low_confidence}}
            n8n->>n8n: Route to human review queue
            Honcho->>VO: Yellow event logged
        end
        
        else Yellow route (multi-region or no region detected)
            n8n->>Honcho: POST activity_log<br/>{type: yellow_route, actor: system, payload: {reason: multi_region}}
            n8n->>n8n: Route to human review queue
        end
    end
```

## Sequence Diagram: Infra Vote → Bridge Flow

```mermaid
sequenceDiagram
    participant Infra as Infra Agents
    participant n8n as n8n infra-vote-broadcast
    participant Vote as vote-aggregator.js
    participant Rules as vote-rules.json
    participant n8n2 as n8n infra-to-work-bridge
    participant Bridge as bridge-config.json
    participant Honcho as Honcho :8000

    Infra->>n8n: Vote request (manual or scheduled)
    n8n->>Infra: Broadcast vote to all infra agents (infra_t3610, infra_gx10, infra_rpi)
    
    loop Collect votes (timeout 900s)
        Infra-->>n8n: Vote response {actor, vote: approve|reject|abstain, topic}
    end
    
    n8n->>Vote: aggregate(votes)
    Vote->>Rules: Load rules (quorum, weights, majority_threshold)
    Rules-->>Vote: Return config values
    
    alt Quorum met (>= 2 of 3)
        Vote->>Vote: Calculate weighted tally (if weights configured)
        Vote->>Vote: Compute approve_ratio = weighted_approve / (weighted_approve + weighted_reject)
        Vote->>Vote: Compare against majority_threshold (0.66 = 2/3)
        
        alt Approve ratio >= threshold
            Vote-->>n8n: {result: approved, method: threshold_0.66, tally, approve_ratio}
        else Approve ratio < threshold
            Vote-->>n8n: {result: rejected, method: threshold_0.66, tally, approve_ratio}
        end
    else Quorum not met
        Vote-->>n8n: {result: pending, method: quorum_not_met, tally}
    end
    
    n8n->>n8n: Broadcast result to all infra agents
    n8n->>n8n2: Pass result to bridge workflow
    n8n2->>Bridge: Load relay conditions (relay_threshold, relay_conditions)
    
    alt Bridge conditions empty (initial state)
        Bridge-->>n8n2: Relay all decisions (no filtering)
        n8n2->>Honcho: POST activity_log<br/>{type: infra_decision, actor: system, payload: {result, topic}}
    else Bridge conditions configured
        n8n2->>n8n2: Check relay_threshold and relay_conditions
        alt Decision matches relay conditions
            n8n2->>Honcho: POST activity_log (relay to work workspace)
        else Decision doesn't match
            n8n2->>n8n2: Drop decision (do not relay)
        end
    end
```

## Sequence Diagram: Autonomous Study/Growth Loop

```mermaid
sequenceDiagram
    participant Timer as systemd Timer
    participant Shell as Shell Script
    participant Study as autonomous-study-scheduler.py
    participant PG as PostgreSQL :5433
    participant Hermes as Hermes API :8643
    participant Honcho as Honcho :8000
    participant Daily as daily-growth-runner.py
    participant Metrics as growth-metrics.py
    participant Dashboard as render-growth-dashboard.py

    Timer->>Shell: Trigger (daily 02:00 or configured interval)
    Shell->>Study: python3 autonomous-study-scheduler.py --mode delta
    
    Study->>PG: SELECT chunks FROM ra_knowledge<br/>WHERE region = 'US' AND updated_at > last_checkpoint
    PG-->>Study: Return chunks (id, source_path, source_hash, content)
    
    loop For each batch (STUDY_BATCH_SIZE=5)
        Study->>Study: Build study prompt with chunk batch
        Study->>Hermes: POST /v1/chat/completions<br/>{model: ra_us, messages: [{role: user, content: study_prompt}]}
        Hermes->>Hermes: Invoke hermes -p ra-us -z <context> --skills ra-expert
        Hermes-->>Study: Extracted insights JSON
        
        alt Parse successful
            Study->>Study: Parse insights (learning points, gaps, recommendations)
            Study->>Honcho: POST message to study session<br/>{type: study_insight, peer: ra_us, content: insights}
            Honcho-->>Study: Message recorded (session_id, message_id)
        else Parse failed
            Study->>Study: Log error, continue to next batch
        end
        
        Study->>Study: Wait CALL_DELAY (1.0s) to avoid overloading GX10
    end
    
    Study->>Honcho: POST session_complete message<br/>{type: session_complete, peer: ra_us, stats: {chunks_studied, insights_generated}}
    Honcho-->>Study: Session complete
    
    par Peer exchange (cross-injection)
        Study->>Honcho: POST top insights from ra_us → ra_eu, ra_kr
        Study->>Honcho: POST top insights from ra_eu → ra_us, ra_kr
        Study->>Honcho: POST top insights from ra_kr → ra_us, ra_eu
    end
    
    Honcho->>Study: All peer exchanges complete
    Study->>Study: Update checkpoint (last_run_ts)
    Study-->>Shell: Bootstrap/delta complete
    
    Shell->>Daily: python3 daily-growth-runner.py --run --date today
    Daily->>PG: Query ra_knowledge for growth cases (non-email-dependent)
    Daily->>Hermes: Generate growth work via RA classification
    Daily->>Honcho: Record growth activity logs
    Daily-->>Shell: Growth cycle complete
    
    Shell->>Metrics: python3 growth-metrics.py --date today
    Metrics->>Honcho: Query sessions/messages for date window
    Metrics->>PG: Query study insights, growth activities
    Metrics->>Metrics: Calculate metrics<br/>(correction_rate, first_pass_match_accuracy, confidence_calibration, warmstart_lift)
    Metrics->>Metrics: Generate metrics JSON
    Metrics-->>Shell: Metrics calculated
    
    Shell->>Dashboard: python3 render-growth-dashboard.py
    Dashboard->>Dashboard: Load metrics JSON, render HTML template
    Dashboard->>Dashboard: Write docs/growth-dashboard.html
    Dashboard-->>Shell: Dashboard rendered
    
    Shell->>Timer: Report completion (logs to /var/log/ra-growth-metrics.log)
```

## Sequence Diagram: Knowledge Indexing Flow

```mermaid
sequenceDiagram
    participant Script as index_ra_knowledge.py
    participant Repo as llm-wiki/ra-project/MD-process
    participant PG as PostgreSQL :5433
    participant NAS as NAS Indexer
    participant Qdrant as Qdrant :6333

    Script->>Repo: Scan markdown files (git clone or local path)
    Repo-->>Script: Return file list
    
    loop For each markdown file
        Script->>Script: Read file, extract metadata
        Script->>Script: Chunk content (500-1000 chars with overlap)
        
        loop For each chunk
            Script->>Script: Generate embeddings (via Ollama Qwen3)
            Script->>PG: INSERT INTO ra_knowledge<br/>(source_path, chunk_hash, content, embedding, region, tags)
            PG-->>Script: Chunk stored
        end
    end
    
    Script-->>Script: Indexing complete (stats: files_processed, chunks_stored)
    
    Note over Repo,PG: [HARD] Read-only knowledge bases<br/>NEVER write to llm-wiki/ra-project/MD-process repos
    
    Script->>NAS: Scan NAS company documents
    NAS-->>Script: Return file list (PDF, DOCX, TXT)
    
    loop For each NAS document
        NAS->>NAS: Extract text (PDF parser, DOCX parser)
        NAS->>NAS: Chunk content (500 chars with overlap)
        
        loop For each chunk
            NAS->>NAS: Generate embeddings (Ollama)
            NAS->>Qdrant: INSERT point (collection: company_docs, vector, payload)
            Qdrant-->>NAS: Point stored
        end
    end
    
    NAS-->>NAS: NAS indexing complete
```

## Sequence Diagram: Human Feedback Loop

```mermaid
sequenceDiagram
    participant Human as Human RA Expert
    participant n8n as n8n feedback-recorder
    participant Honcho as Honcho :8000
    participant Trigger as growth-trigger-config.json
    participant Weight as weight-adjustment-config.json
    participant Study as autonomous-study-scheduler.py

    Human->>n8n: Submit feedback via webhook<br/>POST /webhook/feedback
    n8n->>n8n: Parse feedback {target, feedback_type, original_response, corrected_response, human_note}
    n8n->>Honcho: POST activity_log<br/>{type: human_feedback, actor: human, payload: {target, feedback_type, ...}}
    Honcho-->>n8n: Feedback recorded (session_id, message_id)
    
    alt Feedback type = correction
        Honcho->>Study: Trigger insights re-generation for affected chunks
        Study->>PG: Query chunks affected by correction
        Study->>Hermes: Re-classify with corrected context
        Study->>Honcho: Record corrected insights
        Honcho-->>Study: Correction applied
    end
    
    Honcho->>Trigger: Load growth-trigger thresholds
    Trigger->>Trigger: Check if feedback frequency exceeds thresholds
    
    alt Feedback frequency high (quality issues)
        Trigger-->>Honcho: Trigger growth intervention
        Honcho->>Weight: Load weight-adjustment rules
        Weight->>Weight: Reduce performance weight, increase quality weight
        Weight-->>Honcho: Adjusted weights returned
        Honcho->>Study: Notify weight adjustment for next cycle
        Study->>Study: Apply new weights in growth planning
    end
    
    Human->>Honcho: Query feedback history via API or UI
    Honcho-->>Human: Return feedback timeline + impact metrics
```

## Data Contracts

### RA Analysis Result JSON

**CLAUDE.md Declared Schema (FROZEN contract):**
```json
{
  "actor": "ra_us|ra_eu|ra_kr",
  "wp": "WP-123|null",
  "match": "existing|new",
  "confidence": 0.0-1.0,
  "region": "US|EU|KR",
  "comment": "Brief analysis comment",
  "transition_proposed": "리뷰중|null"
}
```

**ACTUAL Output from hermes-api-server.py parse_wp_comment():**
```json
{
  "wp_comment": {
    "email_type": "완료통보|액션필요|정보수신",
    "wp_title": "String (Korean)",
    "summary": "String (Korean)",
    "recommendation": "String (Korean)",
    "confidence": 0.9,
    "deadline": null|ISO8601-date,
    "product": "String|null",
    "org": "String|null",
    "matched_wp_id": 123|null,
    "source_docs": [
      {"file": "/path/to/doc.pdf", "score": 0.85, "excerpt": "..."},
      {"file": "/path/to/doc2.pdf", "score": 0.72, "excerpt": "..."}
    ],
    "market_analysis": {
      "mfds": "String|null",
      "ce_mdr": "String|null",
      "fda": "String|null"
    },
    "flags": ["flag1", "flag2"]
  }
}
```

> **⚠️ DRIFT WARNING:** The actual output is a **nested structure** with `wp_comment` wrapper. The n8n workflow (`mail-triage.json`) handles **both formats**:
> 1. Hermes format (nested with `wp_comment`)
> 2. Flat format (direct `actor`, `wp`, `match`, `confidence`, `region`, `comment`)
>
> The workflow's `parse-ra-response` node extracts from `parsed.wp_comment` if present, otherwise treats the response as flat format.

**Routing Rules (Yellow Gate):**
- `confidence < YELLOW_CONFIDENCE_THRESHOLD` → Yellow route (human review)
- Invalid/missing required fields → Yellow route
- Ambiguous routing (multi-region) → Yellow route
- Existing WP closed/done state → Yellow route
- OpenProject lookup failure → Yellow route

### Activity Log Format (Honcho Output → Virtual Office Input)

**FROZEN Contract:**
```json
{
  "ts": "ISO8601-timestamp",
  "type": "mail_received|matched|comment_added|transition_proposed|yellow_route|wp_closed|vote_cast|vote_result|score_given|study_insight|session_complete",
  "actor": "ra_us|ra_eu|ra_kr|op_manager|n8n_manager|infra_*|human|system",
  "target": "ra_us|ra_eu|ra_kr|null",
  "payload": {
    "wp": "WP-123",
    "confidence": 0.91,
    "existing": true,
    "note": "진행현황 반영",
    "to": "리뷰중",
    "reason": "low_confidence|multi_region|parse_error",
    "region": "US|EU|KR",
    "subject": "...",
    "result": "approved|rejected|pending",
    "vote": "approve|reject|abstain",
    "topic": "...",
    "target": "Mike 매칭",
    "score": 3
  }
}
```

**Virtual Office Mapping:**
- `activity_log` type messages in Honcho → `adaptHonchoMessage()` → Virtual Office events
- Actor IDs: `ra_us`, `ra_eu`, `ra_kr` (underscore, Honcho peer IDs)
- Character mapping: Mike=`ra_us`, Theo=`ra_eu`, Sam=`ra_kr`

### Growth Metrics Schema

**FROZEN Contract:**
```json
{
  "generated_at": "ISO8601-timestamp",
  "window_start": "ISO8601-date",
  "window_end": "ISO8601-date",
  "metrics": {
    "correction_rate": 0.15,
    "first_pass_match_accuracy": 0.82,
    "confidence_calibration": 0.08,
    "warmstart_lift": 0.35,
    "escalation_precision": 0.91,
    "autonomous_study_sessions": 3,
    "study_insights_count": 42,
    "absence_pattern_signals": []
  },
  "agent_breakdown": {
    "ra_us": {...},
    "ra_eu": {...},
    "ra_kr": {...}
  },
  "readiness": {
    "coverage_score": 0.85,
    "depth_score": 0.73,
    "trend_score": 0.67,
    "overall_verdict": "ready|caution|not_ready"
  }
}
```

**Metric Definitions:**
- `correction_rate` = (human_corrections / total_autonomous_decisions)
- `first_pass_match_accuracy` = (correct_first_pass_matches / total_first_pass_attempts)
- `confidence_calibration` = average(|predicted_confidence - actual_outcome|)
- `warmstart_lift` = (autonomous_accuracy - cold_start_baseline)
- `escalation_precision` = (correct_escalations / total_escalations)
- `autonomous_study_sessions` = count of completed study sessions per agent
- `study_insights_count` = total insights generated across all sessions
- `absence_pattern_signals` = list of gaps in knowledge coverage

## Gate Rules Reference

**Matching + Comment (Green Gate):**
- Autonomous for:
  - Single clear region detected (US/EU/KR)
  - Confidence >= YELLOW_CONFIDENCE_THRESHOLD
  - Valid wp_comment structure
  - Existing WP in active state
- Honcho records: `type=matched` or `type=comment_added`

**Status Transition (escalates with maturity):**
- Initial: Escalates to human for review
- As learning matures: Autonomous for low-risk transitions
- **Close / Reopen WP** = Human-only permanently (GATE-3)

**n8n Workflow Changes:**
- Report first, then proceed (no silent modifications)
- Requires human approval for destructive changes

**Human-Only Actions (permanent):**
- WP close/reopen
- Destructive infra actions (container deletion, DB reset)
- n8n workflow structural changes (require approval)

**Configurable Thresholds:**
- `YELLOW_CONFIDENCE_THRESHOLD` (env var, default 0.75)
- Vote quorum, weights, thresholds (vote-rules.json)
- Bridge relay conditions (bridge-config.json)
- Growth trigger thresholds (growth-trigger-config.json)
