#!/usr/bin/env python3
"""Scan apps/web/*.html for unresolved placeholders.

Default: print a warning list and exit 0. With --strict: exit 1 if any found.
"""
import argparse
import pathlib
import sys

MARKERS = ("[CONFIRM", "REPLACE_ME")
WEB = pathlib.Path(__file__).resolve().parent.parent / "apps" / "web"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any placeholder is found")
    args = ap.parse_args()
    found = []
    for path in sorted(WEB.glob("*.html")):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in MARKERS:
                if m in line:
                    found.append(f"{path.relative_to(WEB.parent.parent)}:{n}: {m}")
    for f in found:
        print("WARNING " + f)
    print(f"{len(found)} placeholder(s) found")
    return 1 if (found and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
