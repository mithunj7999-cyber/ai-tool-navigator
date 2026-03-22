# backend/prompt_generator.py
import json

OUTPUT_LABELS = {
    "presentation": "PowerPoint presentation",
    "image":        "AI-generated image",
    "audio":        "AI-generated audio/music",
    "video":        "AI-generated video",
    "coding":       "code/program",
    "research":     "research report",
    "writing":      "written content",
    "ai_tool_usage":"AI tool usage guide",
}

EXAMPLES = {
    "audio":        'GOOD: "Generate a 60-second upbeat electronic track, 128 BPM, no vocals." BAD: "Audio generation is..."',
    "image":        'GOOD: "A futuristic city at sunset, neon reflections, cyberpunk, 8K." BAD: "Image generation involves..."',
    "presentation": 'GOOD: "Create a 10-slide PPT on AI covering Intro, Types, ML, Advantages, Ethics, Future." BAD: "AI is a broad field..."',
    "coding":       'GOOD: "Write a Python Flask REST API with JWT auth, SQLite, CRUD endpoints." BAD: "Programming is..."',
    "video":        'GOOD: "Generate a 5-second slow-motion raindrop falling into a lake, cinematic golden hour." BAD: "Video generation uses AI..."',
    "writing":      'GOOD: "Write a 600-word blog on intermittent fasting, friendly tone, 3 tips, CTA." BAD: Generic essay.',
    "research":     'GOOD: "Research top 5 quantum computing breakthroughs 2022-2024. For each: what, who, implications." BAD: Generic overview.',
}


def generate_prompts(topic, category, selected_sections):
    from gemini_client import get_client
    from tools_data import AI_TOOLS

    client        = get_client()
    tools         = AI_TOOLS.get(category, AI_TOOLS["writing"])
    output_label  = OUTPUT_LABELS.get(category, "content")
    tools_list    = ", ".join(t["name"] for t in tools)
    sections_note = ("covering: " + ", ".join(selected_sections)) if selected_sections else "covering all key aspects"
    example       = EXAMPLES.get(category, EXAMPLES["writing"])

    prompt = f"""You are an AI prompt engineer. One optimized prompt per tool.
USER WANTS: {output_label} about "{topic}" {sections_note}
TOOLS: {tools_list}
EXAMPLE: {example}
RULES: Tailored per tool. Action verb. Specific to "{topic}". 2-4 sentences. No essay content.

Respond ONLY in this exact JSON, no extra text, no markdown:
{{"general_prompt":"...","tool_prompts":{{"Tool Name":"prompt"}},"tips":["tip1","tip2","tip3"]}}"""

    res = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw = res.text.strip()
    # Remove markdown fences
    raw = raw.replace("```json", "").replace("```", "").strip()
    # Extract only JSON object
    start = raw.find('{')
    end   = raw.rfind('}')
    if start != -1 and end != -1:
        raw = raw[start:end+1]

    parsed = json.loads(raw)

    general = parsed.get("general_prompt", "")
    tps     = parsed.get("tool_prompts", {})
    tips    = parsed.get("tips", [])

    return {
        "topic":    topic,
        "prompt":   general,
        "tips":     "\n".join(f"- {t}" for t in tips),
        "tools":    [{**t, "tool_prompt": tps.get(t["name"], general)} for t in tools],
        "category": category,
    }