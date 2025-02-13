from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral",  # We can also try "llama3" or "mixtral"
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
