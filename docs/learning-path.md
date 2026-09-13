# Learning Path

The lab learns one bounded capability at a time.

## Completed

1. AWS and GitHub authentication foundations.
2. Repeatable infrastructure deployment and drift verification.
3. Managed AgentCore Runtime invocation.
4. Gateway tool exposure and deterministic Policy ALLOW/DENY enforcement.
5. AgentCore Harness human approval: real `tool_use` pause plus reject/approve same-session resume.

## Next

6. Combine approval + Gateway + Policy into one governance chain:
   - reject -> zero provider execution;
   - approve + Policy DENY -> zero provider execution;
   - approve + Policy ALLOW -> harmless provider executes once.
7. Identity context.
8. End-to-end observability and trace correlation.
9. Combine the proven pieces into one small governance demo.

The detailed implementation roadmap remains in `ROADMAP.md` at the repository root.
