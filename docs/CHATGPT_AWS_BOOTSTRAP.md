# ChatGPT AWS Bootstrap

Purpose: let a separate ChatGPT session working on this repository reuse the proven AWS Core MCP + GitHub/OIDC operating model without depending on another chat's memory.

## Source of truth

Detailed environment-specific knowledge lives in private `mytestlab123/chatgpt-aws`:

- `docs/PORTABLE_AWS_MCP_KNOWLEDGE.md`
- `docs/SESSION_BOOTSTRAP.md`
- `docs/EXPERIMENTS.md`

A ChatGPT session with the connected GitHub app should read those files directly before AWS work here.

## New-session procedure

1. Read the three private source-of-truth files above.
2. Read this repository's `AGENTS.md`, `CONTEXT.md`, `SPEC.md`, `ENV.md`, and active Issue/PR.
3. Verify AWS Core in this session with STS `GetCallerIdentity` before any AWS mutation.
4. Confirm the intended PERSONAL/LAB environment and `ap-southeast-1` region.
5. Use direct AWS MCP for discovery, troubleshooting, live provider readback, independent verification, and bounded reversible operations when authorized.
6. Use GitHub + IaC + OIDC for durable infrastructure.
7. Never assume an OIDC role created for another repository can be reused here; verify repository-specific trust first.
8. After any future cloud mutation, verify actual provider state and write public-safe evidence back to GitHub.

## Portability rule

**Git carries knowledge, not authentication.**

Each new session must separately verify:

- AWS Core authentication;
- active AWS account/principal;
- GitHub access;
- AWS/GitHub tool surface exposed in that session;
- current repository Issue/PR authority;
- current live AWS resource state when relevant.

## Execution paths

Use **direct AWS MCP** primarily for inspection, troubleshooting, logs, live readback, independent verification, and small reversible operations when authorized.

Use **GitHub + IaC + OIDC** for persistent infrastructure that should be reviewable, reproducible, rebuildable, or destroyable from code.

Preferred durable loop:

`ChatGPT -> GitHub/IaC -> GitHub Actions/OIDC -> AWS -> AWS MCP verification`

## Publication boundary

This repository is currently private, but committed content should remain public-safe so a later public transition is simpler.

- Do not copy exact AWS account IDs, caller/principal ARNs, repo-external role ARNs, raw inventory, or sensitive resource names here.
- Do not store AWS access keys for GitHub Actions; prefer OIDC.
- Future workflow configuration should use GitHub Variables for ordinary environment-specific values and Secrets only for genuine secrets or values Amit intentionally wants hidden.
- Detailed environment truth may stay in private `mytestlab123/chatgpt-aws` when no workflow needs it.

See `docs/PUBLICATION_BOUNDARY.md`.
