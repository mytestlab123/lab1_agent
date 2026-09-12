# Environment

Status: READY

## Runtime

- Runtime: ChatGPT with connected GitHub and AWS Core apps
- Repository: `mytestlab123/lab1_agent`
- Environment: PERSONAL / LAB

## Cloud

- Provider: AWS
- Intended region: `ap-southeast-1`
- Exact account/principal/role/resource identifiers: intentionally not committed here
- Reusable environment-specific AWS knowledge source: private `mytestlab123/chatgpt-aws`

## External Dependencies

- GitHub connector/app
- AWS Core / managed AWS MCP integration

## Configuration Boundary

If future CI/CD needs environment-specific configuration, use names such as:

- `AWS_REGION` — repository/environment Variable; non-secret
- `AWS_ACCOUNT_ID` — Variable if disclosure is acceptable, otherwise Secret if Amit intentionally wants it hidden
- `AWS_OIDC_ROLE_ARN` — Variable if disclosure is acceptable, otherwise Secret if intentionally hidden
- resource prefixes/names — Variables when they are environment-specific and non-secret

Do not store AWS access keys for the GitHub deployment path. Prefer GitHub OIDC with repository/environment-scoped IAM trust.

Secrets are not a substitute for authorization design: hiding a role ARN does not make an overly broad trust policy safe.

## Credentials And Secrets

Never commit credentials, tokens, private keys, OAuth state, or session credentials. GitHub Secrets should contain only values a workflow genuinely needs and should not be used as a general private documentation database.

## Publication

Before making this repository public, review committed history, Issues/PRs, workflow triggers, IAM OIDC trust, permissions, artifacts, logs, screenshots, and generated evidence. Moving a value to a Secret later does not erase an older committed copy from Git history.
