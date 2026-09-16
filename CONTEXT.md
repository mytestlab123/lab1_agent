# Context

Status: ACTIVE
Updated: 2026-09-17

> Current-only restart state. Completed experiment/connector history belongs in Git and owning Issues/PRs.

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent` (public)
- Current merged `main`: `448cb6b1143abd2a526daf2e7bec259fb0744903`
- Related public knowledge source: `mytestlab123/chatgpt-aws`
- Context: PERSONAL / LAB / ap-southeast-1
- SecCop source: `amitkarpe/aws-secops`; READ-ONLY for this work unless separately authorized

## Current Truth

- GitHub OIDC -> Terraform -> AWS drift/reconciliation remains a proven historical lab path.
- Experiments 01-08 and their docs own detailed evidence/limitations.
- The three operator Harness examples remain recorded as deployed/READY at their accepted milestone; re-verify current AWS state before relying on that runtime claim.
- Approval remains DEMO_ONLY simulation, not a real remediation or authenticated human approval ledger.
- Manual Console/operator PASS remains user-reported evidence, distinct from repository-recorded automated/API proof.
- Cross-session learning entry point remains `docs/HARNESS_CHATGPT_HANDOFF.md`.

## Connector Safety Gate History

- Issue #30 completed the knowledge closeout.
- A root `CHATGPT.md` safety-gate sync was previously blocked twice after the required exact re-read and was not bypassed.
- PR #33 corrected the handoff to state that accurately.
- Do not automatically retry that old blocked connector action in this governance milestone. Current connector actions follow the present safety gate on their own exact targets.

## Active Work

- Issue #34 — align bootstrap/warm-continuation routing and correct related-repository status.

## Current Boundary

- This governance issue authorizes repository documentation changes only.
- No AWS, Harness, Gateway/Policy, SecCop, IAM/OIDC, deployment, resource cleanup, or connector-safety bypass.
- For any future AWS work, re-verify current STS identity and Region; Git carries knowledge, not authentication.

## Next Action

Review Issue #34 / its PR. After that, follow the current user's named lab milestone rather than reopening completed experiments implicitly.

## Continuation

Use the named Issue/PR, latest relevant authorized delta, and current HEAD for warm continuation. Reload broader context only on a real bootstrap/recovery trigger.
