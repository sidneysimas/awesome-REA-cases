#!/usr/bin/env python3
"""Validate canonical case data and generate the public collection (stdlib only)."""
import argparse
import datetime
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'games': '游戏与游戏保存',
    'hardware': '硬件与设备互通',
    'apps': '应用与客户端',
    'algorithms': '算法与功能重建',
}
LABELS = {'REA': 'REA', 'other-ai': '其他 AI 逆向', 'unknown': '未确认使用 REA'}


def validate(records):
    if not isinstance(records, list) or not records:
        raise ValueError('cases.json must contain a non-empty list')
    ids = set()
    source_sets = set()
    required = {'id', 'title', 'category', 'section', 'rea', 'summary',
                'description', 'sources', 'snapshot_date', 'metadata', 'en'}
    for r in records:
        if set(r) != required:
            raise ValueError(f"Invalid fields: {r.get('id')}")
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r['id']) or r['id'] in ids:
            raise ValueError('Invalid or duplicate ID')
        ids.add(r['id'])
        if r['category'] not in CATEGORIES or r['section'] not in ('cases', 'leads') or r['rea'] not in LABELS:
            raise ValueError(f"Invalid classification: {r['id']}")
        for key in ('title', 'summary', 'description'):
            if not isinstance(r[key], str) or not r[key].strip():
                raise ValueError(f'Missing {key}')
        if not isinstance(r['en'], dict) or set(r['en']) != {'title', 'summary'} or not all(isinstance(v, str) and v.strip() for v in r['en'].values()):
            raise ValueError('Every record requires an English title and summary')
        datetime.date.fromisoformat(r['snapshot_date'])
        if not isinstance(r['metadata'], list) or not all(isinstance(m, str) for m in r['metadata']):
            raise ValueError('Invalid metadata')
        if not isinstance(r['sources'], list) or not r['sources']:
            raise ValueError('Every case requires a source')
        urls = []
        for s in r['sources']:
            if set(s) != {'label', 'url'} or not s['label'].strip():
                raise ValueError('Invalid source fields')
            u = urlsplit(s['url'])
            if u.scheme != 'https' or not u.hostname or u.username or u.password:
                raise ValueError('Sources must be public HTTPS URLs without credentials')
            urls.append(s['url'])
        source_key = tuple(sorted(urls))
        if source_key in source_sets:
            raise ValueError('Duplicate source set; merge the records')
        source_sets.add(source_key)
    return records


def detail(r):
    lines = [f"# {r['title']}", '', f"分类：{CATEGORIES[r['category']]} · {LABELS[r['rea']]}",
             f"记录日期：{r['snapshot_date']}", '', r['description'], '']
    if r['metadata']:
        lines += r['metadata'] + ['']
    lines += ['## 来源', ''] + [f"- [{s['label']}]({s['url']})" for s in r['sources']]
    lines += ['', '[返回目录](../README.md)', '']
    return '\n'.join(lines)


def entry(r, prefix):
    return f"- [{r['title']}]({prefix}cases/{r['id']}.md) — {r['summary']} **[{LABELS[r['rea']]}]**"


