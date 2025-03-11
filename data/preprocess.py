import pandas as pd
import os

RAW_DATA_PATH = "../data/raw/"
PROCESSED_DATA_PATH = "../data/processed/"

def preprocess_stock_data(ticker):
    """Load raw stock data, clean it, and save to processed folder."""
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    file_path = os.path.join(RAW_DATA_PATH, f"{ticker}.csv")
    df = pd.read_csv(file_path, index_col="Date", parse_dates=True)

    # Drop missing values
    df = df.dropna()

    # Create additional features
    df["Daily Return"] = df["Close"].pct_change()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["SMA_200"] = df["Close"].rolling(window=200).mean()

    # Save processed file
    processed_file_path = os.path.join(PROCESSED_DATA_PATH, f"{ticker}_processed.csv")
    df.to_csv(processed_file_path)
    
    print(f"✅ Processed data saved at: {processed_file_path}")
    return df

if __name__ == "__main__":
    ticker = "AAPL"
    preprocess_stock_data(ticker)
