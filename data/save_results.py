import pandas as pd
import os

RESULTS_PATH = "../data/results/"

def save_predictions(ticker, predictions):
    """Save stock price predictions to CSV."""
    os.makedirs(RESULTS_PATH, exist_ok=True)
    
    file_path = os.path.join(RESULTS_PATH, f"{ticker}_predictions.csv")
    predictions.to_csv(file_path)
    
    print(f"✅ Predictions saved at: {file_path}")

if __name__ == "__main__":
    # Example: Fake predictions for testing
    example_preds = pd.DataFrame({
        "Date": pd.date_range(start="2025-01-01", periods=10, freq="D"),
        "Predicted_Close": [150, 152, 149, 153, 155, 157, 159, 162, 160, 165]
    }).set_index("Date")
    
    save_predictions("AAPL", example_preds)
