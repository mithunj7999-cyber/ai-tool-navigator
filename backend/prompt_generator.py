# backend/prompt_generator.py

import json
from tools_data import AI_TOOLS

OUTPUT_LABELS = {
    "presentation": "PowerPoint presentation", "image": "AI-generated image",
    "audio": "AI-generated audio/music",       "video": "AI-generated video",
    "coding": "code/program",                  "research": "research report",
    "writing": "written content",              "ai_tool_usage": "AI tool usage guide",
}

EXAMPLES = {
    "audio":        'GOOD: "Generate a 60-second upbeat electronic track, 128 BPM, no vocals, futuristic." BAD: "Audio generation is..."',
    "image":        'GOOD: "A hyper-realistic futuristic city at sunset, neon reflections, cyberpunk, 8K." BAD: "Image generation involves..."',
    "presentation": 'GOOD: "Create a 10-slide PPT on AI covering Intro, Types, ML, Advantages, Ethics, Future." BAD: "AI is a broad field..."',
    "coding":       'GOOD: "Write a Python Flask REST API with JWT auth, SQLite, CRUD endpoints, input validation." BAD: "Programming is..."',
    "video":        'GOOD: "Generate a 5-second slow-motion raindrop falling into a lake, cinematic golden hour." BAD: "Video generation uses AI..."',
    "writing":      'GOOD: "Write a 600-word blog on intermittent fasting, friendly tone, 3 tips, CTA at end." BAD: A generic essay.',
    "research":     'GOOD: "Research top 5 quantum computing breakthroughs 2022-2024. For each: what, who, implications." BAD: Generic overview.',
}


def generate_prompts(topic, category, selected_sections):
    from gemini_client import get_client
    client        = get_client()
    tools         = AI_TOOLS.get(category, AI_TOOLS["writing"])
    output_label  = OUTPUT_LABELS.get(category, "content")
    tools_list    = ", ".join(t["name"] for t in tools)
    sections_note = ("covering: " + ", ".join(selected_sections)) if selected_sections else "covering all key aspects"
    example       = EXAMPLES.get(category, EXAMPLES["writing"])

    prompt = f"""You are an AI prompt engineer. One optimized prompt per tool.
USER WANTS: {output_label} about "{topic}" {sections_note}
TOOLS: {tools_list}
EXAMPLE STYLE: {example}
RULES:
1. Tailored to each specific tool's interface
2. Start with action verb: Generate / Create / Write / Design / Build
3. Specific to "{topic}" with exact details
4. 2-4 dense sentences per prompt
5. Never write essay content — write prompts that go INTO the tool

Respond ONLY in this exact JSON:
{{"general_prompt":"...","tool_prompts":{{"Tool Name":"prompt"}},"tips":["tip1","tip2","tip3"]}}"""

    res    = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    raw    = res.text.strip().replace("```json", "").replace("```", "").strip()
    parsed = json.loads(raw)

    general = parsed.get("general_prompt", "")
    tps     = parsed.get("tool_prompts", {})
    tips    = parsed.get("tips", [])

    return {
        "prompt":   general,
        "tips":     "\n".join(f"- {t}" for t in tips),
        "tools":    [{**t, "tool_prompt": tps.get(t["name"], general)} for t in tools],
        "category": category,
    }
