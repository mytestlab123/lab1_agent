#!/usr/bin/env python3
"""Minimal deterministic HTTP app for Amazon Bedrock AgentCore Runtime.

This intentionally uses only the Python standard library so the first Runtime
proof tests AgentCore hosting and IAM invocation, not model or dependency setup.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

HOST = "0.0.0.0"
PORT = 8080


def response_for(payload):
    """Return the deterministic response body for an invocation payload."""
    prompt = None
    if isinstance(payload, dict):
        if isinstance(payload.get("input"), dict):
            prompt = payload["input"].get("prompt")
        if prompt is None:
            prompt = payload.get("prompt")

    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt must be a non-empty string")

    return {
        "response": f"AgentCore Runtime OK: {prompt.strip()}",
        "status": "success",
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "lab1-agentcore-runtime/1.0"

    def _json(self, status, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/ping":
            self._json(200, {"status": "Healthy"})
            return
        self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/invocations":
            self._json(404, {"error": "not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length) or b"{}")
            self._json(200, response_for(payload))
        except (ValueError, json.JSONDecodeError) as exc:
            self._json(400, {"error": str(exc)})

    def log_message(self, fmt, *args):
        print(f"http: {fmt % args}", flush=True)


def main():
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"AgentCore lab server listening on {HOST}:{PORT}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
