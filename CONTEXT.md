# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws` (read as reusable AWS knowledge source)
- Context: PERSONAL
- Environment: LAB

## Current Truth

- This repository is public and unarchived.
- Cross-session AWS Core/GitHub knowledge reuse is proven.
- Public-safe GitHub OIDC -> Terraform -> AWS deploy/drift/reconciliation is proven.
- Pull-request Terraform validation is AWS-free and uses a committed provider lockfile.
- Experiment 01 proved AgentCore Runtime direct-code Python deployment with IAM/SigV4 invocation.
- Experiment 02 proved AgentCore Gateway + Policy ENFORCE with one Lambda-backed MCP tool: ALLOW executed once; DENY added zero provider executions.
- Experiment 03 proved AgentCore Harness human approval with a real typed `request_approval` `tool_use` pause and same-session REJECTED/APPROVED resume paths.
- Experiment 04 proved the complete governance chain: human REJECT -> zero provider executions; human APPROVE + Policy DENY -> zero provider executions; human APPROVE + Policy ALLOW -> exactly one provider execution.
- GitHub Pages is live through MkDocs Material at `https://mytestlab123.github.io/lab1_agent/`.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged.

## Retained Issue #19 AWS Lab Resources

The cleanup policy changed after the proof completed. Useful resources with negligible idle cost are intentionally retained for reuse rather than deleted.

Currently retained from Experiment 04 include:

- AgentCore Gateway + Lambda target;
- AgentCore Policy Engine + exact permit policy;
- harmless Lambda provider + small CloudWatch log footprint;
- temporary/lab IAM roles and CloudFormation stacks used to provision those resources.

The Experiment 04 Harness had already been deleted before the retention-policy change and is not recreated just for retention.

Cost rule: retain effectively idle/usage-priced resources when expected cost remains comfortably below about USD 2/month per item and below roughly USD 5/month for the retained lab footprint. Review continuously billed resources separately; do not leave EC2, NAT Gateway, load balancers, RDS/Aurora, always-running containers, provisioned capacity, or similar cost-bearing workloads without an explicit reason.

## Documentation

- MkDocs Material build: PASS.
- GitHub Pages deployment: PASS and live.
- Experiment 04 learning is being added in Issue #19 finalization.

## Active Work

- Issue #19: final documentation/PR closeout for Experiment 04.

## Next Action

1. Merge Experiment 04 evidence/docs and close Issue #19.
2. Reuse the retained Gateway/Policy/Lambda path for the next bounded learning milestone.
3. Next recommended experiment: add identity/context-aware authorization, then trace the decision end to end.
