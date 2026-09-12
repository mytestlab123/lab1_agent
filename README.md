# <Project Name>

One sentence explaining the problem this repository solves.

## ChatGPT + AWS sessions

Before AWS work in a new ChatGPT session, read `docs/CHATGPT_AWS_BOOTSTRAP.md`. It points to the private `mytestlab123/chatgpt-aws` source of truth for the proven AWS Core MCP + GitHub/OIDC operating model.

This repository is currently public, so environment-specific AWS account/principal/role details remain in the private source repository.

## Start Here

1. Read `AGENTS.md` for repository rules and read order.
2. Complete `INIT.md` once when the repository is first created from this template.
3. Read `CONTEXT.md` for project identity, current truth, active Issue/PR, and next action.
4. Read `CHATGPT.md` for ChatGPT-Codex collaboration, handoffs, `go` semantics, and repository-mismatch protection.
5. Read `ENV.md` when runtime, cloud, host, profile, or tool dependencies matter.
6. Read `SPEC.md` before implementation, mutation, deployment, cleanup, or trusted-contract changes.

## Template Model

Keep root contracts short and separate by responsibility:

- `AGENTS.md` — router and core repository rules
- `CHATGPT.md` — ChatGPT ↔ Codex collaboration
- `CONTEXT.md` — current project/repository state
- `SPEC.md` — execution authority and milestone contract
- `INIT.md` — one-time short initialization interview
- `ENV.md` — project runtime/tool/cloud dependencies
- `ROADMAP.md` — useful future milestones, not current authority

Prefer one cohesive, reviewable PR containing related phases/tasks over micro-PRs. Reusable cross-project guidance belongs in [Agent OS](https://github.com/amitkarpe/agent-os); machine-specific facts belong in the active `~/.agent/HOST.md` when available.
