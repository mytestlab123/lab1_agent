import importlib.util
import json
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("invoke_gateway.py")
spec = importlib.util.spec_from_file_location("invoke_gateway", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_allow_response_matches():
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": "allow-issue15",
        "result": {
            "isError": False,
            "content": [{"type": "text", "text": "AgentCore Gateway Policy provider executed"}],
        },
    })
    assert module.response_matches_expectation(200, body, "allow")
    assert not module.response_matches_expectation(200, body, "deny")


def test_policy_deny_response_matches():
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": "deny-issue15",
        "error": {
            "code": -32002,
            "message": "Tool Execution Denied: Tool call not allowed due to policy enforcement",
        },
    })
    assert module.response_matches_expectation(200, body, "deny")
    assert not module.response_matches_expectation(200, body, "allow")


def test_iserror_false_is_not_a_deny():
    body = json.dumps({"jsonrpc": "2.0", "result": {"isError": False}})
    assert not module.response_matches_expectation(200, body, "deny")
