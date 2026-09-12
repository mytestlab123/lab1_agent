# ChatGPT AWS Consumer Lab

A small personal LAB repository for proving that a fresh ChatGPT session can reuse AWS operating knowledge from `mytestlab123/chatgpt-aws` without depending on previous-chat memory.

## Current focus

Issue #3 proves the cross-session consumer path with connected GitHub + AWS Core using read-only AWS verification only.

The reusable AWS/MCP knowledge remains centralized in private `mytestlab123/chatgpt-aws`; this repository keeps only project-specific, public-safe decisions and evidence.

## Start Here

1. Read `AGENTS.md`.
2. Read `CONTEXT.md` for current project truth and active work.
3. Read `docs/CHATGPT_AWS_BOOTSTRAP.md` for the cross-session AWS bootstrap.
4. Read `ENV.md` for runtime/tool/environment expectations.
5. Read `SPEC.md` before implementation, AWS mutation, deployment, or cleanup.
6. Read `CHATGPT.md` for ChatGPT-Codex-GitHub collaboration rules.

## Publication boundary

Treat repository content, Issue/PR text, and Git history as potentially public.

Do not commit exact environment identifiers or credentials. If future workflows need environment-specific values, prefer GitHub repository/environment **Variables** for non-secret configuration and **Secrets** only for actual secrets or values Amit intentionally wants hidden. Prefer GitHub OIDC over stored AWS access keys.

See `docs/PUBLICATION_BOUNDARY.md` for what can and cannot be moved into Variables/Secrets.
