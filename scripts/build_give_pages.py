#!/usr/bin/env python3
"""
Build the free "give" pages (the ones a video keyword points to).

Each page uses the /found/ template: hero, what's inside, the shared email gate
(GHL Waitlist Form), then the unlocked steps and copy-button prompt boxes.
Content lives in PAGES below; the prompts live in scripts/give_prompts/.
Run it, then regenerate the mirrors for the pages it wrote.

Usage: python3 scripts/build_give_pages.py            (all pages)
       python3 scripts/build_give_pages.py match guess (just those)

Rules for the words: plain English, no em dashes, no prices or pitch,
no customer names, nothing we have not checked. Every prompt was run once
on a sample before it went on a page.
"""

import html
import json
import sys
from pathlib import Path

BUILD = Path(__file__).parent.parent / "build"
SITE = "https://www.brycenwood.com"
PROMPTS = Path(__file__).parent / "give_prompts"
LONG_DASH = chr(8212)


def esc(s):
    return html.escape(s, quote=True)


def prompt(name):
    return (PROMPTS / f"{name}.txt").read_text(encoding="utf-8").strip()


# ---------------------------------------------------------------- content

PAGES = {}

PAGES["checks"] = dict(
    title="The 12 Checks: Is This Happening to Your Business?",
    desc="Twelve things you can check on your own business in about a minute each, on your phone. What a fail looks like and the first fix for each one. Free.",
    crumb="The 12 Checks",
    h1='Is this happening to your business? <span class="accent">12 checks, a minute each.</span>',
    sub="Every check here is something you can do on your own phone, right now, for free. Each one is a single plain step, what a fail looks like, and the first fix. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the 12 checks",
    perks_h2='The 12 checks, <span class="accent">in four groups</span>',
    perks=[
        ("Can customers find you", "Your name on Google, the map from one town over, the search a stranger does, and whether your address agrees with itself."),
        ("What AI says about you", "Ask ChatGPT who the best is, what you do, and your phone number. See if it is right."),
        ("What a customer actually gets", "Your site on a phone with no wifi, your phone after hours, and your own contact form."),
        ("Reviews and competitors", "Your last ten reviews, and every ad your biggest competitor is running."),
    ],
    perks_note="Each check is one step you can do in about a minute, what a fail looks like, and the first fix. Unlocked by the form below.",
    form_title="Get the 12 checks",
    success_h='The 12 checks are <span class="accent">yours.</span>',
    success_p="Everything is unlocked below. Do them in any order. Tick each one off as you go.",
    steps_eyebrow="Unlocked",
    steps_h2='The 12 checks, <span class="accent">one step each</span>',
    steps_intro="Tick a box when the check passes. Your ticks stay on this device.",
    ticks_on_steps=True,
    steps=[
        ("Google your business name plus &ldquo;reviews&rdquo;",
         "Search your business name with the word reviews after it. Look at the very first result.",
         "<strong>A fail looks like:</strong> the first thing is not yours: a directory, an old listing, or someone else. <strong>First fix:</strong> claim and fill out your Google Business Profile, then ask your next few happy customers to review you there."),
        ("Ask ChatGPT for the best in your city, three ways",
         "Ask: &ldquo;Who is the best [your trade] in [your city]?&rdquo; Then &ldquo;Who should I hire for [the job] near [your city]?&rdquo; Then &ldquo;Recommend a [your trade] in [your city] with good reviews.&rdquo;",
         '<strong>A fail looks like:</strong> your name is in none of the three. <strong>First fix:</strong> the three website checks on <a href="/found/">the Get Found page</a>.'),
        ("Open your website on your phone with the wifi off",
         "Turn wifi off so you are on cell data, open your site, and count the seconds until you can actually read it.",
         "<strong>A fail looks like:</strong> more than about three seconds, or the page jumps around while it loads. A lot of people leave before then. <strong>First fix:</strong> big photos are the most common cause. Shrink those first."),
        ("Search Google Maps from one town over",
         "Open Google Maps, move the map to the next town you serve, and search for what you do.",
         '<strong>A fail looks like:</strong> you disappear. <strong>First fix:</strong> add that town to the service area on your Google profile, and give it its own page on your site (<a href="/towns/">the town page template</a>).'),
        ("Look up your biggest competitor in the Meta Ad Library",
         "Go to facebook.com/ads/library, set your country, and search their name. It is free and public.",
         '<strong>What you get:</strong> every ad they are running and the date each one started. <strong>First move:</strong> the ones that have run the longest are the ones they keep paying for. <a href="/playbook/ad-library-teardown/">The Ad Library Teardown</a> walks through it.'),
        ("Call your own business number after hours",
         "After you close, call your business from a phone that is not yours. Listen to what a customer hears.",
         "<strong>A fail looks like:</strong> it rings out, the voicemail box is full, or the greeting does not say your name or your hours. <strong>First fix:</strong> record a greeting with your business name, your hours and the fastest way to reach you."),
        ("Fill out your own contact form",
         "Use a different email, fill out the form like a customer would, and time how long until a person answers.",
         "<strong>A fail looks like:</strong> nobody answers the same day, or the message never arrives at all. <strong>First fix:</strong> send form messages to a phone someone actually checks, and turn on an instant &ldquo;got it, here is what happens next&rdquo; reply."),
        ("Ask ChatGPT what your business does",
         "Ask: &ldquo;What does [your business name] in [your city] do?&rdquo;",
         '<strong>A fail looks like:</strong> wrong, out of date (an old address, a service you dropped), or made up. <strong>First fix:</strong> put the facts on your website in plain words and as data, check 2 on <a href="/found/">the Get Found page</a>.'),
        ("Check your Google listing address matches your website",
         "Open your Google listing and your website side by side. Compare the address character by character, then the phone and the hours.",
         '<strong>A fail looks like:</strong> any difference at all: a missing suite number, an old address, different hours. <strong>First fix:</strong> <a href="/match/">the listing match checklist</a>, address line first.'),
        ("Search &ldquo;[your trade] near me&rdquo; in a private window",
         "Open a private or incognito tab so Google does not use your history. Search, then count how many businesses sit above you.",
         "<strong>A fail looks like:</strong> you are not in the map results or not on the first screen. <strong>First fix:</strong> Google says it ranks local results by relevance, distance and prominence. You control relevance (every category and service filled in on your profile) and a lot of prominence (reviews and photos)."),
        ("Look at your last ten Google reviews",
         "Count how many of your last ten reviews have a reply from you.",
         '<strong>A fail looks like:</strong> most of them have no reply. <strong>First fix:</strong> reply to every one, good and bad, short and specific. Then run them through <a href="/reviews/">the review prompt</a> to see what keeps coming up.'),
        ("Ask ChatGPT for your phone number",
         "Ask: &ldquo;What is the phone number for [your business name] in [your city]?&rdquo;",
         "<strong>A fail looks like:</strong> a wrong number, an old one, or one it made up. <strong>First fix:</strong> make the number the same everywhere it shows up online: your website, Google, Facebook, Yelp."),
    ],
    boxes=[],
    sticky_btn="Get the 12 checks",
    sticky_sub="12 checks, a minute each &middot; free",
)

