# Sources — Experiment 03

Primary AWS sources used for this experiment:

- AgentCore Harness procedure and security model  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html

- Harness tools / inline functions  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html

- Harness security and execution role  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html

- CreateHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateHarness.html

- InvokeHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html

- AWS guidance for human-in-the-loop approval patterns  
  https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html

## Source-derived expectations

AWS documents `inline_function` as a client-side tool: when the agent calls it, Harness returns the tool call to the caller for external execution. In non-interactive operation, the expected stream stops for tool use and the caller later supplies the tool result.

## Lab-derived finding

The configured Harness became READY and model inference worked, but the bounded model tests did not emit the required typed `tool_use` event. That result is specific to this live experiment and is not inferred from AWS documentation.
