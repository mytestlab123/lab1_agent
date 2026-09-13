# AgentCore Gateway and Policy

Experiment 02 verified a managed Gateway with an attached Policy Engine using a single read-only Lambda tool.

The important result was that an allowed tool request reached the provider, while a denied request was stopped before the provider ran. The provider log count was used as independent evidence.

## What to remember

- Gateway is the managed MCP tool boundary.
- Policy is evaluated separately from the model prompt.
- IAM/SigV4 works well for AWS-internal lab callers.
- Policy analysis can flag rules that are intentionally too broad or too restrictive.
- Provider-side markers are useful when testing negative cases.
- Temporary experiment resources were removed after verification.

For the full experiment source and detailed learning record, open `experiments/02-agentcore-gateway-policy/` in the repository.
