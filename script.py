import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")  # Get API key from .env
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "meta-llama/llama-3-8b-instruct",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

response = requests.post(API_URL, json=payload, headers=headers)
print(response.json())
