#!/usr/bin/env python3
"""SEO and metadata validator for apps/web HTML pages.

Checks every .html file for:
- <title> present and within length bounds (10-60 chars)
- <meta name="description"> present and within length bounds (50-160 chars)
- <link rel="canonical"> present
- Exactly one <h1> per page
- OG tags (og:title, og:description, og:image, og:url) on index.html
- sitemap.xml exists
- robots.txt exists

Exits with code 1 if any error is found. Warnings do not fail the build.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HTML_DIR = Path("apps/web")
OG_TAGS = ["og:title", "og:description", "og:image", "og:url"]

errors: list[str] = []
warnings: list[str] = []


class MetaParser(HTMLParser):
    """Extracts meta/title/link/h1 data from an HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self.title: str | None = None
        self.description: str | None = None
        self.canonical: bool = False
        self.og: dict[str, str] = {}
        self.h1_count: int = 0
        self._in_title = False
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (d.get("name") or "").lower()
            prop = (d.get("property") or "").lower()
            content = d.get("content") or ""
            if name == "description":
                self.description = content
            elif prop in OG_TAGS:
                self.og[prop] = content
        elif tag == "link":
            rel = (d.get("rel") or "").lower()
            if rel == "canonical":
                self.canonical = True
        elif tag == "h1":
            self.h1_count += 1

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip()
            self._in_title = False
            self._buf.clear()


def check_page(page: Path) -> None:
    content = page.read_text(encoding="utf-8")
    name = str(page)

    p = MetaParser()
    p.feed(content)

    # --- Title ---
    if p.title is None:
        errors.append(f"{name}: missing <title>")
    else:
        ln = len(p.title)
        if ln < 10:
            errors.append(f"{name}: title too short ({ln} chars, min 10)")
        elif ln > 60:
            warnings.append(f"{name}: title may be truncated in SERPs ({ln} chars, max 60)")

    # --- Meta description ---
    if p.description is None:
        errors.append(f'{name}: missing <meta name="description">')
    else:
        ln = len(p.description)
        if ln < 50:
            errors.append(f"{name}: meta description too short ({ln} chars, min 50)")
        elif ln > 160:
            warnings.append(f"{name}: meta description may be truncated ({ln} chars, max 160)")

    # --- Canonical ---
    if not p.canonical:
        errors.append(f'{name}: missing <link rel="canonical">')

    # --- One h1 ---
    if p.h1_count == 0:
        errors.append(f"{name}: no <h1> found")
    elif p.h1_count > 1:
        errors.append(f"{name}: {p.h1_count} <h1> tags found (must be exactly 1)")

    # --- OG tags ---
    for tag in OG_TAGS:
        if tag not in p.og:
            if page.name == "index.html":
                errors.append(f"{name}: missing {tag} meta tag")
            else:
                warnings.append(f"{name}: missing {tag} meta tag (recommended)")


def main() -> None:
    pages = sorted(HTML_DIR.glob("**/*.html"))
    if not pages:
        errors.append(f"{HTML_DIR}: no HTML files found")

    for page in pages:
        check_page(page)

    # --- sitemap.xml ---
    if not (HTML_DIR / "sitemap.xml").exists():
        errors.append("apps/web/sitemap.xml: file missing")

    # --- robots.txt ---
    if not (HTML_DIR / "robots.txt").exists():
        errors.append("apps/web/robots.txt: file missing")

    # --- Report ---
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\nSEO check: {len(errors)} error(s), {len(warnings)} warning(s). Fix errors before merging.")
        sys.exit(1)

    print(f"\nSEO check passed. {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()
