"""Generate an offline scorecard for the synthetic incident dataset."""

import json
from pathlib import Path

from agentic_ai_evaluation.offline_evaluator import evaluate_dataset

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "datasets" / "incident_eval_cases.jsonl"


if __name__ == "__main__":
    print(json.dumps(evaluate_dataset(DATASET), indent=2))
