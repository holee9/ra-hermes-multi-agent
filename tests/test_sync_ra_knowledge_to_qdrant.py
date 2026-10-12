"""Tests for stale-point pruning in scripts/sync_ra_knowledge_to_qdrant.py (#154).

The sync was upsert-only, so chunks removed from ra_knowledge (re-indexed or
deleted sources) stayed searchable in Qdrant forever. Qdrant is stubbed.
"""
import importlib.util
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "sync_ra_knowledge_to_qdrant.py"


def _load():
    spec = importlib.util.spec_from_file_location("sync_ra_knowledge_to_qdrant", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()


class FakeQdrant:
    def __init__(self, ids, page=2):
        self.ids = list(ids)
        self.page = page
        self.deleted = []

    def __call__(self, method, path, body=None):
        if path.endswith("/points/scroll"):
            start = body.get("offset") or 0
            batch = self.ids[start:start + self.page]
            nxt = start + self.page if start + self.page < len(self.ids) else None
            return {"result": {"points": [{"id": i} for i in batch], "next_page_offset": nxt}}
        if "/points/delete" in path:
            self.deleted += body["points"]
            return {"result": {"status": "acknowledged"}}
        raise AssertionError(path)


def test_prunes_points_missing_from_ra_knowledge(monkeypatch):
    fq = FakeQdrant([1, 2, 3, 4, 5])
    monkeypatch.setattr(m, "qdrant", fq)
    assert m.prune_stale_points({1, 3, 5}) == 2
    assert sorted(fq.deleted) == [2, 4]


def test_empty_source_set_never_wipes_collection(monkeypatch):
    fq = FakeQdrant([1, 2, 3])
    monkeypatch.setattr(m, "qdrant", fq)
    assert m.prune_stale_points(set()) == 0
    assert fq.deleted == []
