---
title: The Watcher Prompt: An AI That Checks Your Other AIs | Brycen Wood
description: If you have jobs running on their own, the scary part is one breaking quietly and saying everything is fine. One prompt builds a watcher that checks each job actually produced something, and only speaks when something needs you.
url: https://www.brycenwood.com/watch/
last_updated: 2026-04-14
---

From the video · Free

 
# Who checks the robots? An AI that watches the others.

 I have AI jobs running my businesses every night: leads, texts, reports, backups. One more job checks that all the others actually made something, and it only speaks up when something needs me. Here is how it thinks, and the prompt that builds your own. Drop your email below and it unlocks. Nothing to buy.

 
 [Unlock the watcher prompt](#get)
 

 
 
 What&rsquo;s inside

 
## The watcher, one breath each

 
 
 01**Ran is not the same as worked** · It checks the thing each job was supposed to leave behind, not just that the job ran.
 02**It only speaks when it matters** · Quiet when everything is fine. One line per problem when something is not.
 03**One prompt builds yours** · Lists your jobs with you, builds the watcher, then breaks something on purpose to prove it works.
 
 The four ideas behind it, in plain English, and the prompt that builds it. Unlocked by the form below.

 

 
 
 Get the watcher prompt
 Enter your email and this page unlocks immediately. Just this one, not all of them.
 
 
 
 
 Already submitted and nothing happened? [Click here to unlock it.](#)

 
 
 The watcher is yours.
 Everything is unlocked below: how it thinks, and the prompt with a copy button.

 Want more? [All the playbooks](/playbook/), one download each.

 
 

 
 
 Unlocked

 
## How the watcher thinks

 
 
 1
 
 
### &ldquo;Ran&rdquo; is not the same as &ldquo;worked&rdquo;

 The scary part is not a job breaking. It is a job breaking quietly and saying everything is fine. A job can run, hit a snag, write an empty file and still report success. So the watcher checks what the job was supposed to leave behind: the report, the row in the sheet, the sent email, the backup. Was it made, is it new, and does it look like the last few?

 **The rule it is built on:** a false green is worse than a red. An error gets fixed, because you see it. A false &ldquo;all good&rdquo; sits there for weeks, because nobody looks.

 say: "check what it made, not that it ran"
 
 
 
 2
 
 
### Write down what each job should produce

 Before a watcher can judge anything, it needs to know what normal looks like: each job's name, when it runs, and what it leaves behind when it works. The prompt walks you through that list first.

 **One more rule:** if the watcher cannot see a job's output at all, it says &ldquo;cannot check&rdquo;. Never &ldquo;OK&rdquo;.

 
 
 
 3
 
 
### Only speak when something needs you

 My watcher once sent me 16 alerts, and 11 of them were noise. So I stopped reading all of them, including the 5 that mattered. Now it stays quiet when everything is fine, and when something breaks it sends one line per problem: which job, what is wrong, what to do first.

 **Why it matters:** an alert you have learned to ignore is the same as no alert.

 
 
 
 4
 
 
### Prove it by breaking something

 Before you trust it, break one job on purpose (rename a test file) and make sure the watcher catches it. A check that has never failed has never been tested. The prompt does this for you before anything gets switched on.

 
 
 

 
 
 The prompt

 
## One paste builds your watcher

 Copy it, open Claude Code in the folder where your jobs live (or anywhere, and tell it where they are), paste it, and answer its questions one at a time. Before anything is switched on, it shows you what it would have said today.

 
 
 1Open the terminal inside the folder where your jobs or scripts live.
 2Type `claude`.
 3Paste the prompt below and hit enter.
 
 
I have jobs that run on their own: scheduled scripts, automations, AI tasks. I want ONE watcher that checks each job actually PRODUCED something, not just that it ran. Ask me one question at a time, and explain what each piece DOES before how it works.

Step 1. Help me list every job: its name, when it runs, and what it should leave behind when it works (a file, a row in a spreadsheet, a sent email, a report, a backup). If I don&#x27;t know where a job leaves its output, look in this folder and help me find it.

Step 2. Build a watcher that runs once a day, after the jobs should be finished, and checks each job:
- The output exists AND is new since the job&#x27;s last scheduled run. A file that is there but old is a failure.
- The output is not empty and looks normal next to its last few runs. A report with 0 rows when it usually has 40 is a failure, even if the job said "success".
- Give each job one of: OK, LATE, EMPTY, MISSING, or CANNOT CHECK.

Rules:
- A job that says success but left nothing behind is a FAILURE. A false "all good" is worse than an error, because nobody looks.
- If the watcher cannot see a job&#x27;s output at all (wrong folder, no access), it says CANNOT CHECK. Never OK.
- Stay silent when everything is OK. When something needs me, send ONE short message: which job, what is wrong, what to do first. One line per problem. No list of the things that worked.
- Before you switch it on, run it once and show me what it would have said today. Then break one job on purpose (rename a test output file) and show me the watcher catches it. Put the file back after.

Last, tell me how to schedule it on my computer, how to change where the message goes (text, email or just a file I open), and how to turn it off.
 Copy the prompt
 
 Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on [@brycenwood.ai](https://www.instagram.com/brycenwood.ai/).
