#!/usr/bin/env python3
"""build_offer_pages.py - the BrycenAI offer pages, generated from the ruled price sheet.

Writes build/pricing/, build/cohort/, build/community/, build/services/retainer/ (index.html each).
Prices come from _data/marketing/personal_brand/offers/price_sheet_2026-10-19.md (ruled 2026-10-19).
Pay buttons read pay_links.json; an empty link falls back to /contact/, so nothing ever points at a
dead Stripe page. The cohort pay button only appears once BOTH the cohort link and cohort_start are set.
Nav, footer and page scripts are lifted from build/contact/index.html so every page stays in step.
Rerun after any price or link change, then scripts/generate_markdown_mirrors.py.
"""
import json, os, re, html

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(SITE, "build")
DOMAIN = "https://www.brycenwood.com"
LINKS = json.load(open(os.path.join(SITE, "pay_links.json")))

contact = open(os.path.join(BUILD, "contact", "index.html")).read()
NAV = re.search(r"<!-- NAV -->.*?</nav>", contact, re.S).group(0)
FOOTER = re.search(r"<!-- FOOTER -->.*?</footer>", contact, re.S).group(0)
SCRIPT = re.search(r"<!-- JAVASCRIPT -->.*?</script>", contact, re.S).group(0)
GTAG = re.search(r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>", contact, re.S).group(0)
CONTACT_FORM = "m8xHvt2SLJXszIYACZDK"


def pay(key, label, fallback="Book a call"):
    url = LINKS.get(key) or ""
    if url:
        return f'<a href="{url}" class="btn-primary" style="display:block;text-align:center" data-pay="{key}">{label}</a>'
    return f'<a href="/contact/" class="btn-primary" style="display:block;text-align:center">{fallback}</a>'


def page(path, title, desc, crumb, body, faq=None):
    url = f"{DOMAIN}/{path}/"
    graph = [{"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
        {"@type": "ListItem", "position": 2, "name": crumb}]}]
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1)
    faq_html = ""
    if faq:
        items = "\n".join(f'''    <div class="faq-item">
      <div class="faq-question">{html.escape(q)}<span class="faq-toggle">+</span></div>
      <div class="faq-answer"><p>{html.escape(a)}</p></div>
    </div>''' for q, a in faq)
        faq_html = f'''<div class="divider"></div>
<div class="section-dark">
  <div class="section-header reveal"><h2>Common <span class="accent">Questions</span></h2></div>
  <div class="faq-list reveal">
{items}
  </div>
</div>'''
    t, d = html.escape(title), html.escape(desc)
    out = f'''<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;600;800;900&display=swap">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/images/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<script type="application/ld+json">
{ld}
</script>
<link rel="stylesheet" href="/assets/css/global.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
.ladder-note{{color:var(--text-dim);font-size:14px;line-height:1.6;margin-top:12px}}
.price-card .price-period{{min-height:22px}}
.week-row{{display:grid;grid-template-columns:72px 1fr;gap:16px;padding:16px 0;border-bottom:1px solid rgba(255,255,255,0.08)}}
.week-row .wk{{font-family:'JetBrains Mono',monospace;color:var(--lime);font-weight:700}}
.week-row p{{color:var(--text-dim);margin-top:4px}}
.plain-list{{padding:0 20px 0 40px;max-width:760px;margin:0 auto}}
.plain-list li{{margin:8px 0;color:var(--text-dim);line-height:1.6}}
.week-row{{margin:0 20px}}
</style>
</head>
<body>
<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="orb orb-3"></div>
{NAV}
<div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><span>{html.escape(crumb)}</span></div>
{body}
{faq_html}
{FOOTER}
{SCRIPT}
<script>
document.querySelectorAll('.faq-question').forEach(q=>{{q.addEventListener('click',()=>{{const i=q.closest('.faq-item');const o=i.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(x=>x.classList.remove('open'));if(!o)i.classList.add('open');}});}});
document.querySelectorAll('[data-pay]').forEach(a=>a.addEventListener('click',()=>{{if(typeof gtag==='function')gtag('event','pay_click',{{offer:a.dataset.pay}})}}));
</script>
</body>
</html>
'''
    os.makedirs(os.path.join(BUILD, path), exist_ok=True)
    open(os.path.join(BUILD, path, "index.html"), "w").write(out)
    return os.path.join(path, "index.html")


