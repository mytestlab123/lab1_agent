#!/usr/bin/env python3
"""Minimal AgentCore Harness inline_function pause/resume reproduction.

This follows the AWS sample contract:
1. invoke until stopReason == tool_use;
2. reconstruct the inline toolUse block;
3. resume the SAME session with assistant toolUse + user toolResult;
4. run both REJECTED and APPROVED decisions.

No real provider mutation is performed. The only external action is the client-side
request_approval inline function result supplied by this script.
"""
from __future__ import annotations

import json
import os
import sys
import uuid

import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
HARNESS_ARN = os.environ["HARNESS_ARN"]

client = boto3.client("bedrock-agentcore", region_name=REGION)


def new_session() -> str:
    return f"hitl-{uuid.uuid4()}-{uuid.uuid4().hex[:8]}"


def consume(stream) -> dict:
    text: list[str] = []
    stop_reason = None
    current: dict | None = None
    pending: list[dict] = []

    for event in stream:
        if "contentBlockStart" in event:
            start = event["contentBlockStart"].get("start", {})
            if "toolUse" in start:
                tu = start["toolUse"]
                current = {
                    "toolUseId": tu.get("toolUseId"),
                    "name": tu.get("name"),
                    "input_text": "",
                }

        if "contentBlockDelta" in event:
            delta = event["contentBlockDelta"].get("delta", {})
            if "text" in delta:
                text.append(delta["text"])
            if current and "toolUse" in delta:
                current["input_text"] += delta["toolUse"].get("input", "")

        if "contentBlockStop" in event and current:
            raw = current.pop("input_text", "")
            try:
                current["input"] = json.loads(raw or "{}")
            except json.JSONDecodeError:
                current["input"] = {"_unparsed": raw}
            pending.append(current)
            current = None

        if "messageStop" in event:
            stop_reason = event["messageStop"].get("stopReason")

    return {
        "text": "".join(text),
        "stop_reason": stop_reason,
        "tool_uses": pending,
    }


def first_turn(session_id: str) -> dict:
    response = client.invoke_harness(
        harnessArn=HARNESS_ARN,
        runtimeSessionId=session_id,
        messages=[{
            "role": "user",
            "content": [{
                "text": (
                    "Simulation only: a harmless controlled action named DEMO_CHANGE is proposed. "
                    "Do not inspect files, do not use shell, and do not perform any real action. "
                    "Use the required human approval tool before giving the final recommendation."
                )
            }],
        }],
    )
    return consume(response["stream"])


def resume(session_id: str, tool_uses: list[dict], decision: str) -> dict:
    assistant_blocks = []
    result_blocks = []

    for tool in tool_uses:
        assistant_blocks.append({
            "toolUse": {
                "toolUseId": tool["toolUseId"],
                "name": tool["name"],
                "input": tool.get("input", {}),
            }
        })
        if tool["name"] == "request_approval":
            payload = {
                "decision": decision,
                "approver": "lab-reviewer",
                "note": f"Issue 17 {decision.lower()} path proof",
            }
            status = "success"
        else:
            payload = {
                "result": "NOT_EXECUTED",
                "reason": "Only the client-side approval gate is in scope for this proof.",
            }
            status = "error"
        result_blocks.append({
            "toolResult": {
                "toolUseId": tool["toolUseId"],
                "content": [{"text": json.dumps(payload)}],
                "status": status,
            }
        })

    response = client.invoke_harness(
        harnessArn=HARNESS_ARN,
        runtimeSessionId=session_id,
        messages=[
            {"role": "assistant", "content": assistant_blocks},
            {"role": "user", "content": result_blocks},
        ],
    )
    return consume(response["stream"])


def run_case(decision: str) -> dict:
    session_id = new_session()
    turn1 = first_turn(session_id)
    approval_tools = [t for t in turn1["tool_uses"] if t.get("name") == "request_approval"]
    paused = turn1["stop_reason"] == "tool_use" and bool(approval_tools)

    result = {
        "decision": decision,
        "session_id": session_id,
        "turn1": {
            "stop_reason": turn1["stop_reason"],
            "tool_names": [t.get("name") for t in turn1["tool_uses"]],
            "approval_tool_count": len(approval_tools),
            "text_preview": turn1["text"][:240],
        },
        "paused_on_real_approval_tool": paused,
    }

    if not paused:
        result["passed"] = False
        return result

    turn2 = resume(session_id, turn1["tool_uses"], decision)
    result["turn2"] = {
        "stop_reason": turn2["stop_reason"],
        "tool_names": [t.get("name") for t in turn2["tool_uses"]],
        "text_preview": turn2["text"][:400],
    }
    result["resumed"] = turn2["stop_reason"] in {
        "end_turn",
        "max_tokens",
        "max_iterations_exceeded",
        "max_output_tokens_exceeded",
    }
    result["passed"] = paused and result["resumed"]
    return result


def main() -> int:
    evidence = {
        "experiment": "issue-17-agentcore-harness-hitl-repro",
        "region": REGION,
        "reject": run_case("REJECTED"),
        "approve": run_case("APPROVED"),
    }
    evidence["passed"] = evidence["reject"]["passed"] and evidence["approve"]["passed"]

    with open("hitl-result.json", "w", encoding="utf-8") as fh:
        json.dump(evidence, fh, indent=2)
    print(json.dumps(evidence, indent=2))
    return 0 if evidence["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
