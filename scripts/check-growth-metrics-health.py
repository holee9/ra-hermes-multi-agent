#!/usr/bin/env python3
"""
Growth Metrics System Health Check (issue #65)

Enhanced health monitoring with actionable remediation steps.
"""

import sys
import logging
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/growth-metrics-health.log'),
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger(__name__)

def check_growth_metrics_health():
    """Growth metrics 시스템 건강 상태 체크"""

    issues = []
    recommendations = []

    # 1. 최신 리포트 확인 (최근 24시간 이내)
    reports_dir = Path("reports")
    if not reports_dir.exists():
        issues.append("❌ reports 디렉토리 없음")
        recommendations.append("생성: mkdir -p reports")
        return False, recommendations

    latest_growth = list(reports_dir.glob("growth-*.json"))

    if not latest_growth:
        issues.append("❌ 성장 리포트 파일 없음")
        recommendations.append("조치: python3 scripts/growth-metrics.py 실행")
        return False, recommendations

    latest_report_path = max(latest_growth, key=lambda p: p.stat().st_mtime)

    # Check report age
    report_age = datetime.now() - datetime.fromtimestamp(latest_report_path.stat().st_mtime)
    if report_age > timedelta(hours=48):
        issues.append(f"⚠️  리포트가 오래됨 ({report_age.days}일 전)")
        recommendations.append("조치: 최신 데이터 확인 후 growth-metrics.py 재실행")

    # @MX:NOTE: timedelta exposes only days/seconds/microseconds; derive hours explicitly.
    report_age_hours = report_age.total_seconds() / 3600
    print(f"📊 최신 리포트: {latest_report_path.name} ({report_age_hours:.1f}시간 전)")

    # 2. ingestion diagnostics 체크
    try:
        with open(latest_report_path, 'r') as f:
            report = json.load(f)

        ingestion = report.get('ingestion_diagnostics', {})

        # API 상태 및 에러 분류
        api_status = ingestion.get('api_status', 'unknown')
        api_error_summary = ingestion.get('api_error_summary', {})
        api_errors = ingestion.get('api_errors', [])

        print(f"🔌 API 상태: {api_status}")

        if api_errors:
            transient_count = api_error_summary.get('transient_errors', 0)
            permanent_count = api_error_summary.get('permanent_errors', 0)

            print(f"⚠️  API 에러: {len(api_errors)}건 (일시적: {transient_count}, 영구적: {permanent_count})")

            for err in api_errors[:3]:  # 처음 3개만 표시
                method = err.get('method', 'UNKNOWN')
                path = err.get('path', 'UNKNOWN')
                error_type = err.get('error_type', 'unknown')
                attempts = err.get('attempts', 1)
                print(f"   - {method} {path} ({error_type}, 시도: {attempts})")

            # Remediation recommendations
            if permanent_count > 0:
                recommendations.append("영구적 오류: 인증 확인, API 경로 검토, Honcho 서버 상태 확인")
            if transient_count > 3:
                recommendations.append("일시적 오류: 네트워크 안정성 확인, 타임아웃 설정 검토 (GROWTH_METRICS_TIMEOUT)")

        # 데이터 품질 지표
        content_failures = ingestion.get('content_parse_failures', 0)
        messages_window = ingestion.get('messages_in_window', 0)
        expected_records = ingestion.get('expected_records_found', 0)

        print(f"📈 데이터 품질:")
        print(f"   - 메시지 윈도: {messages_window}개")
        failure_rate = content_failures/max(messages_window,1)*100 if messages_window > 0 else 0
        print(f"   - 파싱 실패: {content_failures}개 ({failure_rate:.1f}%)")
        print(f"   - 예상 레코드: {expected_records}개")

        # 건강 상태 판단 (개선됨)
        health_score = 100

        # API 상태 점수화
        if api_status == 'failed':
            health_score -= 40
            recommendations.append("긴급: Honcho API 서버 확인 (http://localhost:8000)")
        elif api_status == 'partial_failure':
            health_score -= 20

        # 파싱 실패 점수화
        if messages_window > 0:
            if failure_rate > 30:
                health_score -= 25
                recommendations.append("데이터 품질: 메시지 파싱 실패율 높음 - 포맷 검토 필요")
            elif failure_rate > 10:
                health_score -= 10

        # 데이터량 점수화
        if expected_records < 5:
            health_score -= 15
            recommendations.append("데이터량: 예상 레코드 부족 - 세션 활동 확인 필요")
        elif expected_records < 10:
            health_score -= 5

        # 건강 상태 결과
        if health_score >= 80:
            print(f"✅ 시스템 건강도: {health_score}/100 (양호)")
        elif health_score >= 60:
            print(f"⚠️  시스템 건강도: {health_score}/100 (주의 필요)")
            issues.append("시스템 건강도 저하")
        else:
            print(f"❌ 시스템 건강도: {health_score}/100 (개선 필요)")
            issues.append("시스템 건강도 저하")

    except json.JSONDecodeError as e:
        print(f"❌ 리포트 JSON 파싱 실패: {e}")
        issues.append("리포트 파일 손상")
        recommendations.append("조치: reports/ 디렉토리 내 JSON 파일 무결성 확인")
    except Exception as e:
        logger.error(f"리포트 분석 실패: {e}")
        print(f"❌ 리포트 분석 실패: {e}")
        issues.append("리포트 분석 실패")
        recommendations.append("조치: logs/growth-metrics-errors.log 확인")

    # 3. 커밋 유무 확인 (개선됨)
    try:
        result = subprocess.run(
            ['/usr/bin/git', 'status', '--short'],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=Path(__file__).parent.parent
        )
        uncommitted_files = result.stdout.strip()
        if uncommitted_files:
            print(f"⚠️  Git 커밋 미정리 파일:\n{uncommitted_files}")
            recommendations.append("버전관리: 변경 사항 커밋 권장")
        else:
            print("✅ Git 작업 디렉토리 깨끗함")
    except subprocess.TimeoutExpired:
        print("⚠️  Git 상태 확인 시간 초과")
    except FileNotFoundError:
        print("⚠️  Git 실행 파일 없음")
    except Exception as e:
        logger.debug(f"Git 상태 확인 불가: {e}")

    # 4. 로그 파일 상태 확인
    logs_dir = Path("logs")
    error_log = logs_dir / "growth-metrics-errors.log"

    if error_log.exists():
        log_size = error_log.stat().st_size / 1024  # KB
        if log_size > 100:  # 100KB 초과
            print(f"⚠️  에러 로그 파일 큼: {log_size:.1f}KB")
            recommendations.append("로그 관리: 에러 로그 파일 정리 또는 로테이션 필요")

    # 5. 최종 결과
    print(f"\n=== 건강 상태 요약 ===")
    print(f"발견된 문제: {len(issues)}건")
    print(f"제안 조치: {len(recommendations)}건")

    if recommendations:
        print(f"\n📋 권장 조치:")
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")

    return len(issues) == 0, recommendations

if __name__ == '__main__':
    print("=== Growth Metrics System Health Check ===")
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Ensure logs directory exists
    logs_dir = Path(__file__).parent.parent / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    is_healthy, recommendations = check_growth_metrics_health()

    print()
    if is_healthy:
        print("🎯 조치 필요 없음 - 시스템 정상 작동")
        sys.exit(0)
    else:
        print("🔧 조치 필요 - 위에서 확인된 문제들을 해결하세요")
        if recommendations:
            print(f"\n💡 우선순위: {recommendations[0]}")
        sys.exit(1)
