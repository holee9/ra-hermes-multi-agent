#!/usr/bin/env python3
"""Anthropic API budget guard — single-file caller with monthly credit cap.

All Anthropic API usage in this repo MUST go through this module so the
monthly usage ledger stays complete and the credit limit is enforced.
Replicate-ready: copy this file + the .env keys to another device.

Env (scripts/.env):
  ANTHROPIC_API_KEY          account-scoped key (required)
  ANTHROPIC_WORKSPACE_ID     required header for account-scoped keys
  ANTHROPIC_MONTHLY_LIMIT_USD  optional, default 200.0

Usage (python):
  from anthropic_guard import guard
  reply = guard.call("claude-haiku-5-5", [{"role": "user", "content": "hi"}], 64)

Usage (cli):
  python3 scripts/anthropic_guard.py --check   # month usage vs limit
  python3 scripts/anthropic_guard.py --test    # tiny live call
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
LEDGER = ROOT / ".anthropic-usage.jsonl"
API_URL = "https://api.anthropic.com/v1/messages"
DEVICE = "t3610"

DEFAULT_LIMIT_USD = 200.0

# USD per 1M tokens: (input, output) — prompts up to 100k tier.
# Verified 2026-10-20 vs anthropic.com/claude-haiku-5-5 announcements.
PRICES = {
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-opus-5-5": (4.00, 20.00),  # secondary source — verify before heavy use
}


class BudgetExceededError(RuntimeError):
    pass


def load_env() -> dict:
    env = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def month_usage_usd() -> float:
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    total = 0.0
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("ts", "").startswith(month):
                total += rec.get("cost_usd", 0.0)
    return total


def _cost_usd(model: str, in_tok: int, out_tok: int) -> float:
    pin, pout = PRICES[model]
    return in_tok / 1_000_000 * pin + out_tok / 1_000_000 * pout


def _estimate_usd(model: str, messages: list, max_tokens: int) -> float:
    in_tok = len(json.dumps(messages)) // 4  # rough chars/4 approximation
    return _cost_usd(model, in_tok, max_tokens)


def call(model: str, messages: list, max_tokens: int = 1024, *, system: str | None = None) -> dict:
    """Send one /v1/messages request, enforcing the monthly credit cap."""
    env = load_env()
    key = env.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY missing in scripts/.env")
    limit = float(env.get("ANTHROPIC_MONTHLY_LIMIT_USD", DEFAULT_LIMIT_USD))
    used = month_usage_usd()
    est = _estimate_usd(model, messages, max_tokens)
    if used + est >= limit:
        raise BudgetExceededError(
            f"monthly credit cap: used ${used:.4f} + est ${est:.4f} >= limit ${limit:.2f} — call blocked"
        )

    body = {"model": model, "max_tokens": max_tokens, "messages": messages}
    if system:
        body["system"] = system
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    ws = env.get("ANTHROPIC_WORKSPACE_ID")
    if ws:
        headers["anthropic-workspace-id"] = ws

    req = urllib.request.Request(API_URL, data=json.dumps(body).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"anthropic api {e.code}: {e.read().decode()[:400]}") from e

    usage = data.get("usage", {})
    cost = _cost_usd(model, usage.get("input_tokens", 0), usage.get("output_tokens", 0))
    rec = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "device": DEVICE,
        "model": model,
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
        "cost_usd": round(cost, 6),
    }
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return data


def main() -> int:
    if "--check" in sys.argv:
        env = load_env()
        limit = float(env.get("ANTHROPIC_MONTHLY_LIMIT_USD", DEFAULT_LIMIT_USD))
        used = month_usage_usd()
        print(f"month={datetime.now(timezone.utc).strftime('%Y-%m')} used=${used:.4f} "
              f"limit=${limit:.2f} remaining=${limit - used:.4f}")
        return 0
    if "--test" in sys.argv:
        data = call("claude-haiku-5-5", [{"role": "user", "content": "Reply with the single word: ok"}], 16)
        print("reply:", data["content"][0]["text"])
        print("last ledger line:", LEDGER.read_text().splitlines()[-1])
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
