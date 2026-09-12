# Context

Status: ACTIVE

## Project Identity

- Project: ChatGPT AWS Consumer Lab
- Primary Repository: `mytestlab123/lab1_agent`
- Authorized Related Repository: `mytestlab123/chatgpt-aws` (read as reusable AWS knowledge source)
- Context: PERSONAL
- Environment: LAB

## Current Truth

- This repository is private and unarchived.
- This repository is the consumer under test; it must not depend on previous-chat memory.
- Reusable AWS Core/MCP + GitHub/OIDC knowledge lives in private `mytestlab123/chatgpt-aws`.
- Fresh-session AWS identity/tool access must be verified independently before any mutation.
- Current consumer proof uses read-only AWS calls only.
- Exact AWS account/principal/role/resource identifiers are intentionally not duplicated here.

## Active Work

- Issue: #3 — cross-session AWS MCP consumer proof
- Branch: `consumer-proof-public-safe`
- Current milestone: verify fresh-session knowledge reuse and produce public-safe evidence.

## Next Action

- Complete Issue #3 in one PR: fresh AWS Core verification, representative read-only AWS checks, GitHub access proof, public-safety boundary, and one next experiment recommendation.