# ---------- /pricing/ ----------
pricing_body = f'''<section class="page-hero">
  <p class="hero-eyebrow">Pricing</p>
  <h1>Start with a <span class="accent">diagnosis.</span></h1>
  <p class="hero-sub">I run a vehicle wrap shop and a meal prep company on Claude Code, and I have never written a line of code. This is how I set the same thing up for your business, in the order I'd do it.</p>
</section>
<div class="divider"></div>
<div class="section-dark">
  <div class="pricing-grid">
    <div class="price-card featured reveal">
      <div class="price-label">Diagnosis</div>
      <div class="price-amount">$1,500</div>
      <div class="price-period">One 90-minute session, written plan in 5 business days</div>
      <ul class="price-features">
        <li>I read your business with you over a screen share: your CRM, books, inbox, spreadsheets</li>
        <li>A written plan: what to automate, in what order, what each piece saves or earns</li>
        <li>What each piece would cost to have built</li>
        <li>One 30-minute follow-up call to walk the plan</li>
        <li>The full $1,500 comes off a build you buy within 30 days</li>
      </ul>
      {pay("diagnosis", "Book a diagnosis")}
      <p class="ladder-note">After you pay, I text you within 24 hours to pick a time.</p>
    </div>
    <div class="price-card reveal">
      <div class="price-label">Setup Day</div>
      <div class="price-amount">$2,500</div>
      <div class="price-period">A half day on your own machine</div>
      <ul class="price-features">
        <li>Claude Code installed and set up the way I run mine</li>
        <li>I interview you and write your business into files and memory it reads every session</li>
        <li>One working system before I leave: a daily brief, a follow-up drafter or a quote drafter</li>
        <li>A "how to come back" card, plus a 30-minute check-in at day 7</li>
        <li>If it cannot be installed in the first hour (locked work laptop), we stop and you pay a quarter</li>
      </ul>
      {pay("setup_day", "Book a Setup Day")}
      <p class="ladder-note">Four hours, on your own machine.</p>
    </div>
    <div class="price-card reveal">
      <div class="price-label">5-week cohort</div>
      <div class="price-amount">$1,500</div>
      <div class="price-period">Run your business on Claude Code</div>
      <ul class="price-features">
        <li>One 90-minute evening a week for 5 weeks, plus a Setup Day in week 1</li>
        <li>8 to 12 business owners, in person in Utah County with a Zoom seat</li>
        <li>You leave with your own system running, shown to the room in week 5</li>
        <li>Full refund before week 1 ends</li>
      </ul>
      <a href="/cohort/" class="btn-secondary" style="display:block;text-align:center">See the cohort</a>
    </div>
  </div>
</div>
<div class="divider"></div>
<div class="section-raised">
  <div class="section-header reveal"><h2>Builds and <span class="accent">upkeep</span></h2></div>
  <div class="container-narrow reveal">
    <ul class="plain-list">
      <li><strong>Build.</strong> One named system built, tested and handed over: a quote page, a follow-up engine, an ordering system, a check-in page. Fixed price, quoted after a diagnosis, because no two businesses need the same thing. Half up front, half at hand-off, 14 days of fixes after.</li>
      <li><strong>Retainer, after a build only.</strong> I keep what I built running and improve it: monitoring, fixes, small changes, a monthly review. $1,500 a month, 3-month minimum, then 30 days notice either way.</li>
      <li><strong>Claude Code Night.</strong> A free Monday night in Utah for owners who already run Claude Code. <a href="/community/" style="color:var(--lime)">Details here.</a></li>
    </ul>
  </div>
</div>'''
pricing_faq = [
    ("Why start with a diagnosis instead of a build?", "Because most owners ask for the wrong first system. In 90 minutes I can see where your money actually leaks, and the plan tells you what to build first. If you then have me build it within 30 days, the diagnosis is free."),
    ("Do I own what you build?", "Yes. Everything runs in your own accounts: your CRM, your hosting, your Claude login. Nothing is locked to me."),
    ("Do I need to know how to code?", "No. I don't. Everything I run, I built by talking to Claude Code in plain English, and that is how you will run it too."),
    ("What if I want changes after a build?", "You get 14 days of fixes after hand-off. After that you can run it yourself, hire me for a change, or take the retainer."),
]
written = [page("pricing", "Pricing | Brycen Wood", "Start with a $1,500 diagnosis, credited against a build. Setup Day $2,500. A 5-week cohort at $1,500. Builds quoted after a diagnosis.", "Pricing", pricing_body, pricing_faq)]

