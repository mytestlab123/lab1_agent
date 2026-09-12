# Specification

Status: COMPLETE
Context: PERSONAL
Environment: LAB
Result: PASS

## Objective

Prove the smallest useful Amazon Bedrock AgentCore Runtime lifecycle with **direct-code Python deployment + IAM/SigV4 invocation**, while keeping the existing Terraform/OIDC proof unchanged.

## Outcome

Issue #13 proved:

`minimal HTTP app -> standard ZIP -> dedicated S3 artifact -> AgentCore Runtime -> IAM InvokeAgentRuntime -> AWS Core verification -> teardown`.

## Authorized Scope Used

Amit activated the LAB milestone with `go` on 2026-09-12. The experiment used only bounded resources owned by Issue #13:

- one temporary S3 artifact bucket/object;
- one temporary AgentCore Runtime execution IAM role and inline policy;
- one temporary AgentCore Runtime;
- one temporary branch-scoped OIDC upload role needed only to produce a standards-generated ZIP after the controller sandbox could not;
- one harmless Runtime invocation and associated Runtime logs.

All experiment-owned cloud resources and log groups were deleted after proof.

## Constraints Satisfied

- AWS caller identity and intended region were re-verified before mutation.
- Direct-code ZIP deployment was used; no ECR or CodeBuild.
- IAM/SigV4 inbound authentication was used; no Cognito/JWT.
- The deterministic HTTP app implemented `POST /invocations` and `GET /ping` on port 8080.
- No Bedrock model invocation was used.
- Runtime execution-role access was limited to Runtime logging/telemetry plus exact artifact read access; no unrelated service access was added.
- Runtime state, invocation, and logs were independently verified through AWS Core.
- No account IDs, principal ARNs, Runtime ARNs, credentials, or generated resource IDs are retained in the final repository files.
- Existing GitHub OIDC Terraform role, Terraform state bucket, and drift-proof SSM parameter were not modified.

## Verification Result

- AgentCore Runtime resource type was available in the LAB region: PASS.
- Pre-deployment readback found zero conflicting Runtimes: PASS.
- Unit tests for direct/wrapped prompt payloads and invalid input: PASS.
- Runtime reached `READY`: PASS.
- `InvokeAgentRuntime` returned HTTP 200 and the deterministic `AgentCore Runtime OK` response: PASS.
- Provider readback confirmed direct-code Python 3.13, HTTP protocol, and no custom authorizer: PASS.
- Runtime logs confirmed the server started, the invocation returned 200, and `/ping` health checks returned 200: PASS.
- Runtime session stop: PASS.
- Runtime/artifact bucket/execution role/temporary package role/log-group cleanup: PASS.
- Final readback found zero experiment Runtimes and no retained Issue #13 resources: PASS.

## Decisions

- AgentCore Runtime: **KEEP**.
- Direct-code deployment: **KEEP** for small Python experiments.
- IAM/SigV4 inbound auth: **KEEP** as the default AWS-internal/lab path.
- Full sample Cognito/frontend/ECR/CodeBuild architecture: **DEFER** until a use case requires it.

## Next Milestone

AgentCore Gateway + Policy ALLOW/DENY using one harmless read-only tool, with the critical proof that a `DENY` decision results in **zero provider execution**.
