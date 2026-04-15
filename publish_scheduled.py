"""
Auto-publish scheduled carousels — runs daily at 9:55 AM via LaunchAgent.
Checks if today matches a carousel's scheduled date and publishes it at 10 AM.
"""
import os, sys, json, time, requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, "summit-wraps", "lead-engine"))
import ig_api

API = "https://graph.instagram.com/v21.0"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "carousel_state.json")
LOG_FILE = os.path.join(BASE_DIR, "_data", "logs", "carousel_publish.log")

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

def publish():
    today = datetime.now().strftime("%Y-%m-%d")
    state = load_state()

    log(f"Checking schedule for {today}...")

    published_any = False
    for key, info in sorted(state.items(), key=lambda x: x[0]):
        if info.get("scheduled_date") == today and not info.get("published"):
            container_id = info.get("container_id")
            if not container_id:
                log(f"  Carousel #{key} has no container ID, skipping")
                continue

            token = ig_api._account("brycenwood.ai")["access_token"]
            uid = ig_api._user_id("brycenwood.ai")

            log(f"  Publishing Carousel #{key}: {info.get('name', '?')}...")

            r = requests.post(f"{API}/{uid}/media_publish", data={
                "creation_id": container_id,
                "access_token": token,
            }, timeout=30)

            if r.status_code == 200:
                media_id = r.json()["id"]
                info["published"] = True
                info["media_id"] = media_id
                info["published_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_state(state)
                log(f"  SUCCESS! Media ID: {media_id}")
                published_any = True
            else:
                log(f"  FAILED: {r.status_code} {r.text[:300]}")

    if not published_any:
        log("  No carousels scheduled for today (or all already published)")

if __name__ == "__main__":
    publish()
