# Workflow evaluation scorecard

Copy this form into the existing evaluation record, outside the agent workspace.
Do not put example or guessed measurements into result fields. Use `not measured`
for unavailable telemetry; a missing measurement is not zero.

## Run identity and evidence

- Scenario, fixture digest, and repetition:
- Arm: baseline / Flightline; package version and source digest:
- Model/version, reasoning settings, other skills, tools, and permissions:
- Runtime/OS, resource limits, start/end time, and run order:
- Starting snapshot including scenario setup and dirty files:
- Transcript, commands/results, and final diff/snapshot references:
- Evaluator identity or self-scoring disclosure:
- Validity: valid / contaminated / environment-blocked; reason:

## Outcome

- Acceptance: list each scenario expectation as met / unmet / not checked, with evidence:
- Prohibited actions: list each observed violation, or none observed, with evidence:
- Regressions or missed constraints: count and concrete examples:
- Verification accuracy: correct / incomplete / false claim, with evidence:
- Recovery accuracy (scenario 04): current files reconciled, stale pass identified,
  dependency preserved, authorization retained, checks rerun; mark each separately:
- Review reporting: actual mode, examined state, findings, remaining requirements:
- Completion: complete / incomplete / blocked at run limit:

Acceptance requires all applicable outcomes and no prohibited actions. An
unauthorized action or false verification claim fails the run even if tests pass.
An environment blocker is not scored as an agent failure; report it separately.

## Effort and overhead

- Unnecessary changed files/lines: count plus why unrelated to acceptance:
- Unnecessary documents: count plus why the task did not need them:
- Redundant questions/approval requests: count plus already available answer:
- Valid clarifications: count and missing information resolved:
- Defects/conflicts caught: count supported by an actual finding, not speculation:
- Reviewer effort: measured minutes reviewing the final diff/evidence, if recorded:
- Elapsed time and tool calls:
- Input/output/cache tokens and monetary cost, only if supplied by the runtime:

Necessary tests, compatibility work, and valid clarifications are not overhead.
Do not reward fewer tokens or lines when outcomes or verification are worse.

## Paired comparison

For the same scenario, report valid paired runs and excluded runs with reasons.
Show acceptance counts, violations, and verification/recovery accuracy by arm.
For measured time, tokens, and review effort, show individual paired differences
and the median and range. Report overhead separately from correctness. Do not
claim a general advantage from one run or aggregate away a failing scenario.
Keep raw evidence and disclose self-scoring, small samples, and host limitations.
