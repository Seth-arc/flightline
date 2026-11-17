# Design records

Use existing repository formats first. These templates are for consequential
decisions, complex work, and handoffs; routine changes need no persistent record
unless policy requires one. Include applicable fields without duplicating records.

## Short change contract

- Actor / task / operating conditions:
- Intended outcome and non-goals:
- Risk tier and reason:
- Authorization source, covered actions and targets, limits or pending approval:
- Binding constraints and affected decisions:
- Assumptions / unknowns:
- Acceptance criteria and relevant checks:

## Decision or experiment

- Decision ID and status (accepted or superseded):
- Decision and reason:
- Material alternative rejected and reason:
- Evidence or experiment result:
- Revisit condition:
- Replacement ID, if superseded:

For experiments also state the question, time/resource bound, and whether the
artifact is disposable. Record observable evidence, not private deliberation.

## Decision-impact review

Before consequential changes, locate affected accepted decisions in existing
specifications, ADRs, or project records. Follow relevant callers and contracts
to assess behavioral impact, not just matching filenames. If no decision is
documented, identify that gap and label inferred intent as an assumption.

For each affected decision, record in the existing plan or review:

- Decision reference and the behavior it protects:
- Supporting assumption and evidence that it still holds, changed, or is unknown:
- Revisit condition and whether the proposal or current evidence triggers it:
- Affected code/contract reference, proposed behavior, and any concrete conflict:
- Resolution: preserve the decision, investigate an unknown, or propose replacement:

A triggered revisit condition calls for reassessment; it does not revoke the
decision. Prefer an implementation that preserves accepted intent. If the
requested outcome requires a conflicting change, resolve authority and scope
before implementing that conflict; continue unaffected work. When replacement
is authorized, retain the old rationale and link the superseding decision.
Recheck affected decisions when implementation discoveries or the final diff
change the assumptions; do not audit unrelated decisions for a routine fix.

Example: an accepted requirement for immediate access revocation conflicts with
a proposed permission cache that can return a revoked grant until expiry.
Reference the actual requirement and cache lookup/invalidation path, then assess
an invalidation mechanism or an authorized requirement change. Do not invent a
requirement or assume a cache is unsafe merely because it exists.

## Research findings

When findings need to survive a handoff or guide complex work, record a short
note: the question, what was found, and file and symbol references (path, symbol,
line where useful). Do not paste file contents. State what was not examined.

## Implementation plan

Write the plan so a fresh context can execute it without the conversation.

- Goal and acceptance criteria (verbatim from the change contract):
- Risk tier, rollback step:
- Authorization source, covered actions and targets, limits or pending approval:
- Constraints and decisions that bind this work (IDs or references):
- Steps, each with: files and symbols, the change, and the check for that step:
- Starting files and symbols to inspect:
- Out of scope:

Investigate additional callers, configuration, fixtures, and dependencies as
needed. Make necessary supporting fixes within the agreed scope and update the
plan when discoveries materially affect implementation or checks. Clarify
unresolved changes to agreed behavior, scope, or authority; discovering another
file is not itself an approval boundary. Explicit protected-path rules still apply.

Split into slices when size, uncertainty, or dependencies warrant independently
verifiable increments. Follow repository commit and PR conventions.

## Slice record

Label each acceptance criterion with an ID. Use the repository's existing
criterion or requirement IDs where they exist; otherwise use plan-local labels
AC-001, AC-002, and so on. These are labels for criteria already derived from
the request, not new requirements.

When slice records are useful, list them in execution order using the existing
project format or this template. The optional JSON format below retains its
required fields and enumerated values.

| Field | Value |
|---|---|
| id | `<issue>-S<n>`, n from 1, for example PROJ-12-S2 |
| issue | Existing issue or sub-issue reference; `request` when no tracker is used |
| kind | `vertical` or `cross-sectional` |
| reason | Cross-sectional only: `migration-step`, `shared-interface`, or `mechanical` |
| enables | Cross-sectional only: the issue this slice unblocks |
| status | `planned`, `in-progress`, `verified`, or `blocked` |
| tier | `routine` or `elevated`; legacy JSON `gated` remains accepted (see below) |
| criteria | Acceptance criterion IDs covered; at least one for a vertical slice |
| delivers | The observable behavior, or for cross-sectional slices the capability added |
| files | Expected repository-relative paths; update as in-scope dependencies emerge |
| checks | The runnable command or repository-relative check file proving the slice |
| rollback | The step that reverses this slice |
| depends_on | IDs of earlier slices that must be verified first; omit if none |

Rules:

- Every acceptance criterion is covered by at least one slice.
- A vertical slice has no reason or enables field.
- A slice depends only on slices listed before it.
- A slice is `verified` only after its checks ran and passed for the applicable
  state and every slice it depends on is verified. If affected evidence becomes
  stale, return it to `in-progress` until revalidated; use `blocked` only for an
  actual blocker. Dependent slices cannot remain `verified` while a declared
  dependency is unverified; reuse unaffected check evidence when restoring status.
- Investigate additional files and make necessary in-scope fixes; update the
  record for material discoveries, respecting explicit protected-path rules.
- Assess authorization per action, separately from tier. Carry existing approval
  across slices within its scope; request only missing authorization.

Update status in the plan as work proceeds; cite the slice ID if making a checkpoint.

## Session checkpoint

Keep a checkpoint when work is long or uncertain, before an anticipated
interruption, or for a handoff. Use the existing project location; phase changes
alone do not require checkpoints. Record the applicable state:

- Goal and acceptance criteria, verbatim rather than paraphrased:
- Decisions made, each with its reason:
- Authorization source, covered actions and targets, limits or pending approval:
- What was tried and ruled out:
- Tested state and evidence references (references/verification-policy.md):
- Checks run, outcomes and stale evidence, uncovered criteria, unresolved failures:
- Review mode, reviewed state, findings, and pending required review, if applicable:
- Current assumptions:
- Plan path and current slice/step, if used; incomplete edits or operations:
- Next action, specific enough to execute cold:

Leave out file contents, raw logs, secrets, and the narrative of how the work
got here. Avoid proliferating journals. If compaction can be guided, preserve the
checkpoint location and any decisions or authorization not yet recorded there.

On resumption or after compaction:

1. Inspect current files and the working tree; preserve unrelated changes and
   identify incomplete edits before continuing them.
2. Compare the plan and checkpoint with current dependencies, configuration,
   decisions, and available check and review results. Use the evidence rules in
   references/verification-policy.md to revalidate affected results and retain
   evidence whose inputs still apply.
3. Carry forward authorization supported by its recorded source within the same
   actions, targets, and limits. Do not infer approval from a completed status.
   Ask only for missing authorization needed by the next consequential action.
4. Update stale plan details and continue from the next valid step. If the
   checkpoint is missing or incomplete, reconstruct needed state from available
   evidence; clarify only consequential gaps that cannot be resolved locally.

For example, if another developer changed a dependency during an interruption,
inspect its effect on the implementation and prior checks, preserve that change,
and rerun affected verification before relying on the earlier result.

## Optional JSON contract format

Adopt only if the project has no suitable equivalent and the task warrants it.
Decision-impact findings, verification receipts, and review records stay in
existing project records; they add no keys to the JSON schemas below. Structural
validation does not establish decision consistency, test success, or evidence freshness.
Use a repository-local JSON file (for example spec/design.json):

```json
{
  "schema_version": 1,
  "goal": "Help facilitators manage live sessions.",
  "user_model": {
    "actor": "facilitator",
    "task": "identify missing submissions",
    "assumption": "Must work while addressing participants.",
    "status": "provisional"
  },
  "constraints": [
    {
      "id": "INV-001",
      "statement": "Rejected transitions leave authoritative state unchanged.",
      "checks": ["tests/stage-transition.test.ts"],
      "owner": "platform-team",
      "severity": "high"
    }
  ],
  "decisions": [
    {
      "id": "DEC-001",
      "statement": "The server owns stage transitions.",
      "reason": "Clients may be stale or bypassed.",
      "status": "accepted",
      "revisit_when": "The authoritative runtime changes."
    }
  ],
  "non_goals": ["Replace authentication."]
}
```

Validate with:
`python3 <skill-dir>/scripts/check_contracts.py spec/design.json --root <repo-root>`
Resolve <skill-dir> from this skill's actual installed path. Paths in checks are
repository-relative file links, not shell commands, globs, URLs, or test IDs.
IDs are globally unique across constraints and decisions. A superseded decision
must name a different existing decision in superseded_by; cycles are invalid.

schema_version is optional and defaults to 1; supported versions are 1 and 2,
and others are rejected.
Unknown keys and duplicate JSON keys are rejected. Constraints may carry an
optional owner (nonempty string) and severity (low, medium, high, or critical).

### Slices in the JSON contract

Set schema_version to 2 to record acceptance criteria and slices. Both keys are
optional; if either is present, acceptance_criteria must be a nonempty array.
Fields and values match the slice record above.

Schema versions 1 and 2 remain unchanged. In version 2, `tier: "gated"` remains
accepted for older records. Treat it as a legacy marker for Elevated review and
assess current action authorization separately; it neither grants permission nor
automatically requires renewed approval. Use `routine` or `elevated` in new
records. Record authorization in the existing plan or checkpoint, not as new JSON
keys: the validator rejects unknown keys and does not validate authorization.

```json
{
  "schema_version": 2,
  "acceptance_criteria": [
    {"id": "AC-001", "statement": "Missing submissions are listed."}
  ],
  "slices": [
    {
      "id": "PROJ-12-S1",
      "issue": "PROJ-12",
      "kind": "cross-sectional",
      "reason": "migration-step",
      "enables": "PROJ-12",
      "status": "verified",
      "tier": "elevated",
      "delivers": "Adds nullable submitted_at column.",
      "files": ["db/migrations/004.sql"],
      "checks": ["tests/migration-004.test.ts"],
      "rollback": "Drop the column."
    },
    {
      "id": "PROJ-12-S2",
      "issue": "PROJ-12",
      "kind": "vertical",
      "status": "planned",
      "tier": "routine",
      "criteria": ["AC-001"],
      "delivers": "Facilitator sees missing submissions.",
      "files": ["src/list.ts", "tests/list.test.ts"],
      "checks": ["tests/list.test.ts"],
      "rollback": "Revert the commit.",
      "depends_on": ["PROJ-12-S1"]
    }
  ]
}
```

The example omits the other required top-level keys for brevity. In JSON, checks
are repository-relative file links, as for constraints, not commands.

The validator enforces: the ID format and its match to issue; the enumerated
values; reason and enables on cross-sectional slices only; at least one
criterion per vertical slice; every criterion covered; criterion references
exist; dependencies name earlier slices; a verified slice has existing check
files and verified dependencies; paths are relative and inside the root; IDs are
unique across constraints, decisions, criteria, and slices. Files in a slice's
files list need not exist yet. It does not check that a slice stayed within its
files, that checks passed, or that status is truthful.

Options:
- `--require-id-in-checks`: each linked check file must contain its constraint ID.
  This shows the file refers to the constraint, not that it tests it.
- `--format json`: print a machine-readable result on stdout for CI.

Exit codes: 0 valid, 1 invalid contract, 2 unreadable or malformed input.
The validator never executes checks, follows network links, proves test coverage,
or checks whether the design is correct. Use existing test runners separately.
