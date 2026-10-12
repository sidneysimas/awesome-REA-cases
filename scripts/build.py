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
STATUS = {'case': '', 'unverified': '待验证', 'in-progress': '进行中', 'analysis-test': '分析测试', 'related-project': '相关项目'}
STATUS_EN = {'case': '', 'unverified': 'Needs verification', 'in-progress': 'In progress', 'analysis-test': 'Analysis test', 'related-project': 'Related project'}


def validate(records):
    if not isinstance(records, list) or not records:
        raise ValueError('cases.json must contain a non-empty list')
    ids = set()
    source_sets = set()
    required = {'id', 'title', 'category', 'status', 'rea', 'summary',
                'description', 'sources', 'snapshot_date', 'metadata', 'en'}
    for r in records:
        if set(r) != required:
            raise ValueError(f"Invalid fields: {r.get('id')}")
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r['id']) or r['id'] in ids:
            raise ValueError('Invalid or duplicate ID')
        ids.add(r['id'])
        if r['category'] not in CATEGORIES or r['status'] not in STATUS or r['rea'] not in LABELS:
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
    if STATUS[r['status']]:
        lines.insert(4, f"阶段：{STATUS[r['status']]}")
    if r['metadata']:
        lines += r['metadata'] + ['']
    lines += ['## 来源', ''] + [f"- [{s['label']}]({s['url']})" for s in r['sources']]
    lines += ['', '[返回目录](../README.md)', '']
    return '\n'.join(lines)


def entry(r, prefix):
    stage = f" · {STATUS[r['status']]}" if STATUS[r['status']] else ''
    return f"- [{r['title']}]({prefix}cases/{r['id']}.md) — {r['summary']} **[{LABELS[r['rea']]}{stage}]**"


def render(records):
    outputs = {f"cases/{r['id']}.md": detail(r) for r in records}
    readme = ['# 全部案例与项目', '',
              '[精选首页](README.md) | [English index](INDEX.en.md)', '',
              '**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**', '',
              '**每天 6 次定时追踪 REA 与 AI 逆向公开案例，自动筛选、去重并更新合集。**', '',
              '收集 REA 与其他 AI 逆向的案例和项目，覆盖游戏保存、硬件互通、应用重建与算法研究。每条说明作者在研究什么、为什么逆向、具体做了什么，并链接原帖、代码或验证记录。', '',
              '[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向分析工具。本集合不局限于 REA，也收录其他 AI 辅助逆向和为 AI 工具实现互通的项目。', '',
              f'当前收录 **{len(records)} 个案例与项目**，按用途分类，不设 Top N 或热度门槛。', '',
              '## 目录', '']
    for slug, title in CATEGORIES.items():
        count = sum(r['category'] == slug for r in records)
        readme.append(f'- [{title}](categories/{slug}.md)（{count}）')
    readme += ['- [贡献案例](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)', '',
               '工具标注：`REA` / `其他 AI 逆向` / `未确认使用 REA`。阶段标注：`待验证` / `进行中` / `分析测试` / `相关项目`；有标注的也列在主目录，但不等同于已完成成果。', '',
               '## 案例与项目', '']
    for slug, title in CATEGORIES.items():
        group = [r for r in records if r['category'] == slug]
        readme += [f'### {title}', ''] + [entry(r, '') for r in group] + ['']
        outputs[f'categories/{slug}.md'] = '\n'.join(
            [f'# {title}', '', '[返回主目录](../README.md)', ''] +
            [entry(r, '../') for r in group] + [''])
    readme += ['## 贡献与收录', '',
               '欢迎提交新案例、补充验证或纠正描述。修改 `data/cases.json` 后运行 `python3 scripts/build.py`，再提交 PR；详见[贡献指南](CONTRIBUTING.md)。', '',
               '优先原作者、具体目标与操作记录。同一项目合并来源；作者自述、静态分析和实际运行分别说明。X 热度保留抓取日期，不作为效果证明。', '',
               '## 说明与许可', '',
               '非 REA 官方项目。结果据作者和项目记录整理，未由本集合独立复现。仅整理原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。', '',
               '本仓库原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利与许可证。研究、复现或再利用前，请确认你拥有相应授权。', '',
               '组织方式参考 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)。[收集范围](research/collection-scope.md) · [结构调研](research/reference-structure.md)', '']
    outputs['INDEX.md'] = '\n'.join(readme)
    categories_en = {'games': 'Games and preservation', 'hardware': 'Hardware and interoperability',
                     'apps': 'Applications and clients', 'algorithms': 'Algorithms and feature recovery'}
    labels_en = {'REA': 'REA', 'other-ai': 'Other AI-assisted work', 'unknown': 'REA use unconfirmed'}
    def english_entry(r):
        stage = f" · {STATUS_EN[r['status']]}" if STATUS_EN[r['status']] else ''
        return f"- [{r['en']['title']}](cases/{r['id']}.md) — {r['en']['summary']} **[{labels_en[r['rea']]}{stage}]**"
    english = ['# All cases and projects', '', '[Editor picks](README.en.md) | [中文总目录](INDEX.md)', '',
               '**Explore software and hardware with AI: rebuild features, bridge protocols, and modernize legacy systems.**', '',
               '**Tracks public REA and AI reverse-engineering cases six times daily, automatically screening, deduplicating, and updating the collection.**', '',
               'A collection of REA and AI reverse-engineering cases and projects, covering game preservation, hardware interoperability, app reconstruction, and algorithm research. Each entry explains the target, the author’s purpose and approach, and links to original posts, code, or verification records.', '',
               '[REA](https://github.com/morluto/rea) (Reverse Engineer Anything) lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also includes work with other AI tools and interoperability projects built for AI agents.', '',
               f'**{len(records)} entries**, organized by use case, without a Top-N or popularity threshold.', '',
               'The index is in English; linked case details, category pages, and contribution/maintenance guides are currently in Chinese.', '',
               '## Contents', '']
    for slug, title in categories_en.items():
        count = sum(r['category'] == slug for r in records)
        english.append(f'- [{title}](categories/{slug}.md) ({count})')
    english += ['- [Contribute a case](CONTRIBUTING.md) · [Maintenance](MAINTENANCE.md)', '',
                'Tool labels distinguish REA, other AI work, and unconfirmed REA use. Stage labels—Needs verification, In progress, Analysis test, and Related project—keep all entries discoverable without presenting them as completed results.', '',
                '## Cases and projects', '']
    for slug, title in categories_en.items():
        english += [f'### {title}', ''] + [english_entry(r) for r in records if r['category'] == slug] + ['']
    english += ['## Contributing and selection', '',
                'Submit new cases, additional verification, or corrections. Edit data/cases.json, run python3 scripts/build.py, and open a PR. See [Contributing](CONTRIBUTING.md).', '',
                'Prefer original authors, concrete targets and recorded work. Merge multiple sources for one project. Distinguish author reports, static analysis and actual execution. X engagement is a dated snapshot, not proof of effectiveness.', '',
                '## Scope and license', '',
                'Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys or private material are distributed.', '',
                'Original summaries, curation data and code use the [MIT License](LICENSE). Linked content retains its own rights and licenses. Ensure you have the relevant authorization before investigating, reproducing or reusing it.', '',
                'Organization inspired by [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills). [Collection scope](research/collection-scope.md) · [Reference study](research/reference-structure.md)', '']
    outputs['INDEX.en.md'] = '\n'.join(english)
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
