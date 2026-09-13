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
- PR #26 merged and Issue #25 closed. Issue #27's proposed audit-correlation adoption is not the current priority; Amit chose direct operator Harness examples instead.
- Issue #28 / PR #29 implements three operator examples without LibreChat or a product GUI/backend.
- lab1_demo_explainer, lab1_demo_reader and lab1_demo_approval are deployed and READY.
- AWS Core and GitHub OIDC independently tested actual invocation paths. Run 34768782767 passed AWS CLI reads, SDK tests, native CLI tests and offline tests.
- The reader returned the actual existing lab setting, desired-v1 / version 4, unchanged before/after.
- Approval is DEMO_ONLY simulation, not a real remediation or authenticated human approval ledger.
- No authenticated Console browser is available. GUI steps are documented, not falsely marked tested.

## Retained Resources

Keep previous near-zero/usage-priced lab resources unchanged, including the Experiment 07 Harness, Gateway/Policy/provider, OIDC roles and observability.

New stack lab1-operator-harness-examples owns three bounded Harnesses, dedicated reader Gateway/Policy/Lambda, model/read execution roles, exact-branch OIDC test role and seven-day Lambda logs. Existing SSM parameter is external and read-only. No continuously billed host or managed Memory was added.

Retain useful idle/usage-priced resources within the standing approximate USD 2/item and USD 5 aggregate lab budget assumption. Actual usage is not capped by these numbers; reassess continuously billed workloads separately. Do not tear down merely for tidiness.

## Documentation and Next Action

- Learning site: https://mytestlab123.github.io/lab1_agent/
- Operator guide: docs/harness-examples.md
- Reproduction and honest results: experiments/08-operator-harness-examples/
- Finish PR #29 review/Pages verification. Next user action is trying the existing Harnesses in the Singapore Console Playground or terminal; no new deployment is required.
