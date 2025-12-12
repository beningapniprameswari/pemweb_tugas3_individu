from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Review
from schemas import ReviewCreate, ReviewResponse
import google.generativeai as genai
from transformers import pipeline
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Setup HuggingFace Sentiment ---
sentiment_model = pipeline("sentiment-analysis")

# --- Setup Gemini ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/analyze-review", response_model=ReviewResponse)
async def analyze_review(data: ReviewCreate, db: Session = Depends(get_db)):

    # 1. Sentiment
    sentiment_result = sentiment_model(data.text)[0]["label"]

    # 2. Keypoints
    model = genai.GenerativeModel("models/text-bison-001")
    response = model.generate_content(
        f"Extract key points from this review in simple bullet points:\n{data.text}"
    )
    keypoints = response.text

    # 3. Save DB
    new_review = Review(
        text=data.text,
        sentiment=sentiment_result,
        keypoints=keypoints
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

@app.get("/api/reviews")
async def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()