PAGES["watch"] = dict(
    title="The Watcher Prompt: An AI That Checks Your Other AIs",
    desc="If you have jobs running on their own, the scary part is one breaking quietly and saying everything is fine. One prompt builds a watcher that checks each job actually produced something, and only speaks when something needs you.",
    crumb="The Watcher",
    h1='Who checks the robots? <span class="accent">An AI that watches the others.</span>',
    sub="I have AI jobs running my businesses every night: leads, texts, reports, backups. One more job checks that all the others actually made something, and it only speaks up when something needs me. Here is how it thinks, and the prompt that builds your own. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the watcher prompt",
    perks_h2='The watcher, <span class="accent">one breath each</span>',
    perks=[
        ("Ran is not the same as worked", "It checks the thing each job was supposed to leave behind, not just that the job ran."),
        ("It only speaks when it matters", "Quiet when everything is fine. One line per problem when something is not."),
        ("One prompt builds yours", "Lists your jobs with you, builds the watcher, then breaks something on purpose to prove it works."),
    ],
    perks_note="The four ideas behind it, in plain English, and the prompt that builds it. Unlocked by the form below.",
    form_title="Get the watcher prompt",
    success_h='The watcher is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below: how it thinks, and the prompt with a copy button.",
    steps_eyebrow="Unlocked",
    steps_h2='How the watcher <span class="accent">thinks</span>',
    steps=[
        ("&ldquo;Ran&rdquo; is not the same as &ldquo;worked&rdquo;",
         "The scary part is not a job breaking. It is a job breaking quietly and saying everything is fine. A job can run, hit a snag, write an empty file and still report success. So the watcher checks what the job was supposed to leave behind: the report, the row in the sheet, the sent email, the backup. Was it made, is it new, and does it look like the last few?",
         "<strong>The rule it is built on:</strong> a false green is worse than a red. An error gets fixed, because you see it. A false &ldquo;all good&rdquo; sits there for weeks, because nobody looks.",
         "say: \"check what it made, not that it ran\""),
        ("Write down what each job should produce",
         "Before a watcher can judge anything, it needs to know what normal looks like: each job's name, when it runs, and what it leaves behind when it works. The prompt walks you through that list first.",
         "<strong>One more rule:</strong> if the watcher cannot see a job's output at all, it says &ldquo;cannot check&rdquo;. Never &ldquo;OK&rdquo;.",
         None),
        ("Only speak when something needs you",
         "My watcher once sent me 16 alerts, and 11 of them were noise. So I stopped reading all of them, including the 5 that mattered. Now it stays quiet when everything is fine, and when something breaks it sends one line per problem: which job, what is wrong, what to do first.",
         "<strong>Why it matters:</strong> an alert you have learned to ignore is the same as no alert.",
         None),
        ("Prove it by breaking something",
         "Before you trust it, break one job on purpose (rename a test file) and make sure the watcher catches it. A check that has never failed has never been tested. The prompt does this for you before anything gets switched on.",
         None, None),
    ],
    boxes_eyebrow="The prompt",
    boxes_h2='One paste builds <span class="accent">your watcher</span>',
    boxes_intro="Copy it, open Claude Code in the folder where your jobs live (or anywhere, and tell it where they are), paste it, and answer its questions one at a time. Before anything is switched on, it shows you what it would have said today.",
    mini_steps=True,
    boxes=[("promptText", None, prompt("watch"), "Copy the prompt")],
    sticky_btn="Get the watcher prompt",
    sticky_sub="The watcher prompt &middot; free",
)

