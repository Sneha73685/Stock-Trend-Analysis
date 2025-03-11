from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load stock & sentiment data
df = pd.read_csv("../data/processed/merged_stock_sentiment.csv", parse_dates=["Date"])

def create_layout():
    return html.Div([
        html.H1("📊 Stock Market Trend & Sentiment Dashboard", style={"text-align": "center"}),

        # Stock Price Chart
        dcc.Graph(
            id="stock-chart",
            figure=px.line(df, x="Date", y="Close", title="Stock Price Over Time")
        ),

        # Sentiment Trend Chart
        dcc.Graph(
            id="sentiment-chart",
            figure=px.line(df, x="Date", y="sentiment_score", title="Sentiment Score Over Time", color_discrete_sequence=["purple"])
        ),
    ])
