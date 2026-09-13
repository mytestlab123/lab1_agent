# AWS Workflow

This lab uses two complementary paths.

- AWS Core is used for discovery, bounded experiments, troubleshooting, cleanup and independent verification.
- GitHub Actions with OIDC and infrastructure as code is used for repeatable state that should be reviewed and retained.

The practical rule is simple: explore and verify with AWS Core; deploy durable state through reviewed GitHub automation.

See [Cross-Session AWS MCP Consumer Proof](CONSUMER_PROOF.md) for the original evidence.
