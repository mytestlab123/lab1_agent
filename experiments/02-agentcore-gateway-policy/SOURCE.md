# Sources — Experiment 02

The implementation and conclusions in this experiment were checked against AWS documentation current during the live lab.

## AgentCore Gateway

- Create an AgentCore gateway using the API  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create-api.html
  - used for MCP Gateway creation;
  - confirmed `AWS_IAM` inbound authorization;
  - confirmed Boto3/API path rather than the starter CLI for IAM-authenticated Gateway creation.

- Set up permissions for AgentCore Gateway  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites-permissions.html
  - used for the Gateway service-role trust model;
  - used for exact Lambda invocation permission guidance;
  - documents the create-first/tighten-later `aws:SourceArn` pattern when the final Gateway ARN is initially unknown.

- AWS Lambda function targets  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-lambda.html
  - used for the Lambda target event/context contract.

- Call a tool in an AgentCore gateway  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-call.html
  - used for MCP `tools/call` request shape and protocol headers.

## AgentCore Policy

- Getting started with Policy in AgentCore  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-getting-started.html
  - used for Policy Engine + Gateway enforcement concepts;
  - documents Cedar resource binding and the two-phase Gateway/policy relationship.

- Create gateway with Policy Engine  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-gateway-with-policy.html
  - used for Gateway `policyEngineConfiguration` with `ENFORCE` mode.

- AgentCore Gateway and Policy IAM permissions  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-permissions.html
  - confirmed that a custom Gateway execution role requires `GetPolicyEngine`, `AuthorizeAction`, and `PartiallyAuthorizeActions`.

- Core concepts  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html
  - used for `AgentCore::IamEntity` principal behavior for IAM-authenticated Gateways.

- Policy conditions  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-conditions.html
  - confirmed the stable assumed-role ARN form used by IAM principals in Cedar.

- CreatePolicy API  
  https://docs.aws.amazon.com/boto3/latest/reference/services/bedrock-agentcore-control/client/create_policy.html
  - used for Cedar definitions, validation mode, enforcement mode, default-deny behavior and policy lifecycle.

## Interpretation boundary

AWS documentation supplies the service contracts and policy semantics. The specific conclusion that **DENY caused zero provider executions** is not copied from documentation; it is the result of this lab's controlled live test and independent Lambda-log measurement.
