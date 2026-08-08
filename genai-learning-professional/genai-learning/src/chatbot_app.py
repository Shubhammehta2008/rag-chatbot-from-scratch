"""
Streamlit chatbot with conversation memory, powered by Groq (LLaMA 3.3 70B).

Run with:
    streamlit run src/chatbot_app.py
"""

import os
from rag_pipeline import ask_rag
import streamlit as st

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot")

# conversation memory 

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                # "You are a helpful assistant. Always respond in exactly "
                "3 bullet points, nothing more, nothing less."
            ),
        }
    ]

# Render previous messages (skip the hidden system prompt)
for msg in st.session_state.messages:

    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# user input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)


    # rag pipeline
    with st.chat_message("assistant"):

        with st.spinner("Searching document..."):

            try:
                ai_reply = ask_rag(user_input)

            except Exception as e:
                ai_reply = f"Error: {e}"

        st.write(ai_reply)

    # 3. Save AI response
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply,
        }
    )
