# Microsoft Foundry vs. Databricks MLflow

## Decision Guidance

Use **Microsoft Foundry first** when Azure is the enterprise control plane, Application Insights is the observability standard, and integrated safety evaluation, red teaming, RBAC, and Azure delivery governance are priorities.

Use **Databricks MLflow first** when the Lakehouse is central to the AI lifecycle, trace-level experiment comparison drives engineering, and custom scorers, multi-turn evaluation, and human-aligned judges are strategic requirements.

Use a **hybrid model** when agents span both ecosystems. Keep common datasets, metric definitions, release thresholds, and evidence requirements while running evaluations close to each workload.

## Microsoft Foundry Strengths

- Agent, task, tool, response-quality, RAG, and risk/safety evaluators
- Rubric evaluators tailored to agent instructions and tools
- OpenTelemetry tracing integrated with Application Insights
- Continuous evaluation and agent monitoring dashboards
- AI Red Teaming Agent for adversarial probing
- GitHub Actions and Azure DevOps evaluation integration

## Databricks MLflow Strengths

- Trace-first evaluation linked to experiments and application versions
- Built-in and custom LLM judges plus deterministic scorers
- Tool-call and multi-turn conversation evaluation
- Human-feedback alignment for eligible judges
- Configurable production-trace sampling
- Unity Catalog integration for governed trace and dataset storage

## Official References

### Microsoft

- [Evaluate your AI agents](https://learn.microsoft.com/azure/foundry/observability/how-to/evaluate-agent)
- [Observability in generative AI](https://learn.microsoft.com/azure/foundry/concepts/observability)
- [Built-in evaluators](https://learn.microsoft.com/azure/foundry/concepts/built-in-evaluators)
- [AI Red Teaming Agent](https://learn.microsoft.com/azure/foundry/concepts/ai-red-teaming-agent)

### Databricks

- [Evaluate and improve](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/)
- [Evaluate and improve an agent](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app)
- [Align LLM judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges)
- [Set up production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring)
- [Evaluate conversations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations)

Documentation reviewed October 3, 2026. Confirm preview status and regional availability before implementation.
