def calculate_fd_return(principal, rate, years):
    """
    Calculates the final return on a Fixed Deposit with annual compounding.

    Args:
        principal (float): The initial investment amount.
        rate (float): The annual interest rate as a percentage (e.g., 6.5).
        years (int): The number of years for the investment.

    Returns:
        float: The total maturity amount after the specified years.
    """
    # Convert the percentage rate to a decimal
    rate_decimal = rate / 100

    # Apply the compound interest formula: A = P(1 + r)^t
    final_amount = principal * (1 + rate_decimal) ** years

    return final_amount


