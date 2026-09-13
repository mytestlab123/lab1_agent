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
- Experiment 06: native observability and audit correlation proof.
- Verified ALLOW correlation across OIDC identity -> Gateway request/trace -> Policy ALLOW -> tool execution -> exactly one Lambda provider marker.
- Verified DENY correlation across OIDC identity -> Gateway request/trace -> Policy default DENY, with no tool execution event and zero provider markers.
- Enabled low-cost native Gateway application logs, Gateway traces and CloudWatch Transaction Search for the retained lab path.

## Active

- Close out Issue #23 through one reviewed PR and publish the Experiment 06 learning page.

## Next

- Experiment 07: full-chain auditable human approval.
- Recreate the small proven Harness approval gate and compose it with the retained observable identity-aware Gateway + Policy + Lambda path.
- Give the approval flow one correlation/session identity and prove:
  - human REJECT -> no Gateway/provider execution;
  - human APPROVE + Policy DENY -> auditable DENY, provider 0;
  - human APPROVE + Policy ALLOW -> auditable ALLOW, provider exactly 1.
- Keep Policy as the final deterministic execution boundary and retain only near-zero/usage-priced resources.

## Later

- Compare the fully proven AgentCore governance pattern with SecCop and recommend one adoption milestone only.
- Multi-tool MCP catalog only when it adds learning beyond the governance path.
- Cognito/JWT + browser invocation only when an end-user UI is actually required.
- Evaluate dashboards/alarms only after the trace fields worth operating on are known.

## Cost / retention rule

Retain useful idle/usage-priced lab resources when expected cost remains negligible and comfortably below roughly USD 2/month per item and roughly USD 5/month for the retained lab footprint. Continuously billed resources such as EC2, NAT Gateway, load balancers, RDS/Aurora, continuously running containers, provisioned capacity, or similar workloads require an explicit retain/delete decision.
