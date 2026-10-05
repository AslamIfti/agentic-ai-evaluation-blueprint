# Synthetic Demonstration Scorecard

**Artifact status:** Synthetic demonstration  
**Dataset:** `incident_eval_cases.jsonl`  
**Executed check:** Approval precedes every production-changing tool call

| Measure | Result |
|---|---:|
| Evaluation cases | 8 |
| Expected policy outcomes matched | 8 |
| Expectation match rate | 100% |

This result validates the deterministic scorer against intentionally designed examples. It is not a claim about production agent quality, Foundry performance, MLflow performance, or client outcomes.

## Next Evidence

1. Connect the same dataset to a Foundry agent and publish sanitized evaluator results.
2. Connect the same dataset to an MLflow-traced agent and publish a version comparison.
3. Add domain-expert reviews using `human_baseline_template.csv`.
4. Measure agreement between automated judges and the human baseline.
