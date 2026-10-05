# Project Instructions

- [x] Clarify project requirements: Python portfolio package for Agentic AI evaluation.
- [x] Scaffold the project with source, tests, datasets, platform adapters, documentation, and CI.
- [x] Customize the project for Microsoft Foundry and Databricks MLflow comparison.
- [x] Install required VS Code Python and Python Environments extensions.
- [x] Compile and validate the project.
- [x] Provide a repeatable test and demo workflow.
- [x] Complete README and repository documentation.

## Engineering Rules

- Keep platform-neutral policy logic under `src/agentic_ai_evaluation`.
- Keep cloud SDK dependencies optional so offline tests require no credentials.
- Label artifacts as `executed`, `synthetic demonstration`, or `design proposal`.
- Never commit credentials, client data, production traces, or sensitive identifiers.
- Use the same versioned evaluation cases across Foundry and MLflow comparisons.
- Add tests for every deterministic scorer and critical release policy.
- Treat LLM-judge output as evidence that requires calibration against human review.
