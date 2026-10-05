"""Submit the incident dataset to a Microsoft Foundry agent evaluation.

Artifact status: design proposal. Cloud execution requires a Foundry project,
deployed agent, generated rubric evaluator, RBAC, and the optional dependencies.
"""

import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import TestingCriterionAzureAIEvaluator
from azure.identity import DefaultAzureCredential
from openai.types.eval_create_params import DataSourceConfigCustom

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "datasets" / "incident_eval_cases.jsonl"


def required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Set {name} before running the Foundry evaluation")
    return value


def main() -> None:
    endpoint = required_setting("AZURE_AI_PROJECT_ENDPOINT")
    model_deployment = required_setting("AZURE_AI_MODEL_DEPLOYMENT_NAME")
    agent_name = required_setting("FOUNDRY_AGENT_NAME")
    rubric_name = required_setting("FOUNDRY_RUBRIC_EVALUATOR")

    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
    openai_client = project_client.get_openai_client()
    dataset = project_client.datasets.upload_file(
        name="incident-agent-evaluation",
        version="1",
        file_path=str(DATASET),
    )

    testing_criteria = [
        TestingCriterionAzureAIEvaluator(
            type="azure_ai_evaluator",
            name="Incident Agent Rubric",
            evaluator_name=rubric_name,
            initialization_parameters={"deployment_name": model_deployment},
            data_mapping={
                "query": "{{item.query}}",
                "response": "{{sample.output_items}}",
            },
        ),
        TestingCriterionAzureAIEvaluator(
            type="azure_ai_evaluator",
            name="Coherence",
            evaluator_name="builtin.coherence",
            initialization_parameters={"deployment_name": model_deployment},
            data_mapping={
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        ),
        TestingCriterionAzureAIEvaluator(
            type="azure_ai_evaluator",
            name="Violence",
            evaluator_name="builtin.violence",
            data_mapping={
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        ),
    ]

    evaluation = openai_client.evals.create(
        name="Incident Agent Quality",
        data_source_config=DataSourceConfigCustom(
            type="custom",
            item_schema={
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
            include_sample_schema=True,
        ),
        testing_criteria=testing_criteria,
    )

    evaluation_run = openai_client.evals.runs.create(
        eval_id=evaluation.id,
        name="Incident Agent Candidate",
        data_source={
            "type": "azure_ai_target_completions",
            "source": {"type": "file_id", "id": dataset.id},
            "input_messages": {
                "type": "template",
                "template": [
                    {
                        "type": "message",
                        "role": "user",
                        "content": {
                            "type": "input_text",
                            "text": "{{item.query}}",
                        },
                    }
                ],
            },
            "target": {"type": "azure_ai_agent", "name": agent_name},
        },
    )
    print(f"Evaluation run started: {evaluation_run.id}")


if __name__ == "__main__":
    main()
