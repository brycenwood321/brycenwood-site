#!/usr/bin/env python3
"""
Render SVG illustrations to PNG using Chrome headless.
Drops PNGs in build/assets/images/illustrations/.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "image-templates"))
from illustrations import ILLUSTRATIONS  # noqa: E402

SITE_DIR = Path(__file__).parent.parent
OUT_DIR = SITE_DIR / "build" / "assets" / "images" / "illustrations"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Render at 2x for crisp display: SVG viewBox 800x500 → render 1600x1000
WIDTH = 1600
HEIGHT = 1000


def render(name, svg_fn):
    svg = svg_fn()
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  body {{ margin:0; padding:0; background:#050508;
         font-family:'Outfit', sans-serif;
         width:{WIDTH}px; height:{HEIGHT}px; overflow:hidden; }}
  svg {{ width:{WIDTH}px; height:{HEIGHT}px; display:block; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;600;800;900&display=swap">
</head><body>{svg}</body></html>"""

    out = OUT_DIR / f"{name}.png"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, dir=str(OUT_DIR)) as f:
        f.write(html)
        tmp = f.name

    try:
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--window-size={WIDTH},{HEIGHT}",
            f"--screenshot={out}",
            f"file://{tmp}",
        ], check=True, capture_output=True, timeout=30)
        print(f"  ✓ {out.name} ({WIDTH}x{HEIGHT})")
    finally:
        Path(tmp).unlink(missing_ok=True)


def main():
    print(f"Rendering {len(ILLUSTRATIONS)} illustrations to {OUT_DIR}")
    for name, fn in ILLUSTRATIONS.items():
        render(name, fn)
    print("Done.")


if __name__ == "__main__":
    main()
