#!/usr/bin/env python3
"""Reproduce Experiment 01 with boto3.

Creates only experiment-owned resources:
- one hardened S3 artifact bucket/object;
- one AgentCore Runtime execution role;
- one direct-code AgentCore Runtime.

Run package.py first. Exact identifiers are stored only in local .runtime-state.json.
"""

from pathlib import Path
import json
import os
import time
import uuid

import boto3
from botocore.exceptions import ClientError

HERE = Path(__file__).resolve()
EXPERIMENT = HERE.parents[1]
REPO = EXPERIMENT.parents[1]
ZIP = REPO / ".build" / "agentcore-runtime" / "deployment_package.zip"
STATE = EXPERIMENT / ".runtime-state.json"

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
AGENT_NAME = "lab1_agent_runtime_proof"
ROLE_NAME = "lab1-agent-agentcore-runtime-proof"
POLICY_NAME = "AgentCoreRuntimeProof"
ARTIFACT_KEY = "runtime/deployment_package.zip"


def save(state):
    STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def main():
    if STATE.exists():
        raise SystemExit(f"Refusing to deploy while state exists: {STATE}")
    if not ZIP.exists():
        raise SystemExit(f"Missing {ZIP}; run scripts/package.py first")

    session = boto3.Session(region_name=REGION)
    sts = session.client("sts")
    s3 = session.client("s3")
    iam = session.client("iam")
    control = session.client("bedrock-agentcore-control")

    account = sts.get_caller_identity()["Account"]
    existing = control.list_agent_runtimes().get("agentRuntimes", [])
    if any(r.get("agentRuntimeName") == AGENT_NAME for r in existing):
        raise SystemExit(f"Runtime {AGENT_NAME} already exists; stop rather than guessing ownership")

    bucket = f"lab1-agent-agentcore-{uuid.uuid4().hex[:10]}"
    role_arn = f"arn:aws:iam::{account}:role/{ROLE_NAME}"
    state = {
        "region": REGION,
        "agent_name": AGENT_NAME,
        "bucket": bucket,
        "artifact_key": ARTIFACT_KEY,
        "role_name": ROLE_NAME,
        "policy_name": POLICY_NAME,
    }
    save(state)

    s3.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration={"LocationConstraint": REGION},
    )
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True,
        },
    )
    s3.put_bucket_encryption(
        Bucket=bucket,
        ServerSideEncryptionConfiguration={
            "Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]
        },
    )
    s3.upload_file(str(ZIP), bucket, ARTIFACT_KEY)

    trust = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "AssumeRolePolicy",
            "Effect": "Allow",
            "Principal": {"Service": "bedrock-agentcore.amazonaws.com"},
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {"aws:SourceAccount": account},
                "ArnLike": {"aws:SourceArn": f"arn:aws:bedrock-agentcore:{REGION}:{account}:*"},
            },
        }],
    }
    iam.create_role(
        RoleName=ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust),
        Description="Temporary AgentCore Runtime execution role for lab1_agent Experiment 01",
        Tags=[
            {"Key": "project", "Value": "lab1-agent"},
            {"Key": "purpose", "Value": "agentcore-runtime-proof"},
        ],
    )

    log_group = f"arn:aws:logs:{REGION}:{account}:log-group:/aws/bedrock-agentcore/runtimes/*"
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "RuntimeLogGroups",
                "Effect": "Allow",
                "Action": ["logs:DescribeLogStreams", "logs:CreateLogGroup"],
                "Resource": log_group,
            },
            {
                "Sid": "RuntimeLogPolicy",
                "Effect": "Allow",
                "Action": ["logs:PutResourcePolicy"],
                "Resource": f"arn:aws:logs:{REGION}:{account}:log-group:/aws/bedrock-agentcore/runtimes/{AGENT_NAME}-*",
            },
            {
                "Sid": "DescribeLogGroups",
                "Effect": "Allow",
                "Action": ["logs:DescribeLogGroups"],
                "Resource": f"arn:aws:logs:{REGION}:{account}:log-group:*",
            },
            {
                "Sid": "RuntimeLogStreams",
                "Effect": "Allow",
                "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
                "Resource": f"{log_group}:log-stream:*",
            },
            {
                "Sid": "RuntimeTelemetry",
                "Effect": "Allow",
                "Action": [
                    "xray:PutTraceSegments",
                    "xray:PutTelemetryRecords",
                    "xray:GetSamplingRules",
                    "xray:GetSamplingTargets",
                ],
                "Resource": "*",
            },
            {
                "Sid": "RuntimeMetrics",
                "Effect": "Allow",
                "Action": ["cloudwatch:PutMetricData"],
                "Resource": "*",
                "Condition": {"StringEquals": {"cloudwatch:namespace": "bedrock-agentcore"}},
            },
            {
                "Sid": "ArtifactBucket",
                "Effect": "Allow",
                "Action": ["s3:GetBucketLocation"],
                "Resource": f"arn:aws:s3:::{bucket}",
            },
            {
                "Sid": "ArtifactRead",
                "Effect": "Allow",
                "Action": ["s3:GetObject"],
                "Resource": f"arn:aws:s3:::{bucket}/{ARTIFACT_KEY}",
            },
        ],
    }
    iam.put_role_policy(
        RoleName=ROLE_NAME,
        PolicyName=POLICY_NAME,
        PolicyDocument=json.dumps(policy),
    )

    # New role propagation is normally quick but not instantaneous.
    time.sleep(8)

    created = control.create_agent_runtime(
        agentRuntimeName=AGENT_NAME,
        description="lab1_agent Experiment 01 deterministic direct-code Runtime proof",
        agentRuntimeArtifact={
            "codeConfiguration": {
                "code": {"s3": {"bucket": bucket, "prefix": ARTIFACT_KEY}},
                "runtime": "PYTHON_3_13",
                "entryPoint": ["main.py"],
            }
        },
        networkConfiguration={"networkMode": "PUBLIC"},
        roleArn=role_arn,
        protocolConfiguration={"serverProtocol": "HTTP"},
        lifecycleConfiguration={"idleRuntimeSessionTimeout": 300, "maxLifetime": 900},
        tags={"project": "lab1-agent", "purpose": "agentcore-runtime-proof"},
    )
    state["runtime_id"] = created["agentRuntimeId"]
    state["runtime_arn"] = created["agentRuntimeArn"]
    save(state)

    for _ in range(30):
        runtime = control.get_agent_runtime(agentRuntimeId=state["runtime_id"])
        status = runtime["status"]
        print(f"Runtime status: {status}")
        if status == "READY":
            print("READY")
            return
        if status.endswith("FAILED") or status == "FAILED":
            raise SystemExit(runtime.get("failureReason", status))
        time.sleep(5)

    raise SystemExit("Timed out waiting for Runtime READY; inspect state and run teardown.py")


if __name__ == "__main__":
    main()
