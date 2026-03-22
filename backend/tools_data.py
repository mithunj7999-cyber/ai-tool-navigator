# backend/tools_data.py
# Pure data — no logic. Add or remove tools here only.

AI_TOOLS = {
    "presentation": [
        {"name": "Gamma AI", "link": "https://gamma.app", "availability": "Free", "best_for": "AI-powered presentations",
         "steps": ["Go to gamma.app and sign up free", "Click Create new and select Presentation", "Paste your generated prompt", "Choose a theme and click Generate", "Edit slides and export as PDF or PPT"]},
        {"name": "Canva AI", "link": "https://canva.com", "availability": "Free/Paid", "best_for": "Beautiful slide design",
         "steps": ["Go to canva.com and log in", "Search Presentation and pick a template", "Use Magic Write to generate slide content", "Customize colors fonts and images", "Download as PPT or share the link"]},
        {"name": "Beautiful.ai", "link": "https://beautiful.ai", "availability": "Paid (free trial)", "best_for": "Smart auto-layout slides",
         "steps": ["Go to beautiful.ai and start free trial", "Click New Presentation", "Choose a Smart Slide type for each section", "Add your AI-generated content", "Export or present directly from browser"]},
    ],
    "image": [
        {"name": "Midjourney", "link": "https://midjourney.com", "availability": "Paid", "best_for": "High-quality AI art generation",
         "steps": ["Join Midjourney via midjourney.com", "Use /imagine command with your prompt", "Choose your preferred variation", "Upscale the best result", "Download the final image"]},
        {"name": "Adobe Firefly", "link": "https://firefly.adobe.com", "availability": "Free/Paid", "best_for": "Commercial-safe AI images",
         "steps": ["Go to firefly.adobe.com", "Click Text to image", "Paste your image prompt", "Adjust style and aspect ratio", "Download in high resolution"]},
        {"name": "DALL-E (ChatGPT)", "link": "https://chat.openai.com", "availability": "Paid", "best_for": "AI image from text",
         "steps": ["Open ChatGPT Plus", "Select GPT-4 with image generation", "Paste your image prompt", "Download the generated image", "Regenerate with tweaks if needed"]},
    ],
    "writing": [
        {"name": "ChatGPT", "link": "https://chat.openai.com", "availability": "Free/Paid", "best_for": "Essays articles summaries",
         "steps": ["Go to chat.openai.com", "Paste your generated prompt", "Review and refine the output", "Ask for rewrites or edits", "Copy the final content"]},
        {"name": "Gemini", "link": "https://gemini.google.com", "availability": "Free", "best_for": "Research-backed writing",
         "steps": ["Go to gemini.google.com", "Type your writing request", "Use Show drafts for variations", "Export to Google Docs directly", "Edit and finalize"]},
    ],
    "coding": [
        {"name": "GitHub Copilot", "link": "https://github.com/features/copilot", "availability": "Paid (free for students)", "best_for": "Code autocomplete and generation",
         "steps": ["Install VS Code extension GitHub Copilot", "Sign in with your GitHub account", "Start typing and Copilot suggests completions", "Press Tab to accept a suggestion", "Use Copilot Chat for complex questions"]},
        {"name": "ChatGPT", "link": "https://chat.openai.com", "availability": "Free/Paid", "best_for": "Code generation and debugging",
         "steps": ["Go to chat.openai.com", "Describe your coding problem", "Paste the generated prompt", "Copy the code and test it", "Ask for bug fixes or explanations"]},
    ],
    "video": [
        {"name": "Runway ML", "link": "https://runwayml.com", "availability": "Free/Paid", "best_for": "AI video generation and editing",
         "steps": ["Go to runwayml.com and sign up", "Choose Gen-2 text-to-video", "Paste your video prompt", "Generate and preview the video", "Download or share your video"]},
        {"name": "Pictory", "link": "https://pictory.ai", "availability": "Paid", "best_for": "Script to video conversion",
         "steps": ["Go to pictory.ai and sign up", "Paste your script or article", "Choose a video template", "Edit scenes and add voiceover", "Export and download"]},
    ],
    "research": [
        {"name": "Perplexity AI", "link": "https://perplexity.ai", "availability": "Free/Paid", "best_for": "AI-powered research with sources",
         "steps": ["Go to perplexity.ai", "Type your research question", "Review answers with citations", "Use Focus mode for academic sources", "Export or copy the research"]},
        {"name": "ChatGPT", "link": "https://chat.openai.com", "availability": "Free/Paid", "best_for": "Deep research and summaries",
         "steps": ["Go to chat.openai.com", "Paste your research prompt", "Ask for structured output", "Request citations and sources", "Refine with follow-up questions"]},
    ],
    "audio": [
        {"name": "Suno AI", "link": "https://suno.com", "availability": "Free/Paid", "best_for": "AI music and song generation",
         "steps": ["Go to suno.com and sign in", "Click Create and choose Custom or Simple mode", "Paste your prompt describing the style and mood", "Click Generate and wait about 30 seconds", "Download the audio or share the link"]},
        {"name": "Udio", "link": "https://udio.com", "availability": "Free/Paid", "best_for": "High-quality AI music creation",
         "steps": ["Go to udio.com and log in", "Type your music prompt with style mood instruments", "Click Generate", "Extend or remix the best variation", "Download the final audio file"]},
        {"name": "ElevenLabs", "link": "https://elevenlabs.io", "availability": "Free/Paid", "best_for": "AI voice and speech generation",
         "steps": ["Go to elevenlabs.io and sign up free", "Click Text to Speech", "Paste your script or prompt text", "Choose a voice style and emotion", "Generate and download the audio"]},
        {"name": "Mubert", "link": "https://mubert.com", "availability": "Free/Paid", "best_for": "AI background music generation",
         "steps": ["Go to mubert.com", "Describe the mood or use case", "Set duration and tempo", "Generate the track", "Download royalty-free music"]},
    ],
    "ai_tool_usage": [
        {"name": "ChatGPT", "link": "https://chat.openai.com", "availability": "Free/Paid", "best_for": "General AI assistant",
         "steps": ["Go to chat.openai.com", "Paste your generated prompt", "Review and refine the output", "Ask follow-up questions to improve", "Copy or export the final result"]},
        {"name": "Gemini", "link": "https://gemini.google.com", "availability": "Free", "best_for": "Google-powered AI assistant",
         "steps": ["Go to gemini.google.com", "Paste your prompt", "Use Show drafts for variations", "Export directly to Google Docs", "Refine with follow-up prompts"]},
    ],
}
