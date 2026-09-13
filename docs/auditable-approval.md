# Full-Chain Auditable Human Approval — Experiment 07

Status: **PASS**

Experiment 07 combines human approval, authenticated identity, deterministic Policy enforcement, provider execution evidence, and native observability into one governance chain.

| Human | Policy | Provider |
|---|---|---:|
| REJECT | not reached | 0 |
| APPROVE | DENY by default | 0 |
| APPROVE | ALLOW | exactly 1 |

```text
Harness typed approval
 -> controller
 -> authenticated IAM caller
 -> AgentCore Gateway
 -> Policy ENFORCE
 -> harmless provider
 -> CloudWatch evidence
```

## Typed human approval

Each case had to produce `stopReason = tool_use` with tool `request_approval`. The controller resumed the same Harness session with the matching `toolUseId` and a typed `toolResult`. Model prose alone was not accepted.

### REJECT

Correlation ID: `issue25-human-reject`

The Harness returned a real REJECTED result. The controller stopped. Exact AWS log inspection found zero matching Gateway events and zero provider markers.

### APPROVE + DENY

Correlation ID: `issue25-approve-deny`

After Harness approval, caller B invoked the retained Gateway using its existing branch-scoped GitHub OIDC role. Gateway logs recorded the caller-B principal, Policy `DENY`, the default-deny reason, no determining policy, and no `Executing tool` event. Provider execution remained **0**.

### APPROVE + ALLOW

Correlation ID: `issue25-approve-allow`

After Harness approval, caller A invoked the same Gateway and tool. Gateway logs recorded the caller-A principal, Policy `ALLOW`, the determining Cedar policy, tool execution, and successful completion. The provider emitted exactly one marker:

```text
PROVIDER_EXECUTION request_id=issue25-approve-allow
```

GitHub Actions run `34748226633` proved the two approved Gateway cases with the existing narrow Issue #21 OIDC identities; their trust was not widened.

## Main learning

Human approval, authentication, authorization, and execution are separate facts. **APPROVED does not override Cedar.** Policy remains the final deterministic execution boundary.

Harness and Gateway are deliberately composed by a controller:

```text
REJECTED -> controller stops
APPROVED -> controller continues -> Gateway -> Policy independently decides
```

This separation is useful for SecCop-style workflows because the human gate and machine-enforced least-privilege boundary remain independent controls.

## Cost and retention

The Experiment 07 Harness is retained because it is usage-priced / near-zero while idle and remains within the lab cost rule. Existing Gateway, Policy Engine, Lambda provider, OIDC roles and Experiment 06 observability are reused. No continuously billed workload was added.

## Next

Compare the proven AgentCore governance chain directly with SecCop and choose one practical adoption milestone rather than adding more AgentCore services without a new learning question.
