import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data from Yahoo Finance."""
    stock = yf.download(ticker, start=start_date, end=end_date)
    stock.to_csv(f"../data/raw/{ticker}.csv")  # Save to raw data folder
    return stock

if __name__ == "__main__":
    ticker = "AAPL"  # Example: Apple stock
    start_date = "2020-01-01"
    end_date = "2025-01-01"
    
    df = fetch_stock_data(ticker, start_date, end_date)
    print(df.head())
