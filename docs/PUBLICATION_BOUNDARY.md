# Publication Boundary

Goal: keep this repository easy to make public later without weakening AWS security.

## What belongs where

| Data | Preferred home | Why |
|---|---|---|
| AWS access keys, tokens, private keys, session credentials | Never commit; avoid creating for CI when OIDC is available | Real secrets |
| Workflow secrets genuinely required at runtime | GitHub Secrets / environment Secrets | Encrypted and not committed |
| AWS region | GitHub Variable or public config | Not secret |
| Account ID | GitHub Variable if disclosure is acceptable; Secret only if Amit intentionally wants it hidden | Identifier, not credential |
| OIDC role ARN | GitHub Variable if disclosure is acceptable; Secret only if intentionally hidden | Identifier, not credential |
| Resource prefixes/names | GitHub Variables if environment-specific | Configuration, usually not secret |
| Reusable architecture/operating rules | Git | Should be reviewable/versioned |
| Detailed private environment knowledge not needed by workflows | Private `mytestlab123/chatgpt-aws` | Better than abusing Secrets as documentation storage |

## What Secrets cannot solve

GitHub Secrets hide values from repository files, but they do **not**:

- erase values already committed in Git history;
- remove values already posted in Issues/PRs, workflow logs, artifacts, screenshots, or comments;
- make a broad IAM policy or weak OIDC trust policy safe;
- provide human-readable cross-session documentation to ChatGPT through the GitHub connector;
- prevent an authorized workflow from using the secret.

Therefore the correct design is **public-safe Git + scoped OIDC + minimal Variables/Secrets**, not "put every string in Secrets".

## OIDC rule

Prefer:

`GitHub Actions -> OIDC -> repository/environment-scoped IAM role -> AWS`

Do not store long-lived AWS access keys merely to make the repository public.

The existing proof role belongs to another repository and must not be reused unless its trust policy is explicitly redesigned. The preferred next experiment is a new/scoped role for this repository or an intentionally reviewed trust-policy change.

## Before switching repository visibility to public

Review all of the following, not only current files:

1. Git history.
2. Open and closed Issues/PRs/comments.
3. GitHub Actions workflow YAML and triggers.
4. Workflow logs and artifacts.
5. Screenshots/evidence files.
6. Terraform state or generated outputs if ever committed accidentally.
7. IAM OIDC trust conditions and permission scope.
8. Repository/environment Variables and Secrets required by workflows.

Publication is safe only when both **repository content** and **AWS trust design** are safe for an untrusted public fork/PR environment.
