#!/usr/bin/env bash
# install-study-scheduler.sh — Install hermes-study systemd timer on T3610.
#
# Usage:
#   bash scripts/install-study-scheduler.sh [--bootstrap]
#
# Options:
#   --bootstrap   Run an immediate bootstrap study (all chunks) before enabling the timer.
#
# Requirements:
#   - systemd (T3610 Linux)
#   - python3 with psycopg2-binary and requests
#   - Running Honcho stack (localhost:8000) and hermes-api-server (localhost:8643)
#   - pgvector ra_knowledge populated (run doc-converter / knowledge ingest first)

set -euo pipefail

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SYSTEMD_DIR="$SCRIPT_DIR/systemd"
SYSTEMD_SYSTEM=/etc/systemd/system

SERVICE_FILE="$SYSTEMD_DIR/hermes-study.service"
TIMER_FILE="$SYSTEMD_DIR/hermes-study.timer"

BOOTSTRAP=false
for arg in "$@"; do
  [[ "$arg" == "--bootstrap" ]] && BOOTSTRAP=true
done

echo "=== RA Hermes Study Scheduler Installer ==="
echo "Repo root: $REPO_ROOT"

# Verify dependencies
echo "[1/5] Checking dependencies..."
python3 -c "import psycopg2, requests" 2>/dev/null || {
  echo "  Installing psycopg2-binary and requests..."
  pip install --quiet psycopg2-binary requests
}
echo "  OK"

# Verify Honcho is reachable
echo "[2/5] Checking Honcho API (localhost:8000)..."
if curl -sf --max-time 5 http://localhost:8000/health > /dev/null 2>&1; then
  echo "  OK"
else
  echo "  WARNING: Honcho not reachable. Timer will be installed but study may fail until Honcho is running."
fi

# Install systemd units
echo "[3/5] Installing systemd units..."
sudo cp "$SERVICE_FILE" "$SYSTEMD_SYSTEM/hermes-study.service"
sudo cp "$TIMER_FILE"   "$SYSTEMD_SYSTEM/hermes-study.timer"
sudo systemctl daemon-reload
sudo systemctl enable hermes-study.timer
sudo systemctl start  hermes-study.timer
echo "  Timer enabled and started."
sudo systemctl status hermes-study.timer --no-pager || true

# Bootstrap run (optional)
echo "[4/5] Bootstrap mode: $BOOTSTRAP"
if [[ "$BOOTSTRAP" == "true" ]]; then
  echo "  Running bootstrap study (this may take a while)..."
  cd "$REPO_ROOT"
  python3 scripts/autonomous-study-scheduler.py bootstrap
  echo "  Bootstrap complete."
else
  echo "  Skipped. Run manually: python3 scripts/autonomous-study-scheduler.py bootstrap"
fi

# Verify checkpoint
echo "[5/5] Checkpoint state:"
if [[ -f "$SCRIPT_DIR/study-checkpoint.json" ]]; then
  cat "$SCRIPT_DIR/study-checkpoint.json"
else
  echo "  No checkpoint yet (will be created after first run)."
fi

echo ""
echo "=== Installation complete ==="
echo "  View logs  : journalctl -u hermes-study.service -f"
echo "  Manual run : sudo systemctl start hermes-study.service"
echo "  Timer next : systemctl list-timers hermes-study.timer"
