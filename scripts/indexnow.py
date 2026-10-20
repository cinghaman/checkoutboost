#!/usr/bin/env python3
"""Submit site URLs to IndexNow (Bing, Yandex, Seznam, Naver and others share submissions).

Usage:
  python3 scripts/indexnow.py                 # every URL in sitemap.xml
  python3 scripts/indexnow.py --since 2026-10-14   # only URLs with lastmod on or after a date
  python3 scripts/indexnow.py https://smartcheckoutwidgets.com/blog/some-post/   # specific URLs
  python3 scripts/indexnow.py --dry-run       # print what would be sent

The key file must be live at https://smartcheckoutwidgets.com/<KEY>.txt before submitting,
so run this after the deploy has finished. The script also checks the key file for two
minutes before sending: a search engine that fetches the key from an edge node that is
still serving the old deploy gets a 404, and Bing then rejects every submission with 403
(UserForbiddedToAccessSite) without fetching the key again. If that happens, rotate the key.
When you rotate the key, deploy the new key file on its own and wait at least 15 minutes
before the first submission. Sevalla's US edge served a 404 for a new key file more than
three minutes after it was live from Europe, and Bingbot fetches from the US.
"""
import argparse
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "smartcheckoutwidgets.com"
KEY = "e9a1612005576f209c2d864cf972d2bc"
ENDPOINT = "https://api.indexnow.org/indexnow"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
# Cloudflare's bot protection returns 403 to the default Python-urllib user agent.
UA = "Mozilla/5.0 (compatible; SmartCheckoutWidgetsIndexNow/1.0; +https://smartcheckoutwidgets.com/)"


def sitemap_urls(since=None):
    tree = ET.parse(ROOT / "sitemap.xml")
    for node in tree.getroot().findall("sm:url", NS):
        loc = node.findtext("sm:loc", namespaces=NS)
        lastmod = node.findtext("sm:lastmod", default="", namespaces=NS)
        if since and lastmod < since:
            continue
        yield loc


def key_is_live():
    try:
        req = urllib.request.Request(f"https://{HOST}/{KEY}.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode().strip() == KEY
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--since", help="YYYY-MM-DD; only sitemap URLs with lastmod on or after this date")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    urls = args.urls or list(sitemap_urls(args.since))
    urls = [u for u in dict.fromkeys(urls) if u.startswith(f"https://{HOST}/")]
    if not urls:
        sys.exit("No URLs to submit.")
    print(f"{len(urls)} URL(s):", *urls, sep="\n  ")
    if args.dry_run:
        return
    for check in range(5):
        if not key_is_live():
            sys.exit(f"Key file https://{HOST}/{KEY}.txt is not live yet. Deploy first, then rerun.")
        if check < 4:
            time.sleep(30)

    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt",
                       "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow:", r.status, "(200 or 202 means accepted)")
    except urllib.error.HTTPError as e:
        sys.exit(f"IndexNow rejected the request: {e.code} {e.read().decode()[:300]}")


if __name__ == "__main__":
    main()
