import streamlit as st
import requests
import json
import pyttsx3
import speech_recognition as sr
from streamlit_lottie import st_lottie
from datetime import datetime
import logging
import os

# ---------------------------- Logging Setup ---------------------------- #
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------------- Voice Engine Setup ------------------------- #
def init_tts_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Alex" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    return engine

tts_engine = init_tts_engine()

# --------------------------- Lottie Animation -------------------------- #
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        logger.error("Failed to load Lottie animation: %s", e)
        return None

# ------------------------- Streamlit Config --------------------------- #
st.set_page_config(page_title="🎤 Beer's AI Chatbot", layout="centered")

# ----------------------------- CSS Styling ----------------------------- #
st.markdown("""
<style>
body {
    background-color: #030508;
    color: white;
}
.chat-container {
    border: 2px solid #00FFEA;
    border-radius: 12px;
    padding: 16px;
    background-color: #111;
    box-shadow: 0 0 10px #00FFEA;
}
.chat-bubble-user {
    background-color: #222;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 5px;
    color: #00FFEA;
}
.chat-bubble-ai {
    background-color: #1a1a1a;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 5px;
    color: #EA00FF;
}
.input-container {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #030508;
    padding: 10px;
    box-shadow: 0 -2px 10px #00FFEA;
}
</style>
""", unsafe_allow_html=True)

# ------------------------ Session State Init -------------------------- #
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'is_speaking' not in st.session_state:
    st.session_state.is_speaking = False

if 'current_reply' not in st.session_state:
    st.session_state.current_reply = ""

# ---------------------- Voice Recognition Logic ------------------------ #
def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak.")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            logger.info("Recognized voice input: %s", text)
            return text
        except sr.WaitTimeoutError:
            st.warning("No speech detected.")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("API unavailable or failed.")
    return ""

# ------------------------ Text-to-Speech Logic ------------------------ #
def speak_text(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        st.error(f"Speech Error: {e}")

# ------------------------ Local AI Model Call ------------------------- #
def get_ai_response(prompt):
    try:
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        r = requests.post("http://localhost:11434/api/generate", json=payload)
        return r.json().get("response", "Sorry, I couldn't understand that.")
    except Exception as e:
        logger.error("Model Error: %s", e)
        return "Error contacting AI model."

# ------------------------- Chatbot Logic ------------------------------ #
def handle_user_input(user_input):
    user_input = user_input.strip()
    st.session_state.chat_history.append(("user", user_input))

    # Predefined commands
    now = datetime.now()
    if "date" in user_input.lower():
        reply = f"Today's date is {now.strftime('%Y-%m-%d')}"
    elif "time" in user_input.lower():
        reply = f"Current time is {now.strftime('%H:%M:%S')}"
    elif "joke" in user_input.lower():
        reply = "Why did the developer go broke? Because he used up all his cache."
    elif "system" in user_input.lower():
        reply = f"Running on {os.name}, Python {os.sys.version.split()[0]}"
    else:
        reply = get_ai_response(user_input)

    st.session_state.chat_history.append(("ai", reply))
    st.session_state.current_reply = reply

# ---------------------------- Sidebar Help ---------------------------- #
st.sidebar.title("🌐 Help & Info")
st.sidebar.markdown("""
**Commands you can try:**
- "Tell me a joke"
- "What's the date?"
- "What's the time?"
- "System info"

**Tips:**
- Use the mic for voice input
- Click the speaker to hear replies

**Model Info:**
- Uses LLaMA 3 locally via Ollama
- Visit: http://localhost:11434
""")

# ------------------------- Chat
