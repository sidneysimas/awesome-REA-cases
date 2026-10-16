"""Daily accumulation counts use publication days, never source-post dates."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GrowthTests(unittest.TestCase):
    def test_chart_adds_three_precollection_zero_days_without_changing_history(self):
        import copy
        import re
        spec = importlib.util.spec_from_file_location('growth', ROOT / 'scripts/growth.py')
        growth = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(growth)
        history = {'daily': [
            {'date': '2026-10-12', 'total': 81},
            {'date': '2026-10-13', 'total': 128}]}
        before = copy.deepcopy(history)
        svg = growth.render_svg(history)
        for day in ('09', '10', '11'):
            self.assertIn(f'2026-10-{day}: 0', svg)
        self.assertIn('pre-collection baseline', svg)
        self.assertEqual(history, before)
        self.assertIn('收录前零基线', growth.render_svg(history, 'zh'))
        points = re.search(r'<polyline points="([^"]+)"', svg).group(1).split()
        self.assertEqual(len(points), 5)
        self.assertTrue(all(point.split(',')[1] == '210.0' for point in points[:3]))

    def test_build_records_growth_and_check_is_read_only(self):
        import json
        import shutil
        import subprocess
        import sys
        import tempfile
        from datetime import datetime
        from zoneinfo import ZoneInfo
        day = datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / 'scripts', root / 'scripts')
            (root / 'data').mkdir()
            records = json.loads((ROOT / 'data/cases.json').read_text())[:2]
            (root / 'data/cases.json').write_text(json.dumps(records))
            history = root / 'data/case-growth.json'
            history.write_text(json.dumps({'timezone': 'Asia/Shanghai', 'daily': [
                {'date': day, 'total': 1}]}))
            subprocess.run([sys.executable, 'scripts/build.py'], cwd=root, check=True, capture_output=True)
            self.assertEqual(json.loads(history.read_text())['daily'][-1]['total'], 2)
            before = history.read_bytes()
            for language in ('en', 'zh'):
                self.assertTrue((root / f'assets/case-growth.{language}.svg').is_file())
            subprocess.run([sys.executable, 'scripts/build.py', '--check'], cwd=root, check=True, capture_output=True)
            self.assertEqual(before, history.read_bytes())

    def test_record_daily_total_fills_gaps_and_updates_only_latest_day(self):
        path = ROOT / 'scripts/growth.py'
        self.assertTrue(path.exists(), 'Missing daily growth recorder and SVG renderer')
        spec = importlib.util.spec_from_file_location('growth', path)
        growth = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(growth)
        history = {'timezone': 'Asia/Shanghai', 'daily': [
            {'date': '2026-10-12', 'total': 81},
            {'date': '2026-10-13', 'total': 128}]}
        result = growth.record_daily(history, 145, '2026-10-15')
        self.assertEqual(result['daily'], history['daily'] + [
            {'date': '2026-10-14', 'total': 128},
            {'date': '2026-10-15', 'total': 145}])
        self.assertEqual(history['daily'][-1]['total'], 128)
        result = growth.record_daily(result, 160, '2026-10-15')
        self.assertEqual(len(result['daily']), 4)
        self.assertEqual(result['daily'][-1]['total'], 160)
        svg = growth.render_svg(result, 'en')
        self.assertIn('<svg', svg)
        self.assertIn('160', svg)
        self.assertIn('2026-10-15', svg)
        self.assertIn('Latest day is partial', svg)
        self.assertNotIn('<script', svg)
        self.assertIn('累计案例', growth.render_svg(result, 'zh'))
        with self.assertRaises(ValueError):
            growth.record_daily(result, 100, '2026-10-13')


if __name__ == '__main__':
    unittest.main()
