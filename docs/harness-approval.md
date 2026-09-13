# AgentCore Harness Human Approval

Status: **PASS**

This experiment proves a real client-side human-approval interrupt with Amazon Bedrock AgentCore Harness.

## Proven behavior

```text
User request
   |
   v
Harness
   |
   v
request_approval inline_function
   |
   +--> stopReason = tool_use
           |
           +--> REJECTED -> resume same session -> final reject
           |
           +--> APPROVED -> resume same session -> final approve
```

The test used a harmless `DEMO_CHANGE` simulation. No real provider change occurred.

## What makes this a real approval gate

The proof did not accept text such as “I will ask for approval.” It required the Harness stream to contain a typed `toolUse` block for `request_approval` and to stop with `tool_use`.

The caller then preserved the same `runtimeSessionId` and returned a matching result:

```text
assistant -> toolUse(toolUseId, name, input)
user      -> toolResult(same toolUseId, APPROVED or REJECTED)
```

Both paths resumed successfully and finished with `end_turn`.

## Key implementation lessons

- `inline_function` is the client-side HITL primitive.
- Preserve `toolUseId`; it links the human decision to the paused call.
- Resume the same Harness session.
- Treat the typed event stream as evidence, not model prose.
- The final successful proof used Nova 2 Lite.
- Caller IAM for `InvokeHarness` also required `InvokeAgentRuntime` on the Harness ARN.
- Stateless `memory.disabled` keeps a narrow approval test simple.

## What this does not prove yet

Approval by itself is not final authorization. The next experiment connects this gate to AgentCore Gateway + Policy:

```text
approve -> Gateway -> Policy -> ALLOW/DENY -> provider
```

The target is to prove independently that human rejection and Policy denial both prevent provider execution.

Detailed evidence and reproducible code live in `experiments/03-agentcore-harness-approval/`.