PAGES["match"] = dict(
    title="The Listing Match Checklist: Google vs Your Website",
    desc="One page: everything that should match between your Google listing and your website (name, address, phone, hours, categories), with a tick box for each. Do the address line first.",
    crumb="Listing Match",
    h1='One wrong line on Google <span class="accent">can hide your whole business.</span>',
    sub="Google trusts the version of your business that agrees everywhere. When your website says one thing and your listing says another, it does not know which one to believe. Here is everything that has to match, with a tick box for each, plus a prompt that compares the two for you. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the checklist",
    perks_h2='What is inside, <span class="accent">one breath each</span>',
    perks=[
        ("The checklist, address first", "Every line that must match between your Google listing and your website, with a tick box."),
        ("What counts as a mismatch", "A missing suite number counts. &ldquo;Ste&rdquo; versus &ldquo;Suite&rdquo; does not."),
        ("A compare prompt", "Paste both into AI and it lists every difference, worst first."),
    ],
    perks_note="The full checklist and the compare prompt. Unlocked by the form below.",
    form_title="Get the listing match checklist",
    success_h='The checklist is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below. Open your Google listing next to your website and start with the address.",
    steps_eyebrow="Unlocked",
    steps_h2='Everything that must match, <span class="accent">address first</span>',
    steps_intro="Open your Google listing on one side and your website on the other. Tick a line only when it matches exactly. Your ticks stay on this device.",
    checklist=[
        ("Google listing vs your website", [
            ("Address (do this one first)", "Street number, street name, suite or unit, city, ZIP. A missing suite number or an old address after a move is a mismatch. &ldquo;Ste&rdquo; versus &ldquo;Suite&rdquo; is fine."),
            ("Business name", "The same words on both. No extra keywords added to the Google name."),
            ("Phone number", "The same number on both, and it is the one that actually rings."),
            ("Hours", "Every day of the week, including the days you are closed. Then any holiday hours."),
            ("Categories", "Your main Google category says the same thing your home page headline says you do."),
            ("Services", "The services on your listing are on your website, with the same names."),
            ("Website link", "The link on your listing opens a real page, and it loads on a phone."),
            ("Service area", "The towns on your listing are towns your website says you serve."),
        ]),
        ("Then the other places people look", [
            ("Apple Maps", "Same address, phone and hours."),
            ("Facebook page", "Same address, phone and hours."),
            ("Yelp and Bing Places", "Same address, phone and hours, if you have them."),
        ]),
    ],
    steps=[],
    boxes_eyebrow="The prompt",
    boxes_h2='Let AI find <span class="accent">every difference</span>',
    boxes_intro="Copy everything you can see on your Google listing, then your website's footer, contact page and home page headline. Paste both into the prompt in ChatGPT, Claude or Gemini. It lists every mismatch, worst first, and the one to fix first.",
    boxes=[("promptText", None, prompt("match"), "Copy the prompt")],
    sticky_btn="Get the checklist",
    sticky_sub="The listing match checklist &middot; free",
)

PAGES["guess"] = dict(
    title="The Do Not Guess Sentence, Plus 3 Versions",
    desc="The one sentence that stops an AI from making things up about your business, plus three versions for ChatGPT, Claude and Gemini, each with a copy button.",
    crumb="Do Not Guess",
    h1='One sentence made my AI <span class="accent">stop making things up.</span>',
    sub="Ask AI a question about your business and it will answer with total confidence, even when it has no idea. It wants to be helpful, so it guesses. Give it permission to say it does not know, and it guesses a lot less. Here is the sentence, plus three versions for the tools you probably use. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the sentence + 3 versions",
    perks_h2='What is inside, <span class="accent">one breath each</span>',
    perks=[
        ("The sentence", "Ten words you add to the end of any question."),
        ("Three versions", "One each for ChatGPT, Claude and Gemini, written for how people usually use that tool."),
        ("Where to put it so it sticks", "So it applies to every chat, not just the one you remember to add it to."),
    ],
    perks_note="The sentence and all three versions, each with a copy button. Unlocked by the form below.",
    form_title="Get the sentence + 3 versions",
    success_h='The sentence is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below, each version with its own copy button.",
    steps_eyebrow="Unlocked",
    steps_h2='Why it works, <span class="accent">and where it goes</span>',
    steps=[
        ("Why AI guesses",
         "An AI tool is built to give you an answer. When it does not have the fact (the year you opened, your exact hours, a price), the most helpful-sounding thing is to fill the gap with something that sounds right. It is not lying on purpose. Nobody told it that &ldquo;I don't know&rdquo; is allowed.",
         None, None),
        ("Give it permission",
         "Add the sentence to the end of your question. Now an honest blank is a good answer, and you can see exactly which facts it does not have.",
         None, "say: \"If you don't know, say you don't know. Don't guess.\""),
        ("Make it stick",
         "Most AI apps have a place in their settings for standing instructions that apply to every chat. Paste one of the versions below there, once, and you stop having to remember.",
         None, None),
        ("Test it on your own business",
         "Ask something it cannot know, like &ldquo;Write the story of my business: what year we opened and who started it.&rdquo; Once without the sentence, once with it. Compare.",
         None, None),
    ],
    boxes_eyebrow="Copy and paste",
    boxes_h2='The sentence, <span class="accent">plus three versions</span>',
    boxes_intro="Use the short one at the end of any question. Use a longer version in your settings so it is always on.",
    boxes=[
        ("promptBase", "The sentence (any tool)", "If you don't know, say you don't know. Don't guess.", "Copy the sentence"),
        ("promptChatgpt", "For ChatGPT (everyday questions)", prompt("guess_chatgpt"), "Copy the ChatGPT version"),
        ("promptClaude", "For Claude (when you paste in your own info)", prompt("guess_claude"), "Copy the Claude version"),
        ("promptGemini", "For Gemini (when it searches the web)", prompt("guess_gemini"), "Copy the Gemini version"),
    ],
    sticky_btn="Get the sentence",
    sticky_sub="The sentence + 3 versions &middot; free",
)

