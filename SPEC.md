# Specification

Status: IMPLEMENTED / SERVICE AND TERMINAL TESTS PASS
Context: PERSONAL
Environment: LAB
Issue: #28
PR: #29
GUI verification: NOT_TESTED

## Objective delivered

Three retained AgentCore Harness examples in ap-southeast-1:

1. lab1_demo_explainer: pasted finding, no effective tools, NOT LIVE VERIFIED output.
2. lab1_demo_reader: one exact existing lab SSM String read through a dedicated Gateway/Policy/Lambda path.
3. lab1_demo_approval: DEMO_ONLY typed inline-function pause and same-session reject/approve simulation. No remediation tool or real human-identity claim.

## Verified acceptance

- One versioned CloudFormation stack reached CREATE_COMPLETE; all three Harnesses reached READY with the intended persisted model/tools/memory/limits.
- Real AWS Core and SDK invocations, independent unchanged SSM value/version, and provider-side read logs.
- AWS CLI GetHarness for all three; native AgentCore CLI complete explainer/reader and typed approval interrupt.
- SDK terminal helper completed both explicit simulation decisions to end_turn with matching toolUseId and unchanged session.
- 12 offline fail-closed tests; forbidden write/shell prompts made no tool calls.
- Full terminal test run 34768782767 PASS. Detailed evidence and versions: experiments/08-operator-harness-examples/RESULTS.md.

## GUI limitation

No authenticated Console browser is connected. Console Playground steps and route are documented from an AWS sample, but clicks and inline-result controls are NOT_TESTED. Full validated decision/resume is available through the terminal helper. Do not relabel this limitation as a browser PASS.

## Scope preserved

Only lab1_agent code/docs and dedicated personal-lab resources. SecCop remains read-only and untouched. Existing SSM parameter is read-only. No static AWS credentials, arbitrary resource selector, remediation/reset, EC2/NAT/database/public app server or scheduled workload.

## Retention and limits

Retain useful usage-priced resources. Each Harness: 3 iterations, 1,024 output tokens, 90-second invocation timeout, 300-second idle timeout, 1,800-second lifetime, Memory disabled. Reader Lambda: 128 MB, 15 seconds, 7-day log retention. Limits are not a monthly billing cap.

## Next

Publish/review this cohesive PR, verify Pages, and let Amit exercise the three already-deployed Console examples. Do not implement the declined audit-correlation adoption proposal or modify SecCop.
