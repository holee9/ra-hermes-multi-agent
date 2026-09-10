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
import errno
import importlib.util
import json
import fcntl
import os
import secrets
import stat
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
    deadlock: list[str] = field(default_factory=list)   # §7: 이 이벤트로 교착이 확정된 경우 refuse actor 목록


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
        self.errors: list[str] = []          # 처리는 계속되지만 보고해야 하는 실패 (예: 거부 알림 미전달)
        self._root_resolved = self.root.resolve()
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

    def _inside_root(self, path: Path) -> bool:
        """리뷰 P1(#151): registry 이름 확인만으로는 경로 이탈을 막지 못한다 — inbox/outbox가
        hive root 밖을 가리키는 symlink이면 root 밖에 파일이 기록됐다. 모든 쓰기·이동 대상과
        outbox 스캔 대상을 **resolve한 실제 경로**가 root 안인지로 판정한다."""
        try:
            resolved = path.resolve()
        except OSError:
            return False
        return resolved == self._root_resolved or self._root_resolved in resolved.parents

    # ---- 경계 보장 열기 (리뷰 P1 2차, #151): 검사 후 경로 교체 경쟁(TOCTOU)을 피하기 위해
    # root 디렉터리 FD에서 출발해 각 구성요소를 O_NOFOLLOW|O_DIRECTORY 로 내려가고, 최종
    # 파일도 O_NOFOLLOW 로 연다. 어느 단계든 symlink 이면 ELOOP → RouterError. 문자열 검사가
    # 아니라 실제 open 시점에 경계가 보장된다. log.jsonl · .router/ · lock · journal · inbox ·
    # outbox 이동 모두 이 경로를 쓴다.
    def _rel(self, path: Path) -> Path:
        try:
            rel = Path(path).relative_to(self.root)
        except ValueError:
            raise RouterError(f"경로 이탈 차단: {path} 는 hive root 아래가 아님")
        if any(part in ("", ".", "..") for part in rel.parts):
            raise RouterError(f"경로 이탈 차단: {path}")
        return rel

    def _dir_fd(self, rel_dir: Path, create: bool = True) -> int:
        fd = os.open(self._root_resolved, os.O_RDONLY | os.O_DIRECTORY)
        try:
            for part in rel_dir.parts:
                flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
                try:
                    st = os.lstat(part, dir_fd=fd)
                    if stat.S_ISLNK(st.st_mode):              # Linux는 O_NOFOLLOW|O_DIRECTORY에 ENOTDIR을 주므로 명시 판정
                        raise RouterError(f"경로 이탈 차단: {self.root / rel_dir} — {part} 는 symlink")
                except FileNotFoundError:
                    pass
                try:
                    nfd = os.open(part, flags, dir_fd=fd)
                except FileNotFoundError:
                    if not create:
                        raise
                    os.mkdir(part, 0o755, dir_fd=fd)
                    nfd = os.open(part, flags, dir_fd=fd)
                except OSError as e:
                    if e.errno == errno.ELOOP:                # symlink 구성요소 = 경로 이탈 시도
                        raise RouterError(f"경로 이탈 차단: {self.root / rel_dir} — {part} 는 symlink")
                    raise                                     # ENOTDIR/EACCES 등은 일반 I/O 실패 (수신 불가 처리)
                os.close(fd)
                fd = nfd
            return fd
        except BaseException:
            os.close(fd)
            raise

    def _open_file(self, path: Path, flags: int, create_dirs: bool = True) -> int:
        rel = self._rel(path)
        dfd = self._dir_fd(rel.parent, create=create_dirs)
        try:
            try:
                if stat.S_ISLNK(os.lstat(rel.name, dir_fd=dfd).st_mode):
                    raise RouterError(f"경로 이탈 차단: {path} 는 symlink")
            except FileNotFoundError:
                pass
            return os.open(rel.name, flags | os.O_NOFOLLOW, 0o644, dir_fd=dfd)
        except OSError as e:
            if e.errno == errno.ELOOP:
                raise RouterError(f"경로 이탈 차단: {path} 는 symlink")
            raise
        finally:
            os.close(dfd)

    def _atomic_write(self, path: Path, data: str):
        rel = self._rel(path)
        dfd = self._dir_fd(rel.parent)
        try:
            tmp = f".tmp-{os.getpid()}-{secrets.token_hex(2)}"
            fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dfd)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(data)
            os.rename(tmp, rel.name, src_dir_fd=dfd, dst_dir_fd=dfd)   # 대상이 symlink이면 링크 자체가 교체됨
        finally:
            os.close(dfd)
        self.touched.append(path)

    def _journal_path(self, msg_id: str) -> Path:
        return self.journal_dir / f"{msg_id}.json"

    def _journal_write(self, j: dict):
        self._atomic_write(self._journal_path(j["id"]), json.dumps(j, ensure_ascii=False))

    # ------------------------------------------------------------ lock
    def acquire_lock(self):
        """단일 실행 lock — OS 파일 잠금(flock)으로 원자적으로 획득한다.

        리뷰 P1(#151): exists()→write_text() 두 단계는 동시에 시작한 두 프로세스가 모두
        통과할 수 있었다. flock은 커널이 단일 소유자를 보장하고, 소유 프로세스가 죽으면
        자동 해제되므로 pid 생사 판정이나 lock 파일 삭제가 필요 없다. 파일 내용(pid)은
        진단용일 뿐 잠금의 근거가 아니다.
        """
        if not self.execute:
            return
        lock = self.state_dir / "lock"
        fd = self._open_file(lock, os.O_CREAT | os.O_RDWR)           # .router/ 및 lock 모두 NOFOLLOW
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            holder = ""
            try:
                holder = os.read(fd, 64).decode(errors="replace").strip()
            except OSError:
                pass
            os.close(fd)
            raise LockHeld(f"다른 라우터 실행 중 (lock 보유자 pid {holder or '?'})")
        os.ftruncate(fd, 0)
        os.write(fd, str(os.getpid()).encode())
        self._lock_fd = fd

    def release_lock(self):
        fd = getattr(self, "_lock_fd", None)
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)
                self._lock_fd = None

    # ------------------------------------------------------------ normalize
    def normalize(self, actor: str, raw: dict) -> dict:
        ev = {k: v for k, v in raw.items() if v is not None}       # null 필드 제거
        ev["v"] = "2.1"
        ev["actor"] = actor                                          # 위장 방지: 디렉토리가 정본
        ev["workspace"] = (self.registry.get(actor) or {}).get("workspace", ev.get("workspace", "work"))
        ev["ts"] = self.now().isoformat(timespec="seconds")
        if "to" in ev:
            # 리뷰 P1(#151): raw 필드 타입은 아직 검증 전이다 — kind={} / act=[] / corr=7 /
            # case="x" 같은 입력이 여기서 TypeError로 run 전체를 죽이지 않도록 타입을 보호하고,
            # 잘못된 값은 그대로 두어 validate()의 스키마 검사가 거부하게 한다.
            kind = ev.get("kind")
            if "act" not in ev:
                ev["act"] = DEFAULT_ACT.get(kind, "inform") if isinstance(kind, str) else "inform"
            act = ev.get("act")
            if "requires_reply" not in ev:                           # 명시하면 보존, 생략 시 파생
                ev["requires_reply"] = isinstance(act, str) and act in OBLIGATING
            corr = ev.get("corr")
            src = self._log_events()[corr][1] if isinstance(corr, str) and corr in self._log_events() else None
            if src is not None:
                try:
                    ev["hops"] = int(src.get("hops", 0)) + 1
                except (TypeError, ValueError):
                    ev["hops"] = 0
                if src.get("conversation"):
                    ev["conversation"] = src["conversation"]
            else:
                ev["hops"] = 0                                       # corr 없음 (있는데 못 찾으면 validate가 거부)
            if "conversation" not in ev:
                case = ev.get("case")
                wp = case.get("wp", "na") if isinstance(case, dict) else "na"
                kind_slug = kind if isinstance(kind, str) else "msg"
                ev["conversation"] = f"conv_{wp}_{kind_slug}_{secrets.token_hex(2)}"
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
        self._fault("before_log_append", ev.get("kind"))
        fd = self._open_file(self.log_path, os.O_WRONLY | os.O_APPEND | os.O_CREAT)
        with os.fdopen(fd, "a", encoding="utf-8") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
            f.flush()
            os.fsync(f.fileno())
        self._log_events()[ev["id"]] = (len(self._log_events()) + 1, ev)
        if self.log_path not in self.touched:
            self.touched.append(self.log_path)
        self._fault("after_log_append", ev.get("kind"))

    def _archive(self, src: Path, sub: str):
        self._fault("before_archive")
        self._move(src, src.parent / sub / src.name)

    def _move(self, src: Path, dest: Path):
        rel_src, rel_dest = self._rel(src), self._rel(dest)
        sdfd = self._dir_fd(rel_src.parent, create=False)
        try:
            try:
                st = os.lstat(rel_src.name, dir_fd=sdfd)
            except FileNotFoundError:
                st = None                                             # 이미 옮겨짐 (재시작)
            if st is not None:
                if stat.S_ISLNK(st.st_mode):
                    raise RouterError(f"경로 이탈 차단: {src} 는 symlink")
                ddfd = self._dir_fd(rel_dest.parent)
                try:
                    os.rename(rel_src.name, rel_dest.name, src_dir_fd=sdfd, dst_dir_fd=ddfd)
                finally:
                    os.close(ddfd)
        finally:
            os.close(sdfd)
        self.touched.append(dest)

    def _router_event(self, kind: str, payload: dict, to: str | None = None, workspace: str = "work") -> dict:
        ev = {"v": "2.1", "id": self._new_id(), "ts": self.now().isoformat(timespec="seconds"),
              "workspace": workspace, "actor": ROUTER_ACTOR, "kind": kind, "payload": payload}
        if to:
            ev.update(to=to, act=DEFAULT_ACT[kind], hops=0, requires_reply=(kind == "escalation"))
            ev["conversation"] = payload.get("conversation") or f"conv_{kind}_{ev['id'][-4:]}"
        return ev

    def _derived(self, j: dict, key: str, make) -> dict:
        """저널에 파생 이벤트(policy/comment/escalation)를 한 번만 만들어 보관한다.

        리뷰 P1(#151): 재시작마다 새 id를 발급하면 log에 policy/comment가 2세트씩 쌓였다.
        파생 이벤트의 id·내용을 저널에 고정해 두면 _append_log(id 멱등)·_deliver_one(inbox
        파일명 멱등)이 재실행에서도 한 번만 효력을 낸다.
        """
        derived = j.setdefault("derived", {})
        if key not in derived:
            derived[key] = make()
            self._journal_write(j)
        return derived[key]

    def _escalate(self, reason: str, ref: dict, extra: dict | None, j: dict, key: str = "escalation") -> None:
        """사람 inbox에 escalation을 기록한다. 기록에 실패하면 RouterError —
        호출자는 원본을 archive하지 않고 outbox에 남겨 다음 실행에서 재시도한다.
        리뷰 P1(#151): 이전에는 반환값을 무시하고 delivered_to=["human"]로 기록했다."""
        def make():
            payload = {"reason": reason, "ref_evt": ref["id"], "conversation": ref.get("conversation")}
            payload.update(extra or {})
            return self._router_event("escalation", payload, to="human", workspace=ref.get("workspace", "work"))
        esc = self._derived(j, key, make)
        if "delivered_to" not in esc["payload"]:
            if not self._deliver_one("human", esc):
                raise RouterError(f"human inbox 기록 실패 — escalation({reason}) for {ref['id']} 미전달, 원본 보류")
            esc["payload"]["delivered_to"] = ["human"]
            self._journal_write(j)                                    # 결과 고정 후 append
        self._append_log(esc)

    def _refuse(self, ev: dict, reasons: list[str], j: dict) -> None:
        pol = self._derived(j, "refuse_policy", lambda: self._router_event(
            "policy", {"action": "refuse-invalid", "reason": ",".join(reasons),
                       "ref_evt": ev["id"], "target_actor": ev["actor"]},
            workspace=ev.get("workspace", "work")))
        self._append_log(pol)

        def make_note():
            note = self._router_event("comment", {"text": f"거부: {','.join(reasons)}", "ref_evt": ev["id"]},
                                      to=ev["actor"], workspace=ev.get("workspace", "work"))
            note["requires_reply"] = False
            return note
        note = self._derived(j, "refuse_notice", make_note)
        # 리뷰 5차(#151): 알림 전달 결과도 저널에 먼저 고정한다. append 뒤·원본 finalizing 전에 죽으면
        # 재실행이 알림을 다시 전달하고(inbox 복구 시) id 멱등 append는 새 결과를 버려 감사가 어긋났다.
        # delivered_to가 이미 고정돼 있으면 재전달하지 않는다 — 실패 알림도 그대로 실패로 남긴다.
        if "delivered_to" not in note["payload"]:
            delivered = self._deliver_one(ev["actor"], note)
            note["payload"]["delivered_to"] = [ev["actor"]] if delivered else []     # 실제 결과만 기록
            self._journal_write(j)
            if not delivered:
                self.errors.append(f"{ev['actor']} inbox 기록 실패 — 거부 알림 {note['id']} 미전달 (거부 자체는 log에 기록됨)")
        self._append_log(note)

    # ------------------------------------------------------------ §7 거절 교착
    def _conv_state(self, conv: str) -> tuple[bool, set[str]]:
        """(사람 응답 전 보류 중인가, 지금까지 refuse한 서로 다른 actor).

        log.jsonl 순서대로: act:refuse의 actor를 모으고, refuse-deadlock escalation이 기록되면
        보류 상태로 들어간다. 그 뒤 같은 conversation에 human 이벤트가 기록되면 보류를 풀고
        refuse 집계를 초기화한다(사람 판단이 스레드를 재개시킨 것으로 본다)."""
        held, refusers = False, set()
        for _, ev in sorted(self._log_events().values(), key=lambda t: t[0]):
            if ev.get("conversation") != conv and (ev.get("payload") or {}).get("conversation") != conv:
                continue
            if ev.get("actor") == "human":
                held, refusers = False, set()
            elif ev.get("kind") == "escalation" and (ev.get("payload") or {}).get("reason") == "refuse-deadlock":
                held = True
            elif ev.get("act") == "refuse" and isinstance(ev.get("actor"), str):
                refusers.add(ev["actor"])
        return held, refusers

    def _release_held(self):
        """사람 응답으로 보류가 풀린 conversation의 `.held/` 메시지를 outbox로 되돌린다 (이번 배치에서 처리)."""
        agents = self.root / "agents"
        if not agents.exists():
            return
        for adir in sorted(agents.iterdir()):
            held_dir = adir / "outbox" / ".held"
            if not held_dir.is_dir() or not self._inside_root(held_dir):
                continue
            for f in sorted(held_dir.glob("*.json")):
                try:
                    raw = json.loads(f.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    continue
                conv = raw.get("conversation") if isinstance(raw, dict) else None
                if not isinstance(conv, str) and isinstance(raw, dict):
                    corr = raw.get("corr")                            # 보류 원본이 corr만 가진 경우
                    if isinstance(corr, str) and corr in self._log_events():
                        conv = self._log_events()[corr][1].get("conversation")
                if isinstance(conv, str) and not self._conv_state(conv)[0]:
                    self._move(f, adir / "outbox" / f.name)
                    self.touched.append(adir / "outbox" / f.name)

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
        deadlock: list[str] = []
        conv = ev.get("conversation")
        if isinstance(conv, str):
            held, refusers = self._conv_state(conv)
            if held and actor != "human":                            # 사람 메시지가 보류를 푸는 응답이다
                return Plan(actor, src, ev["id"], "held", "refuse-deadlock", event=ev)
            if ev.get("act") == "refuse" and refusers - {actor}:
                deadlock = sorted(refusers | {actor})                  # 서로 다른 두 actor의 refuse
        if self.hop_cap is None:
            return Plan(actor, src, ev["id"], "held", "hop-cap-unset", event=ev)
        if ev["hops"] > self.hop_cap:
            return Plan(actor, src, ev["id"], "escalate", "hop-cap", event=ev)
        targets, undeliverable = self.route(ev)
        if not targets:
            return Plan(actor, src, ev["id"], "escalate", "undeliverable", targets=undeliverable, event=ev)
        p = Plan(actor, src, ev["id"], "deliver", targets=targets, event=ev, deadlock=deadlock)
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
        ev = p.event
        if p.outcome == "reject" and ev is None:                     # 파싱 불가: 이벤트 없음
            self._archive(p.src, ".rejected")
            return
        # 리뷰 3·5차(#151): 감사 로그가 이미 확정된(finalizing/audited) 메시지는 route/deliver를
        # 다시 돌리지 않는다 — 확정 뒤 복구된 대상에 새로 전달하면 log와 실제 전달이 어긋난다.
        # 확정 저널은 held(hop_cap 미설정) 재평가보다 먼저 본다: 신규 전달만 보류하고, 이미 확정된
        # 것의 append/archive/cursor 마무리는 cap 설정과 무관하게 끝낸다.
        j = self._find_journal(p.src)
        if j and j.get("step") in ("finalizing", "audited"):
            p.reason = f"resumed-from-journal:{j['step']}"
            self._complete_from_journal(j, p.src)
            return
        if p.outcome == "held":
            if p.reason == "refuse-deadlock":
                self._archive(p.src, ".held")                         # §7: 사람 응답까지 보류
            return                                                    # hop-cap 미설정: outbox에 그대로 둔다
        j = j or {"id": ev["id"], "src": str(p.src), "actor": p.actor,
                  "event": ev, "step": "normalized", "delivered": []}
        self._journal_write(j)

        if p.outcome == "reject":
            self._refuse(ev, p.reason.split(","), j)                 # policy/notice는 derived로 멱등
            self._finalize(j, ".rejected", None)
            self._archive(p.src, ".rejected")
        elif p.outcome == "observe":
            self._finalize(j, ".sent", ev)
            self._archive(p.src, ".sent")
        elif p.outcome == "escalate":
            extra = {"hops_reached": ev["hops"]} if p.reason == "hop-cap" else {"targets": p.targets}
            self._escalate(p.reason, ev, extra, j)                    # 실패 시 RouterError → archive 안 함
            self._finalize(j, ".rejected", None)
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
            undeliverable = list(failed)
            if p.reason.startswith("partial-undeliverable:"):
                undeliverable += p.reason.split(":", 1)[1].split(",")
            j["undeliverable"] = undeliverable
            self._journal_write(j)
            if undeliverable:
                # 실패 시 RouterError: 원본은 outbox에 남고 log에는 아직 아무것도 없다. 다음 실행은
                # inbox 파일명 멱등성으로 성공분을 중복 기록하지 않은 채 실패분 전달과 escalation을
                # 재시도한다 (복구되면 escalation 없이 완결).
                self._escalate("undeliverable", ev, {"targets": undeliverable}, j, key="escalation_undeliverable")
            # 리뷰 P1 2차(#151): log 항목은 **모든 대상이 전달 또는 human escalation으로 확정된 뒤**
            # 한 번만 쓴다. 먼저 쓰면 복구 후 재실행의 실제 전달 결과가 감사 로그에 반영되지 않았다.
            logged = dict(ev)
            logged["payload"] = dict(ev.get("payload") or {})
            logged["payload"]["delivered_to"] = delivered               # 최종 확정된 성공분
            if undeliverable:
                logged["payload"]["undeliverable"] = undeliverable      # 사람에게 넘어간 대상
            # 리뷰 4차(#151): append 뒤 저널 확정까지의 창에서 죽으면 재시작이 route를 다시
            # 평가했다. 최종 결정과 기록할 이벤트를 저널에 먼저 영속(finalizing)하고, 그 다음
            # 멱등 append → audited → archive → cursor 순서로만 진행한다.
            if p.deadlock:                                            # §7: 두 번째 서로 다른 actor의 refuse
                self._escalate("refuse-deadlock", ev, {"refusers": p.deadlock}, j, key="deadlock")
            self._finalize(j, ".sent", logged, delivered=delivered, undeliverable=undeliverable)
            self._archive(p.src, ".sent")
        self._fault("before_cursor")
        self._update_cursor(p.actor, ev["id"])
        j["step"] = "archived"
        self._journal_write(j)

    def _finalize(self, j: dict, archive_sub: str, final_event: dict | None, **final):
        """최종 결정을 저널에 먼저 영속(step=finalizing)한 뒤 멱등 append → step=audited.

        리뷰 3·4차(#151): 어느 지점에서 죽어도 재시작은 저널의 final만 보고 완결한다 — route/
        deliver/escalate를 다시 평가하지 않는다. final_event가 None이면 기록할 원본 이벤트가
        없는 경로(reject/escalate: 파생 이벤트는 derived{}로 이미 멱등)다."""
        if j.get("step") not in ("finalizing", "audited"):
            j["step"] = "finalizing"
            j["final"] = {"archive": archive_sub, "event": final_event, **final}
            self._journal_write(j)
        if j["final"].get("event"):
            self._append_log(j["final"]["event"])                     # id 멱등
        if j["step"] != "audited":
            j["step"] = "audited"
            self._journal_write(j)

    def _complete_from_journal(self, j: dict, src: Path | None):
        """finalizing/audited 저널을 route 평가 없이 완결한다 (재시작·orphan 스윕 공용)."""
        final = j.get("final") or {}
        if final.get("event"):
            self._append_log(final["event"])
        if j["step"] != "audited":
            j["step"] = "audited"
            self._journal_write(j)
        if src is not None:
            self._archive(src, final.get("archive", ".sent"))
        self._fault("before_cursor")
        self._update_cursor(j["actor"], j["id"])
        j["step"] = "archived"
        self._journal_write(j)

    def _sweep_orphans(self):
        """outbox 파일은 이미 옮겨졌는데 cursor/archived 전에 죽은 저널(orphan)을 완결한다."""
        if not self.journal_dir.exists():
            return
        for jp in sorted(self.journal_dir.glob("*.json")):
            try:
                j = json.loads(jp.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if j.get("step") not in ("finalizing", "audited"):
                continue
            src = Path(j.get("src", ""))
            if src.exists():
                continue                                              # pending()이 정상 경로로 처리
            self._complete_from_journal(j, None)

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
            if not self._inside_root(adir) or not self._inside_root(outbox):
                self.errors.append(f"{outbox}: hive root 밖을 가리키는 outbox — 무시 (경로 이탈)")
                continue
            for f in sorted(outbox.iterdir()):
                if f.is_file() and f.suffix == ".json" and not f.name.startswith(".tmp-"):
                    if not self._inside_root(f):
                        self.errors.append(f"{f}: hive root 밖을 가리키는 outbox 파일 — 무시")
                        continue
                    out.append((adir.name, f))
        return out

    def run(self) -> Result:
        plans, errors = [], self.errors
        self.acquire_lock()
        try:
            if self.execute:
                try:
                    self._sweep_orphans()
                except InjectedFault:
                    raise
                except (OSError, RouterError) as e:
                    errors.append(f"orphan journal 완결 실패: {e}")
            if self.execute:
                self._release_held()
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
