import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

NEWS_API_KEY = "YOUR_NEWS_API_KEY"  # Get from https://newsapi.org/
SENTIMENT_DATA_PATH = "../data/raw/sentiment_data.csv"

def fetch_financial_news(ticker, num_articles=10):
    """Fetch recent financial news headlines for a stock ticker."""
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json()["articles"][:num_articles]
        return [{"date": a["publishedAt"], "headline": a["title"]} for a in articles]
    return []

def analyze_sentiment(news_list):
    """Analyze sentiment of news headlines using VADER."""
    analyzer = SentimentIntensityAnalyzer()
    for news in news_list:
        sentiment_score = analyzer.polarity_scores(news["headline"])["compound"]
        news["sentiment_score"] = sentiment_score
    return news_list

if __name__ == "__main__":
    ticker = "AAPL"
    news = fetch_financial_news(ticker)
    sentiment_data = analyze_sentiment(news)

    # Save to CSV
    df = pd.DataFrame(sentiment_data)
    os.makedirs("../data/raw/", exist_ok=True)
    df.to_csv(SENTIMENT_DATA_PATH, index=False)
    print(f"✅ Sentiment data saved at: {SENTIMENT_DATA_PATH}")
