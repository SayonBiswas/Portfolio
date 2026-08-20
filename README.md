# 🧑‍💻 sayon.dev — Personal Portfolio

> A modern editorial portfolio site built with **Python + Jinja2**.  
> Dark by default, light mode toggle, zero JavaScript — pure CSS checkbox hack.  
> Featuring a distinctive bento design system with case study pages.

---

## ✨ Features

- 🌑 **Dark / Light mode** — theme toggle works on all devices (desktop navbar + mobile hamburger menu), powered entirely by CSS (no JS)
- ⚡ **Static site generator** — one `python build.py` command renders everything to a single `output/` folder
- 🧩 **Content-driven** — all text, links, and data live in `content.py`; no HTML editing needed
- 📄 **Project case study pages** — individual detailed pages for each project with GitHub links, live demos, and features
- 📥 **Resume download** — PDF resume download buttons in hero section and footer
- 🎨 **Editorial bento design** — distinctive two-column layout pattern, cyan/orange/lime accents, Syne + Playfair Display typography
- 📱 **Fully responsive** — mobile-first layout, hamburger nav on small screens
- 🖼️ **Inline SVG icons** — custom icon system via `icons.py` for sharp, scalable graphics

---

## 🗂️ Project Structure

```
Portfolio/
├── build.py           # Build script — renders templates + copies static assets
├── content.py         # All your personal data (name, projects, skills, etc.)
├── icons.py           # SVG icon helper used inside Jinja2 templates
├── requirements.txt   # Python dependencies (Jinja2)
├── render.yaml        # Render.com deployment config
├── templates/
│   ├── index.html.j2  # Main portfolio Jinja2 template
│   └── project.html.j2 # Project case study template
└── static/
    └── style.css      # All styles (dark/light tokens, layout, components)
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/SayonBiswas/Portfolio.git
cd Portfolio
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Edit your content

Open `content.py` and fill in your own details — name, bio, projects, skills, socials, contact, etc.

### 4. Add your resume

Place your PDF resume file in the project root directory (e.g., `Your_Name_Resume.pdf`) and update the `resume` field in `content.py` under the `CONTACT` dictionary.

### 5. Build the site

```bash
python build.py
```

This generates an `output/` folder containing:
- `index.html` — Main portfolio page
- `project_*.html` — Individual project case study pages
- `style.css` — Stylesheet
- Your resume file (if present)

### 6. Preview locally

Open `output/index.html` in your browser — that's your portfolio!

---

## 🌐 Deployment

### GitHub Pages

1. Build the site: `python build.py`
2. Copy the contents of `output/` to your `gh-pages` branch or configure Pages to serve from `output/`

### Render.com

The repo includes a `render.yaml` config. Just connect the repo to [Render](https://render.com) and it will auto-deploy.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Build | Python 3 |
| Templating | Jinja2 |
| Styling | Vanilla CSS (custom properties, grid, flexbox) |
| Icons | Inline SVG via `icons.py` |
| Fonts | Syne, Playfair Display, Inter, JetBrains Mono (Google Fonts) |
| Deployment | GitHub Pages / Render.com |

---

## 🎨 Design System

### Colors
- **Dark mode**: #0a0a0a background, #ff6b35 orange, #00dbe9 cyan, #84cc16 lime
- **Light mode**: #eeeae3 warm cream background, same accent colors
- **Footer**: Always #ff6b35 orange regardless of theme

### Typography
- **Syne**: Headings, display text (bold, modern)
- **Playfair Display**: Italic text, editorial feel
- **Inter**: Body text, clean and readable
- **JetBrains Mono**: Labels, code, technical elements

### Layout Pattern
- Two-column sections: 1/3 eyebrow label (mono caps) + 2/3 content
- Bento-style project cards with image overlays
- Horizontal timeline for education and experience
- Consistent 128px section padding, 64px gaps

---

## 🎨 Customisation

| What | Where |
|------|-------|
| Personal info, projects, skills | `content.py` |
| Layout & sections | `templates/index.html.j2` and `templates/project.html.j2` |
| Colors, fonts, spacing | `static/style.css` (CSS custom properties at the top) |
| Icons | `icons.py` |
| Resume file | Project root directory (PDF) |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built by <a href="https://github.com/SayonBiswas">Sayon Biswas</a></p>
