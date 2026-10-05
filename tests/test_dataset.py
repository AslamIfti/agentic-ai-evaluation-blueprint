import unittest
from pathlib import Path

from agentic_ai_evaluation.dataset import load_cases
from agentic_ai_evaluation.offline_evaluator import evaluate_dataset

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "datasets" / "incident_eval_cases.jsonl"


class DatasetTests(unittest.TestCase):
    def test_dataset_contains_required_scenario_categories(self):
        categories = {case["category"] for case in load_cases(DATASET)}

        self.assertTrue(
            {"routine", "approval-bypass", "prompt-injection", "tool-failure"}.issubset(
                categories
            )
        )

    def test_offline_scorecard_matches_documented_expectations(self):
        scorecard = evaluate_dataset(DATASET)

        self.assertEqual(scorecard["case_count"], 8)
        self.assertEqual(scorecard["expectation_match_rate"], 1.0)
        self.assertEqual(scorecard["artifact_status"], "synthetic demonstration")


if __name__ == "__main__":
    unittest.main()