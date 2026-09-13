# Next Experiment

The next milestone adds a visible human decision before a controlled tool request is sent to the existing Gateway and Policy enforcement path.

Target states:

```text
ALLOW
DENY
APPROVAL_REQUIRED
```

For approval-required actions, rejection must result in zero provider execution. Approval allows the request to continue, but the final provider call must still pass the deterministic Gateway policy check.
