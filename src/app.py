from fastapi import FastAPI
from pydantic import BaseModel
from .stock_agent import analyze_stock

app = FastAPI(
    title="Stock Analysis API",
    description="AI-powered stock market analysis",
    version="0.1.0"
)

class AnalysisRequest(BaseModel):
    ticker: str
    question: str = "Should I invest?"

@app.post("/analyze-stock")
async def analyze_endpoint(request: AnalysisRequest):
    return analyze_stock(request.ticker, request.question)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}