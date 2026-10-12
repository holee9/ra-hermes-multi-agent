"""Tests for change-aware re-indexing in scripts/index_github_repos.py (#154).

Reproduces the defect where a source already present in ra_knowledge was
skipped forever, so upstream corrections (e.g. MD-process audit #957 on
DR-07) never reached the agents. No network, DB, or GX10 is touched: every
I/O function is stubbed.
"""
import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "index_github_repos.py"


def _load():
    spec = importlib.util.spec_from_file_location("index_github_repos", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()

REPO = "holee9/MD-process"
PATH = "02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md"
SRC = f"github:{REPO}/{PATH}"
OLD = "# 매트릭스\n\n| DR-07 | 임상적 유효성(해당 시) | 법 제15조 | ◐ |\n" * 3
NEW = "# 매트릭스\n\n| DR-07 | 임상적 유효성(해당 시) | 해석범위(제9조 또는 제10조) | ◐ |\n" * 3


class FakeDB:
    def __init__(self):
        self.rows = {}  # source_path -> {"blob_sha": str|None, "chunks": [str]}
        self.calls = []

    def state(self, source_path):
        return self.rows.get(source_path)

    def delete(self, source_path):
        self.calls.append(("delete", source_path))
        self.rows.pop(source_path, None)

    def upsert(self, points):
        self.calls.append(("upsert", len(points)))
        for p in points:
            r = self.rows.setdefault(p["source_path"], {"blob_sha": None, "chunks": []})
            r["chunks"].append(p["content"])
            r["blob_sha"] = p["metadata"].get("blob_sha")

    def set_blob_sha(self, source_path, blob_sha):
        self.calls.append(("backfill", source_path))
        self.rows[source_path]["blob_sha"] = blob_sha

    def sources(self, prefix):
        return [s for s in self.rows if s.startswith(prefix)]


@pytest.fixture
def env(monkeypatch):
    db = FakeDB()
    content = {"value": NEW}
    embeds = []
    monkeypatch.setattr(m, "pgvector_source_state", db.state, raising=False)
    monkeypatch.setattr(m, "pgvector_delete_by_source", db.delete)
    monkeypatch.setattr(m, "pgvector_upsert", db.upsert)
    monkeypatch.setattr(m, "pgvector_set_blob_sha", db.set_blob_sha, raising=False)
    monkeypatch.setattr(m, "pgvector_sources_with_prefix", db.sources, raising=False)
    monkeypatch.setattr(m, "fetch_file_content", lambda repo, path: content["value"])

    def fake_embed(text):
        embeds.append(text)
        return [0.0]

    monkeypatch.setattr(m, "embed_text", fake_embed)
    return db, content, embeds


def test_changed_source_is_reindexed(env):
    """#154 reproduction: a stale row with a different blob sha must be replaced."""
    db, _, embeds = env
    db.rows[SRC] = {"blob_sha": "oldsha", "chunks": m.chunk_markdown(OLD)}
    added = m.index_file(REPO, PATH, blob_sha="newsha")
    assert added > 0
    assert ("delete", SRC) in db.calls
    assert all("법 제15조" not in c for c in db.rows[SRC]["chunks"])
    assert db.rows[SRC]["blob_sha"] == "newsha"
    assert embeds


def test_unchanged_source_is_skipped_without_fetch(env, monkeypatch):
    db, _, embeds = env
    db.rows[SRC] = {"blob_sha": "same", "chunks": m.chunk_markdown(NEW)}
    monkeypatch.setattr(m, "fetch_file_content", lambda *a: pytest.fail("must not fetch"))
    assert m.index_file(REPO, PATH, blob_sha="same") == -1
    assert not embeds and not db.calls


def test_legacy_row_identical_content_backfills_without_embedding(env):
    db, _, embeds = env
    db.rows[SRC] = {"blob_sha": None, "chunks": m.chunk_markdown(NEW)}
    assert m.index_file(REPO, PATH, blob_sha="sha1") == -1
    assert db.calls == [("backfill", SRC)]
    assert db.rows[SRC]["blob_sha"] == "sha1"
    assert not embeds


def test_legacy_row_changed_content_is_reindexed(env):
    db, _, embeds = env
    db.rows[SRC] = {"blob_sha": None, "chunks": m.chunk_markdown(OLD)}
    assert m.index_file(REPO, PATH, blob_sha="sha1") > 0
    assert all("법 제15조" not in c for c in db.rows[SRC]["chunks"])
    assert embeds


def test_new_source_is_indexed(env):
    db, _, _ = env
    assert m.index_file(REPO, PATH, blob_sha="sha1") > 0
    assert db.rows[SRC]["blob_sha"] == "sha1"


def test_orphan_sources_removed_only_with_nonempty_listing(env):
    db, _, _ = env
    gone = f"github:{REPO}/deleted.md"
    db.rows[gone] = {"blob_sha": "x", "chunks": ["a"]}
    db.rows[SRC] = {"blob_sha": "y", "chunks": ["b"]}
    assert m.remove_orphan_sources(REPO, []) == 0  # empty listing = fetch failure, never wipe
    assert gone in db.rows
    assert m.remove_orphan_sources(REPO, [PATH]) == 1
    assert gone not in db.rows and SRC in db.rows
