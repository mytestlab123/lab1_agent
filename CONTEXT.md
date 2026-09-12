# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws` (read as reusable AWS knowledge source)
- Context: PERSONAL
- Environment: LAB

## Current Truth

- Cross-session AWS MCP consumer proof completed in merged PR #4.
- This repository is public and unarchived.
- Reusable AWS Core/MCP + GitHub/OIDC knowledge lives in private `mytestlab123/chatgpt-aws`.
- The persistent GitHub OIDC -> Terraform -> AWS path and drift/reconciliation proof are complete.
- A repo-specific GitHub OIDC role is scoped to this repository's immutable identity and `main` only.
- A small encrypted, versioned, public-blocked S3 bucket is retained for Terraform state.
- The only Terraform-managed target is one non-sensitive SSM String parameter.
- Runtime AWS identifiers are provided through repository Variables; no long-lived AWS access keys are used.
- Pull-request Terraform validation is intentionally AWS-free: read-only GitHub token, backend disabled, no OIDC, no plan/apply.

## Active Work

- Issue: #11 — public-safe Terraform PR validation and provider lockfile.
- PR: #12 — add PR-only validation and commit the provider lockfile.
- Branch: `issue-11-terraform-pr-ci`.
- Current milestone: merge after PR validation passes, then confirm the existing `main` OIDC deployment remains green with no infrastructure change.

## Next Action

- Review and merge PR #12.
- Confirm the `main` Terraform workflow reports no changes.
- Then start one small AgentCore Runtime hands-on experiment rather than adding more CI ceremony.
