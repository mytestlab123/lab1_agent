# ChatGPT AWS Bootstrap

Purpose: let a separate ChatGPT session working on this repository reuse the proven AWS Core MCP + GitHub/OIDC operating model without depending on another chat's memory.

## Source of truth

The detailed, environment-specific knowledge lives in the **private** repository:

- `mytestlab123/chatgpt-aws/docs/PORTABLE_AWS_MCP_KNOWLEDGE.md`
- `mytestlab123/chatgpt-aws/docs/SESSION_BOOTSTRAP.md`
- `mytestlab123/chatgpt-aws/docs/EXPERIMENTS.md`

A ChatGPT session with the connected GitHub app should read those files directly before AWS work here.

## Start a new ChatGPT session like this

> Use the connected **GitHub** and **AWS Core** apps. Do not rely on memory from another chat.
>
> 1. Read `mytestlab123/chatgpt-aws/docs/PORTABLE_AWS_MCP_KNOWLEDGE.md`, `docs/SESSION_BOOTSTRAP.md`, and `docs/EXPERIMENTS.md`.
> 2. Read this repository's `AGENTS.md`, `CONTEXT.md`, `SPEC.md`, `ENV.md`, and active Issue/PR.
> 3. Verify AWS Core in this session with STS `GetCallerIdentity` before any AWS mutation.
> 4. Use direct AWS MCP for discovery, troubleshooting, live readback, verification, and small reversible operations.
> 5. Use GitHub + IaC + OIDC for durable infrastructure.
> 6. Do not assume an OIDC role created for another repository can be reused here. Verify or create repo-specific trust first.
> 7. After any cloud mutation, verify actual AWS state and document evidence back in GitHub.

## Important portability rule

**Git carries knowledge, not authentication.**

A new ChatGPT session must separately verify:

- AWS Core is connected/authenticated;
- the active AWS account and principal;
- GitHub can read/write the required repositories;
- the current AWS/GitHub tool surface exposed in that session;
- the active project Issue/PR and repository authority.

Do not treat the existence of these docs as proof that authentication or permissions are still valid.

## Execution-path rule

Use **direct AWS MCP** when the main job is:

- inspect inventory/configuration;
- troubleshoot;
- query logs or CloudTrail;
- perform live provider readback;
- make a bounded, reversible, low-cost operational change;
- independently verify an IaC deployment.

Use **GitHub + IaC + OIDC** when infrastructure should be reproducible, reviewable, rebuildable, or cleanly destroyed later.

Preferred durable loop:

`ChatGPT -> GitHub/IaC -> GitHub Actions/OIDC -> AWS -> AWS MCP verification`

## Repository-visibility note

This repository is **public** at the time this bootstrap was added.

For now:

- keep account IDs, IAM principal ARNs, AWS role ARNs, and other environment-specific details in private `mytestlab123/chatgpt-aws`;
- do not add mutation-capable AWS OIDC deployment workflows here by default while the repository remains public;
- if this repository is made private for the lab, a later milestone can create a repo-specific scoped OIDC role/workflow and then verify it end-to-end.

Before eventually making an AWS-enabled repository public, review workflow triggers, IAM trust, permissions, committed history, and environment details.

## What this repository should not duplicate

Do not copy the entire AWS knowledge base into this repo. Keep the reusable AWS/MCP facts centralized in `mytestlab123/chatgpt-aws` and keep only project-specific decisions/evidence here.

That avoids drift between ChatGPT sessions and repositories.