PAGES["reviews"] = dict(
    title="The Review Prompt: What Your Reviews Have in Common",
    desc="Paste your last ten reviews into AI with one prompt. It tells you what people keep praising and what keeps coming up as a complaint. Copy button included.",
    crumb="The Review Prompt",
    h1='Paste your last ten reviews into AI. <span class="accent">Ask one question.</span>',
    sub="You read reviews one at a time. AI reads them together. Whatever shows up more than once is the thing to fix, or the thing to say louder. Here is the exact prompt, with a copy button. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the review prompt",
    perks_h2='What is inside, <span class="accent">one breath each</span>',
    perks=[
        ("What people keep praising", "Every theme that shows up in two or more reviews, with a count and a quote."),
        ("What keeps coming up as a complaint", "Including the polite ones, like &ldquo;only thing I'd change...&rdquo;"),
        ("One fix and one thing to say louder", "Based only on what your customers actually wrote."),
    ],
    perks_note="Four short steps and the prompt with a copy button. Unlocked by the form below.",
    form_title="Get the review prompt",
    success_h='The review prompt is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below: the steps, and the prompt with a copy button.",
    steps_eyebrow="Unlocked",
    steps_h2='Four steps, <span class="accent">ten minutes</span>',
    steps=[
        ("Copy your last ten reviews",
         "From Google, Facebook, wherever you get them. Keep the star rating with each one. Take the names out if you like. The prompt does not need them.",
         None, None),
        ("Paste them into the prompt",
         "Copy the prompt below into ChatGPT, Claude or Gemini, and paste your reviews where it says.",
         None, None),
        ("Read the patterns, not the single reviews",
         "The prompt only counts something as a pattern if it shows up in at least two reviews. One-offs go in their own short list at the end, so one angry customer does not set your to-do list.",
         None, None),
        ("Do one thing with it",
         "Fix the complaint that keeps coming up. Then take the praise that keeps coming up and put it on your home page, in your customers' own words.",
         None, None),
    ],
    boxes_eyebrow="The prompt",
    boxes_h2='The exact <span class="accent">review prompt</span>',
    boxes_intro="Works in ChatGPT, Claude or Gemini. No setup.",
    boxes=[("promptText", None, prompt("reviews"), "Copy the prompt")],
    sticky_btn="Get the review prompt",
    sticky_sub="The review prompt &middot; free",
)

PAGES["churn"] = dict(
    title="The Churn Prompt: Line Up Your Changes With Who Left",
    desc="Customers rarely leave at random. This prompt lines up every change you made with every customer who left, so the pattern shows up. Copy button included.",
    crumb="The Churn Prompt",
    h1='Your customers did not leave randomly. <span class="accent">Find the one change.</span>',
    sub="Look at each customer who left on their own and every reason looks different. Put the dates of your changes next to the dates people left, and a pattern can show up that you would never see one at a time. Here is the prompt that lines them up. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the churn prompt",
    perks_h2='What is inside, <span class="accent">one breath each</span>',
    perks=[
        ("One timeline", "Every change you made and every customer who left, on one list, oldest first."),
        ("Before and after counts", "How many people left in the 30 days before each change, and the 30 days after."),
        ("The one change to look at", "With how sure it is, and one question to ask a customer who left."),
    ],
    perks_note="Four short steps and the prompt with a copy button. Unlocked by the form below.",
    form_title="Get the churn prompt",
    success_h='The churn prompt is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below: the steps, and the prompt with a copy button.",
    steps_eyebrow="Unlocked",
    steps_h2='Four steps, <span class="accent">one pattern</span>',
    steps=[
        ("Write down every change you made, with the date",
         "Prices, hours, menu or services, staff, policies, pickup or delivery, the website, how you bill. Small ones count. The change you forgot about is often the one.",
         None, None),
        ("List who left, and when",
         "Everyone who cancelled, paused or stopped coming, with the date, plus anything you know: how they bought, what they bought, how long they had been a customer. Initials are fine.",
         None, None),
        ("Paste both into the prompt",
         "Copy the prompt below into ChatGPT, Claude or Gemini and paste your two lists where it says. If something is missing, it asks before it starts.",
         None, None),
        ("Read it as &ldquo;after&rdquo;, not &ldquo;because&rdquo;",
         "A timeline can show a pattern. It cannot prove a cause. So the prompt ends with one question to ask a customer who left. That conversation is how you find out.",
         None, None),
    ],
    boxes_eyebrow="The prompt",
    boxes_h2='The exact <span class="accent">churn prompt</span>',
    boxes_intro="Works in ChatGPT, Claude or Gemini. No setup.",
    boxes=[("promptText", None, prompt("churn"), "Copy the prompt")],
    sticky_btn="Get the churn prompt",
    sticky_sub="The churn prompt &middot; free",
)

