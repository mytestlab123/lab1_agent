# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Result: PASS

## Objective

Prove the smallest useful Amazon Bedrock AgentCore **Gateway + Policy** governance path with one harmless Lambda-backed MCP tool, and prove that a policy DENY prevents provider execution.

## Outcome

Issue #15 proved:

`GitHub OIDC IAM caller -> AgentCore Gateway (MCP/AWS_IAM) -> Policy Engine (ENFORCE) -> ALLOW or DENY -> Lambda provider -> independent execution-count verification -> teardown`.

## Live verification

- Gateway reached READY with MCP + AWS_IAM.
- Lambda Gateway target reached READY.
- Policy Engine reached ACTIVE and was attached in ENFORCE mode.
- Exact Cedar permit allowed the controlled tool call.
- Provider baseline count was 0.
- ALLOW returned the deterministic Lambda result and provider count became 1.
- An exact Cedar forbid then caused Gateway JSON-RPC error `-32002` (`Tool Execution Denied`).
- Provider count remained 1 and the DENY request produced zero Lambda execution markers.
- Independent AWS Core readback verified the Gateway, target, Policy Engine, active policies and execution markers.

## Policy analyzer learning

Strict Cedar validation rejected the deliberately absolute forbid as **Overly Restrictive**. Because complete denial of that exact principal/action/resource tuple was the desired negative test, the test forbid was recreated with `IGNORE_ALL_FINDINGS`. Normal policy authoring should continue to use strict validation.

## IAM learning

The custom Gateway execution role required:

- exact `lambda:InvokeFunction` permission for the experiment Lambda;
- `bedrock-agentcore:GetPolicyEngine` on the exact Policy Engine;
- `bedrock-agentcore:AuthorizeAction`;
- `bedrock-agentcore:PartiallyAuthorizeActions`.

During Gateway creation, the policy authorization permission used the narrow known Gateway-name ARN pattern because the final generated Gateway ARN did not yet exist. It was tightened to the exact Gateway ARN immediately after creation.

## Constraints satisfied

- PERSONAL/LAB identity and region reverified before mutation.
- No `NONE` authorizer; inbound authentication was AWS_IAM/SigV4.
- No static AWS access keys.
- One deterministic read-only Lambda target only.
- No AgentCore Runtime, Cognito, frontend, VPC, database or model invocation.
- Existing Terraform/OIDC retained resources were not modified.
- Unrelated pre-existing AgentCore resources were not modified.

## Cleanup

All Issue #15 resources were deleted:

- Gateway and target;
- Policy Engine and all test policies;
- Lambda and experiment log group;
- Lambda execution role;
- Gateway execution role;
- temporary branch-scoped GitHub OIDC caller role;
- temporary CloudFormation stack.

Final AWS Core readback found no Issue #15 cloud resources.

## Decisions

- AgentCore Gateway: **KEEP** as a managed MCP tool boundary.
- AgentCore Policy ENFORCE: **KEEP** as a deterministic authorization boundary.
- AWS_IAM/SigV4: **KEEP** for AWS-internal/lab callers.
- Cedar strict validation: **KEEP** for normal policies.
- Human approval: **NEXT**, implemented as orchestration above Policy rather than replacing Policy.

## Next Milestone

Experiment 03 — minimal **Human Approval Harness** demonstrating:

`ALLOW | DENY | APPROVAL_REQUIRED -> approve/reject`,

with zero provider execution on reject and AgentCore Policy remaining the final deterministic enforcement boundary.
