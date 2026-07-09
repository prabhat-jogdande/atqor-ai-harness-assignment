import json

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.harness.orchestrator.llm_client import generate_response
from src.harness.prompt_manager.prompt_builder import build_prompt
from evaluation.report_generator import generate_report

def normalize(sql: str) -> str:
    """
    Normalize SQL for comparison.
    """

    return " ".join(
        sql.lower().strip().split()
    )


# Load evaluation dataset
with open("evaluation/test_cases.json", "r") as f:
    test_cases = json.load(f)

passed = 0

print("=" * 80)
print("Evaluation Started")
print("=" * 80)

for index, test in enumerate(test_cases, start=1):

    prompt = build_prompt(test["question"])

    generated_sql = generate_response(prompt)

    expected_sql = test["expected_sql"]

    print("\nGenerated SQL:")
    print(generated_sql)

    print("\nExpected SQL:")
    print(expected_sql)

    is_match = normalize(generated_sql) == normalize(expected_sql)

    if is_match:
        passed += 1

    print(f"\nTest Case {index}")
    print("-" * 80)
    print("Question :", test["question"])
    print("Status   :", "PASS ✅" if is_match else "FAIL ❌")

accuracy = (passed / len(test_cases)) * 100

print("\n" + "=" * 80)
print(f"Accuracy : {accuracy:.2f}%")
print("=" * 80)

failed = len(test_cases) - passed

generate_report(
    total=len(test_cases),
    passed=passed,
    failed=failed
)