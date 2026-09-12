# Specification

Status: ACTIVE
Context: PERSONAL
Environment: LAB

## Objective

Prove that a fresh ChatGPT session can safely reuse AWS operating knowledge from `mytestlab123/chatgpt-aws` without relying on another chat's memory.

## Outcome

One reviewable PR that initializes this consumer repository, verifies fresh-session GitHub/AWS Core access with read-only AWS calls, records public-safe evidence, and defines one next experiment without executing it.

## Authorized

- Read `mytestlab123/chatgpt-aws` as the reusable AWS knowledge source.
- Read/write this repository for Issue #3 documentation and initialization.
- Use AWS Core for STS and representative read-only AWS API calls in the personal LAB account.
- Inspect IAM/OIDC trust configuration read-only.

## MUST

- Re-verify AWS identity in this session.
- Verify the intended LAB region.
- Verify GitHub access and repository state.
- Keep exact account/principal/role/resource identifiers out of committed public-facing evidence.
- Record whether knowledge reuse succeeds without Amit repeating prior setup.
- Keep the next persistent-IaC/drift experiment as design only in this PR.

## MUST NOT

- Create, update, delete, deploy, or destroy AWS resources.
- Modify IAM/OIDC trust or permissions.
- Add AWS access keys or other long-lived credentials.
- Commit credentials, tokens, authentication state, raw AWS inventory, exact account IDs, principal ARNs, repo-external role ARNs, or sensitive resource names.
- Assume a GitHub OIDC role created for another repository is reusable here.

## Milestones

1. Reconcile repository truth and initialize the lab.
2. Fresh AWS Core identity/tool verification.
3. GitHub access/state verification.
4. Representative STS/EC2/S3/IAM read proof.
5. Knowledge-reuse and publication-boundary proof.
6. Recommend one persistent IaC + OIDC + drift experiment; do not execute it.

## Verification

- Fresh STS `GetCallerIdentity` succeeds.
- Read-only EC2, S3, and IAM/OIDC calls succeed.
- Current repository metadata confirms private + unarchived state.
- Existing OIDC proof role trust is inspected read-only and shown to be repository-bound.
- PR contains only public-safe evidence.

## Stop Gates

Stop if the AWS account/environment does not match the intended personal LAB, if GitHub repository identity is wrong, if a requested step would mutate AWS/IAM, or if verification cannot be completed safely.

## Acceptance

Result is `PASS`, `PARTIAL`, or `BLOCKED`; all successful checks are documented without exposing environment-specific identifiers; no AWS mutation occurs.
