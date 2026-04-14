#!/bin/bash
# Deploy brycenwood.com and ping IndexNow for instant Bing indexing
# Usage: bash scripts/deploy_and_index.sh

set -e

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$SITE_DIR/build"
INDEXNOW_KEY="446a01e69ec538802a117ca3f13bf9e5"
DOMAIN="https://www.brycenwood.com"

echo "=== Regenerating markdown mirrors ==="
python3 "$SITE_DIR/scripts/generate_markdown_mirrors.py"

echo ""
echo "=== Committing and pushing ==="
cd "$SITE_DIR"
git add build/
git status --short

echo ""
read -p "Commit message: " MSG
git commit -m "$MSG

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
git push origin main

echo ""
echo "=== Waiting for Cloudflare Pages deploy (30s) ==="
sleep 30

echo ""
echo "=== Pinging IndexNow ==="
# Collect all URLs from sitemap
URLS=$(python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('$BUILD_DIR/sitemap.xml')
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
for url in tree.findall('.//sm:url/sm:loc', ns):
    print(url.text)
")

# Build JSON payload
URL_ARRAY=$(echo "$URLS" | python3 -c "
import sys, json
urls = [line.strip() for line in sys.stdin if line.strip()]
print(json.dumps(urls))
")

curl -s -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d "{
    \"host\": \"www.brycenwood.com\",
    \"key\": \"$INDEXNOW_KEY\",
    \"keyLocation\": \"$DOMAIN/$INDEXNOW_KEY.txt\",
    \"urlList\": $URL_ARRAY
  }" && echo " -- IndexNow pinged successfully" || echo " -- IndexNow ping failed (non-critical)"

echo ""
echo "=== Deploy complete ==="
echo "Site: $DOMAIN"
echo "Pages: $(echo "$URLS" | wc -l | tr -d ' ') URLs submitted to IndexNow"
