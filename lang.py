from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
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

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],              # Allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],             # POST, GET, OPTIONS
    allow_headers=["*"],             # Content-Type, Authorization
)

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
