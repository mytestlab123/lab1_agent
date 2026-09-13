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
8. Native observability correlation: connect authenticated principal, Gateway request/trace, Policy decision and provider execution evidence for both ALLOW and DENY.

## Next

9. Reintroduce the Harness approval gate into the observable path so approval, identity, Policy and provider execution can be audited as one chain.
10. Compare the proven AgentCore governance chain with SecCop and select one practical adoption milestone.
11. Add more tools or end-user identity only when they answer a new learning question.

The detailed implementation roadmap remains in `ROADMAP.md` at the repository root.
