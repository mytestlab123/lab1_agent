# Learnings — Experiment 01

Status: IN PROGRESS

## Hypothesis

A minimal direct-code AgentCore Runtime using IAM/SigV4 can prove the hosting/invocation boundary without the full sample stack.

## Verified before deployment

- `AWS::BedrockAgentCore::Runtime` is available in the LAB region.
- Live AWS readback showed zero existing AgentCore Runtimes before this experiment.
- AgentCore supports direct-code Python ZIP deployment from S3.
- IAM/SigV4 is a supported inbound authentication mechanism.
- The HTTP contract requires `POST /invocations` and `GET /ping` on port 8080.

## Result

Pending live deployment/invocation/teardown evidence.

## Decision

- AgentCore Runtime: PENDING
- Direct-code deployment: PENDING
- IAM/SigV4 inbound auth: PENDING
