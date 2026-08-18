---
title: Make Claude Code Talk Back: The Voice Setup I Built in a Truck | Brycen Wood
description: Talk to Claude Code and have it read the answer out loud. The full walkthrough plus the exact copy-paste prompt that builds it, from a founder who does not write code.
url: https://www.brycenwood.com/guides/claude-code-voice/
last_updated: 2026-04-14
---

Free Walkthrough
 
# Make Claude Code Talk Back To You

 I dictate a question. It answers out loud. I built the whole thing on a road trip, and I do not write code. Here is how it works and the exact prompt that builds it.

 Last updated: August 18, 2026
 

## Why I built this

I already talked *to* Claude Code. I use a dictation tool, so I stopped typing prompts a long time ago. The problem was the other direction. Claude would answer, and the answer would be a wall of text on a laptop screen I was not looking at.

I run three businesses. A lot of my actual work happens while I am driving, walking around a shop, or sitting in a different terminal doing something else. In all of those situations the screen is useless to me and the information is still important.

So I made it talk. Now it is a conversation. I ask whether everyone paid this week, and it tells me, out loud, while my hands stay on the wheel.

> The unlock is not text to speech. It is that Claude writes a short spoken summary of its own answer, and reads you that instead of the transcript.

## What it actually does

 - **Reads the answer, not the message.** Claude writes a summary meant to be heard, and only that gets spoken. No file paths, no code, no bullet points read aloud like a robot.
 - **Stops when you talk.** Start speaking and the voice cuts off mid sentence. You never sit there waiting for it to finish.
 - **Talks during the work, not just at the end.** If it finds something that changes what you would do, it says so immediately instead of banking it for the closing summary.
 - **Says the important thing first.** Answer up front, in case you stop listening.
 - **Has an off switch that works everywhere.** One command silences every session at once.
 - **Replays.** A semi goes past, you miss half a sentence, you say replay instead of asking the whole question again.

## How it works, in plain English

Claude Code has something called hooks. A hook is just a command that runs automatically when a certain thing happens. You do not have to write software to use them. You write a small script and tell Claude Code when to run it.

 
 1
 
 
### Dictation in

 This part is not custom. Any good dictation tool lets you talk into the Claude Code prompt instead of typing. This is the half most people already have and never think of as part of a system.

 
 

 
 2
 
 
### A Stop hook speaks the answer

 The Stop hook fires when Claude finishes its turn. It hands your script the finished message, and the script speaks it. On a Mac the speaking part is built into the operating system already, so there is no account to make and nothing to pay for.

 
 

 
 3
 
 
### Claude writes its own spoken summary

 This is the piece that makes it good instead of annoying. Reading a long technical message out loud is unbearable. Instead, Claude writes a short spoken version of the answer inside a marker, and the script reads only that. Everything else on screen is ignored.

 Without a summary, a fallback reads just the opening prose and stops at the first heading, capped at about thirty seconds.

 
 

 
 4
 
 
### A second hook makes it interruptible

 A hook on prompt submission kills any speech in progress. So the moment you start talking back, it stops. This one detail is the difference between a feature you keep and one you turn off in a day.

 
 

 
 5
 
 
### A small command gives you control

 Off, on, stop, status, test, and replay, from any terminal, applying to every session at once. You want this before you want anything fancy, because the first time it talks at a bad moment you need one word that stops it.

 
 

## Three things that broke, so yours does not have to

I am putting these here because they are the parts you would spend an evening on, and none of them announce themselves.

 - **Two sessions talking over each other.** If you run Claude in more than one terminal and both finish around the same time, you get two voices at once. It needs a lock so the second one waits its turn.
 - **It reads the wrong thing.** If the hook fires before the final message is finished, it reads mid-work narration instead of the answer. The fix is structural, not a timing delay. A delay looks like it works and then fails on a long turn.
 - **The off switch that quietly does nothing.** Mine looked like it worked for a while because a backup cleanup was doing the real work. Test that your stop command actually stops it, in the middle of a long sentence, not just that it prints a confirmation.

## The prompt

The full copy-paste prompt that builds this, plus the twelve other systems that run my businesses, is in the playbook. It is free.

[Get the playbook (free)](/playbook/)

System 13 is this one, written out step by step, including the three bugs above and the rule for what is worth saying out loud.

## Two notes before you paste it

**It changes settings that need a restart.** Some of the wiring is read fresh every time, and some is loaded once when a session starts. If a piece does not seem to work right away, restart Claude Code before you assume it is broken.

**Start with the off switch working.** Ask for that first and confirm it, then add the rest. The failure mode you care about is not that it fails to talk, it is that it talks when you do not want it to.

## Questions I got asked

 
 Do I need to know how to code?+
 No. I do not. Every part of this was built by describing what I wanted in plain English and answering questions. The prompt above is written to be pasted in as is.

 
 
 Does this cost anything?+
 The speaking part is built into the operating system, so there is no extra subscription and no API key for the voice itself. You are already paying for Claude Code.

 
 
 Will it read every single thing out loud?+
 Only if you build it badly. The whole point of the summary step is that you hear the answer, not the transcript. If it is reading you file paths, that part is not finished yet.

 
 
 What if I am on Windows?+
 The structure is identical, hooks are hooks. The only piece that changes is which built-in command speaks the text. Say so in the prompt and let Claude pick the right one for your machine.

 
 
 Is this actually useful or is it a toy?+
 Fair question. For me the test was whether I still used it a week later, and I do, because a lot of my work happens away from a screen. If you are always sitting at your desk looking at the terminal, you probably do not need this.

 

## If you build it

Send me what you made. I read every message and the good ideas end up in the next version of mine. That is the only thing I want in return for this.

[Back to all guides](/guides/)
