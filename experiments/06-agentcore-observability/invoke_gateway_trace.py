#!/usr/bin/env python3
"""Invoke one AgentCore Gateway MCP tool with explicit trace and request correlation IDs."""

import argparse
import json
import secrets
import time
import urllib.error
import urllib.request

import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


def xray_trace_header():
    epoch_hex = f"{int(time.time()):08x}"
    unique_hex = secrets.token_hex(12)
    parent_hex = secrets.token_hex(8)
    root = f"1-{epoch_hex}-{unique_hex}"
    return root, f"Root={root};Parent={parent_hex};Sampled=1"


def build_body(tool_name, request_id):
    return json.dumps({
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": {"request_id": request_id},
        },
    }).encode("utf-8")


def response_matches_expectation(status, text, expected):
    body_lower = text.lower()
    if expected == "allow":
        return status == 200 and "agentcore gateway policy provider executed" in body_lower and '"error"' not in body_lower

    if status in {401, 403}:
        return True

    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return "tool execution denied" in body_lower or "not authorized" in body_lower

    error = payload.get("error") if isinstance(payload, dict) else None
    if not isinstance(error, dict):
        return False

    message = str(error.get("message", "")).lower()
    return error.get("code") == -32002 and "denied" in message


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gateway-url", required=True)
    parser.add_argument("--tool-name", required=True)
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--region", required=True)
    parser.add_argument("--expect", choices=["allow", "deny"], required=True)
    args = parser.parse_args()

    url = args.gateway_url.rstrip("/")
    if not url.endswith("/mcp"):
        url += "/mcp"

    trace_root, trace_header = xray_trace_header()
    body = build_body(args.tool_name, args.request_id)
    headers = {
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
        "MCP-Protocol-Version": "2025-03-26",
        "X-Amzn-Trace-Id": trace_header,
    }

    credentials = boto3.Session().get_credentials().get_frozen_credentials()
    request = AWSRequest(method="POST", url=url, data=body, headers=headers)
    SigV4Auth(credentials, "bedrock-agentcore", args.region).add_auth(request)
    signed_headers = dict(request.headers.items())

    req = urllib.request.Request(url, data=body, headers=signed_headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            status = response.status
            text = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        status = exc.code
        text = exc.read().decode("utf-8", errors="replace")

    result = {
        "request_id": args.request_id,
        "xray_trace_id": trace_root,
        "http_status": status,
        "body": text,
    }
    print(json.dumps(result, indent=2))

    if not response_matches_expectation(status, text, args.expect):
        raise SystemExit(f"{args.expect.upper()} expectation failed")


if __name__ == "__main__":
    main()
