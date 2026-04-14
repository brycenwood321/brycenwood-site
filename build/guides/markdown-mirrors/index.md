---
title: Markdown Mirrors — Make Your Website Readable by AI | Brycen Wood
description: Markdown mirrors let ChatGPT, Claude, and Perplexity read your website content cleanly. Learn what they are and why every business needs them.
url: https://www.brycenwood.com/guides/markdown-mirrors/
last_updated: 2026-04-14
---

Free Guide
 
# Your Website Is Invisible to ChatGPT

 AI can't read your fancy HTML. Markdown mirrors fix that. Here's what they are and why they matter.

 Last updated: April 2026

## The Problem: AI Can't Read Your Website

Your website looks great to humans. The colors are right, the fonts are clean, the navigation works, the images load. A person lands on your services page and knows exactly what you do within 5 seconds.

AI tools don't see any of that.

When ChatGPT, Claude, or Perplexity tries to read your website, it doesn't see a beautiful page. It sees raw HTML -- thousands of lines of code that include your navigation menu, footer links, cookie consent banner, analytics scripts, social media widgets, JavaScript bundles, CSS class names, and somewhere buried in the middle of all that noise, your actual content.

The AI has to parse through all of it to find the signal. And most of the time, it fails. Not because it's dumb, but because your page was built for human eyes, not machine readers.

I tested this with my own company. When I asked ChatGPT to read the Summit Wraps services page, it pulled in navigation links, footer text, cookie consent copy, and JavaScript function names -- all mixed in with our actual service descriptions. The AI couldn't tell what was important and what was scaffolding. The result was a garbled mess that barely resembled our actual offering.

That's the problem. Your website is functionally invisible to the AI tools that are increasingly deciding which businesses to recommend.

## What Are Markdown Mirrors?

A markdown mirror is a clean, plain-text version of each page on your website. For every `index.html` on your site, you create an `index.md` right next to it. The `.md` file contains just the content -- no navigation, no scripts, no styling, no cookie banners. Just the information that matters.

Here's what that looks like in practice:

```
your-website.com/services/index.html -- humans read this
your-website.com/services/index.md -- AI reads this

your-website.com/about/index.html -- humans read this
your-website.com/about/index.md -- AI reads this

your-website.com/faq/index.html -- humans read this
your-website.com/faq/index.md -- AI reads this
```

When an AI tool fetches your page, it can request the `.md` version instead of the `.html` version and get exactly the information it needs, cleanly formatted, with zero noise.

The name "mirror" is the key concept. The markdown file mirrors the content of the HTML page. Same information, different format. Humans get the pretty version. Machines get the clean version. Everyone wins.

## Why Markdown Specifically?

AI language models are trained on text. Massive amounts of text. And the format they understand best -- after raw plain text -- is markdown.

Markdown gives you structure without bloat. Headings, lists, links, bold text, code blocks -- all the formatting you need to organize information, with zero overhead. No opening and closing tags. No class names. No nesting nightmares. Just clean, readable text with lightweight formatting.

When you give an AI a clean markdown file instead of an HTML page, it can:

- **Understand your page hierarchy** -- headings tell the AI what's a main topic vs. a subtopic
- **Quote your content accurately** -- no risk of grabbing your footer text or nav menu
- **Recommend your services with the right details** -- service descriptions come through clean
- **Compare you to competitors using real information** -- structured content beats garbled HTML
- **Answer follow-up questions** -- FAQ sections in markdown are trivially easy for AI to parse

HTML was designed for browsers to render visually. Markdown was designed for machines and humans to read as text. For the job of communicating with AI, markdown is the better tool by a mile.

## How Markdown Mirrors Work with llms.txt

If you've already read the [llms.txt guide](/guides/llms-txt/), you know that llms.txt is a site-level summary -- a single file that tells AI what your business does at a high level.

Markdown mirrors go deeper. They give the AI full access to every page's content, not just a summary.

Here's how to think about the relationship:

- **llms.txt** = the executive summary. "Here's who we are, here's what we do, here are our pages."
- **Markdown mirrors** = the full documentation. "Here's everything on each page, in detail."
- **Schema markup** = the structured data layer. Machine-readable facts about your business entity.

Together, these three layers form the AI Visibility Stack. llms.txt gets you in the door. Markdown mirrors give the AI the depth it needs to recommend you confidently and accurately. Schema markup provides the structured metadata that ties it all together.

