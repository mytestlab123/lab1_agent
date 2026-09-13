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
- MkDocs Material + GitHub Pages publication is live.
- Experiment 04: integrated human approval + Gateway + Policy governance proof.
- Verified all three integrated outcomes:
  - human REJECT -> zero provider execution;
  - human APPROVE + Policy DENY -> zero provider execution;
  - human APPROVE + Policy ALLOW -> harmless provider executes exactly once.
- Experiment 05: IAM identity-aware AgentCore Policy proof.
- Verified two authenticated GitHub OIDC IAM callers against the same Gateway/tool:
  - caller A matched an exact Cedar permit -> provider execution exactly once;
  - caller B had no matching permit -> AgentCore default DENY -> provider execution zero.
- Restored the missing retained Gateway target without adding a continuously billed workload.

## Active

- Close out Issue #21 through one reviewed PR and publish the Experiment 05 learning page.

## Next

- Experiment 06: end-to-end observability and trace correlation.
- Reuse the retained identity-aware Gateway + Policy + Lambda path.
- Give one request a correlation ID and prove that the same request can be followed through authenticated caller identity, Gateway invocation, Policy decision and provider-side evidence.
- Prefer existing AgentCore/CloudWatch observability before adding any new infrastructure.

## Later

- Reintroduce the proven Harness approval gate into the correlated trace if useful.
- Multi-tool MCP catalog only after identity and traceability are proven.
- Cognito/JWT + browser invocation only when an end-user UI is actually required.
- Compare the retained AgentCore governance pattern with SecCop and recommend one adoption milestone only.

## Cost / retention rule

Retain useful idle/usage-priced lab resources when expected cost remains negligible and comfortably below roughly USD 2/month per item and roughly USD 5/month for the retained lab footprint. Continuously billed resources such as EC2, NAT Gateway, load balancers, RDS/Aurora, continuously running containers, provisioned capacity, or similar workloads require an explicit retain/delete decision.
