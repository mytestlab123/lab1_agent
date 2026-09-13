# Gateway and Policy Notes

The second AgentCore lab verified a managed MCP Gateway with an attached Policy Engine and one read-only provider tool.

## Result

An allowed request reached the provider exactly once. A denied request was stopped at the Gateway policy layer and produced zero additional provider executions.

## Lessons

- The Gateway is a useful managed tool boundary.
- Policy enforcement is separate from model prompting.
- IAM/SigV4 is suitable for AWS-internal lab callers.
- Strict policy analysis can identify rules that are too broad or intentionally restrictive.
- Provider-side execution markers are useful for proving negative cases.
- Temporary resources should be removed after the experiment.

The complete implementation record is available under `experiments/02-agentcore-gateway-policy/`.
