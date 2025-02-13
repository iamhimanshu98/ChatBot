from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = "You said: " + user_input  # Placeholder response
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
