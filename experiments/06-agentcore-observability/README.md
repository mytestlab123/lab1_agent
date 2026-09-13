# Experiment 06 — AgentCore observability correlation

Status: **PASS**
Issue: #23

## Goal

Prove that one AgentCore Gateway request can be explained after the fact across three distinct stages:

```text
GitHub OIDC identity
  -> Gateway + Policy authorization
     -> provider execution
```

The proof reused the Experiment 05 Gateway, Policy Engine, harmless Lambda-backed tool and two caller identities. Authorization semantics were not changed.

## Native observability enabled

The experiment enabled the minimum native AWS telemetry needed for the retained Gateway:

1. CloudWatch Transaction Search for the account;
2. X-Ray trace segment destination -> `CloudWatchLogs`;
3. default Transaction Search indexing retained at 1%;
4. Gateway `APPLICATION_LOGS` delivery to a 7-day CloudWatch log group;
5. Gateway `TRACES` delivery to X-Ray / CloudWatch Transaction Search.

The durable consolidated resource definition is `infra/experiment06-observability.yaml`. Transaction Search is account-level configuration and is documented as a prerequisite because it does not map directly to the template used here.

## Live proof

GitHub Actions run `34746346691` used the two already-proven branch-scoped OIDC roles and generated two correlation IDs:

- `issue23-observe-allow`
- `issue23-observe-deny`

The workflow independently printed different STS assumed-role identities for caller A and caller B before invoking the same Gateway tool.

### ALLOW

Gateway application logs contained the correlation ID and one native Gateway trace ID (`6aa656a2…f913`). The same trace contained:

- request start;
- `tools/call` receipt;
- execution of the retained tool;
- Policy decision `ALLOW`;
- the authenticated caller-A IAM principal;
- the determining Cedar policy;
- successful Gateway response.

The Lambda provider log then contained exactly one marker:

```text
PROVIDER_EXECUTION request_id=issue23-observe-allow
```

Its Lambda X-Ray report used the same trace identity as the Gateway record, proving the Gateway -> provider correlation.

### DENY

Gateway application logs contained `issue23-observe-deny` and a different native trace ID (`6aa656a6…7bb9`). The same trace contained:

- request start;
- `tools/call` receipt;
- Policy decision `DENY`;
- the authenticated caller-B IAM principal;
- reason: no policy applied, therefore denied by default;
- no determining policy;
- `Tool Execution Denied`.

There was no `Executing tool` event in this trace and independent provider-log inspection found:

```text
PROVIDER_EXECUTION request_id=issue23-observe-deny -> count 0
```

## Acceptance result

| Stage | ALLOW | DENY |
|---|---|---|
| Authentication | caller A OIDC role | caller B OIDC role |
| Gateway correlation | request ID + trace ID | request ID + trace ID |
| Policy | ALLOW + determining policy | DENY by default |
| Tool reached | yes | no |
| Provider marker | exactly 1 | 0 |
| Result | PASS | PASS |

## What each signal proves

- **STS output** proves which GitHub OIDC identity authenticated.
- **Gateway application log** is the bridge: it carries request ID, trace ID, principal, Policy decision and Gateway/tool processing.
- **Policy fields inside the Gateway log** prove the authorization result independently of client/model prose.
- **Lambda provider marker** proves execution actually happened.
- **Absence of the DENY marker** proves Policy stopped execution before the provider.

## Important lessons

### Application logs are sufficient for the first audit proof

AgentCore Gateway vended application logs already expose `trace_id`, `span_id`, AWS request ID, request/response data and Policy evaluation details. That made the first deterministic audit chain possible without adding a custom tracing service.

### Transaction Search is account-wide

Enabling Transaction Search changes the account-level trace segment destination to CloudWatch Logs. This is broader than a single Gateway, so it should be treated as shared observability configuration rather than an experiment-local toggle.

### Trace availability is asynchronous

AWS documents that newly enabled Transaction Search can take up to roughly ten minutes before spans are searchable. Gateway application logs arrived first and supplied the immediate correlation evidence. The proof does not treat delayed span indexing as an authorization failure.

### Existing OIDC trust stayed narrow

The Experiment 05 caller roles remained trusted only for their exact existing repository branch subject. The temporary proof workflow was executed from that already-authorized branch rather than widening OIDC trust for observability.

## Cost / retention

The retained additions are low-cost/usage-priced CloudWatch log/trace delivery resources with a seven-day application-log retention. No EC2, NAT Gateway, load balancer, database, VPC, always-running container or provisioned capacity was added.
