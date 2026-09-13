# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws`
- Context: PERSONAL
- Environment: LAB

## Current Truth

- Repository is public; MkDocs Material GitHub Pages is live.
- Public-safe GitHub OIDC -> Terraform -> AWS drift/reconciliation is proven.
- Experiment 01: AgentCore Runtime direct-code + IAM/SigV4 — PASS.
- Experiment 02: Gateway + Policy ALLOW/DENY — PASS.
- Experiment 03: typed Harness human approval pause/resume — PASS.
- Experiment 04: integrated approval + Gateway + Policy matrix — PASS.
- Experiment 05: IAM identity-aware Policy — PASS.
- Experiment 06: native audit correlation across identity -> Gateway -> Policy -> provider — PASS.
- Experiment 07: full auditable chain from typed human approval through authenticated caller, Policy ENFORCE and provider evidence — PASS.

## Experiment 07 Result

| Human | Policy | Provider |
|---|---|---:|
| REJECT | not reached | 0 |
| APPROVE | DENY by default | 0 |
| APPROVE | ALLOW | exactly 1 |

- All three Harness cases emitted a real typed `request_approval` pause and same-session resume.
- `issue25-human-reject` has no downstream Gateway event and no provider marker.
- GitHub Actions run `34748226633` proved the approved DENY and ALLOW Gateway cases using the existing narrow Issue #21 OIDC identities.
- Native Gateway logs record caller identity, Policy result, trace IDs and tool-processing state.
- Approval does not override Cedar; Policy remains the final deterministic execution boundary.

## Retained Low-Cost Lab Resources

- AgentCore Gateway + Lambda target + harmless provider.
- Policy Engine and exact caller-A permit.
- Narrow GitHub OIDC caller roles.
- Gateway application logs/traces + Transaction Search.
- Experiment 07 Harness `lab1i25approval`, stateless with explicit execution limits.

Retain idle/usage-priced resources when expected cost remains comfortably below about USD 2/month per item and roughly USD 5/month for the retained lab footprint. Continuously billed workloads require an explicit retain/delete decision.

## Documentation

- GitHub Pages: `https://mytestlab123.github.io/lab1_agent/`
- Experiments 01-07 are verified learning milestones.

## Active Work

- Issue #25: final PR closeout for Experiment 07.
- Branch: `issue-25-auditable-approval`.

## Next Action

1. Merge Experiment 07 evidence/docs and close Issue #25.
2. Compare the proven AgentCore governance pattern with SecCop.
3. Select one practical adoption milestone rather than adding more AgentCore features by default.
