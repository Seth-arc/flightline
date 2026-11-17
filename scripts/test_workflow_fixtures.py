"""Check evaluation fixture behavior, not agent performance. Requires Node.js 18+."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


FIXTURES = Path(__file__).resolve().parents[1] / 'evaluations' / 'fixtures'
NODE = shutil.which('node')


class WorkflowFixturesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if NODE is None:
            raise RuntimeError('Node.js is required for workflow fixture checks')

    def check(self, workspace, filename, passes):
        result = subprocess.run(
            [NODE, filename], cwd=workspace, capture_output=True, text=True, timeout=15)
        if passes:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('AssertionError', result.stderr)

    def test_starting_behavior(self):
        cases = [
            ('01-routine', 'test.cjs', False),
            ('02-dependency', 'test.cjs', False),
            ('03-dirty-tree', 'test.cjs', False),
            ('04-stale-checkpoint', 'test.cjs', True),
            ('05-failing-baseline', 'test-name.cjs', False),
            ('05-failing-baseline', 'test-badge.cjs', False),
            ('06-compatibility', 'test.cjs', True),
            ('07-decision-conflict', 'test.cjs', True),
        ]
        for scenario, test, passes in cases:
            with self.subTest(scenario=scenario, test=test):
                self.check(FIXTURES / scenario, test, passes)

    def test_dependency_update_invalidates_old_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / 'project'
            shutil.copytree(FIXTURES / '04-stale-checkpoint', workspace)
            self.check(workspace, 'test.cjs', True)
            dependency = "exports.version = '2.0.0';\nexports.encode = value => ({ text: value.toLowerCase() });\n"
            (workspace / 'dependency.cjs').write_text(dependency, encoding='utf-8')
            self.check(workspace, 'test.cjs', False)
            app = workspace / 'app.cjs'
            app.write_text(app.read_text(encoding='utf-8').replace(
                'encode(value);', 'encode(value).text;'), encoding='utf-8')
            self.check(workspace, 'test.cjs', True)
            self.assertEqual((workspace / 'dependency.cjs').read_text(encoding='utf-8'), dependency)

    def test_formatter_fix_leaves_unrelated_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / 'project'
            shutil.copytree(FIXTURES / '05-failing-baseline', workspace)
            app = workspace / 'app.cjs'
            app.write_text(app.read_text(encoding='utf-8').replace(
                'value.toLowerCase()', 'value.trim().toLowerCase()'), encoding='utf-8')
            self.check(workspace, 'test-name.cjs', True)
            self.check(workspace, 'test-badge.cjs', False)

    def test_cache_without_invalidation_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / 'project'
            shutil.copytree(FIXTURES / '07-decision-conflict', workspace)
            app = workspace / 'app.cjs'
            source = app.read_text(encoding='utf-8').replace(
                'const grants = new Set();', 'const grants = new Set();\n  const cache = new Map();')
            source = source.replace('canAccess: id => grants.has(id),', '''canAccess: id => {
      if (!cache.has(id)) cache.set(id, grants.has(id));
      return cache.get(id);
    },''')
            app.write_text(source, encoding='utf-8')
            self.check(workspace, 'test.cjs', False)
            source = source.replace('id => grants.add(id)', 'id => { cache.delete(id); grants.add(id); }')
            app.write_text(source, encoding='utf-8')
            self.check(workspace, 'test.cjs', False)
            source = source.replace('id => grants.delete(id)', 'id => { cache.delete(id); grants.delete(id); }')
            app.write_text(source, encoding='utf-8')
            self.check(workspace, 'test.cjs', True)


if __name__ == '__main__':
    unittest.main()
