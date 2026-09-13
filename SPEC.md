# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Issue: #23
Result: PASS

## Objective

Reuse the retained Experiment 05 identity-aware AgentCore Gateway + Policy Engine + harmless Lambda provider path and prove end-to-end observability for one ALLOW request and one DENY request without changing authorization semantics.

Proven path:

```text
GitHub OIDC caller
  -> AgentCore Gateway
     -> AgentCore Policy decision
        -> provider execution when allowed
           -> CloudWatch / X-Ray correlation evidence
```

## Acceptance result

| Case | Caller | Policy | Provider | Result |
|---|---|---|---:|---|
| ALLOW | caller A | ALLOW | exactly 1 | PASS |
| DENY | caller B | DENY by default | 0 | PASS |

Authentication, authorization, Gateway handling and provider execution were observed as separate stages. Model/UI text alone was not accepted as evidence.

## Live proof

- GitHub Actions run `34746346691` authenticated caller A and caller B through their existing narrow GitHub OIDC roles.
- Caller A invoked the same retained Gateway/tool and received a successful MCP response.
- Caller B invoked the same retained Gateway/tool and received JSON-RPC `-32002` / `Tool Execution Denied` because no policy applied to that principal.
- Native Gateway application logs carried the test correlation ID, AWS request ID, native trace ID, authenticated IAM principal, Policy decision and tool-processing events.
- ALLOW logs showed the exact caller-A principal, a determining Cedar policy, `Executing tool`, and a successful response.
- DENY logs showed the exact caller-B principal, `DENY`, the default-deny reason and no tool-execution event.
- The Lambda provider log contained exactly one `issue23-observe-allow` execution marker and zero `issue23-observe-deny` markers.
- The ALLOW Lambda X-Ray report carried the same native trace identity as the Gateway record.

## Observability configuration

The minimum native observability configuration was enabled for the retained Gateway:

1. CloudWatch Transaction Search enabled account-wide;
2. X-Ray trace segment destination set to `CloudWatchLogs` and verified `ACTIVE`;
3. default Transaction Search indexing retained at 1%;
4. Gateway `APPLICATION_LOGS` delivered to a dedicated CloudWatch Logs group with seven-day retention;
5. Gateway `TRACES` delivered to X-Ray / Transaction Search.

The reproducible Gateway delivery definition is stored in `infra/experiment06-observability.yaml`. Transaction Search is account-level configuration and is documented separately from the resource template.

## Important learning

### Gateway application logs are an audit bridge

For this first audit proof, native Gateway vended logs were sufficient to stitch together request correlation, principal identity, Policy outcome, Gateway/tool behavior and provider execution evidence.

### Authorization and execution remain separate facts

A successful authentication event does not prove authorization, and an ALLOW decision does not by itself prove downstream execution. The proof required all three stages independently:

```text
STS / OIDC identity
  -> Policy decision
     -> provider-side execution marker
```

### DENY is observable before provider execution

The DENY trace contained the caller identity and Policy reason but no `Executing tool` event and no provider marker. This makes the enforcement boundary operationally explainable after the fact.

### Trace indexing is asynchronous

AWS documents that Transaction Search may take several minutes after first enablement before spans become searchable. Gateway application logs arrived earlier, so delayed span indexing was not treated as an authorization failure.

### Existing OIDC trust stayed narrow

The retained caller roles remained trusted only for the exact existing repository branch subject. The temporary proof workflow ran from that already-authorized branch rather than widening OIDC trust solely for observability.

## Guardrails satisfied

- PERSONAL/LAB only in `ap-southeast-1`.
- STS identity reverified before AWS mutation.
- AgentCore Policy remained `ENFORCE`.
- Caller A permit and caller B default-deny semantics were unchanged.
- No OIDC trust or Gateway execution permission was broadened for telemetry.
- No static AWS credentials.
- No EC2, NAT Gateway, load balancer, database, VPC, frontend, always-running container or provisioned capacity was introduced.

## Retention

The new retained resources are low-cost/usage-priced observability components: Gateway log/trace delivery, a seven-day CloudWatch application-log group and account-level Transaction Search configuration. They remain within the repository's existing low-cost lab rule.

## Durable output

Experiment 06 learning is recorded under `experiments/06-agentcore-observability/`, published in `docs/observability-trace.md`, and represented by the reproducible observability template in `infra/experiment06-observability.yaml`.
