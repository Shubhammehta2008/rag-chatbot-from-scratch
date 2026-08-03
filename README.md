# 🤖 AI Chatbot with Memory

A conversational AI chatbot built with Python, Streamlit, and the Groq API. 
The chatbot maintains conversation history, allowing it to remember context 
across multiple messages in a session.

## Features

- Real-time chat interface built with Streamlit
- Powered by Groq's LLaMA 3.3 70B model for fast inference
- Maintains full conversation memory within a session
- Clean, chat-bubble style UI

## Tech Stack

- **Python** – core logic
- **Streamlit** – web UI framework
- **Groq API** – LLM inference (LLaMA 3.3 70B)
- **python-dotenv** – secure API key management

## How It Works

The app stores conversation history in Streamlit's `session_state` and sends 
the full history with each request to the Groq API, allowing the model to 
maintain context across the conversation.

## Setup

1. Clone this repository
2. Install dependencies:
## Screenshots
![Chatbot Screenshot](c:\Users\Shubham Mehta\Pictures\Screenshots\Screenshot 2026-08-03 144451.png)