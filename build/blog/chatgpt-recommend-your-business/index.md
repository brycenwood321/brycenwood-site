---
title: How I Made ChatGPT Recommend My Business (With Screenshots) | Brycen Wood
description: ChatGPT is recommending my vehicle wrap company to real customers in Utah. Here's the exact 3-file setup I used, with proof screenshots.
url: https://www.brycenwood.com/blog/chatgpt-recommend-your-business/
last_updated: 2026-04-14
---

Blog
 
# How I Made ChatGPT Recommend My Business

 I asked ChatGPT for vehicle wrap shops in Utah. My company showed up. Here is exactly how.

 Last updated: April 2026

 BW
 
 [Brycen Wood](/about/)
 Business Automation Consultant -- Built 80+ systems with zero coding experience
 

> **Key Takeaway:** Three files -- llms.txt, markdown mirrors, and structured schema -- make your website readable by AI tools. I added them to my vehicle wrap company's site. ChatGPT now recommends us by name when customers ask for wrap shops in Utah. This is not SEO. This is a different channel entirely, and almost nobody is using it yet.

## The Screenshot That Changed Everything

In late March 2026, I opened ChatGPT and typed a simple question: "What are the best vehicle wrap shops in Utah?"

I was not expecting what came back.

ChatGPT returned a list of five businesses. Summit Wraps and Graphics -- my company, the one I co-own with my partner Landon in Springville, Utah -- was on the list. It wasn't just mentioned in passing. ChatGPT described our services, mentioned our locations, and gave specific reasons why we were a good fit for different types of customers.

This was not a paid ad. We did not submit an application. We did not pay a platform fee. ChatGPT recommended us because it could read our website and understand what we do. And the reason it could read our website is because I had deliberately set it up to be machine-readable using three specific files.

That screenshot became the basis for a video that resonated hard with business owners. But the screenshot is not the point. The point is that ChatGPT, Claude, Perplexity, and every other AI assistant are becoming the new front door for customer discovery. And most businesses have no idea this is happening.

## Why AI Tools Can't Read Most Websites

Here is the fundamental problem. Your website was built for humans and for Google. The HTML, the CSS, the JavaScript, the images, the animations -- all of it is designed to look good in a browser and rank well in search results. But when an AI tool tries to read your site, it hits a wall of markup.

Think about what your homepage looks like under the hood. There are hundreds of lines of navigation code, footer code, stylesheet references, tracking scripts, cookie banners, and layout divs before the AI ever gets to a sentence about what you actually do. The content is buried inside a structure that was designed for visual rendering, not comprehension.

Google figured this out decades ago with sitemaps and meta tags. Google's crawler knows how to parse HTML and extract meaning. But AI language models work differently. They perform best when content is delivered in clean, structured, plain-text formats. When you give ChatGPT a messy HTML page, it can extract some meaning, but it misses context, misinterprets structure, and often skips content that is hidden behind JavaScript rendering.

This is why most businesses are invisible to AI. Their content exists, but it is locked inside a format that AI tools struggle to parse efficiently. The 3-file system solves this problem completely.

## File 1: llms.txt -- Your Business Card for AI

The first file is called `llms.txt`. It lives at your domain root -- like `yoursite.com/llms.txt` -- and it serves as a structured introduction to your business specifically for AI tools.

Think of it like a robots.txt file, but instead of telling search crawlers which pages to index, it tells AI tools who you are, what you do, where you are located, what makes you different, and how to learn more.

The format is simple. Plain text. Clear headings. Structured information. No HTML, no styling, no JavaScript. Just the facts about your business laid out in a way that any language model can parse in milliseconds.

For Summit Wraps, our llms.txt includes our business name, both locations (Springville and Lehi), the specific services we offer (full wraps, partial wraps, fleet branding, PPF, tint), our target market (commercial fleet operators, small businesses, individuals), what makes us different (in-house design, free consultations, dual-location coverage), and links to every important page on our site.

