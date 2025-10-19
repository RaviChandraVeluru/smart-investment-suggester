import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_historical_data(ticker):
    """
    Fetches 5 years of historical stock data for a given ticker from Yahoo Finance.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'RELIANCE.NS').

    Returns:
        pd.DataFrame: A DataFrame containing the historical data, or an empty DataFrame if not found.
    """
    stock = yf.Ticker(ticker)
    hist_data = stock.history(period='5y')
    return hist_data


def calculate_cagr(historical_data):
    """
    Calculates the Compound Annual Growth Rate (CAGR) from historical stock data.

    Args:
        historical_data (pd.DataFrame): DataFrame containing 'Close' prices.

    Returns:
        float: The calculated CAGR as a percentage.
    """
    # Get the first and last closing prices
    end_value = historical_data['Close'].iloc[-1]
    start_value = historical_data['Close'].iloc[0]

    # Calculate the number of years, accounting for trading days (~252 per year)
    num_years = len(historical_data) / 252

    # Calculate CAGR using the formula
    cagr = ((end_value / start_value) ** (1 / num_years)) - 1

    return cagr * 100


def plot_investment_growth(historical_data, initial_investment):
    """
    Generates a Matplotlib chart showing the growth of a hypothetical investment.

    Args:
        historical_data (pd.DataFrame): DataFrame containing 'Close' prices.
        initial_investment (float): The starting amount of the investment.

    Returns:
        matplotlib.figure.Figure: The generated plot figure.
    """
    # Normalize the closing prices to track growth from a starting point of 1
    normalized_prices = historical_data['Close'] / historical_data['Close'].iloc[0]

    # Calculate the value of the investment over time
    investment_value = normalized_prices * initial_investment

    # --- Create the Plot ---
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axes for the plot
    ax.plot(investment_value.index, investment_value)

    # --- Formatting ---
    ax.set_title(f"Growth of a ₹{initial_investment:,.0f} Investment", fontsize=16)
    ax.set_ylabel("Investment Value (₹)")
    ax.grid(True, linestyle='--', alpha=0.6)  # Add a grid for readability

    return fig