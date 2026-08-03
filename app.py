import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.title("🤖 My Groq Chatbot")

# Client ko session_state mein rakho
if "client" not in st.session_state:
    st.session_state.client = Groq(api_key=api_key)

# History ko khud maintain karo (Groq mein built-in chat session nahi hota)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani messages screen par dikhao
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    # User ka message history mein add karo
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Poori history bhejo Groq ko (sirf naya message nahi)
    response = st.session_state.client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    ai_reply = response.choices[0].message.content

    # AI ka response history mein add karo
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)