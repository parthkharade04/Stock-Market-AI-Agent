from duckduckgo_search import DDGS
from langchain.tools import tool

@tool
def get_stock_price(ticker: str) -> float:
    """Fetches current stock price for given ticker using web search"""
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(f"{ticker} stock price", max_results=1)]
        
    if not results:
        return 0.0
        
    try:
        # Extract numerical value from text
        return float(''.join(
            c for c in results[0]['body'].split()[0] 
            if c.isdigit() or c == '.'
        ))
    except:
        return 0.0