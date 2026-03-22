# backend/category_detector.py

KEYWORD_MAP = {
    "presentation": ["ppt", "presentation", "slide", "deck", "slides"],
    "image":        ["image", "photo", "picture", "logo", "art", "illustration", "design", "poster", "banner"],
    "audio":        ["audio", "sound", "music", "song", "voice", "speech", "tts"],
    "video":        ["video", "reel", "clip", "animation", "film", "movie"],
    "coding":       ["code", "program", "script", "app", "website", "debug", "function", "python", "java", "html", "coding"],
    "research":     ["research", "study", "analyze", "report", "survey", "thesis", "paper"],
    "writing":      ["essay", "article", "blog", "write", "content"],
}

VALID_CATEGORIES = ["presentation", "image", "audio", "video", "coding", "research", "writing", "ai_tool_usage"]


def detect_category(topic):
    t = topic.lower()
    for cat, kws in KEYWORD_MAP.items():
        if any(k in t for k in kws):
            return cat
    return _ai_classify(topic)


def _ai_classify(topic):
    try:
        from gemini_client import get_client
        client = get_client()
        prompt = (
            f'Classify into ONE category: "{topic}"\n'
            f'Categories: {", ".join(VALID_CATEGORIES)}\n'
            f'Reply ONLY with the category name.'
        )
        res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        cat = res.text.strip().lower().replace(" ", "_")
        return cat if cat in VALID_CATEGORIES else "writing"
    except Exception:
        return "writing"
