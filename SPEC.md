# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB
Issue: #19

## Objective

Compose the independently proven AgentCore Harness approval gate with the independently proven Gateway + Policy ENFORCE boundary and one harmless deterministic Lambda provider.

Target flow:

```text
Harness
  -> request_approval
      REJECT -> STOP / zero provider execution
      APPROVE -> AgentCore Gateway -> AgentCore Policy
                   DENY  -> zero provider execution
                   ALLOW -> harmless provider executes exactly once
```

## Acceptance

PASS only if independent provider-side evidence proves all three cases:

| Human decision | Policy decision | Provider execution |
|---|---|---:|
| REJECT | not reached | 0 |
| APPROVE | DENY | 0 |
| APPROVE | ALLOW | exactly 1 |

Typed Harness `tool_use` / `toolResult`, Gateway response, Policy enforcement and provider markers must be recorded. Model/UI prose alone is not evidence.

## Authorized temporary AWS scope

Issue #19 may create and delete only experiment-owned PERSONAL/LAB resources needed for the bounded proof:

- one stateless AgentCore Harness and its managed Runtime;
- one AgentCore Gateway and one Lambda-backed target;
- one Policy Engine with narrowly scoped ALLOW/DENY test policies;
- one harmless Lambda provider and its log group;
- temporary least-privilege IAM roles for Lambda, Gateway, Harness and branch-scoped GitHub OIDC caller;
- no Cognito, frontend, VPC, database, persistent application data or destructive provider operation.

Existing retained Terraform/OIDC lab resources and unrelated AgentCore resources must not be modified.

## Guardrails

- PERSONAL/LAB only, `ap-southeast-1`.
- Reverify STS identity before mutation.
- No static AWS access keys.
- Harness uses `memory.disabled` and explicit iteration/token/timeout limits.
- Human REJECT must not call Gateway.
- AgentCore Policy remains ENFORCE and is the final deterministic execution authorization boundary.
- Provider execution must be counted independently from provider-side markers.
- Tear down every Issue #19 resource and verify absence before closing.

## Durable output

Record the reproducible controller/client code and public-safe evidence under `experiments/04-agentcore-integrated-governance/`, add the learning to `docs/`, update roadmap/context, and finish through one cohesive PR.
