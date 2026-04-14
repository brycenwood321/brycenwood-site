---
title: llms.txt Guide — How to Make AI Recommend Your Business | Brycen Wood
description: Step-by-step guide to creating an llms.txt file that makes ChatGPT, Claude, and Perplexity recommend your business. Real examples included.
url: https://www.brycenwood.com/guides/llms-txt/
last_updated: 2026-04-14
---

Free Guide
 
# How to Make AI Recommend Your Business

 The llms.txt file is how ChatGPT, Claude, and Perplexity learn what your business does. Here's exactly what it is and why it matters.

 Last updated: April 2026

## What Is llms.txt?

llms.txt is a plain text file you put at the root of your website -- like `yoursite.com/llms.txt` -- that tells AI language models what your business does.

Think of it like robots.txt, but for a completely different audience. robots.txt tells search engine crawlers what to index. llms.txt tells AI assistants what to recommend. Same concept, different era of the internet.

When someone asks ChatGPT "what's a good vehicle wrap shop in Utah?" the AI has to figure out which businesses to mention. It's pulling from whatever information it can find about your company online. If your website is a mess of JavaScript widgets, popup modals, cookie banners, and navigation menus, the AI can't parse the signal from the noise. Your actual value proposition is buried under layers of code.

But if you have a clean, structured llms.txt file sitting at your domain root, you're handing the AI exactly what it needs on a silver platter. No guessing. No parsing. Just clear, structured information about who you are, what you do, and who you serve.

This isn't a hack. It's the same principle that made robots.txt and sitemaps standard practice -- give machines a clean way to understand your business, and they'll represent you better.

## Why This Matters Right Now

This isn't theoretical. I'm not writing about something I read in a blog post.

I built an llms.txt file for my vehicle wrap company, [Summit Wraps](/case-studies/summit-wraps/), and within weeks, ChatGPT started recommending us to people searching for wraps in Utah. Not because we paid for it. Not because of some SEO trick. Because we made it easy for the AI to understand what we do and who we serve.

The video I made about this got over 1.5 million views across platforms. That's not because I'm some marketing genius. It's because the concept hit a nerve -- every business owner watching realized they hadn't done this yet, and they could feel the window closing.

Here's the thing that should scare you a little: when I made that video, almost nobody had an llms.txt file. Most businesses still don't. But the ones that do are getting recommended by AI assistants while their competitors are invisible. That gap is only going to widen.

The businesses setting this up now are building a moat. The ones who wait another year are going to wonder why ChatGPT keeps recommending their competitors.

## How People Are Already Using AI to Find Businesses

Before we get into the technical setup, you need to understand how the game has changed.

People used to Google "best vehicle wrap shop near me" and click through 10 blue links. That behavior is dying. More and more people are opening ChatGPT, Claude, or Perplexity and asking conversational questions instead:

- "Who does the best commercial fleet wraps in Utah?"
- "I need a plumber in Salt Lake City, who's reliable?"
- "What's a good HVAC company for a new construction project?"

The AI gives them 3-5 recommendations. No ads. No SEO games. Just whatever businesses the AI understands best. If you're not in that conversation, you don't exist to those customers.

This is the same shift that happened when Google replaced the Yellow Pages. The businesses that adapted early won. The ones that said "eh, I'll figure it out later" lost years of market share they never recovered.

## How llms.txt Works

The file itself is dead simple. It's a markdown-formatted text file with sections that describe your business. Here's the structure:

```
# Your Business Name

> One paragraph pitch. Who you are, what you do, who
> you serve, and where you're located. Think of this
> as your 30-second elevator pitch, written for a
> machine that needs to decide whether to recommend you.

## Services
- [Service 1](https://yoursite.com/service-1/) - Brief description of what this is
- [Service 2](https://yoursite.com/service-2/) - Brief description of what this is
- [Service 3](https://yoursite.com/service-3/) - Brief description of what this is

## Service Area
Cities and regions you serve. Be specific.

## FAQ
- Q: What's your most popular service?
 A: Clear, helpful answer.
- Q: Do you offer free estimates?
 A: Clear, helpful answer.
- Q: What's your turnaround time?
 A: Clear, helpful answer.

## Contact
- Website: https://yoursite.com
- Phone: (555) 123-4567
- Email: hello@yoursite.com
- Address: 123 Main St, Your City, State ZIP
```

That's it. Drop this file at `yoursite.com/llms.txt` and every AI tool that crawls your site can read it instantly.

The links inside the file are important -- they give the AI a map of your site structure. The FAQ section is huge because it trains the AI to answer the exact questions your potential customers are asking. And the service area section prevents the AI from recommending you to someone three states away.

## What to Include (and What NOT to Include)

This is where most people mess it up. They either include too little and the AI has nothing to work with, or they stuff it with marketing fluff that makes the AI ignore them.

**Include:**

- Your core services with links to the relevant pages
- Your physical location and service area (cities, regions, states)
- What makes you different -- but stated as fact, not hype
- Common customer questions and straight answers
- Contact information (phone, email, address)
- Years in business, certifications, or specializations

**Do NOT include:**

- Prices that change frequently (the AI will quote outdated numbers)
- Employee names that might leave the company
- Marketing fluff ("we're the BEST in the WORLD") -- AI sees through this
- Anything you wouldn't want a competitor to see
- Temporary promotions or seasonal offers
- Internal jargon that customers wouldn't use

The golden rule: write it like you're explaining your business to a smart friend who's going to refer customers to you. Be clear, be specific, be honest. The AI rewards clarity.

