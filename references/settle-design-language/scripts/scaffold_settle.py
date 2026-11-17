#!/usr/bin/env python3
"""Copy the Settle runtime into a project.

Usage:
    python3 scripts/scaffold_settle.py TARGET_DIR [--with-icons] [--with-starter] [--force]

Copies settle-tokens.css, settle.css and settle-motion.js into TARGET_DIR.
--with-icons    also copies the SVG icons into TARGET_DIR/icons/
--with-starter  also writes TARGET_DIR/settle-starter.html, a blank page wired to the three files
--force         overwrite files that already exist (otherwise they are skipped and reported)
"""

import argparse
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"
CORE = ["settle-tokens.css", "settle.css", "settle-motion.js"]

STARTER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Settle starter</title>
<link rel="stylesheet" href="settle-tokens.css">
<link rel="stylesheet" href="settle.css">
<script src="settle-motion.js"></script>
<style>
  .page { max-width: 1200px; margin: 0 auto; padding: var(--space-8); }
  .intro { max-width: 34em; margin-bottom: var(--space-7); }
  .intro p { color: var(--ink-muted); }
</style>
</head>
<body>
<main class="page">
  <section class="intro">
    <p class="st-type-caption">Getting started</p>
    <h1 class="st-type-headline">One idea per scene</h1>
    <p class="st-type-body">Replace this with the page's single message, then add one primary action.</p>
  </section>
  <button class="st-btn st-btn-primary" type="button">Continue</button>
</main>
<script>
  document.querySelectorAll('.st-btn').forEach(function (b) { window.Settle.press(b); });
</script>
</body>
</html>
"""


def copy(src: Path, dst: Path, force: bool, report: list) -> None:
    if dst.exists() and not force:
        report.append(("skipped (exists)", dst))
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    report.append(("copied", dst))


def main() -> int:
    parser = argparse.ArgumentParser(description="Copy the Settle runtime into a project.")
    parser.add_argument("target", help="Directory to copy the files into (created if missing)")
    parser.add_argument("--with-icons", action="store_true", help="Also copy SVG icons into TARGET/icons/")
    parser.add_argument("--with-starter", action="store_true", help="Also write TARGET/settle-starter.html")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    report = []

    for name in CORE:
        copy(ASSETS / name, target / name, args.force, report)

    if args.with_icons:
        for icon in sorted((ASSETS / "icons").glob("*.svg")):
            copy(icon, target / "icons" / icon.name, args.force, report)

    if args.with_starter:
        starter = target / "settle-starter.html"
        if starter.exists() and not args.force:
            report.append(("skipped (exists)", starter))
        else:
            starter.write_text(STARTER, encoding="utf-8")
            report.append(("written", starter))

    for status, path in report:
        print(f"{status:18} {path}")
    print("\nLoad order: settle-tokens.css, settle.css, then settle-motion.js (window.Settle).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
