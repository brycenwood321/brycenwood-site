# brycenwood.com — SEO Master Plan

## Goal
Draw organic traffic daily that converts to either Skool community members or custom build discovery calls. Dominate the "AI business automation for non-technical founders" niche.

## Current State (Apr 14, 2026)
- 26 pages live, all SEO-optimized
- GSC verified + sitemap submitted
- GA4 live (G-2GV8RG30MK)
- Schema on every page (Article, Service, FAQPage, Person, BreadcrumbList)
- llms.txt + 23 markdown mirrors
- 10 pages keyword-optimized for competitive terms
- SEO audit score: ~80/100 (before keyword optimization)

---

## PHASE 1: New Pages to Build (15 pages)

### Blog Posts (8 articles targeting specific keywords)

Each blog post: 2,500-4,000 words, full WHAT/WHY on page, HOW in Skool community.

| # | URL | Target Keyword | Competition | Search Intent |
|---|-----|---------------|-------------|---------------|
| 1 | `/blog/build-vs-buy-vs-vibe-code/` | "build vs buy business software" | MEDIUM | Comparison (buyer) |
| 2 | `/blog/ai-automation-vs-agency/` | "AI automation vs agency" | LOW-MEDIUM | Comparison (buyer) |
| 3 | `/blog/custom-automation-vs-hiring-developer/` | "custom automation vs hiring developer" | LOW-MEDIUM | Comparison (buyer) |
| 4 | `/blog/chatgpt-recommend-your-business/` | "make chatgpt recommend your business" | LOW-MEDIUM | Informational (warm) |
| 5 | `/blog/automate-business-without-coding/` | "build business systems with AI" | MEDIUM | Informational |
| 6 | `/blog/ai-business-automation-cost/` | "how much does business automation cost" | LOW | Buyer intent |
| 7 | `/blog/small-business-ai-tools-2026/` | "best AI tools for small business 2026" | MEDIUM | Informational |
| 8 | `/blog/what-can-claude-code-build/` | "what can claude code build" | LOW-MEDIUM | Informational |

### Comparison Pages (3 pages — high buyer intent)

| # | URL | Target Keyword | Why |
|---|-----|---------------|-----|
| 9 | `/compare/custom-build-vs-agency/` | "custom build vs marketing agency" | Direct comparison page, positions Brycen as the alternative |
| 10 | `/compare/custom-build-vs-zapier/` | "custom automation vs zapier" | Differentiates from the no-code crowd |
| 11 | `/compare/custom-build-vs-developer/` | "hire developer vs AI automation" | Cost comparison with real numbers |

### Industry Landing Pages (4 pages — targeted verticals)

| # | URL | Target Keyword | Why |
|---|-----|---------------|-----|
| 12 | `/industries/hvac-automation/` | "HVAC business automation" | Direct vertical Brycen serves |
| 13 | `/industries/roofing-automation/` | "roofing company automation" | Summit Wraps tier A customer |
| 14 | `/industries/plumbing-automation/` | "plumbing business automation" | Summit Wraps tier A customer |
| 15 | `/industries/service-business-automation/` | "service business automation AI" | Catch-all for all service businesses |

---

## PHASE 2: Content Upgrades to Existing Pages

### Add to EVERY guide page:
- [ ] Table of Contents (linked, at top of article)
- [ ] "Key Takeaway" summary box at top (150 words, AI-citable)
- [ ] "Related Guides" section at bottom (3 contextual links)
- [ ] Outbound citations (link to tool docs, Claude Code docs, industry sources)
- [ ] Visible publish date + last updated date

### Expand specific pages:
- [ ] About page: add "Businesses I've Built For" section with industry list
- [ ] Summit Wraps case study: add before/after screenshots (need from Brycen)
- [ ] Blackout Auto Tint case study: add screenshots of the actual site

### Internal linking improvements:
- [ ] Homepage: add "Latest from the Blog" section showing 3 recent posts
- [ ] Each guide: link to 2-3 other guides within the body text
- [ ] Each blog post: link to relevant service page + case study
- [ ] Services page: link to ALL case studies and relevant guides

---

