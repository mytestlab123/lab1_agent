# Harness example test results

**Service/API and terminal examples: PASS. Manual Console/operator verification: PASS (user-reported 2026-09-14 SGT).**

[Open the prompts and Console/CLI steps](harness-examples.md).

| Example | SDK/terminal helper | Native AgentCore CLI | AWS CLI |
| --- | --- | --- | --- |
| Finding explainer | PASS, no tools, end_turn | PASS, no tools, end_turn | READY |
| Exact live AWS reader | PASS, one tool and independent SSM match | PASS, provider result and end_turn | READY |
| Approval practice | PASS, REJECTED and APPROVED same-session resume | PASS, real tool_use interrupt; full resume uses helper | READY |

12 offline parser tests passed. Write/shell requests to the explainer and reader produced no tool execution. The existing parameter stayed desired-v1 / version 4. The reader's execution permissions contain only exact SSM read and its own logging.

Verified GitHub Actions [run 34768782767](https://github.com/mytestlab123/lab1_agent/actions/runs/34768782767), plus final-head live/strict-doc validation on run `34769104231`. Tested AWS CLI 2.36.40, AgentCore CLI 1.0.0-preview.30, boto3/botocore 1.43.93, Node 22.23.2, Python 3.13.15.

The original automated run had no authenticated Console browser, so it correctly recorded GUI as NOT_TESTED. On 2026-09-14 SGT Amit subsequently reported that the remaining manual tests passed. Preserve that provenance: manual Console/operator PASS is user-reported, while API/CLI/SDK evidence is independently recorded in the repository and GitHub Actions.

Automated approval decisions were test fixtures, not authenticated human approvals. No remediation tool exists in these examples.

The first terminal run exposed a test-parser mismatch: native CLI uses `start.toolUse.name`, not `start.name`. Corrected parsing and a full successful rerun prevented a false evidence claim.
