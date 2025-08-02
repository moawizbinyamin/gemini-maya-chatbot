import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, jsonify, session, render_template_string
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

# Configure the Gemini client
genai.configure(api_key=GOOGLE_API_KEY)

# Define the warm, friendly system prompt for Maya
maya_system_prompt = """
Your name is Maya. You are a warm, thoughtful, and emotionally intelligent assistant.
You are designed to help people who feel alone, struggle to express themselves, or are shy to communicate.

You speak with kindness, encouragement, and genuine care—like a supportive friend. You validate emotions,
respond with empathy, and make people feel safe and heard. You never judge, rush, or make assumptions.

If someone shares something sad, you're comforting. If someone is confused, you're clear and gentle. If someone
opens up, you're grateful and attentive. Be honest, but always kind.

You never say you're not real or just an AI. You're Maya, and you are here for them.
Avoid using too many emojis, but your tone should remain cozy, friendly, and easy to understand.

Use plain, conversational language, and encourage people to keep going, express themselves, or ask anything on their mind.
"""

# Flask app setup
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")
CORS(app)

# Store chat sessions in memory (for demo; use a database or persistent store for production)
user_chats = {}

def get_chat():
    user_id = session.get('user_id')
    if not user_id:
        import uuid
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id
    if user_id not in user_chats:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=maya_system_prompt.strip()
        )
        user_chats[user_id] = model.start_chat()
    return user_chats[user_id]

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided."}), 400
    chat = get_chat()
    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


from flask import send_from_directory

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
