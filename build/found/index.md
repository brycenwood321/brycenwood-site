---
title: Get Found by ChatGPT: The Three Checks | Brycen Wood
description: Ask ChatGPT who the best is in your city. If it does not say your name, three things on your website fix it: a sitemap, your business as data, and a file that tells AI what you do. Explained in plain English, plus one prompt that sets up all three.
url: https://www.brycenwood.com/found/
last_updated: 2026-04-14
---

From the video · Free

 
# Ask ChatGPT who the best is in your city. Then make it say your name.

 ChatGPT has named my wrap shop when asked for the best in American Fork, Utah, and some days it does not. The answer changes from one ask to the next. These three things on your website are the part you control, and I do not know which one matters most, so do all three. Each one explained in plain English, then one prompt that sets all three up for you. Drop your email below and it unlocks. Nothing to buy.

 
 [Unlock the three + the prompt](#get)
 
 Here from the ChatGPT Business Hub video? The same email unlocks every step and the fine print, at the bottom of this page.

 
 
 What&rsquo;s inside

 
## The three checks, one breath each

 
 
 01**A sitemap** · A plain list of every page on your site, so AI and Google can find all of it instead of guessing.
 02**Your business as data** · Your name, address, phone, hours and services written in the format machines read, not just words on the page.
 03**A file that tells AI what you do** · One plain-English page at your site&rsquo;s address that answers who you are, what you do and where.
 
 The full explanation of each one, how to check whether you already have it, and one prompt that sets up all three. Unlocked by the form below.

 

 
 
 Get the three checks + the prompt
 Enter your email and this page unlocks immediately. Just this one, not all of them.
 
 
 
 
 Already submitted and nothing happened? [Click here to unlock it.](#)

 
 
 The three checks are yours.
 Everything is unlocked below: each check explained, and the prompt with a copy button that sets up all three.

 Want more? [All the playbooks](/playbook/), one download each.

 
 

 
 
 Unlocked

 
## The three checks, explained

 

 
 1
 
 
### A sitemap

 A sitemap is a plain list of every page on your website with its full address. Without one, AI tools and Google have to discover your pages by following links, and they miss some. With one, they get the whole site in one read. It is the least glamorous file on any website and the one most small business sites are missing.

 **How to check:** type your website address into a browser and add `/sitemap.xml` to the end. If you see a list of your pages, you have one. If you see an error or your homepage, you do not.

 say: "make me a sitemap and point robots.txt at it"
 
 
 
 2
 
 
### Your business as data

 Your name, address, phone, hours and services are probably on your site as words, or worse, inside a picture. Machines read data, not paragraphs. Structured data is a small block, hidden in the page, that states each fact in a format every AI and search engine understands. It is how ChatGPT knew my shop was in American Fork, what it does and that it is open.

 **How to check:** search "Google Rich Results Test", paste your homepage address in, and look for a LocalBusiness result. Nothing found means your business is words only.

 say: "add LocalBusiness structured data to the home page"
 
 
 
 3
 
 
### A file that tells AI what you do

 A new convention called llms.txt: one plain-English page at your site&rsquo;s address, written for AI assistants. Who you are, what you do, who it is for, where you are, the services with a link each, how to reach you. No marketing fluff. Mine is at brycenwood.com/llms.txt if you want to see one. It is cheap to make and almost nobody in your town has one yet.

 **How to check:** add `/llms.txt` to the end of your website address. If you get a plain text page about your business, you have one.

 say: "write an llms.txt for this business"
 
 

 

 
 
 The prompt

 
## One paste sets up all three checks

 Copy it, open Claude Code inside your website&rsquo;s folder, paste it, and answer its questions one at a time. No folder? It still works: it writes the three files out and tells you exactly where each one goes, so whoever runs your site can drop them in.

 
 
 1Open the terminal inside your website&rsquo;s folder (or anywhere, if you do not have the files).
 2Type `claude`.
 3Paste the prompt below and hit enter.
 
 
I want AI tools like ChatGPT to find and recommend my business. Set up three things for my website. Ask me one question at a time when you need something, and explain what each thing DOES before how it works. If you can see my website's files in this folder, make the changes here. If you cannot, write each file out for me in full and tell me exactly where it goes and who to hand it to.

First, ask me for: my business name, what we do in one sentence, the city and state we serve, our street address, phone number, opening hours, our website address, and links to our Google Business Profile, Instagram and any other profiles we have.

1. A SITEMAP. Make a sitemap.xml that lists every page on the site with its full address, and a robots.txt that points to it. If either already exists, check that it lists every real page and fix what is missing.

2. MY BUSINESS AS DATA. Add LocalBusiness structured data (JSON-LD) to the home page, using the most specific business type that fits what we do: name, description, address, phone, opening hours, service area, website, and our profile links as sameAs. Read the home page first so the words on the page and the data say the same thing.

3. A FILE THAT TELLS AI WHAT WE DO. Make an llms.txt file at the root of the site, in plain English: our name, what we do, who it is for, where we are, each service with a link, and how to contact us. Facts only, no marketing fluff, written so an assistant could recommend us correctly.

When all three are done: show me each file, tell me how to check each one myself (open /sitemap.xml in a browser, paste the home page into Google's Rich Results Test, open /llms.txt), and remind me to ask ChatGPT "who is the best [what we do] in [our city]?" again in a few weeks. It takes time for the answer to change.
 Copy the prompt
 
 Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on [@brycenwood.ai](https://www.instagram.com/brycenwood.ai/).

 

 
 
 Bonus · the checker from the video

 
## Ask ten times, get a score

 Asking ChatGPT once tells you almost nothing, because the answer changes every time. This is the exact prompt I typed to build a little tool that asks ten separate times and shows how many of the ten named your business, how often you were the top pick, and who got named instead. Mine was built in about 6 minutes.

 
 
 1. You need your own OpenAI key (from platform.openai.com). In an empty folder, save it in a file called `.env` as `OPENAI_API_KEY=your key`. Each check is 11 small requests on your key, a few cents.

 2. Open Claude Code in that folder, paste the prompt below and hit enter.

 3. Run it on your business, then do the three checks above and run it again in a few weeks.

 
 Build me a one-page tool where I type a business, a service and a town, and it asks OpenAI's model (with web search on) "Who is the best [service] in [town]?" ten separate times. Then show me a score card: how many of the ten answers named the business, how many made it the top pick, which other businesses got named instead, and what it said about them. My OpenAI key is in the file .env, never show it on screen, and test the tool on yourself before you hand it to me.Copy the checker prompt
 One honest note: the tool asks OpenAI&rsquo;s model with web search turned on. That is very close to what ChatGPT does, not identical, so treat the score as a strong hint and not a promise.

 

 
 
 From the Business Hub video

 
## Claim your business in ChatGPT, step by step

 ChatGPT now lets business owners claim their own listing. It is called Business Hub. You control what ChatGPT says about you, you get a blue check, and you can see how often you come up. Here is every step I took, and the fine print I read before I signed.

 
 
 1. Go to **chatgpt.com/business-hub** and sign in. A free ChatGPT account worked for me. Search your business name. Starting here accepts OpenAI&rsquo;s terms, so read the fine print below first.

 2. If your business shows up, claim it. If not, add it with your website. Right now you need a website to claim. To prove the site is yours, it gives you one line of text (a TXT record) to add in your domain&rsquo;s DNS settings, wherever you bought the domain. Mine passed on the first try.

 3. Pick your category and write your description. Check the category it suggests. It suggested Gym for my meal prep company. Describe what you sell, where, and who it is for, in plain words.

 4. Add your contact details. Use a real cell number for the text code. It rejected my internet business line. Then confirm the email code.

 5. Verify your ID. After that it goes to review. OpenAI does not publish how long review takes. When it clears, a blue check shows on your listing.

 
 
 The fine print, in plain English

 From OpenAI&rsquo;s Businesses in ChatGPT terms, last updated November 9, 2026.

 **You are listed either way.** OpenAI can list your business whether or not you claim it. Claiming is how you get a say in what it shows.

 **Claiming is not full control.** OpenAI can still add to, edit or replace what you write, or choose not to show it.

 **No promised ranking.** In their words: claiming does not guarantee higher placement or sales.

 **Your basic info is licensed to them for good.** Name, address, contact details, category, hours and website. That license is permanent and cannot be taken back.

 **Their AI may call you.** You agree their assistant can phone your business for ChatGPT users. The terms link to an opt-out.

 **You agree not to sue them over your own online content.** The terms include a promise not to bring claims about content you have published online, and you cover OpenAI for claims tied to your business or listing. My plain-English reading, not legal advice. If it matters to you, have a lawyer read it.

 **The stats are confidential.** The mentions and website-clicks numbers in your dashboard are OpenAI&rsquo;s confidential info. Do not post screenshots of them.

 **Own it with a partner?** Whoever clicks is agreeing on behalf of the whole company. Check with your partner first.

 **Cost:** no price is listed anywhere. I was not charged anything.

 
 Want to read it yourself? [OpenAI&rsquo;s full terms are here](https://openai.com/policies/businesses-in-chatgpt-terms/).
