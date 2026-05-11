#!/usr/bin/env python3
"""
Generate branded images for brycenwood.com using Chrome headless.

Takes a list of image jobs (template + data) and renders each as a PNG
using the site's brand DNA (dark bg, lime accent, grid pattern, Outfit type).

Outputs go to build/assets/images/generated/.

Usage: python3 scripts/generate_images.py
"""

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

SITE_DIR = Path(__file__).parent.parent
OUT_DIR = SITE_DIR / "build" / "assets" / "images" / "generated"
TEMPLATES_DIR = Path(__file__).parent / "image-templates"
BASE_CSS = (TEMPLATES_DIR / "_base.css").read_text()

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# ---------------------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------------------

def tpl_og(data):
    """1200x630 social/OG card. Big H1 + subhead + 4 stats."""
    stats_html = "".join(
        f'<div><div class="stat-val">{s["val"]}</div>'
        f'<div class="stat-label">{s["label"]}</div></div>'
        for s in data.get("stats", [])
    )
    accent = data.get("accent", "")
    h1 = data["h1"]
    if accent:
        h1 = h1.replace(accent, f'<span class="accent">{accent}</span>')
    return f"""
<style>
body {{ width: 1200px; height: 630px; }}
.content {{ padding: 60px 80px; }}
.eyebrow {{ font-size: 14px; margin-bottom: 20px; }}
h1 {{
  font-weight: 900; font-size: 72px; line-height: 1.05;
  letter-spacing: -2px; color: var(--text); max-width: 900px;
}}
.sub {{
  font-size: 22px; color: var(--text-dim);
  margin-top: 20px; max-width: 700px; line-height: 1.5;
}}
.stats {{
  display: flex; gap: 44px; margin-top: 40px;
  padding-top: 24px; border-top: 1px solid var(--border);
}}
.stat-val {{ font-family: var(--mono); font-size: 24px; font-weight: 700; color: var(--lime); }}
.stat-label {{
  font-family: var(--mono); font-size: 10px; font-weight: 500;
  color: var(--text-muted); letter-spacing: 1.5px;
  text-transform: uppercase; margin-top: 4px;
}}
.brand {{ font-size: 14px; }}
</style>
<div class="orb-1"></div><div class="orb-2"></div>
<div class="content">
  <div class="eyebrow">{data.get('eyebrow', '')}</div>
  <h1>{h1}</h1>
  <div class="sub">{data.get('sub', '')}</div>
  {('<div class="stats">' + stats_html + '</div>') if stats_html else ''}
</div>
<div class="brand">BRYCENWOOD.COM</div>
"""


def tpl_industry_banner(data):
    """1600x600 wide industry page banner. Eyebrow + H1 + tag chips."""
    chips_html = "".join(f'<span class="chip">{c}</span>' for c in data.get("chips", []))
    accent = data.get("accent", "")
    h1 = data["h1"]
    if accent:
        h1 = h1.replace(accent, f'<span class="accent">{accent}</span>')
    return f"""
<style>
body {{ width: 1600px; height: 600px; }}
.content {{ padding: 80px 100px; }}
.eyebrow {{ font-size: 13px; margin-bottom: 24px; }}
h1 {{
  font-weight: 900; font-size: 76px; line-height: 1.05;
  letter-spacing: -2.5px; color: var(--text); max-width: 1100px;
}}
.sub {{
  font-size: 22px; color: var(--text-dim);
  margin-top: 24px; max-width: 800px; line-height: 1.5;
}}
.chips {{ margin-top: 36px; max-width: 1100px; }}
.brand {{ font-size: 14px; }}
.brand-mark {{ font-size: 14px; }}
</style>
<div class="orb-1"></div><div class="orb-2"></div><div class="orb-3"></div>
<div class="brand-mark">BRYCEN&nbsp;WOOD</div>
<div class="content">
  <div class="eyebrow">{data.get('eyebrow', 'Industry Solutions')}</div>
  <h1>{h1}</h1>
  <div class="sub">{data.get('sub', '')}</div>
  {('<div class="chips">' + chips_html + '</div>') if chips_html else ''}
</div>
<div class="brand">BRYCENWOOD.COM</div>
"""


