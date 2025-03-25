#import required libraries
import streamlit as st
import speech_recognition as sr
from utils import get_openai_response, PREDEFINED_RESPONSES

def transcribe_audio():
    """Captures audio and converts to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "Could not request results. Check your internet connection."



# Streamlit UI
st.set_page_config(page_title="Voice Chatbot", page_icon="🗣", layout="wide")

st.title("🗣 Voice-Driven Chatbot")
st.write("### Ask one of the predefined questions using keywords:")

# Styling Sidebar
st.sidebar.image("https://static.vecteezy.com/system/resources/previews/053/465/553/non_2x/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector.jpg", width=100)
st.sidebar.title("Chatbot Info")
st.sidebar.write("This chatbot responds to predefined questions based on keywords.")
st.sidebar.markdown("---")

st.markdown(
    "<style> .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; } </style>",
    unsafe_allow_html=True
)

st.write("\n".join([f"- {q}" for q in PREDEFINED_RESPONSES.keys()]))

if st.button("🎤 Speak to Voice-Chatbot"):
    user_input = transcribe_audio()
    st.write(f"**You said:** {user_input}")
    
    if user_input:
        response_text = get_openai_response(user_input)
        st.success(response_text)


