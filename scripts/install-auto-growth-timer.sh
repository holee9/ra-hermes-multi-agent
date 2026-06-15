#!/usr/bin/env bash
# install-auto-growth-timer.sh — Install hermes-auto-growth systemd timer.

set -euo pipefail

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SYSTEMD_DIR="$SCRIPT_DIR/systemd"
SYSTEMD_SYSTEM=/etc/systemd/system

SERVICE_FILE="$SYSTEMD_DIR/hermes-auto-growth.service"
TIMER_FILE="$SYSTEMD_DIR/hermes-auto-growth.timer"

ENABLE=false
START_NOW=false
for arg in "$@"; do
  [[ "$arg" == "--enable" ]] && ENABLE=true
  [[ "$arg" == "--start-now" ]] && START_NOW=true
done

echo "=== RA Hermes Auto Growth Timer Installer ==="
echo "Repo root: $REPO_ROOT"

echo "[1/4] Checking dependencies..."
python3 -c "import psycopg2, requests" 2>/dev/null || {
  echo "Missing Python dependencies: psycopg2 and requests"
  exit 2
}
echo "  OK"

echo "[2/4] Running readiness check..."
cd "$REPO_ROOT"
python3 scripts/pre-auto-growth-loop.py \
  --iterations 1 \
  --pending-scope ra \
  --max-pending 0 \
  --sleep-seconds 10 \
  --drain-timeout-seconds 900
echo "  OK"

echo "[3/4] Installing systemd units..."
sudo cp "$SERVICE_FILE" "$SYSTEMD_SYSTEM/hermes-auto-growth.service"
sudo cp "$TIMER_FILE" "$SYSTEMD_SYSTEM/hermes-auto-growth.timer"
sudo systemctl daemon-reload
echo "  Units installed."

if [[ "$ENABLE" == "true" ]]; then
  echo "[4/4] Enabling timer..."
  sudo systemctl enable hermes-auto-growth.timer
  sudo systemctl start hermes-auto-growth.timer
  sudo systemctl status hermes-auto-growth.timer --no-pager || true
else
  echo "[4/4] Enable skipped. Run with --enable after review."
fi

if [[ "$START_NOW" == "true" ]]; then
  echo "Starting one immediate auto-growth service run..."
  sudo systemctl start hermes-auto-growth.service
fi

echo ""
echo "Manual run : sudo systemctl start hermes-auto-growth.service"
echo "Timer next : systemctl list-timers hermes-auto-growth.timer"
echo "Logs       : journalctl -u hermes-auto-growth.service -f"
