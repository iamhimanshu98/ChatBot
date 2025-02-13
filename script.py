import requests

API_KEY = "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"
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
