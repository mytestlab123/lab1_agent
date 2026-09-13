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

## Governance results

Experiment 04 proved the human-approval governance chain:

- Human REJECT -> provider executions = 0.
- Human APPROVE + Policy DENY -> provider executions = 0.
- Human APPROVE + Policy ALLOW -> provider executions = exactly 1.

Experiment 05 then proved authenticated identity matters independently of the requested tool:

- caller A -> exact Cedar permit -> provider executions = exactly 1;
- caller B -> no matching permit -> default Policy DENY -> provider executions = 0.

See `integrated-governance.md` and `identity-aware-policy.md` for the verified evidence and implementation learning.
