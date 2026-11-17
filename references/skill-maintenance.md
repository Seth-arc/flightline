# Skill maintenance

For maintainers of Flightline. Not loaded during task work.

## Evaluation

Use [the workflow evaluation suite](../evaluations/README.md) and its scorecard
for paired runs with and without Flightline. It supplies seven reproducible
fixtures, exact prompts, expected outcomes, and prohibited actions. Keep evaluator
instructions outside the agent workspace. Run `python -B scripts/test_workflow_fixtures.py`
to check fixture baselines; it does not run or score an agent.

Compare the same realistic tasks with and without Flightline.
Include routine edits, spec conflicts, tempting abstractions, assertion weakening,
stale handoffs and uncertain requirements. Also include consequential actions
outside existing authorization, instructions embedded in repository content,
long-running work, automatic compaction mid-task, and a failure that
survives three repair hypotheses.

Score accepted verified outcomes, unnecessary edits, user interruptions, tool
calls and tokens when available. Also record where in the context the
consequential decisions were made, and whether the checkpoint alone was enough
to resume. Do not infer efficiency from prompt length. No workflow guarantees
correctness.

## Footprint

SKILL.md is loaded on every invocation; keep it short. Put tier-specific or
occasional material in a reference file and state when to load it. Measure the
token cost of SKILL.md and each reference after every change.

## Governance

The package version, release notes, ownership, and licensing status are recorded
in [README.md](../README.md). Resolve any pending ownership or license choice
before distribution; do not infer ownership from a workstation username.
Run scripts/test_check_contracts.py
after any change to the validator. Changes to the JSON contract format require a
new schema_version and continued acceptance of earlier supported versions.