def tpl_offer_card(data):
    """800x600 square card for homepage offer grid. Tag + title + desc + stat."""
    return f"""
<style>
body {{ width: 800px; height: 600px; }}
.content {{ padding: 60px 56px; justify-content: space-between; }}
.top {{ display: flex; flex-direction: column; }}
.tag {{
  font-family: var(--mono); font-size: 11px; font-weight: 600;
  letter-spacing: 2.5px; text-transform: uppercase;
  color: var(--lime); margin-bottom: 28px;
}}
.title {{
  font-weight: 900; font-size: 46px; line-height: 1.1;
  letter-spacing: -1.5px; color: var(--text); max-width: 700px;
}}
.desc {{
  font-size: 17px; color: var(--text-dim);
  margin-top: 18px; line-height: 1.55; max-width: 660px;
}}
.bottom {{
  display: flex; align-items: flex-end; justify-content: space-between;
  border-top: 1px solid var(--border); padding-top: 24px; margin-top: 24px;
}}
.metric {{ font-family: var(--mono); font-size: 28px; font-weight: 700; color: var(--lime); }}
.metric-label {{
  font-family: var(--mono); font-size: 10px; font-weight: 500;
  color: var(--text-muted); letter-spacing: 1.5px;
  text-transform: uppercase; margin-top: 4px;
}}
.arrow {{ font-family: var(--mono); font-size: 13px; color: var(--lime); letter-spacing: 2px; }}
.brand {{ display: none; }}
</style>
<div class="orb-1" style="width:400px;height:400px;top:-180px;right:-100px;left:auto;opacity:0.08"></div>
<div class="content">
  <div class="top">
    <div class="tag">{data['tag']}</div>
    <div class="title">{data['title']}</div>
    <div class="desc">{data['desc']}</div>
  </div>
  <div class="bottom">
    <div>
      <div class="metric">{data['metric']}</div>
      <div class="metric-label">{data['metric_label']}</div>
    </div>
    <div class="arrow">{data.get('cta', 'LEARN MORE →')}</div>
  </div>
</div>
"""


def tpl_guide_cover(data):
    """1200x630 guide cover. Category + title + accent line."""
    return f"""
<style>
body {{ width: 1200px; height: 630px; }}
.content {{ padding: 70px 90px; justify-content: center; }}
.category {{
  font-family: var(--mono); font-size: 13px; font-weight: 600;
  letter-spacing: 4px; text-transform: uppercase;
  color: var(--lime); margin-bottom: 28px;
}}
.title {{
  font-weight: 900; font-size: 78px; line-height: 1.05;
  letter-spacing: -2.5px; color: var(--text); max-width: 1000px;
}}
.accent-line {{ width: 120px; height: 3px; margin: 32px 0 0; }}
.brand {{ font-size: 14px; }}
.brand-mark {{ font-size: 14px; }}
</style>
<div class="orb-1"></div><div class="orb-2"></div>
<div class="brand-mark">BRYCEN&nbsp;WOOD</div>
<div class="content">
  <div class="category">{data.get('category', 'GUIDE')}</div>
  <div class="title">{data['title']}</div>
  <div class="accent-line"></div>
</div>
<div class="brand">BRYCENWOOD.COM</div>
"""


TEMPLATES = {
    "og": (tpl_og, 1200, 630),
    "industry-banner": (tpl_industry_banner, 1600, 600),
    "offer-card": (tpl_offer_card, 800, 600),
    "guide-cover": (tpl_guide_cover, 1200, 630),
}


# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------

def render(job):
    """Render one image. job = dict with 'template', 'data', 'output'."""
    template_name = job["template"]
    tpl_fn, width, height = TEMPLATES[template_name]
    body = tpl_fn(job["data"])

    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>{BASE_CSS}</style></head>
