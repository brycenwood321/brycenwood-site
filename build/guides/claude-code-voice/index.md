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

This is the whole thing. Open Claude Code in any folder, paste this in, and answer its questions as it goes. It will tell you what it is doing in plain English as it builds.

```
I want Claude Code to read its answers to me out loud, so working
with you is a conversation instead of me reading a screen. I am not
a programmer, so explain what you are doing in plain English as you
go, and do not assume I know what any of these pieces are.

Build this on my machine:

1. A Stop hook that speaks your final message aloud when you finish
 a turn. Use whatever text to speech is already built into my
 operating system. Nothing paid, no API key.

2. IMPORTANT: do not read the whole message. Reading a long technical
 answer out loud is unbearable. Instead:
 - Let you write a short spoken summary inside a marker in your
 message, and speak ONLY that, verbatim.
 - If there is no marker, fall back to reading just the opening
 prose and stop at the first heading or bullet, capped at about
 30 seconds.
 - Strip code blocks, file paths, and URLs before speaking, since
 they are unlistenable.

3. A hook on prompt submission that kills any speech in progress,
 so when I start talking back it shuts up immediately. It must
 NOT touch my on/off setting.

4. A command called `voice` I can run from any terminal that
 controls every session at once:
 - voice off / voice on
 - voice stop (kill the sentence in progress right now)
 - voice status (is it on, which voice, is it speaking)
 - voice test (say a sample line)
 - voice again (replay the last thing it said, for when I miss it)

5. A way for you to speak DURING a turn, not only at the end, so you
 can tell me something important the moment you find it instead of
 saving it for the summary. Make it non-blocking so it never slows
 the work down.

Handle these three failure cases, because they are the ones that
will actually bite:

- If I have two Claude sessions running and both finish at once,
 they must not talk over each other. Use a lock and queue the
 second one.
- Make sure the hook reads my FINAL answer, not mid-work narration.
 Solve this structurally. Do not paper over it with a timing delay,
 because a delay will look fine and then break on a long turn.
- Make sure `voice stop` genuinely kills speech mid sentence. Prove
 it to me by testing it while a long sentence is playing, not just
 by showing me that it prints a confirmation.

Then write me a test suite that verifies all of it, and make sure
the tests DO NOT speak out loud when they run.

Before you start, tell me your plan and what you are about to change
on my machine. Then build it, test it, and tell me exactly how to
turn it off if I hate it.
```

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
