# End-to-End AgentCore Observability — Experiment 06

Status: **PASS**

Experiment 06 answers an operator's audit question:

> Who called the tool, what did Policy decide, and did the provider actually execute?

## Proven chain

```text
GitHub OIDC caller
   |
   v
STS identity
   |
   v
AgentCore Gateway APPLICATION_LOGS
   |  request_id + trace_id
   +-------------------------+
   |                         |
   v                         v
Policy decision          tool/provider
ALLOW or DENY            execution marker
```

The same Gateway and tool were used for both callers.

| Case | Identity | Policy | Tool reached | Provider |
|---|---|---|---|---:|
| ALLOW | caller A | ALLOW | yes | exactly 1 |
| DENY | caller B | default DENY | no | 0 |

## The key AWS signal

Gateway vended application logs provided the correlation bridge. A single structured record set carried:

- the application request/correlation ID;
- AWS request ID;
- native `trace_id` and `span_id`;
- authenticated IAM principal used by Policy;
- Policy decision and reason;
- determining policies for ALLOW;
- Gateway tool-processing events;
- response or denial information.

This means authentication, authorization and execution can be separated without relying on a model's explanation.

## ALLOW path

Correlation ID: `issue23-observe-allow`

The Gateway records showed:

```text
caller A
 -> Policy ALLOW
 -> retained tool executed
 -> successful response
```

The provider then emitted exactly one matching execution marker. The provider's X-Ray report used the same trace identity as the Gateway record.

## DENY path

Correlation ID: `issue23-observe-deny`

The Gateway records showed:

```text
caller B
 -> Policy DENY
 -> reason: no policy applies / denied by default
 -> no tool execution
```

Independent provider-log inspection found zero matching execution markers.

## Native AWS observability configuration

The lab enabled only native AgentCore/CloudWatch telemetry:

- CloudWatch Transaction Search;
- trace segment destination `CloudWatchLogs`;
- 1% Transaction Search indexing;
- Gateway application-log delivery with seven-day retention;
- Gateway trace delivery.

The reusable CloudFormation definition is in `infra/experiment06-observability.yaml`.

## Operational model learned

For this lab, use the signals in this order:

1. **STS** — who authenticated?
2. **Gateway application log** — which request/trace handled the operation?
3. **Policy fields** — why was it allowed or denied?
4. **Provider marker** — did execution really occur?

This is a useful audit pattern for a future security-remediation agent because an operator can reconstruct the control decision without trusting the agent's prose.

## Caveat: trace indexing is asynchronous

AWS documents that Transaction Search can take several minutes after enablement before spans are searchable. Application logs can arrive sooner and already expose the native trace ID and Policy decision. Delayed span indexing should therefore be treated as observability propagation, not as an authorization failure.

## Next milestone

The core controls are now separately proven:

- human approval;
- deterministic Policy enforcement;
- authenticated identity-aware authorization;
- provider-side execution proof;
- end-to-end audit correlation.

Experiment 07 should reintroduce the small Harness approval gate into this observable path and prove one full auditable chain for REJECT, APPROVE+DENY and APPROVE+ALLOW. After that, compare the resulting architecture directly with SecCop and select one adoption milestone.
