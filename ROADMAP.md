# Roadmap

## Completed

- Cross-session AWS Core/GitHub knowledge reuse proof.
- Public-safe GitHub OIDC + Terraform persistent state/drift proof.
- Public-safe Terraform pull-request validation with no AWS credentials.
- Experiment 01: AgentCore Runtime direct-code + IAM/SigV4 proof.

## Next

- **Experiment 02 — AgentCore Gateway + Policy ALLOW/DENY.**
- Use one harmless read-only tool.
- Make the policy decision visible.
- Prove `DENY` results in **zero provider execution**.
- Keep it isolated from SecCop until the value is proven.

## Later

- AG-UI/MCP tool-activity experiment if Gateway/Policy proves useful.
- Cognito/JWT + browser Runtime invocation only when an end-user UI is actually needed.
- Compare retained AgentCore patterns with SecCop and recommend one adoption milestone only.
