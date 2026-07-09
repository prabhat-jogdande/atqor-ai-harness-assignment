"""
Generate evaluation report.
"""

import json
from datetime import datetime
from pathlib import Path


def generate_report(
    total,
    passed,
    failed
):

    accuracy = round((passed / total) * 100, 2)

    report = {
        "timestamp": str(datetime.now()),
        "total_test_cases": total,
        "passed": passed,
        "failed": failed,
        "accuracy": accuracy
    }

    output = Path("evaluation/report.json")

    with open(output, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\nReport saved to {output}")