PAGES["towns"] = dict(
    title="The Town Page Template: One Page for Every Town You Serve",
    desc="A fill-in-the-blank page template for each town you serve, with the town in the title, plus a prompt that fills it in from real jobs without making anything up.",
    crumb="Town Pages",
    h1='One page for every town you serve. <span class="accent">With the town in the title.</span>',
    sub="One thing Google looks at is whether a page uses the exact words people type. When someone searches for what you do plus their town, a page with that town in the title is a direct match. A line on your homepage listing ten towns is not. Here is the template, and a prompt that fills it in. Drop your email below and it unlocks. Nothing to buy.",
    btn="Unlock the template",
    perks_h2='What is inside, <span class="accent">one breath each</span>',
    perks=[
        ("The template", "Every line of a town page, fill in the blanks: title, headline, first two sentences, sections."),
        ("The rules that keep it safe", "What makes a town page real, and what makes it look like a copy."),
        ("A fill-it-in prompt", "Asks you for real jobs and local details, and leaves blanks instead of making things up."),
    ],
    perks_note="The template and the prompt, each with a copy button. Unlocked by the form below.",
    form_title="Get the town page template",
    success_h='The template is <span class="accent">yours.</span>',
    success_p="Everything is unlocked below: the rules, the template and the prompt.",
    steps_eyebrow="Unlocked",
    steps_h2='Four rules <span class="accent">before you start</span>',
    steps=[
        ("One town, one page",
         "Not a line on your homepage. A real page, with its own address on your site, and the town name in the title and the main headline.",
         None, None),
        ("Make every page real",
         "A real job you did there, how long it takes you to get there, something you actually know about the area. Pages that are the same with only the town name swapped look like copies. Google's own spam rules call those doorway pages, and they can do more harm than good.",
         None, None),
        ("Keep your real address",
         "Each page lists the address you actually work from, exactly as it is on your Google listing. Never claim an office in a town you only drive to.",
         None, None),
        ("Link to every town page",
         "Add each one to your services or service area page, and to your sitemap, so Google can find it.",
         None, None),
    ],
    boxes_eyebrow="Copy and paste",
    boxes_h2='The template, <span class="accent">and the prompt that fills it</span>',
    boxes_intro="Fill the template in yourself, or paste the prompt into ChatGPT, Claude or Gemini (or Claude Code inside your website's folder) and answer its questions.",
    boxes=[
        ("promptTemplate", "The template", prompt("towns").split("TEMPLATE", 1)[1].strip(), "Copy the template"),
        ("promptText", "The fill-it-in prompt", prompt("towns"), "Copy the prompt"),
    ],
    sticky_btn="Get the town page template",
    sticky_sub="The town page template &middot; free",
)


# ---------------------------------------------------------------- template

HEAD_STYLE = """<style>
.five-step{display:grid;grid-template-columns:56px 1fr;gap:20px;padding:28px 0;border-bottom:1px solid var(--card-border)}
.five-step:last-child{border-bottom:none}
.five-num{font-family:var(--mono);font-size:32px;font-weight:700;color:var(--lime);line-height:1}
.five-step h3{font-size:22px;font-weight:800;margin:0 0 8px;line-height:1.2}
.five-step .what{font-size:16px;color:var(--text);line-height:1.65;margin:0 0 12px}
.five-step .how{font-size:15px;color:var(--text-dim);line-height:1.65;margin:0}
.five-step .how strong{color:var(--text)}
.five-step a,.tick-list a{color:var(--lime)}
.five-step .say{display:inline-block;font-family:var(--mono);font-size:13px;color:var(--lime);background:var(--lime-dim);padding:3px 8px;border-radius:4px;margin-top:10px}
.prompt-box{position:relative;background:var(--card);border:1px solid var(--card-border);border-left:3px solid var(--lime);border-radius:8px;padding:24px;margin-top:24px}
.prompt-box h3{font-size:18px;font-weight:800;margin:0 0 14px}
.prompt-box pre{font-family:var(--mono);font-size:13.5px;line-height:1.7;color:var(--text);white-space:pre-wrap;word-wrap:break-word;margin:0;background:none;padding:0}
.copy-btn{width:100%;margin-top:18px;padding:16px;font-family:var(--sans);font-size:17px;font-weight:800;background:var(--lime);color:#050508;border:none;border-radius:8px;cursor:pointer;letter-spacing:0.3px}
.copy-btn:active{transform:scale(0.99)}
.copy-btn.done{background:var(--lime-deep)}
.mini-steps{display:grid;gap:10px;margin-top:20px}
.mini-steps div{display:grid;grid-template-columns:28px 1fr;gap:12px;font-size:15px;color:var(--text-dim);line-height:1.6}
.mini-steps span{font-family:var(--mono);color:var(--lime);font-weight:700}
.tick-group{margin-top:32px}
.tick-group h3{font-size:20px;font-weight:800;margin:0 0 8px}
.tick{display:grid;grid-template-columns:32px 1fr;gap:12px;padding:18px 0;border-bottom:1px solid var(--card-border);cursor:pointer}
.tick:last-child{border-bottom:none}
.tick input,.step-tick input{width:22px;height:22px;margin-top:2px;accent-color:var(--lime);cursor:pointer}
.tick strong{display:block;font-size:17px;color:var(--text);margin-bottom:4px}
.tick span{font-size:15px;color:var(--text-dim);line-height:1.6}
.step-tick{display:inline-flex;align-items:center;gap:10px;margin-top:14px;font-size:14px;color:var(--text-dim);cursor:pointer}
.steps-intro{font-size:16px;color:var(--text-dim);max-width:600px;margin:16px auto 0;line-height:1.6;text-align:center}
.locked-content{display:none}
@media (max-width:600px){.five-step{grid-template-columns:40px 1fr;gap:14px}.five-num{font-size:26px}.five-step h3{font-size:19px}}
</style>"""

