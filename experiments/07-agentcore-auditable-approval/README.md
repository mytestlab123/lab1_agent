# Experiment 07 — Full-Chain Auditable Human Approval

Status: **PASS**  
Issue: #25

## Goal

Compose the independently proven Harness approval gate with the retained identity-aware Gateway + Policy + provider path and the native observability added in Experiment 06.

```text
Human decision
  -> AgentCore Harness approval gate
     -> authenticated IAM caller
        -> AgentCore Gateway
           -> AgentCore Policy ENFORCE
              -> harmless Lambda provider
                 -> CloudWatch audit evidence
```

## Result

| Case | Harness decision | Policy | Provider | Result |
|---|---|---|---:|---|
| human reject | REJECTED | not reached | 0 | PASS |
| approve + deny | APPROVED | DENY by default | 0 | PASS |
| approve + allow | APPROVED | ALLOW | exactly 1 | PASS |

## Harness evidence

A small retained Harness named `lab1i25approval` was created with explicit iteration/token/timeout limits and stateless memory.

The live proof used per-invocation overrides for:

- `global.amazon.nova-2-lite-v1:0`;
- one client-side `inline_function` named `request_approval`;
- `allowedTools=["*"]`;
- a system prompt that requires the approval tool and forbids real action.

All three cases produced a real typed boundary:

```text
messageStop.stopReason = tool_use
tool name = request_approval
same runtimeSessionId resumed with matching toolUseId
second turn stopReason = end_turn
```

Correlation IDs:

- `issue25-human-reject`
- `issue25-approve-deny`
- `issue25-approve-allow`

The rejected case ended after the Harness resume and was intentionally not sent to Gateway.

## Approved Gateway proof

GitHub Actions run `34748226633` reused the already-proven narrow Issue #21 OIDC identities rather than widening trust:

- caller B handled `issue25-approve-deny`;
- caller A handled `issue25-approve-allow`.

Both invoked the same retained Gateway and same harmless tool.

### APPROVE + DENY

The Gateway returned JSON-RPC `-32002` / `Tool Execution Denied`.

Native Gateway application logs correlated the request to one trace and recorded:

- the caller-B IAM principal;
- Policy decision `DENY`;
- reason: no matching policy, therefore default deny;
- no `Executing tool` event.

Independent provider-log inspection found zero matching execution markers.

### APPROVE + ALLOW

The Gateway returned a successful MCP result.

Native Gateway application logs correlated the request to one trace and recorded:

- the caller-A IAM principal;
- Policy decision `ALLOW`;
- the determining Cedar policy;
- `Executing tool`;
- successful request completion.

The Lambda provider emitted exactly one marker:

```text
PROVIDER_EXECUTION request_id=issue25-approve-allow
```

## REJECT proof

After the real Harness `REJECTED` resume, the controller did not perform a Gateway invocation for `issue25-human-reject`.

Independent inspection of both the Gateway application-log group and provider log group found no event containing that correlation ID.

This proves the approval gate stopped the flow before the deterministic authorization/execution boundary.

## Important architecture lesson

The Harness approval and Gateway call are intentionally separated by a controller boundary:

```text
Harness says APPROVED
  != provider may execute

Controller continues
  -> authenticated IAM principal
     -> Gateway
        -> Policy still decides
```

Human approval does not override Cedar. `APPROVED + DENY` still produced provider execution 0.

Likewise, model prose is not treated as approval evidence. The acceptance signal is the typed Harness `tool_use` / `toolResult` lifecycle.

## Retention

The Harness is retained because it is a low-cost/usage-priced lab resource and the user explicitly prefers retaining useful resources below the lab cost threshold. The existing Gateway, Policy Engine, provider, OIDC roles and observability resources remain unchanged.

No EC2, NAT Gateway, load balancer, database, VPC, continuously running container or provisioned capacity was added.

## Next

Experiment 07 completes the planned AgentCore governance learning chain. The next work should compare this proven pattern with SecCop and select one practical adoption milestone rather than adding AgentCore features for their own sake.
