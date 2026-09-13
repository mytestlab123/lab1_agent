# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Result: PASS

## Objective

Prove the smallest useful Amazon Bedrock AgentCore Harness human-approval lifecycle using a client-side `inline_function` gate.

## Outcome

Issue #17 proved:

```text
request -> Harness -> typed request_approval tool_use -> PAUSE
  REJECTED -> same-session toolResult -> end_turn
  APPROVED -> same-session toolResult -> end_turn
```

The final proof used a harmless simulation and performed no provider mutation.

## Live verification

- PERSONAL/LAB identity and region were reverified.
- Harness reached `READY` with stateless `memory.disabled`.
- Final successful model: `global.amazon.nova-2-lite-v1:0`.
- Both test cases emitted a real typed `request_approval` tool-use event.
- Both first turns stopped with `tool_use`.
- Matching `toolUseId` values were returned to the same sessions through `toolResult` messages.
- REJECTED resumed to a final rejection with no additional tool call.
- APPROVED resumed to a final approval with no additional tool call.
- GitHub OIDC was used for the reproducible caller; no static AWS credentials were stored.

## Important implementation learning

### Harness HITL resume contract

Resume requires two messages in the same `runtimeSessionId`:

1. assistant re-sends the paused `toolUse` block;
2. user supplies the matching `toolResult`.

The typed stream is the acceptance boundary. Model prose about requesting approval is not evidence of approval enforcement.

### Caller IAM

`InvokeHarness` required the temporary GitHub OIDC caller to have both:

- `bedrock-agentcore:InvokeHarness`
- `bedrock-agentcore:InvokeAgentRuntime`

scoped to the exact Harness ARN.

### Execution-role trust

Harness provisions managed Runtime infrastructure underneath. The temporary execution role therefore required AgentCore service trust with `aws:SourceAccount` plus an account/region AgentCore SourceArn scope broad enough for the managed child resources.

### Model/account setup

A Claude Sonnet 4.6 reproduction was blocked by the account-level Anthropic use-case-details requirement. That was treated as model entitlement/configuration, not as an HITL failure. Nova 2 Lite completed the proof.

## Constraints satisfied

- PERSONAL/LAB only.
- No production/work resources.
- No static AWS access keys.
- No provider mutation in the approval proof.
- Stateless Harness memory.
- Explicit iterations/tokens/timeout guardrails.
- Existing Terraform/OIDC retained resources were not modified.

## Next Milestone

Experiment 04 — combine the proven approval gate with the proven Gateway + Policy enforcement path:

```text
human reject -> zero provider execution
human approve + Policy DENY -> zero provider execution
human approve + Policy ALLOW -> harmless provider executes exactly once
```

Human approval remains an orchestration gate; AgentCore Policy remains the final deterministic authorization boundary.
