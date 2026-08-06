"""
Streamlit chatbot with conversation memory, powered by Groq (LLaMA 3.3 70B).

Run with:
    streamlit run src/chatbot_app.py
"""

import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

st.set_page_config(page_title="AI Chatbot with Memory", page_icon="🤖")
st.title("🤖 AI Chatbot with Memory")

if not API_KEY:
    st.error(
        "GROQ_API_KEY is not set. Create a `.env` file (see `.env.example`) "
        "and add your Groq API key before using the chatbot."
    )
    st.stop()

if "client" not in st.session_state:
    st.session_state.client = Groq(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. Always respond in exactly "
                "3 bullet points, nothing more, nothing less."
            ),
        }
    ]

# Render previous messages (skip the hidden system prompt)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Send the full conversation history so the model has context
    response = st.session_state.client.chat.completions.create(
        model=MODEL_NAME,
        messages=st.session_state.messages,
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
