"""
Streamlit chatbot with conversation memory, powered by Groq.

Run with:
    streamlit run src/chatbot_app.py
"""

import streamlit as st
from rag_pipeline import ask_rag


# -------------------------
# Streamlit configuration
# -------------------------

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
)

st.title("🤖 RAG Chatbot")


# -------------------------
# Conversation memory
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------
# Render previous messages
# -------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# -------------------------
# User input
# -------------------------

user_input = st.chat_input("Type your message...")


if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):
        st.write(user_input)


    # -------------------------
    # RAG pipeline
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("Searching document..."):

            try:
                ai_reply = ask_rag(user_input)

            except Exception as e:
                ai_reply = f"Error: {e}"

        st.write(ai_reply)


    # -------------------------
    # Save AI response
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply,
        }
    )