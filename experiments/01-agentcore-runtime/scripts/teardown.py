#!/usr/bin/env python3
"""Delete only resources recorded by Experiment 01 deploy.py."""

from pathlib import Path
import json
import time

import boto3
from botocore.exceptions import ClientError

HERE = Path(__file__).resolve()
EXPERIMENT = HERE.parents[1]
STATE = EXPERIMENT / ".runtime-state.json"


def main():
    if not STATE.exists():
        raise SystemExit(f"Missing state: {STATE}")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    session = boto3.Session(region_name=state["region"])
    data = session.client("bedrock-agentcore")
    control = session.client("bedrock-agentcore-control")
    s3 = session.client("s3")
    iam = session.client("iam")
    logs = session.client("logs")

    if state.get("last_session_id") and state.get("runtime_arn"):
        try:
            data.stop_runtime_session(
                agentRuntimeArn=state["runtime_arn"],
                runtimeSessionId=state["last_session_id"],
                qualifier="DEFAULT",
            )
        except ClientError as exc:
            print(f"Session stop skipped: {exc.response['Error']['Code']}")

    if state.get("runtime_id"):
        try:
            control.delete_agent_runtime(agentRuntimeId=state["runtime_id"])
        except ClientError as exc:
            if exc.response["Error"]["Code"] != "ResourceNotFoundException":
                raise

        for _ in range(30):
            try:
                control.get_agent_runtime(agentRuntimeId=state["runtime_id"])
                time.sleep(3)
            except ClientError as exc:
                if exc.response["Error"]["Code"] == "ResourceNotFoundException":
                    break
                raise

    # Runtime log groups are experiment-owned and can outlive Runtime deletion.
    prefix = f"/aws/bedrock-agentcore/runtimes/{state['agent_name']}-"
    for group in logs.describe_log_groups(logGroupNamePrefix=prefix).get("logGroups", []):
        logs.delete_log_group(logGroupName=group["logGroupName"])

    try:
        s3.delete_object(Bucket=state["bucket"], Key=state["artifact_key"])
        s3.delete_bucket(Bucket=state["bucket"])
    except ClientError as exc:
        if exc.response["Error"]["Code"] not in {"NoSuchBucket", "404"}:
            raise

    try:
        iam.delete_role_policy(RoleName=state["role_name"], PolicyName=state["policy_name"])
    except ClientError as exc:
        if exc.response["Error"]["Code"] != "NoSuchEntity":
            raise
    try:
        iam.delete_role(RoleName=state["role_name"])
    except ClientError as exc:
        if exc.response["Error"]["Code"] != "NoSuchEntity":
            raise

    STATE.unlink(missing_ok=True)
    print("Experiment 01 teardown complete")


if __name__ == "__main__":
    main()
