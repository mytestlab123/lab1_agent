# Learnings — Experiment 02

Status: **PASS**

## What was proved

AgentCore Gateway + Policy enforced a deterministic decision before the Lambda provider boundary.

```text
ALLOW -> provider execution count +1
DENY  -> provider execution count +0
```

The DENY response was returned by Gateway/Policy as JSON-RPC error `-32002`, while independent CloudWatch log evidence showed no provider marker for the denied request.

## Key lessons

### 1. Policy is a real enforcement boundary

This was not a UI-only approval simulation. The Gateway rejected the tool call before the Lambda target ran.

For a security automation agent, this is materially different from asking the LLM to follow a prompt such as "do not run dangerous tools".

### 2. Cedar is default-deny and `forbid` overrides `permit`

A baseline permit allowed the exact IAM principal/tool/Gateway combination. Adding an exact forbid caused the same signed call to be denied.

### 3. The Cedar analyzer catches dangerous policy shapes

Strict validation rejected the intentionally absolute forbid as **Overly Restrictive**. This is useful production feedback. The experiment used `IGNORE_ALL_FINDINGS` only because total denial of that exact test combination was the desired negative case.

### 4. IAM-authenticated principals have a stable Cedar role identity

For a Gateway using `AWS_IAM`, AgentCore Policy represents an assumed role as `AgentCore::IamEntity` using the STS assumed-role ARN without the session-name suffix. That makes exact role matching practical.

### 5. Gateway + Policy requires more than Lambda invoke permission

A custom Gateway execution role needed the Policy runtime permissions in addition to `lambda:InvokeFunction`:

- `GetPolicyEngine`
- `AuthorizeAction`
- `PartiallyAuthorizeActions`

The service surfaced each missing permission during creation-time checks.

### 6. Gateway creation has a bootstrap/tighten IAM pattern

Before the Gateway exists, its final ARN is not known. The narrow creation-time policy therefore used the known Gateway-name ARN pattern. Immediately after creation the policy and trust were tightened to the exact Gateway ARN.

### 7. GitHub OIDC is a useful test caller

A branch-scoped temporary GitHub Actions role provided a clean, reproducible AWS_IAM caller for the Gateway without static access keys. The role was deleted after proof.

## Architecture decision

**KEEP:**

- AgentCore Gateway as the managed MCP tool boundary;
- AWS_IAM/SigV4 for AWS-internal testing;
- AgentCore Policy ENFORCE mode;
- provider-side execution markers for negative-control testing;
- strict Cedar validation for normal policies.

**DEFER:**

- Cognito/JWT;
- browser UI;
- multi-tool catalogs;
- natural-language policy generation;
- persistent production policy deployment.

## Why this matters for SecCop-style agents

The desired security flow can now be grounded in a real enforcement point:

```text
Agent proposes action
      |
      v
Approval/orchestration layer
      |
      v
AgentCore Gateway
      |
      v
AgentCore Policy
  ALLOW / DENY
      |
      v
Provider tool
```

A future `APPROVAL_REQUIRED` state should not weaken the Policy boundary. Human approval should decide whether the request is allowed to proceed to the Gateway; Policy should still make the final deterministic authorization decision at execution time.

## Next experiment

Build the smallest approval harness that can visibly demonstrate:

```text
ALLOW
DENY
APPROVAL_REQUIRED -> approve -> execute
                  -> reject  -> zero provider executions
```