# ---------- /cohort/ ----------
start = LINKS.get("cohort_start") or ""
cohort_pay = (pay("cohort", f"Take a seat, starts {html.escape(start)}") if (LINKS.get("cohort") and start)
              else '<a href="#seat" class="btn-primary" style="display:inline-block">Hold me a seat</a>')
when = f"Starts {html.escape(start)}." if start else "First cohort starts in December or January. Dates go to the people on the list first."
cohort_body = f'''<section class="page-hero">
  <p class="hero-eyebrow">5-week cohort, $1,500</p>
  <h1>Run your business on <span class="accent">Claude Code.</span></h1>
  <p class="hero-sub">Five weeks, one evening a week, 8 to 12 business owners. You leave with your business written into files your AI reads every day, and one system of your own running. {when}</p>
  <div class="btn-group" style="margin-top:24px">{cohort_pay}</div>
</section>
<div class="divider"></div>
<div class="section-dark">
  <div class="section-header reveal"><h2>The five <span class="accent">weeks</span></h2></div>
  <div class="container-narrow reveal">
    <div class="week-row"><div class="wk">WEEK 1</div><div><strong>Build the house.</strong><p>Plus your Setup Day that week. Claude Code installed, your folders, your standing rules. You leave with it working on your own machine.</p></div></div>
    <div class="week-row"><div class="wk">WEEK 2</div><div><strong>The interview and the files.</strong><p>Your business written down in files Claude reads every session, so you stop explaining yourself every time. Memory working.</p></div></div>
    <div class="week-row"><div class="wk">WEEK 3</div><div><strong>The plan.</strong><p>A ranked list of what to automate. You pick one and write its scope. A 20-minute one-on-one with me this week.</p></div></div>
    <div class="week-row"><div class="wk">WEEK 4</div><div><strong>Build your first system.</strong><p>A daily brief, a follow-up drafter or a quote drafter, running on your real data.</p></div></div>
    <div class="week-row"><div class="wk">WEEK 5</div><div><strong>Make it stick, and show it.</strong><p>The habits for coming back, one scheduled job, and a 3-minute demo to the room.</p></div></div>
  </div>
</div>
<div class="divider"></div>
<div class="section-raised">
  <div class="section-header reveal"><h2>Who it is <span class="accent">for</span></h2></div>
  <div class="container-narrow reveal">
    <ul class="plain-list">
      <li><strong>For:</strong> business owners who want to run their own system, not hand it off.</li>
      <li><strong>Not for:</strong> people who want it built for them. That is a <a href="/pricing/" style="color:var(--lime)">build</a>, not a cohort.</li>
      <li><strong>Where:</strong> in person in Utah County, with a Zoom seat. Sessions run in the evening, Mountain time, so US time zones only.</li>
      <li><strong>The guarantee:</strong> come to all five sessions and the Setup Day, and if you leave without a working system, you get your money back. Change your mind before week 1 ends and you get a full refund, no questions.</li>
      <li><strong>Included:</strong> a cohort group chat for the five weeks and a 20-minute one-on-one in week 3.</li>
      <li><strong>After:</strong> graduates keep coming to Claude Code Night, the free Monday room.</li>
    </ul>
  </div>
</div>
<div class="divider"></div>
<section class="section-dark" id="seat" style="padding:72px 0;">
  <div class="container-narrow">
    <div class="form-wrapper reveal">
      <div class="form-title">Hold me a seat</div>
      <div class="form-sub">Leave your name and email and write COHORT in the message. You hear the dates first, and nothing is charged until you take the seat.</div>
      <iframe src="https://api.leadconnectorhq.com/widget/form/{CONTACT_FORM}" style="display:inline;width:100%;height:640px;border:none;border-radius:4px" id="inline-{CONTACT_FORM}" data-layout="{{'id':'INLINE'}}" data-trigger-type="alwaysShow" data-activation-type="alwaysActivated" data-deactivation-type="neverDeactivate" data-height="640" data-layout-iframe-id="inline-{CONTACT_FORM}" data-form-id="{CONTACT_FORM}" title="Hold a cohort seat"></iframe>
      <script src="https://link.msgsndr.com/js/form_embed.js"></script>
    </div>
  </div>
</section>'''
cohort_faq = [
    ("Do I need to know how to code?", "No. I have never written a line of code. Everything happens by talking to Claude Code in plain English."),
    ("What does it cost to run afterward?", "Your own Claude subscription, which you pay Anthropic directly. Nothing is paid to me after the five weeks."),
    ("What if I miss a session?", "Tell the group chat. Week 3 has a one-on-one with me, and that is where we catch you up."),
    ("Can you just build it for me instead?", "Yes, but that is a different thing. Start with a diagnosis on the pricing page."),
]
written.append(page("cohort", "Run Your Business on Claude Code, 5-Week Cohort | Brycen Wood", "Five weeks, one evening a week, 8 to 12 business owners. Leave with your own Claude Code system running. $1,500, full refund before week 1 ends.", "Cohort", cohort_body, cohort_faq))

