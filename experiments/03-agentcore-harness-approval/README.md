# Experiment 03 — AgentCore Harness Human Approval

Status: **PARTIAL**

## Goal

Prove a real human-in-the-loop interruption with AgentCore Harness `inline_function`.

Target flow:

```text
request -> Harness -> inline_function approval event -> human decision
reject  -> zero downstream execution
approve -> resume -> controlled downstream path
```

## What passed

- AgentCore Harness creation in the PERSONAL/LAB account.
- Harness reached `READY` after correcting execution-role trust scope.
- Stateless configuration using `memory.disabled` worked.
- Bedrock model invocation through Harness worked.
- Model/version updates worked without recreating the Harness.
- Explicit execution limits were used.
- No static AWS credentials were created.

## What did not pass

The acceptance criterion requires a **real Harness `tool_use` event** for the configured `inline_function`.

Three bounded model tests were attempted:

1. Nova Micro
2. Nova Lite
3. Nova 2 Lite
4. Claude Haiku 4.5

The models described or simulated calls to `request_approval` in text instead of emitting the required Harness `tool_use` event. A final per-invocation tool override also failed to produce a valid approval tool-use stream.

Therefore this experiment does **not** claim HITL approval is proven.

## Important learning

A model saying “I will request approval” is not an approval control. The acceptance test must inspect the typed Harness stream and require:

```text
stopReason = tool_use
```

plus a real `toolUse` content block with the expected tool name and arguments.

Anything else is prose, not enforcement.

## IAM / deployment learning

Harness creates underlying AgentCore Runtime infrastructure. Restricting the execution-role trust policy only to `harness/*` caused role validation to fail. For this temporary lab, the documented AgentCore SourceArn scope was used so the managed Runtime resource could assume the role.

The first failed create also demonstrated that default Harness memory can leave a managed memory name during failure/retry. The successful retry explicitly used stateless `memory.disabled`.

## Cleanup

Experiment-owned Harness and IAM execution-role deletion was requested. No experiment Memory resources remained when independently listed.

## Next retry

Do not cycle more models. Reproduce the same inline-function configuration with the official AgentCore CLI/TUI or an AWS-published Harness HITL sample, capture the expected `tool_use` stream shape, then compare that request/config directly with this SDK-created Harness.