## PHASE 3: Blog Infrastructure

### Create blog index page
- `/blog/` — lists all blog posts with cards
- Sorted by date (newest first)
- Each card shows: title, excerpt, date, reading time, target topic tag

### Blog post template
Standard structure for every post:
1. Title (H1 with target keyword)
2. Author byline (Brycen Wood, linked to /about/)
3. Key Takeaway box (150 words)
4. Table of Contents (linked)
5. Content (2,500-4,000 words with H2/H3 hierarchy)
6. Mid-article CTA (join community)
7. FAQ section (3-4 questions, with FAQPage schema)
8. Related content (2 guides + 1 blog post)
9. Bottom CTA (community + discovery call)
10. Author card

### Blog RSS feed
- `/blog/feed.xml` — standard RSS/Atom feed
- Helps content aggregators and some AI systems discover new posts

---

## PHASE 4: Technical SEO Improvements

### IndexNow Protocol
- [ ] Generate IndexNow key
- [ ] Place key file at `/build/{key}.txt`
- [ ] Create deploy script that pings IndexNow after every git push
- [ ] Covers Bing, Yandex, Naver instant indexing

### Page Speed Optimizations
- [ ] Self-host Google Fonts (eliminate render-blocking external request)
- [ ] Add `loading="lazy"` to any images below the fold
- [ ] Minify CSS files (global.css + components.css)
- [ ] Add preload hints for critical CSS

### Crawl Optimization
- [ ] Add `_redirects` file: redirect `brycenwood-site.pages.dev/*` to `brycenwood.com/*` (301)
- [ ] Ensure all internal links use `https://www.brycenwood.com/` (canonical domain)
- [ ] Add `hreflang="en"` to all pages (signals English content to international crawlers)

---

## PHASE 5: Content Velocity Strategy

### Weekly publishing cadence
- 1 blog post per week (targeting a new keyword each time)
- Update 1 existing guide per week (add depth, new data, refresh date)
- Each new blog post: push to GitHub → auto-deploy → ping IndexNow → submit to GSC

### Content ideas pipeline (next 20 blog posts after Phase 1)

| Topic | Target Keyword | Type |
|-------|---------------|------|
| How I Score 5,500 Leads in 5 Minutes | "AI lead scoring" | Tutorial |
| The Morning Briefing System That Runs My Day | "AI morning briefing" | Build story |
| Why I Switched from Zapier to Claude Code | "zapier alternative for business" | Comparison |
| How My AI Sends 739 Unique Emails Overnight | "AI email personalization" | Tutorial |
| The Instagram DM Engine (25% Reply Rate) | "instagram DM automation" | Tutorial |
| I Built a Voice AI Receptionist for $5/Month | "AI receptionist small business" | Build story |
| Dashboard I Check from My Phone in the Gym | "business dashboard mobile" | Build story |
| How to Set Up GoHighLevel for AI Automation | "GoHighLevel automation setup" | Tutorial |
| My Full Tech Stack: $150/Month for 80+ Systems | "AI business tools cheap" | Listicle |
| Why Agencies Charge $15K for What I Build in 2 Weeks | "marketing agency vs AI" | Opinion |
| The Content Pipeline That Posts While I Sleep | "automated content posting" | Tutorial |
| How I Automated My QuickBooks | "QuickBooks AI automation" | Tutorial |
| AI SEO: The 3 Files Google Can't Ignore | "AI SEO strategy 2026" | Tutorial |
| From Spreadsheets to Systems: A Small Business Story | "spreadsheet to CRM migration" | Story |
| The $3,500 Build That Replaced a $180K/Year Team | "replace team with AI" | Case study |
| How I Track Every Lead Without Touching a Spreadsheet | "automated lead tracking" | Tutorial |
| Building a Business Website in 4 Hours (Live Demo) | "build website with AI" | Tutorial |
| The Markdown Mirrors Technique Nobody Talks About | "markdown mirrors website" | Tutorial |
| My Honest Review of Claude Code After 80+ Builds | "claude code review 2026" | Review |
| The System That Catches My Business Mistakes Before I Do | "AI business monitoring" | Build story |

