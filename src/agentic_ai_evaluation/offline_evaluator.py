"""Run deterministic policy evaluation without cloud credentials."""

from pathlib import Path
from typing import Any

from .dataset import load_cases
from .policy_scorers import ToolEvent, approval_precedes_production_change


def evaluate_dataset(path: str | Path) -> dict[str, Any]:
    """Evaluate policy behavior and return a portable scorecard."""
    results = []
    for case in load_cases(path):
        events = [ToolEvent(**event) for event in case["tool_events"]]
        actual_score = approval_precedes_production_change(events)
        results.append(
            {
                "id": case["id"],
                "category": case["category"],
                "actual_score": actual_score,
                "expected_score": case["expected_policy_score"],
                "matched_expectation": actual_score == case["expected_policy_score"],
            }
        )

    matched = sum(result["matched_expectation"] for result in results)
    return {
        "artifact_status": "synthetic demonstration",
        "case_count": len(results),
        "expectation_match_rate": matched / len(results),
        "results": results,
    }
