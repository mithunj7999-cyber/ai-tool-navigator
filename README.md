# ✦ AI Tool Navigator

<div align="center">

**Your intelligent guide to AI tools & perfect prompts**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini_AI-2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

🌐 **Live Demo → [ai-tool-navigator.onrender.com](https://ai-tool-navigator.onrender.com)**

</div>

---

## 📖 Overview

**AI Tool Navigator** is a full-stack web application that helps anyone — students, creators, developers — find the best AI tools and generate optimized prompts for their specific task in seconds.

No more guessing which AI tool to use or how to write a good prompt. Just describe what you want to create and get instant, tailored guidance.

---

## ✨ Features

### Core Features
- 🎯 **Auto-Detection** — Automatically detects your task category (presentation, image, code, audio, video, research, writing)
- ✦ **Optimized Prompts** — Generates one tailored prompt per AI tool using Gemini 2.0 Flash
- 🛠️ **20+ AI Tools** — Curated database of the best tools for every category
- 📋 **Step-by-Step Guidance** — Exact steps to use each tool
- 💡 **Smart Sections** — Dynamically suggests relevant sections for your topic
- 📋 **One-Click Copy** — Copy any prompt instantly

### Auth & User Features (v2.0)
- 🔐 **Email & Password Signup** — Email is optional, only name + password required
- 👤 **Login with Username or Email** — Flexible login options
- 📊 **Personal Dashboard** — View your name, email, and usage stats
- 📋 **Prompt History** — Every generated prompt saved automatically when logged in
- 🗑️ **Delete History** — Remove any saved prompt from your dashboard
- 🔒 **Secure** — Passwords hashed with bcrypt, API key protected via environment variables

---

## 🖥️ Pages

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Enter topic, select sections, click Generate |
| **Results** | `/results` | View prompts, tools, steps and tips |
| **Login** | `/login` | Sign in with username or email |
| **Sign Up** | `/signup` | Create account (email optional) |
| **Dashboard** | `/dashboard` | View profile, stats and prompt history |

---

## 🗂️ Project Structure

```
project/
├── .env                          ← API key & secrets (never commit)
├── .gitignore
├── README.md
│
├── backend/                      ← All Python server files
│   ├── app.py                    ← Entry point — run this
│   ├── routes.py                 ← Flask URL routes
│   ├── auth.py                   ← Login, signup, logout, history APIs
│   ├── models.py                 ← User & PromptHistory database models
│   ├── database.py               ← SQLite database setup
│   ├── gemini_client.py          ← Gemini API connection
│   ├── category_detector.py      ← Auto-detects topic category
│   ├── section_suggestions.py    ← Dynamic section checkboxes
│   ├── prompt_generator.py       ← Builds & sends prompts to Gemini
│   ├── tools_data.py             ← AI tools database
│   ├── Procfile                  ← Render deployment config
│   └── requirements.txt
│
└── frontend/                     ← All HTML, CSS, JavaScript files
    ├── pages/
    │   ├── index.html            ← Home page
    │   ├── results.html          ← Results page
    │   ├── login.html            ← Login page
    │   ├── signup.html           ← Sign up page
    │   └── dashboard.html        ← User dashboard
    ├── css/
    │   ├── base.css              ← Shared light blue design system
    │   ├── index.css             ← Home page styles
    │   ├── results.css           ← Results page styles
    │   ├── auth.css              ← Login & signup styles
    │   └── dashboard.css         ← Dashboard styles
    └── js/
        ├── nav.js                ← Shared navbar auth state
        ├── index.js              ← Home page logic
        ├── results.js            ← Results page logic
        └── dashboard.js          ← Dashboard history logic
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-tool-navigator.git
cd ai-tool-navigator
```

### 2. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Create `.env` file
Create a `.env` file in the `project/` root folder:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=any-long-random-string-here
FLASK_DEBUG=true
```

> Get your free Gemini API key at → **https://aistudio.google.com/apikey**

### 4. Run the app
```bash
cd backend
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## 🛠️ Supported Categories & Tools

| Category | AI Tools |
|----------|----------|
| 📊 **Presentation** | Gamma AI, Canva AI, Beautiful.ai |
| 🎨 **Image** | Midjourney, Adobe Firefly, DALL-E |
| ✍️ **Writing** | ChatGPT, Gemini |
| 💻 **Coding** | GitHub Copilot, ChatGPT |
| 🎵 **Audio** | Suno AI, Udio, ElevenLabs, Mubert |
| 🎬 **Video** | Runway ML, Pictory |
| 🔬 **Research** | Perplexity AI, ChatGPT |
| 🤖 **General AI** | ChatGPT, Gemini |

---

## ⚙️ How It Works

```
User enters topic
       ↓
Category auto-detected (keyword match + Gemini fallback)
       ↓
Dynamic sections suggested for the topic
       ↓
User selects sections → clicks Generate
       ↓
Gemini 2.0 Flash generates one optimized prompt per tool
       ↓
Results page shows prompts + tools + steps + tips
       ↓
If logged in → prompt automatically saved to history
       ↓
View all past prompts in Dashboard
```

---

## 🔐 Authentication Flow

```
Sign Up → name + password (email optional)
        ↓
Login → username OR email + password
        ↓
Session created → navbar shows name + Dashboard + Logout
        ↓
Generate prompts → auto-saved to your history
        ↓
Dashboard → view stats, history, copy or delete prompts
```

---

## 🔧 Customization

### Add a new AI tool
Edit `backend/tools_data.py`:
```python
{
    "name": "New Tool",
    "link": "https://newtool.com",
    "availability": "Free",
    "best_for": "What it does best",
    "steps": ["Step 1", "Step 2", "Step 3"]
}
```

### Change color scheme
Edit `frontend/css/base.css`:
```css
--accent:       #2563eb;   /* primary blue */
--blue-500:     #3b82f6;   /* lighter blue */
--bg:           #f0f6ff;   /* background   */
```

### Change AI model
Edit `backend/prompt_generator.py`:
```python
model="gemini-2.0-flash"   # or gemini-2.5-flash for better quality
```

### Add a new category
Edit `backend/category_detector.py`:
```python
KEYWORD_MAP = {
    "your_category": ["keyword1", "keyword2"],
}
```

---

## 🚢 Deployment on Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Configure settings:

| Setting | Value |
|---------|-------|
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

5. Add environment variables:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | your Gemini API key |
| `SECRET_KEY` | any long random string |

6. Click **Deploy** ✅

> Note: SQLite database (`users.db`) is created automatically on first run. On Render free tier, the database resets on each deploy. For persistent storage consider upgrading to PostgreSQL.

---

## 📦 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3, Flask | Web framework |
| **AI** | Google Gemini 2.0 Flash | Prompt generation |
| **Database** | SQLite + SQLAlchemy | User & history storage |
| **Auth** | Flask-Login + Flask-Bcrypt | Session management + password hashing |
| **Frontend** | HTML5, CSS3, Vanilla JS | UI with light blue design |
| **Fonts** | Plus Jakarta Sans, JetBrains Mono | Typography |
| **Deployment** | Render + Gunicorn | Cloud hosting |

---

## 🗺️ Roadmap

- [ ] Google OAuth login
- [ ] Prompt rating system
- [ ] Share prompt via link
- [ ] Multi-language support
- [ ] PostgreSQL for persistent storage
- [ ] Dark / Light mode toggle
- [ ] Prompt variations (Basic / Advanced)

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch → `git checkout -b feature/your-feature`
3. Commit → `git commit -m "add your feature"`
4. Push → `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify and distribute.

---

## 🙏 Acknowledgements

- [Google Gemini API](https://aistudio.google.com) — AI prompt generation
- [Flask](https://flask.palletsprojects.com) — Python web framework
- [Render](https://render.com) — Free hosting platform
- [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) — UI font

---

<div align="center">

Made with ❤️ and ✦ AI

⭐ **Star this repo if you found it helpful!**

</div>