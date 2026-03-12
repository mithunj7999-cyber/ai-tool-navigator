def tool_recommender(category):

    tools_db = {
        "presentation": [
            {"name": "Gamma AI", "performance": 9, "link": "https://gamma.app"},
            {"name": "Canva AI", "performance": 8.5, "link": "https://canva.com"},
        ],
        "coding": [
            {"name": "GitHub Copilot", "performance": 9.5, "link": "https://github.com/copilot"},
            {"name": "ChatGPT", "performance": 9, "link": "https://chat.openai.com"},
        ],
        "general": [
            {"name": "ChatGPT", "performance": 9, "link": "https://chat.openai.com"},
            {"name": "Gemini", "performance": 8.5, "link": "https://gemini.google.com"},
        ]
    }

    return tools_db.get(category, tools_db["general"])