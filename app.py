# --- Core Libraries ---
import streamlit as st
import pandas as pd

# --- Custom Modules ---
from calculations import calculate_fd_return
from analysis import fetch_historical_data, calculate_cagr,plot_investment_growth
from forecast import generate_forecast

# --- Data Loading ---
# Load the bank interest rate data from the CSV file
df = pd.read_csv('interest_rates.csv')

# --- Page Configuration & Title ---
st.set_page_config(page_title="Smart Investment Suggester", layout="wide")
st.title("Smart Investment Suggester 📈")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go To",['FD Calculator','Historical Analysis','Future Forecast'])

# ==============================================================================
# --- PAGE 1: FIXED DEPOSIT (FD) CALCULATOR ---
# ==============================================================================
if selection == 'FD Calculator':
    st.header("Fixed Deposit Returns Calculator")

    # --- User Inputs for FD Calculator ---
    st.sidebar.header("User Input Parameters")
    principal_amount = st.sidebar.number_input("Principal Amount (₹)", min_value=10000, step=1000)
    years = st.sidebar.slider("Investment Tenure (Years)", min_value=1, max_value=5, step=1)
    bank = st.sidebar.selectbox('Select a Bank', df['bank_name'].unique().tolist(), index=0)

    # --- Calculation and Display Logic ---
    if bank == "Select your bank":
        st.warning('Please Choose a Bank !.')
    else:
        # Filter the DataFrame to find the correct interest rate
        interest_df =df[(df['bank_name']==bank)& (df['tenure_years']== years)]
        if st.button('Calculate'):

            # Ensure an interest rate was found before calculating
            if not interest_df.empty:
                rate = interest_df['interest_rate'].iloc[0]

                # Perform the calculation
                final_amount = calculate_fd_return(principal_amount, rate, years)
                interest_earned = final_amount - principal_amount

                # Display the results in columns for a clean layout
                col1, col2, col3, col4 = st.columns(4)
                col1.metric('Interest Rate', f"{rate}%")
                col2.metric('Principal Amount', f"₹{principal_amount:,.0f}")
                col3.metric('Interest Earned', f"₹{interest_earned:,.2f}")
                col4.metric("Maturity Amount", f"₹{final_amount:,.2f}")
            else:
                st.error(f"No interest rate data found for {bank} for a {years}-year tenure.")

# ==============================================================================
# --- PAGE 2: HISTORICAL PERFORMANCE ANALYZER ---
# ==============================================================================
elif selection == 'Historical Analysis':
    st.header("Historical Performance Analyzer")

    # --- User Inputs for Historical Analysis ---
    principal_amount = st.sidebar.number_input("Initial Investment (₹)", min_value=10000, step=1000)
    ticker_input = st.text_input("Enter Stock Ticker (e.g., RELIANCE.NS for NSE)")

    # --- Analysis Logic ---
    if st.button('Analyze Performance'):
        if ticker_input:  # Check if the user has entered a ticker
            try:
                # Attempt to fetch the historical data
                data = fetch_historical_data(ticker_input)

                if not data.empty:
                    st.toast(f"Displaying data for {ticker_input}", icon="📊")

                    # --- Calculations & Visualization ---
                    cagr_value = calculate_cagr(data)
                    growth_chart = plot_investment_growth(data, principal_amount)

                    # --- Display Results ---
                    st.metric("5-Year Compound Annual Growth Rate (CAGR)", f"{cagr_value:.2f}%")
                    st.pyplot(growth_chart)

                    with st.expander("View Raw Historical Data"):
                        st.dataframe(data)
                else:
                    st.error("Could not find data for this ticker. Please check the symbol and try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}. Please check your internet connection.")
        else:
            st.warning("Please enter a stock ticker to analyze.")


# ==============================================================================
# --- PAGE 3: FUTURE PRICE FORECASTER ---
# ==============================================================================
else:
    st.header('Future Price Forecaster')

    # --- User Input for Forecasting ---
    ticker_input = st.text_input("Enter Stock Ticker to Forecast (e.g., INFY.NS for NSE)")

    # --- Forecasting Logic ---
    if st.button('Generate Forecast'):
        if ticker_input:  # Check if the user has entered a ticker
            try:
                # Attempt to fetch data first
                data = fetch_historical_data(ticker_input)

                if not data.empty:
                    # If data is found, generate the forecast
                    model, forecast = generate_forecast(data)
                    st.success(f"1-Year forecast for {ticker_input} generated successfully.")

                    # --- Display Forecast Plot ---
                    forecast_chart = model.plot(forecast)
                    st.pyplot(forecast_chart)

                    # --- CRITICAL DISCLAIMER ---
                    st.warning(
                        "**Disclaimer:** This is a statistical forecast based on historical data and should **not** be considered financial advice. "
                        "Past performance is not indicative of future results."
                    )

                    with st.expander("View Forecast Data"):
                        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
                else:
                    st.error("Could not find data for this ticker. Please check the symbol and try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}. Please check your internet connection.")
        else:
            st.warning("Please enter a stock ticker to forecast.")