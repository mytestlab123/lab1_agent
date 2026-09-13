# Three Harness examples: no product GUI

These are separate retained Harnesses in **Asia Pacific (Singapore), ap-southeast-1**. They do not depend on LibreChat, a custom web server, or the SecCop deployment. Start with the **reader** to see a real AWS read through a managed agent loop.

| Harness | What to learn | What it cannot do |
| --- | --- | --- |
| `lab1_demo_explainer` | Paste a finding and get an explanation | Read live AWS state or change resources |
| `lab1_demo_reader` | Harness -> Gateway -> Policy -> Lambda -> one actual SSM read | Select arbitrary resources or remediate |
| `lab1_demo_approval` | Typed client-tool pause and same-session decision/resume | Perform remediation or prove a person's identity |

## Copy/paste prompts

### 1. Finding explainer

> Pasted finding: a demo security group allows inbound TCP 22 from 0.0.0.0/0. Explain the risk, a proposed fix, and what to verify, in under 120 words. Do not make changes.

Expected: an explanation and proposed checks, explicitly **NOT LIVE VERIFIED**. No tool call. This illustrates why a fluent answer is not evidence of AWS resource state.

### 2. Read-only AWS checker

> Read the current lab setting once. Show its observed value, version, expected value and compliance status. No changes.

Expected: one `ReadLab___check_lab_setting` invocation, a provider value/version and status. The initial independent read found `desired-v1`, version `4`, matching the expected value. Future legitimate changes can change that result; the agent must report the current read, not memorize this page.

The single SSM String parameter is fixed by deployment configuration. The Lambda accepts no resource name or other input and has only exact `ssm:GetParameter` permission plus its own logging. This is a configuration-check learning example, **not an account-wide security scanner**.

### 3. Approval practice

> Start approval practice for DEMO_ONLY. Request my decision and wait. Do not execute any AWS change.

Expected first turn: exactly one `request_approval` with `{"action":"DEMO_ONLY"}` and `stopReason=tool_use`.

Supply `REJECTED` or `APPROVED` using the terminal helper below. It returns the original assistant `toolUse` and a matching user `toolResult` to the same session. The final turn must be `end_turn` and say no AWS action executed. Both outcomes are **simulations**. There is no remediation tool, no authenticated human-identity service and no durable business approval ledger.

## AWS Console GUI

1. Sign in to the same personal AWS lab account used for these examples.
2. Choose **Singapore / ap-southeast-1**.
3. Open **Amazon Bedrock AgentCore**, then **Harnesses**. Select one of the exact names above.
4. Check it is **READY** and uses **Nova 2 Lite**. Do not create another Harness or change the configuration.
5. Open its **Playground/Test** view and paste the matching prompt.
6. Inspect the tool/result details rather than treating model prose as evidence. Use a new session when switching examples or repeating approval practice.

An AWS-owned sample prints the Console route in this form:

```text
https://ap-southeast-1.console.aws.amazon.com/bedrock-agentcore/harnesses/playground?id=<harnessId>
```

Use the resource's actual ID, obtained from the Console or `list-harnesses`; never substitute just the friendly name.

**GUI verification boundary:** this work can test authenticated service APIs and terminal clients, but no authenticated AWS Console browser is connected to the test runner. The click path and GUI approval-result controls are **NOT_TESTED**. The Console Playground route is supported by the AWS sample source, not by a claimed browser test here. The inline approval example may require the terminal helper to supply a structured `toolResult`; merely typing "approved" in a chat box is not the validated resume contract.

## Terminal: fastest repeatable path

Use **AWS CloudShell** from the same signed-in account, or a local terminal with an already-configured AWS profile. Do not create or paste long-lived AWS keys. Commands below use Bash (CloudShell/Amazon Linux); the Python helper also works from Windows with `python` and `--profile <your-profile>`.

### A. Check account, Region and deployed examples with AWS CLI

```bash
export AWS_REGION=ap-southeast-1
aws --version
aws sts get-caller-identity
aws bedrock-agentcore-control list-harnesses --region "$AWS_REGION" \
  --query 'harnesses[?starts_with(harnessName, `lab1_demo_`)].[harnessName,status,harnessId]' \
  --output table
```

