# backend/section_suggestions.py

import json

DEFAULT_SECTIONS = {
    "presentation": [
        {"id": "intro",         "label": "Introduction",  "icon": "📌"},
        {"id": "features",      "label": "Features",      "icon": "⚙️"},
        {"id": "advantages",    "label": "Advantages",    "icon": "✅"},
        {"id": "disadvantages", "label": "Disadvantages", "icon": "❌"},
        {"id": "use_cases",     "label": "Use Cases",     "icon": "💡"},
        {"id": "future",        "label": "Future Scope",  "icon": "🚀"},
        {"id": "conclusion",    "label": "Conclusion",    "icon": "🎯"},
    ],
    "image":    [{"id":"style","label":"Art Style","icon":"🎨"},{"id":"mood","label":"Mood","icon":"🌅"},{"id":"colors","label":"Color Palette","icon":"🎭"},{"id":"details","label":"Fine Details","icon":"🔍"}],
    "coding":   [{"id":"func","label":"Core Functionality","icon":"⚙️"},{"id":"stack","label":"Tech Stack","icon":"🛠️"},{"id":"errors","label":"Error Handling","icon":"🐛"},{"id":"docs","label":"Documentation","icon":"📝"}],
    "writing":  [{"id":"intro","label":"Introduction","icon":"📌"},{"id":"main","label":"Main Content","icon":"📄"},{"id":"examples","label":"Examples","icon":"💡"},{"id":"concl","label":"Conclusion","icon":"🎯"}],
    "audio":    [{"id":"genre","label":"Genre / Style","icon":"🎵"},{"id":"mood","label":"Mood & Emotion","icon":"🎭"},{"id":"tempo","label":"Tempo & Rhythm","icon":"🥁"},{"id":"instruments","label":"Instruments","icon":"🎸"},{"id":"vocals","label":"Vocals / Voice","icon":"🎤"}],
    "video":    [{"id":"concept","label":"Concept","icon":"💡"},{"id":"script","label":"Script","icon":"📝"},{"id":"style","label":"Visual Style","icon":"🎬"},{"id":"audio","label":"Audio/Music","icon":"🎵"}],
    "research": [{"id":"background","label":"Background","icon":"📚"},{"id":"objective","label":"Objectives","icon":"🎯"},{"id":"method","label":"Methodology","icon":"🔬"},{"id":"findings","label":"Key Findings","icon":"💡"},{"id":"conclusion","label":"Conclusion","icon":"✅"}],
}


def get_default_sections(category):
    return DEFAULT_SECTIONS.get(category, DEFAULT_SECTIONS["writing"])


def get_dynamic_sections(topic, category):
    try:
        from gemini_client import get_client
        client = get_client()
        prompt = (
            f'User wants a {category} about: "{topic}"\n'
            f'Suggest 5-7 relevant sections SPECIFIC to "{topic}".\n'
            f'Return ONLY a JSON array, no other text:\n'
            f'[{{"id":"id","label":"Label","icon":"emoji"}}]\n'
            f'Keep labels 2-4 words. Use relevant emojis.'
        )
        res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        raw = res.text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except Exception:
        return get_default_sections(category)
