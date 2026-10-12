import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build', ROOT / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.records = json.loads((ROOT / 'data/cases.json').read_text())

    def test_valid_data(self):
        self.assertEqual(build.validate(self.records), self.records)

    def test_duplicate_id_rejected(self):
        self.records.append(copy.deepcopy(self.records[0]))
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_private_url_rejected(self):
        self.records[0]['sources'][0]['url'] = 'https://user:secret@example.com/a'
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_missing_source_rejected(self):
        self.records[0]['sources'] = []
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_bad_classification_rejected(self):
        self.records[0]['rea'] = 'assumed'
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_render_counts_and_boundaries(self):
        outputs = build.render(self.records)
        page = outputs['docs/index.html']
        self.assertEqual(page.count('<article '), len(self.records))
        n = sum(r['section'] == 'cases' for r in self.records)
        self.assertIn(f'**{n} 个案例**', outputs['README.md'])
        self.assertIn('TH095', outputs['cases/touhou-reconstruction.md'])
        self.assertNotIn('可以延伸', page)

    def test_html_escapes_content(self):
        self.records[0]['description'] = '<script>alert(1)</script>'
        page = build.render(self.records)['docs/index.html']
        self.assertIn('&lt;script&gt;', page)
        self.assertNotIn('<script>alert(1)</script>', page)

if __name__ == '__main__':
    unittest.main()
