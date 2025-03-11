import pandas as pd
import matplotlib.pyplot as plt

def moving_averages(df, short_window=50, long_window=200):
    """Calculate short and long moving averages."""
    df["SMA_50"] = df["Close"].rolling(window=short_window).mean()
    df["SMA_200"] = df["Close"].rolling(window=long_window).mean()
    return df

def plot_moving_averages(df, ticker):
    """Plot stock prices with moving averages."""
    plt.figure(figsize=(12,6))
    plt.plot(df["Close"], label=f"{ticker} Closing Price", alpha=0.7)
    plt.plot(df["SMA_50"], label="50-Day SMA", linestyle="--")
    plt.plot(df["SMA_200"], label="200-Day SMA", linestyle="--")
    plt.title(f"{ticker} Stock Price with Moving Averages")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"
    df = pd.read_csv(f"../data/raw/{ticker}.csv", index_col="Date", parse_dates=True)
    df = moving_averages(df)
    plot_moving_averages(df, ticker)
