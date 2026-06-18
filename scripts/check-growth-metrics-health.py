#!/usr/bin/env python3
"""
Growth Metrics Error Handling Improvement (issue #65)

Enhanced error handling and logging for growth-metrics.py
"""

import sys
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/growth-metrics-errors.log'),
        logging.StreamHandler(sys.stderr)
    ]
)

def check_growth_metrics_health():
    """Growth metrics 시스템 건강 상태 체크"""

    issues = []

    # 1. 최신 리포트 확인
    reports_dir = Path("reports")
    latest_growth = list(reports_dir.glob("growth-*.json"))

    if not latest_growth:
        issues.append("❌ 성장 리포트 파일 없음")
        return False

    latest_report = max(latest_growth, key=lambda p: p.stat().st_mtime)

    print(f"📊 최신 리포트: {latest_report.name}")

    # 2. ingestion diagnostics 체크
    try:
        import json
        with open(latest_report, 'r') as f:
            report = json.load(f)

        ingestion = report.get('ingestion_diagnostics', {})

        # API 상태
        api_status = ingestion.get('api_status', 'unknown')
        print(f"🔌 API 상태: {api_status}")

        # 에러 체크
        api_errors = ingestion.get('api_errors', [])
        if api_errors:
            print(f"⚠️  API 에러: {len(api_errors)}건")
            for err in api_errors[:3]:  # 처음 3개만 표시
                print(f"   - {err.get('method', 'UNKNOWN')} {err.get('path', 'UNKNOWN')}")

        # 데이터 품질 지표
        content_failures = ingestion.get('content_parse_failures', 0)
        messages_window = ingestion.get('messages_in_window', 0)
        expected_records = ingestion.get('expected_records_found', 0)

        print(f"📈 데이터 품질:")
        print(f"   - 메시지 윈도: {messages_window}개")
        print(f"   - 파싱 실패: {content_failures}개 ({content_failures/max(messages_window,1)*100:.1f}%)")
        print(f"   - 예상 레코드: {expected_records}개")

        # 건강 상태 판단
        health_score = 100
        if api_status != 'ok':
            health_score -= 30
        if content_failures > messages_window * 0.5:
            health_score -= 20
        if expected_records < 10:
            health_score -= 10

        if health_score >= 80:
            print(f"✅ 시스템 건강도: {health_score}/100 (양호)")
        elif health_score >= 60:
            print(f"⚠️  시스템 건강도: {health_score}/100 (주의 필요)")
        else:
            print(f"❌ 시스템 건강도: {health_score}/100 (개선 필요)")
            issues.append("시스템 건강도 저하")

    except Exception as e:
        print(f"❌ 리포트 분석 실패: {e}")
        issues.append("리포트 분석 실패")

    # 3. 커밋 유무 확인
    import subprocess
    try:
        result = subprocess.run(['git', 'status', '--short'],
                              capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print(f"⚠️  Git 커밋 미정리 파일 있음")
    except:
        pass

    return len(issues) == 0

if __name__ == '__main__':
    print("=== Growth Metrics System Health Check ===")
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    is_healthy = check_growth_metrics_health()

    print()
    if is_healthy:
        print("🎯 조치 필요 없음 - 시스템 정상 작동")
        sys.exit(0)
    else:
        print("🔧 조치 필요 - 위에서 확인된 문제들을 해결하세요")
        sys.exit(1)
