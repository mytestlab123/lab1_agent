# Roadmap

## Completed

- Cross-session AWS Core/GitHub knowledge reuse proof.
- Public-safe GitHub OIDC + Terraform persistent state/drift proof.
- Public-safe Terraform PR validation with no AWS credentials.
- Experiment 01: AgentCore Runtime direct-code + IAM/SigV4.
- Experiment 02: Gateway + Policy ALLOW/DENY, including DENY -> zero provider executions.
- Experiment 03: Harness typed human approval pause + same-session reject/approve resume.
- MkDocs Material + GitHub Pages publication.
- Experiment 04: integrated approval + Gateway + Policy governance matrix.
- Experiment 05: identity-aware Policy with two authenticated IAM callers.
- Experiment 06: native observability correlation across identity -> Gateway -> Policy -> provider.
- Experiment 07: full-chain auditable human approval.
- Verified Experiment 07 outcomes:
  - human REJECT -> Gateway not reached -> provider 0;
  - human APPROVE + Policy DENY -> auditable DENY -> provider 0;
  - human APPROVE + Policy ALLOW -> auditable ALLOW -> provider exactly 1.

## Active

- Close out Issue #25 through one reviewed PR and publish the Experiment 07 learning page.

## Next

- Experiment 08: SecCop adoption comparison.
- Map the proven AgentCore controls against the SecCop architecture:
  - human approval;
  - authenticated principal;
  - Gateway/tool routing;
  - Policy enforcement;
  - provider mutation boundary;
  - trace/audit evidence.
- Identify the current SecCop equivalent, the gap, and whether to adopt or defer.
- Recommend **one** practical adoption milestone only.

## Later

- Add more AgentCore services only when they answer a new SecCop or governance learning question.
- Multi-tool MCP catalog, Cognito/JWT, browser, memory, dashboards or alarms are deferred unless justified by a concrete need.

## Cost / retention rule

Retain useful idle/usage-priced lab resources when expected cost remains negligible and comfortably below roughly USD 2/month per item and roughly USD 5/month for the retained lab footprint. Continuously billed resources such as EC2, NAT Gateway, load balancers, RDS/Aurora, continuously running containers or provisioned capacity require an explicit retain/delete decision.
