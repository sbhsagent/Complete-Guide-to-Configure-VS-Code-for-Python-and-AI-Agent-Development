import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.rag_chain import get_rag_chain

# Load environment variables from .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI(
    title="RAG API Server",
    version="1.0",
    description="A simple API server for a Retrieval-Augmented Generation agent.",
)


# --- Pydantic Models for Request and Response ---
class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


# --- API Endpoints ---
@app.get("/", summary="Health Check")
async def health_check():
    """A simple health check endpoint to confirm the server is running."""
    return {"status": "ok", "message": "RAG API is running"}


@app.post("/query", response_model=QueryResponse, summary="Query the RAG Agent")
async def query_agent(request: QueryRequest):
    """
    Receives a question, processes it through the RAG chain, and returns the answer.
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY not found in environment variables.",
        )

    if not request.question:
        raise HTTPException(status_code=400, detail="Question field cannot be empty.")

    try:
        # Get the singleton RAG chain instance
        rag_chain = get_rag_chain()
        answer = rag_chain.invoke(request.question)
        return QueryResponse(answer=answer)
    except Exception as e:
        # A generic error handler for issues during chain invocation
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# To run this app:
# uvicorn src.main_rag_api:app --reload --port 8000