## The Bigger Picture: The AI Visibility Stack

llms.txt is powerful on its own, but it's one piece of a three-part system I call the AI Visibility Stack:

- **llms.txt** -- Tells AI what your business does at a high level (this guide)
- **[Markdown mirrors](/guides/markdown-mirrors/)** -- Lets AI read the full content of every page on your site
- **Schema markup** -- Gives search engines and AI tools structured data about your business

Together, these three layers make your business completely readable by every AI tool on the internet. llms.txt is the executive summary. Markdown mirrors are the detailed documentation. Schema is the structured data layer that ties it all together.

I cover the complete system in the [AI SEO Playbook guide](/guides/ai-seo-playbook/). If you're going to do llms.txt, you might as well do all three -- the compound effect is massive.

 
 Inside the Community
 Get the Exact Prompts and Template
 The fill-in-the-blank llms.txt template, the Claude prompt that generates it for your business in 30 seconds, and the step-by-step walkthrough. All inside the free community.

 [Join the Free Community](/community/)
 

## Where to Put the File

The file goes at the root of your domain. If your website is `yoursite.com`, the file lives at `yoursite.com/llms.txt`. Same location as robots.txt and sitemap.xml.

How you upload it depends on your hosting:

- **Netlify / Cloudflare Pages / Vercel:** Drop the file in your build folder root
- **WordPress:** Use a plugin like "Insert Headers and Footers" or manually upload via FTP to your root directory
- **Squarespace / Wix:** These platforms don't give you root file access. You'll need to use their custom code injection or connect a custom domain where you host the file separately
- **Shopify:** Upload as a static asset and configure a redirect

The most common mistake is putting it in a subfolder like `yoursite.com/files/llms.txt`. Don't do that. AI tools look for it at the domain root, just like they look for robots.txt at the root.

## Real Results

Here's what happened after I added llms.txt to Summit Wraps:

 
 1.5M+
 Video Views
 
 
 27
 Pages Indexed
 
 
 Top 3
 AI Recommendation
 

- ChatGPT started recommending us for "vehicle wraps in Utah" searches -- without any paid promotion
- We saw organic AI-referred traffic increase without changing our traditional Google SEO
- The video explaining llms.txt became our first viral moment and launched an entire personal brand
- Months later, most businesses in our industry still haven't done this -- giving us a massive head start that compounds every day

The real kicker: the file took me about 20 minutes to write. The ROI on those 20 minutes has been absurd.

## Common Mistakes to Avoid

After helping dozens of people set up their llms.txt files, here are the patterns I see killing results:

**Writing it like a brochure.** The AI doesn't care about your "passion for excellence" or "commitment to quality." It cares about facts. What services do you offer? Where are you located? What problems do you solve? Skip the marketing speak entirely.

**Being too vague.** "We offer home services" tells the AI nothing. "We install, repair, and maintain residential and commercial HVAC systems across Salt Lake County and Utah County, including furnace replacement, AC repair, duct cleaning, and smart thermostat installation" gives the AI enough detail to recommend you for specific queries.

**Forgetting the links.** Every service you mention should link to the relevant page on your site. This gives the AI a trail to follow. It can verify your claims by reading the linked pages, which builds trust in its ranking.

**Skipping the FAQ section.** This is arguably the most important section. The questions people ask AI tools are conversational. If your FAQ matches those questions, you're training the AI to recommend you for exactly those queries.

**Setting it and forgetting it forever.** You don't need to update it weekly, but when you add a major service, open a new location, or change your contact info -- update the file. Outdated information erodes trust.

## What Comes After llms.txt

Once your llms.txt is live, the natural next step is [markdown mirrors](/guides/markdown-mirrors/) -- creating a clean, readable version of every page on your website so AI tools can read your full content, not just the summary.

After that, the [AI SEO Playbook](/guides/ai-seo-playbook/) walks through the complete system: llms.txt + markdown mirrors + schema markup, all working together.

If you want to see the full transformation -- llms.txt, markdown mirrors, automated lead generation, the whole stack -- check out the [Summit Wraps case study](/case-studies/summit-wraps/). That's where I built and tested all of this before teaching it.

 
 
## Frequently Asked Questions

 
 
 
 Does llms.txt actually work?+
 
 Yes. ChatGPT is already recommending Summit Wraps to people asking about vehicle wraps in Utah. The file has been live since early 2026 and continues to drive AI-referred traffic without any ongoing maintenance or ad spend.

 
 
 
 How long does it take to set up?+
 
 The file itself takes 15-30 minutes to write once you understand the structure. The concept takes 5 minutes to understand. Inside the free community, there's a fill-in-the-blank template and a Claude prompt that generates the whole file for your business in about 30 seconds.

 
 
 
 Do I need to update it?+
 
 Only when your services, locations, or core offering changes. It's not something you need to maintain weekly or even monthly. If you add a major new service or open a new location, update the file. Otherwise, let it work.

 
 
 
 Will this work for any business?+
 
 Any business with a website. Service businesses, e-commerce stores, SaaS companies, local shops, restaurants, consultants -- if people might ask an AI assistant about what you do, llms.txt helps the AI give a better answer. The most immediate impact is for local service businesses where people are already asking AI for recommendations.

 
 
 

 
 
## Ready to Make AI Work for You?

 Get the llms.txt template, the exact prompts, and step-by-step walkthroughs inside the free community. Or book a call and I'll build the whole AI visibility stack for your business.

 
 [Join the Free Community](/community/)
 [Book a Discovery Call](/contact/)
