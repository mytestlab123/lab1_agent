# Next Experiment — Full-Chain Auditable Approval

Status: **NEXT**

The lab has now proven:

1. AgentCore Runtime deployment and invocation.
2. Gateway + Policy deterministic ALLOW/DENY.
3. Harness human approval with a real typed pause/resume lifecycle.
4. Integrated approval -> Gateway -> Policy -> provider governance.
5. IAM identity-aware Policy: the same Gateway/tool behaves differently for two authenticated callers.
6. Native AgentCore/CloudWatch observability: caller identity, Gateway trace, Policy decision and provider execution can be correlated after the fact.

## Next milestone

Combine the approval proof with the observable identity-aware execution path:

```text
Human decision
   -> Harness approval gate
      -> authenticated controller/caller
         -> AgentCore Gateway
            -> AgentCore Policy
               -> Lambda provider
                  -> CloudWatch / trace evidence
```

The purpose is not another UI or model experiment. The purpose is one auditable governance chain showing exactly where a request stopped or executed.

## Acceptance idea

| Case | Expected audit result |
|---|---|
| REJECT | approval event recorded; Gateway/provider not reached |
| APPROVE + DENY | approval recorded; caller + Gateway + Policy DENY correlated; provider 0 |
| APPROVE + ALLOW | approval recorded; caller + Gateway + Policy ALLOW correlated; provider exactly 1 |

Requirements:

- use real typed Harness approval events, not model prose;
- keep AgentCore Policy as the final deterministic execution boundary;
- preserve narrow GitHub OIDC trust;
- reuse the retained Gateway, Policy Engine, target, caller identities and provider where possible;
- reuse native observability rather than add a separate tracing platform;
- no EC2, NAT Gateway, database, load balancer or continuously billed workload;
- document the final audit chain in MkDocs/GitHub Pages.

After this proof, compare the architecture directly with SecCop and choose one adoption milestone rather than continuing to add AgentCore features for their own sake.
