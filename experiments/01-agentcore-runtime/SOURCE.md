# Source Ledger

## Primary upstream reference

- Repository: `aws-samples/sample-amazon-bedrock-agentcore-fullstack-webapp`
- Source URL: https://github.com/aws-samples/sample-amazon-bedrock-agentcore-fullstack-webapp
- Reviewed commit: `7a9e70f3abc879b736f0011657462023746f0c36`
- License: MIT No Attribution

## Classification

| Upstream item | Decision | This experiment |
|---|---|---|
| `agent/strands_agent.py` | ADAPT | Keep the idea of one clear AgentCore entrypoint and simple request handling, but implement the HTTP service contract with Python stdlib for the first deterministic proof. |
| `cdk/lib/runtime-stack.ts` | LEARN | Learn the Runtime lifecycle, IAM role, network mode, and endpoint concepts. Do not copy the full stack. |
| Cognito/JWT auth | SKIP | Default IAM/SigV4 inbound auth is enough for the first Runtime proof. |
| React + CloudFront frontend | SKIP | No UI is needed to prove Runtime hosting/invocation. |
| ECR + CodeBuild container pipeline | SKIP | Current AgentCore direct-code deployment supports a ZIP artifact in S3. |
| Lambda build waiter | SKIP | It exists to coordinate the sample's CodeBuild path and is unnecessary for direct code. |
| Strands tools/model call | SKIP | First isolate Runtime itself with a deterministic response and zero model cost. |

## Additional authoritative references

AWS AgentCore Runtime documentation was used to confirm:

- HTTP apps must expose `POST /invocations` and `GET /ping` on port `8080`;
- direct-code Python deployment accepts a ZIP archive from S3;
- direct-code Runtime supports Python 3.13 and an explicit entry point;
- IAM/SigV4 is a supported/default inbound authentication mechanism.

No upstream repository was copied wholesale.
