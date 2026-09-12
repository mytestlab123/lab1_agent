# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws` (read as reusable AWS knowledge source)
- Context: PERSONAL
- Environment: LAB

## Current Truth

- This repository is public and unarchived.
- Cross-session AWS Core/GitHub knowledge reuse is proven.
- Public-safe GitHub OIDC -> Terraform -> AWS deploy/drift/reconciliation is proven.
- Pull-request Terraform validation is AWS-free and uses a committed provider lockfile.
- Reusable environment-specific AWS knowledge remains in private `mytestlab123/chatgpt-aws`.
- Experiment 01 proved AgentCore Runtime direct-code Python deployment with IAM/SigV4 invocation and was merged in PR #14.
- Experiment 01 cloud resources were fully torn down; no AgentCore Runtime from that experiment is retained.
- Experiment 02 targets AgentCore Gateway + Policy with one read-only Lambda tool and measurable ALLOW/DENY provider execution.
- Gateway, GatewayTarget, PolicyEngine, and Lambda resource types are available in the intended LAB region.
- The pre-existing Terraform/OIDC state bucket, deployment role, and SSM drift-proof parameter remain unchanged and out of scope.

## Active Work

- Issue: #15 — AgentCore Gateway + Policy ALLOW/DENY proof.
- Branch: `issue-15-agentcore-gateway-policy`.
- Critical acceptance: DENY must result in zero provider execution.

## Next Action

- Implement the deterministic Lambda/Gateway/Policy experiment.
- Run ALLOW and DENY tests with provider execution-count evidence.
- Independently verify and clean up all Issue #15 resources.
- Review/merge one cohesive Issue #15 PR if the experiment passes.
