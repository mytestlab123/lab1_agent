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
- Experiment 01 proved AgentCore Runtime direct-code Python deployment with IAM/SigV4 invocation and was merged in PR #14.
- Experiment 02 proved AgentCore Gateway + Policy ENFORCE with one Lambda-backed MCP tool.
- Experiment 02 proved ALLOW caused one provider execution while DENY caused zero additional provider executions.
- Experiment 02 cloud resources were fully torn down after verification.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged.

## Active Work

- Issue #15 result: PASS; branch contains the durable Experiment 02 package for final PR merge.
- Documentation goal: publish accumulated learning through MkDocs Material + GitHub Pages.

## Next Action

1. Merge the completed Experiment 02 package.
2. Add MkDocs Material + GitHub Pages documentation site and convert the accumulated learning into navigable pages.
3. Begin Experiment 03: minimal Human Approval Harness with `ALLOW | DENY | APPROVAL_REQUIRED` while retaining AgentCore Policy as the final enforcement boundary.
