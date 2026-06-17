#!/bin/bash

# Day 1 Baseline Check Script (Simple)
echo "=== Day 1 Baseline Check ==="
echo "Timestamp: $(date -Iseconds)"
echo ""

PASS=0
FAIL=0
WARN=0

check_pass() {
    echo "[PASS] $1"
    ((PASS++))
}

check_fail() {
    echo "[FAIL] $1"
    ((FAIL++))
}

check_warn() {
    echo "[WARN] $1"
    ((WARN++))
}

echo "## 1. System Status Check"
echo "========================="

# Honcho API health
if curl -f -s http://localhost:8000/health > /dev/null 2>&1; then
    check_pass "Honcho API is healthy"
else
    check_fail "Honcho API is not responding"
fi

# PostgreSQL pgvector
if docker exec honcho-postgres-1 pg_isready > /dev/null 2>&1; then
    check_pass "PostgreSQL pgvector is ready"
else
    check_warn "PostgreSQL pgvector check failed (manual verification needed)"
fi

# Redis
if docker exec honcho-redis-1 redis-cli ping > /dev/null 2>&1; then
    check_pass "Redis is responsive"
else
    check_warn "Redis check failed (manual verification needed)"
fi

# Honcho deriver
if docker ps | grep -q deriver; then
    check_pass "Honcho deriver is running"
else
    check_fail "Honcho deriver is not running"
fi

echo ""
echo "## 2. Growth Loop Status"
echo "========================="

echo "Checking daily-growth-runner.py availability..."
if [ -f scripts/daily-growth-runner.py ]; then
    check_pass "daily-growth-runner.py exists"
    echo "  → For dry-run mode, use without --execute (default is dry-run)"
    echo "  → Execute 'python3 scripts/daily-growth-runner.py --help' for options"
else
    check_fail "daily-growth-runner.py not found"
fi

# autonomous-study-scheduler.py checkpoint
if [ -f scripts/study-checkpoint.json ]; then
    check_pass "autonomous-study-scheduler.py checkpoint exists"
else
    check_warn "autonomous-study-scheduler.py checkpoint not found"
fi

echo ""
echo "## 3. Growth Metrics Baseline"
echo "=============================="

LATEST_REPORT=$(find reports -name "growth-*.json" -type f 2>/dev/null | sort -r | head -1)

if [ -n "$LATEST_REPORT" ] && [ -f "$LATEST_REPORT" ]; then
    echo "Latest report: $LATEST_REPORT"
    check_pass "Growth metrics baseline established"
    echo "Current metrics (first 20 lines):"
    head -20 "$LATEST_REPORT"
else
    check_warn "No growth report found"
fi

echo ""
echo "## 4. Deriver Backlog Status"
echo "============================"
check_warn "Deriver backlog needs manual verification"

echo ""
echo "## 5. RA Agents Session Status"
echo "=============================="

if curl -f -s http://localhost:8000/agents > /tmp/agents-list.json 2>&1; then
    check_pass "Agents list retrieved"
    echo "  → Saved to /tmp/agents-list.json"
else
    check_warn "Cannot retrieve agents list"
fi

echo ""
echo "## Summary"
echo "========="
echo "PASS: $PASS"
echo "WARN: $WARN"
echo "FAIL: $FAIL"

echo ""
echo "## Manual Verification Required"
echo "================================"
echo "Please verify:"
echo "1. Check Honcho deriver logs"
echo "2. Verify RA agents (ra_us, ra_eu, ra_kr) recent activity"
echo "3. Review daily-growth-runner.py options for actual execution"
echo "4. Check growth report values"

echo ""
echo "## Baseline Record"
echo "=================="
echo "Timestamp: $(date -Iseconds)"
echo "System Status: $PASS pass, $WARN warn, $FAIL fail"
echo "Latest Report: ${LATEST_REPORT:-'No report found'}"

echo ""
echo "## Next Steps for Day 1"
echo "======================="
if [ $FAIL -eq 0 ]; then
    echo "[COMPLETE] Day 1 baseline checks passed"
    echo "[ACTION] Review growth report values and record baseline metrics"
    echo "[ACTION] Proceed to Day 2 monitoring tomorrow"
else
    echo "[INCOMPLETE] Some checks failed"
    echo "[ACTION] Resolve FAIL items before auto-growth activation"
    echo "[NOTE] WARN items are acceptable for baseline establishment"
fi