def render(records):
    selected = [r for r in records if r['section'] == 'cases']
    leads = [r for r in records if r['section'] == 'leads']
    outputs = {f"cases/{r['id']}.md": detail(r) for r in records}
    readme = ['# Awesome REA Cases', '',
              '**中文（默认）** | [English](README.en.md)', '',
              '收集 REA 与其他 AI 辅助逆向的实际案例。每条讲清楚对象是什么、作者为什么逆向、做了什么，以及报告了什么结果。', '',
              '> 非 REA 官方项目。收录不代表工具或作者背书；不收集软件安装包、密钥、私人记录或未授权资产。', '',
              f'当前收录 **{len(selected)} 个案例**；另保留 **{len(leads)} 条待补证据、工具测试或未入选线索**。所有结果均据作者或项目记录整理，未由本项目独立复现。', '',
              '## 目录', '']
    for slug, title in CATEGORIES.items():
        count = sum(r['category'] == slug for r in selected)
        readme.append(f'- [{title}](categories/{slug}.md)（{count}）')
    readme += ['- [待跟进与未入选线索](LEADS.md)',
               '- [贡献指南](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)', '',
               '## 案例', '']
    for slug, title in CATEGORIES.items():
        group = [r for r in selected if r['category'] == slug]
        readme += [f'### {title}', ''] + [entry(r, '') for r in group] + ['']
        outputs[f'categories/{slug}.md'] = '\n'.join(
            [f'# {title}', '', '[返回主目录](../README.md)', ''] +
            [entry(r, '../') for r in group] + [''])
    readme += ['## 收录口径', '',
               '- REA、其他 AI 逆向与工具未确认分别标注，不把所有 AI 案例写成 REA 成果。',
               '- 不设 Top N、固定数量或时间窗口；有具体对象、过程和结果的优先，热度不作为门槛。',
               '- 自述结果注明边界，工具支持不等于完整产品重建；为 AI 工具做互通不等于 AI 完成全部逆向。',
               '- X 热度只保留带日期的抓取快照，不代表实时排名；发布日期不等于项目完成日期。',
               '- 同一项目的多条帖子合并；不同作者或不同目标不人为归并。',
               '- 新案例请修改 `data/cases.json` 并提交 PR，生成文件由脚本统一更新。', '',
               '## 许可与致谢', '',
               '本仓库原创摘要、数据整理与代码采用 [MIT License](LICENSE)。链接指向的第三方软件、文档、帖子和游戏资产仍遵循各自权利与许可证；本仓库许可不赋予其使用或分发权。', '',
               '组织方式参考 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)，具体调研见 [结构与维护调研](research/reference-structure.md)。', '']
    outputs['README.md'] = '\n'.join(readme)
    outputs['LEADS.md'] = '\n'.join(['# 待跟进与未入选线索', '',
        '这里保存已发现但尚不能作为完成案例展示的材料：证据不足、工具排障测试，或并非逆向的项目。它们不计入主目录案例数。', '',
        '[返回主目录](README.md)', ''] + [entry(r, '') for r in leads] + [''])
    categories_en = {'games': 'Games and preservation', 'hardware': 'Hardware and interoperability',
                     'apps': 'Applications and clients', 'algorithms': 'Algorithms and feature recovery'}
    labels_en = {'REA': 'REA', 'other-ai': 'Other AI-assisted work', 'unknown': 'REA use unconfirmed'}
    def english_entry(r):
        return f"- [{r['en']['title']}](cases/{r['id']}.md) — {r['en']['summary']} **[{labels_en[r['rea']]}]**"
    english = ['# Awesome REA Cases', '', '[中文（默认）](README.md) | **English**', '',
               'A curated collection of REA and AI-related reverse-engineering cases: the target, the author’s purpose, what they did, and the reported outcome.', '',
               '> Unofficial collection. Inclusion is not an endorsement. No proprietary binaries, keys, private records or unauthorized assets are distributed.', '',
               f'**{len(selected)} cases**, plus **{len(leads)} leads** with incomplete evidence, tool tests or exclusion notes. Results are attributed to authors and project records, not independently reproduced by this collection.', '',
               'The index below is in English. Linked case details, category pages, contribution and maintenance guides are currently in Chinese.', '',
               '## Contents', '']
    for slug, title in categories_en.items():
        count = sum(r['category'] == slug for r in selected)
        english.append(f'- [{title}](categories/{slug}.md) ({count})')
    english += ['- [Leads and excluded material](LEADS.md)',
                '- [Contributing](CONTRIBUTING.md) · [Maintenance](MAINTENANCE.md)', '', '## Cases', '']
    for slug, title in categories_en.items():
        english += [f'### {title}', ''] + [english_entry(r) for r in selected if r['category'] == slug] + ['']
    english += ['## Leads', ''] + [english_entry(r) for r in leads] + ['',
                '## Selection and evidence', '',
                '- No Top-N or fixed date limit. Prefer concrete targets, methods and results over popularity.',
                '- REA, other AI-assisted work and unconfirmed REA use are labeled separately. An AI-tool integration does not prove AI performed the investigation itself.',
                '- Static analysis, source-built fixtures, author reports and runtime checks have different scopes. A supported platform is not a complete product reconstruction.',
                '- X engagement is a dated snapshot, not a live ranking. Post date is not necessarily project completion date.',
                '- Merge multiple posts about the same project. Keep separate targets or independent projects distinct.',
                '- Edit data/cases.json and run python3 scripts/build.py. Generated files must stay synchronized.', '',
                '## License and acknowledgements', '',
                'Original summaries, curation data and code use the [MIT License](LICENSE). Linked software, documents, posts and game assets retain their own rights and licenses; this license does not authorize their redistribution.', '',
                'Organization inspired by [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills). See the [reference study](research/reference-structure.md).', '']
    outputs['README.en.md'] = '\n'.join(english)
    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Validate without writing; fail on stale outputs')
    args = parser.parse_args()
    records = validate(json.loads((ROOT / 'data/cases.json').read_text(encoding='utf-8')))
    outputs = render(records)
    stale = []
    for rel, content in outputs.items():
        path = ROOT / rel
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    expected_cases = {r['id'] + '.md' for r in records}
    orphaned = {p.name for p in (ROOT / 'cases').glob('*.md')} - expected_cases
    if stale or orphaned:
        raise SystemExit(f'Stale outputs: {stale}; orphaned case files: {sorted(orphaned)}')
    print(f'OK: {len(records)} records, {len(outputs)} generated files; check={args.check}')


if __name__ == '__main__':
    main()