I built all three for [Summit Wraps](/case-studies/summit-wraps/) and the compound effect was what made ChatGPT start recommending us to real customers. The full system is covered in the [AI SEO Playbook guide](/guides/ai-seo-playbook/).

## What Goes in a Markdown Mirror

Each `.md` file should be a clean representation of its corresponding HTML page. Not a rewrite -- a mirror. Same content, stripped down to pure text and markdown formatting.

**Include:**

- Page title as an H1 heading
- All section headings (H2, H3) that structure the page
- All paragraph content -- service descriptions, about text, any prose on the page
- Lists of services, features, benefits
- FAQ questions and answers
- Links to related pages on your site
- Contact information if it appears on the page

**Do NOT include:**

- Navigation menus
- Footer content
- Cookie consent banners
- JavaScript or tracking code
- Social media widget embeds
- Image alt text (unless it contains important content)
- CSS class names or HTML attributes
- Call-to-action buttons (the AI doesn't need to know about your button styling)

Here's an example of what a markdown mirror looks like for a services page:

```
# Vehicle Wrap Services — Summit Wraps

Summit Wraps offers full-service vehicle wrapping, fleet
graphics, and commercial branding in Utah. We serve
businesses across Salt Lake County, Utah County, and the
Wasatch Front from our two locations in Springville and Lehi.

## Full Vehicle Wraps
Complete color-change wraps for cars, trucks, vans, and SUVs.
Premium 3M and Avery vinyl with a 5-year warranty.
Typical turnaround: 3-5 business days.

## Commercial Fleet Graphics
Custom branding for business fleets of any size. Consistent
branding across all vehicles. Volume pricing available for
fleets of 5+ vehicles.

## Partial Wraps and Decals
Logos, lettering, and partial coverage options for businesses
that want visibility without a full wrap.

## FAQ
**How long does a full wrap last?**
5-7 years with proper care. We use premium 3M and Avery
materials with manufacturer warranties.

**Do you offer design services?**
Yes. Our in-house design team creates custom wrap designs
from scratch. Design is included with every full wrap order.
```

Clean. Readable. No noise. The AI can consume this in one pass and know exactly what the page is about.

 
 Inside the Community
 Get the Auto-Generator Script
 The Python script that automatically generates markdown mirrors for your entire website, plus the exact server config to serve them correctly. All inside the free community.

 [Join the Free Community](/community/)
 

## The Technical Setup

There are two things you need to get markdown mirrors working:

### 1. Create the Markdown Files

You need an `index.md` file next to every `index.html` on your site. You can create these manually for a small site, or use a script to generate them automatically for a larger one.

For Summit Wraps, I built a Python script that walks every page on the site, strips out the HTML scaffolding, and generates clean markdown. 27 pages, 27 mirrors, done in about 10 seconds. The script is inside the community for anyone who wants it.

If your site has fewer than 10 pages, you can honestly just write them by hand. Open each page in your browser, copy the content, paste it into a text file, add markdown formatting, save as `index.md`. 5-10 minutes per page.

### 2. Configure Your Server

This is the part most people miss. Your web server needs to serve `.md` files as plain text so browsers and AI tools render them inline instead of forcing a download.

The configuration depends on your hosting platform:

**Netlify / Cloudflare Pages** -- add a `_headers` file to your build root:

```
/*.md
 Content-Type: text/plain; charset=utf-8
 Cache-Control: public, max-age=3600
 X-Robots-Tag: index, follow
```

**Vercel** -- add to your `vercel.json`:

```
{
 "headers": [
 {
 "source": "/(.*).md",
 "headers": [
 { "key": "Content-Type", "value": "text/plain; charset=utf-8" },
 { "key": "X-Robots-Tag", "value": "index, follow" }
 ]
 }
 ]
}
```

**Apache** -- add to your `.htaccess`:

```
AddType text/plain .md
```

The `X-Robots-Tag: index, follow` header is important. It tells search engines that these files are meant to be indexed and that their links should be followed. Without it, some crawlers might skip your markdown mirrors entirely.

## How AI Tools Discover Your Mirrors

You might be wondering: "How does ChatGPT know to look for the `.md` version of my page?"

Two ways:

**Through llms.txt.** Your llms.txt file links to all your pages. Smart AI crawlers will check for both the `.html` and `.md` versions of every URL they find. If they see a clean markdown version available, they'll use it.

**Through direct discovery.** AI tools are getting better at checking for alternative content formats. When they encounter a page that's hard to parse, they'll look for simpler versions -- including `.md` files in the same directory.

You can also reference your mirrors directly in llms.txt. Instead of linking to `/services/`, link to `/services/index.md`. That guarantees the AI reads the clean version.

## Real Results from Summit Wraps

 
 27
 Mirrors Created
 
 
 28K
 Video Views (20h)
 
 
 14.5%
 Comment Rate
 

After deploying 27 markdown mirrors across the entire Summit Wraps website:

- AI tools could read every page cleanly in a single fetch -- no more garbled HTML mixed with content
- Combined with llms.txt, this is what triggered ChatGPT to start recommending Summit Wraps to real customers asking about vehicle wraps in Utah
- The video explaining this concept hit 28K views in 20 hours with a 14.5% comment rate and a 10% save rate -- both in the top percentile for any business content on Instagram
- The concept resonated because it's something anyone can do, it takes minimal time, and the results are immediate

The most important result isn't the video views. It's that our competitors still haven't done this. Their websites are still invisible to AI tools. Ours isn't. That gap compounds every single day.

## Common Questions People Ask After Setting This Up

**"Should the markdown file be an exact copy of the HTML content?"**

As close as possible. The content should match -- same headings, same descriptions, same facts. You're not rewriting anything, you're reformatting. The only things you strip out are the non-content elements: navigation, footer, scripts, widgets.

**"What about blog posts? Do they need mirrors too?"**

Yes, especially if your blog posts contain valuable information about your business. Blog posts are often the highest-word-count pages on your site, which means they give AI the most material to work with. Mirror them.

**"Can I add extra information to the markdown that isn't on the HTML page?"**

You can, but be careful. If the information on your `.md` version contradicts or significantly differs from your `.html` version, AI tools might flag the inconsistency and trust neither. Keep them in sync. If you want to add more detail, add it to both versions.

**"What about dynamic content -- like product listings that change?"**

For pages with frequently changing content, you have two choices: regenerate the mirrors on a schedule (daily, weekly) or only mirror your static pages and skip the dynamic ones. Most businesses have 10-30 static pages that matter for AI visibility. Focus on those first.

## What Comes Next

Markdown mirrors are the second layer of the AI Visibility Stack. If you haven't set up [llms.txt](/guides/llms-txt/) yet, start there -- it's faster and gives you immediate results.

Once both are live, the [AI SEO Playbook](/guides/ai-seo-playbook/) covers the third layer (schema markup) and how all three work together to create a compound effect that's hard for competitors to replicate.

If you want to see the complete transformation -- from zero AI visibility to ChatGPT recommending the business -- the [Summit Wraps case study](/case-studies/summit-wraps/) shows exactly how it played out.

 
 
## Frequently Asked Questions

 
 
 
 Do I need markdown mirrors if I already have llms.txt?+
 
 Yes -- they serve different purposes. llms.txt is a site-level summary that tells AI what your business does at a high level. Markdown mirrors let AI read the full content of every individual page. Think of llms.txt as the table of contents and markdown mirrors as the actual chapters.

 
 
 
 Can I generate these automatically?+
 
 Yes. I built a Python script that walks your entire website and generates .md files for every page. It strips out HTML scaffolding, preserves content, and outputs clean markdown. The script and step-by-step walkthrough are available inside the free community.

 
 
 
 Will this hurt my regular SEO?+
 
 No. The .md files are separate from your HTML pages. Google continues to index your HTML pages normally. Markdown mirrors are an addition to your site, not a replacement for anything. They give AI tools a clean reading path without affecting your existing search rankings.

 
 
 
 How many markdown mirrors do I need?+
 
 One for every content page on your site -- services pages, about page, FAQ, location pages, blog posts. Skip pages that are purely functional like login, cart, or checkout. For Summit Wraps, that was 27 mirrors across all pages.

 
 
 

 
 
## Make Your Website Visible to AI

 Get the auto-generator script, server configs, and step-by-step walkthroughs inside the free community. Or book a call and I'll build the whole AI visibility stack for your business.

 
 [Join the Free Community](/community/)
 [Book a Discovery Call](/contact/)
