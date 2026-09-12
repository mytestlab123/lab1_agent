# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB

## Objective

Prove the smallest useful Amazon Bedrock AgentCore Runtime lifecycle with **direct-code Python deployment + IAM/SigV4 invocation**, while keeping the existing Terraform/OIDC proof unchanged.

## Outcome

One cohesive Issue #13 PR covering:

`minimal HTTP app -> ZIP -> dedicated S3 artifact -> AgentCore Runtime -> IAM InvokeAgentRuntime -> AWS Core verification -> teardown`.

## Authorized

Amit activated the next LAB milestone with `go` on 2026-09-12. Issue #13 defines the bounded mutation scope. Within this PERSONAL/LAB scope ChatGPT may:

- create/delete one dedicated S3 artifact bucket/object for the experiment;
- create/delete one dedicated AgentCore Runtime execution IAM role and inline policy;
- create/invoke/read/delete exactly one AgentCore Runtime in the intended LAB region;
- inspect the experiment Runtime's logs/state;
- stop the experiment runtime session when applicable;
- perform only experiment-owned cleanup.

## MUST

- Re-verify AWS caller identity and intended region before mutation.
- Use direct-code ZIP deployment; no ECR or CodeBuild for this proof.
- Use IAM/SigV4 inbound authentication; no Cognito/JWT yet.
- Use a deterministic HTTP app with `POST /invocations` and `GET /ping` on port 8080.
- Avoid Bedrock model invocation in this milestone.
- Keep execution-role permissions to the minimum required Runtime/logging/telemetry set; do not add unrelated service access.
- Independently verify Runtime state and invocation through AWS Core.
- Tear down experiment-owned Runtime, artifact bucket/object, and execution role after proof.
- Keep committed evidence public-safe; do not commit account IDs, principal ARNs, runtime ARNs, or credentials.

## MUST NOT

- Modify or widen the existing GitHub OIDC Terraform role.
- Modify the Terraform state bucket or drift-proof SSM parameter except normal read-only verification if needed.
- Create Cognito, CloudFront, frontend hosting, Gateway, Policy, VPC/networking, ECR, CodeBuild, databases, or static AWS credentials.
- Reuse unrelated IAM roles merely because they already exist.
- Retain experiment cloud resources after acceptance unless Amit explicitly changes the retention decision.

## Milestones

1. Rebaseline repository docs and record the upstream source ledger.
2. Implement/test a dependency-free AgentCore HTTP app and ZIP packager.
3. Create dedicated artifact storage and a dedicated Runtime execution role.
4. Deploy one direct-code Runtime and invoke it once through IAM/SigV4.
5. Independently verify provider state/log evidence and record sanitized results.
6. Tear down experiment-owned AWS resources and return KEEP/DROP decisions.

## Verification

- `AWS::BedrockAgentCore::Runtime` is available in the intended region.
- Pre-deployment readback shows no conflicting experiment Runtime.
- Unit tests pass for direct/wrapped prompt payloads and invalid input.
- Runtime reaches a ready state.
- `InvokeAgentRuntime` returns the deterministic `AgentCore Runtime OK` response.
- Provider readback confirms IAM auth/direct-code Runtime and no skipped full-stack components.
- Cleanup readback confirms the experiment Runtime, artifact bucket, and execution role are gone.

## Stop Gates

Stop if caller identity/region differs from the intended PERSONAL/LAB target, direct-code deployment requires broad/unclear permissions, deployment requires unrelated public/network resources, or experiment-resource ownership/cleanup becomes ambiguous.

## Acceptance

Return `PASS | PARTIAL | BLOCKED` with one successful deterministic AgentCore Runtime invocation, independent verification, clean teardown, no model/Cognito/ECR/CodeBuild dependency, and one recommended next milestone.
