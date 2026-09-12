# Experiment 01 — AgentCore Runtime direct-code IAM proof

## Question

Can this LAB deploy and invoke one minimal Amazon Bedrock AgentCore Runtime without first adopting Cognito, a frontend, ECR/CodeBuild, Gateway, or a Bedrock model call?

## Target flow

```text
main.py
  -> ZIP artifact
  -> S3
  -> AgentCore Runtime (direct code, Python 3.13)
  -> IAM/SigV4 InvokeAgentRuntime
  -> deterministic JSON response
```

## Deliberate constraints

- Region: repository `AWS_REGION` / LAB default.
- HTTP protocol only.
- `GET /ping` and `POST /invocations` on port 8080.
- Python standard library only in the deployed app.
- No model invocation and therefore no model cost/permissions in this milestone.
- No Cognito/JWT, browser UI, ECR, CodeBuild, Lambda waiter, VPC, or static AWS credentials.
- Experiment-owned AWS resources are temporary and must be torn down after proof.

## Local tests

```bash
python -m unittest discover -s experiments/01-agentcore-runtime/tests -v
```

Optional local HTTP smoke:

```bash
python experiments/01-agentcore-runtime/app/main.py
curl http://localhost:8080/ping
curl -X POST http://localhost:8080/invocations \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"hello"}'
```

Expected invocation response:

```json
{"response":"AgentCore Runtime OK: hello","status":"success"}
```

## Reproduce the cloud lifecycle

Prerequisites:

- Python 3.10+;
- `boto3` available in the active environment;
- an explicitly authorized PERSONAL/LAB AWS identity with the bounded permissions required by Issue #13.

Build the standard direct-code ZIP:

```bash
python experiments/01-agentcore-runtime/scripts/package.py
```

This writes `.build/agentcore-runtime/deployment_package.zip` and does not include credentials or environment identifiers.

Deploy the temporary artifact bucket, execution role, and Runtime:

```bash
python experiments/01-agentcore-runtime/scripts/deploy.py
```

Invoke through IAM/SigV4:

```bash
python experiments/01-agentcore-runtime/scripts/invoke.py
```

Tear down all experiment-owned resources:

```bash
python experiments/01-agentcore-runtime/scripts/teardown.py
```

The scripts keep exact generated identifiers only in the ignored local `.runtime-state.json` file. They do not modify the existing GitHub/Terraform OIDC role, state bucket, or SSM drift-proof parameter.

## Result

**PASS.** The live proof reached Runtime `READY`, returned the expected deterministic HTTP 200 response through `InvokeAgentRuntime`, produced Runtime/health-check logs, and completed a clean teardown. See `LEARNINGS.md` for the provider evidence and decisions.

See `SOURCE.md` for upstream classification.
