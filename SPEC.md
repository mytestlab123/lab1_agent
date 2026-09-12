# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB

## Objective

Prove one small persistent AWS IaC lifecycle from `mytestlab123/lab1_agent` using GitHub Actions + repository-scoped OIDC, then independently verify and detect one harmless drift with AWS Core MCP.

## Outcome

One cohesive Issue #5 PR and provider proof covering:

`GitHub Actions -> OIDC -> repo-scoped IAM role -> Terraform -> one SSM parameter -> AWS Core verification -> harmless drift -> Terraform reconciliation -> AWS Core verification`.

## Authorized

Amit activated Issue #5 with `go` on 2026-09-12. Within this PERSONAL/LAB scope ChatGPT may:

- create/update the repo-specific GitHub OIDC IAM role and least-privilege inline policy;
- create/retain one hardened S3 bucket for Terraform remote state;
- create/update/delete only the Issue #5 test SSM String parameter;
- run the GitHub Actions/Terraform workflow;
- introduce one reversible value-only drift to that parameter;
- reconcile it through Terraform;
- perform provider readback and bounded cleanup/retention checks.

## MUST

- Use GitHub OIDC; no static AWS access keys.
- Trust only `repo:mytestlab123/lab1_agent:ref:refs/heads/main` with audience `sts.amazonaws.com`.
- Do not trust `pull_request` subjects.
- Keep the IAM permissions limited to the state bucket and target parameter.
- Keep the state bucket encrypted, versioned, and blocked from public access.
- Use exactly one Terraform-managed target resource: a non-sensitive SSM String parameter.
- Verify deploy, drift, and reconciliation independently through AWS Core.
- Keep committed evidence public-safe enough for a later publication review.

## MUST NOT

- Create long-lived AWS credentials.
- Widen the OIDC trust beyond this repository's `main` branch.
- Modify unrelated IAM roles, buckets, parameters, or AWS resources.
- Create networking, compute, databases, public endpoints, or expensive services.
- Treat role ARNs/account IDs as credentials; however avoid duplicating identifiers where workflow execution does not require them.

## Milestones

1. Public-safe OIDC/Terraform design.
2. Bootstrap repo-scoped OIDC role and hardened state bucket.
3. Deploy one persistent SSM parameter through GitHub Actions/Terraform.
4. Independently verify provider state through AWS Core.
5. Introduce one value-only drift, detect/reconcile it through Terraform, verify again.
6. Record retention/publication result and whether the repository is technically ready for public visibility.

## Verification

- IAM trust readback confirms exact `main`-only subject.
- IAM policy readback confirms state-bucket + target-parameter scope only.
- S3 readback confirms encryption, versioning, and full public-access block.
- GitHub Actions run succeeds using OIDC.
- AWS Core reads the target parameter after deployment.
- AWS Core changes only the test value to the drift marker and confirms it.
- Terraform restores the desired value.
- AWS Core confirms final reconciled state.

## Stop Gates

Stop if the AWS account/environment differs from the intended PERSONAL/LAB target, if workflow OIDC trust does not match the exact repository/main subject, if validation would require widening IAM/network/public exposure, or if cleanup/retention state becomes ambiguous.

## Acceptance

Return `PASS | PARTIAL | BLOCKED` with one workflow-backed persistent resource, independent provider verification, one harmless drift/reconciliation proof, no static AWS credentials, and a publication-readiness verdict.
