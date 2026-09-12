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
- This repository is private and unarchived.
- Reusable AWS Core/MCP + GitHub/OIDC knowledge lives in private `mytestlab123/chatgpt-aws`.
- Issue #5 owns the persistent IaC + OIDC + drift proof.
- A repo-specific GitHub OIDC role is scoped to `mytestlab123/lab1_agent` `main` only.
- A small encrypted, versioned, public-blocked S3 bucket is retained for Terraform state.
- The only Terraform-managed target is one non-sensitive SSM String parameter.
- No long-lived AWS access keys are used.

## Active Work

- Issue: #5 — persistent IaC + OIDC + drift proof
- Branch: `issue-5-iac-oidc-drift`
- Current milestone: add and validate the main-only GitHub Actions/Terraform path, then prove deploy -> independent verify -> harmless drift -> reconcile -> verify.

## Next Action

- Review and merge the Issue #5 PR so the `main`-scoped OIDC workflow can execute.
- Verify the resulting AWS state with AWS Core, introduce one bounded parameter-value drift, run Terraform reconciliation, and record public-safe evidence.
