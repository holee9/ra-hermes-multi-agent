#!/usr/bin/env python3
"""hive drain gate — inbox 파일이 peer의 턴이 되는 조건 판정 (P3-2 참조 구현).

docs/governance/delivery-gate.md §3·§3.1·§4·§5.1·§6 을 코드로 옮긴 **판정 로직만** 담는다.
Hermes 상태 소스·입력 sink는 주입되는 콜러블이며 여기서 추정하지 않는다(#2 G3, P3-0 실측 전).
소스가 없으면 상태는 항상 `unavailable`이고 자동 전달은 일어나지 않는다.

계약 요약
- 상태 값: idle | busy | unknown | stale | unavailable. **idle일 때만 전달**, 나머지는 보류(실패 아님).
- 잠잠함·시간 경과는 idle의 증거가 아니다 — 이 모듈은 로그를 읽지 않는다.
- 수동 해제(manual)는 일시정지(paused)만 우회한다. idle·유예·브레이커·턴 간격은 그대로.
- 턴 단위 최소 간격: 직전 전달분이 `handled`로 확인되기 전에는 다음 메시지를 넣지 않는다.
- 수신측 compare-and-accept 계약이 없으면(sink가 accept 신호를 주지 않으면) **배치당 peer별 1건**.
- 상태 값이 GATE_MAX_AGE보다 오래됐으면 stale로 강등한다.
- 배치당 1건은 속도 제한이지 원자성 보장이 아니다(TOCTOU는 수신측 직렬 수락만 없앤다).
- 현재 RA peer의 실제 진입점은 hermes-api-server의 일회성 `hermes -p` subprocess다(delivery-gate §3.1) —
  이 모듈은 그 경로에 입력을 주입하지 않으며, 주입은 P3-0 수락 계약 실측 뒤에만 sink로 붙인다.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

STATES = ("idle", "busy", "unknown", "stale", "unavailable")
INBOX_NAME = re.compile(r"^(?P<ts>\d{8}T\d{6}[^-]*)-(?P<id>evt_[A-Za-z0-9_]+)\.json$")


@dataclass
class GateState:
    """authoritative 소스가 돌려준 상태. observed_at 이 없으면 소스가 시각을 주지 않은 것 → stale 판정 불가 → unknown."""
    value: str
    observed_at: datetime | None = None
    accept_token: str | None = None       # 수신측 compare-and-accept 계약이 있으면 채워진다


@dataclass
class Peer:
    actor: str
    paused: bool = False
    booted_at: datetime | None = None
    breaker: str = "ok"                   # ok | degraded | stopped (레벨 명칭은 P3/P4에서 확정)
    last_written: str | None = None       # 직전 전달 메시지 id (handled 확인 전까지 유지)


@dataclass
class Decision:
    actor: str
    src: Path | None
    msg_id: str | None
    action: str                           # deliver | hold | none
    reason: str = ""


@dataclass
class Config:
    grace: timedelta = timedelta(seconds=0)          # 시작 유예 — 실측 후 사람이 정한다
    max_age: timedelta = timedelta(seconds=30)       # GATE_MAX_AGE
    per_batch: int = 1                               # 수신측 accept 계약 없을 때 peer당 배치 한도


def _normalize(state: GateState | None, now: datetime, cfg: Config) -> str:
    if state is None:
        return "unavailable"
    v = state.value if state.value in STATES else "unknown"
    if v == "idle":
        if state.observed_at is None:
            return "unknown"                         # 시각 없는 idle은 신뢰하지 않는다
        if now - state.observed_at > cfg.max_age:
            return "stale"
    return v


def next_message(inbox: Path) -> tuple[Path, str] | None:
    """§6: 파일명 사전순 = 도착순, `manual:true`는 선두. .done/.tmp-/비정형 이름 제외."""
    candidates = []
    for f in sorted(inbox.glob("*.json")):
        m = INBOX_NAME.match(f.name)
        if not m or f.name.startswith(".tmp-"):
            continue
        manual = False
        try:
            raw = json.loads(f.read_text(encoding="utf-8"))
            manual = isinstance(raw, dict) and raw.get("manual") is True
        except (OSError, json.JSONDecodeError):
            pass
        candidates.append((0 if manual else 1, f.name, f, m.group("id"), manual))
    if not candidates:
        return None
    _, _, f, mid, _ = min(candidates)
    return f, mid


def decide(peer: Peer, state: GateState | None, msg: tuple[Path, str] | None, now: datetime,
           cfg: Config, handled: Callable[[str], bool], delivered_this_batch: int = 0) -> Decision:
    """한 peer에 대한 한 번의 판정. 전부 충족 시에만 deliver (§3)."""
    if msg is None:
        return Decision(peer.actor, None, None, "none", "empty-inbox")
    src, mid = msg
    manual = False
    try:
        manual = json.loads(src.read_text(encoding="utf-8")).get("manual") is True
    except (OSError, json.JSONDecodeError, AttributeError):
        pass
    hold = lambda why: Decision(peer.actor, src, mid, "hold", why)  # noqa: E731

    if peer.breaker == "stopped":
        return hold("breaker-stopped")
    if peer.paused and not manual:                                   # §4: 수동 해제는 이 조건만 우회
        return hold("paused")
    if peer.booted_at is not None and now - peer.booted_at < cfg.grace:
        return hold("boot-grace")
    if peer.last_written and not handled(peer.last_written):        # 턴 단위 최소 간격 (§3)
        return hold(f"awaiting-handled:{peer.last_written}")
    st = _normalize(state, now, cfg)
    if st != "idle":
        return hold(f"state-{st}")
    if delivered_this_batch >= cfg.per_batch and not (state and state.accept_token):
        return hold("per-batch-limit")                               # §3.1 수락 계약 없으면 배치당 1건
    return Decision(peer.actor, src, mid, "deliver", "manual" if manual else "idle")


@dataclass
class Drain:
    root: Path
    cfg: Config = field(default_factory=Config)
    source: Callable[[str], GateState | None] | None = None      # actor → 상태 (없으면 unavailable)
    sink: Callable[[str, Path], bool] | None = None              # (actor, file) → 넘겼는가. 없으면 dry-run
    handled: Callable[[str], bool] = lambda _id: False           # §5.1 handled 확인 — 기본은 '미확인'
    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)

    def run(self, peers: list[Peer]) -> list[Decision]:
        out = []
        for peer in peers:
            inbox = self.root / "agents" / peer.actor / "inbox"
            if not inbox.is_dir():
                out.append(Decision(peer.actor, None, None, "none", "no-inbox"))
                continue
            state = self.source(peer.actor) if self.source else None
            d = decide(peer, state, next_message(inbox), self.now(), self.cfg, self.handled)
            if d.action == "deliver" and self.sink is not None:
                if self.sink(peer.actor, d.src):
                    peer.last_written = d.msg_id
                else:
                    d = Decision(peer.actor, d.src, d.msg_id, "hold", "sink-refused")
            out.append(d)
        return out


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="hive drain gate — dry-run 판정 출력 (소스·sink 미주입 = 전달 없음)")
    ap.add_argument("root")
    ap.add_argument("--peer", action="append", default=[], help="actor id (반복 가능)")
    a = ap.parse_args(argv)
    for d in Drain(Path(a.root)).run([Peer(p) for p in a.peer]):
        print(json.dumps({"actor": d.actor, "msg": d.msg_id, "action": d.action, "reason": d.reason}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
