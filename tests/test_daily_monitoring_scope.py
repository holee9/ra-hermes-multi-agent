"""#141 — 일일 점검의 NORMAL 문구가 점검 범위를 넘어 단정하던 문제.

스크립트가 보는 것은 Honcho/PostgreSQL/Redis/deriver/성장 리포트/스케줄러뿐이고
메일 유입·mail-triage 처리 경로는 **한 건도 검사하지 않는다**. 그런데 FAIL=0 이면
"All critical systems operational" 이라고 적어 메일이 처리되고 있다는 뜻으로 읽혔다.
스크립트를 실행하지 않고 소스 계약만 검사한다(운영 접속 없음).
"""
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "daily-monitoring.sh"
SRC = SCRIPT.read_text(encoding="utf-8")


def test_script_really_has_no_mail_path_check():
    """전제 확인 — 메일 점검이 실제로 없다. 생기면 이 테스트가 먼저 깨져 문구를 재검토하게 된다."""
    lowered = SRC.lower()
    checks = [l for l in SRC.splitlines() if "check_pass" in l or "check_fail" in l or "check_warn" in l]
    mail_checks = [l for l in checks if any(k in l.lower() for k in ("mail", "메일", "triage", "n8n"))]
    assert mail_checks == [], f"메일 점검이 추가됐다 — 판정 문구를 다시 보라: {mail_checks}"
    assert "honcho" in lowered and "redis" in lowered          # 인프라 점검은 존재


# 주석이 아니라 **실제 출력 줄**만 본다 — 주석의 설명 문구가 단언을 깨는 일을 막는다.
EMITTED = "\n".join(l for l in SRC.splitlines()
                    if ">> \"$CHECKLIST_FILE\"" in l and not l.strip().startswith("#"))


def test_normal_verdict_is_scoped_not_absolute():
    assert "All critical systems operational" not in EMITTED, "점검 범위를 넘는 단정이 출력된다"
    assert "인프라 점검 범위" in EMITTED, "판정이 점검 범위로 한정되지 않았다"


def test_unverified_scope_is_stated():
    assert "확인하지 않은 것" in EMITTED, "검사하지 않은 범위를 명시하지 않는다"
    assert "증거가 아니다" in EMITTED, "메일 처리 증거가 아님을 밝히지 않는다"


def test_warnings_appear_in_verdict():
    """경고가 있는데 판정에 아무 표시가 없으면 없는 것처럼 읽힌다."""
    assert "경고 ${WARN}" in EMITTED, "WARN 이 판정 문구에 반영되지 않는다"


def test_failure_verdicts_unchanged():
    """반대편 보존: 실패 판정 문구는 건드리지 않았다."""
    assert "🟡 **ATTENTION**" in EMITTED and "🔴 **CRITICAL**" in EMITTED
