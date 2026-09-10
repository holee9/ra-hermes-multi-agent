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
- dry-run(기본)은 어떤 파일도 쓰지 않고 sink도 부르지 않는다. execute에서도 sink 호출 전에 `submitting`을 저널에
  영속하며, 저장 실패·중단 뒤 재시작은 sink를 다시 부르지 않고 수신측 안정 id 조회(lookup)로만 복구한다.
- execute 실행은 `.drain/lock`(flock) 단일 소유 — read-submit-save를 한 프로세스만 수행. 수신측은 sink에 명시된
  msg_id로 멱등이어야 한다(P3-0 수락 계약 인수 항목). 저널은 fsync 후 rename, 손상 저널은 덮어쓰지 않고 보류.
- 배치당 1건은 속도 제한이지 원자성 보장이 아니다(TOCTOU는 수신측 직렬 수락만 없앤다).
- 현재 RA peer의 실제 진입점은 hermes-api-server의 일회성 `hermes -p` subprocess다(delivery-gate §3.1) —
  이 모듈은 그 경로에 입력을 주입하지 않으며, 주입은 P3-0 수락 계약 실측 뒤에만 sink로 붙인다.
"""
from __future__ import annotations

import fcntl
import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

STATES = ("idle", "busy", "unknown", "stale", "unavailable")


class DrainError(Exception):
    pass
INBOX_NAME = re.compile(r"^(?P<ts>\d{8}T\d{6}[^-]*)-(?P<id>evt_[A-Za-z0-9_]+)\.json$")


@dataclass
class GateState:
    """authoritative 소스가 돌려준 상태. observed_at 이 없으면 소스가 시각을 주지 않은 것 → stale 판정 불가 → unknown."""
    value: str
    observed_at: datetime | None = None
    accept_token: str | None = None       # 수신측 compare-and-accept 계약이 있으면 채워진다
    error: str | None = None              # 소스 조회 실패 사유 (unknown 판정의 근거)


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
    v = state.value if isinstance(state.value, str) and state.value in STATES else "unknown"
    if v == "idle":
        t = state.observed_at
        if not isinstance(t, datetime) or t.tzinfo is None:
            return "unknown"                         # 시각 없음·naive 시각의 idle은 신뢰하지 않는다
        if t > now:
            return "unknown"                         # 미래 시각 — 소스 시계 불일치
        if now - t > cfg.max_age:
            return "stale"
    return v


def _query(source, actor: str) -> GateState | None:
    """소스 실패는 판정 실패가 아니라 `unknown` 보류다 — run() 전체를 종료하지 않는다."""
    if source is None:
        return None
    try:
        st = source(actor)
    except Exception as e:                            # noqa: BLE001 — 소스 종류를 모른다(주입 콜러블)
        return GateState("unknown", None, None, error=f"{type(e).__name__}: {e}")
    return st if isinstance(st, GateState) else GateState("unknown")


def next_message(inbox: Path, exclude: set[str] | frozenset[str] = frozenset()) -> tuple[Path, str] | None:
    """§6: 파일명 사전순 = 도착순, `manual:true`는 선두. .done/.tmp-/비정형 이름·이미 written 된 id 제외."""
    candidates = []
    for f in sorted(inbox.glob("*.json")):
        m = INBOX_NAME.match(f.name)
        if not m or f.name.startswith(".tmp-") or m.group("id") in exclude:
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
    """peer별 저널 `.drain/<actor>.json`이 정본이다: written 된 id는 다시 선택되지 않고, handled 확인 후
    `inbox/.done/`으로 옮긴다(§5.1 — 이동은 확인 이후의 정리이지 완료의 증거가 아니다). 재시작해도 메모리에
    의존하지 않는다."""
    root: Path
    cfg: Config = field(default_factory=Config)
    source: Callable[[str], GateState | None] | None = None      # actor → 상태 (없으면 unavailable)
    sink: Callable[[str, Path, str, str | None], bool] | None = None  # (actor, file, msg_id, accept_token) → 수신측이 받았는가; 수신측은 msg_id로 멱등
    handled: Callable[[str], bool] = lambda _id: False           # §5.1 handled 확인 — 기본은 '미확인'
    lookup: Callable[[str, str], bool | None] | None = None      # (actor, msg_id) → 수신측이 이 id를 받았는가 (안정 id 조회)
    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)
    execute: bool = False                                        # False = dry-run: 어떤 파일도 쓰지 않고 sink도 부르지 않는다

    _lock_fd: int | None = None

    def _journal_path(self, actor: str) -> Path:
        return self.root / ".drain" / f"{actor}.json"

    # 단일 소유: read-submit-save 전체를 한 프로세스만 수행한다(codex 재현: 두 프로세스가 같은 저널을 읽고
    # 각각 submit → sink 2회). OS flock — 보유 프로세스가 죽으면 커널이 해제한다.
    def acquire_lock(self):
        (self.root / ".drain").mkdir(parents=True, exist_ok=True)
        fd = os.open(self.root / ".drain" / "lock", os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            os.close(fd)
            raise DrainError("drain lock 보유 중 — 다른 drain 프로세스가 실행 중이므로 거부") from None
        os.ftruncate(fd, 0)
        os.write(fd, str(os.getpid()).encode())
        self._lock_fd = fd

    def release_lock(self):
        if self._lock_fd is not None:
            os.close(self._lock_fd)                                 # close = 커널 해제
            self._lock_fd = None

    def _load(self, actor: str) -> dict | None:
        """None = 저널이 있으나 손상됨 → 이 actor는 아무것도 하지 않고 보류(덮어쓰지 않는다)."""
        p = self._journal_path(actor)
        if not p.exists():
            j = {}
        else:
            try:
                j = json.loads(p.read_text(encoding="utf-8"))
                if not isinstance(j, dict) or not isinstance(j.get("written", {}), dict):
                    return None
            except (OSError, json.JSONDecodeError):
                return None
        j.setdefault("written", {})                  # id → {"ts", "accept_token", "status": submitting|written|handled}
        j.setdefault("last_written", None)
        return j

    def _save(self, actor: str, j: dict):
        if not self.execute:
            return
        p = self._journal_path(actor)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(f".tmp-{p.name}")
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
        try:
            os.write(fd, json.dumps(j, ensure_ascii=False, indent=1).encode("utf-8"))
            os.fsync(fd)                                             # 내용 → 디스크
        finally:
            os.close(fd)
        os.replace(tmp, p)
        dfd = os.open(p.parent, os.O_RDONLY)
        try:
            os.fsync(dfd)                                            # rename → 디스크
        finally:
            os.close(dfd)

    def _settle(self, actor: str, inbox: Path, j: dict) -> None:
        """written 중 handled 확인된 것을 .done/으로 정리하고 last_written 을 비운다."""
        for mid, rec in list(j["written"].items()):
            if rec.get("status") != "written" or not self.handled(mid):
                continue
            if self.execute:
                for f in inbox.glob(f"*-{mid}.json"):
                    (inbox / ".done").mkdir(exist_ok=True)
                    f.replace(inbox / ".done" / f.name)
            rec["status"] = "handled"
            if j["last_written"] == mid:
                j["last_written"] = None

    def run(self, peers: list[Peer]) -> list[Decision]:
        if self.execute:
            self.acquire_lock()
        try:
            return self._run(peers)
        finally:
            self.release_lock()

    def _run(self, peers: list[Peer]) -> list[Decision]:
        out = []
        for peer in peers:
            inbox = self.root / "agents" / peer.actor / "inbox"
            if not inbox.is_dir():
                out.append(Decision(peer.actor, None, None, "none", "no-inbox"))
                continue
            j = self._load(peer.actor)
            if j is None:
                out.append(Decision(peer.actor, None, None, "hold", "journal-corrupt"))
                continue
            self._settle(peer.actor, inbox, j)
            amb = self._resolve_submitting(peer.actor, j)
            if amb is not None:                                     # 제출 결과 불명 → 재전송 금지, 조회로만 복구
                self._save(peer.actor, j)
                out.append(amb)
                continue
            peer.last_written = j["last_written"] or peer.last_written   # 저널이 정본, 없으면 호출자 상태
            pending = {mid for mid, rec in j["written"].items() if rec.get("status") in ("written", "submitting")}
            state = _query(self.source, peer.actor)
            d = decide(peer, state, next_message(inbox, pending), self.now(), self.cfg, self.handled)
            if state is not None and state.error and d.action == "hold":
                d.reason = f"{d.reason}:{state.error}"
            if d.action == "deliver" and self.execute and self.sink is not None:
                d = self._submit(peer, d, state.accept_token if state else None, j)
            self._save(peer.actor, j)
            out.append(d)
        return out

    def _submit(self, peer: Peer, d: Decision, token: str | None, j: dict) -> Decision:
        """intent-before-submit: sink 호출 **전에** `submitting`을 저널에 영속한다. sink 뒤 저장이 실패해도
        재시작이 sink를 다시 부르지 않는다(중복 전달 금지) — 결과는 lookup으로만 복구한다."""
        j["written"][d.msg_id] = {"ts": self.now().isoformat(timespec="seconds"), "accept_token": token,
                                  "status": "submitting"}
        self._save(peer.actor, j)
        if self.sink(peer.actor, d.src, d.msg_id, token):
            j["written"][d.msg_id]["status"] = "written"
            j["last_written"] = d.msg_id
            peer.last_written = d.msg_id
            return d
        del j["written"][d.msg_id]                                  # 수신측이 명시적으로 거절 — 전달 안 됨
        return Decision(peer.actor, d.src, d.msg_id, "hold", "sink-refused")

    def _resolve_submitting(self, actor: str, j: dict) -> Decision | None:
        """이전 실행이 sink 뒤·저장 전에 죽은 `submitting` 기록의 복구. 수신측 안정 id 조회(lookup)가 있으면
        결과로 확정하고, 없으면 `ambiguous-submit` 보류(사람 확인) — 어느 경우에도 sink를 다시 부르지 않는다."""
        for mid, rec in j["written"].items():
            if rec.get("status") != "submitting":
                continue
            got = self.lookup(actor, mid) if self.lookup else None
            if got is True:
                rec["status"] = "written"
                j["last_written"] = mid
                return None
            if got is False:
                del j["written"][mid]                               # 수신측에 없음 → 다음 배치에서 정상 재판정
                return None
            return Decision(actor, None, mid, "hold", f"ambiguous-submit:{mid}")
        return None


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="hive drain gate — dry-run 판정 출력 (소스·sink 미주입 = 전달 없음)")
    ap.add_argument("root")
    ap.add_argument("--peer", action="append", default=[], help="actor id (반복 가능)")
    ap.add_argument("--execute", action="store_true", help="저널·.done 정리를 실제로 쓴다 (sink는 CLI에서 주입 불가 → 전달 없음)")
    a = ap.parse_args(argv)
    for d in Drain(Path(a.root), execute=a.execute).run([Peer(p) for p in a.peer]):
        print(json.dumps({"actor": d.actor, "msg": d.msg_id, "action": d.action, "reason": d.reason}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
