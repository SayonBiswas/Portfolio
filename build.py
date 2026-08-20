"""
build.py - The only script you need to run.

How it works:
  1. Imports your content from content.py
  2. Loads the HTML template from templates/index.html.j2
  3. Renders the template with your content using Jinja2
  4. Writes the final index.html into the output/ folder
  5. Generates individual project pages
  6. Copies style.css and assets into the output/ folder

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

# Add custom filter for project URL generation
def project_url(title):
    return title.lower().replace(" ", "_").replace("/", "_").replace(":", "")

env.filters["project_url"] = project_url

# ── Render Main Page ─────────────────────────────────────────────────────
template = env.get_template("index.html.j2")

html = template.render(
    site                = c.SITE,
    nav_links           = c.NAV_LINKS,
    socials             = c.SOCIALS,
    hero                = c.HERO,
    about               = c.ABOUT,
    about_tagline       = c.ABOUT_TAGLINE,
    education           = c.EDUCATION,
    experience          = c.EXPERIENCE,
    projects_completed  = c.PROJECTS_COMPLETED,
    projects_ongoing    = c.PROJECTS_ONGOING,
    skills              = c.SKILLS,
    skills_flat         = c.SKILLS_FLAT,
    achievements        = c.ACHIEVEMENTS,
    certifications      = c.CERTIFICATIONS,
    contact             = c.CONTACT,
    footer              = c.FOOTER,
)

# ── Write main index.html ───────────────────────────────────────────────
(OUTPUT / "index.html").write_text(html, encoding="utf-8")

# ── Generate Project Pages ───────────────────────────────────────────────
project_template = env.get_template("project.html.j2")

all_projects = c.PROJECTS_COMPLETED + c.PROJECTS_ONGOING
for project in all_projects:
    # Create safe filename from project title
    safe_title = project.get("title", "").lower().replace(" ", "_").replace("/", "_").replace(":", "")
    project_html = project_template.render(
        site                = c.SITE,
        project             = project,
        socials             = c.SOCIALS,
        contact             = c.CONTACT,
        footer              = c.FOOTER,
    )
    (OUTPUT / f"project_{safe_title}.html").write_text(project_html, encoding="utf-8")
    print(f"📄  Generated: project_{safe_title}.html")

# ── Copy static files ───────────────────────────────────────────────────
for file in (BASE / "static").iterdir():
    shutil.copy(file, OUTPUT / file.name)

# ── Copy resume file if exists ─────────────────────────────────────────────
if c.CONTACT.get("resume"):
    resume_path = BASE / c.CONTACT["resume"]
    if resume_path.exists():
        shutil.copy(resume_path, OUTPUT / c.CONTACT["resume"])
    else:
        print(f"⚠️  Resume file not found: {resume_path}")

print("✅  Site built successfully!")
print(f"📁  Output → {OUTPUT.resolve()}")
print("🌐  Open output/index.html in your browser to preview.")
print(f"📄  Generated {len(all_projects)} project case study pages.")