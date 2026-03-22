import os
from google import genai
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(env_path)

_client = None

def get_client():
    global _client
    if _client is None:
        key = os.getenv("GEMINI_API_KEY")
        _client = genai.Client(api_key=key)
    return _client
