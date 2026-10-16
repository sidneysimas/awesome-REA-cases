import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EditorialReadmeTests(unittest.TestCase):
    def test_build_preserves_hand_edited_readmes_and_generates_full_indexes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'scripts').mkdir()
            (root / 'data').mkdir()
            shutil.copy(ROOT / 'scripts/build.py', root / 'scripts/build.py')
            shutil.copy(ROOT / 'data/cases.json', root / 'data/cases.json')
            editorial = {'README.md': '# Editor picks\n\nChosen by the editor.\n',
                         'README.zh-CN.md': '# 人工精选\n\n由编辑选择。\n',
                         'README.en.md': '# Legacy entry\n\n[English](README.md) | [简体中文](README.zh-CN.md)\n'}
            for name, text in editorial.items():
                (root / name).write_text(text)
            subprocess.run(['python3', str(root / 'scripts/build.py')], check=True, capture_output=True)
            records = json.loads((root / 'data/cases.json').read_text())
            for name in ('INDEX.md', 'INDEX.en.md'):
                index = (root / name).read_text()
                case_dir = 'cases/en' if name == 'INDEX.en.md' else 'cases'
                for record in records:
                    self.assertIn(f"]({case_dir}/{record['id']}.md)", index)
            subprocess.run(['python3', str(root / 'scripts/build.py'), '--check'], check=True, capture_output=True)
            for name, text in editorial.items():
                self.assertEqual((root / name).read_text(), text, 'build must never overwrite any static README')


if __name__ == '__main__':
    unittest.main()
