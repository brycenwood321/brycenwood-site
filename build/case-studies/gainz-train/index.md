---
title: Gainz Train: A Meal Prep Company Run on Claude Code | Brycen Wood
description: Case study: how Brycen Wood and Jayson launched Gainz Train, high-protein meal prep in Orem, Utah, with every system outside the kitchen built with Claude Code.
url: https://www.brycenwood.com/case-studies/gainz-train/
last_updated: 2026-04-14
---

Case Study

 
# A Meal Prep Company.Run on Claude Code.

 How my partner Jayson and I launched [Gainz Train](https://gainztrainprep.com/), weekly high-protein meal prep in Orem, Utah, with him in the kitchen and every system outside it built through conversation with AI.

 Last updated: October 2026

 
 
 June 2026
 Launched
 
 
 41
 Paying Customers
 
 
 ~438
 Meals a Week
 
 
 1,000+
 Automated Tests
 
 
 Customer and meal counts read October 20, 2026.

 BW
 
 [Brycen Wood](/about/)
 Co-founder, Gainz Train · Co-owner, Summit Wraps & Graphics
 

 
## What Gainz Train Is

 [Gainz Train](https://gainztrainprep.com/) makes fresh, never-frozen, high-protein meals every week for people in Utah County: lifters, runners, athletes, fitness people, and anyone trying to eat healthy without cooking every night. Meals average about 45 grams of protein and run $8.50 to $10.50 each depending on how many you order. Customers pick the week's meals from the [weekly menu](https://gainztrainprep.com/menu/), then pick them up Sunday at our kitchen in Orem or get them delivered.

 It's a 50/50 partnership. Jayson has been meal prepping for himself for four years and runs everything in the kitchen: recipes, sourcing, the weekly prep, and quality. I run everything outside the kitchen. We launched on June 11, 2026.

 
## The Split: Kitchen and Systems

 A meal prep company looks like a cooking business. Most of the work is actually logistics: who ordered what, who paid, who is picking up and who needs delivery, what to buy, what to cook, how to pack each bag, and who to remind. Get any of that wrong on a Sunday and someone goes without food for the week.

 I have no coding background. Every piece of software Gainz Train runs on was built by describing what we needed to [Claude Code](https://claude.ai/code) in plain English, the same way I built the systems for [Summit Wraps](/case-studies/summit-wraps/).

 
## What I Built

 
### Ordering and Subscriptions

 The [gainztrainprep.com](https://gainztrainprep.com/) site handles the whole customer side: sign up, choose a plan, pick meals, pause, skip a week, and manage the account. Subscriptions run through Stripe and bill every Saturday. The more meals a week, the lower the price per meal, and the site does that math on its own.

 
### The Weekly Menu and Lock

 Every week has a cutoff. Before it, customers change whatever they want. After it, orders lock and the kitchen gets a final count. If a new menu isn't published in time, a failsafe rolls the last one forward so customers never face an empty page.

 
### The Kitchen Side

 Jayson works from an owners' dashboard: it edits the menu and add-ons, builds the shopping list, and gives him a packing checklist where each customer's bag, with each add-on, gets ticked off before it counts as done. The kitchen can handle about 1,000 meals a week, so the systems are built for growth.

 
### Customer Communication

 Pickup reminders go out before the Sunday window, and the system checks that each one was delivered. New customers get a check-in a few days after their first order. Referrals are tracked automatically: when a customer brings in a friend who pays, the credit lands on their next bill without anyone keeping a spreadsheet.

 
### Being Found by Google and AI

 The same playbook that got ChatGPT recommending Summit Wraps runs on Gainz Train: structured data, an `llms.txt` file, honest comparison pages like [Utah meal prep prices compared](https://gainztrainprep.com/utah-meal-prep-prices/), and free tools like the [protein calculator](https://gainztrainprep.com/protein-calculator/). A weekly check asks the major AI assistants who they recommend for meal prep in Utah County and tracks whether Gainz Train shows up.

 
### Guardrails

 Because real people's food and money run through it, the code is checked by more than 1,000 automated tests before any change can go live, and no update can ship from Friday evening to Saturday morning, while orders lock and billing runs.

 
## What It Shows

 Summit Wraps proved the approach on a service business. Gainz Train proves it on something completely different: food, subscriptions, a weekly deadline, and a physical handoff every Sunday. The kitchen still takes a skilled person. Everything around it can be built by someone who knows the business and can explain it clearly.

 
> Jayson makes food people come back for. My job is making sure nothing around the kitchen gets in the way of that.

 Want to eat it? See this week's menu at [gainztrainprep.com](https://gainztrainprep.com/menu/). Want systems like this for your own business? That's what I do.

 
 
## Want this for your business?

 Every system on this page was built in conversation with AI. I can build the same for your business, around how you actually work.

 
 [Book a Discovery Call](/contact/)
 [Visit Gainz Train](https://gainztrainprep.com/)
