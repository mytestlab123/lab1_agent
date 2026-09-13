# Integrated Governance — Experiment 04

Status: **PASS**

Experiment 04 combined Harness approval, AgentCore Gateway, AgentCore Policy ENFORCE, and one harmless Lambda-backed provider.

## Results

| Human decision | Policy decision | Provider execution |
|---|---|---:|
| REJECT | not reached | 0 |
| APPROVE | DENY | 0 |
| APPROVE | ALLOW | exactly 1 |

Evidence:

- Run `34741039778`: real Harness approval pause; REJECT path; Gateway not called; provider count 0.
- Run `34741113362`: APPROVE path; Gateway returned `-32002 Tool Execution Denied`; provider count 0.
- Run `34741189887`: APPROVE path; Policy ALLOW; provider returned success; independent log marker count exactly 1.

The successful provider marker was:

`PROVIDER_EXECUTION request_id=issue19-policy-allow`

## Main learning

Human approval and deterministic authorization are separate controls. Approval decides whether a request proceeds. AgentCore Policy remains the final authorization boundary before provider execution.

Negative tests were verified from provider-side logs rather than inferred from model text or UI messages.

## Retained resources

The lab now keeps useful resources with negligible idle cost instead of deleting them automatically. The remaining Gateway, Policy Engine/policy, Lambda provider, IAM roles, CloudFormation stacks, and small logs are intentionally retained for reuse. The Harness had already been deleted before this policy changed and is not recreated only for retention.

Continuously billed resources such as EC2, NAT Gateway, load balancers, RDS/Aurora, always-running containers, or provisioned capacity still require an explicit cost decision.

## Next

Reuse the retained Gateway/Policy/Lambda path for an identity/context-aware authorization experiment, then add end-to-end observability and trace correlation.
