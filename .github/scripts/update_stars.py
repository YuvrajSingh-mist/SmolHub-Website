#!/usr/bin/env python3
"""Scan all markdown files with github_url frontmatter, fetch real star counts
from the GitHub API, and update the `stars:` field in-place."""

import os
import re
import sys
import time
import urllib.request
import urllib.error
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
COLLECTIONS = ["_models", "_rl", "_projects", "_datasets"]
GH_TOKEN = os.environ.get("GH_TOKEN", "")

_star_cache: dict[str, int] = {}


def gh_stars(owner_repo: str) -> int | None:
    if owner_repo in _star_cache:
        return _star_cache[owner_repo]
    url = f"https://api.github.com/repos/{owner_repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if GH_TOKEN:
        req.add_header("Authorization", f"Bearer {GH_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            stars = data.get("stargazers_count")
            _star_cache[owner_repo] = stars
            return stars
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} for {owner_repo}", file=sys.stderr)
    except Exception as e:
        print(f"  Error fetching {owner_repo}: {e}", file=sys.stderr)
    return None


def parse_github_url(url: str) -> str | None:
    """Extract owner/repo from any github.com URL."""
    m = re.search(r"github\.com/([^/]+/[^/?\s#]+)", url)
    if not m:
        return None
    return m.group(1).rstrip("/")


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    # Must have frontmatter
    if not text.startswith("---"):
        return False

    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        return False

    fm = fm_match.group(1)
    url_match = re.search(r'^github_url:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not url_match:
        return False

    owner_repo = parse_github_url(url_match.group(1).strip())
    if not owner_repo:
        return False

    stars = gh_stars(owner_repo)
    if stars is None:
        return False

    time.sleep(0.1)  # stay well within rate limits

    stars_line = f"stars: {stars}"

    if re.search(r'^stars:\s*\S+', fm, re.MULTILINE):
        new_fm = re.sub(r'^stars:\s*\S+', stars_line, fm, flags=re.MULTILINE)
    else:
        new_fm = fm.rstrip() + f"\n{stars_line}"

    if new_fm == fm:
        return False  # nothing changed

    new_text = text.replace(fm_match.group(1), new_fm, 1)
    path.write_text(new_text, encoding="utf-8")
    print(f"  {path.relative_to(REPO_ROOT)}: {stars} stars ({owner_repo})")
    return True


changed = 0
for collection in COLLECTIONS:
    collection_path = REPO_ROOT / collection
    if not collection_path.is_dir():
        continue
    for md in sorted(collection_path.glob("*.md")):
        if update_file(md):
            changed += 1

print(f"\nDone — updated {changed} file(s).")