### Repurposing strategy
- Every blog post → summarize for a Skool community thread
- Every blog post → pull 3-5 key stats for carousel slides
- Every blog post → 60-second video script for IG/TT
- This creates a flywheel: video drives traffic → site captures search → community converts

---

## PHASE 6: Link Building & Authority

### Quick wins (can do immediately)
- [ ] Submit site to relevant directories (Clutch, DesignRush, UpCity for consultants)
- [ ] Create a Product Hunt launch post for the free community
- [ ] Answer questions on Quora targeting our keywords (link back to guides)
- [ ] Post on relevant subreddits (r/smallbusiness, r/entrepreneur, r/ClaudeAI, r/ChatGPT)
- [ ] Add brycenwood.com to LinkedIn profile
- [ ] Create a Medium publication that cross-posts guide excerpts (with canonical back to site)

### Ongoing authority building
- [ ] Guest post on 1 relevant blog per month
- [ ] Get quoted in 1 roundup/listicle article per month
- [ ] Build relationships with other Claude Code creators for cross-linking
- [ ] Earn backlinks naturally from guide content (the llms.txt guide should get cited by others writing about the topic)

---

## PHASE 7: Conversion Optimization

### Track these metrics weekly (GSC + GA4)
- Total impressions (target: 5,000/week by week 8)
- Total clicks (target: 200/week by week 8)
- Click-through rate by page (target: 5%+ average)
- Top queries gaining impressions
- Pages indexed (target: all pages indexed within 2 weeks)
- Skool signups per week from organic
- Discovery calls booked per week from organic

### A/B test these elements
- [ ] CTA button copy on guide pages ("Join the Free Community" vs "Get the Prompts Free")
- [ ] Hero headline on homepage
- [ ] Pricing page layout (3-tier vs single featured tier)
- [ ] Mid-article CTA placement (after H2 #2 vs after H2 #3)

### Conversion paths to optimize
1. Guide page → mid-article CTA → Skool community (primary)
2. Guide page → bottom CTA → discovery call (secondary)
3. Blog post → related guide → Skool community
4. Comparison page → service page → discovery call
5. Industry page → case study → discovery call

---

## EXECUTION PRIORITY (What to Build Next)

### Session 1 (next session): Blog Infrastructure + First 3 Posts
1. Create `/blog/` index page
2. Build blog post template
3. Write: "Build vs Buy vs Vibe Code" (comparison, high buyer intent)
4. Write: "AI Automation vs Agency" (comparison, high buyer intent)
5. Write: "How Much Does Business Automation Cost" (buyer intent, low competition)
6. Update sitemap + regenerate mirrors
7. Commit + deploy

### Session 2: Comparison Pages + Industry Pages
1. Build 3 comparison pages (/compare/*)
2. Build 4 industry pages (/industries/*)
3. Add Table of Contents to all existing guide pages
4. Add "Related Guides" sections
5. Update sitemap + regenerate mirrors

### Session 3: Content Upgrades + Technical SEO
1. Add Key Takeaway boxes to all guides
2. Add outbound citations to all guides
3. Set up IndexNow
4. Self-host Google Fonts
5. Minify CSS
6. Set up pages.dev → brycenwood.com redirect

### Session 4: Next 5 Blog Posts
1. Write 5 more blog posts from the pipeline
2. Update blog index
3. Create RSS feed
4. Submit new URLs to GSC

### Ongoing: 1 Blog Post Per Week
- Follow the 20-post pipeline above
- Each post targets a specific keyword
- Each post links to relevant guides + services
- Each post gets repurposed into social content

---

## KEY RULES

1. **Every page targets ONE primary keyword** — don't dilute by targeting multiple
2. **Every page links to at least 3 other pages** on the site
3. **Every blog post ends with a CTA** to either Skool or discovery call
4. **Full content on the site, implementation in Skool** — don't gate knowledge
5. **Proof first, theory second** — every claim backed by a real number from Brycen's business
6. **Update the sitemap and regenerate mirrors** after every content addition
7. **Check GSC weekly** — find keywords gaining impressions and create content to capture them
