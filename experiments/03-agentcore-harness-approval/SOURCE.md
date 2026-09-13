# Sources — Experiment 03

Primary AWS sources used for this experiment:

- AgentCore Harness overview  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Harness tools / inline functions  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html
- Harness security and execution role  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html
- CreateHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateHarness.html
- InvokeHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html
- Human-in-the-loop guidance  
  https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html

## AWS sample used to close the proof

The working pause/resume contract was studied from the public AWS sample repository:

- repository: `aws-samples/sample-sentinel-harness`
- scenario: `scenarios/scenario_hitl_resume.py`
- supporting stream/resume helpers: `sentinel_harness/core.py`
- inspected revision: `98bff3c649978f0301eb7674b2350c16f60a7fcb`

The lab implementation follows the pattern rather than copying the sample verbatim.

## Source-derived contract

AWS documents `inline_function` as a client-side tool. A non-interactive caller receives the tool request, supplies the result externally, and resumes the same Harness session.

The AWS sample makes the wire contract concrete:

```text
assistant: toolUse(toolUseId, name, input)
user:      toolResult(same toolUseId, decision)
```

Every pending tool-use ID must receive a matching tool result before the conversation can safely continue.

## Lab-derived findings

The final live proof used Nova 2 Lite and produced a typed `request_approval` tool-use pause for both reject and approve cases. Both same-session resumptions completed with `end_turn`.

Additional live findings specific to this account/setup:

- the successful Harness used default `allowedTools=["*"]`; earlier restrictive tests did not yield the usable stream;
- `InvokeHarness` caller IAM required both `InvokeHarness` and `InvokeAgentRuntime` on the Harness ARN;
- Claude Sonnet 4.6 invocation was blocked by the account-level Anthropic use-case-details requirement, so Nova 2 Lite was used for the final proof;
- `memory.disabled` is appropriate for this stateless approval experiment.
