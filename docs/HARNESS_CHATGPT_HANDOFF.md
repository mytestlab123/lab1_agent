# AgentCore Harness cross-session handoff

Use this page when a new ChatGPT/Codex session needs to continue the `mytestlab123/lab1_agent` learning lab without reconstructing the story from chat history.

## Read order

1. `AGENTS.md`
2. `CONTEXT.md`
3. `CHATGPT.md`
4. `docs/HARNESS_CHATGPT_HANDOFF.md` — this page
5. `docs/harness-examples.md` — copy/paste prompts and Console/CLI usage
6. `docs/harness-examples-results.md` — compact test status
7. `experiments/08-operator-harness-examples/RESULTS.md` and `SOURCE.md` — detailed evidence and source ledger
8. `SPEC.md` before any mutation/deployment/change

For fresh AWS work, also read `docs/CHATGPT_AWS_BOOTSTRAP.md` and re-verify STS identity. Git stores knowledge, not authentication.

## Current operator-learning result

Issue #28 / PR #29 delivered three retained AgentCore Harness examples in `ap-southeast-1`:

| Harness | Purpose | Boundary |
| --- | --- | --- |
| `lab1_demo_explainer` | Explain pasted security findings | No live AWS tools; output must say NOT LIVE VERIFIED |
| `lab1_demo_reader` | Read one exact lab SSM setting | Harness -> Gateway -> Policy ENFORCE -> Lambda -> exact `ssm:GetParameter`; no writes/resource selector |
| `lab1_demo_approval` | Practice typed approval pause/resume | `DEMO_ONLY`; no remediation capability or durable human-identity/approval ledger |

All three were deployed as READY with Nova 2 Lite, disabled managed Memory, explicit allowed tools, bounded iterations/tokens/timeouts and no continuously running host.

## Test status

Automated/service evidence already recorded in Git:

- AWS Core direct invocation: PASS for explainer, reader and approval interrupt.
- GitHub OIDC live run `34768782767`: PASS.
- Final-head branch run `34769104231`: PASS.
- AWS CLI `GetHarness`: READY for all three.
- Native AgentCore CLI: explainer PASS, reader PASS, approval typed `tool_use` interrupt PASS.
- SDK terminal helper: APPROVED and REJECTED same-session resume PASS.
- 12 offline fail-closed parser tests: PASS.
- Forbidden write/shell prompts to explainer/reader: zero tool executions.
- Reader value/version matched independent SSM read; parameter remained unchanged.
- MkDocs strict build and GitHub Pages deployment: PASS.

On 2026-09-14 SGT, Amit reported the remaining manual operator/Console tests also passed. Treat that as **user-reported manual verification**, distinct from connector/API evidence. Do not rewrite it as an independently browser-verified ChatGPT result.

## Fast learning path

Start with `lab1_demo_reader` because it demonstrates a real AWS read without a custom product GUI/backend.

Then try:

1. `lab1_demo_explainer` — learn the difference between model explanation and live evidence.
2. `lab1_demo_reader` — learn managed Harness tool use through Gateway/Policy/provider.
3. `lab1_demo_approval` — learn client-side inline-function pause/resume without granting remediation.

Public guide: `https://mytestlab123.github.io/lab1_agent/harness-examples/`

## Retained resources and scope

The stack `lab1-operator-harness-examples` owns the three Harnesses plus the dedicated reader Gateway/Policy/Lambda, execution roles, exact-branch OIDC test role and short-retention Lambda logs. The existing lab SSM parameter is external and read-only.

Do not modify SecCop or infer production authority from this lab. No EC2/NAT/database/always-running host was added. Retain useful usage-priced lab resources unless a later approved cleanup/deployment decision changes that rule.

## Connector Safety Gate

This repository follows the reusable GitHub connector safety-gate policy.

Canonical source:

`amitkarpe/work/docs/chatgpt/CHATGPT_COLLABORATION_PROTOCOL.md`

Template source:

`amitkarpe/repo-starter/CHATGPT.md`

Section name in both:

`## Connector Safety Gate`

Operational rule: treat a connector/platform safety block as a distinct failure class. Re-read the exact repo/branch/PR/target/SHA, keep scope and safeguards unchanged, retry the identical bounded action at most once, then stop connector retries and report `BLOCKED_CONNECTOR_SAFETY` if blocked again. Do not widen permissions, weaken safeguards, change repo/branch, create a bypass handoff, or switch model/thinking effort merely to get past the gate.

The root `CHATGPT.md` in this repository does **not** yet contain that local section: the exact connector mutation was blocked twice and was intentionally not bypassed. Until a later authorized local/Codex sync is completed, use the canonical and template sources above as the authoritative safety-gate text.

## What a new chat should do

For read/learning requests: read the files above and summarize current state; no AWS action is needed.

For testing: reuse the existing Harnesses and documented prompts before creating anything new.

For implementation/mutation: verify repository binding, active Issue/SPEC authority, STS identity/account/Region, and current GitHub state first. Prefer one cohesive PR and preserve the explicit safety/retention boundaries.