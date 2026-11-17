# Verification policy

Select checks by behavioral impact, not changed line count.

| Change | Evidence |
|---|---|
| Copy or style | Applicable build and focused rendered inspection |
| Business logic | Acceptance behavior, meaningful edge cases, affected integration |
| Permissions or persistence | Negative cases, authoritative boundary, compatibility and recovery |
| Timing or concurrency | Defined workload, resource budgets, fault behavior, repeatability |
| Hardware interface | Representative target or clearly labeled simulation limits |
| Public API or schema | Backward-compatibility or contract tests, deprecation path |
| Data migration | Dry run, expand/contract sequencing, tested rollback |
| Dependency upgrade | Changelog review, lockfile diff, vulnerability and licence scan |
| Infrastructure or config | Plan diff, staged rollout, rollback step |
| Security-sensitive | Negative authorization tests, abuse cases |

Reuse existing commands. Read untrusted project scripts before execution where
appropriate. Avoid tests that merely duplicate implementation. A broader suite
is warranted when shared interfaces or uncertain impact make selection unsafe.
Do not skip mandatory repository checks to meet an informal token target.

Summarize check output; retain and link raw logs when needed for diagnosis or
reproduction. Run broad suites after the design and focused checks are settled.

For performance, declare workload, environment, baseline, measurement method,
threshold and variance. Do not invent targets or claim an optimization from code
inspection alone. Control clocks, random seeds, ordering and external inputs for
replay when feasible; document tolerances otherwise.

Flaky tests: record the failure and the evidence that it is intermittent and
unrelated. Use the repository's existing quarantine mechanism if one exists.
Never retry silently until green, and never report a retried pass as a clean pass.

## Evidence tied to tested state

Capture the state used by each check or group of checks sharing the same inputs.
Reuse existing CI run and artifact identifiers when they identify that state.
For a local run, record the revision plus an identifiable snapshot or content
digest of relevant staged, unstaged, and untracked inputs, including deletions.
A commit ID, timestamp, or list of changed filenames alone cannot identify dirty
contents. Without usable version control, use a snapshot or file-content hashes
and state the limitation; do not create a commit just to obtain an identifier.

Record the command, working directory, outcome, and material runtime, dependency,
configuration, fixture, or external-service inputs. Describe relevant environment
settings without copying credentials or personal data. Keep shared context once
and reference it from related checks. Routine work can retain this evidence in
the existing tool output or CI run without a separate receipt file.

Before reporting a result against the final state, check for input changes since
the run, including changes made while it was running. If the tested state cannot
be established, report that uncertainty and rerun against a known state when
feasible. Do not relabel an earlier pass as a pass of later code.

When relevant source, tests, dependencies, configuration, or environment changes,
keep the original outcome attached to its original state and mark its applicability
to the current state as stale. Rerun affected checks before using them as current
evidence. Retain other results only when their input scope is known and unaffected;
if impact is uncertain, broaden the checks or report the remaining gap. A failing
result is not resolved merely because it is stale. Required repository checks
still apply even when narrower evidence could otherwise be reused.

For example, a documentation-only edit may leave an isolated logic-test result
applicable; a change to that test's dependency lockfile requires reassessment.
Passing structural validation of a contract proves neither its behavioral claims
nor that its recorded `verified` status is current.

## Verification receipt

For routine work, report what changed, checks run and their outcomes, and gaps
or pre-existing failures. No separate receipt is required.

For consequential work or a handoff, use the existing PR or change record and
include the applicable fields below. Omit irrelevant fields unless repository
policy requires them; do not omit material verification gaps.

- Request or ticket reference:
- Slice ID, kind, and resulting status, if the work was sliced:
- Risk tier (of the slice, if sliced):
- Tested state identifier and relevant changed inputs:
- Commands and working directory, outcomes, and evidence/run references:
- Material environment and dependency inputs:
- Acceptance criteria mapped to supporting checks and observed results:
- Evidence applicability: current or stale, with reason and needed rechecks:
- Uncovered or partially covered criteria and items not checked:
- Pre-existing failures, with evidence:
- Review mode/reviewer, reviewed state, findings, limitations, and pending requirements:
- Rollback step (Elevated):

Never label a linked test as proof merely because its file exists. Preserve
concise summaries; retain raw logs when needed to reproduce a failure. Tie
evidence to tested inputs.

## Repeated failures

After two failed repair attempts on one failure, capture the reproducer, examine
why the current explanation failed, choose a new hypothesis, and run a check
that distinguishes it from alternatives. If that hypothesis also fails, write the
reproducer and what was ruled out to a checkpoint and reassess from that evidence.
Use a fresh context if helpful and available; otherwise continue with an explicit
reassessment. Do not repeat an unchanged hypothesis without new evidence.
Continue useful work within scope; escalate only genuine blockers. Never loosen
checks to conceal failure.

## Review and its limits

For Elevated changes, use a fresh-context reviewer when available and authorized.
Provide the request or plan, acceptance criteria, affected decisions, final diff,
and state-bound check results as starting evidence. Allow inspection of relevant
source, callers, and tests. Review decision conflicts, behavioral regressions,
compatibility, failure paths, and verification gaps applicable to the change.
Record findings with locations and consequences, without incidental rewrites.

If fresh-context review is unavailable or not authorized, perform an explicit
second pass over the final diff and supporting evidence. Report why this fallback
was used and label it self-review. A new prompt to the same ongoing implementation
context is not an independent review. A fresh agent review does not substitute
for a required human or code-owner review unless repository policy permits it.

In the existing receipt or review record, identify the actual reviewer or mode
(independent human, fresh-context agent, or self-review), reviewed state, findings
and their disposition, scope limitations, and unmet review requirements. If no
defects were found, say so within the examined scope; do not claim complete
assurance. A planned or unavailable review is pending, not completed.

After fixes or other edits, reassess affected findings and verification evidence,
and review the affected final changes before carrying forward the outcome.
Retain an earlier review only for portions whose relevant inputs are unchanged.
If repository policy requires independent review, leave that requirement pending,
do not claim the change is ready for the action it gates, and continue authorized
work that does not depend on it.
