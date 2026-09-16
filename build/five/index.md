---
title: 5 Things That Make Claude Code a System, Not a Chatbot | Brycen Wood
description: A folder, a memory, a rules-only file, a model table, and never trusting done. Each one explained in plain English, plus one prompt that sets all five up for you.
url: https://www.brycenwood.com/five/
last_updated: 2026-04-14
---

From the video · Free Playbook

 
# 5 things that make Claude Code a system, not a chatbot

 Each one explained the way I wish someone had explained it to me. Then one prompt that sets all five up for you. Drop your email below and it unlocks. I do not write code. Neither will you.

 
 [Unlock the five + the prompt](#get)
 

 
 
 What&rsquo;s inside

 
## The five, one breath each

 
 
 01**Work out of a folder, not a chat** · Everything it needs to know becomes a file it can open.
 02**Give it a memory** · A folder it writes to before it closes and reads before it starts.
 03**Rules only in the main file** · With a line cap. Everything else lives somewhere it can look up.
 04**One table: which model for which job** · It looks the job up. It never guesses. About seven times cheaper.
 05**Never trust done** · Nothing is done until it shows you the log. A hook blocks what it cannot undo.
 
 The full explanation of each one, the exact line to say to Claude Code for it, and the one-paste prompt that builds all five are below the form.

 

 
 
 Get the five + the prompt
 Enter your email and this playbook unlocks immediately. Just this one, not all of them.
 
 
 
 
 Already submitted and nothing happened? [Click here to unlock it.](#)

 
 
 The five is yours.
 The PDF should be downloading, and everything is unlocked below: the full explanations and the prompt with a copy button.

 [Download the PDF](/guides/playbooks/five.pdf)
 Want a different one? [All the playbooks](/playbook/), one download each.

 
 

 
 
 Unlocked

 
## The five, explained

 

 
 1
 
 
### Work out of a folder, not a chat

 A chat forgets everything the second you close it. A folder does not. When Claude Code runs inside a folder, every file in it is something it can go open and read on its own, so you stop re-explaining your business every morning.

 **How:** make a folder for the project. Open the terminal inside it and type `claude`. The first thing you say is *"run init"*. It writes a file called CLAUDE.md. That file is read at the start of every session. It is where you tell it who you are, what this is, and how you want it to talk to you.

 say: "run init"
 
 
 
 2
 
 
### Give it a memory

 Memory is not magic. It is a folder plus one rule. Mine has over five hundred files in it, one fact per file, and one index file that lists them in a line each. Tomorrow's session reads the index first and knows what yesterday learned.

 **How:** add a folder called `memory` with a `MEMORY.md` index inside it. Then put one rule in CLAUDE.md: *"Before a session ends, write anything durable you learned as one file in memory/ and add a one-line pointer to MEMORY.md. Read MEMORY.md at the start of every session."* Then actually say *"write down what you learned"* before you close. The rule is the habit. The folder is just where it lands.

 say: "write down what you learned"
 
 
 
 3
 
 
### Rules only in the main file

 CLAUDE.md loads on every single request. Every line in it costs attention on everything it does. So the more you "help" it by stuffing that file, the worse it gets. Mine is rules only, with a hard line cap.

 **How:** add this rule to CLAUDE.md: *"This file is rules only and stays under 150 lines. Anything only needed sometimes goes in its own file and this file points to it."* Then ask it to check the current file against that rule and move anything that is not a rule. The wrap-shop details go in a wrap-shop file. The main file just says where that file is.

 say: "check CLAUDE.md against the rules-only rule"
 
 
 
 4
 
 
### One table: which model for which job

 Claude comes in sizes. The biggest brain costs about seven times more per call than the smallest. If you let it guess, it uses the biggest brain to rename a file. One small table fixes that forever.

 **How:** add a section to CLAUDE.md called *Which model for which job*. Sorting, extracting, summarizing and routing go to the smallest model. Drafting, analysis and generating go to the middle one. Reviewing work and design decisions go to the biggest. Then the rule that makes it stick: *"When you spawn an agent or write a script that calls the API, look the job up in this table. Never guess."*

 say: "add the model table and never guess"
 
 
 
 5
 
 
### Never trust done

 Mine once told me a message queue had sent zero. Meanwhile 162 customers had already been answered. Both were true. It was reading its own notes instead of the actual log. Confident is not the same as true.

 **How:** two rules in CLAUDE.md: *"Nothing is done until you show me the actual output or log, never your summary of it."* and *"A command that exits clean with no output is a failure, not a pass."* Then the one that matters most, a **hook**: a tiny script that runs before every command it tries and blocks anything that deletes files or spends money. A rule is something it tries to follow. A hook is something it cannot get past. Ask it to build the hook and explain what it blocks before it saves it.

 say: "show me the log, not your summary"
 
 

 

 
 
 The prompt

 
## One paste sets up all five

 Copy it, open Claude Code inside the folder you want it to run from, paste it, and answer its questions one at a time. It shows you everything it built at the end.

 
 
 1Make a folder for the project. Any name.
 2Open the terminal inside that folder and type `claude`.
 3Paste the prompt below and hit enter.
 
 
Set up this folder as a system, not a chat. Do these five things, and ask me one question at a time when you need something from me.

1. FOLDER. If there is no CLAUDE.md here, create one. Ask me what this project is, who I am, and how I want you to talk to me. Keep it short.

2. MEMORY. Create a folder called memory with a MEMORY.md index inside. Add this rule to CLAUDE.md: "Before a session ends, write anything durable you learned (a preference, a gotcha, a decision and why) as one file per fact in memory/, and add a one-line pointer to MEMORY.md. Read MEMORY.md at the start of every session."

3. RULES ONLY. Add this rule to CLAUDE.md: "This file is rules only and stays under 150 lines. Anything only needed sometimes goes in its own file under docs/ and this file points to it." Then check the current file against that and move anything that is not a rule.

4. MODEL TABLE. Add a section to CLAUDE.md called Which model for which job, with a table: classify, extract, summarize and route go to the smallest model; drafting, analysis and generating go to the middle model; reviewing work and design decisions go to the largest model. Add the rule: "When you spawn an agent or write a script that calls the API, look the job up in this table. Never guess."

5. TRUST. Add these rules to CLAUDE.md: "Nothing is done until you show me the actual output or log, never your summary of it." and "A command that exits clean with no output is a failure, not a pass." Then set up a PreToolUse hook that runs before every Bash command and blocks anything that deletes files, force-pushes, or spends money. Explain to me in plain English what it blocks before you save it.

When all five are done, show me the CLAUDE.md, the memory folder, and the hook, and tell me the one thing you would add next.
 Copy the prompt
 
 Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on [@brycenwood.ai](https://www.instagram.com/brycenwood.ai/).
