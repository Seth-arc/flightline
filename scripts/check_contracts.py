#!/usr/bin/env python3
"""Validate optional Flightline JSON structure and repository-local file links.

Exit codes: 0 valid, 1 invalid contract, 2 unreadable or malformed input.
"""
import argparse
import json
import re
import sys
from pathlib import Path


SCHEMA_VERSIONS = (1, 2)
SEVERITIES = ('low', 'medium', 'high', 'critical')
KINDS = ('vertical', 'cross-sectional')
REASONS = ('migration-step', 'shared-interface', 'mechanical')
STATUSES = ('planned', 'in-progress', 'verified', 'blocked')
TIERS = ('routine', 'elevated', 'gated')
SLICE_ID = re.compile(r'^(.+)-S([1-9][0-9]*)$')
SCOPE = 'contract structure and file links only; behavior not verified'
V2_KEYS = {'acceptance_criteria', 'slices'}
KEYS = {
    'contract': {'schema_version', 'goal', 'user_model', 'constraints', 'decisions', 'non_goals'},
    'user_model': {'actor', 'task', 'assumption', 'status'},
    'constraints': {'id', 'statement', 'checks', 'owner', 'severity'},
    'decisions': {'id', 'statement', 'reason', 'status', 'revisit_when', 'superseded_by'},
    'acceptance_criteria': {'id', 'statement'},
    'slices': {'id', 'issue', 'kind', 'reason', 'enables', 'status', 'tier', 'criteria',
               'delivers', 'files', 'checks', 'rollback', 'depends_on'},
}


def unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f'duplicate JSON key: {key}')
        obj[key] = value
    return obj