When ChatGPT encounters this file, it gets a perfect summary of our business without having to crawl through 27 pages of HTML to piece it together. That efficiency translates directly into recommendation quality. The AI can confidently describe who we are and why we might be the right fit for a specific customer.

The deep dive on llms.txt, including the exact format and a template you can copy, is in our [llms.txt guide](/guides/llms-txt/).

## File 2: Markdown Mirrors -- Clean Content for Every Page

The second file type is what I call markdown mirrors. For every HTML page on your site, you create a corresponding `.md` file that contains the same content in clean, structured markdown format.

So if you have a page at `yoursite.com/services/`, you also create `yoursite.com/services/index.md`. The HTML version is what humans see in their browser. The markdown version is what AI tools read when they want to understand that page's content.

Why markdown specifically? Because it is the native language of AI comprehension. Large language models were trained on billions of pages of markdown documentation, README files, and structured text. When you give an AI tool markdown, it processes it with near-perfect accuracy. When you give it HTML, it has to do translation work -- stripping tags, inferring structure, guessing what is content versus what is layout -- and that translation introduces errors.

For Summit Wraps, I built a Python script that generates markdown mirrors for all 27 pages automatically. Each mirror contains the page title, a meta description, and the full content of the page in clean markdown with proper headings, lists, and links. The script runs in about 15 seconds and the mirrors are deployed alongside the HTML pages.

The result: when ChatGPT browses our fleet wraps page, it can read the markdown mirror and get perfect comprehension of our fleet branding services, pricing context, portfolio references, and contact information. No HTML wrestling. No missed content. No misinterpretation.

I filmed a side-by-side comparison showing the same page in HTML versus markdown and the difference in AI comprehension quality was dramatic. That video hit 28,000 views in 20 hours. The full guide on setting up markdown mirrors is at [our markdown mirrors guide](/guides/markdown-mirrors/).

## File 3: Structured Schema -- The Metadata Layer

The third component is structured schema markup. This is JSON-LD code embedded in your page headers that tells both search engines and AI tools exactly what type of content is on each page and how it relates to your business.

Schema markup is not new -- Google has supported it for years. But most small businesses either don't have it at all or have a bare-minimum implementation that covers the basics (business name, address, phone number) without going deeper.

The schema that makes AI recommendations work goes further. It includes `LocalBusiness` schema with your full service area, `Service` schema for each offering with descriptions and price ranges, `Review` schema that surfaces your best customer testimonials, `FAQPage` schema that answers common questions directly in the markup, and `Article` schema for your blog content that establishes topical authority.

When all three files work together -- llms.txt providing the business overview, markdown mirrors providing page-level content, and schema providing structured metadata -- AI tools get a complete, multi-layered understanding of your business. That depth of understanding is what drives confident recommendations.

## The Results: What Happened After Implementation

Let me share the real numbers, because this is where it gets interesting.

Before adding the 3-file system, Summit Wraps was invisible to AI tools. I tested ChatGPT, Claude, Perplexity, and Gemini with various Utah vehicle wrap queries. We appeared in zero recommendations.

Within two weeks of deploying llms.txt, markdown mirrors, and enhanced schema markup, Summit Wraps began appearing in ChatGPT recommendations for queries like "best vehicle wrap shop in Utah," "commercial fleet wraps Salt Lake City," and "vehicle branding near Provo." We now appear consistently across multiple AI platforms for service-relevant queries.

The traffic impact was also measurable. Our website saw a 2,100% increase in organic traffic after the full SEO and AI optimization push. Not all of that is attributable to the 3-file system alone -- we also rewrote meta titles, added FAQ content, and improved site structure -- but the AI recommendation channel brought visitors who were significantly more qualified than typical organic search traffic. These were people who had already been told by a trusted AI assistant that we were a good fit. The conversion intent was higher from the first click.

The videos documenting this process -- the llms.txt video and the markdown mirrors video -- generated thousands of comments from business owners asking how to implement it. That tells me something important: business owners are hungry for this information. They know AI is changing how customers find businesses, but nobody is showing them the specific tactical steps to prepare for it.

