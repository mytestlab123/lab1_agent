# Sources and implementation decisions

Primary sources checked during Issue #28:

- [Harness getting started](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html): CLI/SDK invocation, READY lifecycle, streamed response.
- [Harness tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html): Gateway integration, tool allowlists and inline-function pause/resume.
- [Harness security](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html): caller permissions, execution roles and trusted invocation overrides.
- [Harness CloudFormation resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-harness.html).
- [GatewayTarget CloudFormation resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-gatewaytarget.html).
- [Native CLI invocation](https://github.com/aws/agentcore-cli/blob/main/src/cli/commands/invoke/command.tsx) and [event types](https://github.com/aws/agentcore-cli/blob/main/src/cli/aws/agentcore-harness.ts).
- [AWS Console Playground link generation](https://github.com/aws-samples/sample-playwright-cli-browser-agent-on-bedrock-agentcore/blob/main/harness/deploy.py). Used only to identify the documented UI route, not to copy that sample's broad permissions or browser deployment.
- [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

AWS Core amazon-bedrock skill references for Harness/Gateway were also read before deployment. Service readback, not a sample's outdated status label or remembered default, determines readiness.

## Decisions

No tools for pasted explanations. One exact SSM String parameter for live state, with no model-supplied resource selector. A separate inline-only approval simulation shares the model-only role. None of the execution roles has remediation permissions. No Gateway is connected to the approval Harness.

Persist defaults in CloudFormation so Console users do not have to supply hidden per-invocation model/tool overrides. Reuse the existing lab parameter, but create dedicated learning dependencies rather than change SecCop resources. Caller roles use OIDC rather than stored AWS keys.

## Boundaries

`allowedTools` restricts the model's normal tool selection, not every action an IAM-authorized caller could request via invocation overrides. Direct authorized Harness users are trusted. These examples are not an untrusted multi-user production service. The terminal helper validates typed approval, but does not implement a durable signed approval ledger.

Native CLI invocation by ARN was tested without an AgentCore project or redeployment. Native CLI typed interrupt was tested; complete APPROVED/REJECTED resume uses the repo helper. AWS Console clicks and GUI tool-result submission remain untested.
