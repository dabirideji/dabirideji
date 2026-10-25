"""Refresh the auto-generated stats block in README.md.

Reads the public contribution calendar (which includes private contributions
when "show private contributions" is on), so it needs no token. If GitHub is
unreachable or the page layout changes, the previous numbers are kept and only
the refresh date moves - the run never fails because of a parse problem.
"""

from __future__ import annotations

import datetime as dt
import html
import os
import re
import sys
import urllib.request
from pathlib import Path

USER = os.environ.get("PROFILE_USER", "dabirideji")
FIRST_YEAR = int(os.environ.get("PROFILE_FIRST_YEAR", "2022"))
README = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"
TIMEOUT_SECONDS = 30

_CELL_RE = re.compile(r'<td[^>]*?data-date="(\d{4}-\d{2}-\d{2})"[^>]*?id="([^"]+)"')
_TIP_RE = re.compile(r'<tool-tip[^>]*?for="([^"]+)"[^>]*>([^<]*)</tool-tip>')
_COUNT_RE = re.compile(r"^([\d,]+) contributions?\b")


def fetch_year(year: int) -> dict[str, int]:
    url = f"https://github.com/users/{USER}/contributions?from={year}-01-01&to={year}-12-31"
    req = urllib.request.Request(url, headers={"User-Agent": f"{USER}-profile-refresh"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        page = resp.read().decode("utf-8")

    date_by_cell = {cell_id: date for date, cell_id in _CELL_RE.findall(page)}
    days: dict[str, int] = {}
    for cell_id, text in _TIP_RE.findall(page):
        date = date_by_cell.get(cell_id)
        if not date:
            continue
        match = _COUNT_RE.match(html.unescape(text).strip())
        days[date] = int(match.group(1).replace(",", "")) if match else 0
    if not days:
        raise ValueError(f"no calendar cells parsed for {year}")
    return days


def compute_stats(days: dict[str, int], today: dt.date) -> dict[str, int]:
    ordered = sorted((dt.date.fromisoformat(d), n) for d, n in days.items())
    ordered = [(d, n) for d, n in ordered if d <= today]

    longest = run = 0
    for _, count in ordered:
        run = run + 1 if count > 0 else 0
        longest = max(longest, run)

    year_ago = today - dt.timedelta(days=365)
    last_year = [(d, n) for d, n in ordered if d > year_ago]
    return {
        "total": sum(n for _, n in ordered),
        "last_year": sum(n for _, n in last_year),
        "active_days": sum(1 for _, n in last_year if n > 0),
        "longest": longest,
    }


def render(stats: dict[str, int] | None, previous: str, today: dt.date) -> str:
    refreshed = f"<sub>Auto-refreshed {today.isoformat()} (UTC) by a GitHub Action in this repo.</sub>"
    if stats is None:
        # Keep the last good numbers; only the refresh line changes.
        kept, replaced = re.subn(r"<sub>Auto-refreshed.*?</sub>", refreshed, previous, flags=re.S)
        return kept if replaced else f"{previous.rstrip()}\n\n{refreshed}\n"

    return "\n".join([
        "",
        "| Contributions since 2022 | Last 12 months | Active days (12 mo) | Longest streak |",
        "|:---:|:---:|:---:|:---:|",
        f"| **{stats['total']:,}** | **{stats['last_year']:,}** | **{stats['active_days']}** | **{stats['longest']} days** |",
        "",
        refreshed,
        "",
    ])


def main() -> int:
    today = dt.datetime.now(dt.timezone.utc).date()
    readme = README.read_text(encoding="utf-8")
    try:
        head, rest = readme.split(START, 1)
        previous, tail = rest.split(END, 1)
    except ValueError:
        print(f"README is missing the {START} / {END} markers", file=sys.stderr)
        return 1

    stats = None
    try:
        days: dict[str, int] = {}
        for year in range(FIRST_YEAR, today.year + 1):
            days.update(fetch_year(year))
        stats = compute_stats(days, today)
        print(f"stats: {stats}")
    except Exception as exc:  # network or layout change: degrade, never fail the run
        print(f"stats unavailable, keeping previous numbers: {exc!r}", file=sys.stderr)

    updated = f"{head}{START}{render(stats, previous, today)}{END}{tail}"
    if updated != readme:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print("README.md updated")
    else:
        print("README.md unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
