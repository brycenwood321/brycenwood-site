---
title: The AI Editor: How I Have Claude Edit My Videos | Brycen Wood
description: How my AI video editor is set up, in plain English, plus the starter prompt that builds a basic one on your own computer: it cuts the dead air, cuts your retakes, and adds captions. Free.
url: https://www.brycenwood.com/edit/
last_updated: 2026-04-14
---

From the video · Free

 
# I film one messy take. AI does the edit.

 Here is how mine is set up, with nothing hidden, and the starter prompt that builds a basic version on your own computer. You talk to the camera once. It cuts the dead air and your retakes and adds the captions. Drop your email below and it unlocks. Nothing to buy.

 
 [Unlock the setup](#get)
 

 
 
 What&rsquo;s inside

 
## What the starter builds, one line each

 
 
 01**It hears every word** · It writes down what you said with a time for each word. Everything else is built on that.
 02**It cuts the dead air and your retakes** · Long pauses come out. When you say a line twice, it keeps the last one and shows you what it cut.
 03**It adds the captions** · A few words at a time, timed to your voice, sized for a phone.
 
 How mine works, three steps to build yours, and the prompt with a copy button. Unlocked by the form below.

 

 
 
 Get the setup
 Enter your email and this page unlocks immediately. Just this one, not all of them.
 
 
 
 
 Already submitted and nothing happened? [Click here to unlock it.](#)

 
 
 The setup is yours.
 Everything is unlocked below: how mine works, three steps, and the prompt with a copy button.

 Want more? [All the playbooks](/playbook/), one download each.

 
 

 
 
 Unlocked

 
## How mine works, then how to start yours

 
 
 1
 
 
### How mine is set up

 It runs in [Claude Code](https://claude.com/claude-code) on my own Mac. I drop in one take. One AI plans the cut and picks effects from a library I built with it over a few weeks. A second AI grades that plan and sends it back with a fix. Plain rules in code check the rest, like captions never covering my face.

 **The honest part.** Mine took weeks of me saying &ldquo;no, not like that.&rdquo; The starter below gets you the first three jobs on day one: dead air, retakes, captions. The fancy stuff comes from giving it notes.

 
 
 
 2
 
 
### Make a folder and put one clip in it

 Any talking video from your phone works. Open Claude Code in that folder. Claude Code needs a paid Claude plan, and everything else it uses is free and runs on your computer.

 
 
 
 3
 
 
### Paste the prompt, then give it notes

 It builds the editor, runs it on your clip, and tells you what it cut. Watch the video once. Then tell it what you did not like in plain words, and it fixes the editor itself, so the next video comes out better.

 **Watch before you post.** It will miss things at first. Mine still gets a note from me now and then.

 
 
 

 
 
 The prompt

 
## Copy, paste, drop in a clip

 Tested once on a 20 second practice clip before it went on this page: it took out the long pauses, cut a line that was started twice, and added the captions (20 seconds became 9). That clip was a computer voice, not a real person, so watch your first cut.

 
 
 1Put one clip in a folder.
 2Open Claude Code there and paste the prompt.
 3Watch it once, then give it notes.
 
 
I want you to be my video editor. I film myself talking to the camera in one messy take, and I want a clean, captioned vertical video back without editing it myself. I am not technical, so keep it simple: ask me one question at a time, explain what each thing DOES in one sentence before you do it, and never ask me to write or read code.

First, look in this folder for a video file. If there is more than one, ask me which one. If there is none, tell me to drag my clip into this folder and wait.

Then build me a small editing tool in this folder and run it on my clip. Use free tools that run on my own computer (ffmpeg for the video, a local Whisper model for the words; use the small "base" model so an ordinary laptop can run it). If something is not installed, tell me in one sentence what it is and install it for me. Install anything Python inside a virtual environment in this folder, never system-wide. If one tool fails, find another way yourself instead of asking me to fix it. The tool does four things, in this order:

1. HEAR EVERY WORD. Transcribe the clip with a time for every word. Save the transcript so I can read it.

2. CUT THE DEAD AIR. Remove silences longer than about half a second, and trim the silence at the very start and end, leaving a tiny bit of breathing room so no word gets clipped.

3. CUT MY MISTAKES. When I start a sentence, stop, and say it again, keep only the LAST full version. Here is how to find them: split what I said into phrases at every pause and every full stop. If a phrase starts with the same three or more words as a phrase that comes soon after it, the earlier one is a failed attempt, so cut the WHOLE earlier phrase, even when there is a long pause between them and even when the failed attempt is long. Check again after cutting, because I sometimes try a line three times. Show me a short list of what you cut and why, in plain words, before you render. If you are not sure whether something is a mistake, keep it and tell me.

4. ADD CAPTIONS. Burn captions onto the video, two to four words at a time, timed to my voice, big and easy to read on a phone, in the lower middle of the screen and never covering my face. If your ffmpeg cannot draw text, draw each caption as an image and lay it over the video instead.

Save the result as a NEW file next to my clip. Never change or delete my original. If my clip is sideways (horizontal), ask me if I want it cropped to vertical for Reels and TikTok, and keep my face in the middle if I say yes.

When it is done, check your own work: you cannot watch video, so transcribe the NEW file and read it. Every sentence should appear once, no failed attempt should be left in, and the first and last words should be whole. Look at one still frame to check the captions. If the check finds a problem, fix it and check again before you show me. Then tell me where the new file is, how long the original was, how long the new one is, and what you cut. Then ask me what I want changed. When I give you a note (for example "the captions are too small" or "you cut a word at 0:12"), fix the tool itself, not just this one video, so it gets better every time I use it.

Do not add music, effects or zooms unless I ask. Do not promise the cut is perfect; tell me to watch it once before I post.
 Copy the prompt
 
 Nothing to buy here. If it helps, that is the whole point. I post what I learn as I build on [@brycenwood.ai](https://www.instagram.com/brycenwood.ai/).
