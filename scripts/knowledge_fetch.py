#!/usr/bin/env python3
"""
knowledge_fetch.py — Layer 4 real-time knowledge fetch
Issue: #30, #31

Queries four live sources alongside Layer 1 (Qdrant NAS):
  4a. llm-wiki      — Gitea diskstation:7001, H&abyz R&D / RA concept wiki
  4b. openFDA       — 510(k) clearance DB (ra-us / ra-eu context)
  4c. law.go.kr     — Korean medical device law text (ra-kr context)
  4d. data.go.kr    — MFDS medical device license/manufacturer DB (ra-kr context)

Usage:
  python3 knowledge_fetch.py "query string" [--profile ra-us|ra-eu|ra-kr] [--top N]

Output: JSON {"results": {"llm_wiki": [...], "openfda": [...], "law_kr": [...], "data_go_kr": [...]}}
  Each source returns [] on error — all sources are independently optional.

Environment (read from shell, inherited from .env):
  GITEA_URL         — default: http://diskstation:7001
  GITEA_TOKEN       — required for llm-wiki
  GITEA_WIKI_REPO   — default: DR_RnD/ra-llm-wiki
  OPENFDA_API_KEY   — required for openFDA
  LAW_GO_KR_OC      — required for law.go.kr (ra-kr only)
  DATA_GO_KR_API_KEY — required for data.go.kr (ra-kr only)
  LAYER4_TIMEOUT    — per-source timeout seconds (default: 8)
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

GITEA_URL = os.environ.get("GITEA_URL", "http://diskstation:7001")
GITEA_TOKEN = os.environ.get("GITEA_TOKEN", "")
GITEA_WIKI_REPO = os.environ.get("GITEA_WIKI_REPO", "DR_RnD/ra-llm-wiki")
OPENFDA_API_KEY = os.environ.get("OPENFDA_API_KEY", "")
LAW_GO_KR_OC = os.environ.get("LAW_GO_KR_OC", "")
DATA_GO_KR_API_KEY = os.environ.get("DATA_GO_KR_API_KEY", "")
TIMEOUT = int(os.environ.get("LAYER4_TIMEOUT", "8"))

# data.go.kr MFDS medical device endpoints (org code 1471000)
# Dataset 15057971: 의료기기 제조·수입업 허가정보
# Dataset 15059056: 추적관리대상 의료기기 정보
# Dataset 15057456: 의료기기 품목허가 정보 — service name unresolved, skipped
_DATA_GO_KR_BASE = "https://apis.data.go.kr/1471000"
_DATA_GO_KR_SERVICES = [
    {
        "path": "MdlpMnfcturPrmisnInfoService01/getMdlpMnfcturPrmisnList01",
        "name": "의료기기 제조·수입업 허가",
        "item_fields": ["ENTRPS", "INDUTY_TYPE", "BIZ_STTUS", "PRMISN_DT", "ADRES1"],
    },
    {
        "path": "TraceManageMdlpInfoService01/getTraceManageMdlpInfoList01",
        "name": "추적관리대상 의료기기",
        "item_fields": ["ITEM_NAME", "ITEM_SEQ", "ENTP_NAME", "PRDLST_MST_CD"],
    },
]

# H&abyz product code map for openFDA lookup
_PRODUCT_CODE_MAP = {
    "detector": ["MQB"],
    "x-ray detector": ["MQB"],
    "flat panel": ["MQB"],
    "fpd": ["MQB"],
    "hnx": ["IZL", "EAF"],
    "x-ray source": ["IZL", "EAF"],
    "handheld x-ray": ["IZL", "EAF"],
    "hnvue": ["LLZ", "QIH"],
    "software": ["LLZ", "QIH"],
    "imaging software": ["LLZ", "QIH"],
}

# Module-level cache: {repo: (file_list, fetch_time)}
_wiki_file_cache: dict = {}


def _http_get(url: str, headers: dict | None = None, timeout: int = TIMEOUT) -> bytes | None:
    """Simple GET with timeout. Returns body bytes or None on error."""
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None


def _gitea_headers() -> dict:
    return {"Authorization": f"token {GITEA_TOKEN}"} if GITEA_TOKEN else {}


def _get_wiki_files() -> list[str]:
    """Return list of wiki MD file paths from Gitea (cached per process lifetime)."""
    global _wiki_file_cache
    if GITEA_WIKI_REPO in _wiki_file_cache:
        return _wiki_file_cache[GITEA_WIKI_REPO]

    url = f"{GITEA_URL}/api/v1/repos/{GITEA_WIKI_REPO}/git/trees/HEAD?recursive=true"
    body = _http_get(url, _gitea_headers())
    if not body:
        return []
    try:
        data = json.loads(body)
        files = [
            f["path"]
            for f in data.get("tree", [])
            if f.get("type") == "blob" and f["path"].endswith(".md")
            and not f["path"].startswith(".obsidian")
        ]
        _wiki_file_cache[GITEA_WIKI_REPO] = files
        return files
    except Exception:
        return []


def _tokenize(text: str) -> set[str]:
    """Lowercase + split on non-alphanumeric. Drop short tokens."""
    tokens = re.split(r"[^a-z0-9]+", text.lower())
    return {t for t in tokens if len(t) >= 3}


def _score_file(path: str, query_tokens: set[str]) -> float:
    """Score wiki file path relevance to query. Uses stem of filename only."""
    # e.g. "wiki/concepts/iec-60601-1-3.md" → "iec 60601 1 3"
    stem = re.sub(r"\.md$", "", path.rsplit("/", 1)[-1])
    file_tokens = _tokenize(stem)
    if not file_tokens:
        return 0.0
    overlap = query_tokens & file_tokens
    return len(overlap) / len(file_tokens | query_tokens)


def _fetch_wiki_file(path: str) -> str:
    """Fetch raw file content from Gitea."""
    url = f"{GITEA_URL}/api/v1/repos/{GITEA_WIKI_REPO}/raw/{path}?ref=main"
    body = _http_get(url, _gitea_headers())
    if not body:
        return ""
    return body.decode("utf-8", errors="replace")


def fetch_llm_wiki(query: str, top: int = 3) -> list[dict]:
    """Return top N wiki articles matching query. Each item: {path, excerpt}."""
    if not GITEA_TOKEN:
        return []
    files = _get_wiki_files()
    if not files:
        return []

    query_tokens = _tokenize(query)
    if not query_tokens:
        return []

    scored = [(f, _score_file(f, query_tokens)) for f in files]
    scored.sort(key=lambda x: x[1], reverse=True)
    top_files = [(f, s) for f, s in scored if s > 0][:top]

    results = []
    for path, score in top_files:
        content = _fetch_wiki_file(path)
        if not content:
            continue
        # Extract first 600 chars of meaningful content (skip frontmatter)
        body = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)
        excerpt = body.strip()[:600]
        results.append({
            "source": "llm_wiki",
            "path": path,
            "relevance_score": round(score, 3),
            "excerpt": excerpt,
        })
    return results


def _extract_product_codes(query: str) -> list[str]:
    """Extract H&abyz product codes from query text."""
    q_lower = query.lower()
    codes: set[str] = set()

    # Explicit product code patterns (e.g., "MQB", "IZL")
    explicit = re.findall(r"\b([A-Z]{3})\b", query)
    known_codes = {"MQB", "IZL", "EAF", "LLZ", "QIH"}
    codes.update(c for c in explicit if c in known_codes)

    # Keyword → product code mapping
    for keyword, pcodes in _PRODUCT_CODE_MAP.items():
        if keyword in q_lower:
            codes.update(pcodes)

    return list(codes)


def fetch_openfda(query: str, top: int = 3) -> list[dict]:
    """Query openFDA 510(k) database for relevant clearances."""
    if not OPENFDA_API_KEY:
        return []

    product_codes = _extract_product_codes(query)
    if not product_codes:
        # Fallback: generic keyword search on device_name
        keywords = [t for t in query.split() if len(t) >= 4][:3]
        if not keywords:
            return []
        search_term = f"device_name:{urllib.parse.quote(keywords[0])}"
    else:
        search_term = f"product_code:({'+OR+'.join(product_codes)})"

    # Request recent clearances (last 5 years)
    url = (
        f"https://api.fda.gov/device/510k.json"
        f"?api_key={OPENFDA_API_KEY}"
        f"&search={search_term}"
        f"&sort=decision_date:desc"
        f"&limit={top}"
    )
    body = _http_get(url)
    if not body:
        return []
    try:
        data = json.loads(body)
        items = data.get("results", [])
    except Exception:
        return []

    results = []
    for item in items:
        results.append({
            "source": "openfda_510k",
            "k_number": item.get("k_number", ""),
            "device_name": item.get("device_name", ""),
            "applicant": item.get("applicant", ""),
            "product_code": item.get("product_code", ""),
            "decision_code": item.get("decision_code", ""),
            "decision_date": item.get("decision_date", ""),
            "summary": (
                f"{item.get('device_name','')} [{item.get('k_number','')}] "
                f"— 결정: {item.get('decision_code','')} ({item.get('decision_date','')})"
            ),
        })
    return results


def _extract_law_keywords(query: str) -> str:
    """Extract Korean law/regulation keywords for law.go.kr search.
    law.go.kr does not support multi-word phrase queries — use first keyword only.
    """
    ko_keywords = re.findall(r"[가-힯]+", query)
    if ko_keywords:
        # Use longest Korean word (most likely the domain term, e.g. '의료기기')
        return max(ko_keywords, key=len)
    return query.split()[0][:30] if query.split() else ""


def _extract_ko_keywords(query: str, max_len: int = 30) -> str:
    """Extract the longest Korean word from query for data.go.kr search."""
    ko_words = re.findall(r"[가-힯]+", query)
    if ko_words:
        return max(ko_words, key=len)[:max_len]
    return query.split()[0][:max_len] if query.split() else ""


def fetch_data_go_kr(query: str, top: int = 2) -> list[dict]:
    """Query data.go.kr MFDS medical device DBs for ra-kr context.

    Searches 2 approved services: 제조수입업 허가정보, 추적관리대상 의료기기 정보.
    """
    if not DATA_GO_KR_API_KEY:
        return []

    keyword = _extract_ko_keywords(query)
    if not keyword:
        return []

    results = []
    for svc in _DATA_GO_KR_SERVICES:
        url = (
            f"{_DATA_GO_KR_BASE}/{svc['path']}"
            f"?serviceKey={urllib.parse.quote(DATA_GO_KR_API_KEY)}"
            f"&type=json"
            f"&numOfRows={top}"
            f"&pageNo=1"
        )
        body = _http_get(url)
        if not body:
            continue
        try:
            data = json.loads(body)
            if data.get("header", {}).get("resultCode") != "00":
                continue
            items = data.get("body", {}).get("items", [])
            total = data.get("body", {}).get("totalCount", 0)
        except Exception:
            continue

        if not items:
            continue
        for item in items[:top]:
            summary_parts = [
                f"{k}: {item.get(k, '')}"
                for k in svc["item_fields"]
                if item.get(k)
            ]
            results.append({
                "source": "data_go_kr",
                "service": svc["name"],
                "total_count": total,
                "summary": " | ".join(summary_parts),
                "item": {k: item.get(k) for k in svc["item_fields"]},
            })
    return results


def fetch_law_kr(query: str, top: int = 2) -> list[dict]:
    """Query law.go.kr for Korean medical device regulation text."""
    if not LAW_GO_KR_OC:
        return []

    keywords = _extract_law_keywords(query)
    if not keywords.strip():
        return []

    # Law search API — HTTPS is blocked from T3610; use HTTP
    search_url = (
        "http://www.law.go.kr/DRF/lawSearch.do"
        f"?OC={urllib.parse.quote(LAW_GO_KR_OC)}"
        f"&target=law"
        f"&query={urllib.parse.quote(keywords)}"
        f"&type=JSON"
    )
    body = _http_get(search_url)
    if not body:
        return []
    try:
        data = json.loads(body)
        laws_raw = data.get("LawSearch", {}).get("law", [])
        if isinstance(laws_raw, dict):
            laws_raw = [laws_raw]
    except Exception:
        return []

    results = []
    for law in laws_raw[:top]:
        law_name = law.get("법령명한글", law.get("법령명", ""))
        law_id = law.get("법령ID", "")
        results.append({
            "source": "law_go_kr",
            "law_name": law_name,
            "law_id": law_id,
            "summary": f"법령: {law_name} (ID: {law_id})",
        })
    return results


def fetch_all(query: str, profile: str = "ra-us", top: int = 3) -> dict:
    """Run all applicable Layer 4 sources and return combined results."""
    wiki_results = fetch_llm_wiki(query, top=top)
    fda_results: list[dict] = []
    law_results: list[dict] = []
    data_go_kr_results: list[dict] = []

    # openFDA: relevant for FDA/MDR contexts (ra-us, ra-eu)
    if profile in ("ra-us", "ra-eu", "hermes-ra"):
        fda_results = fetch_openfda(query, top=top)

    # Korean regulatory sources: ra-kr only
    if profile == "ra-kr":
        law_results = fetch_law_kr(query, top=top)
        data_go_kr_results = fetch_data_go_kr(query, top=top)

    return {
        "results": {
            "llm_wiki": wiki_results,
            "openfda": fda_results,
            "law_kr": law_results,
            "data_go_kr": data_go_kr_results,
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Layer 4 knowledge fetch")
    parser.add_argument("query", help="Search query string")
    parser.add_argument("--profile", default="ra-us", help="RA profile: ra-us|ra-eu|ra-kr")
    parser.add_argument("--top", type=int, default=3, help="Results per source")
    args = parser.parse_args()

    result = fetch_all(args.query, args.profile, args.top)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
