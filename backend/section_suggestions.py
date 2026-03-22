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


def get_smart_questions(topic, category):
    """
    Generate smart follow-up questions with options so user can
    provide specific details that make the final prompt much better.
    """
    try:
        from gemini_client import get_client
        client = get_client()
        prompt = f"""A user typed: "{topic}" (category: {category})

Your job: Generate 3-4 smart follow-up questions to gather specific details
that will make the AI prompt MUCH more targeted and useful.

Examples of good questions for different topics:
- "logo design" → ask: logo style (minimalist/vintage/modern/playful), color preference, industry/business type, what to include (icon/text/both)
- "PPT on AI" → ask: audience (students/professionals/kids), slide count, tone (academic/casual/business), specific AI subtopic focus
- "write a blog" → ask: target audience, word count, tone (formal/casual/funny), specific angle or opinion
- "music for video" → ask: video mood, duration, genre preference, tempo (slow/medium/fast)
- "Python script" → ask: experience level, specific feature needed, should it have a UI or CLI
- "YouTube video" → ask: channel niche, video length, style (educational/entertaining/vlog)

Rules:
1. Questions must be DIRECTLY relevant to "{topic}"
2. Each question must have 3-5 short clickable options (not open-ended)
3. Options must be specific and useful — not generic like "yes/no"
4. Include one question about color/style/aesthetic when relevant
5. Max 4 questions — quality over quantity

Return ONLY this JSON array, nothing else:
[
  {{
    "id": "unique_id",
    "question": "Short specific question about {topic}?",
    "icon": "relevant emoji",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"]
  }}
]"""

        res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        raw = res.text.strip().replace("```json", "").replace("```", "").strip()
        questions = json.loads(raw)
        return questions
    except Exception:
        return []
