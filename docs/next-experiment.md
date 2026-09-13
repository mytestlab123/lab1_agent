# Next Experiment — End-to-End Observability

Status: **NEXT**

The lab has now proven:

1. AgentCore Runtime deployment and invocation.
2. Gateway + Policy deterministic ALLOW/DENY.
3. Harness human approval with a real typed pause/resume lifecycle.
4. Integrated approval -> Gateway -> Policy -> provider governance.
5. IAM identity-aware Policy: the same Gateway/tool behaves differently for two authenticated callers.

## Next milestone

Trace one request end to end without changing the authorization model:

```text
GitHub OIDC caller
   -> AgentCore Gateway
      -> AgentCore Policy decision
         -> Lambda provider
            -> CloudWatch / AgentCore observability
```

Use one correlation/request ID and prove where it can be observed at each boundary.

## Acceptance idea

- identify the authenticated caller;
- capture the Gateway request/correlation identifier;
- capture the Policy ALLOW or DENY decision where AWS exposes it;
- correlate an ALLOW request to exactly one provider marker;
- correlate a DENY request to zero provider markers;
- prefer existing AgentCore/CloudWatch telemetry before creating new infrastructure;
- keep retained cost within the lab's low-cost boundary.

This should be Experiment 06. After that, decide whether to reintroduce Harness approval into the correlated trace or compare the proven pattern directly with SecCop.
