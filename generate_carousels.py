"""
Carousel Generator — Builds HTML files for each carousel and screenshots all slides.
Run: python3 personal/brycenwood-site/generate_carousels.py
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "carousels")
os.makedirs(OUT_DIR, exist_ok=True)

# ── Read the CSS from the template ──
with open(os.path.join(BASE_DIR, "carousel-template.html"), encoding="utf-8") as f:
    template_html = f.read()
# Extract style block
style_start = template_html.index("<style>")
style_end = template_html.index("</style>") + len("</style>")
STYLE_BLOCK = template_html[style_start:style_end]


def slide_cover(tag, headline, sub, num, total):
    return f'''<div class="slide slide-cover">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> {tag}</div>
  <span class="slide-num">{num}/{total}</span>
  <div class="slide-inner">
    <div class="cover-tag">&nbsp;</div>
    <div style="margin-top:auto">
      <div class="cover-headline">{headline}</div>
      <div class="cover-rule"></div>
      <div class="cover-sub">{sub}</div>
    </div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_content(cat, status, title, desc, number, num, total):
    return f'''<div class="slide slide-content">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> SYSTEMS</div>
  <span class="slide-num">{num}/{total}</span>
  <span class="content-num">{number}</span>
  <div class="slide-inner">
    <div class="content-cat">{cat}</div>
    <div class="content-body">
      <div class="content-status"><span class="dot live"></span> {status}</div>
      <div class="content-title">{title}</div>
      <div class="content-desc">{desc}</div>
    </div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_content_list(cat, items_text, num, total):
    """Content slide with a list of items instead of title+desc."""
    items_html = ""
    for item in items_text:
        items_html += f'<div style="font-size:18px;color:var(--text-mid);padding:4px 0;line-height:1.4">{item}</div>\n'
    return f'''<div class="slide slide-content">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> SYSTEMS</div>
  <span class="slide-num">{num}/{total}</span>
  <div class="slide-inner">
    <div class="content-cat">{cat}</div>
    <div class="content-body" style="margin-bottom:40px">
      {items_html}
    </div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_stats(value, label, num, total):
    bars = ''.join(f'<span style="height:{h}%"></span>' for h in [30,45,25,60,40,75,55,85,50,65,90,70,95,80,60,45,70,55,85,100,75,50,65,40])
    return f'''<div class="slide slide-stats">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> BY THE NUMBERS</div>
  <span class="slide-num">{num}/{total}</span>
  <div class="stats-bars">{bars}</div>
  <div class="stats-inner">
    <div class="stats-val">{value}</div>
    <div class="stats-label">{label}</div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_compare(left_items, right_items, num, total):
    left_html = ''.join(f'<div class="compare-item">{i}</div>' for i in left_items)
    right_html = ''.join(f'<div class="compare-item">{i}</div>' for i in right_items)
    return f'''<div class="slide slide-compare">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> COMPARISON</div>
  <span class="slide-num" style="color:var(--text-dim)">{num}/{total}</span>
  <div class="compare-divider"></div>
  <div class="compare-grid">
    <div class="compare-side compare-left">
      <div class="compare-label">You</div>
      {left_html}
    </div>
    <div class="compare-side compare-right">
      <div class="compare-label">My AI</div>
      {right_html}
    </div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_compare_single(left_text, right_text, num, total):
    return f'''<div class="slide slide-compare">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> COMPARISON</div>
  <span class="slide-num" style="color:var(--text-dim)">{num}/{total}</span>
  <div class="compare-divider"></div>
  <div class="compare-grid">
    <div class="compare-side compare-left" style="justify-content:center">
      <div class="compare-label">You</div>
      <div style="font-size:26px;color:var(--text-dim);line-height:1.4">{left_text}</div>
    </div>
    <div class="compare-side compare-right" style="justify-content:center">
      <div class="compare-label">My AI</div>
      <div style="font-size:26px;color:var(--text);line-height:1.4;font-weight:500">{right_text}</div>
    </div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_cta(pre, main_text, after, desc, num, total):
    return f'''<div class="slide slide-cta">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> JOIN</div>
  <span class="slide-num">{num}/{total}</span>
  <div class="slide-inner">
    <div class="cta-pre">{pre}</div>
    <div class="cta-main">Comment<br><span class="accent">BUILD</span></div>
    <div class="cta-after">{after}</div>
    <div class="cta-desc">{desc}</div>
    <div class="cta-handle">@brycenwood.ai</div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def slide_quote(quote, attr, num, total):
    return f'''<div class="slide slide-quote">
  <div class="slide-vignette"></div><div class="slide-streak"></div>
  <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
  <div class="corner corner-bl"></div><div class="corner corner-br"></div>
  <div class="slide-tag"><span class="tag-dot"></span> REAL DMS</div>
  <div class="quote-marks">"</div>
  <div class="slide-inner">
    <div class="quote-text">"{quote}"</div>
    <div class="quote-rule"></div>
    <div class="quote-attr">{attr}</div>
  </div>
  <div class="brand"><span>@BRYCENWOOD.AI</span><span class="brand-community">BUSINESS ON AUTOPILOT</span></div>
</div>'''


def build_html(title, slides_html):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{STYLE_BLOCK}
</head><body>
<div class="page-header"><h1>{title}</h1></div>
<div class="slides-row">
{slides_html}
</div></body></html>'''


def save_carousel(folder_name, title, slides_html):
    html = build_html(title, slides_html)
    folder = os.path.join(OUT_DIR, folder_name)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "carousel.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Built: {folder_name}/carousel.html ({slides_html.count('class=\"slide ')} slides)")
    return filepath


# ════════════════════════════════════════════
# BUILD ALL 10 CAROUSELS
# ════════════════════════════════════════════

print("Building carousel HTML files...\n")

# ── #2: You vs My AI ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "STILL DOING<br>EVERYTHING<br><span class='accent'>MANUALLY?</span>", "Here's what my AI does instead.", 1, 8))
slides.append(slide_compare_single("Send cold emails one by one", "Emailed <span class='hl'>5,500 businesses</span> overnight — each one personalized after reading their website", 2, 8))
slides.append(slide_compare_single("Spend hours figuring out what to focus on", "Briefs me every morning at 8 AM with <span class='hl'>ranked priorities</span> from my CRM, inbox, and calendar", 3, 8))
slides.append(slide_compare_single("Manually post to every platform", "Posts to Instagram once, auto cross-posts to <span class='hl'>YouTube with SEO titles</span>", 4, 8))
slides.append(slide_compare_single("Ignore DMs because there's too many", "Reads every profile and writes a personalized reply. <span class='hl'>45% click rate.</span>", 5, 8))
slides.append(slide_compare_single("Forget to follow up with leads", "Tracks every lead through <span class='hl'>10 stages</span> and follows up automatically", 6, 8))
slides.append(slide_compare_single("Hope your website gets found", "Built a site that <span class='hl'>outranks competitors</span> and got recommended by ChatGPT by name", 7, 8))
slides.append(slide_cta("Ready to stop doing it all manually?", "", "to get on the waitlist.", "I'm building a free community where I break down how I built every one of these systems. Zero code required.", 8, 8))
save_carousel("02-you-vs-my-ai", "Carousel #2 — You vs My AI", "\n".join(slides))

# ── #3: 80+ Automations List ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "80+<br>AUTOMATIONS.<br><span class='accent'>ZERO CODE.</span>", "Here's every system I built for my business.", 1, 12))
slides.append(slide_content_list("CRM & SALES — 12 SYSTEMS", ["AI Lead Scorer", "AI Email Writer", "Auto Email Sender", "Reply Detector", "Bounce Tracker", "Follow-Up Sequencer", "Pipeline State Machine", "Stage Sync", "Touchpoint Logger", "QuickBooks Sync", "CRM Migration", "Hot Lead Alerts"], 2, 12))
slides.append(slide_content_list("CONTENT CREATION — 11 SYSTEMS", ["AI Clip Analyzer", "Reel Composer", "Video Renderer", "Cover Image Generator", "AI Content Calendar", "Content Multiplier", "YouTube Cross-Post (x2)", "Filming Brief Generator", "Competitor Scraper", "Post Auditor"], 3, 12))
slides.append(slide_content_list("INSTAGRAM DM ENGINE — 8 SYSTEMS", ["Auto Follower Detection", "Profile Scanner", "Personalized Message Generator", "Conversation Phase Tracker", "A/B Strategy Tester", "Pitch Keyword Blocker", "Reactivation Scheduler", "Weekly DM Analyzer"], 4, 12))
slides.append(slide_content_list("DASHBOARD & MONITORING — 6 SYSTEMS", ["Full Business Dashboard", "Phone Access Anywhere", "Morning Auto-Briefing", "System Watchdog (Guardian)", "Instagram Webhooks", "File Sharing Server"], 5, 12))
slides.append(slide_content_list("WEBSITE & SEO — 9 SYSTEMS", ["Full Website (24 pages)", "Markdown Mirrors (24 pages)", "llms.txt", "Schema Markup", "Search Console API", "Image Geo-Tagging", "Image Compression", "AI SEO Playbook", "Lead Magnet Funnel"], 6, 12))
slides.append(slide_content_list("INSTAGRAM + VOICE + WRAP DESIGN — 14 SYSTEMS", ["Manychat Funnel (45% CTR)", "Graph API Integration", "Multi-Account Management", "Ad Tracker", "Engagement Analyzer", "Voice Clone ($5/mo)", "Voiceover Generator", "AI Design Generator", "Illustrator Pipeline", "Component Library", "Brand Scraper", "Template Analyzer", "Batch Generator", "Mockup Generator"], 7, 12))
slides.append(slide_content_list("CLIENT DELIVERY + OPS — 11 SYSTEMS", ["Website Audit Tool", "Blueprint Generator", "Prospect Ranker", "Waitlist Manager", "5 Demo Sites Delivered", "Task Manager", "Habit Tracker", "Goal Tracker", "Journal System", "Weekly Review", "Hiring Pipeline"], 8, 12))
slides.append(slide_content_list("API INTEGRATIONS — 8 CONNECTED", ["GoHighLevel CRM", "Instagram Graph API", "Gmail API", "Google Search Console", "YouTube Data API (x2)", "QuickBooks Online", "ElevenLabs Voice AI", "Cloudflare"], 9, 12))
slides.append(slide_stats("104", "total systems.<br><strong>79 live. 25+ planned.</strong>", 10, 12))
slides.append(slide_content_list("COMING SOON — 25+ PLANNED", ["Voice DM Responder", "AI Receptionist", "Auto Client Onboarding", "Content Repurposing", "Competitor Alerts", "Client Dashboard", "Auto Weekly Reports", "Proposal Generator", "Smart Pricing Engine", "Referral Tracking", "+ 15 more in development"], 11, 12))
slides.append(slide_cta("Want to build this for YOUR business?", "", "to get on the waitlist.", "Every prompt. Every tool. Every system broken down inside a free community.", 12, 12))
save_carousel("03-full-list", "Carousel #3 — 80+ Automations Full List", "\n".join(slides))

# ── #4: 5 AI Tools ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "5 TOOLS.<br><span class='accent'>ENTIRE<br>BUSINESS.</span>", "My full tech stack. No employees. No agencies.", 1, 7))
slides.append(slide_content("TOOL 1", "PRIMARY", "Claude Code", "The brain. Built every automation, every script, every website, every system. I don't write code — I describe what I need and it builds it.", "01", 2, 7))
slides.append(slide_content("TOOL 2", "$97/MONTH", "GoHighLevel", "My command center. Contacts, pipelines, invoices, calendar, forms, automations. Everything funnels here.", "02", 3, 7))
slides.append(slide_content("TOOL 3", "$5/MONTH", "ElevenLabs", "Cloned my voice. Generates voiceovers for Reels and voice memos for DM replies. People can't tell the difference.", "03", 4, 7))
slides.append(slide_content("TOOL 4", "45% CTR", "Manychat", "Automated DM funnel. Comment a keyword → instant personalized DM with the link. 45% click-through rate.", "04", 5, 7))
slides.append(slide_content("TOOL 5", "FREE TIER", "Cloudflare", "DNS, security, and a tunnel that turns my laptop into a web server. Business dashboard from my phone. Anywhere.", "05", 6, 7))
slides.append(slide_cta("Want the full breakdown?", "", "to get on the waitlist.", "I'm showing people how to set up this exact stack inside a free community. No coding required.", 7, 7))
save_carousel("04-five-tools", "Carousel #4 — 5 AI Tools", "\n".join(slides))

# ── #5: What AI Actually Looks Like ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "NOT CHATGPT.<br>NOT ROBOTS.<br><span class='accent'>THIS.</span>", "What AI actually looks like when you run a real business.", 1, 8))
slides.append(slide_content("REAL AI", "8 AM DAILY", "My Morning Briefing", "Every day at 8 AM, my AI pulls my CRM, inbox, calendar, and pipeline. Tells me exactly what to focus on.", "01", 2, 8))
slides.append(slide_content("REAL AI", "RUNS NIGHTLY", "My Cold Email System", "AI visits each company's website, reads their content, writes a personalized email. Sends 15/day. Detects replies.", "02", 3, 8))
slides.append(slide_content("REAL AI", "25% REPLY RATE", "My DM Engine", "Reads every new follower's profile. Writes a custom message based on their bio and business. Compliment strategy wins.", "03", 4, 8))
slides.append(slide_content("REAL AI", "10 STAGES", "My Sales Pipeline", "Every lead tracked. Follow-ups queued automatically. CRM updates itself. Haven't manually moved a card in 3 weeks.", "04", 5, 8))
slides.append(slide_content("REAL AI", "$5/MONTH", "My Voice Clone", "AI-generated voice memos that sound exactly like me. Used for Reel voiceovers and DM replies.", "05", 6, 8))
slides.append(slide_content("REAL AI", "FROM ANYWHERE", "My Phone Dashboard", "Full business dashboard through a Cloudflare tunnel. Pipeline, finances, tasks, habits, alerts. One screen.", "06", 7, 8))
slides.append(slide_cta("This is what AI can do for YOUR business.", "", "to get on the waitlist.", "Free community. Every system broken down. The prompts, the tools, all of it. Zero coding experience needed.", 8, 8))
save_carousel("05-what-ai-looks-like", "Carousel #5 — What AI Actually Looks Like", "\n".join(slides))

# ── #6: 0 to 7,000 Followers ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "0 TO 7,000.<br><span class='accent'>3 WEEKS.</span>", "Here's exactly what happened. No ads. No tricks.", 1, 9))
slides.append(slide_stats("0", "followers on Day 1.<br><strong>No audience. No brand. Just an idea.</strong>", 2, 9))
slides.append(slide_content("WEEK 1", "POSTED", "First Video: llms.txt", '"ChatGPT is recommending my business." Face-to-camera, 60 seconds. Went to bed with 50 views. Woke up with 10,000.', "01", 3, 9))
slides.append(slide_stats("1.1M", "views on that one video.<br><strong>4,300 new followers. 47,000 saves.</strong>", 4, 9))
slides.append(slide_content("WEEK 2", "6 MINUTES", "Set Up Manychat", "Automated DM funnel. Comment a keyword → instant DM. 45% click rate. 253 leads captured in one day.", "02", 5, 9))
slides.append(slide_content("WEEK 2", "AUDIENCE-PICKED", "Part 2: Markdown Mirrors", "Topic came from Part 1 comments. 48K views, 14.5% comment rate, 10% save rate. The community was building itself.", "03", 6, 9))
slides.append(slide_content("WEEK 3", "KEPT GOING", "More Videos. Same Funnel.", "Part 4, morning briefing, systems overview. Every video → same CTA → same funnel → waitlist grows.", "04", 7, 9))
slides.append(slide_stats("7,000+", "followers. 1,374 waitlist signups.<br><strong>Zero dollars spent on ads.</strong>", 8, 9))
slides.append(slide_cta("The playbook is free.", "", "to get on the waitlist.", "I'm breaking down exactly how I did this — the content strategy, the funnel, the tools — inside a free community.", 9, 9))
save_carousel("06-zero-to-7k", "Carousel #6 — 0 to 7,000 Followers", "\n".join(slides))

# ── #7: 3 Files for AI Recommendations ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "3 FILES.<br><span class='accent'>AI RECOMMENDS<br>YOU.</span>", "How I got ChatGPT to recommend my business by name.", 1, 8))
slides.append(slide_content("FILE 1", "10 MINUTES", "llms.txt", "A plain text file at your website's root. Tells AI crawlers what your business does, what services you offer, and where to find content.", "01", 2, 8))
slides.append(slide_content("FILE 2", "ONE SCRIPT", "Markdown Mirrors", "A clean .md version of every page. AI reads these instead of wrestling through HTML, popups, and tracking scripts.", "02", 3, 8))
slides.append(slide_content("FILE 3", "SUBMIT TO GSC", "Updated XML Sitemap", "Your sitemap tells Google AND AI crawlers which pages exist. Include your new .md URLs. Submit to Search Console.", "03", 4, 8))
slides.append(slide_stats("1.1M", "views on the video where I showed this working.<br><strong>ChatGPT recommended my business by name.</strong>", 5, 8))
slides.append(slide_compare_single("Your website is invisible to AI. ChatGPT doesn't know you exist.", "Built all 3 files. ChatGPT recommends my business for <span class='hl'>4 different search queries.</span>", 6, 8))
slides.append(slide_quote("Wait, ChatGPT actually recommends your business? How?", "— thousands of comments on the original video", 7, 8))
slides.append(slide_cta("Want to set this up?", "", "to get on the waitlist.", "I break down exactly how — the files, the prompts, the tools — inside a free community. No coding needed.", 8, 8))
save_carousel("07-three-files", "Carousel #7 — 3 Files for AI Recommendations", "\n".join(slides))

# ── #8: Morning Briefing Breakdown ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "EVERY MORNING.<br>8 AM.<br><span class='accent'>AUTOMATIC.</span>", "My AI briefs me before I wake up. Here's what it shows.", 1, 8))
slides.append(slide_content("SECTION 1", "RANKED BY IMPACT", "Top 5 Priorities", "Pulls from my CRM, inbox, and calendar. Ranks everything by what moves the needle most. High/medium/low tags. No guessing.", "01", 2, 8))
slides.append(slide_content("SECTION 2", "LIVE DATA", "Pipeline Status", "47 active leads. 8 need follow-up. 3 replies overnight. $21.3K revenue this month. 564 cold emails queued.", "02", 3, 8))
slides.append(slide_content("SECTION 3", "CHECKMARKS", "Overnight Activity Log", "Everything my AI did while I slept. Emails sent, replies classified, CRM updated, YouTube posted, competitors scraped.", "03", 4, 8))
slides.append(slide_content("SECTION 4", "FROM CRM", "Today's Calendar", "Discovery calls, design reviews, filming sessions. Even calculates golden hour for outdoor content shoots.", "04", 5, 8))
slides.append(slide_content("SECTION 5", "STREAKS", "Habit Tracker", "Weightlifting, journaling, reading, time with my wife. Streak counts. Keeps me accountable outside of business.", "05", 6, 8))
slides.append(slide_stats("17", "automations feeding into one briefing.<br><strong>Every morning. Zero effort.</strong>", 7, 8))
slides.append(slide_cta("Want your own morning briefing?", "", "to get on the waitlist.", "I'm showing people how to build this exact system inside a free community. No coding experience needed.", 8, 8))
save_carousel("08-morning-briefing", "Carousel #8 — Morning Briefing Breakdown", "\n".join(slides))

# ── #9: 5,500 Personalized Emails ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "5,500 EMAILS.<br><span class='accent'>ONE NIGHT.</span>", "Every single one personalized. Here's the system.", 1, 9))
slides.append(slide_content("STEP 1", "A/B/C GRADES", "Score Every Business", "AI grades every business by industry, fleet size, and location. 5,500 scored. Only Grade A gets emailed first.", "01", 2, 9))
slides.append(slide_content("STEP 2", "WEB SCRAPE", "Read Their Website", "For each business, my AI visits their actual website. Reads what they do, their services, their about page.", "02", 3, 9))
slides.append(slide_content("STEP 3", "AI DRAFTED", "Write a Custom Email", "Using the website content, AI writes a fully personalized email. References their specific services. Never pitches.", "03", 4, 9))
slides.append(slide_content("STEP 4", "15/DAY", "Send on Autopilot", "Gmail API sends, logs every send, prevents double-sending. Warms up the domain naturally.", "04", 5, 9))
slides.append(slide_content("STEP 5", "EVERY HOUR", "Detect Replies", "AI scans inbox hourly. Classifies: interested, not interested, out of office. Updates CRM. Queues follow-up.", "05", 6, 9))
slides.append(slide_content("STEP 6", "AUTOMATIC", "Follow Up at the Right Time", "No manual tracking. No spreadsheets. The system knows who got what and when they need the next touch.", "06", 7, 9))
slides.append(slide_stats("$0", "spent on developers.<br><strong>I described what I needed. Claude Code built it.</strong>", 8, 9))
slides.append(slide_cta("Want to build your own email system?", "", "to get on the waitlist.", "I'm breaking down the exact process — including the prompts — inside a free community. Zero coding needed.", 9, 9))
save_carousel("09-cold-email-system", "Carousel #9 — 5,500 Personalized Emails", "\n".join(slides))

# ── #10: $3,600 Saved ──
slides = []
slides.append(slide_cover("@brycenwood.ai", "$3,600 SAVED.<br><span class='accent'>ONE<br>CONVERSATION.</span>", "I was overpaying for my CRM. AI fixed it.", 1, 8))
slides.append(slide_stats("$400", "per month.<br><strong>What I was paying for my CRM through a reseller.</strong>", 2, 8))
slides.append(slide_content("THE PROBLEM", "4X MARKUP", "Paying a Middleman", "My CRM was through a $400/month reseller. Same software, marked up 4x. I didn't know I could go direct for $97.", "—", 3, 8))
slides.append(slide_content("THE FIX", "ONE CONVERSATION", "Migrated Everything", "Told my AI to move everything. 192 contacts. 160 opportunities. 33 custom fields. 8 pipelines. Nothing lost.", "→", 4, 8))
slides.append(slide_stats("$97", "per month. Same software. Direct.<br><strong>No middleman.</strong>", 5, 8))
slides.append(slide_compare(
    ["$400/month", "Middleman markup", "Limited support", "Locked in"],
    ["<span class='hl'>$97/month</span>", "<span class='hl'>Direct access</span>", "<span class='hl'>Full control</span>", "<span class='hl'>$3,600 saved/year</span>"],
    6, 8))
slides.append(slide_quote("You can just... move everything over? With AI?", "— what I said before I tried it", 7, 8))
slides.append(slide_cta("What's your business overpaying for?", "", "to get on the waitlist.", "I'm breaking down how I built every system — including this migration — inside a free community.", 8, 8))
save_carousel("10-crm-savings", "Carousel #10 — $3,600 Saved", "\n".join(slides))

print("\n✅ All 9 carousels built! (Carousel #1 already exists from template)")
print(f"   Output: {OUT_DIR}/")
