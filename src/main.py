import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Load environment variables first
load_dotenv()

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="AI Agent Server", version="1.0.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# --- State object to hold the model ---
class AppState:
    llm = None


# --- Pydantic model for request body ---
class PredictionRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.5


# --- App startup event to initialize the model ---
@app.on_event("startup")
async def startup_event():
    # Initialize with error handling
    if not os.getenv("OPENAI_API_KEY"):
        print(
            "🔴 CRITICAL: OPENAI_API_KEY is not set. The /predict endpoint will not work."
        )
        AppState.llm = None
    else:
        try:
            AppState.llm = ChatOpenAI(model="gpt-4o-mini")
            print("✅ OpenAI client initialized successfully.")
        except Exception as e:
            print(f"🔴 CRITICAL: Could not initialize OpenAI client: {e}")
            AppState.llm = None


# --- API Endpoints ---
@app.post("/predict")
@limiter.limit("5/minute")  # Limit to 5 requests per minute per IP
async def predict(request: PredictionRequest, req: Request):
    if AppState.llm is None:
        raise HTTPException(
            status_code=503,
            detail="AI model is not available. Check server logs for initialization errors.",
        )

    try:
        messages = [HumanMessage(content=request.prompt)]
        # Use the model instance from the app state
        response = AppState.llm.invoke(messages)
        return {"response": response.content}
    except Exception as e:
        # Catch potential API errors during invocation
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {e}",
        )


@app.get("/health")
async def health_check():
    health_status = {
        "status": "healthy",
        "message": "AI Agent Server is running",
        "model_initialized": AppState.llm is not None,
    }
    return health_status
