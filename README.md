# Flightline

Every change preserves agreed intent, produces reviewable evidence, and can be
resumed without losing important decisions.

Flightline is an agent skill for maintaining existing software and developing
coherent designs. It adds proportionate planning, decision-impact review,
verification, and recovery guidance to your existing workflow. It does not
replace your issue tracker, specifications, test runner, or PR conventions.

## Install and invoke

Copy this folder, retaining the name `flightline`, into your Codex skills directory:
`$CODEX_HOME/skills/flightline`, or `~/.codex/skills/flightline` when `CODEX_HOME`
is unset. On Windows, `~` means your user profile directory. Preserve the complete
folder structure, including `references/`, `scripts/`, and `agents/`. Check for an
existing installation before copying; do not overwrite local changes blindly.
Start a new session and invoke `$flightline`.

For a project-local trial without installing, ask your agent to read
`<absolute-path-to-flightline>/SKILL.md` and use it for the requested task.
Other hosts must support loading skills or their equivalent; metadata alone
does not establish host compatibility. Automatic invocation remains enabled for
hosts that honor `agents/openai.yaml`.

Routine example:

> Use $flightline to fix whitespace handling in this name formatter. Preserve
> its existing interface and verify the changed behavior.

Expected treatment: inspect affected behavior, make a focused fix, run relevant
checks, and summarize results. No planning files or commits solely for ceremony.

Consequential example:

> Use $flightline to add paginated results while preserving existing list
> consumers. Implement and test locally; deployment is outside this task.

Expected treatment: identify affected contracts and decisions, record a concise
plan and rollback, check compatibility, and produce evidence tied to the tested
state. Use independent review when available and authorized, otherwise identify
self-review and any required review still pending.

## Requirements and checks

The skill text needs no runtime. The optional validator requires Python 3.9+
and uses only the standard library. It has been exercised here with Python
3.12.10 on Windows; other Python/OS combinations have not been tested here.
From this folder, run:

```text
python -B scripts/test_check_contracts.py
```

Use `python3`, `py -3`, or an absolute Python executable path if your system's
`python` launcher is unavailable. No package installation is needed.

Only if your project adopts the optional JSON contract format:

```text
python scripts/check_contracts.py path/to/design.json --root path/to/project --format json
```

Schema versions 1 and 2, including legacy `gated` records, remain accepted. A
validator pass establishes structure and local file links, not test success,
evidence freshness, authorization, or correct design. Existing project formats
remain the default; see [design records](references/design-record.md).

## Evaluate the workflow

[The evaluation suite](evaluations/README.md) contains seven isolated projects,
exact task prompts, setup instructions, expected outcomes, prohibited actions,
and a paired-run scorecard. Node.js 18+ is needed for these synthetic projects;
npm is needed only for the local dependency scenario. Neither is required for
Flightline's Python validator. Check the fixture baselines with:

```text
python -B scripts/test_workflow_fixtures.py
```

Some fixture tests deliberately fail before an agent completes its task. The
fixture health check verifies those expected failures; it is not an evaluation
of an agent. No comparative performance claim follows from fixture validation.

## Ownership, versioning, and distribution

Package version: **0.1.0 (unreleased)**. This README is the package version record;
JSON `schema_version` is separate. Increment the package version and record the
change below when the workflow or packaging changes. Breaking contract-format
changes require a new schema version while retaining older supported versions.

Maintainer: **Sethu Nguna**. Copyright **2026 Sethu Nguna**.
Licensed under [Apache License 2.0](LICENSE); see [NOTICE](NOTICE) for attribution.
This covers the skill, references, scripts, and synthetic evaluation fixtures.
The bundled evaluation dependency is part of this package, not a separately
licensed third-party product. No external contact address has been designated.

### 0.1.0 — 2026-11-17 (unreleased)

- Separate technical risk from authorization and keep routine work small.
- Support evolving plans, interrupted-work recovery, and decision-impact review.
- Tie verification and review to the examined state and report limitations.
- Add workflow evaluation fixtures, adoption documentation, and portable path tests.
- Remove metadata references to missing optional icon assets.
- Establish Apache-2.0 licensing and Sethu Nguna as maintainer and copyright holder.

Maintenance guidance: [references/skill-maintenance.md](references/skill-maintenance.md).

## GitHub Pages

The static landing page lives in `docs/` and uses the supplied Settle design
language. It has no build dependencies. Preview it with:

```text
python -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Open `http://127.0.0.1:4173`. Before publishing changes to the downloadable skill,
run `python scripts/package_site.py`; it creates and verifies the ZIP served by
the page. The ZIP includes skill sources and evaluations, excluding the website
and local preview artifacts.

Publish `main` → `/docs` under the repository's Settings → Pages → Deploy from a
branch, as described in [GitHub's publishing guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
All site assets use relative paths so project Pages URLs work. The Settle font
stylesheet loads Google Fonts and includes local fallback fonts.

`scripts/check_site.js` is an assertion-based browser check: use the Playwright
browser tool's run-code filename option after navigating to the local preview.
It covers responsive layout, keyboard selection, appearance, clipboard fallback,
download availability, reduced motion, and content without JavaScript.
