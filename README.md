# ✦ AI Tool Navigator

<div align="center">

**Your intelligent guide to AI tools & perfect prompts**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini_AI-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
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

- 🎯 **Auto-Detection** — Automatically detects your task category
- ✦ **Optimized Prompts** — Generates one tailored prompt per AI tool using Gemini 2.5 Flash
- 🛠️ **20+ AI Tools** — Curated database of the best tools for every category
- 📋 **Step-by-Step Guidance** — Exact steps to use each tool
- 💡 **Smart Sections** — Dynamically suggests relevant sections for your topic
- 📋 **One-Click Copy** — Copy any prompt instantly
- 🔒 **Secure** — API key protected via environment variables

---

## 🖥️ Pages

### Page 1 — Home
Enter your topic, select sections you want covered, click Generate.

### Page 2 — Results
View your optimized prompt, recommended AI tools, step-by-step guides and pro tips.

---

## 🗂️ Project Structure

```
project/
├── .env                          ← API key (never committed to git)
├── .gitignore
├── README.md
│
├── backend/                      ← All Python files
│   ├── app.py                    ← Entry point
│   ├── routes.py                 ← Flask URL routes
│   ├── gemini_client.py          ← Gemini API connection
│   ├── category_detector.py      ← Auto-detects topic category
│   ├── section_suggestions.py    ← Dynamic section checkboxes
│   ├── prompt_generator.py       ← Builds & sends prompts to Gemini
│   ├── tools_data.py             ← AI tools database
│   ├── Procfile                  ← Render deployment config
│   └── requirements.txt
│
└── frontend/                     ← All HTML, CSS, JS files
    ├── pages/
    │   ├── index.html            ← Home page
    │   └── results.html          ← Results page
    ├── css/
    │   ├── base.css              ← Shared design system
    │   ├── index.css             ← Home page styles
    │   └── results.css           ← Results page styles
    └── js/
        ├── index.js              ← Home page logic
        └── results.js            ← Results page logic
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
FLASK_DEBUG=true
```

> Get your free API key at → **https://aistudio.google.com/apikey**

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
Gemini 2.5 Flash generates one optimized prompt per tool
       ↓
Results page shows prompts + tools + steps + tips
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
--vivid:  #1a7fe0;   /* main blue  */
--bright: #3d9eff;   /* accent     */
--ink:    #04111f;   /* background */
```

### Change AI model
Edit `backend/prompt_generator.py`:
```python
model="gemini-2.5-flash"
```

---

## 🚢 Deployment on Render

1. Fork this repository
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your forked repo
4. Set these values:

| Setting | Value |
|---------|-------|
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

5. Add environment variable → `GEMINI_API_KEY` = your key
6. Click **Deploy** ✅

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3, Flask |
| **AI** | Google Gemini 2.5 Flash |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Fonts** | Outfit, JetBrains Mono |
| **Deployment** | Render, Gunicorn |

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

---

<div align="center">

Made with ❤️ and ✦ AI

⭐ **Star this repo if you found it helpful!**

</div>
