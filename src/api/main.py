from fastapi import FastAPI
from pydantic import BaseModel

from src.pipeline.pipeline import run_pipeline
from typing import Optional
from src.harness.feedback.feedback_store import save_feedback

class FeedbackRequest(BaseModel):

    session_id: str

    question: str

    sql: str

    summary: str

    rating: str

    corrected_sql: Optional[str] = None



app = FastAPI(
    title="NL to SQL API",
    version="1.0"
)


class QueryRequest(BaseModel):
    session_id: str = "default"
    role: str = "executive"
    question: str


@app.get("/")
def home():

    return {
        "message": "NL to SQL API Running"
    }


@app.post("/query")
def query(request: QueryRequest):
    return run_pipeline(
        question=request.question,
        session_id=request.session_id,
        role=request.role
    )

@app.post("/feedback")
def feedback(request: FeedbackRequest):

    save_feedback(
        session_id=request.session_id,
        question=request.question,
        sql=request.sql,
        summary=request.summary,
        rating=request.rating,
        corrected_sql=request.corrected_sql
    )

    return {
        "success": True,
        "message": "Feedback Saved Successfully"
    }