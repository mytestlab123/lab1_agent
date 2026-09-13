# AWS and AgentCore Hands-on Lab

Public learning notes from small, verified AWS and Amazon Bedrock AgentCore experiments.

## Current status

- MkDocs Material build: **PASS**
- GitHub Pages deployment: **LIVE**
- Experiment 01 — AgentCore Runtime: **PASS**
- Experiment 02 — Gateway + Policy ALLOW/DENY: **PASS**
- Experiment 03 — Harness human approval: **PASS**
- Experiment 04 — integrated approval + Gateway + Policy: **PASS**

## Core governance result

Experiment 04 proved all three required outcomes with independent provider evidence:

- Human REJECT -> provider executions = 0.
- Human APPROVE + Policy DENY -> provider executions = 0.
- Human APPROVE + Policy ALLOW -> provider executions = exactly 1.

See `integrated-governance.md` for the full Experiment 04 result and retained-resource policy.