## Why Almost Nobody Is Doing This Yet

The opportunity right now is enormous specifically because almost nobody has caught on. I ran an informal audit of 200 businesses in the home services space in Utah -- roofers, HVAC companies, plumbers, landscapers. Zero had llms.txt files. Zero had markdown mirrors. Fewer than 10% had schema markup beyond the bare minimum Google My Business data.

This means the bar for standing out in AI recommendations is incredibly low. You don't need to be the best business in your market. You just need to be the most readable one. When a customer asks ChatGPT for a recommendation and only two businesses in your area have machine-readable content, those two businesses get the recommendation regardless of how many competitors exist.

This will not last forever. As awareness grows, more businesses will implement these files and the competitive advantage will diminish. But right now, in April 2026, we are in the earliest days of AI-driven customer discovery. The businesses that move first will build an AI presence that compounds over time -- just like early SEO adopters built Google authority that new entrants still struggle to match decades later.

## The Difference Between This and Traditional SEO

I want to be explicit about what this is and what it is not, because the distinction matters.

Traditional SEO is about ranking on Google. You optimize for keywords, build backlinks, improve page speed, and compete for one of ten positions on a search results page. It works. It is still valuable. I do it for Summit Wraps and recommend it to every business owner.

AI optimization is a different channel entirely. When someone uses ChatGPT or Claude to find a service provider, there is no results page. The AI gives a direct recommendation -- usually one to three businesses with explanations for why each is a good fit. There is no position four. You are either recommended or you are not.

The economics are radically different. In Google SEO, ranking #3 still gets you traffic. In AI recommendations, being the single named recommendation is worth orders of magnitude more than being one of ten search results. The click-through rate on a personalized AI recommendation is functionally 100% -- the user was looking for a recommendation and received one. Compare that to a 3-8% click-through rate on a top-three Google result.

Both channels matter. Both should be optimized. But AI optimization is where the asymmetric opportunity exists right now because competition is virtually nonexistent. You can build a dominant AI presence in your market this week with a few hours of work. Building a dominant Google presence takes months or years.

## What You Need to Do Next

The 3-file system is deliberately simple. I am not a developer. I built all of this using Claude Code -- an AI assistant that writes code based on plain English descriptions. If you can describe your business, you can implement this.

The two detailed guides cover each file type in depth:

- [How to Create an llms.txt File](/guides/llms-txt/) -- the complete walkthrough with templates, formatting rules, and examples from multiple industries.
- [How to Build Markdown Mirrors](/guides/markdown-mirrors/) -- the step-by-step process for creating markdown versions of your site pages, including the automated script approach I used.

Both guides show you the WHAT and the WHY in full detail. For the exact prompts, templates, and build-along walkthroughs, those are inside the [founding member community](/community/) where local service business owners are implementing these systems together.

The window of opportunity is open right now. Every week that passes, more businesses will discover this channel and the first-mover advantage shrinks. The businesses that implement the 3-file system this month will have months of AI recommendation history building in their favor before the majority catches on.

I know this because I watched it happen with Google SEO twenty years ago. The businesses that built authority early still dominate. The same pattern is starting right now with AI, and the cost of entry is three text files and a few hours of work.

 
 Inside the Community
 Get the Exact Prompts and Templates
 The llms.txt template, the markdown mirror generator script, the schema snippets -- everything you need to make AI recommend your business. Free to join.

 [Get Founding Access -- $97/mo](/community/)
 

## What Comes After the 3-File System

The 3-file system is the foundation. Once your business is readable by AI, there are several ways to extend your presence and increase the frequency and quality of recommendations.

First, content depth matters. AI tools recommend businesses they understand deeply. The more substantive content you have on your site -- service pages, case studies, FAQs, educational blog posts -- the more context the AI has to draw from when making recommendations. A business with 5 pages and an llms.txt file will get recommended. A business with 30 pages of detailed content plus the 3-file system will get recommended more often and with more specific, compelling descriptions.

