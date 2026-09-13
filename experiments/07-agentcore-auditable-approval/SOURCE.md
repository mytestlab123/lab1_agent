# Sources — Experiment 07

Primary AWS references used:

- AgentCore Harness managed loop and deployment workflow  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Harness tools and client-side `inline_function` contract  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html
- Harness security and IAM requirements  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html
- CreateHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateHarness.html
- InvokeHarness API  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html
- AgentCore Gateway observability data  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-gateway-metrics.html
- AgentCore Policy observability data  
  https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-policy-metrics.html

## Reused local proofs

Experiment 07 reuses already-proven repository components:

- Experiment 03: typed Harness pause/resume contract.
- Experiment 05: caller-A exact permit vs caller-B default deny.
- Experiment 06: native Gateway request/trace/Policy/provider correlation.
- `experiments/02-agentcore-gateway-policy/invoke_gateway.py`: signed Gateway client.

## Live proof references

- Harness approval cases ran through AWS Core against retained `lab1i25approval`, using per-invocation Nova 2 Lite and `request_approval` overrides.
- GitHub Actions run `34748226633` executed the approved DENY and approved ALLOW Gateway cases under the retained Issue #21 OIDC caller identities.
- Native Gateway logs and provider logs were then read independently through AWS Core.

## Lab-derived conclusion

A real human approval boundary and deterministic Policy boundary are complementary, not interchangeable:

```text
APPROVED -> Policy may still DENY
REJECTED -> controller must stop before Policy/provider
```

This is the governance property carried forward to the SecCop comparison milestone.
