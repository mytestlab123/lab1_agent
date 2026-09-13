# Experiment 05 — Identity-Aware AgentCore Policy

Status: **PASS**

## Goal

Prove that the same AgentCore Gateway tool can be allowed or denied based on authenticated IAM caller identity, with provider-side evidence rather than model/UI text.

## Proven matrix

| Authenticated caller | Policy result | Provider execution |
|---|---|---:|
| caller A | ALLOW | exactly 1 |
| caller B | DENY by default | 0 |

GitHub Actions run: `34743717610`.

## Control path

```text
GitHub Actions
   -> OIDC
      -> caller A or caller B IAM role
         -> SigV4 AgentCore Gateway
            -> Policy ENFORCE
               -> Lambda provider only when permitted
```

Both caller roles use the same repository/branch OIDC trust and can invoke only the retained lab Gateway. The authorization difference is in AgentCore Policy, not in static credentials or different provider code.

## Cedar behavior

Caller A has one exact permit scoped to:

- its assumed-role identity;
- the current Lambda-backed MCP tool action;
- the retained Gateway.

Caller B has no matching permit. AgentCore therefore returns its default-deny result before the Lambda provider executes. An explicit `forbid` is not required to prove identity-aware denial.

## Independent provider proof

AWS Core filtered the Lambda provider log group after the successful workflow:

- `issue21-caller-a` -> exactly one `PROVIDER_EXECUTION` marker;
- `issue21-caller-b` -> zero markers.

This is the acceptance boundary for the experiment.

## Unexpected retained-state finding

The Gateway and Lambda provider had been retained from Experiment 04, but the Gateway target itself was absent. The symptoms were:

1. the old direct tool name returned `Unknown tool`;
2. `tools/list` exposed only the semantic-search helper;
3. the helper reported that the Gateway had no configured targets.

The lab restored only the missing Lambda target. The existing Lambda, Gateway and Policy Engine were reused.

## Semantic-search learning

This Gateway uses semantic search. With that mode, `tools/list` exposes the built-in `x_amz_bedrock_agentcore_search` helper rather than the complete provider tool catalog. After the target was restored, semantic search returned the current provider tool name, which was then used for the final proof.

## Policy-schema learning

The existing Experiment 04 permit referenced the older target/action. Current AgentCore validation reported that pre-existing rule as not matching the latest tool input schema. The new caller A rule was first validated against the current Gateway schema and then tightened to the exact restored tool action.

This is useful operationally: retained policy text can become stale when target/tool schemas change even though the Policy Engine itself remains ACTIVE.

## Retention

The restored target, caller A permit and both OIDC caller roles are retained because they are effectively idle/usage-priced lab resources under the repository's low-cost retention rule. No EC2, NAT Gateway, load balancer, database, VPC or always-running workload was added.

## Next

Experiment 06 should trace one correlation ID end to end:

```text
caller identity -> Gateway -> Policy decision -> provider marker/log/trace
```

Prefer existing AgentCore and CloudWatch observability before adding infrastructure.
