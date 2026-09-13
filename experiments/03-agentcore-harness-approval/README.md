# Experiment 03 — AgentCore Harness Human Approval

Status: **PASS**

## Goal

Prove a real human-in-the-loop interruption with AgentCore Harness `inline_function`.

## Proven flow

```text
request
  -> Harness
  -> typed request_approval tool_use
  -> PAUSE
       -> REJECTED -> resume same session -> final reject
       -> APPROVED -> resume same session -> final approve
```

GitHub Actions run `34738408771` proved both decision paths with a harmless `DEMO_CHANGE` simulation. No provider mutation was performed.

## Acceptance evidence

For both REJECTED and APPROVED cases:

- first turn stopped with `stop_reason = tool_use`;
- the typed tool name was exactly `request_approval`;
- one approval tool call was captured;
- the same Harness session was resumed with matching `toolUseId`;
- second turn stopped with `end_turn`;
- no second tool call was emitted.

Reject returned a final rejection and no action. Approve returned a final approval while explicitly noting that the proof performed no real action.

## The correct resume contract

The working pattern came from the AWS Sentinel Harness sample:

1. reconstruct `toolUseId`, tool name, and input from the stream;
2. keep the same `runtimeSessionId`;
3. send an assistant message containing the original `toolUse` block;
4. send a user message containing the matching `toolResult`;
5. invoke Harness again and consume the continuation stream.

A model saying “I will request approval” is not enough. Acceptance requires the typed tool-use boundary.

## Important findings

### 1. `allowedTools` matters

Earlier restrictive tests did not produce a usable tool-use stream. The successful proof used the Harness default `allowedTools=["*"]`, while the system prompt constrained the model to the configured `request_approval` path for this simulation.

Treat this as a reproducible lab finding, not yet a claim that the allowlist was the only earlier root cause.

### 2. Nova 2 Lite completed the proof

The final successful run used `global.amazon.nova-2-lite-v1:0`.

An attempted reproduction with Claude Sonnet 4.6 reached the Harness but Bedrock returned an account-level requirement to submit Anthropic model use-case details. The lab therefore used Nova 2 Lite rather than treating that entitlement as an HITL defect.

### 3. InvokeHarness caller IAM has a non-obvious requirement

The GitHub OIDC caller needed both:

- `bedrock-agentcore:InvokeHarness`
- `bedrock-agentcore:InvokeAgentRuntime`

on the **Harness ARN**. Scoping `InvokeAgentRuntime` only to the generated Runtime ARN failed.

### 4. Harness execution-role trust spans managed Runtime infrastructure

Harness provisions AgentCore Runtime infrastructure underneath. A trust policy limited only to `harness/*` failed role validation. The temporary LAB role therefore used the documented account/region AgentCore SourceArn scope plus `aws:SourceAccount`.

### 5. Stateless mode keeps the proof small

`memory.disabled` avoided creating a managed Memory resource and kept the experiment focused on the approval lifecycle.

## Scope boundary

This experiment proves only the Harness pause/reject/approve/resume lifecycle. It does **not** yet prove the complete governance chain through AgentCore Gateway + Policy + provider execution.

## Next experiment

Stitch the proven approval gate to the already-proven Gateway + Policy boundary:

```text
Harness -> request_approval
  reject -> STOP / zero provider execution
  approve -> Gateway -> Policy
               DENY  -> zero provider execution
               ALLOW -> harmless provider executes exactly once
```
