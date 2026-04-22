"""
Auto-publish scheduled carousels — runs daily at 9:55 AM via LaunchAgent.
Publishes today's carousel AND retries any past-due unpublished carousels.
If an old container is stale, recreates it fresh before publishing.
"""
import os, sys, json, time, requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, "summit-wraps", "lead-engine"))
import ig_api

# Import carousel definitions for recreation
from schedule_carousels import CAROUSELS

API = "https://graph.instagram.com/v21.0"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "carousel_state.json")
LOG_FILE = os.path.join(BASE_DIR, "_data", "logs", "carousel_publish.log")
IMG_BASE = "https://hq.summitwrapsandgraphics.com/downloads/carousels"

MAX_RETRIES = 2
RETRY_DELAY = 5


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def try_publish(uid, token, container_id):
    """Attempt to publish. Returns media_id on success, None on failure."""
    r = requests.post(f"{API}/{uid}/media_publish", data={
        "creation_id": container_id,
        "access_token": token,
    }, timeout=30)

    if r.status_code == 200:
        return r.json()["id"]

    log(f"    Publish failed: {r.status_code} {r.text[:200]}")
    return None


def recreate_container(num, uid, token):
    """Create a fresh carousel container from scratch. Returns container_id or None."""
    c = CAROUSELS.get(num)
    if not c:
        log(f"    No carousel definition for #{num}")
        return None

    log(f"    Recreating container (stale) — {c['slides']} slides...")
    slide_ids = []
    for i in range(1, c["slides"] + 1):
        img_url = f"{IMG_BASE}/{c['folder']}/slide_{i:02d}.png"
        r = requests.post(f"{API}/{uid}/media", data={
            "image_url": img_url,
            "is_carousel_item": "true",
            "access_token": token,
        }, timeout=15)
        if r.status_code == 200:
            slide_ids.append(r.json()["id"])
        else:
            log(f"    Slide {i} failed: {r.text[:150]}")
            return None
        time.sleep(0.5)

    r = requests.post(f"{API}/{uid}/media", data={
        "media_type": "CAROUSEL",
        "children": ",".join(slide_ids),
        "caption": c["caption"],
        "access_token": token,
    }, timeout=15)

    if r.status_code == 200:
        container_id = r.json()["id"]
        log(f"    New container: {container_id}")
        # Wait for processing
        time.sleep(8)
        return container_id

    log(f"    Container creation failed: {r.text[:200]}")
    return None


def publish():
    today = datetime.now().strftime("%Y-%m-%d")
    state = load_state()

    log(f"Checking schedule for {today}...")

    published_any = False
    for key, info in sorted(state.items(), key=lambda x: x[0]):
        scheduled = info.get("scheduled_date", "")
        if scheduled <= today and not info.get("published"):
            container_id = info.get("container_id")
            if not container_id:
                log(f"  Carousel #{key} has no container ID, skipping")
                continue

            token = ig_api._account("brycenwood.ai")["access_token"]
            uid = ig_api._user_id("brycenwood.ai")

            past_due = " (PAST DUE)" if scheduled < today else ""
            log(f"  Publishing Carousel #{key}: {info.get('name', '?')}{past_due}...")

            # Try existing container first
            media_id = try_publish(uid, token, container_id)

            # If failed, recreate container and retry
            if not media_id:
                log(f"    Old container stale, recreating...")
                num = int(key)
                new_container = recreate_container(num, uid, token)
                if new_container:
                    info["container_id"] = new_container
                    save_state(state)
                    media_id = try_publish(uid, token, new_container)

            if media_id:
                info["published"] = True
                info["media_id"] = media_id
                info["published_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_state(state)
                log(f"  SUCCESS! Media ID: {media_id}")
                published_any = True
                time.sleep(2)
            else:
                log(f"  FAILED after recreation attempt")

    if not published_any:
        log("  No carousels due for today (or all already published)")


if __name__ == "__main__":
    publish()
