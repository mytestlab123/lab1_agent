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
- Experiment 07 — full-chain auditable human approval: **PASS**

## Final governance matrix

| Human | Policy | Provider |
|---|---|---:|
| REJECT | not reached | 0 |
| APPROVE | DENY | 0 |
| APPROVE | ALLOW | exactly 1 |

Experiment 07 combines the controls proven in earlier milestones:

- real typed Harness `request_approval` pause/resume;
- authenticated GitHub OIDC IAM principal;
- AgentCore Gateway tool routing;
- deterministic AgentCore Policy ENFORCE;
- provider-side execution marker;
- native Gateway/CloudWatch audit correlation.

The central lesson is that **human approval, authentication, authorization, and execution are separate facts**. Approval does not override Cedar Policy.

See `auditable-approval.md` for the complete Experiment 07 result. Earlier pages document each control separately.
