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
- Experiment 05 proved IAM identity-aware AgentCore Policy: caller A -> ALLOW -> exactly one provider execution; caller B -> default DENY -> zero provider executions.
- Experiment 06 is active: correlate caller identity -> Gateway -> Policy -> provider using native AgentCore/CloudWatch observability where possible.
- GitHub Pages is live through MkDocs Material at `https://mytestlab123.github.io/lab1_agent/`.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged.

## Retained AWS Lab Resources

Useful resources with negligible idle cost are intentionally retained for reuse.

Current reusable AgentCore path includes:

- AgentCore Gateway with Policy ENFORCE;
- Lambda-backed Gateway target used by Experiment 05;
- AgentCore Policy Engine, the earlier Experiment 04 policy, and the exact Experiment 05 caller A permit;
- harmless Lambda provider + small CloudWatch log footprint;
- narrowly scoped GitHub OIDC IAM caller roles for the identity proof;
- CloudFormation stacks used to provision the retained low-cost resources.

The Experiment 04 Harness had already been deleted before the retention-policy change and is not recreated only for retention.

Cost rule: retain effectively idle/usage-priced resources when expected cost remains comfortably below about USD 2/month per item and below roughly USD 5/month for the retained lab footprint. Review continuously billed resources separately; do not leave EC2, NAT Gateway, load balancers, RDS/Aurora, always-running containers, provisioned capacity, or similar cost-bearing workloads without an explicit reason.

## Documentation

- MkDocs Material build/deploy: PASS.
- GitHub Pages: live.
- Experiments 01-05 are documented as verified learning milestones.

## Active Work

- Issue #23: Experiment 06 end-to-end observability and trace correlation.
- Branch: `issue-23-observability-trace`.

## Next Action

1. Inspect current native Gateway/Policy observability state and enable only what is required.
2. Execute one ALLOW and one DENY request with unique correlation IDs.
3. Correlate identity, Gateway, Policy decision and provider evidence.
4. Publish Experiment 06 learning and close through one reviewed PR.
