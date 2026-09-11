#!/bin/bash

# Daily Monitoring Script for Day 2-3
# Runs automatically and generates checklist status

# Optional date override: `bash daily-monitoring.sh 2026-07-03` regenerates a
# past day's checklist (e.g. back-fill auto-detected [x] after a fix like #100).
# Default (no arg) = today, preserving cron behavior.
DATE="${1:-$(date +%Y-%m-%d)}"
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

# Get latest growth report — prefer today's dated snapshot, else newest by mtime.
# (sort -r on names mis-picks "growth-transition-readiness-..." ahead of "growth-YYYY-MM-DD".)
TODAY_GROWTH_REPORT="reports/growth-$(date +%Y-%m-%d).json"
if [ -f "$TODAY_GROWTH_REPORT" ]; then
    LATEST_REPORT="$TODAY_GROWTH_REPORT"
else
    LATEST_REPORT=$(find reports -maxdepth 1 -name "growth-*.json" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
fi

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

    # Check if there's recent activity (today's executions).
    # Covers both the legacy daily-growth-DATE.json path and the current
    # pre-auto-growth-loop output under reports/auto-growth/.
    TODAY="$DATE"   # reuse the (possibly overridden) report date for detection
    if find reports \( -name "daily-growth-*${TODAY}*.json" -o -name "pre-execute-${TODAY}*.json" \) -type f 2>/dev/null | grep -q .; then
        check_pass "Today's growth execution found"
    else
        check_warn "No today's growth execution yet"
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

# #141: 이 스크립트가 보는 것은 **인프라 점검 항목**뿐이다 — Honcho/PostgreSQL/Redis/
# deriver/성장 리포트/스케줄러. 메일 유입과 mail-triage 처리 경로는 **한 건도 검사하지
# 않는다**. 그런데 FAIL=0 이면 "All critical systems operational" 이라고 적어, 메일이
# 실제로 처리되고 있다는 뜻으로 읽혔다(#141 의 팬텀 트래픽이 실제 처리량을 가린 맥락과
# 같은 오독을 부른다). 판정 문구를 **점검한 범위로 한정**하고, 검사하지 않은 것을 명시한다.
# WARN 도 판정에 싣는다 — 경고가 있는데 아무 표시가 없으면 없는 것처럼 읽힌다.
if [ $FAIL -eq 0 ]; then
    if [ $WARN -eq 0 ]; then
        echo "🟢 **NORMAL (인프라 점검 범위)** - 점검한 인프라 항목 모두 정상" >> "$CHECKLIST_FILE"
    else
        echo "🟢 **NORMAL (인프라 점검 범위, 경고 ${WARN}건)** - 실패 없음. 경고 항목은 위 목록 확인" >> "$CHECKLIST_FILE"
    fi
elif [ $FAIL -le 2 ]; then
    echo "🟡 **ATTENTION** - Some issues detected, review required" >> "$CHECKLIST_FILE"
else
    echo "🔴 **CRITICAL** - Multiple failures detected, immediate action required" >> "$CHECKLIST_FILE"
fi
echo "" >> "$CHECKLIST_FILE"
echo "> **이 점검이 확인하지 않은 것**: 메일 유입과 mail-triage 처리 경로는 검사 대상이 아니다." >> "$CHECKLIST_FILE"
echo "> 위 판정은 인프라 구성요소의 응답 여부이며, **메일이 실제로 처리되고 있다는 증거가 아니다**." >> "$CHECKLIST_FILE"
echo "> 처리 여부는 n8n 실행 이력과 OpenProject 반영으로 따로 확인해야 한다 (#141)." >> "$CHECKLIST_FILE"

# Copy checklist to dashboard location for easy viewing
cp "$CHECKLIST_FILE" "docs/monitoring/today-status.md"

echo "Daily monitoring complete: $CHECKLIST_FILE"
echo "Dashboard copy: docs/monitoring/today-status.md"
