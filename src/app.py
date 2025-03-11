import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock(ticker):
    df = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    return df

st.title("📈 Stock Market Trend Analysis")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")

if st.button("Analyze"):
    stock_data = fetch_stock(ticker)
    
    # Display Data
    st.write(stock_data.tail())

    # Plot Stock Price
    st.subheader(f"{ticker} Stock Closing Price")
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(stock_data["Close"], label="Closing Price", color="blue")
    ax.set_title(f"{ticker} Stock Price Over Time")
    ax.legend()
    st.pyplot(fig)