NAV = """<nav>
  <a href="/" class="nav-logo">BRYCEN WOOD</a>
  <div class="nav-links" id="navLinks">
    <a href="/services/" class="nav-link">Services</a>
    <a href="/case-studies/" class="nav-link">Case Studies</a>
    <a href="/guides/" class="nav-link">Guides</a>
    <a href="/playbook/" class="nav-link">Playbooks</a>
    <a href="/about/" class="nav-link">About</a>
    <a href="/contact/" class="nav-link">Contact</a>
  </div>
  <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
    <span></span><span></span><span></span>
  </button>
</nav>"""

FORM = """      <div id="ghl-form">
        <iframe
          src="https://api.leadconnectorhq.com/widget/form/Z1F5E7GVhmaDPvn8B7ww"
          style="display:inline;width:100%;height:600px;border:none;border-radius:4px"
          id="inline-Z1F5E7GVhmaDPvn8B7ww"
          data-layout="{'id':'INLINE'}"
          data-trigger-type="alwaysShow"
          data-trigger-value=""
          data-activation-type="alwaysActivated"
          data-activation-value=""
          data-deactivation-type="neverDeactivate"
          data-deactivation-value=""
          data-form-name="Waitlist Form"
          data-height="600"
          data-layout-iframe-id="inline-Z1F5E7GVhmaDPvn8B7ww"
          data-form-id="Z1F5E7GVhmaDPvn8B7ww"
          title="Playbook request"
        ></iframe>
        <script src="https://link.msgsndr.com/js/form_embed.js"></script>
      </div>"""

FOOTER = """<footer>
  <div class="footer-grid">
    <div>
      <div class="footer-brand">BRYCEN WOOD</div>
      <div class="footer-desc">Custom business operating systems built with Claude Code. No coding experience required. Based in Utah.</div>
    </div>
    <div>
      <div class="footer-heading">Pages</div>
      <a href="/services/" class="footer-link">Services</a>
      <a href="/case-studies/" class="footer-link">Case Studies</a>
      <a href="/guides/" class="footer-link">Guides</a>
      <a href="/about/" class="footer-link">About</a>
    </div>
    <div>
      <div class="footer-heading">Resources</div>
      <a href="/playbook/" class="footer-link">Playbooks</a>
      <a href="/tools/" class="footer-link">Tools</a>
      <a href="/contact/" class="footer-link">Contact</a>
    </div>
    <div>
      <div class="footer-heading">Social</div>
      <a href="https://www.instagram.com/brycenwood.ai/" class="footer-link" target="_blank" rel="noopener">Instagram</a>
      <a href="https://www.tiktok.com/@brycenwood1" class="footer-link" target="_blank" rel="noopener">TikTok</a>
      <a href="https://www.youtube.com/@brycenwood-ai" class="footer-link" target="_blank" rel="noopener">YouTube</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>BUILT WITH <span class="lime">CLAUDE CODE</span> &nbsp;&middot;&nbsp; BRYCENWOOD.COM &nbsp;&middot;&nbsp; &copy; 2026</p>
  </div>
</footer>"""

