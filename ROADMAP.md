# Roadmap

## Completed

- Cross-session AWS Core/GitHub knowledge reuse proof.
- Public-safe GitHub OIDC + Terraform persistent state/drift proof.
- Public-safe Terraform pull-request validation with no AWS credentials.
- Experiment 01: AgentCore Runtime direct-code + IAM/SigV4 proof.
- Experiment 02: AgentCore Gateway + Policy ALLOW/DENY proof with one harmless Lambda-backed MCP tool.
- Verified security property: `DENY` resulted in **zero provider executions**.

## Next

- Publish accumulated learning with **MkDocs Material + GitHub Pages**.
- **Experiment 03 — Human Approval Harness.**
- Demonstrate `ALLOW | DENY | APPROVAL_REQUIRED`.
- For approval-required actions, prove:
  - reject -> zero provider execution;
  - approve -> request proceeds to Gateway/Policy and only executes when Policy also permits it.

## Later

- Identity/user context for approval decisions.
- AgentCore observability and end-to-end trace correlation.
- Multi-tool MCP catalog only after the governance loop is proven.
- Cognito/JWT + browser invocation only when an end-user UI is actually required.
- Compare retained AgentCore patterns with SecCop and recommend one adoption milestone only.
