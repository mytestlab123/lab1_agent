#!/usr/bin/env python3
"""Invoke the Runtime created by deploy.py using IAM/SigV4."""

from pathlib import Path
import json
import uuid

import boto3

HERE = Path(__file__).resolve()
EXPERIMENT = HERE.parents[1]
STATE = EXPERIMENT / ".runtime-state.json"


def main():
    if not STATE.exists():
        raise SystemExit(f"Missing state: {STATE}")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    session = boto3.Session(region_name=state["region"])
    client = session.client("bedrock-agentcore")
    runtime_session_id = f"lab1agentcore{uuid.uuid4().hex}"

    response = client.invoke_agent_runtime(
        agentRuntimeArn=state["runtime_arn"],
        runtimeSessionId=runtime_session_id,
        payload=json.dumps({"prompt": "hello from experiment 01"}).encode("utf-8"),
        qualifier="DEFAULT",
    )
    raw = response["response"].read()
    print(raw.decode("utf-8"))

    state["last_session_id"] = runtime_session_id
    STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
