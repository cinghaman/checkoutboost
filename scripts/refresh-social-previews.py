#!/usr/bin/env python3
"""Check each page's social preview and ask Facebook to re-scrape it.

Usage:
  python3 scripts/refresh-social-previews.py                  # every URL in sitemap.xml
  python3 scripts/refresh-social-previews.py --since 2026-10-14
  python3 scripts/refresh-social-previews.py URL [URL ...]

What it does per URL:
  1. Fetches the live page and checks og:image and twitter:image resolve to an image.
  2. Facebook (also used by Instagram, Messenger, WhatsApp link previews): if FB_APP_TOKEN is
     set ("APP_ID|APP_SECRET" from a Meta developer app), POSTs a re-scrape so the new image is
     picked up now. Without the token it prints the Sharing Debugger link instead.
  3. LinkedIn has no public re-scrape API. It prints the Post Inspector link; opening it once
     refreshes LinkedIn's cache for that URL.
  4. X has no refresh endpoint. X re-reads cards after about a week, or immediately when the
     image URL changes, which is why preview images get a new filename when they change.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from indexnow import sitemap_urls  # noqa: E402

UA = "Mozilla/5.0 (compatible; SmartCheckoutWidgetsPreviewCheck/1.0)"


def get(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=20)


def meta(html, attr, name):
    m = re.search(rf'<meta {attr}="{re.escape(name)}" content="([^"]+)"', html)
    return m.group(1) if m else None


def check(url):
    html = get(url).read().decode("utf-8", "replace")
    problems = []
    for attr, name in (("property", "og:image"), ("name", "twitter:image")):
        img = meta(html, attr, name)
        if not img:
            problems.append(f"missing {name}")
            continue
        try:
            r = get(img, "HEAD")
            ctype = r.headers.get("Content-Type", "")
            if not ctype.startswith("image/"):
                problems.append(f"{name} is {ctype}, not an image")
        except Exception as e:
            problems.append(f"{name} {img} failed: {e}")
    return meta(html, "property", "og:image"), problems


def facebook_rescrape(url, token):
    data = urllib.parse.urlencode({"id": url, "scrape": "true", "access_token": token}).encode()
    req = urllib.request.Request("https://graph.facebook.com/", data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.loads(r.read())
    imgs = body.get("image") or []
    return imgs[0].get("url") if imgs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--since")
    args = ap.parse_args()
    urls = args.urls or list(sitemap_urls(args.since))
    token = os.environ.get("FB_APP_TOKEN")
    inspector = []
    for url in urls:
        try:
            og, problems = check(url)
        except Exception as e:
            print(f"FAIL {url}: {e}")
            continue
        print(("OK  " if not problems else "WARN") + f" {url}\n     image: {og}")
        for p in problems:
            print(f"     ! {p}")
        if token:
            try:
                print(f"     facebook: re-scraped, image now {facebook_rescrape(url, token)}")
            except Exception as e:
                print(f"     facebook: re-scrape failed: {e}")
        else:
            print("     facebook: https://developers.facebook.com/tools/debug/?q=" + urllib.parse.quote(url, safe=""))
        inspector.append("https://www.linkedin.com/post-inspector/inspect/" + urllib.parse.quote(url, safe=""))
    print("\nOpen each link once to refresh LinkedIn's cache:")
    print(*inspector, sep="\n")


if __name__ == "__main__":
    main()
