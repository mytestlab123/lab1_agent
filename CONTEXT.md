# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: mytestlab123/lab1_agent (public)
- Related private knowledge source: mytestlab123/chatgpt-aws
- Context: PERSONAL / LAB / ap-southeast-1
- SecCop source: amitkarpe/aws-secops; READ-ONLY for this work

## Current Truth

- GitHub OIDC -> Terraform -> AWS drift/reconciliation remains proven.
- Experiments 01-07 record Runtime, Gateway/Policy, typed approval, identity and observability learning. Their evidence and limitations remain in the corresponding experiment folders/docs.
- Issue #28 / PR #29 delivered three operator Harness examples without LibreChat or a product GUI/backend; PR #29 is merged.
- `lab1_demo_explainer`, `lab1_demo_reader` and `lab1_demo_approval` are deployed and READY.
- AWS Core and GitHub OIDC independently tested actual invocation paths. Run `34768782767` passed AWS CLI reads, SDK tests, native CLI tests and offline tests; final-head run `34769104231` also passed live/strict-doc validation.
- The reader returned the actual existing lab setting, `desired-v1` / version 4, unchanged before/after.
- Approval is DEMO_ONLY simulation, not a real remediation or authenticated human approval ledger.
- The automated test environment did not have an authenticated Console browser. On 2026-09-14 SGT Amit subsequently reported that the remaining manual Console/operator tests passed. Preserve this provenance as user-reported manual PASS, distinct from repository-recorded automated/API evidence.
- Cross-session learning entry point: `docs/HARNESS_CHATGPT_HANDOFF.md`.

## Connector Safety Gate

- Canonical: `amitkarpe/work/docs/chatgpt/CHATGPT_COLLABORATION_PROTOCOL.md`
- Template: `amitkarpe/repo-starter/CHATGPT.md`
- Section in both: `## Connector Safety Gate`
- A connector/platform safety block is a distinct failure class; re-read exact target/SHA, retry the identical bounded action at most once, then stop retries and report `BLOCKED_CONNECTOR_SAFETY` without widening permissions/scope or using model/thinking mode as a bypass.
- Issue #30 is the owning docs handoff. The GitHub connector blocked the attempted local `CHATGPT.md` sync twice after the required exact re-read; do not retry that connector action. Complete that one local/template sync through the existing Issue #30 Codex/local handoff if desired.

## Retained Resources

Keep previous near-zero/usage-priced lab resources unchanged, including the Experiment 07 Harness, Gateway/Policy/provider, OIDC roles and observability.

Stack `lab1-operator-harness-examples` owns three bounded Harnesses, dedicated reader Gateway/Policy/Lambda, model/read execution roles, exact-branch OIDC test role and seven-day Lambda logs. Existing SSM parameter is external and read-only. No continuously billed host or managed Memory was added.

Retain useful idle/usage-priced resources within the standing approximate USD 2/item and USD 5 aggregate lab budget assumption. Actual usage is not capped by these numbers; reassess continuously billed workloads separately. Do not tear down merely for tidiness.

## Documentation and Next Action

- Learning site: https://mytestlab123.github.io/lab1_agent/
- Cross-session handoff: `docs/HARNESS_CHATGPT_HANDOFF.md`
- Operator guide: `docs/harness-examples.md`
- Compact results: `docs/harness-examples-results.md`
- Reproduction and detailed evidence: `experiments/08-operator-harness-examples/`
- Issue #30 owns the knowledge closeout and connector-safety-gate sync. No AWS or SecCop mutation is required.
