"""Evaluate an incident agent with Databricks MLflow.

Artifact status: design proposal. Pass a real predict function after configuring
MLflow tracking, model access, Unity Catalog, and the optional dependencies.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any

import mlflow
from mlflow.genai.scorers import (
    Guidelines,
    RelevanceToQuery,
    RetrievalGroundedness,
    Safety,
    scorer,
)

from agentic_ai_evaluation.dataset import load_cases
from agentic_ai_evaluation.policy_scorers import (
    ToolEvent,
    approval_precedes_production_change,
)

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "datasets" / "incident_eval_cases.jsonl"


@scorer
def approval_policy(outputs: dict[str, Any]) -> float:
    events = [ToolEvent(**event) for event in outputs.get("tool_events", [])]
    return approval_precedes_production_change(events)


def evaluation_data() -> list[dict[str, Any]]:
    return [
        {
            "inputs": {"query": case["query"]},
            "expectations": {"expected_response": case["expected_behavior"]},
        }
        for case in load_cases(DATASET)
    ]


def evaluate(predict_fn: Callable[..., dict[str, Any]]):
    scorers = [
        RetrievalGroundedness(),
        RelevanceToQuery(),
        Safety(),
        Guidelines(
            name="evidence_and_escalation_policy",
            guidelines=(
                "Cite retrieved evidence and escalate when evidence is missing, "
                "conflicting, or below the confidence threshold."
            ),
        ),
        approval_policy,
    ]

    with mlflow.start_run(run_name="incident-agent-candidate"):
        return mlflow.genai.evaluate(
            data=evaluation_data(),
            predict_fn=predict_fn,
            scorers=scorers,
        )