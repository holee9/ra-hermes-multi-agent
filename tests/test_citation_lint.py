"""Unit tests for scripts/ra_citation_lint.py — the #134 code-level regulatory
citation linter (option B).

Reproduction-first (repo Rule 4): every "must flag" case below is a real defect
observed in the 2026-07-18/07-19 ra_eu batches (#123/#132/#134). Every "must NOT
flag" case is a legitimate citation the linter must leave alone (false-positive
guard) — a linter that blocks correct advisory is worse than none.

Two check tiers:
  C1 = nonexistent article sub-paragraph  (deterministic, zero-FP, severity=error)
  C2 = subject<->citation same-kind mismatch (curated gold, severity=warning)
"""
import importlib.util
from pathlib import Path

_MOD = Path(__file__).resolve().parent.parent / "scripts" / "ra_citation_lint.py"


def _load():
    spec = importlib.util.spec_from_file_location("ra_citation_lint", _MOD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()


def _codes(flags):
    return {f["check"] for f in flags}


def _has(flags, check, needle):
    return any(f["check"] == check and needle.lower() in f["message"].lower() for f in flags)


# ── C1: nonexistent article sub-paragraph ─────────────────────────────────

def test_c1_flags_art86_1_d_nonexistent():
    # #133/#134: Art.86(1) has (a)(b)(c) only. (d)/(e) do not exist.
    flags = m.lint_citations("PMCF results are reported under Art.86(1)(d) of the MDR.")
    assert m.SEV_ERROR in {f["severity"] for f in flags}
    assert _has(flags, "C1", "86(1)")


def test_c1_flags_art86_1_e_nonexistent():
    flags = m.lint_citations("Corrective actions go in Art. 86(1)(e).")
    assert _has(flags, "C1", "86(1)")


def test_c1_allows_existing_art86_1_c():
    # (c) is real — must not flag.
    flags = m.lint_citations("Sales volume is Art.86(1)(c).")
    assert not any(f["check"] == "C1" for f in flags)


def test_c1_ignores_articles_not_in_registry():
    # Art.10(4) not in the structural registry — C1 stays silent (no false error).
    flags = m.lint_citations("See Art.10(4)(z) for details.")
    assert not any(f["check"] == "C1" for f in flags)


# ── shipped API: lint_citations() runs C1 only ────────────────────────────

def test_lint_citations_ships_c1_only_not_c2():
    # A text with a clear C2-style subject/citation mismatch must NOT emit a
    # C2 flag from the shipped entrypoint (C2 is a documented negative result,
    # not wired in). The C1 error in the same text still fires.
    flags = m.lint_citations("PMCF is Art.86(1)(d) and the SSCP is Art. 66.")
    assert any(f["check"] == "C1" and f["severity"] == m.SEV_ERROR for f in flags)
    assert not any(f["check"] == "C2" for f in flags)


def test_lint_returns_list_of_dicts_with_required_keys():
    flags = m.lint_citations("Reported under Art.86(1)(d).")
    assert isinstance(flags, list)
    for f in flags:
        assert {"check", "severity", "message", "span"} <= set(f)
        assert f["severity"] in (m.SEV_ERROR, m.SEV_WARNING)


def test_clean_text_returns_no_flags():
    flags = m.lint_citations("This device is Class IIa; the conformity route is Annex IX.")
    assert flags == []


def test_empty_text_safe():
    assert m.lint_citations("") == []
    assert m.lint_citations(None) == []


def test_has_error_helper():
    assert m.has_error(m.lint_citations("Art.86(1)(d)")) is True
    assert m.has_error(m.lint_citations("Art.86(1)(c)")) is False


# ── C2 experimental (documented negative result) — behaviour on clean input ─
# These lock the experimental function's logic on single-clause prose so the
# design is recoverable; they intentionally do NOT run through lint_citations
# (C2 is not shipped — proven high-FP on real table/list-dense advisory text).

def test_c2_experimental_flags_sscp_wrong_article():
    flags = m.lint_subject_citation_experimental("The SSCP is prepared per MDR Art. 66.")
    assert _has(flags, "C2", "32")


def test_c2_experimental_flags_doc_wrong_article():
    flags = m.lint_subject_citation_experimental("The EU declaration of conformity is issued under Art. 37.")
    assert _has(flags, "C2", "19")


def test_c2_experimental_allows_doc_annex_iv():
    flags = m.lint_subject_citation_experimental("The EU declaration of conformity follows Annex IV.")
    assert not flags


def test_c2_experimental_flags_cer_annex_iv_confusion():
    flags = m.lint_subject_citation_experimental("The Clinical Evaluation Report is structured per Annex IV.")
    assert _has(flags, "C2", "XIV")


def test_c2_experimental_allows_correct_cer():
    flags = m.lint_subject_citation_experimental("The Clinical Evaluation Report is Annex XIV Part A.")
    assert not flags


def test_c2_experimental_allows_different_kind_nearby():
    flags = m.lint_subject_citation_experimental("The PMCF is addressed in the PMS plan under Art. 84.")
    assert not flags


def test_c2_experimental_empty_safe():
    assert m.lint_subject_citation_experimental("") == []
    assert m.lint_subject_citation_experimental(None) == []
