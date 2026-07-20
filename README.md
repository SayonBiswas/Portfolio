# 🧑‍💻 sayon.dev — Personal Portfolio

> A backend-developer-themed personal portfolio site built with **Python + Jinja2**.  
> Dark by default, light mode toggle, zero JavaScript — pure CSS checkbox hack.

---

## ✨ Features

- 🌑 **Dark / Light mode** — theme toggle works on all devices (desktop navbar + mobile hamburger menu), powered entirely by CSS (no JS)
- ⚡ **Static site generator** — one `python build.py` command renders everything to a single `output/` folder
- 🧩 **Content-driven** — all text, links, and data live in `content.py`; no HTML editing needed
- 🖼️ **Lightbox image viewer** — achievements and certifications support image previews via CSS checkbox lightbox
- 📱 **Fully responsive** — mobile-first layout, hamburger nav on small screens
- 🎨 **Terminal aesthetic** — JetBrains Mono, green accent, grid background, glowing cards

---

## 🗂️ Project Structure

```
Portfolio/
├── build.py           # Build script — renders template + copies static assets
├── content.py         # All your personal data (name, projects, skills, etc.)
├── icons.py           # SVG icon helper used inside Jinja2 templates
├── requirements.txt   # Python dependencies (Jinja2)
├── render.yaml        # Render.com deployment config
├── templates/
│   └── index.html.j2  # Jinja2 HTML template
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

### 4. Build the site

```bash
python build.py
```

This generates an `output/` folder containing `index.html` and `style.css`.

### 5. Preview locally

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
|---|---|
| Build | Python 3 |
| Templating | Jinja2 |
| Styling | Vanilla CSS (custom properties, grid, flexbox) |
| Icons | Inline SVG via `icons.py` |
| Fonts | Inter + JetBrains Mono (Google Fonts) |
| Deployment | GitHub Pages / Render.com |

---

## 🎨 Customisation

| What | Where |
|---|---|
| Personal info, projects, skills | `content.py` |
| Layout & sections | `templates/index.html.j2` |
| Colors, fonts, spacing | `static/style.css` (CSS custom properties at the top) |
| Icons | `icons.py` |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built by <a href="https://github.com/SayonBiswas">Sayon Biswas</a></p>