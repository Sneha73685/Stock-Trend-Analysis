import yfinance as yf
import pandas as pd
import os

DATA_PATH = "../data/raw/"

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock price data from Yahoo Finance and save it."""
    os.makedirs(DATA_PATH, exist_ok=True)
    
    stock = yf.download(ticker, start=start_date, end=end_date)
    file_path = os.path.join(DATA_PATH, f"{ticker}.csv")
    
    stock.to_csv(file_path)
    print(f"✅ Data saved at: {file_path}")
    
    return stock

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    fetch_stock_data(ticker, start_date, end_date)
