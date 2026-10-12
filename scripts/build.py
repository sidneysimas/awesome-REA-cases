#!/usr/bin/env python3
"""Validate canonical case data and generate the public collection (stdlib only)."""
import argparse
import datetime
import html
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
                'description', 'sources', 'snapshot_date', 'metadata'}
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
              'A curated collection of real-world REA and AI-assisted reverse-engineering cases.', '',
              '收集 REA 与其他 AI 辅助逆向的实际案例。每条讲清楚对象是什么、作者为什么逆向、做了什么，以及报告了什么结果。', '',
              '> 非 REA 官方项目。收录不代表工具或作者背书；不收集软件安装包、密钥、私人记录或未授权资产。', '',
              f'当前收录 **{len(selected)} 个案例**；另保留 **{len(leads)} 条待补证据、工具测试或未入选线索**。所有结果均据作者或项目记录整理，未由本项目独立复现。', '',
              '## 目录', '']
    for slug, title in CATEGORIES.items():
        count = sum(r['category'] == slug for r in selected)
        readme.append(f'- [{title}](categories/{slug}.md)（{count}）')
    readme += ['- [待跟进与未入选线索](LEADS.md)',
               '- [HTML 阅读版](docs/index.html)（下载后用浏览器打开）',
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
               '- 有具体对象、过程和结果的优先；自述结果注明边界，工具支持不等于完整产品重建。',
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
    esc = html.escape
    sections = []
    for section, title in [('cases', '案例'), ('leads', '待跟进与未入选线索')]:
        cards = []
        for r in records:
            if r['section'] != section:
                continue
            links = ' '.join(f'<a href="{esc(s["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{esc(s["label"])} ↗</a>' for s in r['sources'])
            metadata = ''.join(f'<div class="meta">{esc(m)}</div>' for m in r['metadata'])
            cards.append(f'<article id="{r["id"]}" data-section="{section}" data-category="{r["category"]}"><h3>{esc(r["title"])}</h3><div class="meta">{esc(CATEGORIES[r["category"]])} · {esc(LABELS[r["rea"]])}</div>{metadata}<p>{esc(r["description"])}</p><div class="links">{links}</div></article>')
        note = '<p class="meta">以下不计入主目录案例数，不作为已完成成果展示。</p>' if section == 'leads' else ''
        sections.append(f'<section data-section="{section}"><h2>{title}</h2>{note}{"".join(cards)}</section>')
    css = '''*{box-sizing:border-box}body{margin:0;background:#f7f7f2;color:#283128;font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;line-height:1.9}main{max-width:900px;margin:auto;padding:44px 30px}h1{font-size:34px;line-height:1.35}h2{font-size:23px;padding-bottom:12px;border-bottom:2px solid #586e4c}h3{font-size:21px;margin:0 0 8px}article{padding:26px 0;border-bottom:1px solid #d4dccb;scroll-margin-top:12px}article p{font-size:16px}.meta,footer{font-size:12px;color:#727e68}a{color:#385a37;text-underline-offset:4px}.links{display:flex;gap:8px 20px;flex-wrap:wrap}.links a{min-height:44px;display:inline-flex;align-items:center}nav{display:flex;gap:8px;flex-wrap:wrap}button{background:transparent;border:1px solid #b5c2ab;padding:9px 16px;font:inherit;color:#385a37;min-height:44px;cursor:pointer}button.active{background:#385a37;color:white}[hidden]{display:none!important}a:focus-visible,button:focus-visible{outline:3px solid #9ba980;outline-offset:3px}@media(max-width:500px){main{padding:25px 18px}h1{font-size:29px}h3{font-size:19px}}@media print{nav{display:none}body{background:white}main{padding:0}article{break-inside:avoid}article p,.meta,.links,footer{font-size:12pt}}'''
    js = '''const buttons=[...document.querySelectorAll('[data-filter]')];buttons.forEach(b=>b.onclick=()=>{const v=b.dataset.filter;buttons.forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b))});document.querySelectorAll('section[data-section]').forEach(s=>s.hidden=v!=='all'&&s.dataset.section!==v)});document.getElementById('print').onclick=()=>window.print();'''
    outputs['docs/index.html'] = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Awesome REA Cases</title><style>{css}</style></head><body><main><header><h1>Awesome REA Cases</h1><p>REA 与 AI 辅助逆向的实际案例。背景、作者做法和报告结果。</p><p class="meta">{len(selected)} 个案例 · {len(leads)} 条补充线索 · 数据快照：{max(r['snapshot_date'] for r in records)}<br>据作者与项目记录整理，未独立复现；第三方内容保留原始来源。</p><nav><button class="active" data-filter="all" aria-pressed="true">全部</button><button data-filter="cases" aria-pressed="false">案例</button><button data-filter="leads" aria-pressed="false">补充线索</button><button id="print">打印 / 存为 PDF</button></nav></header>{''.join(sections)}<footer>本阅读版由 data/cases.json 自动生成。<a href="https://github.com/songshikang0111/awesome-REA-cases">GitHub 项目与贡献指南</a></footer></main><script>{js}</script></body></html>\n'''
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
