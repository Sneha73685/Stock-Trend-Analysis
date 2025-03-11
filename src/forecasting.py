import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(df):
    """Train ARIMA model for stock forecasting."""
    model = ARIMA(df["Close"], order=(5,1,0))  # ARIMA(5,1,0) - Change params if needed
    model_fit = model.fit()
    return model_fit

def forecast_next_days(model_fit, steps=30):
    """Forecast stock prices for the next N days."""
    forecast = model_fit.forecast(steps=steps)
    return forecast

def plot_forecast(df, forecast, steps=30):
    """Plot actual vs. predicted stock prices."""
    plt.figure(figsize=(10,5))
    plt.plot(df["Close"], label="Actual Prices")
    plt.plot(pd.date_range(start=df.index[-1], periods=steps, freq='D'), forecast, label="Predicted", linestyle="--")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"
    df = pd.read_csv(f"../data/raw/{ticker}.csv", index_col="Date", parse_dates=True)
    
    model_fit = train_arima_model(df)
    forecast = forecast_next_days(model_fit, steps=30)
    
    plot_forecast(df, forecast, steps=30)
