"""
Schedule Carousels — Creates all carousel containers via Instagram API.
Containers can then be published immediately or on a schedule.

Usage:
  python3 personal/brycenwood-site/schedule_carousels.py --create-all     # Create all containers
  python3 personal/brycenwood-site/schedule_carousels.py --publish 1      # Publish carousel #1
  python3 personal/brycenwood-site/schedule_carousels.py --publish-next   # Publish next scheduled carousel
  python3 personal/brycenwood-site/schedule_carousels.py --status         # Show status of all carousels
"""
import os, sys, json, time, requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, "summit-wraps", "lead-engine"))
import ig_api

API = "https://graph.instagram.com/v21.0"
IMG_BASE = "https://hq.summitwrapsandgraphics.com/downloads"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "carousel_state.json")

# ── Carousel definitions ──
CAROUSELS = {
    1: {
        "name": "10 Things My AI Does While I Sleep",
        "folder": "01",
        "slides": 10,  # skip bonus quote slide (11)
        "date": "2026-04-14",
        "caption": """While you sleep, my AI sends cold emails, classifies replies, moves leads through my pipeline, cross-posts to YouTube, monitors all 17 systems, and scrapes my competitors.

I built all of this with zero coding experience using Claude Code.

I'm breaking down every system inside a free community. The prompts, the tools, the mistakes, all of it.

Comment BUILD to get on the waitlist.

#claudecode #ai #aiautomation #smallbusiness #entrepreneur #aiforbusiness"""
    },
    2: {
        "name": "You vs My AI",
        "folder": "02",
        "slides": 8,
        "date": "2026-04-16",
        "caption": """Still doing everything manually?

My AI sends 5,500 personalized emails. Briefs me before I wake up. Cross-posts my content. Manages my DMs. Follows up with every lead. And built my website.

I didn't write a single line of code.

Comment BUILD to get on the waitlist for the free community where I break down every system.

#ai #aiautomation #smallbusiness #entrepreneur #businessowner #claudecode"""
    },
    3: {
        "name": "80+ Automations Full List",
        "folder": "03",
        "slides": 12,
        "date": "2026-04-18",
        "caption": """80+ automations. 10 APIs. 24 cron jobs running 24/7. Zero coding experience.

Here's every single system I built for my business using Claude Code.

Save this for later. I'm breaking down each one inside a free community.

Comment BUILD to get on the waitlist.

#claudecode #ai #aiautomation #smallbusiness #entrepreneur #aiforbusiness #automation"""
    },
    4: {
        "name": "5 AI Tools That Run My Business",
        "folder": "04",
        "slides": 7,
        "date": "2026-04-20",
        "caption": """My entire business runs on 5 tools. No employees. No agencies. No developers.

1. Claude Code — builds everything
2. GoHighLevel — runs my CRM
3. ElevenLabs — cloned my voice ($5/mo)
4. Manychat — automated DM funnel (45% CTR)
5. Cloudflare — makes my laptop a web server

Comment BUILD to get on the waitlist for the free community where I break it all down.

#techstack #ai #smallbusiness #claudecode #entrepreneur #tools #automation"""
    },
    5: {
        "name": "What AI Actually Looks Like",
        "folder": "05",
        "slides": 8,
        "date": "2026-04-22",
        "caption": """AI isn't ChatGPT writing you a poem. This is what it actually looks like when you use it to run a real business.

Morning briefings. Automated cold email. DM personalization. Sales pipeline on autopilot. Voice clone. Business dashboard from my phone.

All built with zero coding experience.

Comment BUILD to join the free community where I break down every system.

#ai #aiforbusiness #smallbusiness #entrepreneur #claudecode #automation #realbusiness"""
    },
    6: {
        "name": "0 to 7,000 Followers in 3 Weeks",
        "folder": "06",
        "slides": 9,
        "date": "2026-04-24",
        "caption": """3 weeks ago I had zero followers. Today I have 7,000+, 1.1 million video views, and 1,374 people on a waitlist.

No ads. No agency. No viral hack. Just real content about real systems I actually built.

Here's the week-by-week breakdown of exactly what happened.

Comment BUILD to join the free community.

#growthhacking #instagramgrowth #ai #entrepreneur #zerotoone #smallbusiness #claudecode"""
    },
    7: {
        "name": "3 Files for AI Recommendations",
        "folder": "07",
        "slides": 8,
        "date": "2026-04-26",
        "caption": """ChatGPT recommends my vehicle wrap business by name. Three text files made it happen.

1. llms.txt — tells AI what your business does
2. Markdown mirrors — clean versions AI can actually read
3. Updated sitemap — tells crawlers where everything is

1.1 million people watched me prove this on camera.

Comment BUILD to join the free community where I show you how to set it up.

#seo #aiseo #chatgpt #llmstxt #smallbusiness #claudecode #digitalmarketing"""
    },
    8: {
        "name": "Morning Briefing Breakdown",
        "folder": "08",
        "slides": 8,
        "date": "2026-04-28",
        "caption": """Every morning at 8 AM, my AI generates a full briefing before I wake up.

Top priorities ranked by impact. Pipeline status. What my AI did overnight. Today's calendar. Even my habit streaks.

17 automations feed into one screen. I open my phone and know exactly what to do.

Zero coding experience. Built entirely with Claude Code.

Comment BUILD to get on the waitlist for the free community.

#morningroutine #productivity #ai #automation #smallbusiness #claudecode #entrepreneur"""
    },
    9: {
        "name": "5,500 Personalized Emails",
        "folder": "09",
        "slides": 9,
        "date": "2026-04-30",
        "caption": """My AI read 5,500 websites and wrote a personalized cold email for every single one. Overnight.

Here's the 6-step system:
1. Score every lead (A/B/C)
2. Read their website
3. Write a custom email
4. Send 15/day automatically
5. Detect and classify replies
6. Follow up at the right time

$0 spent on developers. Zero coding experience.

Comment BUILD to join the free community where I break it all down.

#coldemail #leadgeneration #ai #automation #smallbusiness #claudecode #sales"""
    },
    10: {
        "name": "$3,600 Saved",
        "folder": "10",
        "slides": 8,
        "date": "2026-05-02",
        "caption": """I was paying $400/month for my CRM through a reseller. The same software costs $97/month direct.

I told my AI to migrate everything. 192 contacts. 160 opportunities. 33 custom fields. Done.

$3,600 saved per year. One conversation with Claude Code.

What's your business overpaying for?

Comment BUILD to join the free community.

#crm #businesstips #savemoney #ai #automation #smallbusiness #claudecode #entrepreneur"""
    },
}


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def create_carousel(num):
    """Create a carousel container via the API. Returns container ID."""
    c = CAROUSELS[num]
    token = ig_api._account("brycenwood.ai")["access_token"]
    uid = ig_api._user_id("brycenwood.ai")

    print(f"\n{'='*60}")
    print(f"Creating Carousel #{num}: {c['name']}")
    print(f"{'='*60}")

    # Step 1: Create image containers
    slide_ids = []
    for i in range(1, c["slides"] + 1):
        img_url = f"{IMG_BASE}/c{c['folder']}_slide_{i:02d}.png"
        r = requests.post(f"{API}/{uid}/media", data={
            "image_url": img_url,
            "is_carousel_item": "true",
            "access_token": token,
        }, timeout=15)
        if r.status_code == 200:
            cid = r.json()["id"]
            slide_ids.append(cid)
            print(f"  Slide {i}/{c['slides']}: {cid}")
        else:
            print(f"  Slide {i} FAILED: {r.text[:200]}")
            return None
        time.sleep(0.5)

    # Step 2: Create carousel container
    print(f"\n  Creating carousel container ({len(slide_ids)} slides)...")
    r = requests.post(f"{API}/{uid}/media", data={
        "media_type": "CAROUSEL",
        "children": ",".join(slide_ids),
        "caption": c["caption"],
        "access_token": token,
    }, timeout=15)

    if r.status_code == 200:
        container_id = r.json()["id"]
        print(f"  Container created: {container_id}")
        return container_id
    else:
        print(f"  FAILED: {r.text[:300]}")
        return None


