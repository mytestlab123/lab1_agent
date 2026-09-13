# Next Experiment — Compose Human Approval with Gateway + Policy

Status: **NEXT**

The lab has independently proven:

1. AgentCore Runtime deployment and invocation.
2. AgentCore Gateway + Policy deterministic ALLOW/DENY, including provider-side proof that DENY caused zero provider executions.
3. AgentCore Harness `inline_function` human approval with a real typed `tool_use` pause and same-session APPROVED / REJECTED resume.

The next milestone composes those controls into one governance chain:

```text
Harness
  -> request_approval
      REJECT -> stop / zero provider execution
      APPROVE -> AgentCore Gateway -> AgentCore Policy
                   DENY  -> zero provider execution
                   ALLOW -> harmless provider executes exactly once
```

Acceptance requires independent provider-side execution markers. Model/UI text is not sufficient evidence.

Tracked in GitHub Issue #19.
