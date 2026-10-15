import copy
import importlib.util
import json
import re
import subprocess
import tempfile
import shutil
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

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
        self.assertIn(f'**{n} 个案例与项目**', outputs['INDEX.md'])
        self.assertIn(f'**{n} entries**', outputs['INDEX.en.md'])
        self.assertIn('TH095', outputs['cases/touhou-reconstruction.md'])
        self.assertNotIn('HTML 阅读版', outputs['INDEX.md'])
        self.assertFalse(any(p.endswith('.html') for p in outputs))
        self.assertFalse((ROOT / 'docs/index.html').exists())

    def test_english_index_complete(self):
        outputs = build.render(self.records)
        self.assertIn('[English index](INDEX.en.md)', outputs['INDEX.md'])
        self.assertIn('[中文总目录](INDEX.md)', outputs['INDEX.en.md'])
        for r in self.records:
            self.assertIn(r['en']['title'], outputs['INDEX.en.md'])
            self.assertEqual(outputs['INDEX.en.md'].count(f"](cases/en/{r['id']}.md)"), 1)

    def test_english_details_and_navigation(self):
        outputs = build.render(self.records)
        self.assertEqual({p for p in outputs if p.startswith('cases/en/')},
                         {f"cases/en/{r['id']}.md" for r in self.records})
        for r in self.records:
            with self.subTest(case=r['id']):
                english = outputs[f"cases/en/{r['id']}.md"]
                chinese = outputs[f"cases/{r['id']}.md"]
                self.assertIn(r['en']['description'], english)
                self.assertIn(f"# {r['en']['title']}\n", english)
                self.assertIn(f"Record date: {r['snapshot_date']}", english)
                self.assertIn(f"Category: {build.CATEGORIES_EN[r['category']]} · {build.LABELS_EN[r['rea']]}", english)
                if build.STATUS_EN[r['status']]:
                    self.assertIn(f"Stage: {build.STATUS_EN[r['status']]}", english)
                self.assertIn(f"[中文](../{r['id']}.md)", english)
                self.assertIn(f"[English](en/{r['id']}.md)", chinese)
                self.assertIn('[Back to editor picks](../../README.en.md)', english)
                self.assertIn('[Full index](../../INDEX.en.md)', english)
                self.assertIn(f"](../../categories/en/{r['category']}.md)", english)
                for note in r['en']['metadata']:
                    self.assertIn(note, english)
                for label, source in zip(r['en']['source_labels'], r['sources']):
                    self.assertIn(f"[{label}]({source['url']})", english)
                self.assertEqual(re.findall(r'^- \[[^]]+\]\((https://[^)]+)\)$', english, re.M),
                                 [source['url'] for source in r['sources']])
                self.assertIn(f"](../../cases/en/{r['id']}.md)",
                              outputs[f"categories/en/{r['category']}.md"])
        for slug in build.CATEGORIES:
            self.assertIn(f"](categories/en/{slug}.md)", outputs['INDEX.en.md'])
            self.assertIn(f"](../{slug}.md)", outputs[f'categories/en/{slug}.md'])
            self.assertIn(f"](en/{slug}.md)", outputs[f'categories/{slug}.md'])

    def test_incomplete_english_rejected(self):
        for key, value in [('description', ''), ('description', None),
                           ('description', '   '), ('metadata', []), ('metadata', ['']),
                           ('metadata', None), ('metadata', [1, 2]),
                           ('metadata', ['a', 'b', 'extra']),
                           ('source_labels', []), ('source_labels', ['']),
                           ('source_labels', ['a', 'extra']), ('source_labels', [1]),
                           ('source_labels', 'Source')]:
            records = copy.deepcopy(self.records)
            records[0]['en'][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                build.validate(records)
        records = copy.deepcopy(self.records)
        records[0]['en']['urls'] = []
        with self.assertRaises(ValueError):
            build.validate(records)
        for key in ('description', 'metadata', 'source_labels'):
            records = copy.deepcopy(self.records)
            records[0]['en'].pop(key)
            with self.subTest(missing=key), self.assertRaises(ValueError):
                build.validate(records)

    def test_english_homepage_links_to_english_reading_path(self):
        text = (ROOT / 'README.en.md').read_text()
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith('cases/'):
                self.assertTrue(target.startswith('cases/en/'), target)
        for slug in build.CATEGORIES:
            self.assertIn(f'](categories/en/{slug}.md)', text)

    def test_all_local_markdown_links_and_anchors(self):
        outputs = build.render(self.records)
        documents = {str(p.relative_to(ROOT)): p.read_text() for p in ROOT.rglob('*.md')
                     if '.git' not in p.parts}
        documents.update(outputs)
        def anchors(text):
            counts = {}
            result = set()
            for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
                heading = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', heading)
                slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
                count = counts.get(slug, 0)
                counts[slug] = count + 1
                result.add(slug + (f'-{count}' if count else ''))
            return result
        for rel, text in documents.items():
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                path = (ROOT / rel).parent / unquote(url.path) if url.path else ROOT / rel
                path = path.resolve()
                with self.subTest(document=rel, target=target):
                    self.assertTrue(path.is_relative_to(ROOT))
                    key = str(path.relative_to(ROOT))
                    self.assertTrue(key in documents or path.is_file(), target)
                    if url.fragment and key in documents:
                        self.assertIn(unquote(url.fragment), anchors(documents[key]))

    def test_check_detects_stale_and_orphaned_cases_in_both_languages(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for directory in ('scripts', 'data'):
                (root / directory).mkdir()
            shutil.copy(ROOT / 'scripts/build.py', root / 'scripts/build.py')
            shutil.copy(ROOT / 'data/cases.json', root / 'data/cases.json')
            command = ['python3', str(root / 'scripts/build.py')]
            subprocess.run(command, check=True, capture_output=True)
            for language in ('', 'en/'):
                case = root / 'cases' / language / f"{self.records[0]['id']}.md"
                original = case.read_text()
                case.write_text(original + '\nStale\n')
                result = subprocess.run(command + ['--check'], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(str(case.relative_to(root)), result.stderr)
                case.write_text(original)
                orphan = root / 'cases' / language / 'orphan.md'
                orphan.write_text('# Orphan\n')
                result = subprocess.run(command + ['--check'], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(str(orphan.relative_to(root)), result.stderr)
                orphan.unlink()

    def test_all_records_in_main_directory(self):
        outputs = build.render(self.records)
        self.assertNotIn('LEADS.md', outputs)
        for r in self.records:
            self.assertEqual(outputs['INDEX.md'].count(f"](cases/{r['id']}.md)"), 1)
            self.assertIn(r['title'], outputs[f"categories/{r['category']}.md"])
            if build.STATUS[r['status']]:
                self.assertIn(build.STATUS[r['status']], outputs[f"cases/{r['id']}.md"])
                self.assertIn(build.STATUS_EN[r['status']], outputs['INDEX.en.md'])

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
        extra['en']['source_labels'] = ['Test']
        self.records.append(extra)
        build.validate(self.records)
        outputs = build.render(self.records)
        self.assertIn('cases/additional-test-case.md', outputs)
        self.assertIn('additional-test-case.md', outputs['INDEX.md'])
        self.assertIn('additional-test-case.md', outputs['INDEX.en.md'])

if __name__ == '__main__':
    unittest.main()