def validate(data, root, require_ids=False):
    errors = []
    def fail(message):
        errors.append(message)
    def string(obj, key, loc):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            fail(f'{loc}.{key}: expected nonempty string')
            return None
        return value
    def known(obj, kind, loc, extra=()):
        for key in sorted(set(obj) - KEYS[kind] - set(extra)):
            fail(f'{loc}.{key}: unknown key')
    def local(link, label):
        if not isinstance(link, str) or not link.strip():
            fail(f'{label}: expected nonempty file path')
            return None
        path = Path(link)
        if path.is_absolute():
            fail(f'{label}: absolute path forbidden: {link}')
            return None
        target = (root / path).resolve()
        if not target.is_relative_to(root):
            fail(f'{label}: path escapes root: {link}')
            return None
        return target
    if not isinstance(data, dict):
        return ['contract: expected object']
    version = data.get('schema_version', 1)
    if type(version) is not int or version not in SCHEMA_VERSIONS:
        fail(f'contract.schema_version: expected one of {list(SCHEMA_VERSIONS)}')
        version = 1
    known(data, 'contract', 'contract', V2_KEYS)
    if version < 2:
        for key in sorted(V2_KEYS & set(data)):
            fail(f'contract.{key}: requires schema_version 2')
    string(data, 'goal', 'contract')
    user = data.get('user_model')
    if not isinstance(user, dict):
        fail('user_model: expected object')
    else:
        known(user, 'user_model', 'user_model')
        for key in ('actor', 'task', 'assumption'):
            string(user, key, 'user_model')
        if user.get('status') not in ('provisional', 'validated', 'invalidated'):
            fail('user_model.status: expected provisional, validated, or invalidated')
    groups = {}
    ids = set()
    decisions = {}
    for group in ('constraints', 'decisions'):
        rows = data.get(group)
        if not isinstance(rows, list):
            fail(f'{group}: expected array')
            rows = []
        groups[group] = rows
        for index, row in enumerate(rows):
            loc = f'{group}[{index}]'
            if not isinstance(row, dict):
                fail(f'{loc}: expected object')
                continue
            known(row, group, loc)
            ident = string(row, 'id', loc)
            string(row, 'statement', loc)
            if ident:
                if ident in ids:
                    fail(f'{loc}.id: duplicate {ident}')
                ids.add(ident)
            if group == 'constraints':
                if 'owner' in row:
                    string(row, 'owner', loc)
                if 'severity' in row and row.get('severity') not in SEVERITIES:
                    fail(f'{loc}.severity: expected low, medium, high, or critical')
                checks = row.get('checks')
                if not isinstance(checks, list) or not checks:
                    fail(f'{loc}.checks: expected nonempty array of file paths')
                    continue
                for link in checks:
                    target = local(link, f'{loc}.checks')
                    if target is None:
                        continue
                    if not target.is_file():
                        fail(f'{loc}.checks: file missing: {link}')
                    elif require_ids and ident:
                        try:
                            text = target.read_text(encoding='utf-8', errors='replace')
                        except OSError as exc:
                            fail(f'{loc}.checks: unreadable file: {link}: {exc}')
                            continue
                        if ident not in text:
                            fail(f'{loc}.checks: {ident} not referenced in {link}')
            else:
                string(row, 'reason', loc)
                string(row, 'revisit_when', loc)
                status = row.get('status')
                if status not in ('accepted', 'superseded'):
                    fail(f'{loc}.status: expected accepted or superseded')
                if status == 'superseded':
                    string(row, 'superseded_by', loc)
                elif 'superseded_by' in row:
                    fail(f'{loc}: accepted decision cannot have superseded_by')
                if ident:
                    decisions[ident] = row
    goals = data.get('non_goals')
    if not isinstance(goals, list) or any(not isinstance(x, str) or not x.strip() for x in goals):
        fail('non_goals: expected array of nonempty strings')
    cycles = set()
    for ident, row in decisions.items():
        replacement = row.get('superseded_by')
        if row.get('status') == 'superseded' and isinstance(replacement, str):
            if replacement == ident or replacement not in decisions:
                fail(f'{ident}.superseded_by: expected another existing decision')
        seen = []
        current = ident
        while current in decisions:
            if current in seen:
                cycle = frozenset(seen[seen.index(current):])
                if cycle not in cycles:
                    cycles.add(cycle)
                    fail(f'{min(cycle)}: supersession cycle')
                break
            seen.append(current)
            nxt = decisions[current].get('superseded_by')
            if not isinstance(nxt, str):
                break
            current = nxt
    if version >= 2 and V2_KEYS & set(data):
        criteria = {}
        rows = data.get('acceptance_criteria')
        if not isinstance(rows, list) or not rows:
            fail('acceptance_criteria: expected nonempty array')
            rows = []
        for index, row in enumerate(rows):
            loc = f'acceptance_criteria[{index}]'
            if not isinstance(row, dict):
                fail(f'{loc}: expected object')
                continue
            known(row, 'acceptance_criteria', loc)
            ident = string(row, 'id', loc)
            string(row, 'statement', loc)
            if ident:
                if ident in ids:
                    fail(f'{loc}.id: duplicate {ident}')
                ids.add(ident)
                criteria[ident] = False
        rows = data.get('slices')
        if not isinstance(rows, list):
            fail('slices: expected array')
            rows = []
        slices = {}
        for index, row in enumerate(rows):
            loc = f'slices[{index}]'
            if not isinstance(row, dict):
                fail(f'{loc}: expected object')
                continue
            known(row, 'slices', loc)
            ident = string(row, 'id', loc)
            issue = string(row, 'issue', loc)
            if ident:
                if ident in ids:
                    fail(f'{loc}.id: duplicate {ident}')
                ids.add(ident)
                match = SLICE_ID.match(ident)
                if not match or (issue and match.group(1) != issue):
                    fail(f'{loc}.id: expected <issue>-S<n> with n >= 1')
            kind = row.get('kind')
            if kind not in KINDS:
                fail(f'{loc}.kind: expected vertical or cross-sectional')
            elif kind == 'cross-sectional':
                if row.get('reason') not in REASONS:
                    fail(f'{loc}.reason: expected migration-step, shared-interface, or mechanical')
                string(row, 'enables', loc)
            else:
                for key in ('reason', 'enables'):
                    if key in row:
                        fail(f'{loc}.{key}: allowed only for cross-sectional slices')
            status = row.get('status')
            if status not in STATUSES:
                fail(f'{loc}.status: expected planned, in-progress, verified, or blocked')
            if row.get('tier') not in TIERS:
                fail(f'{loc}.tier: expected routine, elevated, or gated')
            string(row, 'delivers', loc)
            string(row, 'rollback', loc)
            refs = row.get('criteria', [])
            if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs):
                fail(f'{loc}.criteria: expected array of acceptance criterion IDs')
                refs = []
            if kind == 'vertical' and not refs:
                fail(f'{loc}.criteria: vertical slice must cover at least one criterion')
            for ref in refs:
                if ref not in criteria:
                    fail(f'{loc}.criteria: unknown criterion {ref}')
                else:
                    criteria[ref] = True
            files = row.get('files')
            if not isinstance(files, list) or not files:
                fail(f'{loc}.files: expected nonempty array of file paths')
                files = []
            for link in files:
                local(link, f'{loc}.files')
            checks = row.get('checks')
            if not isinstance(checks, list) or not checks:
                fail(f'{loc}.checks: expected nonempty array of file paths')
                checks = []
            for link in checks:
                target = local(link, f'{loc}.checks')
                if target is not None and status == 'verified' and not target.is_file():
                    fail(f'{loc}.checks: file missing for verified slice: {link}')
            deps = row.get('depends_on', [])
            if not isinstance(deps, list) or any(not isinstance(x, str) for x in deps):
                fail(f'{loc}.depends_on: expected array of slice IDs')
                deps = []
            for dep in deps:
                if dep not in slices:
                    fail(f'{loc}.depends_on: expected an earlier slice: {dep}')
                elif status == 'verified' and slices[dep] != 'verified':
                    fail(f'{loc}.depends_on: verified slice depends on unverified {dep}')
            if ident:
                slices[ident] = status
        for ident, covered in criteria.items():
            if not covered:
                fail(f'{ident}: not covered by any slice')
    return errors


def report(fmt, status, errors):
    if fmt == 'json':
        print(json.dumps({'status': status, 'errors': errors, 'scope': SCOPE}))
        return
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    if status == 'pass':
        print(f'PASS: {SCOPE}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract', type=Path)
    parser.add_argument('--root', type=Path, required=True, help='Repository root for check links')
    parser.add_argument('--require-id-in-checks', action='store_true',
                        help='Require each linked check file to contain its constraint ID')
    parser.add_argument('--format', choices=('text', 'json'), default='text',
                        help='Output format; json prints one object on stdout')
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error('--root must be an existing directory')
    try:
        data = json.loads(args.contract.read_text(encoding='utf-8'), object_pairs_hook=unique_pairs)
        errors = validate(data, root, args.require_id_in_checks)
    except (OSError, ValueError, RecursionError) as exc:
        report(args.format, 'error', [str(exc)])
        return 2
    if errors:
        report(args.format, 'fail', errors)
        return 1
    report(args.format, 'pass', [])
    return 0


if __name__ == '__main__':
    sys.exit(main())
