import dash
from dash import html, dcc
from layout import create_layout

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Set layout from external file
app.layout = create_layout()

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)
