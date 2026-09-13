# Next Experiment — SecCop Adoption Comparison

Status: **NEXT**

The AgentCore learning chain has now proven:

1. Runtime deployment and invocation.
2. Gateway tool exposure.
3. deterministic Policy ALLOW/DENY.
4. typed Harness human approval.
5. integrated approval + Policy governance.
6. authenticated IAM identity-aware authorization.
7. native request/trace/Policy/provider audit correlation.
8. one full auditable chain where REJECT stops before Gateway, APPROVE+DENY stops before provider, and APPROVE+ALLOW executes exactly once.

## Next milestone

Do not add another AgentCore service merely to extend the lab. Compare the proven controls directly with SecCop and select one adoption milestone.

Suggested comparison:

| Control | Proven AgentCore mechanism | SecCop equivalent / gap |
|---|---|---|
| Human approval | Harness typed `request_approval` + controller | map current approval UI/controller |
| Authenticated principal | GitHub OIDC IAM caller | identify execution identity |
| Tool routing | AgentCore Gateway | map current AWS action/tool layer |
| Deterministic authorization | AgentCore Policy ENFORCE | identify current hard enforcement boundary |
| Provider execution proof | Lambda/provider marker | map SSM/AWS evidence |
| Audit correlation | Gateway trace + Policy fields + provider log | map SecCop evidence/audit model |

## Decision rule

Choose **one** practical adoption milestone with the best learning/security value and smallest integration cost.

A strong first candidate is:

> Put one harmless read-only SecCop AWS action behind AgentCore Gateway + Policy and prove the existing SecCop approval flow cannot bypass the deterministic Policy boundary.

Adopt this only if the comparison shows a genuine gap. Otherwise document why the existing SecCop control is sufficient and defer AgentCore integration.
