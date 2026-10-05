"""Load and validate portable JSONL evaluation datasets."""

import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "id",
    "category",
    "query",
    "expected_behavior",
    "tool_events",
    "expected_policy_score",
    "artifact_status",
}


def load_cases(path: str | Path) -> list[dict[str, Any]]:
    """Load JSONL cases and reject records that cannot support reproducible evaluation."""
    cases = []
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        case = json.loads(line)
        missing = REQUIRED_FIELDS.difference(case)
        if missing:
            fields = ", ".join(sorted(missing))
            raise ValueError(f"Line {line_number} is missing required fields: {fields}")
        cases.append(case)

    if not cases:
        raise ValueError("Evaluation dataset is empty")
    return cases
