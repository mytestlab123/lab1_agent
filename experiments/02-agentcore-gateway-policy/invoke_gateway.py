#!/usr/bin/env python3
"""Invoke one AgentCore Gateway MCP tool using AWS SigV4 credentials."""

import argparse
import json
import urllib.error
import urllib.request

import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


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

    body = build_body(args.tool_name, args.request_id)
    headers = {
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
        "MCP-Protocol-Version": "2025-03-26",
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

    print(json.dumps({"http_status": status, "body": text}, indent=2))

    body_lower = text.lower()
    if args.expect == "allow":
        if status != 200 or "agentcore gateway policy provider executed" not in body_lower:
            raise SystemExit("ALLOW expectation failed")
    else:
        denied = status in {401, 403} or "denied" in body_lower or "not authorized" in body_lower or "iserror" in body_lower
        if not denied:
            raise SystemExit("DENY expectation failed")


if __name__ == "__main__":
    main()
