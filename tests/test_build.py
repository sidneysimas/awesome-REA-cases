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
        n = len(self.records)
        self.assertIn(f'**{n} 个案例与项目**', outputs['README.md'])
        self.assertIn(f'**{n} entries**', outputs['README.en.md'])
        self.assertIn('TH095', outputs['cases/touhou-reconstruction.md'])
        self.assertNotIn('HTML 阅读版', outputs['README.md'])
        self.assertFalse(any(p.endswith('.html') for p in outputs))
        self.assertFalse((ROOT / 'docs/index.html').exists())

    def test_english_readme_complete(self):
        outputs = build.render(self.records)
        self.assertIn('[English](README.en.md)', outputs['README.md'])
        self.assertIn('[中文（默认）](README.md)', outputs['README.en.md'])
        for r in self.records:
            self.assertIn(r['en']['title'], outputs['README.en.md'])
            self.assertEqual(outputs['README.en.md'].count(f"](cases/{r['id']}.md)"), 1)

    def test_all_records_in_main_directory(self):
        outputs = build.render(self.records)
        self.assertNotIn('LEADS.md', outputs)
        for r in self.records:
            self.assertEqual(outputs['README.md'].count(f"](cases/{r['id']}.md)"), 1)
            self.assertIn(r['title'], outputs[f"categories/{r['category']}.md"])
            if build.STATUS[r['status']]:
                self.assertIn(build.STATUS[r['status']], outputs[f"cases/{r['id']}.md"])
                self.assertIn(build.STATUS_EN[r['status']], outputs['README.en.md'])

    def test_invalid_status_rejected(self):
        self.records[0]['status'] = 'verified-without-evidence'
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_missing_translation_rejected(self):
        self.records[0]['en']['summary'] = ''
        with self.assertRaises(ValueError):
            build.validate(self.records)

    def test_no_top_n_truncation(self):
        extra = copy.deepcopy(self.records[0])
        extra['id'] = 'additional-test-case'
        extra['sources'] = [{'label': 'Test', 'url': 'https://example.com/additional'}]
        extra['en']['title'] = 'Additional test case'
        self.records.append(extra)
        build.validate(self.records)
        outputs = build.render(self.records)
        self.assertIn('cases/additional-test-case.md', outputs)
        self.assertIn('additional-test-case.md', outputs['README.md'])
        self.assertIn('additional-test-case.md', outputs['README.en.md'])

if __name__ == '__main__':
    unittest.main()
