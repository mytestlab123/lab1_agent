# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB

## Objective

Prove the smallest useful Amazon Bedrock AgentCore **Gateway + Policy** governance path with one harmless Lambda-backed MCP tool, and prove that a policy DENY prevents provider execution.

## Outcome

One cohesive Issue #15 PR covering:

`IAM caller -> AgentCore Gateway (MCP/AWS_IAM) -> Policy Engine (ENFORCE) -> ALLOW or DENY -> Lambda provider -> independent execution-count verification -> teardown`.

## Authorized

Amit activated this LAB milestone with `go` on 2026-09-12. Issue #15 defines the bounded mutation scope. Within this PERSONAL/LAB scope ChatGPT may:

- create/delete one dedicated Lambda function and its execution role;
- create/delete one dedicated AgentCore Gateway service role;
- create/delete one AgentCore Gateway and one Lambda target/tool;
- create/delete one AgentCore Policy Engine and bounded Cedar policies;
- create/delete one temporary GitHub OIDC caller role scoped only to the Issue #15 branch for signed Gateway test calls;
- invoke the harmless tool for ALLOW/DENY tests;
- inspect Lambda metrics/logs, Gateway/Policy state, and CloudTrail evidence;
- perform only experiment-owned cleanup.

## MUST

- Re-verify AWS caller identity and intended region before mutation.
- Use Gateway inbound `AWS_IAM`; do not use `NONE`.
- Use MCP Gateway protocol and exactly one Lambda target/tool.
- Keep the Lambda deterministic and read-only; it may only return lab status/input and write its normal execution log.
- Use Policy Engine mode `ENFORCE`.
- Establish provider execution count before and after each controlled call.
- Prove ALLOW causes provider execution and DENY does not increase provider execution count.
- Scope Gateway service role to invoke only the experiment Lambda.
- Scope temporary GitHub caller role to invoke only the experiment Gateway and trust only the exact Issue #15 branch OIDC subject.
- Use no long-lived AWS credentials.
- Keep committed evidence public-safe.
- Tear down all Issue #15 cloud resources and experiment log groups after proof.

## MUST NOT

- Modify or widen the existing main-branch GitHub OIDC/Terraform role.
- Modify the retained Terraform state bucket or SSM drift-proof parameter.
- Create AgentCore Runtime, Cognito, frontend hosting, VPC/networking, databases, or model invocation.
- Grant Lambda mutation permissions to the tool.
- Use `authorizerType=NONE`.
- Retain experiment cloud resources after acceptance unless Amit explicitly changes the decision.

## Milestones

1. Rebaseline repository docs and add `experiments/02-agentcore-gateway-policy/`.
2. Create the deterministic Lambda provider, its execution role, Gateway service role, and temporary branch-scoped caller role.
3. Create one MCP/AWS_IAM Gateway, Lambda target, and ENFORCE Policy Engine.
4. Create an ALLOW Cedar policy and prove one successful tool/provider execution.
5. Replace the effective permit with a DENY/default-deny state and prove the Gateway rejects the call while provider execution count remains unchanged.
6. Independently verify evidence, record lessons, and tear down every Issue #15 resource.

## Verification

- Gateway/Policy/Lambda resource types are available in `ap-southeast-1`.
- Gateway and target reach READY state.
- Policy Engine reaches ACTIVE and is attached to Gateway in ENFORCE mode.
- ALLOW tool call returns the Lambda response and execution count increases by exactly one controlled invocation.
- DENY call is rejected and execution count/log marker does not increase.
- Final AWS Core readback confirms experiment resources are absent after teardown.

## Stop Gates

Stop if caller identity/region differs from the intended PERSONAL/LAB target, policy/gateway is unavailable, Cedar/action naming cannot be resolved unambiguously, permissions would need broad unrelated access, or provider execution cannot be measured reliably.

## Acceptance

Return `PASS | PARTIAL | BLOCKED` with deterministic ALLOW/DENY evidence, zero provider execution on DENY, clean teardown, and one recommended next learning milestone.
