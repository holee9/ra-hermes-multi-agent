#!/usr/bin/env bash
# growth-metrics-cron.sh — Daily cron wrapper for growth-metrics.py
#
# Run as: bash scripts/growth-metrics-cron.sh
# Crontab entry (T3610, daily at 02:00):
#   0 2 * * * HONCHO_URL=http://localhost:8000 HONCHO_WORKSPACE=work \
#             bash /path/to/scripts/growth-metrics-cron.sh >> /var/log/growth-metrics.log 2>&1
#
# Also compatible with systemd timer — see comments at end of file.

set -euo pipefail
SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

PYTHON="${PYTHON:-/usr/bin/python3}"
HONCHO_URL="${HONCHO_URL:-http://localhost:8000}"
HONCHO_WORKSPACE="${HONCHO_WORKSPACE:-work}"

echo "=== growth-metrics $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

export HONCHO_URL HONCHO_WORKSPACE

"${PYTHON}" "${REPO_ROOT}/scripts/growth-metrics.py" \
  --days 1 \
  --output "${REPO_ROOT}/reports/growth-$(date +%Y-%m-%d).json"

echo "=== done ==="

# ---------------------------------------------------------------------------
# Systemd timer setup (T3610, one-time manual install):
#
# sudo tee /etc/systemd/system/ra-growth-metrics.service <<EOF
# [Unit]
# Description=RA Hermes Growth Metrics
# After=network.target
#
# [Service]
# Type=oneshot
# User=abyz-lab
# WorkingDirectory=/home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent
# Environment=HONCHO_URL=http://localhost:8000
# Environment=HONCHO_WORKSPACE=work
# ExecStart=/usr/bin/bash scripts/growth-metrics-cron.sh
# StandardOutput=append:/var/log/ra-growth-metrics.log
# StandardError=append:/var/log/ra-growth-metrics.log
# EOF
#
# sudo tee /etc/systemd/system/ra-growth-metrics.timer <<EOF
# [Unit]
# Description=Daily RA Growth Metrics at 02:00
#
# [Timer]
# OnCalendar=*-*-* 02:00:00
# Persistent=true
#
# [Install]
# WantedBy=timers.target
# EOF
#
# sudo systemctl daemon-reload
# sudo systemctl enable --now ra-growth-metrics.timer
# sudo systemctl status ra-growth-metrics.timer
# ---------------------------------------------------------------------------
