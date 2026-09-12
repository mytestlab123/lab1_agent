"""Read-only provider for AgentCore Gateway + Policy Experiment 02."""


def lambda_handler(event, context):
    request_id = event.get("request_id", "missing") if isinstance(event, dict) else "invalid"
    print(f"PROVIDER_EXECUTION request_id={request_id}", flush=True)
    return {
        "status": "ok",
        "request_id": request_id,
        "provider": "lambda",
        "message": "AgentCore Gateway Policy provider executed",
    }
