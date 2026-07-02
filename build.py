"""
build.py - The only script you need to run.

How it works:
  1. Imports your content from content.py
  2. Loads the HTML template from templates/index.html.j2
  3. Renders the template with your content using Jinja2
  4. Writes the final index.html into the output/ folder
  5. Copies style.css into the output/ folder

To run:
  python build.py

Then open output/index.html in your browser, or push the
output/ folder to GitHub Pages.
"""

import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from icons import icon
import content as c

# ── Paths ──────────────────────────────────────────────────────────────
BASE   = Path(__file__).parent
OUTPUT = BASE / "output"
OUTPUT.mkdir(exist_ok=True)

# ── Jinja2 Environment ─────────────────────────────────────────────────
env = Environment(
    loader=FileSystemLoader(BASE / "templates"),
    autoescape=False,         # we use | safe on icon() calls explicitly
)

# Make the icon() helper available inside every template
env.globals["icon"] = icon

# ── Render ─────────────────────────────────────────────────────────────
template = env.get_template("index.html.j2")

html = template.render(
    site        = c.SITE,
    nav_links   = c.NAV_LINKS,
    socials     = c.SOCIALS,
    hero        = c.HERO,
    about       = c.ABOUT,
    education   = c.EDUCATION,
    experience  = c.EXPERIENCE,
    projects    = c.PROJECTS,
    skills      = c.SKILLS,
    achievements= c.ACHIEVEMENTS,
    contact     = c.CONTACT,
    footer      = c.FOOTER,
)

# ── Write output ───────────────────────────────────────────────────────
(OUTPUT / "index.html").write_text(html, encoding="utf-8")
shutil.copy(BASE / "static" / "style.css", OUTPUT / "style.css")
shutil.copy(BASE / "static" / "profile_photo.jpeg", OUTPUT / "profile_photo.jpeg")
shutil.copy(BASE / "static" / "examhub.png", OUTPUT / "examhub.png")

print("✅  Site built successfully!")
print(f"📁  Output → {OUTPUT.resolve()}")
print("🌐  Open output/index.html in your browser to preview.")