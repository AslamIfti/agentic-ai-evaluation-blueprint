# Evaluation Lifecycle

## Control Plane

The evaluation contract is platform neutral. Foundry and MLflow execute platform-specific evaluators, then publish normalized evidence into one governance scorecard.

```mermaid
sequenceDiagram
    participant E as Evaluation Dataset
    participant A as Candidate Agent
    participant T as Trace Store
    participant D as Deterministic Scorers
    participant J as LLM Judges
    participant H as Human Reviewers
    participant G as Release Gate

    E->>A: Run versioned cases
    A->>T: Emit retrieval, memory, tool, and response spans
    T->>D: Validate policy and tool sequence
    T->>J: Evaluate task, retrieval, quality, and safety
    T->>H: Sample high-risk and disagreement cases
    D->>G: Publish deterministic results
    J->>G: Publish judge results and rationale
    H->>G: Publish human baseline
    G-->>A: Approve or reject candidate version
```

## Required Trace Fields

- Session, request, agent, model, prompt, tool, and dataset versions
- Retrieval query, returned evidence, graph path, and authorization context
- Agent handoffs, memory reads and writes, and tool arguments
- Approval state before production-changing actions
- Latency, token use, retries, errors, and final outcome
- Automated scores, judge rationale, human feedback, and release decision

## Release Decision

A release gate must fail when a critical deterministic policy fails, even if aggregate LLM-judge quality improves. Quality thresholds should be segmented by risk and use case rather than hidden in one average score.
