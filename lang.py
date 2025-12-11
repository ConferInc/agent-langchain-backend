from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize model
llm = ChatOpenAI(
    model="gpt-4.1-nano",
    openai_api_key=openai_api_key,
    openai_api_base="https://litellm.confer.today"
)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = llm.invoke(req.message)
    return {"response": response.content}

# Run on Uvicorn (PRODUCTION MODE)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("lang:app", host="0.0.0.0", port=4000)
