# Smart Investment Suggester 📈

## About This Project

This is a multi-page web application built with Streamlit that serves as a toolkit for basic investment analysis. The app provides tools for calculating fixed deposit returns, analyzing historical stock performance, and generating machine learning-based future price forecasts.

## Features

- **FD Calculator:** Calculates the maturity amount for Fixed Deposits using real, up-to-date interest rates from various Indian banks.
- **Historical Performance Analyzer:** Fetches 5 years of historical data for any NSE-listed stock, calculates its Compound Annual Growth Rate (CAGR), and visualizes the growth of a user-defined investment.
- **Future Price Forecaster:** Uses the Prophet time-series model to generate and visualize a 1-year forecast of a stock's future price trend.

## Technology Stack

- **Language:** Python
- **Core Libraries:** Streamlit, Pandas, yfinance, Matplotlib, Prophet

## How to Run It Locally

1.  Clone this repository.
2.  Create and activate a virtual environment: `python -m venv venv`
3.  Install the dependencies: `pip install -r requirements.txt`
4.  Run the app: `streamlit run app.py`

## Screenshot

![App Screenshot](image_f0ca87.png)