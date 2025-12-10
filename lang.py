from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemma-3-4b-it", api_key=gemini_api_key)

print("Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        break
    response = llm.invoke(user_input)
    print(f"Bot: {response.content}")