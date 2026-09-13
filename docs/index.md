# AWS and AgentCore Hands-on Lab

Public learning notes from small, verified AWS and Amazon Bedrock AgentCore experiments.

## Current status

- MkDocs Material build: **PASS**
- GitHub Pages deployment: **LIVE**
- Experiment 01 — AgentCore Runtime: **PASS**
- Experiment 02 — Gateway + Policy ALLOW/DENY: **PASS**
- Experiment 03 — Harness human approval: **PASS**
- Experiment 04 — integrated approval + Gateway + Policy: **PASS**
- Experiment 05 — IAM identity-aware Policy: **PASS**
- Experiment 06 — native observability correlation: **PASS**

## Governance results

Experiment 04 proved the human-approval governance chain:

- Human REJECT -> provider executions = 0.
- Human APPROVE + Policy DENY -> provider executions = 0.
- Human APPROVE + Policy ALLOW -> provider executions = exactly 1.

Experiment 05 then proved authenticated identity matters independently of the requested tool:

- caller A -> exact Cedar permit -> provider executions = exactly 1;
- caller B -> no matching permit -> default Policy DENY -> provider executions = 0.

Experiment 06 made those decisions operationally explainable after the fact:

- native Gateway logs correlate request ID, trace ID, IAM principal and Policy decision;
- ALLOW correlates to tool execution and exactly one provider marker;
- DENY records the principal and denial reason with no downstream provider execution;
- the ALLOW Lambda X-Ray report carries the same trace identity as the Gateway record.

See `integrated-governance.md`, `identity-aware-policy.md` and `observability-trace.md` for the verified evidence and implementation learning.