<body>{body}</body></html>"""

    out_path = OUT_DIR / job["output"]
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, dir=str(OUT_DIR)
    ) as f:
        f.write(html)
        tmp_html = f.name

    try:
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                f"--window-size={width},{height}",
                f"--screenshot={out_path}",
                "--default-background-color=00000000",
                f"file://{tmp_html}",
            ],
            check=True,
            capture_output=True,
            timeout=30,
        )
        print(f"  ✓ {job['output']} ({width}x{height})")
    finally:
        Path(tmp_html).unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# IMAGE JOBS
# ---------------------------------------------------------------------------

JOBS = [
    # ===== HOMEPAGE: NEW OG / SOCIAL IMAGE =====
    {
        "template": "og",
        "output": "og-home.png",
        "data": {
            "eyebrow": "Most owners use AI to rewrite emails",
            "h1": "Run your business with AI. Not just rewrite emails.",
            "accent": "Not just rewrite emails.",
            "sub": "Custom business operating systems built with Claude Code. 6x revenue, zero new hires, zero lines of code.",
            "stats": [
                {"val": "$300K+", "label": "Revenue"},
                {"val": "80+", "label": "Systems"},
                {"val": "10", "label": "APIs"},
                {"val": "0", "label": "Code Written"},
            ],
        },
    },

    # ===== HOMEPAGE: OFFER CARDS (replacement for the "What I Build" grid) =====
    {
        "template": "offer-card",
        "output": "card-custom-build.png",
        "data": {
            "tag": "SERVICE",
            "title": "Custom Business Operating System",
            "desc": "60-min interview, custom plan in 72 hours, 2-week build, full handoff. Your entire business — automated.",
            "metric": "$3.5K",
            "metric_label": "Founder Rate",
            "cta": "LEARN MORE →",
        },
    },
    {
        "template": "offer-card",
        "output": "card-summit-story.png",
        "data": {
            "tag": "CASE STUDY",
            "title": "$52K → $300K in 18 Months",
            "desc": "Vehicle wrap shop scaled 6x with 80+ AI systems. Zero developers. Zero agencies. Zero new hires.",
            "metric": "6×",
            "metric_label": "Revenue Growth",
            "cta": "READ THE STORY →",
        },
    },
    {
        "template": "offer-card",
        "output": "card-community.png",
        "data": {
            "tag": "COMMUNITY",
            "title": "Business On Autopilot",
            "desc": "The same systems I'm using to scale Summit Wraps. Modules, live builds, exact prompts. Founding rate locked for life.",
            "metric": "$97/mo",
            "metric_label": "Founding Rate",
            "cta": "JOIN FOUNDING →",
        },
    },

    # ===== INDUSTRY HERO BANNERS (1 per industry page) =====
    {
        "template": "industry-banner",
        "output": "banner-service-business.png",
        "data": {
            "eyebrow": "Industry Solutions",
            "h1": "Service Business Automation",
            "accent": "Automation",
            "sub": "Trucks, techs, and teams in the field. Automated from lead to invoice.",
            "chips": ["HVAC", "Roofing", "Plumbing", "Electrical", "Landscaping", "Pest Control", "Painting"],
        },
    },
    {
        "template": "industry-banner",
        "output": "banner-hvac.png",
        "data": {
            "eyebrow": "Industry Solutions",
            "h1": "HVAC Automation",
            "accent": "Automation",
            "sub": "Capture every call. Schedule every job. Earn every review. Without lifting a finger.",
            "chips": ["Lead Capture", "Dispatch", "Maintenance Plans", "Review Generation", "Marketing Automation"],
        },
    },
    {
        "template": "industry-banner",
        "output": "banner-roofing.png",
        "data": {
            "eyebrow": "Industry Solutions",
            "h1": "Roofing Automation",
            "accent": "Automation",
            "sub": "Storm response, insurance follow-up, estimate sequences. The plays that turn $30M roofers into $30M roofers.",
            "chips": ["Storm Response", "Insurance Claims", "Estimate Follow-Up", "Review Generation"],
        },
    },
    {
        "template": "industry-banner",
        "output": "banner-plumbing.png",
        "data": {
            "eyebrow": "Industry Solutions",
            "h1": "Plumbing Automation",
            "accent": "Automation",
            "sub": "Route emergency leads in seconds. Remind for maintenance. Dispatch on autopilot.",
            "chips": ["Emergency Routing", "Dispatch", "Maintenance Plans", "Review Generation"],
        },
    },
    {
        "template": "industry-banner",
        "output": "banner-ecommerce.png",
        "data": {
            "eyebrow": "Industry Solutions",
            "h1": "Run your store with AI. Not just abandoned cart emails.",
            "accent": "Not just abandoned cart emails.",
            "sub": "Cart recovery, email flows, inventory automation, review collection. Custom-built. Not a Klaviyo template.",
            "chips": ["Shopify", "WooCommerce", "BigCommerce", "DTC", "Subscription", "Apparel", "Beauty"],
        },
    },

    # ===== GUIDE COVERS (top 4 most-trafficked guides) =====
    {
        "template": "guide-cover",
        "output": "cover-llms-txt.png",
        "data": {
            "category": "GUIDE · AI SEO",
            "title": "The llms.txt file that made ChatGPT recommend my business",
        },
    },
    {
        "template": "guide-cover",
        "output": "cover-markdown-mirrors.png",
        "data": {
            "category": "GUIDE · AI SEO",
            "title": "Markdown mirrors: how to make your site readable by ChatGPT",
        },
    },
    {
        "template": "guide-cover",
        "output": "cover-ai-seo-playbook.png",
        "data": {
            "category": "GUIDE · AI SEO",
            "title": "The 3-file AI SEO playbook",
        },
    },
    {
        "template": "guide-cover",
        "output": "cover-business-os.png",
        "data": {
            "category": "GUIDE · OPERATIONS",
            "title": "What a business operating system actually is",
        },
    },
]


def main():
    print(f"Generating {len(JOBS)} images...")
    print(f"Output: {OUT_DIR}")
    print()
    for job in JOBS:
        render(job)
    print()
    print(f"Done. {len(JOBS)} images in {OUT_DIR}")


if __name__ == "__main__":
    main()