Second, freshness signals matter. AI tools are increasingly able to detect when content was last updated. A site that was built three years ago and never touched sends a different signal than a site that publishes new content regularly. Blog posts, case study updates, and portfolio additions all contribute to a freshness signal that AI tools factor into recommendation confidence.

Third, cross-platform presence amplifies AI recommendations. When your business shows up not only on your website but also in social media content, YouTube videos, directory listings, and review platforms -- all saying consistent things about who you are and what you do -- AI tools build higher confidence in their recommendation. The Summit Wraps system includes automated cross-posting to YouTube and structured social media content specifically to build this cross-platform consistency.

Every one of these extensions is something I built for Summit Wraps using Claude Code. Every one of them is documented inside the community. And every one of them starts with the same foundation: making your business readable by AI through the 3-file system.

 
 
## Frequently Asked Questions

 
 
 
 Does ChatGPT actually recommend specific businesses to users?+
 
 Yes, and it is happening right now. When someone asks ChatGPT for a recommendation -- "best vehicle wrap shop in Utah," "plumber near Salt Lake City," "web designer in Denver" -- ChatGPT does not randomly guess. It pulls from content it has been trained on and content it can access through browsing. If your business has structured, machine-readable content on your website, you are exponentially more likely to appear in those recommendations. I have screenshots of ChatGPT recommending Summit Wraps by name, with our address, services, and even reasons why we are a good fit. This is not theoretical. It is happening to real customers searching for real services, and most businesses have no idea it is even a channel.

 
 
 
 How long does it take to set up llms.txt and markdown mirrors?+
 
 If you are doing it manually, setting up an llms.txt file takes about 30 minutes. You write a structured summary of your business -- name, location, services, unique selling points -- and save it as a plain text file at your domain root (yoursite.com/llms.txt). Markdown mirrors take longer because you need one for each page on your site, but the process is straightforward: create a clean markdown version of each page's content and serve it alongside the HTML. For Summit Wraps, I built a Python script that generates all 27 markdown mirrors automatically in about 15 seconds. If you are using Claude Code, you can describe what you want and have the entire setup -- llms.txt, mirrors, and schema -- built in a single session. The deep-dive guides for each file walk through every step: llms.txt guide at /guides/llms-txt/ and markdown mirrors guide at /guides/markdown-mirrors/.

 
 
 
 Will this work for any type of business?+
 
 Yes, with one caveat: your business needs a website with real content. The 3-file system works for service businesses, local shops, e-commerce stores, SaaS companies, consultants, freelancers -- any business that has a web presence and wants AI tools to understand and recommend it. The key is that your content must be substantive. A one-page site with nothing but a logo and a phone number will not generate AI recommendations regardless of what files you add. AI tools recommend businesses they can understand deeply, which means your site needs detailed service descriptions, location information, pricing context, and proof of quality. The 3-file system makes that existing content machine-readable. It does not replace the need for good content -- it makes good content discoverable by AI.

 
 
 
 Is this the same as traditional SEO?+
 
 No, and this distinction matters. Traditional SEO optimizes your website for Google's search crawler -- you are competing for position on a results page with ten blue links. AI optimization makes your content readable by large language models like ChatGPT, Claude, Perplexity, and Gemini. These AI tools do not show a list of results. They give a direct recommendation, often naming one or two businesses. That means the upside of being recommended by AI is dramatically higher than ranking on page one of Google -- there is no position two. The tactics are also different. Google cares about backlinks, page speed, and keyword density. AI tools care about structured content, clear descriptions, and machine-readable formats like llms.txt and markdown. The good news is that both strategies are complementary. But the 3-file system specifically targets AI recommendation engines in a way that traditional SEO does not.

 
 
 

 
 
## Ready to Make AI Recommend Your Business?

 Get founding access alongside local service business owners building AI-readable websites. Or book a discovery call to get your entire operating system built in 2 weeks.

 
 [Get Founding Access -- $97/mo](/community/)
 [Book a Discovery Call](/contact/)
