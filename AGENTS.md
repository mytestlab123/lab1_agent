# AGENTS.md

## Bootstrap / Recovery Order

Use this order for cold start, recovery, materially changed governing context, or stale/incomplete/contradictory state. For warm continuation, use the named Issue/PR, latest relevant authorized delta, and current HEAD; do not reread the full context set on every handoff.

1. `AGENTS.md`
2. `CONTEXT.md`
3. `INIT.md` only when repository initialization is incomplete
4. `CHATGPT.md` when ChatGPT/Codex/GitHub collaboration or connector-safety rules matter
5. `docs/CHATGPT_AWS_BOOTSTRAP.md` when AWS, AWS Core/MCP, GitHub OIDC, or cross-session AWS knowledge is relevant
6. `ENV.md` when runtime, cloud, host, or tool facts matter
7. `SPEC.md` before implementation, mutation, deployment, cleanup, or trusted-contract changes

## Rules

- Follow KISS: optimize for one useful outcome, not the smallest possible task.
- Preserve existing work. Do not revert unrelated changes or use destructive Git actions without authority.
- Keep durable code, decisions, and reports in Git. Never commit secrets, credentials, authentication state, or copied repositories.
- Update `CONTEXT.md` when repository identity, current truth, active Issue/PR, or next action materially changes.
- `SPEC.md` is the repository execution contract. Proceed inside an ACTIVE approved scope and stop on a genuine safety, scope, authorization, repository-identity, access, or validation failure.
- Prefer one cohesive PR with related phases/tasks over micro-PRs. Small isolated fixes may remain small.
- When the current objective is known, short continuation such as `go`, `g`, `.`, `Y`, or `yes` means execute/continue it within existing authority unless Amit explicitly selected plan/review/discussion mode.
- Before cross-repo mutation, apply the repository-binding guard in `CHATGPT.md`.
- For AWS work in a new ChatGPT session, use the shared bootstrap and re-verify STS caller identity; Git carries knowledge, not authentication.
- A previously safety-blocked connector write is not retried merely because a new governance milestone starts; use the owning historical record and current Connector Safety Gate.

## Global Guidance

When available, use `~/.agent/CORE.md` as the shared machine-wide operating contract and `~/.agent/HOST.md` for active host facts. Tool homes such as `~/.codex/` remain tool-specific adapters/runtime state.

Agent OS is reusable guidance, never automatic project authority. Current user instruction plus this repository's `AGENTS.md`, `SPEC.md`, owning Issue/PR, and project context take precedence.
