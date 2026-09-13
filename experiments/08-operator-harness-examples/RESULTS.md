# Operator Harness example results

Issue #28 / PR #29. Tests executed 2026-09-13 UTC (2026-09-14 SGT).

## Verdict

**All three service/terminal use cases PASS. Authenticated Console GUI: NOT_TESTED.**

CloudFormation stack `lab1-operator-harness-examples`: CREATE_COMPLETE. All three Harnesses were independently described as READY with the intended Nova 2 Lite model, explicit allowed tools, disabled Memory, invocation limits and session limits.

GitHub Actions run [34768782767](https://github.com/mytestlab123/lab1_agent/actions/runs/34768782767) passed the offline and live jobs against code commit `dc70f90004015adb42fb4b668931259ffb4d3b9d`.

| Check | Result |
| --- | --- |
| Offline fail-closed parser tests | 12 PASS locally and in GitHub Actions |
| Fresh GitHub OIDC identity | Dedicated test role; exact repository/test-branch trust |
| AWS CLI GetHarness | READY for explainer, reader and approval |
| Explainer SDK invocation | end_turn; zero tools; NOT LIVE VERIFIED |
| Reader SDK invocation | end_turn; exactly one expected tool; matching provider result |
| Approval REJECTED fixture | one typed request_approval; same-session matching result; end_turn |
| Approval APPROVED fixture | one typed request_approval; same-session matching result; end_turn |
| Explainer and reader forbidden write/shell prompts | zero tool executions |
| Native AgentCore CLI explainer | end_turn; zero tools |
| Native AgentCore CLI reader | end_turn; expected tool; value/version match independent SSM read |
| Native AgentCore CLI approval | real typed request_approval; stops at tool_use |
| Parameter before/after | desired-v1, version 4; unchanged |
| Authenticated Console Playground clicks | NOT_TESTED; no logged-in browser connected |
| GUI approval-result controls | NOT_TESTED; use the validated terminal helper for full resume |

The native CLI approval test validates the interrupt, not a complete interactive TUI resume. Full reject/approve continuation was tested with the repo's boto3 terminal helper. Automated decisions are labeled test fixtures and do not prove a human identity or production approval ledger.

## Independently checked through AWS Core

- Fresh STS identity and Singapore region matched the approved personal lab.
- The three deployed defaults were read back before invocation; no per-call overrides were used to rescue incorrect defaults.
- Explainer, reader and typed approval interrupt worked through real InvokeHarness calls.
- SSM returned the same String value/version independently.
- Reader Lambda permissions contain only exact GetParameter and own log writes; no managed policies attached.
- Dedicated Gateway is READY / AWS_IAM / Policy ENFORCE.
- Lambda-side LAB_SETTING_READ events record version 4 / COMPLIANT.

## Tested versions

AWS CLI 2.36.40; native AgentCore CLI 1.0.0-preview.30; boto3/botocore 1.43.93; GitHub runner Python 3.13.15; Node 22.23.2. Local offline parser tests also passed with Python 3.13.5.

## Useful failure found and fixed

The first CLI test run failed because our evidence parser looked for `start.name`. The native CLI emits `start.toolUse.name`, while boto3 uses the AWS event envelope. The agent read succeeded; the test correctly refused to mark its evidence PASS. The parser was corrected and the full suite rerun successfully. A CLI exit code or JSON success flag alone is insufficient for a typed-tool proof.

## Scope and retention

No SecCop modifications, parameter write, reset, EC2/NAT/database or scheduled workload. Retain the three bounded Harnesses and their minimal usage-priced dependencies. This is a learning suite, not a replacement for durable, authenticated, single-use business approval enforcement.
