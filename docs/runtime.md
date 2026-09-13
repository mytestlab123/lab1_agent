# Runtime Notes

The first managed-runtime lab verified a small Python deployment, authenticated invocation, health checks, independent provider verification, and full cleanup.

## Lessons

- Start with the smallest deployable application.
- Standard archive tooling was more reliable than hand-built archives.
- Use short-lived AWS authentication rather than stored access keys.
- Verify provider state and logs independently from deployment output.
- Remove temporary cloud resources after a learning experiment.

The complete implementation record is available under `experiments/01-agentcore-runtime/`.