SCRIPT = r"""<script>
const navToggle=document.getElementById('navToggle');
const navLinks=document.getElementById('navLinks');
if(navToggle&&navLinks){
  navToggle.addEventListener('click',()=>{
    navLinks.classList.toggle('open');
    const spans=navToggle.querySelectorAll('span');
    if(navLinks.classList.contains('open')){
      spans[0].style.transform='rotate(45deg) translate(5px,5px)';
      spans[1].style.opacity='0';
      spans[2].style.transform='rotate(-45deg) translate(5px,-5px)';
    }else{
      spans[0].style.transform='none';
      spans[1].style.opacity='1';
      spans[2].style.transform='none';
    }
  });
}
const revealObs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){e.target.classList.add('visible');revealObs.unobserve(e.target);}
  });
},{threshold:0.1});
document.querySelectorAll('.reveal').forEach(el=>revealObs.observe(el));

const SLUG='__SLUG__';
try{localStorage.setItem('bw_playbook_pending',SLUG)}catch(e){}
let unlocked=false;
function unlock(opts){
  if(unlocked)return;
  unlocked=true;
  try{localStorage.removeItem('bw_playbook_pending')}catch(e){}
  try{localStorage.setItem('bw_playbook_'+SLUG,'1')}catch(e){}
  const formPanel=document.getElementById('formPanel');
  const successPanel=document.getElementById('successPanel');
  if(formPanel)formPanel.style.display='none';
  if(successPanel)successPanel.style.display='block';
  document.querySelectorAll('.locked-content').forEach(el=>{el.style.display='block';el.classList.add('visible')});
  if(typeof gtag==='function'){gtag('event','playbook_unlock',{playbook:SLUG})}
  if(successPanel)successPanel.scrollIntoView({behavior:'smooth',block:'center'});
}
// 0: came back from the GHL redirect
if(new URLSearchParams(window.location.search).get('dl')==='1'){setTimeout(unlock,500);}
// already unlocked this one on this device
try{if(localStorage.getItem('bw_playbook_'+SLUG)==='1'&&!unlocked){unlock({noDownload:true});}}catch(e){}
// 1: GHL postMessage
window.addEventListener('message',function(e){
  try{
    var d=e.data;
    if(typeof d==='string'&&(d.includes('formSubmitted')||d.includes('form_submitted')||d.includes('lcWidget')))unlock();
    if(typeof d==='object'&&d){
      var json=JSON.stringify(d).toLowerCase();
      if(json.includes('formsubmitted')||json.includes('form_submitted')||json.includes('lcwidget')||json.includes('appreciate')||json.includes('thank you'))unlock();
    }
  }catch(err){}
});
// 2: iframe shrinks after submit (only after it was tall, loaded, for 4 s)
const ghlIframe=document.getElementById('inline-Z1F5E7GVhmaDPvn8B7ww');
if(ghlIframe){
  let lastHeight=0,tallSince=0;
  const heightPoll=setInterval(()=>{
    try{
      const h=ghlIframe.offsetHeight||ghlIframe.clientHeight;
      const now=Date.now();
      if(h>400){if(!tallSince)tallSince=now;}
      if(lastHeight>400&&h<350&&!unlocked&&tallSince&&(now-tallSince)>4000){unlock();clearInterval(heightPoll);}
      lastHeight=h;
    }catch(err){}
  },500);
  setTimeout(()=>clearInterval(heightPoll),600000);
}
// 3: manual
const manualLink=document.getElementById('manualTriggerLink');
if(manualLink){manualLink.addEventListener('click',function(e){e.preventDefault();unlock();});}

const stickyBar=document.getElementById('stickyBar');
if(stickyBar){
  const heroEl=document.querySelector('.page-hero');
  const stickyObs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      const gateVisible=(()=>{const g=document.getElementById('get');if(!g)return false;const r=g.getBoundingClientRect();return r.top<window.innerHeight&&r.bottom>0})();
      if(!e.isIntersecting&&!gateVisible&&!unlocked){stickyBar.classList.add('visible')}else{stickyBar.classList.remove('visible')}
    });
  },{threshold:0});
  if(heroEl)stickyObs.observe(heroEl);
}

// tick boxes remember their state on this device
document.querySelectorAll('input[data-tick]').forEach(function(box){
  var key='bw_tick_'+SLUG+'_'+box.getAttribute('data-tick');
  try{if(localStorage.getItem(key)==='1')box.checked=true}catch(e){}
  box.addEventListener('change',function(){try{localStorage.setItem(key,box.checked?'1':'0')}catch(e){}});
});

function fallbackCopy(text){
  const ta=document.createElement('textarea');
  ta.value=text;ta.style.position='fixed';ta.style.opacity='0';
  document.body.appendChild(ta);ta.focus();ta.select();
  let ok=false;
  try{ok=document.execCommand('copy')}catch(e){ok=false}
  document.body.removeChild(ta);
  return ok;
}
document.querySelectorAll('.copy-btn[data-target]').forEach(function(btn){
  const label=btn.textContent;
  btn.addEventListener('click',async()=>{
    const src=document.getElementById(btn.getAttribute('data-target'));
    if(!src)return;
    const text=src.textContent;
    let ok=false;
    try{
      if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(text);ok=true}
      else{ok=fallbackCopy(text)}
    }catch(e){ok=fallbackCopy(text)}
    if(ok){
      btn.textContent='Copied. Now paste it in.';
      btn.classList.add('done');
      if(typeof gtag==='function'){gtag('event','copy_prompt',{page:SLUG,box:btn.getAttribute('data-target')})}
      setTimeout(()=>{btn.textContent=label;btn.classList.remove('done')},4000);
    }else{
      btn.textContent='Press and hold the text above to copy it';
    }
  });
});
</script>"""

CLOSING = '    <p style="text-align:center;font-size:14px;color:var(--text-muted);margin-top:28px;line-height:1.6">Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on <a href="https://www.instagram.com/brycenwood.ai/" target="_blank" rel="noopener" style="color:var(--lime)">@brycenwood.ai</a>.</p>'