The expected three names are above. Stop on an account mismatch or absent Harness; do not create duplicates. The operator needs ListHarnesses, GetHarness, InvokeHarness and InvokeAgentRuntime on these examples. InvokeHarness needs the latter two invocation permissions on the Harness ARN; deployment administration is not needed just to chat.

### B. Native AgentCore CLI: no project or redeployment

AWS CLI (`aws`) and AgentCore CLI (`agentcore`) are different programs. Use AWS CLI for control-plane reads; AgentCore CLI handles streaming invocation. Node.js 20+ is required for the native CLI.

```bash
node --version
npm install --global @aws/agentcore@preview
agentcore --version
HARNESS_ARN=$(aws bedrock-agentcore-control list-harnesses --region "$AWS_REGION" \
  --query 'harnesses[?harnessName==`lab1_demo_reader`].arn | [0]' --output text)
agentcore invoke --harness-arn "$HARNESS_ARN" --region "$AWS_REGION" \
  'Read the current lab setting once. Show its value, version and compliance status. No changes.'
```

Repeat by changing `lab1_demo_reader` to `lab1_demo_explainer` and using its prompt. For approval inspection, select `lab1_demo_approval` and add `--verbose` to see typed events. Non-interactive native invocation may stop at the client-tool request rather than prompt for a decision. The helper below provides a complete explicit decision/resume flow.

**Do not run `agentcore create`, `deploy` or `dev` to test these already-created resources.** `agentcore dev` can provision Harness infrastructure before opening the AWS Agent Inspector. It is not merely a browser viewer for this externally managed CloudFormation stack.

### C. Complete approval practice from the terminal

From a new checkout, or use your existing checkout instead of cloning again:

```bash
git clone https://github.com/mytestlab123/lab1_agent.git
cd lab1_agent/experiments/08-operator-harness-examples
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'boto3>=1.43.93,<2'
python examples.py explainer
python examples.py reader
python examples.py approval
```

The last command pauses and asks you to type **REJECTED** or **APPROVED**. Run it twice in separate sessions to try both. Invalid input stops without continuing. The helper never calls a mutation tool.

For an automated **simulation**, explicitly use:

```bash
python examples.py approval --decision REJECTED
python examples.py approval --decision APPROVED
```

These fixtures are not evidence that a human clicked Approve. `test_examples.py` tests malformed/extra tool calls, scope mismatch, missing tool ID, incomplete/error streams and prose masquerading as approval. `live_tests.py` checks the actual service, SDK, native CLI and independent provider read.

## What this teaches about replacing a GUI

A Harness supplies the model/tool loop; the Console Playground or a terminal supplies the interaction. The live checker runs directly through Gateway/Policy to a narrow provider without a product backend. However, durable jobs, authenticated approvers, single-use business approvals, replay prevention and dashboards still require deliberate application design. Do not equate this approval simulation with the SecCop production-style execution boundary.

## Cost and retention

Three Harness definitions are retained; no additional always-on host is deployed. Each uses 3 iterations, 1,024 total output tokens, a 90-second invocation timeout, a 5-minute idle session timeout, a 30-minute maximum session lifetime and no managed Memory. The reader Lambda has 128 MB/15 seconds and 7-day log retention. There is no schedule or background poller.

Harness has no additional fee; model inference, underlying Runtime CPU/memory, Gateway/Policy, Lambda and logging are consumption-priced. An idle retained definition is not the same as an active session: Runtime memory can still accrue during the idle-session window. Small manual tests should be inexpensive, but these limits are **not a monthly spending cap**. Repeated invocations, large inputs or changed overrides can exceed the lab budget.

Sources: [Harness getting started](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html), [tools and inline resume](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html), [security](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html), [AWS Console Playground sample](https://github.com/aws-samples/sample-playwright-cli-browser-agent-on-bedrock-agentcore/blob/main/harness/deploy.py), [native CLI implementation](https://github.com/aws/agentcore-cli/blob/main/src/cli/commands/invoke/command.tsx), [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).
