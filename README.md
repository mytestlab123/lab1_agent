# ChatGPT AWS Consumer Lab

A small public PERSONAL/LAB repository for hands-on AWS and AgentCore experiments driven by ChatGPT + GitHub + AWS Core, while reusable private AWS operating knowledge remains centralized in `mytestlab123/chatgpt-aws`.

## Current focus

The AWS consumer/OIDC/Terraform foundations are proven. The lab is now evaluating small AgentCore capabilities one at a time.

**Experiment 01 — AgentCore Runtime direct-code IAM proof: PASS.**

It proved the smallest Runtime path:

```text
Python HTTP app -> ZIP -> S3 -> AgentCore Runtime -> IAM/SigV4 invoke -> verify -> teardown
```

No Cognito, frontend, ECR, CodeBuild, VPC, or Bedrock model call was needed.

See `experiments/01-agentcore-runtime/` for code, source classification, reproducible scripts, and learnings.

## Start Here

1. Read `AGENTS.md`.
2. Read `CONTEXT.md` for current project truth and active work.
3. Read `docs/CHATGPT_AWS_BOOTSTRAP.md` for the cross-session AWS bootstrap.
4. Read `ENV.md` for runtime/tool/environment expectations.
5. Read `SPEC.md` before implementation, AWS mutation, deployment, or cleanup.
6. Read `CHATGPT.md` for ChatGPT-Codex-GitHub collaboration rules.

## Publication boundary

Treat repository content, Issue/PR text, Actions logs, and Git history as public.

Never commit credentials, tokens, private keys, session credentials, or private environment data. Use GitHub Variables for non-secret runtime configuration and Secrets only for genuine secrets. Prefer scoped GitHub OIDC over stored AWS access keys.

See `docs/PUBLICATION_BOUNDARY.md`.
