# Identity-Aware AgentCore Policy — Experiment 05

Status: **PASS**

Experiment 05 reused the retained AgentCore Gateway, Policy Engine and Lambda provider to prove authorization from authenticated IAM caller identity.

## Result

| Caller | AgentCore Policy | Provider execution |
|---|---|---:|
| caller A | ALLOW | exactly 1 |
| caller B | DENY by default | 0 |

The two callers were separate GitHub OIDC IAM roles with the same narrow ability to invoke the lab Gateway. The provider code and requested tool were identical; only authenticated principal identity differed.

## What Policy enforced

Caller A matched a Cedar `permit` scoped to:

- the exact assumed-role identity;
- the exact current tool action;
- the exact Gateway.

Caller B had no matching permit. In ENFORCE mode, AgentCore returned JSON-RPC `-32002` with `Tool Execution Denied` and explained that no policy applied, so the request was denied by default.

## Independent evidence

GitHub Actions run `34743717610` proved both OIDC identities and both Gateway outcomes.

AWS Core then checked provider-side logs independently:

```text
issue21-caller-a -> PROVIDER_EXECUTION count = 1
issue21-caller-b -> PROVIDER_EXECUTION count = 0
```

A successful response or model message alone was not accepted as proof.

## Retained-state lesson

The Gateway and Lambda provider still existed from the previous experiment, but the Gateway target did not. A retained top-level resource does not guarantee that all dependent configuration is still present.

The missing target was detected through three signals:

1. the previous tool name became unknown;
2. `tools/list` exposed only the semantic-search helper;
3. semantic search reported that no targets were configured.

Only the missing Lambda target was restored.

## Semantic-search lesson

The Gateway is configured for semantic search. In this mode, `tools/list` exposes `x_amz_bedrock_agentcore_search` rather than every provider tool. After the target was restored, the search helper returned the real Lambda-backed tool used for the identity test.

## Policy-schema lesson

AgentCore's analyzer reported that the older retained Experiment 04 policy no longer matched the newest tool input schema. The new identity permit validated against the current target and was then tightened to the exact current action.

Policy engines can remain healthy while individual retained rules become stale as target schemas change. Revalidation belongs in the change workflow.

## Architecture learned

```text
GitHub OIDC
   |
   +-- caller A ----+
   |                |
   +-- caller B ----+--> AWS_IAM Gateway
                         |
                         v
                    Policy ENFORCE
                     /          \
                  ALLOW       default DENY
                    |             X
                    v
              Lambda provider
```

IAM authenticates the caller; AgentCore Policy decides whether that authenticated identity may execute the tool.

## Next

Experiment 06 should add end-to-end observability without changing the governance model. One correlation ID should be traceable across caller identity, Gateway invocation, Policy result and provider-side evidence.
