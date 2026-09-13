# Roadmap

## Completed

- Cross-session AWS Core/GitHub knowledge reuse proof.
- Public-safe GitHub OIDC + Terraform persistent state/drift proof.
- Public-safe Terraform pull-request validation with no AWS credentials.
- Experiment 01: AgentCore Runtime direct-code + IAM/SigV4 proof.
- Experiment 02: AgentCore Gateway + Policy ALLOW/DENY proof with one harmless Lambda-backed MCP tool.
- Verified security property: Policy `DENY` resulted in **zero provider executions**.
- Experiment 03: AgentCore Harness `inline_function` human approval proof.
- Verified a real typed `tool_use` pause plus same-session REJECTED and APPROVED resumptions.

## Active

- Publish accumulated learning with **MkDocs Material + GitHub Pages**. Build/artifact are ready; live deployment waits for repository Pages source = GitHub Actions.

## Next

- Experiment 04: integrate the proven approval gate with Gateway + Policy.
- Prove all three governance outcomes:
  - human reject -> zero provider execution;
  - human approve + Policy DENY -> zero provider execution;
  - human approve + Policy ALLOW -> harmless provider executes exactly once.

## Later

- Identity/user context for approval decisions.
- AgentCore observability and end-to-end trace correlation.
- Multi-tool MCP catalog only after the governance loop is proven.
- Cognito/JWT + browser invocation only when an end-user UI is actually required.
- Compare retained AgentCore patterns with SecCop and recommend one adoption milestone only.
