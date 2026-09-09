#!/usr/bin/env python3
"""
hive 라우터 — P2 격리 참조 구현 (SPEC-HIVE-001 §4 P2, docs/hive/router-spec.md).

상태 머신 (outbox 파일 1개 = 1 메시지):
  normalize → validate → route → deliver → audit → archive

원칙:
  - dry-run이 기본. --execute 없이는 어떤 파일도 쓰지 않는다.
  - 단일 실행 lock (.router/lock, pid 확인 없이는 삭제하지 않음).
  - 저널(.router/journal/<id>.json)에 단계별 진행을 먼저 기록 → 재시작 시 이어서 처리.
    같은 메시지를 두 번 처리해도 inbox 파일·log 항목이 중복되지 않는다 (id가 멱등 키).
  - 실제 inbox 기록에 성공한 대상만 log의 payload.delivered_to에 남긴다.
  - 조용히 사라지는 메시지는 없다: 거부는 .rejected/ + policy(refuse-invalid), 수신 불가는
    human inbox로 escalation(undeliverable), 홉 초과는 escalation(hop-cap).
  - HOP_CAP 미설정이면 대화 이벤트(to 있음)는 전달하지 않고 outbox에 그대로 둔다.
  - git 커밋은 이 모듈이 하지 않는다. run()이 이번 배치가 만든 경로 목록을 반환하므로
    호출자가 `git add <paths>`로만 stage한다 (git add -A 금지, router-spec §8).

사용:
  python3 tools/hive_router.py <hive-root>                      # dry-run: 계획만 출력
  python3 tools/hive_router.py <hive-root> --execute --hop-cap 12
종료코드: 0 처리 완료 / 1 처리 중 오류 / 2 lock 보유 중 또는 입력 문제
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import secrets
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from pathlib import Path

_VE = Path(__file__).resolve().parent / "validate_events.py"
_spec = importlib.util.spec_from_file_location("validate_events", _VE)
validate_events = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate_events)

TERMINAL = validate_events.TERMINAL
OBLIGATING = validate_events.OBLIGATING
DEFAULT_ACT = validate_events.DEFAULT_ACT
KST = timezone(timedelta(hours=9))
ROUTER_ACTOR = "n8n_router"
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "docs/contract/event-v2.1.schema.json"

# 저널 단계 — 이 순서로만 전진한다
STEPS = ("normalized", "validated", "routed", "delivered", "audited", "archived")


class RouterError(Exception):
    pass


class LockHeld(RouterError):
    pass


class InjectedFault(RuntimeError):
    """테스트용 장애 주입 — 실제 운영 경로에서는 발생하지 않는다."""


@dataclass
class Plan:
    """한 메시지의 처리 계획. dry-run은 이것만 출력한다."""
    actor: str
    src: Path
    msg_id: str
    outcome: str                      # deliver | observe | reject | escalate | held
    reason: str = ""
    targets: list[str] = field(default_factory=list)
    event: dict | None = None


@dataclass
class Result:
    plans: list[Plan]
    touched: list[Path]               # 이번 배치가 만든/바꾼 경로 (git add 대상)
    errors: list[str]


class HiveRouter:
    def __init__(self, root: Path, *, hop_cap: int | None, execute: bool,
                 schema_path: Path = SCHEMA_PATH, now=None, fault_at: str | None = None,
                 fault_target: str | None = None):
        self.root = Path(root)
        self.hop_cap = hop_cap
        self.execute = execute
        self.now = now or (lambda: datetime.now(KST))
        self.fault_at = fault_at
        self.fault_target = fault_target
        self.schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
        self.validator = validate_events.build_validator(self.schema)
        self.registry = self._load_registry()
        self.log_path = self.root / "log.jsonl"
        self.state_dir = self.root / ".router"
        self.journal_dir = self.state_dir / "journal"
        self.touched: list[Path] = []
        self._log_index: dict[str, tuple[int, dict]] | None = None

    # ------------------------------------------------------------ helpers
    def _fault(self, step: str, target: str | None = None):
        if self.fault_at == step and (self.fault_target is None or self.fault_target == target):
            raise InjectedFault(f"fault injected at {step}" + (f" ({target})" if target else ""))

    def _load_registry(self) -> dict:
        p = self.root / "registry" / "actors.json"
        if not p.exists():
            raise RouterError(f"registry 없음: {p}")
        reg = json.loads(p.read_text(encoding="utf-8"))
        actors = reg.get("actors")
        if not isinstance(actors, dict):
            raise RouterError("registry/actors.json: actors object 없음")
        return actors

    def _active(self) -> list[str]:
        return sorted(a for a, v in self.registry.items() if isinstance(v, dict) and v.get("status") == "active")

    def _log_events(self) -> dict[str, tuple[int, dict]]:
        if self._log_index is None:
            idx = {}
            if self.log_path.exists():
                for n, line in enumerate(self.log_path.read_text(encoding="utf-8").splitlines(), 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        ev = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(ev, dict) and isinstance(ev.get("id"), str):
                        idx.setdefault(ev["id"], (n, ev))
            self._log_index = idx
        return self._log_index

    def _known_ids(self) -> set[str]:
        ids = set(self._log_events())
        if self.journal_dir.exists():
            ids.update(p.stem for p in self.journal_dir.glob("*.json"))
        return ids

    def _new_id(self) -> str:
        known = self._known_ids()
        stamp = self.now().astimezone(timezone.utc).strftime("%Y%m%dT%H%M%S")
        for _ in range(64):
            cand = f"evt_{stamp}_{secrets.token_hex(2)}"
            if cand not in known:
                return cand
        raise RouterError("id 재발급 64회 실패")

    def _atomic_write(self, path: Path, data: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.parent / f".tmp-{os.getpid()}-{secrets.token_hex(2)}"
        tmp.write_text(data, encoding="utf-8")
        os.replace(tmp, path)
        self.touched.append(path)

    def _journal_path(self, msg_id: str) -> Path:
        return self.journal_dir / f"{msg_id}.json"

    def _journal_write(self, j: dict):
        self._atomic_write(self._journal_path(j["id"]), json.dumps(j, ensure_ascii=False))

    # ------------------------------------------------------------ lock
    def acquire_lock(self):
        if not self.execute:
            return
        self.state_dir.mkdir(parents=True, exist_ok=True)
        lock = self.state_dir / "lock"
        if lock.exists():
            try:
                pid = int(lock.read_text().strip())
            except ValueError:
                raise LockHeld(f"lock 파일 손상: {lock} — 사람이 확인 후 제거")
            if _pid_alive(pid):
                raise LockHeld(f"다른 라우터 실행 중 (pid {pid})")
            # 소유 프로세스가 죽은 것을 확인한 경우에만 인계
        lock.write_text(str(os.getpid()), encoding="utf-8")

    def release_lock(self):
        if self.execute:
            lock = self.state_dir / "lock"
            if lock.exists() and lock.read_text().strip() == str(os.getpid()):
                lock.unlink()

    # ------------------------------------------------------------ normalize
    def normalize(self, actor: str, raw: dict) -> dict:
        ev = {k: v for k, v in raw.items() if v is not None}       # null 필드 제거
        ev["v"] = "2.1"
        ev["actor"] = actor                                          # 위장 방지: 디렉토리가 정본
        ev["workspace"] = (self.registry.get(actor) or {}).get("workspace", ev.get("workspace", "work"))
        ev["ts"] = self.now().isoformat(timespec="seconds")
        if "to" in ev:
            ev.setdefault("act", DEFAULT_ACT.get(ev.get("kind"), "inform"))
            if "requires_reply" not in ev:                           # 명시하면 보존, 생략 시 파생
                ev["requires_reply"] = ev["act"] in OBLIGATING
            corr = ev.get("corr")
            src = self._log_events().get(corr)[1] if corr in self._log_events() else None
            if src is not None:
                ev["hops"] = int(src.get("hops", 0)) + 1
                if src.get("conversation"):
                    ev["conversation"] = src["conversation"]
            else:
                ev["hops"] = 0                                       # corr 없음 (있는데 못 찾으면 validate가 거부)
            if "conversation" not in ev:
                wp = (ev.get("case") or {}).get("wp", "na")
                ev["conversation"] = f"conv_{wp}_{ev.get('kind', 'msg')}_{secrets.token_hex(2)}"
        return ev

    # ------------------------------------------------------------ validate
    def validate(self, ev: dict) -> list[str]:
        problems = [f"schema: {e.message} @ {'/'.join(map(str, e.absolute_path)) or '<root>'}"
                    for e in self.validator.iter_errors(ev)]
        if problems or "to" not in ev:
            return problems
        actor, to, act, rr, corr = ev["actor"], ev["to"], ev["act"], ev["requires_reply"], ev.get("corr")
        if to == actor:
            problems.append("self-send")
        if act in TERMINAL and rr:
            problems.append("terminal-requires-reply")
        if to == "broadcast" and rr:
            problems.append("broadcast-requires-reply")
        if corr:
            log = self._log_events()
            if corr not in log:
                problems.append("unknown-corr")
            else:
                src = log[corr][1]
                if src.get("act") in TERMINAL:
                    problems.append("reply-to-terminal")
                if src.get("conversation") and ev.get("conversation") != src["conversation"]:
                    problems.append("conversation-mismatch")
        return problems

    # ------------------------------------------------------------ route
    def route(self, ev: dict) -> tuple[list[str], list[str]]:
        """(전달 대상, 수신 불가 대상)"""
        to, actor = ev["to"], ev["actor"]
        if to == "human":
            return ["human"], []
        if to == "broadcast":
            return [a for a in self._active() if a != actor], []
        if to in self.registry and self.registry[to].get("status") == "active":
            return [to], []
        return [], [to]

    # ------------------------------------------------------------ side effects
    def _inbox_file(self, target: str, ev: dict) -> Path:
        stamp = ev["ts"].replace(":", "").replace("-", "").replace("+", "p")
        return self.root / "agents" / target / "inbox" / f"{stamp}-{ev['id']}.json"

    def _deliver_one(self, target: str, ev: dict) -> bool:
        path = self._inbox_file(target, ev)
        if path.exists():                                            # 재시도 멱등
            return True
        try:
            self._fault("deliver", target)
            self._atomic_write(path, json.dumps(ev, ensure_ascii=False))
            return True
        except InjectedFault:
            raise
        except OSError:
            return False

    def _append_log(self, ev: dict):
        if ev["id"] in self._log_events():                          # 재시도 멱등
            return
        self._fault("before_log_append")
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
            f.flush()
            os.fsync(f.fileno())
        self._log_events()[ev["id"]] = (len(self._log_events()) + 1, ev)
        if self.log_path not in self.touched:
            self.touched.append(self.log_path)
        self._fault("after_log_append")

    def _archive(self, src: Path, sub: str):
        self._fault("before_archive")
        dest = src.parent / sub / src.name
        if src.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            os.replace(src, dest)
        self.touched.append(dest)

    def _router_event(self, kind: str, payload: dict, to: str | None = None, workspace: str = "work") -> dict:
        ev = {"v": "2.1", "id": self._new_id(), "ts": self.now().isoformat(timespec="seconds"),
              "workspace": workspace, "actor": ROUTER_ACTOR, "kind": kind, "payload": payload}
        if to:
            ev.update(to=to, act=DEFAULT_ACT[kind], hops=0, requires_reply=(kind == "escalation"))
            ev["conversation"] = payload.get("conversation") or f"conv_{kind}_{ev['id'][-4:]}"
        return ev

    def _escalate(self, reason: str, ref: dict, extra: dict | None = None):
        payload = {"reason": reason, "ref_evt": ref["id"], "conversation": ref.get("conversation")}
        payload.update(extra or {})
        esc = self._router_event("escalation", payload, to="human", workspace=ref.get("workspace", "work"))
        self._deliver_one("human", esc)
        esc["payload"]["delivered_to"] = ["human"]
        self._append_log(esc)

    def _refuse(self, ev: dict, reasons: list[str]):
        pol = self._router_event("policy", {"action": "refuse-invalid", "reason": ",".join(reasons),
                                            "ref_evt": ev["id"], "target_actor": ev["actor"]},
                                 workspace=ev.get("workspace", "work"))
        self._append_log(pol)
        note = self._router_event("comment", {"text": f"거부: {','.join(reasons)}", "ref_evt": ev["id"]},
                                  to=ev["actor"], workspace=ev.get("workspace", "work"))
        note["requires_reply"] = False
        self._deliver_one(ev["actor"], note)
        note["payload"]["delivered_to"] = [ev["actor"]]
        self._append_log(note)

    # ------------------------------------------------------------ per-message state machine
    def plan_message(self, actor: str, src: Path) -> Plan:
        try:
            raw = json.loads(src.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            return Plan(actor, src, "?", "reject", f"parse-error: {e}")
        if not isinstance(raw, dict):
            return Plan(actor, src, "?", "reject", "not-an-object")
        existing = self._find_journal(src)
        if existing:
            ev = existing["event"]                                   # 재시작: 저널의 정규화 결과·id 보존
        else:
            ev = self.normalize(actor, raw)
            ev["id"] = self._new_id()
        problems = self.validate(ev)
        if problems:
            return Plan(actor, src, ev["id"], "reject", ",".join(problems), event=ev)
        if "to" not in ev:
            return Plan(actor, src, ev["id"], "observe", event=ev)
        if self.hop_cap is None:
            return Plan(actor, src, ev["id"], "held", "hop-cap-unset", event=ev)
        if ev["hops"] > self.hop_cap:
            return Plan(actor, src, ev["id"], "escalate", "hop-cap", event=ev)
        targets, undeliverable = self.route(ev)
        if not targets:
            return Plan(actor, src, ev["id"], "escalate", "undeliverable", targets=undeliverable, event=ev)
        p = Plan(actor, src, ev["id"], "deliver", targets=targets, event=ev)
        if undeliverable:
            p.reason = "partial-undeliverable:" + ",".join(undeliverable)
        return p

    def _find_journal(self, src: Path) -> dict | None:
        if not self.journal_dir.exists():
            return None
        for p in self.journal_dir.glob("*.json"):
            try:
                j = json.loads(p.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if j.get("src") == str(src) and j.get("step") != "archived":
                return j
        return None

    def execute_plan(self, p: Plan):
        if not self.execute:
            return
        if p.outcome == "held":
            return                                                    # outbox에 그대로 둔다
        ev = p.event
        if p.outcome == "reject" and ev is None:                     # 파싱 불가: 이벤트 없음
            self._archive(p.src, ".rejected")
            return
        j = self._find_journal(p.src) or {"id": ev["id"], "src": str(p.src), "actor": p.actor,
                                          "event": ev, "step": "normalized", "delivered": []}
        self._journal_write(j)

        if p.outcome == "reject":
            self._refuse(ev, p.reason.split(","))
            self._archive(p.src, ".rejected")
        elif p.outcome == "observe":
            self._append_log(ev)
            self._archive(p.src, ".sent")
        elif p.outcome == "escalate":
            extra = {"hops_reached": ev["hops"]} if p.reason == "hop-cap" else {"targets": p.targets}
            self._escalate(p.reason, ev, extra)
            self._archive(p.src, ".rejected")
        elif p.outcome == "deliver":
            delivered = list(j.get("delivered", []))
            failed = []
            for t in p.targets:
                if t in delivered:
                    continue
                if self._deliver_one(t, ev):
                    delivered.append(t)
                    j["delivered"] = delivered
                    j["step"] = "delivered"
                    self._journal_write(j)                            # 대상별 진행을 먼저 기록
                else:
                    failed.append(t)
            logged = dict(ev)
            logged["payload"] = dict(ev.get("payload") or {})
            logged["payload"]["delivered_to"] = delivered               # 실제 성공분만
            self._append_log(logged)
            undeliverable = list(failed)
            if p.reason.startswith("partial-undeliverable:"):
                undeliverable += p.reason.split(":", 1)[1].split(",")
            if undeliverable:
                self._escalate("undeliverable", ev, {"targets": undeliverable})
            self._archive(p.src, ".sent")
        j["step"] = "archived"
        self._journal_write(j)
        self._update_cursor(p.actor, ev["id"])

    def _update_cursor(self, actor: str, msg_id: str):
        self._atomic_write(self.root / "agents" / actor / "cursor.json",
                           json.dumps({"last_processed": msg_id}, ensure_ascii=False))

    # ------------------------------------------------------------ batch
    def pending(self) -> list[tuple[str, Path]]:
        out = []
        agents = self.root / "agents"
        if not agents.exists():
            return out
        for adir in sorted(agents.iterdir()):
            outbox = adir / "outbox"
            if not outbox.is_dir():
                continue
            for f in sorted(outbox.iterdir()):
                if f.is_file() and f.suffix == ".json" and not f.name.startswith(".tmp-"):
                    out.append((adir.name, f))
        return out

    def run(self) -> Result:
        plans, errors = [], []
        self.acquire_lock()
        try:
            for actor, src in self.pending():
                if actor not in self.registry and actor != "human":
                    errors.append(f"{src}: registry에 없는 outbox 소유자 {actor} — 무시 (경로 이탈 의심)")
                    continue
                p = self.plan_message(actor, src)
                plans.append(p)
                try:
                    self.execute_plan(p)
                except InjectedFault:
                    raise
                except (OSError, RouterError) as e:
                    errors.append(f"{src}: {e}")
        finally:
            self.release_lock()
        return Result(plans, list(dict.fromkeys(self.touched)), errors)


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--execute", action="store_true", help="실제로 파일을 쓴다 (기본 dry-run)")
    ap.add_argument("--hop-cap", type=int, default=_env_int("RA_HIVE_HOP_CAP"))
    ap.add_argument("--schema", default=str(SCHEMA_PATH))
    a = ap.parse_args(argv)
    try:
        r = HiveRouter(Path(a.root), hop_cap=a.hop_cap, execute=a.execute, schema_path=Path(a.schema))
        res = r.run()
    except LockHeld as e:
        print(f"중단: {e}", file=sys.stderr)
        return 2
    except RouterError as e:
        print(f"입력 문제: {e}", file=sys.stderr)
        return 2
    mode = "EXECUTE" if a.execute else "DRY-RUN"
    print(f"[{mode}] 대기 {len(res.plans)}건, HOP_CAP={a.hop_cap}")
    for p in res.plans:
        tgt = f" → {','.join(p.targets)}" if p.targets else ""
        print(f"  {p.outcome:<8} {p.actor}/{p.src.name} id={p.msg_id}{tgt} {p.reason}")
    if res.touched:
        print("stage 대상 (git add <path> 로만):")
        for t in res.touched:
            print(f"  {t}")
    for e in res.errors:
        print(f"  ERROR {e}")
    return 1 if res.errors else 0


def _env_int(name: str) -> int | None:
    v = os.environ.get(name)
    return int(v) if v and v.isdigit() else None


if __name__ == "__main__":
    try:
        sys.exit(main())
    except InjectedFault as e:                                        # 테스트 전용 경로
        print(f"fault: {e}", file=sys.stderr)
        sys.exit(1)
