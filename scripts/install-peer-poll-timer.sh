#!/usr/bin/env bash
# install-peer-poll-timer.sh — Install hermes-peer-poll systemd timer (SPEC-DEVCOMM-001 M2).
#
# Pattern: install-auto-growth-timer.sh (sudo + explicit confirm flag).
# Safe install copies the units only; activation requires the approval marker.

set -euo pipefail

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SYSTEMD_DIR="$SCRIPT_DIR/systemd"
SYSTEMD_SYSTEM=/etc/systemd/system

SERVICE_FILE="$SYSTEMD_DIR/hermes-peer-poll.service"
TIMER_FILE="$SYSTEMD_DIR/hermes-peer-poll.timer"

ENABLE=false
START_NOW=false
CONFIRM_ACTIVATION=false
for arg in "$@"; do
  [[ "$arg" == "--enable" ]] && ENABLE=true
  [[ "$arg" == "--start-now" ]] && START_NOW=true
  [[ "$arg" == "--confirm-peer-poll-activation" ]] && CONFIRM_ACTIVATION=true
done

if { [[ "$ENABLE" == "true" ]] || [[ "$START_NOW" == "true" ]]; } && [[ "$CONFIRM_ACTIVATION" != "true" ]]; then
  cat >&2 <<'EOF'
Refusing to activate the peer comment poller without explicit approval.

Allowed safe install:
  bash scripts/install-peer-poll-timer.sh

Activation requires the approval marker:
  bash scripts/install-peer-poll-timer.sh --enable --confirm-peer-poll-activation

Immediate service execution also requires the marker:
  bash scripts/install-peer-poll-timer.sh --start-now --confirm-peer-poll-activation
EOF
  exit 2
fi

echo "=== RA Hermes Peer Poll Timer Installer ==="
echo "Repo root: $REPO_ROOT"

echo "[1/4] Checking dependencies..."
[[ -x /usr/bin/gh ]] || { echo "Missing /usr/bin/gh (GitHub CLI)"; exit 2; }
[[ -f "$SCRIPT_DIR/.env" ]] || { echo "Missing scripts/.env (API_SERVER_KEY required)"; exit 2; }
echo "  OK"

echo "[2/4] Running poller dry-run readiness check..."
cd "$REPO_ROOT"
set -a; . "$SCRIPT_DIR/.env"; set +a
/usr/bin/python3 scripts/peer-comment-poller.py --dry-run
echo "  OK"

echo "[3/4] Installing systemd units..."
sudo cp "$SERVICE_FILE" "$SYSTEMD_SYSTEM/hermes-peer-poll.service"
sudo cp "$TIMER_FILE" "$SYSTEMD_SYSTEM/hermes-peer-poll.timer"
sudo systemctl daemon-reload
echo "  Units installed."

if [[ "$ENABLE" == "true" ]]; then
  echo "[4/4] Enabling timer..."
  sudo systemctl enable hermes-peer-poll.timer
  sudo systemctl start hermes-peer-poll.timer
  sudo systemctl status hermes-peer-poll.timer --no-pager || true
else
  echo "[4/4] Enable skipped. Run with --enable --confirm-peer-poll-activation after review."
fi

if [[ "$START_NOW" == "true" ]]; then
  echo "Starting one immediate peer-poll service run..."
  sudo systemctl start hermes-peer-poll.service
fi

echo ""
echo "Manual run : sudo systemctl start hermes-peer-poll.service"
echo "Timer next : systemctl list-timers hermes-peer-poll.timer"
echo "Logs       : journalctl -u hermes-peer-poll.service -f"