# ---------- /community/ ----------
community_body = '''<section class="page-hero">
  <p class="hero-eyebrow">Claude Code Night</p>
  <h1>A Monday night for owners who <span class="accent">run Claude Code.</span></h1>
  <p class="hero-sub">Free, in person, in Utah County. Everyone in the room already runs their business on Claude Code. Every week a real setup goes up on the screen and the room works on what people are stuck on.</p>
  <div class="btn-group" style="margin-top:24px"><a href="https://www.instagram.com/brycenwood.ai/" class="btn-primary" target="_blank" rel="noopener">DM me NIGHT for the address</a></div>
</section>
<div class="divider"></div>
<div class="section-dark">
  <div class="section-header reveal"><h2>What to <span class="accent">bring</span></h2></div>
  <div class="container-narrow reveal">
    <ul class="plain-list">
      <li>Your laptop with Claude Code open.</li>
      <li>The thing you are stuck on, or a build you want to show.</li>
    </ul>
    <p class="ladder-note">Never used Claude Code? The <a href="/cohort/" style="color:var(--lime)">5-week cohort</a> is built for exactly that.</p>
  </div>
</div>'''
community_faq = [
    ("Is it really free?", "Yes. The room is free. The cohort and the services on the pricing page are what cost money."),
    ("I have never used Claude Code. Should I come?", "Come and watch, but you will get more from the 5-week cohort first. The room is for people already running it."),
    ]
written.append(page("community", "Claude Code Night, Utah | Brycen Wood", "A free Monday night in Utah County for business owners who run Claude Code. A real build on the wall, two problems worked live, one commitment each.", "Community", community_body, community_faq))

# ---------- /services/retainer/ ----------
retainer_body = '''<section class="page-hero">
  <p class="hero-eyebrow">Retainer, after a build</p>
  <h1>I keep what I built <span class="accent">running.</span></h1>
  <p class="hero-sub">A retainer is only for systems I built for you. It keeps them alive and getting better, without you becoming a part-time developer.</p>
</section>
<div class="divider"></div>
<div class="section-dark">
  <div class="pricing-grid" style="grid-template-columns:1fr;max-width:560px;margin:0 auto">
    <div class="price-card featured reveal">
      <div class="price-label">Retainer</div>
      <div class="price-amount">$1,500<span style="font-size:20px;opacity:0.6">/month</span></div>
      <div class="price-period">3-month minimum, then 30 days notice either way</div>
      <ul class="price-features">
        <li>Monitoring and fixes on the system I built</li>
        <li>Small changes, each under about two hours</li>
        <li>A 30-minute review every month</li>
        <li>A written log of everything that changed</li>
      </ul>
      <a href="/pricing/" class="btn-primary" style="display:block;text-align:center">Start with a diagnosis</a>
      <p class="ladder-note">Not included: new systems (that is a build), same-day or on-call response, other businesses.</p>
    </div>
  </div>
</div>'''
written.append(page(os.path.join("services", "retainer"), "Retainer | Brycen Wood", "After a build only: monitoring, fixes, small changes and a monthly review for the system I built. $1,500 a month, 3-month minimum.", "Retainer", retainer_body))

for w in written:
    print("wrote build/" + w)
