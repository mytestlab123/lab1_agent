# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws` (read as reusable AWS knowledge source)
- Context: PERSONAL
- Environment: LAB

## Current Truth

- This repository is public and unarchived.
- Cross-session AWS Core/GitHub knowledge reuse is proven.
- Public-safe GitHub OIDC -> Terraform -> AWS deploy/drift/reconciliation is proven.
- Pull-request Terraform validation is AWS-free and uses a committed provider lockfile.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- Experiment 01 proved AgentCore Runtime direct-code Python deployment with IAM/SigV4 invocation.
- Experiment 01 used no Cognito, frontend, ECR, CodeBuild, VPC, or Bedrock model call.
- Experiment 01 cloud resources were fully torn down after verification; no AgentCore Runtime from the experiment is retained.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged.

## Active Work

- Issue: #13 — AgentCore Runtime direct-code IAM proof.
- Branch: `issue-13-agentcore-runtime`.
- Result: PASS; preparing the final review/merge package with code, reproducible scripts, source ledger, evidence, and lessons.

## Next Action

- Review and merge the Issue #13 PR.
- Then open exactly one next experiment: AgentCore Gateway + Policy ALLOW/DENY with one harmless read-only tool and proof that DENY causes zero provider execution.