def render(slug, p):
    url = f"{SITE}/{slug}/"
    t, d = esc(p["title"]), esc(p["desc"])
    ld_page = json.dumps({"@context": "https://schema.org", "@type": "WebPage", "name": p["title"],
                          "description": p["desc"], "url": url,
                          "author": {"@type": "Person", "name": "Brycen Wood", "url": f"{SITE}/about/"}})
    ld_crumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Playbook", "item": f"{SITE}/playbook/"},
        {"@type": "ListItem", "position": 3, "name": p["crumb"]}]})

    perks = "\n".join(
        f'      <div class="perk"><div class="perk-icon">{i:02d}</div><div class="perk-text"><strong>{a}</strong> &middot; {b}</div></div>'
        for i, (a, b) in enumerate(p["perks"], 1))

    blocks = []
    for i, s in enumerate(p.get("steps", []), 1):
        h3, what = s[0], s[1]
        how = s[2] if len(s) > 2 else None
        say = s[3] if len(s) > 3 else None
        parts = [f'        <h3>{h3}</h3>', f'        <p class="what">{what}</p>']
        if how:
            parts.append(f'        <p class="how">{how}</p>')
        if say:
            parts.append(f'        <span class="say">{esc(say)}</span>')
        if p.get("ticks_on_steps"):
            parts.append(f'        <label class="step-tick"><input type="checkbox" data-tick="s{i}"> Passed</label>')
        blocks.append('    <div class="five-step">\n      <div class="five-num">%d</div>\n      <div>\n%s\n      </div>\n    </div>' % (i, "\n".join(parts)))

    for gi, (gname, items) in enumerate(p.get("checklist", []), 1):
        rows = "\n".join(
            f'      <label class="tick"><input type="checkbox" data-tick="g{gi}i{ii}"><div><strong>{a}</strong><span>{b}</span></div></label>'
            for ii, (a, b) in enumerate(items, 1))
        blocks.append(f'    <div class="tick-group tick-list">\n      <h3>{gname}</h3>\n{rows}\n    </div>')

    if not p.get("boxes"):
        blocks.append(CLOSING)

    intro = f'\n      <p class="steps-intro">{p["steps_intro"]}</p>' if p.get("steps_intro") else ""
    unlocked = f"""<section class="locked-content" id="unlocked" style="padding:48px 0;">
  <div class="container-narrow">
    <div class="section-header">
      <p class="hero-eyebrow">{p['steps_eyebrow']}</p>
      <h2>{p['steps_h2']}</h2>{intro}
    </div>
{chr(10).join(blocks)}
  </div>
</section>"""

    boxes_html = ""
    if p.get("boxes"):
        boxes = []
        for bid, heading, text, label in p["boxes"]:
            h = f"\n      <h3>{heading}</h3>" if heading else ""
            boxes.append(f'    <div class="prompt-box">{h}\n<pre id="{bid}">{esc(text)}</pre>\n      <button class="copy-btn" data-target="{bid}">{label}</button>\n    </div>')
        mini = ""
        if p.get("mini_steps"):
            mini = """
    <div class="mini-steps">
      <div><span>1</span><div>Open the terminal inside the folder where your jobs or scripts live.</div></div>
      <div><span>2</span><div>Type <code>claude</code>.</div></div>
      <div><span>3</span><div>Paste the prompt below and hit enter.</div></div>
    </div>"""
        boxes_html = f"""
<section class="locked-content" id="prompt" style="padding:32px 0 72px;">
  <div class="container-narrow">
    <div class="section-header">
      <p class="hero-eyebrow">{p['boxes_eyebrow']}</p>
      <h2>{p['boxes_h2']}</h2>
      <p style="font-size:16px;color:var(--text-dim);max-width:600px;margin:16px auto 0;line-height:1.6">{p['boxes_intro']}</p>
    </div>{mini}
{chr(10).join(boxes)}
{CLOSING}
  </div>
</section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2GV8RG30MK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-2GV8RG30MK');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t} | Brycen Wood</title>
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
<meta property="og:image" content="{SITE}/assets/images/og-default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<script type="application/ld+json">
{ld_page}
</script>
<script type="application/ld+json">
{ld_crumb}
</script>
<link rel="stylesheet" href="/assets/css/global.css">
<link rel="stylesheet" href="/assets/css/components.css">
{HEAD_STYLE}
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="orb orb-3"></div>

{NAV}

<div class="breadcrumb">
  <a href="/">Home</a><span class="sep">/</span>
  <a href="/playbook/">Playbooks</a><span class="sep">/</span>
  <span>{p['crumb']}</span>
</div>

<section class="page-hero">
  <p class="hero-eyebrow">From the video &middot; Free</p>
  <h1>{p['h1']}</h1>
  <p class="hero-sub">{p['sub']}</p>
  <div class="btn-group" style="margin-top:24px">
    <a href="#get" class="btn-primary">{p['btn']}</a>
  </div>
</section>

<div class="divider"></div>

<section style="padding:56px 0;">
  <div class="container-narrow">
    <div class="section-header reveal">
      <p class="hero-eyebrow">What&rsquo;s inside</p>
      <h2>{p['perks_h2']}</h2>
    </div>
    <div class="perks reveal" style="margin-top:40px">
{perks}
    </div>
    <p class="reveal" style="text-align:center;font-size:15px;color:var(--text-dim);margin-top:28px;line-height:1.6">{p['perks_note']}</p>
  </div>
</section>

<div class="divider"></div>

<section class="section-raised" id="get" style="padding:72px 0;">
  <div class="container-narrow">
    <div class="form-wrapper reveal" id="formPanel">
      <div class="form-title">{p['form_title']}</div>
      <div class="form-sub">Enter your email and this page unlocks immediately. Just this one, not all of them.</div>
{FORM}
      <p style="text-align:center;margin-top:20px;font-size:14px;color:var(--text-dim)">Already submitted and nothing happened? <a href="#" id="manualTriggerLink" style="color:var(--lime);text-decoration:underline;font-weight:600">Click here to unlock it.</a></p>
    </div>
    <div id="successPanel" style="display:none;text-align:center;padding:48px 24px;">
      <div style="font-size:32px;font-weight:800;margin-bottom:12px;color:var(--text)">{p['success_h']}</div>
      <p style="color:var(--text-dim);margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto">{p['success_p']}</p>
      <p style="font-size:14px;color:var(--text-muted);margin-top:24px">Want more? <a href="/playbook/" style="color:var(--lime)">All the playbooks</a>, one download each.</p>
    </div>
  </div>
</section>


{unlocked}
{boxes_html}

<div class="sticky-bar" id="stickyBar">
  <a href="#get" class="sticky-bar-btn">{p['sticky_btn']}</a>
  <div class="sticky-bar-sub">{p['sticky_sub']}</div>
</div>

{FOOTER}

{SCRIPT.replace('__SLUG__', slug)}
</body>
</html>
"""


def main():
    wanted = sys.argv[1:] or list(PAGES)
    for slug in wanted:
        out = BUILD / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        page = render(slug, PAGES[slug])
        if LONG_DASH in page:
            raise SystemExit(f"{slug}: long dash found, fix the content")
        out.write_text(page, encoding="utf-8")
        print(f"  wrote {out.relative_to(BUILD.parent)}")


if __name__ == "__main__":
    main()
