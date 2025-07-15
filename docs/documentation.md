1. Overview

The LLM Web Chatbot is an AI-powered conversational assistant built using apache, a Python-based framework for creating interactive web apps. This chatbot offers both text and voice-based interaction, and communicates with a locally hosted llama3 model via Ollama to generate intelligent and context-aware responses.

Key functionalities include real-time streamed responses, text-to-speech output, Lottie animations, and a neon-themed UI. Designed for offline usage, this project is ideal for developers and AI enthusiasts who want to explore local LLMs with integrated speech capabilities.
2. Table of Contents

    Overview

    Table of Contents

    Features

    Technologies Used

    Project Structure

    Setup Instructions

    Usage Guide

    Code Explanation

        8.1 Streamlit Layout

        8.2 LLM Integration

        8.3 Voice Input

        8.4 Text-to-Speech

        8.5 Lottie Animation

        8.6 Custom Styling

    Session Management

    Error Handling

    Limitations

    Future Enhancements

    License

3. Features

    Text Input: Type your queries directly in the chat input bar.

    Voice Input: Speak to the bot using your system’s microphone.

    Text-to-Speech Output: The bot’s replies can be spoken aloud.

    Streamed Responses: Receive real-time, token-by-token replies from the LLM.

    Offline Model: Interacts with a local Gemma:7b model via Ollama.

    Special Commands: Recognizes phrases like “show date” and “tell me the time.”

    Neon-Themed Interface: Stylish UI with glowing chat bubbles and animated elements.

    Lottie Animation: Displays an engaging animation to enhance user experience.

    Session History: Retains chat history throughout the session.

4. Technologies Used
Technology	Purpose
Python 3.8+	Core language
Streamlit	Web UI framework
Ollama	Local model server for Gemma:7b
requests	HTTP communication with the LLM backend
speech_recognition	Voice input capture and transcription
pyttsx3	Text-to-speech conversion
streamlit_lottie	Animation rendering
datetime	Command handling (e.g., date and time)
CSS	Custom user interface styling
5. Project Structure

llm-web-chatbot/
│
├── app.py                # Main application script
├── requirements.txt      # Required Python dependencies
└── assets/
    └── chatbot.json      # Lottie animation file (optional)

6. Setup Instructions
6.1 Clone the Repository

git clone https://github.com/Balkaransinghgill/llm-web-chatbot.git
cd llm-web-chatbot

6.2 Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

6.3 Install Dependencies

pip install -r requirements.txt

6.4 Launch Ollama with llama3 Model

ollama run llama3

Make sure it's running at http://localhost:11434/api/generate.
6.5 Run the Application

streamlit run app.py

Your app will be live at http://localhost:8501.
7. Usage Guide

    Open the app in your browser.

    Type a message or press the 🎤 button to speak.

    View the AI’s response in the chat window.

    Press 🔊 to hear the AI's response aloud.

    Use special commands like:

        “Show date”

        “Tell me the time”

        “Show datetime”

8. Code Explanation
8.1 Streamlit Layout

    The app uses st.set_page_config to define layout and page title.

    Chat messages are rendered in a styled container.

    The input bar is fixed at the bottom for seamless UX.

8.2 LLM Integration

    The user prompt is sent via a POST request:

POST http://localhost:11434/api/generate

The payload:

    {
      "model": "llama3",
      "prompt": "Your input",
      "stream": true
    }

    Streamed responses are parsed in real-time and displayed incrementally.

8.3 Voice Input

    Uses speech_recognition to capture voice.

    Sends audio to Google’s API for transcription.

    Handles timeouts and microphone access issues.

8.4 Text-to-Speech

    Uses pyttsx3 to vocalize AI responses.

    Configurable voice settings for different OS platforms.

    Controlled using a "Speak" button.

8.5 Lottie Animation

    Fetches animation JSON from a URL or file.

    Renders it with streamlit_lottie.

    Used to visually enrich the chat interface.

8.6 Custom Styling

    Neon cyan border effects with box-shadow.

    Dark theme with modern hover transitions.

    Custom scrollbar and chat bubbles.

    Injected with unsafe_allow_html=True in st.markdown.

9. Session Management

    st.session_state maintains:

        chat_history: List of (user, bot) message pairs.

        is_speaking: Tracks TTS status.

        current_reply: Last AI reply for speaking.

This ensures persistence across user interactions.
10. Error Handling
Error Type	Handling Method
Voice timeout	Prompts the user to retry
Unrecognized speech	Alerts the user for unclear audio
API/network failures	Displays error messages inside chat
TTS failure	Logs or prints descriptive error messages
11. Limitations

    Voice Output Compatibility: Default voice may differ by OS.

    Local Model Requirement: Ollama + llama3 must be running.

    English Only: Current setup supports English interaction only.

    No Long-Term Storage: Chat history is session-based.

    Google Speech API Dependence: Requires internet for voice input.

12. Future Enhancements

    Add multilingual input/output support.

    Allow voice configuration on Windows and Linux.

    Enable persistent chat storage using databases or JSON.

    Introduce user authentication for multiple sessions.

    Add theming options and additional Lottie animations.

    Integrate external model APIs (e.g., OpenAI, Mistral).

13. License

This project is licensed under the MIT License.
Please refer to the LICENSE file for full terms and conditions.