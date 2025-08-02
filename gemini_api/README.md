# Gemini API Chatbot with Maya

This project provides a conversational web interface to Google's Gemini API, featuring Maya—a warm, emotionally intelligent assistant.

## Features
- Conversational chat with Gemini API (Maya persona)
- Web frontend (HTML/CSS/JS) for a modern chat experience
- Smart conversation ending (detects "bye", "exit", etc.)
- Session-based chat context

## Directory Structure
```
gemini_api/
│   main.py              # Flask backend and Gemini API logic
│   requirements.txt     # Python dependencies
│   README.md            # Project documentation
│
└───static/
    │   index.html       # Frontend HTML
    │   style.css        # Frontend CSS
    │   app.js           # Frontend JS
```

## Setup
1. Clone the repository and navigate to `gemini_api/`.
2. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key
   FLASK_SECRET_KEY=your_flask_secret_key
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python main.py
   ```
5. Open your browser to [http://localhost:5000](http://localhost:5000)

## Usage
- Type your message and press Send.
- To end the conversation, type "bye", "exit", or click the End Conversation button.

## Notes
- For production, use a persistent session store instead of in-memory sessions.
- The frontend is in the `static/` folder and can be customized.

---
**Maya** is here to listen, support, and encourage you. 🌸
