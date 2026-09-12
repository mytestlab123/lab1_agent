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

## Packaging

The direct-code ZIP needs only `main.py` for this deterministic proof:

```bash
python experiments/01-agentcore-runtime/scripts/package.py
```

This writes `.build/agentcore-runtime/deployment_package.zip` and does not include credentials or environment identifiers.

## Cloud lifecycle

The owning Issue #13 authorizes one dedicated Runtime execution role, one dedicated artifact bucket/object, one Runtime, one harmless invocation, provider verification, and teardown. Exact account/resource identifiers are intentionally not stored in this public repository.

See `SOURCE.md` for upstream classification and `LEARNINGS.md` for the verified result.
