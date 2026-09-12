# Cross-Session AWS MCP Consumer Proof

Result: **PASS**
Date: 2026-09-12
Owning Issue: #3

## Verified

- GitHub can read private `mytestlab123/chatgpt-aws` in this session: PASS.
- GitHub can read/write `mytestlab123/lab1_agent`: PASS.
- `lab1_agent` repository state is private + unarchived: PASS.
- Fresh AWS Core STS identity check: PASS.
- Intended LAB region `ap-southeast-1`: PASS.
- Representative real AWS reads: EC2 PASS, S3 PASS, IAM/OIDC PASS.
- Existing GitHub OIDC proof role trust is repository-bound to the earlier `assignment-cicd` proof: PASS.
- AWS mutations performed by this consumer proof: **0**.

Exact account/principal/role/resource identifiers and live inventory are intentionally omitted from this repository. Detailed environment truth remains in private `mytestlab123/chatgpt-aws`.

## AWS Core surface discovered in this session

The current AWS Core integration exposes, at minimum:

- authenticated AWS API execution through a sandboxed script/call surface;
- AWS documentation search/read;
- AWS skill/workflow retrieval;
- AWS region and regional-availability discovery;
- S3 pre-signed URL support;
- polling for long-running AWS MCP tasks.

Tool names and schemas are session/client details and should be rediscovered rather than treated as permanent API contracts.

## Knowledge reuse

The saved `chatgpt-aws` documentation was sufficient to continue without asking Amit to repeat the previous setup.

It correctly provided the operating model and the facts that needed fresh verification:

1. **Direct AWS MCP path** — use for discovery, troubleshooting, live provider readback, verification, and bounded reversible operations when authorized.
2. **GitHub + IaC + OIDC path** — use for persistent infrastructure that should be reviewed, reproduced, rebuilt, or destroyed from code.
3. **Preferred durable loop** — `ChatGPT -> GitHub/IaC -> GitHub Actions/OIDC -> AWS -> AWS MCP independent verification`.
4. **OIDC scope rule** — never assume a role created for one repository can be assumed by another repository.
5. **Cross-session rule** — Git carries knowledge; authentication and current provider state must be re-established in each session.

One stale saved fact was found: older bootstrap material described `lab1_agent` as public. Current GitHub metadata is authoritative and shows it is private + unarchived. The current branch corrects that project-specific documentation.

## Next experiment — design only

Build one low-cost persistent IaC resource from this repository using a repository-scoped GitHub OIDC role, then independently verify it through AWS Core MCP.

Proposed cycle:

1. Terraform creates one low-cost persistent resource through GitHub Actions/OIDC.
2. AWS Core verifies the deployed provider state independently.
3. Introduce one harmless, reversible drift outside Terraform.
4. AWS Core detects the drift.
5. Terraform plan shows the drift.
6. Terraform reconciles desired state.
7. AWS Core independently verifies the reconciled state.

Do not execute this experiment under Issue #3.
