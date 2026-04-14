#!/usr/bin/env python3
"""
Generate markdown mirrors for brycenwood.com
Creates a clean .md version of each HTML page for AI readability.
Modeled on: summit-wraps/lead-engine/generate_markdown_mirrors.py

Usage: python3 scripts/generate_markdown_mirrors.py
"""

import os
import re
from pathlib import Path

BUILD_DIR = Path(__file__).parent.parent / "build"

# Pages to skip (no mirror needed)
SKIP = {"playbook/thanks", "privacy", "terms"}


def strip_html(html: str) -> str:
    """Extract main content from HTML, strip tags, return clean text."""
    # Remove everything before </nav> (nav + head)
    nav_end = html.find("</nav>")
    if nav_end != -1:
        html = html[nav_end + 6:]

    # Remove footer and everything after
    footer_start = html.find("<footer")
    if footer_start != -1:
        html = html[:footer_start]

    # Remove sticky bar
    sticky_start = html.find('<div class="sticky-bar"')
    if sticky_start != -1:
        sticky_end = html.find("</div>", sticky_start)
        if sticky_end != -1:
            html = html[:sticky_start] + html[sticky_end + 6:]

    # Remove script tags
    html = re.sub(r"<script[\s\S]*?</script>", "", html)

    # Remove style tags
    html = re.sub(r"<style[\s\S]*?</style>", "", html)

    # Remove orb divs
    html = re.sub(r'<div class="orb[^"]*"></div>', "", html)

    # Remove breadcrumb
    html = re.sub(r'<div class="breadcrumb">[\s\S]*?</div>', "", html)

    # Remove iframe embeds (forms)
    html = re.sub(r"<iframe[\s\S]*?</iframe>", "", html)

    # Convert headings
    html = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n# \1\n", html, flags=re.DOTALL)
    html = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", html, flags=re.DOTALL)
    html = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", html, flags=re.DOTALL)
    html = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", html, flags=re.DOTALL)

    # Convert links
    html = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", html, flags=re.DOTALL)

    # Convert strong/em
    html = re.sub(r"<strong>(.*?)</strong>", r"**\1**", html, flags=re.DOTALL)
    html = re.sub(r"<em>(.*?)</em>", r"*\1*", html, flags=re.DOTALL)

    # Convert blockquotes
    html = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>", lambda m: "\n> " + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n", html, flags=re.DOTALL)

    # Convert list items
    html = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1", html, flags=re.DOTALL)

    # Convert code blocks
    html = re.sub(r"<pre[^>]*><code[^>]*>(.*?)</code></pre>", r"\n```\n\1\n```\n", html, flags=re.DOTALL)
    html = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", html, flags=re.DOTALL)

    # Convert paragraphs to double newlines
    html = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", html, flags=re.DOTALL)

    # Remove remaining HTML tags
    html = re.sub(r"<[^>]+>", "", html)

    # Decode HTML entities
    html = html.replace("&amp;", "&")
    html = html.replace("&mdash;", " -- ")
    html = html.replace("&ndash;", " - ")
    html = html.replace("&middot;", "·")
    html = html.replace("&rarr;", "→")
    html = html.replace("&copy;", "©")
    html = html.replace("&nbsp;", " ")
    html = html.replace("&#39;", "'")
    html = html.replace("&quot;", '"')
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")

    # Remove <span class="accent"> artifacts
    html = re.sub(r"\s*class=['\"][^'\"]*['\"]", "", html)

    # Clean up whitespace
    html = re.sub(r"\n{3,}", "\n\n", html)
    html = re.sub(r" {2,}", " ", html)

    return html.strip()


def extract_title(html: str) -> str:
    """Extract the <title> tag content."""
    match = re.search(r"<title>(.*?)</title>", html)
    return match.group(1) if match else "Untitled"


def extract_description(html: str) -> str:
    """Extract the meta description."""
    match = re.search(r'<meta name="description" content="(.*?)"', html)
    return match.group(1) if match else ""


def get_url_path(file_path: Path) -> str:
    """Convert file path to URL path."""
    rel = file_path.parent.relative_to(BUILD_DIR)
    if str(rel) == ".":
        return "/"
    return f"/{rel}/"


def generate_mirror(html_path: Path):
    """Generate a markdown mirror for a single HTML file."""
    rel_path = html_path.parent.relative_to(BUILD_DIR)
    rel_str = str(rel_path)

    # Skip excluded pages
    if rel_str in SKIP:
        return None

    html = html_path.read_text(encoding="utf-8")
    title = extract_title(html)
    description = extract_description(html)
    url_path = get_url_path(html_path)
    content = strip_html(html)

    md = f"""---
title: {title}
description: {description}
url: https://www.brycenwood.com{url_path}
last_updated: 2026-04-14
---

{content}
"""

    md_path = html_path.parent / "index.md"
    md_path.write_text(md, encoding="utf-8")
    return md_path


def main():
    html_files = sorted(BUILD_DIR.rglob("index.html"))
    generated = 0
    skipped = 0

    for html_path in html_files:
        result = generate_mirror(html_path)
        if result:
            rel = result.relative_to(BUILD_DIR)
            print(f"  Generated: {rel}")
            generated += 1
        else:
            rel = html_path.parent.relative_to(BUILD_DIR)
            print(f"  Skipped:   {rel}")
            skipped += 1

    print(f"\nDone. {generated} mirrors generated, {skipped} skipped.")


if __name__ == "__main__":
    main()