def publish_carousel(num):
    """Publish a previously created carousel container."""
    state = load_state()
    key = str(num)
    if key not in state or "container_id" not in state[key]:
        print(f"Carousel #{num} has no container. Run --create-all first.")
        return False

    if state[key].get("published"):
        print(f"Carousel #{num} already published!")
        return False

    token = ig_api._account("brycenwood.ai")["access_token"]
    uid = ig_api._user_id("brycenwood.ai")
    container_id = state[key]["container_id"]

    print(f"Publishing Carousel #{num}: {CAROUSELS[num]['name']}...")
    r = requests.post(f"{API}/{uid}/media_publish", data={
        "creation_id": container_id,
        "access_token": token,
    }, timeout=15)

    if r.status_code == 200:
        media_id = r.json()["id"]
        state[key]["published"] = True
        state[key]["media_id"] = media_id
        state[key]["published_at"] = time.strftime("%Y-%m-%d %H:%M")
        save_state(state)
        print(f"  Published! Media ID: {media_id}")
        return True
    else:
        print(f"  FAILED: {r.text[:300]}")
        return False


def create_all():
    """Create containers for all carousels."""
    state = load_state()
    for num in sorted(CAROUSELS.keys()):
        key = str(num)
        if key in state and state[key].get("container_id"):
            print(f"Carousel #{num} already has container: {state[key]['container_id']}")
            continue

        container_id = create_carousel(num)
        if container_id:
            state[key] = {
                "name": CAROUSELS[num]["name"],
                "container_id": container_id,
                "scheduled_date": CAROUSELS[num]["date"],
                "published": False,
                "slides": CAROUSELS[num]["slides"],
            }
            save_state(state)
        time.sleep(1)

    print(f"\n{'='*60}")
    print("All containers created! Use --publish N to publish.")
    show_status()


def publish_next():
    """Publish the next scheduled carousel that hasn't been published yet."""
    state = load_state()
    for num in sorted(CAROUSELS.keys()):
        key = str(num)
        if key in state and not state[key].get("published"):
            publish_carousel(num)
            return
    print("All carousels already published!")


def show_status():
    """Show status of all carousels."""
    state = load_state()
    print(f"\n{'='*60}")
    print("CAROUSEL STATUS")
    print(f"{'='*60}")
    for num in sorted(CAROUSELS.keys()):
        c = CAROUSELS[num]
        key = str(num)
        s = state.get(key, {})
        status = "PUBLISHED" if s.get("published") else ("READY" if s.get("container_id") else "NOT CREATED")
        icon = "✅" if status == "PUBLISHED" else ("📦" if status == "READY" else "⬜")
        pub_date = s.get("published_at", c["date"])
        print(f"  {icon} #{num:2d} | {c['date']} | {status:12s} | {c['name']}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  --create-all     Create all carousel containers")
        print("  --publish N      Publish carousel #N")
        print("  --publish-next   Publish next unpublished carousel")
        print("  --status         Show status of all carousels")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "--create-all":
        create_all()
    elif cmd == "--publish":
        num = int(sys.argv[2])
        publish_carousel(num)
    elif cmd == "--publish-next":
        publish_next()
    elif cmd == "--status":
        show_status()
