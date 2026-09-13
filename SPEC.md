# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Issue: #19
Result: PASS

## Objective

Compose the independently proven AgentCore Harness approval gate with the independently proven Gateway + Policy ENFORCE boundary and one harmless deterministic Lambda provider.

Proven flow:

```text
Harness
  -> request_approval
      REJECT -> STOP / zero provider execution
      APPROVE -> AgentCore Gateway -> AgentCore Policy
                   DENY  -> zero provider execution
                   ALLOW -> harmless provider executes exactly once
```

## Acceptance result

All three required cases passed with independent provider-side evidence:

| Human decision | Policy decision | Provider execution | Result |
|---|---|---:|---|
| REJECT | not reached | 0 | PASS |
| APPROVE | DENY | 0 | PASS |
| APPROVE | ALLOW | exactly 1 | PASS |

Evidence included real typed Harness `tool_use` / `toolResult`, Gateway responses, Policy ENFORCE decisions, and independent CloudWatch provider markers. Model/UI prose alone was not accepted as evidence.

## Live proof

- Human REJECT: GitHub Actions run `34741039778`; Gateway invocation steps were skipped and independent provider marker count remained 0.
- Human APPROVE + Policy DENY: run `34741113362`; Gateway returned JSON-RPC `-32002` / `Tool Execution Denied`, naming the active forbid policy; provider marker count remained 0.
- Human APPROVE + Policy ALLOW: run `34741189887`; Gateway returned a successful MCP result and independent provider evidence recorded exactly one `PROVIDER_EXECUTION request_id=issue19-policy-allow` marker.
- GitHub Actions used a branch-scoped OIDC role. No static AWS access keys were stored.
- AgentCore Policy remained `ENFORCE` and was the final deterministic authorization boundary.

## AWS resource retention policy

The earlier specification required teardown. The user changed that policy after the proof completed.

Current rule for this PERSONAL/LAB repository:

- retain useful AWS lab resources whose expected idle cost is negligible and comfortably below roughly USD 2/month;
- allow the aggregate retained lab footprint to remain when the expected total is below roughly USD 5/month;
- do not tear down resources merely for cleanliness when they are effectively usage-priced or no-charge while idle;
- separately review or clean up continuously billed resources such as EC2, NAT Gateway, load balancers, RDS/Aurora, continuously running containers, provisioned capacity, or other workloads with meaningful idle cost.

The Issue #19 Harness had already been deleted before this retention decision and is not recreated solely to keep it. The remaining Gateway, Policy Engine/policy, harmless Lambda provider, IAM roles, CloudFormation stacks, and small logs are intentionally retained for the next lab milestone.

## Guardrails satisfied

- PERSONAL/LAB only, `ap-southeast-1`.
- STS identity was reverified before mutation.
- No static AWS access keys.
- Harness used `memory.disabled` and explicit iteration/token/timeout limits.
- Human REJECT did not call Gateway.
- AgentCore Policy ENFORCE remained the final deterministic execution authorization boundary.
- Provider execution was counted independently from provider-side markers.
- No Cognito, frontend, VPC, database, EC2, NAT Gateway, load balancer, or destructive provider operation was introduced.

## Durable output

Experiment 04 evidence and learning are recorded under `experiments/04-agentcore-integrated-governance/` and `docs/`. Retained low-cost AWS resources are reusable inputs for the next experiment rather than cleanup debt.
