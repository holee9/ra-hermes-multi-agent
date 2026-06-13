# RA Hermes Multi-Agent — Architecture Codemaps

Visual diagrams of the RA Hermes Multi-Agent system architecture, data flows, and agent interactions.

**Generated**: 2026-06-10  
**Project**: RA Hermes Multi-Agent (Medical Device Regulatory Affairs)  
**Status**: Operational baseline with safety/QA hardening reflected in repo (2026-06-13)

---

## Diagrams

### 1. **system-overview.mmd** — Full System Architecture

Comprehensive view of the entire system showing:

- **Three Hardware Nodes**: T3610 (Honcho server), GX10 (LLM inference), RPi (automation & WP management)
- **Service Stack**: FastAPI, PostgreSQL with pgvector, Redis, n8n workflows, OpenProject
- **Workspaces**: Business Workspace (RA agents + ops) and Infrastructure Workspace (infra agents + voting)
- **Data Paths**: Email → n8n → RA analysis → Honcho → Activity log → Virtual Office
- **Network**: 2.5G LAN connections between all three nodes

**Key Components**:
- T3610: Honcho stack (API, deriver, database, memory)
- GX10: Qwen3 inference engine (4096-dim embeddings)
- RPi: n8n workflows, OpenProject, external integrations
- Two Hermes workspaces: business and infrastructure (complete isolation)

**Read this for**: Understanding hardware placement, service responsibilities, and inter-system connections.

---

### 2. **agent-interaction.mmd** — Email Triage & Decision Flow

Detailed sequence showing how incoming emails are processed and routed:

- **Intake**: Email webhook → n8n mail-triage
- **Parsing**: Body normalization, regulatory authority detection (FDA, MDR, KGMP)
- **Routing**: Decision to send to ra_us, ra_eu, or ra_kr based on region
- **Analysis**: RA experts analyze and search Honcho for matching Work Packages (WPs)
- **Matching**: Confidence scoring for existing vs. new WP decision
- **Safety Hardening**: Low confidence, parse failure, existing WP closed/done state, or OpenProject lookup failure routes to Yellow
- **Gate Rules** (Color-coded):
  - **Green (GATE-1)**: Autonomous — matching + comment addition only when confidence and WP status are allowed
  - **Yellow (GATE-2)**: Human review — status transitions, low confidence, parse failure, ambiguous routing, closed/done WP match, OP lookup failure
  - **Red (GATE-3)**: Human only — close/reopen WP
- **Actions**: Create WP, add comment, propose status change, store in Honcho
- **Learning Loop**: Human 3-point evaluation → Deriver inference → weight adjustment for next run
- **Output**: Activity log → Virtual Office + Infrastructure voting

**Read this for**: Understanding the email-to-decision pipeline and gate rules.

---

## How to Render

### GitHub Markdown

The `.mmd` files render directly in GitHub when viewed in a browser:
1. Navigate to the file in the GitHub repository
2. GitHub's built-in Mermaid renderer displays the diagram automatically

No additional tools or setup required.

### Local Rendering

To render locally with Mermaid CLI:

```bash
# Install Mermaid CLI
npm install -g mermaid-cli

# Render all diagrams
mmdc -i system-overview.mmd -o system-overview.svg
mmdc -i agent-interaction.mmd -o agent-interaction.svg

# Or render to PNG
mmdc -i system-overview.mmd -o system-overview.png -t default
```

### VS Code

Install the "Markdown Preview Mermaid Support" extension:
1. Install: https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid
2. Open the `.mmd` file in VS Code
3. Use `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac) to preview

---

## Reading the Diagrams

### Color Coding (system-overview.mmd)

- **Light Blue**: T3610 server (Honcho, RA experts)
- **Light Green**: GX10 server (inference, embeddings)
- **Light Orange**: Raspberry Pi (automation, WP management)
- **Light Purple**: Business Workspace (RA agents, ops)
- **Light Pink**: Infrastructure Workspace (infra agents, voting)

### Color Coding (agent-interaction.mmd)

- **Light Blue**: Email input
- **Light Purple**: Parse & routing
- **Light Orange**: RA analysis
- **Light Green**: Matching & decision
- **Light Pink**: Gate rules
- **Light Cyan**: Actions & storage
- **Light Violet**: Learning cycle
- **Light Blue**: Output & monitoring
- **Yellow**: Decision nodes
- **Green**: GATE-1 autonomous actions
- **Orange**: GATE-2 human review
- **Red**: GATE-3 human-only actions

---

## System Architecture Summary

### Three-Node Hardware Layout

| Node | Hardware | Role |
|------|----------|------|
| **T3610** | Xeon 12C/24T, 32GB, Linux | Honcho server (FastAPI :8000, PostgreSQL :5433, Redis :6379, deriver) + RA experts |
| **GX10** | Grace Blackwell ARM | Qwen3 LLM inference via Ollama :11434 (OpenAI-compatible endpoint) |
| **RPi** | Raspberry Pi 5+, 16GB RAM | n8n automation (mail-triage, bridge, feedback), OpenProject WP management |

### Two Workspaces (Complete Isolation)

- **Business Workspace**: RA agents (ra_us, ra_eu, ra_kr) + ops agents (op_manager, n8n_manager)
- **Infrastructure Workspace**: Infra agents (infra_t3610, infra_gx10, infra_rpi) + consensus voting engine

### Data Contracts (Frozen)

**RA Analysis Result JSON**:
```json
{
  "actor": "ra_us|ra_eu|ra_kr",
  "wp": "WP-123|null",
  "match": "existing|new",
  "confidence": 0.0-1.0,
  "region": "US|EU|KR",
  "comment": "Analysis summary",
  "transition_proposed": "in-review|null"
}
```

**Activity Log JSON**:
```json
{
  "ts": "ISO8601",
  "type": "mail_received|matched|comment_added|feedback_submitted|state_changed",
  "actor": "ra_us|...|human|system",
  "payload": {...}
}
```

---

## Gate Rules (Hard Rules)

| Action | Authority | Status |
|--------|-----------|--------|
| RA analysis execution | Agent autonomous | GATE-1 (Green) |
| Comment addition | Agent autonomous | GATE-1 (Green) |
| WP creation | Agent autonomous | GATE-1 (Green) |
| Low confidence / parse failure / ambiguous routing | Human review | GATE-2 (Yellow) |
| Existing WP closed/done/unknown or lookup failed | Human review | GATE-2 (Yellow) |
| Status transition (review → approval) | Human review | GATE-2 (Yellow) |
| n8n workflow changes | Human approval | GATE-2 (Yellow) |
| **WP close / reopen** | **Human only** | **GATE-3 (Red)** |
| Destructive infra ops | Human approval | GATE-3 (Red) |

---

## Related Documentation

- **`.moai/project/structure.md`**: Detailed directory structure and module responsibilities
- **`docs/RA-multi-agent-master-design.md`**: Master design document (philosophy, technical foundation, organization)
- **`docs/implementation-spec.md`**: Implementation boundaries (what to code vs. what Hermes handles)
- **`docs/operations-guide.md`**: Runtime operations and configuration
- **`README.md`**: Current project status and progress

---

## Navigation

To understand the system:

1. **First**: Read this file (overview of diagrams)
2. **Then**: Look at `system-overview.mmd` (hardware + services)
3. **Next**: Study `agent-interaction.mmd` (email → decision flow)
4. **Finally**: Review `.moai/project/structure.md` for directory responsibilities

---

**Last Updated**: 2026-06-13
**Maintainer**: Project Architecture  
**Verification**: GitHub Issues + Code Review
