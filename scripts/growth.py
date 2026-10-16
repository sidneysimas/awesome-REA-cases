"""Small, dependency-free daily collection snapshot and SVG chart renderer."""
import copy
from datetime import date, timedelta
from math import ceil
from xml.sax.saxutils import escape


def record_daily(history, total, day):
    """Record the current publication-day total; carry flat days forward."""
    result = copy.deepcopy(history)
    rows = result['daily']
    today = date.fromisoformat(day)
    if not rows or type(total) is not int or total < 0:
        raise ValueError('Daily history and nonnegative integer total required')
    previous = None
    for row in rows:
        current = date.fromisoformat(row['date'])
        if previous is not None and current <= previous:
            raise ValueError('Daily history must be ordered and unique')
        if type(row['total']) is not int or row['total'] < 0:
            raise ValueError('Invalid daily total')
        previous = current
    if today < previous:
        raise ValueError('Cannot rewrite a past publication day')
    while previous < today:
        previous += timedelta(days=1)
        rows.append({'date': previous.isoformat(), 'total': rows[-1]['total']})
    rows[-1]['total'] = total
    return result


def render_svg(history, language='en'):
    rows = history['daily']
    zh = language == 'zh'
    title = '累计案例' if zh else 'Case accumulation'
    subtitle = '每日累计 · 北京时间' if zh else 'Cumulative total · Beijing time'
    note = '按实际入库日期统计 · 最后一天为截至当前' if zh else 'By collection date · Latest day is partial · UTC+8'
    end = rows[-1]['date']
    maximum = max(row['total'] for row in rows)
    step = max(1, 10 ** max(0, len(str(maximum)) - 1))
    ceiling = max(step, ceil(maximum / step) * step)
    left, right, top, bottom = 54, 812, 82, 210
    span = max(1, len(rows) - 1)
    points = [(left + (right-left) * i/span,
               bottom - (bottom-top)*row['total']/ceiling) for i, row in enumerate(rows)]
    coords = ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="880" height="286" viewBox="0 0 880 286" role="img" aria-labelledby="title desc">',
           f'<title id="title">{title}: {rows[-1]["total"]} · {end}</title>',
           '<desc id="desc">' + escape('; '.join(f'{r["date"]}: {r["total"]}' for r in rows)) + '</desc>',
           '<defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#10b981" stop-opacity=".18"/><stop offset="1" stop-color="#10b981" stop-opacity="0"/></linearGradient></defs>',
           '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","WenQuanYi Zen Hei","Segoe UI","Noto Sans CJK SC",sans-serif;fill:#64748b;font-size:12px}.bg{fill:#fff}.heading{fill:#0f172a;font-size:17px;font-weight:600}.grid{stroke:#e2e8f0;stroke-dasharray:3 5}.value{fill:#059669;font-size:13px;font-weight:600}@media(prefers-color-scheme:dark){.bg{fill:#0d1117}text{fill:#8b949e}.heading{fill:#e6edf3}.grid{stroke:#30363d}.value{fill:#34d399}}</style>',
           '<rect class="bg" width="880" height="286" rx="12"/>',
           f'<text class="heading" x="28" y="32">{title}</text>',
           f'<text x="28" y="53">{subtitle}</text>',
           f'<text x="842" y="32" text-anchor="end">{rows[0]["date"]} — {end}</text>']
    for tick in range(4):
        value = ceiling * tick/3
        y = bottom - (bottom-top)*tick/3
        svg.append(f'<path class="grid" d="M {left} {y:.1f} H {right}"/><text x="42" y="{y+4:.1f}" text-anchor="end">{value:.0f}</text>')
    svg += [f'<path d="M {left} {bottom} L ' + ' L '.join(f'{x:.1f} {y:.1f}' for x,y in points) + f' L {points[-1][0]:.1f} {bottom} Z" fill="url(#area)"/>',
            f'<polyline points="{coords}" fill="none" stroke="#10b981" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>']
    # Limit labels on long histories, not the underlying daily observations.
    stride = max(1, ceil(len(rows)/7))
    for i, ((x,y), row) in enumerate(zip(points, rows)):
        if i % stride == 0 or i == len(rows)-1:
            svg += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#10b981"/>',
                    f'<text class="value" x="{x:.1f}" y="{y-12:.1f}" text-anchor="middle">{row["total"]}</text>',
                    f'<text x="{x:.1f}" y="234" text-anchor="middle">{row["date"][5:]}</text>']
    svg += [f'<text x="28" y="266" style="font-size:11px">{note}</text>', '</svg>\n']
    return '\n'.join(svg)
