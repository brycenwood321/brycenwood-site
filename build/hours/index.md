---
title: 420 Hours in Claude Code: The Three Lessons | Brycen Wood
description: A list of its own mistakes that has to become code, a grader that never built the thing, and a greeting that leads with what is working. Each one explained in plain English, plus one prompt that sets all three up.
url: https://www.brycenwood.com/hours/
last_updated: 2026-04-14
---

From the video · Free Playbook

 
# 420 hours in Claude Code. The three lessons.

 Running a wrap shop and a meal prep company with it since March. These three took the longest to learn, and I paid the hours so you do not have to. Each one explained in plain English, then one prompt that sets all three up. Drop your email below and it unlocks. Nothing to buy.

 
 [Unlock the three + the prompt](#get)
 

 
 
 What&rsquo;s inside

 
## The three, one breath each

 
 
 01**It keeps a list of its own mistakes** · A mistake that is only a note is not learned. Every one has to become a check that runs on its own.
 02**The one that builds never grades** · A second Claude with no memory of the work grades it cold. D+ to A- in five passes.
 03**The greeting shapes who you think you are** · Mine opened with everything unfinished. Every morning. Now it opens with what is working.
 
 The full explanation of each one, the exact line to say to Claude Code for it, and the one-paste prompt that builds all three are below the form.

 

 
 
 Get the three + the prompt
 Enter your email and this playbook unlocks immediately. Just this one, not all of them.
 
 
 
 
 Already submitted and nothing happened? [Click here to unlock it.](#)

 
 
 The three is yours.
 The PDF should be downloading, and everything is unlocked below: the full explanations and the prompt with a copy button.

 [Download the PDF](/guides/playbooks/hours.pdf)
 Want a different one? [All the playbooks](/playbook/), one download each.

 
 

 
 
 Unlocked

 
## The three, explained

 

 
 1
 
 
### It keeps a list of its own mistakes

 Every AI forgets what it got wrong. So mine writes each mistake into one file the moment it happens: what went wrong, and what that mistake has to turn into. A hook that blocks it, a test that catches it, or a scheduled check that reports it. Thirty-six entries so far. The rule is simple: a mistake that is still just a note after one session was not learned.

 **How:** a file called `lessons.json` and one rule in CLAUDE.md: *When you get something wrong, add it to lessons.json the same turn with what happened and what it must become. Build that thing before the session ends and mark it implemented.* The first time it corrects itself you will feel the difference. The tenth time you will have a system that gets harder to fool every week.

 say: "add that to the lessons ledger"
 
 
 
 2
 
 
### The one that builds never grades

 Whoever writes a plan cannot see its own blind spot. Checking a connection you built feels sound from the inside. So a second Claude, a brand new process with no memory of the work, reads the plan file cold and grades it. It is only allowed to read, never to fix. Mine took a plan from a D+ to an A- in five passes and every single pass found something the author swore was fine. Same model both times. Different job, different blind spots.

 **How:** a two-line script, `grade.sh`, that starts a fresh `claude -p` with read-only tools and this job: *Read the file at this path. Grade it A to F. List every claim you cannot verify, every number with no source, and every step that cannot be run as written. Do not fix anything.* Then the rule: *Before I approve any plan you wrote, run grade.sh on it and show me the findings word for word.* Give it the PATH, never a summary. A summary is the author's framing all over again.

 say: "grade this plan cold"
 
 
 
 3
 
 
### The greeting shapes who you think you are

 A SessionStart hook is a tiny script that runs the second you open Claude Code, before you type a word. Mine used to print everything I had not finished. Every morning, the first thing I read was the to-do list. That was feeding a story about myself I am trying to get out from under. Now it prints what is working first, then what needs me. Same information, opposite effect. You talk to this thing every day. Design the greeting on purpose.

 **How:** a hook in `.claude/settings.json` under SessionStart that runs a small script. The script prints WORKING, three things shipped or running from the last week, then NEEDS ME, at most three. Working always prints first. Plus one rule in CLAUDE.md: *Open every session with what is working before what is unfinished. Never read the to-do list back to me as a greeting.*

 say: "lead with what is working"
 
 

 

 
 
 The prompt

 
## One paste sets up all three

 Copy it, open Claude Code inside the folder it already runs from, paste it, and answer its questions one at a time. It shows you everything it built at the end and runs the new greeting once.

 
 
 1Open the terminal inside your project folder.
 2Type `claude`.
 3Paste the prompt below and hit enter.
 
 
Set up three things in this folder. Ask me one question at a time when you need something from me, and explain what each thing DOES before how it works.

1. A LIST OF YOUR OWN MISTAKES. Create a file called lessons.json. Add this rule to CLAUDE.md: "When you get something wrong, or I correct you, add an entry to lessons.json the same turn with: what happened, the date, and what it must become: a hook that blocks it, a test that catches it, or a scheduled check that reports it. Then build that thing before the session ends and mark the entry implemented. An entry that is still only a note after one session means it was not learned." Then ask me for the last three times you or any AI got something wrong for me, and write them in as the first three entries, each with what it should become.

2. THE BUILDER NEVER GRADES. Create a short script called grade.sh that takes a file path and runs a brand new Claude Code process with read-only tools to grade it: claude -p "Read the file at $1. Grade it A to F. List every claim you cannot verify, every number that has no source, and every step that cannot be run as written. Do not fix anything, only report." --allowedTools "Read,Glob,Grep". Add this rule to CLAUDE.md: "Whoever writes a plan never grades it. Before I approve any plan you wrote, run grade.sh on the file and show me the grade and the findings word for word. Fix, regrade, repeat until it is an A or I say stop." Then explain to me, in plain English, why a fresh process with no memory of the work finds things you cannot.

3. THE GREETING. Set up a SessionStart hook that runs a small script every time I open Claude Code here, before I type anything. It prints two short blocks: WORKING, three things that are running or shipped, from the last week of git history and anything in a file called working.md, and then NEEDS ME, at most three things. Working always prints first. Add this rule to CLAUDE.md: "Open every session with what is working before what is unfinished. Never read the to-do list back to me as a greeting." Ask me what I want the WORKING block to pull from if there is no git history yet.

When all three are done, show me lessons.json, grade.sh, the hook, and the new lines in CLAUDE.md, and run the greeting once so I can see it.
 Copy the prompt
 
 Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on [@brycenwood.ai](https://www.instagram.com/brycenwood.ai/).
