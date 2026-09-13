# Roadmap

## Completed learning

- Cross-session AWS Core/GitHub knowledge reuse.
- GitHub OIDC/Terraform state, drift/reconciliation and AWS-free PR validation.
- Experiment 01: Runtime direct-code + IAM/SigV4.
- Experiment 02: Gateway/Policy ALLOW versus DENY with provider evidence.
- Experiment 03: Harness typed client-tool approval pause/resume.
- Experiment 04: controlled approval/Gateway/Policy/provider matrix.
- Experiment 05: caller-identity-specific authorization.
- Experiment 06: native request/Policy/provider observability correlation.
- Experiment 07: correlated approval practice and downstream evidence, PR #26 merged.
- Operator examples (Issue #28 / PR #29): three actual Harnesses, AWS CLI/SDK/native CLI tests, 12 offline tests and unchanged provider state. Console clicks are not claimed tested.

## Current priority

Let Amit use the three retained examples directly: pasted finding explanation, exact live AWS read, and DEMO_ONLY approval practice. Publish prompts, terminal instructions, Console route and honest test results.

The proposed Issue #27 SecCop audit-correlation adoption is not being implemented; Amit selected the operator experience instead. No cross-repository writes are authorized by this work.

## Next

Capture Amit's Console feedback, especially whether its current Playground exposes a structured inline tool-result control. Use the already-tested terminal helper for complete decision/resume. Only after that feedback choose one useful next capability; do not automatically add another service or deploy a product GUI.

## Retention

Keep useful near-zero/usage-priced resources; do not delete merely for tidiness. Standing budget assumptions remain approximately USD 2/item and USD 5 aggregate lab footprint, subject to actual usage. Active sessions/model inference/logs can cost money. No additional EC2/NAT/database/always-running host is part of the operator examples.
