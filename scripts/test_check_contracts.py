#!/usr/bin/env python3
"""Tests for check_contracts.py. Run: python3 scripts/test_check_contracts.py"""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_contracts  # noqa: E402

SCRIPT = HERE / 'check_contracts.py'

BASE = {
    'schema_version': 1,
    'goal': 'Help facilitators manage live sessions.',
    'user_model': {
        'actor': 'facilitator',
        'task': 'identify missing submissions',
        'assumption': 'Must work while addressing participants.',
        'status': 'provisional',
    },
    'constraints': [
        {'id': 'INV-001', 'statement': 'State unchanged on reject.', 'checks': ['tests/a.test.ts']},
    ],
    'decisions': [
        {'id': 'DEC-001', 'statement': 'Server owns transitions.', 'reason': 'Clients may be stale.',
         'status': 'accepted', 'revisit_when': 'Runtime changes.'},
    ],
    'non_goals': ['Replace authentication.'],
}


class ValidateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / 'tests').mkdir()
        (self.root / 'tests' / 'a.test.ts').write_text('// covers INV-001\n', encoding='utf-8')
        self.data = copy.deepcopy(BASE)

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self, **kwargs):
        return check_contracts.validate(self.data, self.root, **kwargs)

    def test_valid(self):
        self.assertEqual(self.errors(), [])

    def test_schema_version_optional(self):
        del self.data['schema_version']
        self.assertEqual(self.errors(), [])

    def test_schema_version_unsupported(self):
        for value in (3, '1', True):
            self.data['schema_version'] = value
            self.assertTrue(any('schema_version' in e for e in self.errors()), value)

    def test_unknown_keys(self):
        self.data['extra'] = 1
        self.data['user_model']['role'] = 'x'
        self.data['constraints'][0]['check'] = ['tests/a.test.ts']
        self.data['decisions'][0]['checks'] = ['tests/a.test.ts']
        found = self.errors()
        for expected in ('contract.extra', 'user_model.role', 'constraints[0].check:', 'decisions[0].checks'):
            self.assertTrue(any(expected in e and 'unknown key' in e for e in found), expected)

    def test_owner_and_severity(self):
        self.data['constraints'][0].update(owner='platform-team', severity='high')
        self.assertEqual(self.errors(), [])
        self.data['constraints'][0].update(owner=' ', severity='urgent')
        found = self.errors()
        self.assertTrue(any('.owner' in e for e in found))
        self.assertTrue(any('.severity' in e for e in found))

    def test_missing_and_escaping_paths(self):
        self.data['constraints'][0]['checks'] = [
            'tests/none.ts', '../outside.ts', str(self.root / 'absolute.test.ts')]
        found = self.errors()
        self.assertTrue(any('file missing' in e for e in found))
        self.assertTrue(any('escapes root' in e for e in found))
        self.assertTrue(any('absolute path forbidden' in e for e in found))

    def test_duplicate_ids(self):
        self.data['decisions'][0]['id'] = 'INV-001'
        self.assertTrue(any('duplicate INV-001' in e for e in self.errors()))

    def test_require_ids(self):
        self.assertEqual(self.errors(require_ids=True), [])
        (self.root / 'tests' / 'a.test.ts').write_text('// nothing\n', encoding='utf-8')
        self.assertEqual(self.errors(), [])
        self.assertTrue(any('INV-001 not referenced' in e for e in self.errors(require_ids=True)))

    def test_supersession(self):
        self.data['decisions'][0].update(status='superseded', superseded_by='DEC-002')
        self.assertTrue(any('expected another existing decision' in e for e in self.errors()))
        self.data['decisions'].append(
            {'id': 'DEC-002', 'statement': 's', 'reason': 'r', 'status': 'accepted', 'revisit_when': 'w'})
        self.assertEqual(self.errors(), [])

    def test_cycle_reported_once(self):
        row = {'statement': 's', 'reason': 'r', 'status': 'superseded', 'revisit_when': 'w'}
        self.data['decisions'] = [
            dict(row, id='DEC-001', superseded_by='DEC-002'),
            dict(row, id='DEC-002', superseded_by='DEC-001'),
            dict(row, id='DEC-003', superseded_by='DEC-001'),
        ]
        cycles = [e for e in self.errors() if 'supersession cycle' in e]
        self.assertEqual(cycles, ['DEC-001: supersession cycle'])

    def run_cli(self, text, *extra):
        contract = self.root / 'design.json'
        contract.write_text(text, encoding='utf-8')
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(contract), '--root', str(self.root), *extra],
            capture_output=True, text=True)

    def test_cli_text(self):
        result = self.run_cli(json.dumps(self.data))
        self.assertEqual(result.returncode, 0)
        self.assertTrue(result.stdout.startswith('PASS:'))

    def test_cli_json(self):
        result = self.run_cli(json.dumps(self.data), '--format', 'json')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)['status'], 'pass')
        self.data['goal'] = ''
        result = self.run_cli(json.dumps(self.data), '--format', 'json')
        self.assertEqual(result.returncode, 1)
        body = json.loads(result.stdout)
        self.assertEqual(body['status'], 'fail')
        self.assertTrue(body['errors'])

    def test_cli_duplicate_json_key_and_malformed(self):
        result = self.run_cli('{"goal": "a", "goal": "b"}')
        self.assertEqual(result.returncode, 2)
        self.assertIn('duplicate JSON key: goal', result.stderr)
        result = self.run_cli('{not json', '--format', 'json')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)['status'], 'error')


class SliceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / 'tests').mkdir()
        (self.root / 'tests' / 'a.test.ts').write_text('// covers INV-001\n', encoding='utf-8')
        self.data = copy.deepcopy(BASE)
        self.data['schema_version'] = 2
        self.data['acceptance_criteria'] = [
            {'id': 'AC-001', 'statement': 'Missing submissions are listed.'},
            {'id': 'AC-002', 'statement': 'The list updates on submit.'},
        ]
        self.data['slices'] = [
            {'id': 'PROJ-12-S1', 'issue': 'PROJ-12', 'kind': 'cross-sectional',
             'reason': 'migration-step', 'enables': 'PROJ-12', 'status': 'verified',
             'tier': 'gated', 'delivers': 'Adds nullable submitted_at column.',
             'files': ['db/migrations/004.sql'], 'checks': ['tests/a.test.ts'],
             'rollback': 'Drop the column.'},
            {'id': 'PROJ-12-S2', 'issue': 'PROJ-12', 'kind': 'vertical', 'status': 'planned',
             'tier': 'routine', 'criteria': ['AC-001', 'AC-002'],
             'delivers': 'Facilitator sees missing submissions.',
             'files': ['src/list.ts'], 'checks': ['tests/list.test.ts'],
             'rollback': 'Revert the commit.', 'depends_on': ['PROJ-12-S1']},
        ]

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self):
        return check_contracts.validate(self.data, self.root)

    def has(self, text):
        return any(text in e for e in self.errors())

    def test_valid(self):
        self.assertEqual(self.errors(), [])

    def test_requires_version_2(self):
        self.data['schema_version'] = 1
        found = self.errors()
        self.assertTrue(any('slices: requires schema_version 2' in e for e in found))
        self.assertTrue(any('acceptance_criteria: requires schema_version 2' in e for e in found))

    def test_version_2_without_slices(self):
        del self.data['slices'], self.data['acceptance_criteria']
        self.assertEqual(self.errors(), [])

    def test_slices_need_criteria(self):
        del self.data['acceptance_criteria']
        self.assertTrue(self.has('acceptance_criteria: expected nonempty array'))

    def test_id_format(self):
        for bad in ('S2', 'PROJ-12-S0', 'OTHER-1-S2', 'PROJ-12-2'):
            self.data['slices'][1]['id'] = bad
            self.assertTrue(self.has('expected <issue>-S<n>'), bad)

    def test_enumerations(self):
        self.data['slices'][1].update(kind='horizontal', status='done', tier='high')
        for expected in ('.kind:', '.status:', '.tier:'):
            self.assertTrue(self.has(expected), expected)

    def test_cross_sectional_rules(self):
        self.data['slices'][0]['reason'] = 'convenience'
        del self.data['slices'][0]['enables']
        self.assertTrue(self.has('slices[0].reason'))
        self.assertTrue(self.has('slices[0].enables'))

    def test_vertical_rules(self):
        self.data['slices'][1].update(reason='mechanical', criteria=[])
        self.assertTrue(self.has('slices[1].reason: allowed only for cross-sectional'))
        self.assertTrue(self.has('vertical slice must cover at least one criterion'))

    def test_coverage(self):
        self.data['slices'][1]['criteria'] = ['AC-001', 'AC-009']
        self.assertTrue(self.has('unknown criterion AC-009'))
        self.assertTrue(self.has('AC-002: not covered by any slice'))

    def test_paths(self):
        self.data['slices'][1]['files'] = ['../x.ts', str(self.root / 'absolute.ts')]
        self.assertTrue(self.has('slices[1].files: path escapes root'))
        self.assertTrue(self.has('slices[1].files: absolute path forbidden'))

    def test_verified_needs_check_file(self):
        self.data['slices'][0]['checks'] = ['tests/none.ts']
        self.assertTrue(self.has('file missing for verified slice'))

    def test_dependencies(self):
        self.data['slices'][1]['depends_on'] = ['PROJ-12-S9']
        self.assertTrue(self.has('expected an earlier slice: PROJ-12-S9'))
        self.data['slices'][1]['depends_on'] = ['PROJ-12-S1']
        self.data['slices'][0]['status'] = 'in-progress'
        self.data['slices'][1]['status'] = 'verified'
        (self.root / 'tests' / 'list.test.ts').write_text('x', encoding='utf-8')
        self.assertTrue(self.has('verified slice depends on unverified PROJ-12-S1'))

    def test_ids_unique_across_groups(self):
        self.data['acceptance_criteria'][0]['id'] = 'INV-001'
        self.assertTrue(self.has('duplicate INV-001'))

    def test_unknown_slice_key(self):
        self.data['slices'][1]['owner'] = 'x'
        self.assertTrue(self.has('slices[1].owner: unknown key'))


if __name__ == '__main__':
    unittest.main()
