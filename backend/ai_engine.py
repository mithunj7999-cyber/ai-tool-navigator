def classify_task(prompt):

    prompt = prompt.lower()

    if "ppt" in prompt or "presentation" in prompt or "slides" in prompt:
        return "presentation"

    elif "code" in prompt or "program" in prompt or "python" in prompt:
        return "coding"

    elif "image" in prompt or "design" in prompt:
        return "design"

    else:
        return "general"

def generate_options(category):

    tools = {
        "presentation": [
            {"tool": "Gamma AI", "performance": "High"},
            {"tool": "Beautiful.ai", "performance": "High"}
        ],

        "coding": [
            {"tool": "GitHub Copilot", "performance": "High"},
            {"tool": "ChatGPT", "performance": "High"}
        ],

        "design": [
            {"tool": "Canva AI", "performance": "High"},
            {"tool": "Adobe Firefly", "performance": "Medium"}
        ],

        "general": [
            {"tool": "ChatGPT", "performance": "High"},
            {"tool": "Gemini", "performance": "High"}
        ]
    }

    return tools.get(category, [])


def generate_full_response(prompt, sections=None):
    return f"AI generated response for: {prompt}"