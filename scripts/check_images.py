#!/usr/bin/env python3
"""Image standards validator for apps/web HTML pages.

Checks every .html file for:
- Every <img> has a non-empty alt attribute
- Every <img> has width and height attributes (CLS prevention)
- Every locally-referenced <img src> file exists on disk
- The og:image file referenced in each page exists on disk

Exits with code 1 if any error is found. Warnings do not fail the build.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HTML_DIR = Path("apps/web")

errors: list[str] = []
warnings: list[str] = []


class ImageParser(HTMLParser):
    """Collects img tag attributes and og:image content from an HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self.imgs: list[dict[str, str | None]] = []
        self.og_image: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if tag == "img":
            self.imgs.append(d)
        elif tag == "meta":
            prop = (d.get("property") or "").lower()
            if prop == "og:image":
                self.og_image = d.get("content")


def check_page(page: Path) -> None:
    content = page.read_text(encoding="utf-8")
    name = str(page)

    p = ImageParser()
    p.feed(content)

    for attrs in p.imgs:
        src = attrs.get("src") or ""
        snippet = f'src="{src}"'

        # alt attribute
        if "alt" not in attrs:
            errors.append(f"{name}: <img {snippet}> missing alt attribute")
        elif (attrs["alt"] or "").strip() == "":
            warnings.append(f"{name}: <img {snippet}> has empty alt (ok if decorative)")

        # width and height (CLS)
        if "width" not in attrs or "height" not in attrs:
            warnings.append(f"{name}: <img {snippet}> missing width/height (causes layout shift)")

        # local src exists
        if src and not src.startswith(("http://", "https://", "data:", "//")):
            local = HTML_DIR / src.lstrip("/")
            if not local.exists():
                errors.append(f"{name}: referenced image not found on disk: {src}")

    # og:image file
    if p.og_image:
        path_match = re.search(r"https?://[^/]+(/[^\s\"']+)", p.og_image)
        if path_match:
            og_local = HTML_DIR / path_match.group(1).lstrip("/")
            if not og_local.exists():
                warnings.append(
                    f"{name}: og:image not found on disk ({p.og_image}) — add before going live"
                )


def main() -> None:
    pages = sorted(HTML_DIR.glob("**/*.html"))
    if not pages:
        errors.append(f"{HTML_DIR}: no HTML files found")
        sys.exit(1)

    for page in pages:
        check_page(page)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\nImage check: {len(errors)} error(s), {len(warnings)} warning(s). Fix errors before merging.")
        sys.exit(1)

    print(f"\nImage check passed. {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()
