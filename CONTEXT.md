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
- Experiment 01 proved AgentCore Runtime direct-code Python deployment with IAM/SigV4 invocation.
- Experiment 02 proved AgentCore Gateway + Policy ENFORCE with one Lambda-backed MCP tool: ALLOW executed once; DENY added zero provider executions.
- Experiment 03 proved AgentCore Harness human approval with a real typed `request_approval` `tool_use` pause and same-session REJECTED/APPROVED resume paths.
- Experiment 03 final proof used Nova 2 Lite and performed no real provider mutation.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged.

## Documentation

- MkDocs Material build: PASS.
- GitHub Pages artifact upload: PASS.
- Live Pages deployment still requires repository **Settings -> Pages -> Source = GitHub Actions**.

## Active Work

- Issue #17: finalize durable Experiment 03 evidence and cleanup.
- Issue #16: publish the already-building MkDocs site after the one GitHub Pages repository setting is enabled.

## Next Action

1. Complete Experiment 03 cleanup and merge its public-safe evidence/docs.
2. Enable GitHub Pages source = GitHub Actions and verify the live learning site.
3. Begin Experiment 04: human approval -> Gateway -> Policy -> provider, proving reject / policy deny / policy allow independently.
