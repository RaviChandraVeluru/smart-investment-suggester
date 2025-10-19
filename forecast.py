from prophet import Prophet
import pandas as pd


def generate_forecast(historical_data):
    """
    Generates a 1-year future price forecast using the Prophet model.

    Args:
        historical_data (pd.DataFrame): DataFrame containing historical stock data.

    Returns:
        tuple: A tuple containing the trained Prophet model and the forecast DataFrame.
    """
    # --- 1. Data Preparation ---
    # Prophet requires specific column names: 'ds' (datestamp) and 'y' (value)
    df_forecast = historical_data.reset_index()
    df_forecast = df_forecast[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})

    # Remove timezone information, as Prophet requires timezone-naive datetime objects
    df_forecast['ds'] = df_forecast['ds'].dt.tz_localize(None)

    # --- 2. Model Training ---
    model = Prophet()
    model.fit(df_forecast)

    # --- 3. Forecasting ---
    # Create a DataFrame for future dates (1 year = 365 days)
    future = model.make_future_dataframe(periods=365)

    # Generate the prediction
    forecast = model.predict(future)

    return model, forecast