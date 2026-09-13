# Learning Path

The lab learns one bounded capability at a time.

## Completed

1. AWS and GitHub authentication foundations.
2. Repeatable infrastructure deployment and drift verification.
3. Managed AgentCore Runtime invocation.
4. Gateway tool exposure and deterministic Policy ALLOW/DENY enforcement.
5. AgentCore Harness human approval: real `tool_use` pause plus reject/approve same-session resume.
6. Integrated governance: approval + Gateway + Policy with provider-side proof for REJECT, DENY and ALLOW.
7. Identity-aware Policy: two authenticated IAM callers against the same Gateway/tool, with caller A allowed exactly once and caller B denied before provider execution.

## Next

8. End-to-end observability and trace correlation across caller identity -> Gateway -> Policy -> provider.
9. Reintroduce Harness approval into the correlated trace if it adds useful evidence.
10. Add more tools only after identity and tracing are proven.
11. Compare the proven governance pattern with the SecCop architecture.

The detailed implementation roadmap remains in `ROADMAP.md` at the repository root.
