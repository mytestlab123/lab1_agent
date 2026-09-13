# AgentCore Harness Human Approval

Status: **PASS**

A real AgentCore Harness produced a typed `request_approval` `tool_use` event and paused. The same session was then resumed with a matching `toolResult` for both human decisions.

```text
request -> Harness -> request_approval tool_use -> PAUSE
  reject  -> resume -> final rejection
  approve -> resume -> final approval
```

The proof used a harmless `DEMO_CHANGE` simulation and performed no provider mutation.

## What matters

- Approval is a typed execution boundary, not model prose.
- `toolUseId` must be preserved across pause/resume.
- Resume uses the same `runtimeSessionId`.
- The caller re-sends the assistant `toolUse` and supplies a user `toolResult` with the same ID.
- Both reject and approve paths ended cleanly with `end_turn`.
- Nova 2 Lite completed the final proof.

## Next experiment

Connect this proven approval gate to the already-proven Gateway + Policy path:

```text
Harness
  |
  v
request_approval
  |
  +-- reject --> STOP / zero provider execution
  |
  +-- approve
        |
        v
   AgentCore Gateway
        |
        v
   AgentCore Policy
      /     \
   DENY     ALLOW
    |         |
 zero       provider
execution   executes once
```

The important design rule is unchanged: **human approval decides whether the request may continue; AgentCore Policy remains the final deterministic authorization boundary at execution time.**

Detailed evidence: `experiments/03-agentcore-harness-approval/`.
