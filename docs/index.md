# AWS and AgentCore Hands-on Lab

Public learning notes from small AWS and Amazon Bedrock AgentCore experiments.

## Start here: use AgentCore without a product GUI

[Three deployed Harness examples: prompts and Console/CLI steps](harness-examples.md)

Try **lab1_demo_reader** first for a real AWS read, **lab1_demo_explainer** for pasted findings, and **lab1_demo_approval** for typed approval practice without remediation.

[Actual test results](harness-examples-results.md): all three API/terminal cases PASS; authenticated Console GUI is explicitly NOT_TESTED.

## Earlier learning

- [Runtime](runtime.md): direct-code deployment and IAM/SigV4.
- [Gateway and Policy](gateway-policy.md): deterministic ALLOW/DENY.
- [Harness approval](harness-approval.md): typed pause/resume.
- [Integrated governance](integrated-governance.md): approval and Policy are separate gates.
- [Identity-aware Policy](identity-aware-policy.md): authenticated caller A/B outcomes.
- [Observability](observability-trace.md): request, principal, Policy and provider evidence.
- [Auditable approval](auditable-approval.md): correlated controlled lab flow.

Historical PASS labels describe the bounded experiment evidence, not universal production readiness. See each experiment's scope and source notes. The operator approval example is a simulation, not a durable human authorization system.
