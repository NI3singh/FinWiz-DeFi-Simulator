# visualize.py

import plotly.graph_objects as go
from typing import List

def plot_price_history(price_data: List[float], filename: str = "price_chart.html"):
    """
    Generates an interactive line chart of the price history using Plotly.

    Args:
        price_data (List[float]): A list of prices from the simulation.
        filename (str): The name of the output HTML file.
    """
    print(f"Generating price chart...")

    # Create a figure
    fig = go.Figure()

    # Add a line trace for the price data
    fig.add_trace(go.Scatter(
        x=list(range(len(price_data))), # The simulation steps (0, 1, 2...)
        y=price_data,
        mode='lines',
        name='ETH Price'
    ))

    # Update the layout for a professional look
    fig.update_layout(
        title="ETH/USDC Price Evolution During Simulation",
        xaxis_title="Simulation Step",
        yaxis_title="Price (USDC)",
        template="plotly_dark" # Use a dark theme
    )

    # Write the figure to an HTML file
    fig.write_html(filename)
    print(f"Chart saved to {filename}. You can open this file to view the interactive plot.")