import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(model="gemini-2.0-flash")
print("🤖 Gemini Chatbot")
print("Type 'exit' to quit.")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("AI: Goodbye!")
        break

    response = chat.send_message(question)

    print("AI:", response.text)
    response = chat.send_message(question)
    # print("--- HISTORY ---")
    # print(chat.get_history())
    # print("---------------")
    