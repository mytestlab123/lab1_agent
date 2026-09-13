# Operator Harness Examples

Service/terminal tests: **PASS**. Authenticated Console GUI: **NOT_TESTED**.

Start with the [published prompt and Console/CLI guide](https://mytestlab123.github.io/lab1_agent/harness-examples/).

| Example | Harness | Purpose |
| --- | --- | --- |
| explainer | lab1_demo_explainer | Pasted-finding explanation, no effective tools |
| reader | lab1_demo_reader | One exact provider-backed SSM read through Gateway + Policy |
| approval | lab1_demo_approval | DEMO_ONLY typed pause/resume; no remediation capability |

`examples.py` discovers the three named resources in the current AWS account/region. It uses existing AWS credential providers, not embedded keys. Invoke `python examples.py approval` for an explicit terminal decision prompt; `--decision APPROVED|REJECTED` is an automated simulation fixture.

`test_examples.py` is offline and fails closed for malformed/extra tool calls, invalid scope/decision, missing IDs, incomplete/error streams and prose-only approval. `live_tests.py` makes low-volume real model/tool invocations and independent provider reads; run it only against this approved lab.

Desired infrastructure: `infra/operator-harness-examples.yaml`. Existing lab parameter is an external read-only input. Fresh STS plus AWS Core applied the versioned stack; a separate exact-branch GitHub OIDC role ran terminal tests.

See [results](RESULTS.md) and [source ledger](SOURCE.md). The complete reader path is Harness -> Gateway -> Policy -> Lambda -> SSM, without a product GUI/backend. The approval example is explicitly not real remediation, authenticated human identity, or replay-safe business authorization.
