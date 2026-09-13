# Human Approval Harness — Current Learning

Status: **PARTIAL**

A real AgentCore Harness was created and reached `READY`. Model invocation through the managed Harness also worked.

The intended approval architecture is:

```text
request -> Harness -> inline_function approval event -> human decision
reject  -> zero downstream execution
approve -> resume -> controlled downstream path
```

## What we learned

- Harness is materially easier to deploy than a custom Runtime loop: model, tools and limits are configuration.
- A stateless Harness can disable managed memory for a narrow lab.
- The managed Harness provisions Runtime infrastructure underneath, which matters when scoping its execution-role trust policy.
- `inline_function` is the right AWS primitive for a client-side approval interrupt.
- The acceptance test must inspect the typed stream and require a real `tool_use` event. Text such as “I will request approval” is **not** an approval control.

## Current blocker

In the live lab, bounded tests with Nova Micro, Nova Lite, Nova 2 Lite and Claude Haiku 4.5 generated prose or simulated function-call text instead of a typed Harness `tool_use` event. A final per-invocation inline-tool override also did not produce the required stream.

Therefore HITL approval is **not yet claimed as proven**.

## Next retry

Use the official AgentCore CLI/TUI or an AWS-published Harness HITL sample with the same inline-function schema. Capture the expected working `tool_use` stream first, then compare that configuration directly with the SDK-created Harness.

Detailed evidence: `experiments/03-agentcore-harness-approval/`.
