# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Issue: #21
Result: PASS

## Objective

Reuse the retained AgentCore Gateway + Policy Engine + harmless Lambda provider and prove deterministic authorization from authenticated IAM caller identity.

Proven flow:

```text
GitHub OIDC caller A -> Gateway -> Policy -> ALLOW -> provider executes exactly once
GitHub OIDC caller B -> Gateway -> Policy -> DENY  -> provider executes zero times
```

## Acceptance result

| Caller | Policy decision | Provider execution | Result |
|---|---|---:|---|
| caller A | ALLOW | exactly 1 | PASS |
| caller B | DENY by default | 0 | PASS |

Authorization was attributable to authenticated IAM identity, not model/UI text. Provider execution was independently verified from provider-side CloudWatch markers.

## Live proof

- GitHub Actions run `34743717610` authenticated two different branch-scoped OIDC IAM roles in the same workflow.
- Caller A assumed the dedicated allow role and invoked the retained Gateway successfully.
- Caller A matched an exact Cedar permit for its assumed-role identity, the exact restored tool action, and the exact retained Gateway.
- Caller B assumed a different dedicated role and had no matching permit.
- AgentCore Policy returned JSON-RPC `-32002` with `Tool Execution Denied` and `No policy applies to the request (denied by default)` for caller B.
- AWS Core independently verified one provider marker for `issue21-caller-a` and zero provider markers for `issue21-caller-b`.
- No static AWS credentials were stored.

## Important learning

### Retained resource does not always mean retained dependency

The retained Gateway was still `READY`, but its Lambda target was absent. Before restoration:

- direct invocation of the old tool name returned `Unknown tool`;
- `tools/list` exposed only the built-in semantic-search helper;
- semantic search reported that no targets were configured.

The existing Lambda provider was still present, so the lab restored only the missing Gateway target. No new continuously billed workload was introduced.

### Semantic-search Gateway behavior

The retained Gateway uses semantic search. `tools/list` therefore exposes the built-in `x_amz_bedrock_agentcore_search` helper instead of enumerating every provider tool directly. After the target was restored, that helper resolved the real tool name used by the proof.

### Policy schema drift is detectable

The pre-existing Experiment 04 permit referenced the previous target/action and was reported by the current AgentCore policy analyzer as not matching the most recent tool input schema. The new Issue #21 caller A permit passed validation only after the current target/tool schema existed, then was tightened to the exact current action.

### Default deny is sufficient for caller B

Caller B required no explicit `forbid` rule. With Policy ENFORCE enabled and no matching permit for caller B, AgentCore denied the request by default before provider execution.

## Guardrails satisfied

- PERSONAL/LAB only in `ap-southeast-1`.
- STS identity was reverified before mutation.
- AgentCore Policy stayed in ENFORCE mode.
- Both GitHub OIDC roles trust only the exact repository identity and Issue #21 branch subject.
- Both roles can invoke only the retained Gateway required by this proof.
- No Cognito, frontend, VPC, database, EC2, NAT Gateway, load balancer, always-running container, provisioned capacity or destructive provider operation was introduced.

## Retention

Useful near-zero/usage-priced resources are intentionally retained under the lab cost rule. This includes the restored Gateway target, the caller A identity permit, and the two narrowly scoped OIDC caller roles. Continuously billed workloads still require a separate explicit decision.

## Durable output

Experiment 05 learning is recorded under `experiments/05-agentcore-identity/` and `docs/identity-aware-policy.md`, and is published through the MkDocs/GitHub Pages learning site.
