# visualize.py

import plotly.graph_objects as go
from typing import List
from plotly.subplots import make_subplots

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


def plot_evaluation_results(price_data: List[float], portfolio_data: List[float], filename: str = "evaluation_chart.html"):
    """
    Generates an interactive chart with two Y-axes for price and portfolio value.
    """
    print(f"Generating evaluation chart...")

    # Create a figure with a secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add Price History trace
    fig.add_trace(
        go.Scatter(x=list(range(len(price_data))), y=price_data, name="ETH Price"),
        secondary_y=False,
    )

    # Add Portfolio Value trace
    fig.add_trace(
        go.Scatter(x=list(range(len(portfolio_data))), y=portfolio_data, name="Portfolio Value"),
        secondary_y=True,
    )

    # Add figure title and axis labels
    fig.update_layout(
        title_text="Agent Performance Evaluation",
        template="plotly_dark"
    )
    fig.update_xaxes(title_text="Simulation Step")
    fig.update_yaxes(title_text="<b>Price (USDC)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Portfolio Value (USDC)</b>", secondary_y=True)

    fig.write_html(filename)
    print(f"Chart saved to {filename}.")