#!/bin/bash

# Daily Monitoring Script for Day 2-3
# Runs automatically and generates checklist status

DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date -Iseconds)
REPORT_DIR="reports/daily-monitoring"
CHECKLIST_FILE="$REPORT_DIR/checklist-$DATE.md"

# Create report directory
mkdir -p "$REPORT_DIR"

echo "=== Daily Monitoring Report ===" > "$CHECKLIST_FILE"
echo "Date: $DATE" >> "$CHECKLIST_FILE"
echo "Timestamp: $TIMESTAMP" >> "$CHECKLIST_FILE"
echo "" >> "$CHECKLIST_FILE"

PASS=0
FAIL=0
WARN=0

check_pass() {
    echo "- [x] $1" >> "$CHECKLIST_FILE"
    ((PASS++))
}

check_fail() {
    echo "- [ ] $1 ❌ FAILED" >> "$CHECKLIST_FILE"
    ((FAIL++))
}

check_warn() {
    echo "- [ ] $1 ⚠️  MANUAL CHECK" >> "$CHECKLIST_FILE"
    ((WARN++))
}

echo "## 1. System Status" >> "$CHECKLIST_FILE"
echo "=================" >> "$CHECKLIST_FILE"

# Honcho API
if curl -f -s http://localhost:8000/health > /dev/null 2>&1; then
    check_pass "Honcho API healthy"
else
    check_fail "Honcho API not responding"
fi

# PostgreSQL
if docker exec honcho-postgres-1 pg_isready > /dev/null 2>&1; then
    check_pass "PostgreSQL pgvector ready"
else
    check_fail "PostgreSQL not ready"
fi

# Redis
if docker exec honcho-redis-1 redis-cli ping > /dev/null 2>&1; then
    check_pass "Redis responsive"
else
    check_fail "Redis not responding"
fi

# Deriver
if docker ps | grep -q deriver; then
    check_pass "Honcho deriver running"
else
    check_fail "Deriver not running"
fi

echo "" >> "$CHECKLIST_FILE"
echo "## 2. Growth Metrics" >> "$CHECKLIST_FILE"
echo "=================" >> "$CHECKLIST_FILE"

# Get latest growth report
LATEST_REPORT=$(find reports -name "growth-*.json" -type f 2>/dev/null | sort -r | head -1)

if [ -n "$LATEST_REPORT" ] && [ -f "$LATEST_REPORT" ]; then
    echo "Latest report: $LATEST_REPORT" >> "$CHECKLIST_FILE"

    if command -v jq > /dev/null 2>&1; then
        echo "" >> "$CHECKLIST_FILE"
        echo "### Current Metrics" >> "$CHECKLIST_FILE"
        jq -r '.metrics // . // empty' "$LATEST_REPORT" 2>/dev/null >> "$CHECKLIST_FILE" || echo "No metrics found" >> "$CHECKLIST_FILE"
    fi

    check_pass "Growth metrics available"
else
    check_fail "No growth report found"
fi

echo "" >> "$CHECKLIST_FILE"
echo "## 3. Growth Loop Status" >> "$CHECKLIST_FILE"
echo "=======================" >> "$CHECKLIST_FILE"

# daily-growth-runner availability
if [ -f scripts/daily-growth-runner.py ]; then
    check_pass "daily-growth-runner available"

    # Check if there's recent activity (today's executions)
    TODAY=$(date +%Y-%m-%d)
    if find reports -name "daily-growth-*$TODAY*.json" -type f 2>/dev/null | grep -q .; then
        check_pass "Today's growth execution found"
    else
        check_warn "No today's growth execution yet (Day 2-3: dry-run expected)"
    fi
else
    check_fail "daily-growth-runner not found"
fi

# autonomous-study-scheduler
if [ -f scripts/study-bootstrap-progress.json ]; then
    check_pass "Study scheduler checkpoint exists"

    if command -v jq > /dev/null 2>&1; then
        LAST_RUN=$(jq -r '.last_bootstrap_ts // "N/A"' scripts/study-bootstrap-progress.json)
        echo "Bootstrap progress: $LAST_RUN" >> "$CHECKLIST_FILE"
    fi
else
    check_warn "Study scheduler checkpoint not found"
fi

echo "" >> "$CHECKLIST_FILE"
echo "## 4. Summary" >> "$CHECKLIST_FILE"
echo "=========" >> "$CHECKLIST_FILE"
echo "- **PASS**: $PASS" >> "$CHECKLIST_FILE"
echo "- **WARN**: $WARN" >> "$CHECKLIST_FILE"
echo "- **FAIL**: $FAIL" >> "$CHECKLIST_FILE"

echo "" >> "$CHECKLIST_FILE"
echo "## 5. Status" >> "$CHECKLIST_FILE"

if [ $FAIL -eq 0 ]; then
    echo "🟢 **NORMAL** - All critical systems operational" >> "$CHECKLIST_FILE"
elif [ $FAIL -le 2 ]; then
    echo "🟡 **ATTENTION** - Some issues detected, review required" >> "$CHECKLIST_FILE"
else
    echo "🔴 **CRITICAL** - Multiple failures detected, immediate action required" >> "$CHECKLIST_FILE"
fi

# Copy checklist to dashboard location for easy viewing
cp "$CHECKLIST_FILE" "docs/monitoring/today-status.md"

echo "Daily monitoring complete: $CHECKLIST_FILE"
echo "Dashboard copy: docs/monitoring/today-status.md"
