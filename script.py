import os
import requests
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Ensure API key exists
if not API_KEY:
    print("Error: Missing API key. Please set OPENROUTER_API_KEY in .env file.")
    exit()

# Initialize chat history
chat_history = []

# Function to send a message and receive a response
def chat_with_bot(user_input):
    global chat_history  # Keep track of conversation

    # Add user input to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Create request payload
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": chat_history
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Send request
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        assistant_reply = data["choices"][0]["message"]["content"]

        # Add bot response to chat history
        chat_history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply
    else:
        return f"Error: {response.json()}"

# Chat loop
print("Chatbot: Hello! Type 'exit' to quit.\n")
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    bot_response = chat_with_bot(user_message)
    print(f"Chatbot: {bot_response}\n")
