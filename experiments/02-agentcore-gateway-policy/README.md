# Experiment 02 — AgentCore Gateway + Policy

Status: **PASS**

## Objective

Prove that Amazon Bedrock AgentCore Gateway + Policy can make a deterministic tool authorization decision **before** a provider executes.

Critical property:

> A denied tool call must produce **zero provider executions**.

## Architecture

```text
GitHub Actions
  -> temporary branch-scoped OIDC caller
  -> SigV4
  -> AgentCore Gateway (MCP, AWS_IAM)
  -> Policy Engine (ENFORCE)
     -> ALLOW -> Lambda provider
     -> DENY  -> stop before Lambda
```

## Provider

The Lambda target is intentionally boring. It:

- accepts a correlation `request_id`;
- writes one `PROVIDER_EXECUTION` marker to its normal log;
- returns a deterministic read-only JSON result;
- has no permissions to mutate other AWS services.

That log marker is the independent execution counter.

## Result

Controlled evidence:

| Point | Provider execution count |
|---|---:|
| Baseline | 0 |
| After ALLOW | 1 |
| After DENY | 1 |

The ALLOW request produced exactly one `allow-issue15` marker. The DENY request returned JSON-RPC error `-32002` (`Tool Execution Denied`) and produced **zero** `deny-issue15` markers.

## Policy behavior

The permit policy matched the exact IAM role principal, exact generated tool action, and exact Gateway resource.

A second explicit `forbid` rule for the same combination was intentionally absolute. AgentCore's strict Cedar analyzer flagged it as **Overly Restrictive** and refused creation. For this negative test only, the exact rule was recreated with `IGNORE_ALL_FINDINGS`; it then became ACTIVE and overrode the permit as expected.

This is an important distinction:

- production policy authoring should normally keep strict validation;
- a deliberately total DENY used to prove enforcement can legitimately trigger the analyzer's restrictive-policy finding.

## IAM learning

The custom Gateway execution role required:

- `lambda:InvokeFunction` on the exact Lambda;
- `bedrock-agentcore:GetPolicyEngine` on the exact Policy Engine;
- `bedrock-agentcore:AuthorizeAction` for policy evaluation;
- `bedrock-agentcore:PartiallyAuthorizeActions` for Gateway/Policy evaluation.

During Gateway creation, the authorization permission also had to cover the future Gateway ARN. The bootstrap policy used the narrow resource-name pattern necessary for creation, then was tightened to the exact Gateway ARN after creation.

## Authentication

Inbound Gateway auth used **AWS_IAM**. The test caller was a temporary GitHub Actions OIDC role trusted only for the experiment branch and used SigV4 service name `bedrock-agentcore`.

No static AWS access keys were created.

## Cleanup

All experiment-owned cloud resources were removed after verification:

- Gateway and Lambda target;
- Policy Engine and policies;
- Lambda and its log group;
- Lambda execution role;
- Gateway execution role;
- temporary branch-scoped GitHub OIDC caller role;
- temporary CloudFormation stack.

Unrelated existing AgentCore resources and the retained Terraform/OIDC lab resources were not modified.

## Files

- `lambda_function.py` — deterministic read-only provider.
- `invoke_gateway.py` — SigV4 MCP `tools/call` client.
- `test_invoke_gateway.py` — response-classification regression tests.
- `LEARNINGS.md` — concise conclusions and architecture decisions.
- `SOURCE.md` — upstream AWS documentation used for the experiment.

## Next milestone

Build a minimal **Human Approval Harness** that represents:

```text
ALLOW | DENY | APPROVAL_REQUIRED
```

AgentCore Policy remains the deterministic final enforcement boundary; approval is orchestration above it.
