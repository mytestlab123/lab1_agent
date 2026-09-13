# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB
Issue: #23

## Objective

Reuse the retained Experiment 05 identity-aware AgentCore Gateway + Policy Engine + harmless Lambda provider path and prove end-to-end observability for one ALLOW request and one DENY request without changing authorization semantics.

Target:

```text
GitHub OIDC caller
  -> AgentCore Gateway
     -> AgentCore Policy decision
        -> provider marker/log when allowed
```

Use one unique correlation/request ID per case and identify which native AWS telemetry carries evidence for authentication, authorization, Gateway handling and provider execution.

## Acceptance

PASS only if independent evidence proves:

| Case | Caller | Policy | Provider | Required evidence |
|---|---|---|---:|---|
| ALLOW | caller A | ALLOW | exactly 1 | caller identity + Gateway + Policy + provider correlation |
| DENY | caller B | DENY | 0 | caller identity + Gateway + Policy correlation + no provider marker |

The evidence must distinguish authentication, authorization and execution as separate stages. Model/UI text alone is not evidence.

## Authorized scope

- PERSONAL/LAB only in `ap-southeast-1`.
- Reuse the retained Gateway, Policy Engine, Gateway target, Lambda provider and Issue #21 OIDC caller roles.
- Prefer native AgentCore and CloudWatch observability already available for Gateway and Policy.
- Add only the minimum low-cost CloudWatch/AgentCore observability configuration required for the proof.
- No EC2, NAT Gateway, load balancer, database, VPC, frontend, Cognito, always-running container or provisioned capacity.
- No static AWS credentials.

## Guardrails

- Reverify STS identity before AWS mutation.
- Keep existing authorization semantics unchanged: caller A remains exact permit; caller B remains default deny.
- Keep AgentCore Policy in ENFORCE mode.
- Do not broaden OIDC trust or Gateway IAM permissions merely to obtain telemetry.
- Provider execution must be independently verified from provider-side markers.
- Prefer native Gateway/Policy spans, logs and metrics before adding custom tracing infrastructure.
- Retain only useful near-zero/usage-priced observability resources within the existing lab cost boundary.

## Durable output

Record reproducible evidence under `experiments/06-agentcore-observability/`, publish the learning through MkDocs/GitHub Pages, update `CONTEXT.md` and `ROADMAP.md`, and finish through one cohesive PR.
