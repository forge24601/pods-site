#!/usr/bin/env python3
"""Build the POD Society site: src/<page>.html (body only, with a metadata comment on the first line)
-> <page>.html at the repo root, wrapped in the shared header, navigation and footer.

    python3 tools/build.py

First line of each source page:  <!-- {"title": "About", "description": "…", "nav": "about"} -->
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

NAV = [  # (key, label, href)
    ("home", "Home", "index.html"),
    ("about", "About", "about.html"),
    ("programs", "Programs", "programs.html"),
    ("reentry-home", "Reentry Home", "reentry-home.html"),
    ("impact", "Impact", "impact.html"),
    ("events", "Events", "events.html"),
    ("resources", "Resources", "resources.html"),
    ("contact", "Contact", "contact.html"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="images/pods-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,700..900&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to the main content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="images/pods-logo.png" alt=""><span>POD Society<small>Positive Outreach Development Society</small></span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul class="menu" id="menu">
{menu}
      <li><a class="btn" href="get-involved.html#donate">Donate</a></li>
    </ul>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="images/pods-logo.png" alt="POD Society">
        <p>Positive Outreach Development Society, Inc. is a 501(c)(3) nonprofit working to end recidivism through
        mentorship, cognitive programming, reentry support and community partnership.</p>
      </div>
      <div>
        <h2>Programs</h2>
        <ul>
          <li><a href="forge.html">FORGE</a></li>
          <li><a href="reentry-home.html">Reentry Home</a></li>
          <li><a href="successful-reentry.html">FORGE Successful Reentry</a></li>
          <li><a href="forge-your-success.html">FORGE Your Success class</a></li>
          <li><a href="job-skills.html">Job skills classes</a></li>
          <li><a href="programs.html">All programs</a></li>
        </ul>
      </div>
      <div>
        <h2>Get involved</h2>
        <ul>
          <li><a href="get-involved.html#donate">Donate</a></li>
          <li><a href="get-involved.html#volunteer">Volunteer</a></li>
          <li><a href="get-involved.html#partner">Partner with us</a></li>
          <li><a href="events.html">Events</a></li>
          <li><a href="reading-list.html">Books for the road</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:+14705025982">(470) 502-5982</a></li>
          <li><a href="mailto:positiveoutreachdevelopment23@gmail.com">positiveoutreachdevelopment23@gmail.com</a></li>
          <li><a href="https://www.instagram.com/podmovement23/">Instagram: @podmovement23</a></li>
        </ul>
      </div>
    </div>
    <p class="foot-legal">&copy; 2026 Positive Outreach Development Society, Inc. &nbsp;|&nbsp; 501(c)(3) nonprofit &nbsp;|&nbsp; EIN 99-2858905</p>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def build():
    pages = sorted(SRC.glob("*.html"))
    for src in pages:
        text = src.read_text()
        m = re.match(r"<!--\s*(\{.*?\})\s*-->\s*\n", text, re.S)
        assert m, f"{src.name}: first line must be a metadata comment"
        meta = json.loads(m.group(1))
        body = text[m.end():]
        menu = "\n".join(
            f'      <li><a href="{href}"{" aria-current=\"page\"" if key == meta.get("nav") else ""}>{label}</a></li>'
            for key, label, href in NAV)
        title = meta["title"] if meta.get("nav") == "home" else f'{meta["title"]} | POD Society'
        html = HEAD.format(title=title, description=meta["description"], menu=menu) + body + FOOT
        (ROOT / src.name).write_text(html)
        print(src.name)


if __name__ == "__main__":
    build()
