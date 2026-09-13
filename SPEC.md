# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Issue: #25
Result: PASS

## Objective

Prove one auditable governance chain using the independently verified AgentCore controls:

```text
Human decision
 -> Harness typed approval
 -> authenticated IAM caller
 -> AgentCore Gateway
 -> AgentCore Policy ENFORCE
 -> harmless provider
 -> native audit evidence
```

## Acceptance result

| Case | Human | Policy | Provider | Result |
|---|---|---|---:|---|
| REJECT | REJECTED | not reached | 0 | PASS |
| APPROVE + DENY | APPROVED | DENY by default | 0 | PASS |
| APPROVE + ALLOW | APPROVED | ALLOW | exactly 1 | PASS |

## Live proof

- A retained Harness `lab1i25approval` ran with stateless memory and explicit iteration/token/timeout limits.
- Per-invocation overrides used Nova 2 Lite and one client-side `request_approval` inline function.
- Every case produced `stopReason=tool_use`, exactly one typed `request_approval`, matching same-session `toolResult`, and a successful resumed turn.
- `issue25-human-reject` stopped at the controller boundary; exact Gateway and provider log inspection found zero matching downstream events.
- GitHub Actions run `34748226633` executed only the two approved Gateway cases under the existing narrow Issue #21 OIDC caller roles.
- `issue25-approve-deny` correlated to caller B, Policy default DENY, no `Executing tool` event, and provider count 0.
- `issue25-approve-allow` correlated to caller A, Policy ALLOW, the determining Cedar policy, tool execution, and exactly one provider marker.

## Guardrails satisfied

- PERSONAL/LAB only in `ap-southeast-1`.
- STS identity reverified before AWS mutation.
- No static AWS credentials.
- Existing OIDC trust was not widened for this proof.
- AgentCore Policy remained `ENFORCE` and the final deterministic execution boundary.
- Human REJECT stopped before Gateway.
- Human APPROVE did not bypass Policy.
- Provider execution was independently verified from provider-side logs.
- No EC2, NAT Gateway, load balancer, RDS/Aurora, VPC, frontend, Cognito, always-running container or provisioned capacity was introduced.

## Retention

The Experiment 07 Harness and previously retained Gateway, Policy, Lambda, caller roles and observability resources remain because they are low-cost/usage-priced and within the lab retention rule.

## Durable output

Experiment 07 evidence is stored under `experiments/07-agentcore-auditable-approval/` and published through the MkDocs learning site.

## Next

Do not add AgentCore features by default. Compare this proven governance chain with SecCop and select one practical adoption milestone.
