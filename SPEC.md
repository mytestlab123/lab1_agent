# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB
Issue: #28

## Objective

Create and retain three useful AgentCore Harness examples that Amit can test without building a product GUI:

1. Pasted finding explainer, no effective tools.
2. One exact live read of the existing lab SSM parameter through a dedicated Gateway/Policy/Lambda path.
3. Approval practice using a typed inline-function pause and same-session APPROVED/REJECTED resume. This is a simulation, not live remediation.

## Authorized scope

- `mytestlab123/lab1_agent` owns code, tests, documentation and PR.
- PERSONAL/LAB `ap-southeast-1` only; fresh STS must match the documented lab identity.
- Minimal three Harness resources plus dedicated narrowly scoped IAM, Gateway/Policy, Lambda and seven-day logs as needed.
- Existing SSM drift-demo parameter is read-only. SecCop and all earlier lab resources remain unchanged.
- Versioned CloudFormation/configuration is desired state. AWS Core may bootstrap this exact bounded stack; GitHub/OIDC performs independent terminal tests without static credentials.
- Retain useful idle/usage-priced resources. No EC2, NAT, load balancer, database, public application server or provisioned capacity.
- Explicit token, iteration, invocation timeout and idle-session limits; no scheduled traffic.

## Acceptance

- Verify intended model, tools, IAM, memory and limits with GetHarness after READY.
- Live invocation of all three examples with saved public-safe results.
- Checker result matches independent SSM GetParameter, with unchanged value/version.
- Approval practice produces exactly one expected typed tool call, validates input/toolUseId and resumes the same session to end_turn for both decisions. No mutation tool exists. Test decisions are labeled simulated.
- AWS CLI control-plane and terminal streaming/approval tests run through GitHub OIDC. Report native AgentCore CLI separately if not exercised.
- Provide current AWS Console/Inspector instructions. GUI testing is PASS only if an authenticated graphical interaction actually ran; otherwise document it as NOT_TESTED, not assumed.
- Publish prompts, expected responses, CLI commands, GUI steps, sources, costs and limitations through MkDocs/GitHub Pages.

## Not in scope

No audit-correlation adoption change, SecCop write, remediation/reset, generic AWS tool, customer data, new scanner or dashboard. Do not claim this example suite replaces SecCop's durable jobs, single-use approval binding or production identity controls.
