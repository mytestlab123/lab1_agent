# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB
Issue: #21

## Objective

Reuse the retained Experiment 04 AgentCore Gateway + Policy Engine + harmless Lambda provider and prove deterministic authorization from authenticated IAM caller identity.

Target:

```text
GitHub OIDC caller A -> Gateway -> Policy -> ALLOW -> provider executes exactly once
GitHub OIDC caller B -> Gateway -> Policy -> DENY  -> provider executes zero times
```

## Acceptance

PASS only if independent evidence proves:

| Caller | Policy decision | Provider execution |
|---|---|---:|
| caller A | ALLOW | exactly 1 |
| caller B | DENY | 0 |

The authorization rule must be attributable to authenticated IAM identity/context. Provider execution must be verified independently from provider-side markers; model/UI text is not evidence.

## Authorized scope

- PERSONAL/LAB only in `ap-southeast-1`.
- Reuse retained Experiment 04 Gateway, Policy Engine, Lambda target/provider and small logs.
- Add at most two narrowly scoped GitHub OIDC IAM caller roles for the Issue #21 branch.
- Add narrowly scoped Cedar policy rules needed to distinguish caller A from caller B.
- No Cognito, frontend, VPC, database, EC2, NAT Gateway, load balancer, always-running container, provisioned capacity or destructive provider operation.
- No static AWS credentials.

## Guardrails

- Reverify STS identity before mutation.
- Keep AgentCore Policy in ENFORCE mode.
- Caller roles must trust only the exact repository identity and Issue #21 branch subject.
- Caller permissions must be limited to the retained Gateway access required by the proof.
- Do not weaken the existing Gateway or Policy Engine to make the test pass.
- Independently count provider-side execution markers after each case.

## Retention

Useful idle/usage-priced lab resources may remain when expected cost stays comfortably below roughly USD 2/month per item and roughly USD 5/month for the retained lab footprint. Continuously billed workloads require a separate explicit decision.

## Durable output

Record the reproducible test/evidence under `experiments/05-agentcore-identity/`, publish the learning through MkDocs/GitHub Pages, update `CONTEXT.md` and `ROADMAP.md`, and finish through one cohesive PR.
