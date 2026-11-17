#!/usr/bin/env python3
"""Check Settle colour pairs against WCAG 2 contrast floors, in every theme.

Usage:
    python3 scripts/check_contrast.py [TOKENS_JSON] [--pair FG BG MIN]...

With no TOKENS_JSON, reads assets/tokens.json from this skill.
Default checks: text tokens 4.5:1 on all four surfaces; signal 4.5:1 on all surfaces;
line-control 3:1 on all surfaces; on-fill-primary on fill-primary and on-signal on signal 4.5:1;
status colours 4.5:1 on their -soft backgrounds.
Add your own pairs with --pair, e.g. --pair ink stone 4.5
Exits 1 if any pair fails, so it can gate a change to the palette.
"""

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SURFACES = ["surface", "surface-raised", "surface-sunken", "surface-overlay"]
DEFAULT_PAIRS = (
    [(fg, bg, 4.5) for fg in ["ink", "ink-muted", "ink-subtle", "signal"] for bg in SURFACES]
    + [("line-control", bg, 3.0) for bg in SURFACES]
    + [("on-fill-primary", "fill-primary", 4.5), ("on-signal", "signal", 4.5)]
    + [(s, s + "-soft", 4.5) for s in ["positive", "caution", "critical", "signal"]]
    + [("ink", "stone", 4.5), ("ink-muted", "stone", 4.5)]
)


def resolve(tokens, name, theme, depth=0):
    if depth > 16:
        raise ValueError(f"alias chain too deep at {name}")
    tok = tokens.get(name)
    if tok is None:
        raise KeyError(f"unknown colour token: {name}")
    v = tok["value"]
    if isinstance(v, dict):
        first = next(iter(v.values()))
        v = v.get(theme, first)
    m = re.fullmatch(r"\{(.+)\}", v)
    return resolve(tokens, m.group(1), theme, depth + 1) if m else v


def to_rgb(value):
    h = value.strip().lstrip("#")
    if re.fullmatch(r"[0-9a-fA-F]{3,4}", h):
        h = "".join(c * 2 for c in h[:3])
    if re.fullmatch(r"[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", h):
        return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    raise ValueError(f"only hex colours can be checked here, got {value!r}")


def luminance(rgb):
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(to_rgb(a)), luminance(to_rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    parser = argparse.ArgumentParser(description="Check Settle colour contrast in every theme.")
    parser.add_argument("tokens", nargs="?", default=str(SKILL_DIR / "assets" / "tokens.json"))
    parser.add_argument("--pair", nargs=3, action="append", metavar=("FG", "BG", "MIN"), help="Extra pair to check")
    args = parser.parse_args()

    data = json.loads(Path(args.tokens).read_text(encoding="utf-8"))
    tokens = {t["name"]: t for t in data["color"]["tokens"]}
    themes = [t["id"] for t in data["color"]["themes"]]
    pairs = list(DEFAULT_PAIRS) + [(f, b, float(m)) for f, b, m in (args.pair or [])]

    failures = 0
    for theme in themes:
        print(f"== {theme}")
        for fg, bg, minimum in pairs:
            if fg not in tokens or bg not in tokens:
                print(f"  skip  {fg} on {bg} (token missing)")
                continue
            try:
                r = ratio(resolve(tokens, fg, theme), resolve(tokens, bg, theme))
            except ValueError as e:
                print(f"  skip  {fg} on {bg} ({e})")
                continue
            ok = r >= minimum
            failures += 0 if ok else 1
            print(f"  {'pass' if ok else 'FAIL'}  {r:5.2f}:1  {fg} on {bg} (needs {minimum}:1)")
    print(f"\n{failures} failing pair(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
