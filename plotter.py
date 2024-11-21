import matplotlib.pyplot as plt
import pandas as pd

def plot_normalized_prices(stock_data, stock_name):
    """
    parameters:
        - stock_data (DataFrame): DataFrame containing 'Date' and 'Normalized Price'.
        - stock_name (str): Name of the stock to be displayed on the plot.
    outputs:
        - a graph with normalized monthly prices for each stock in the portfolio. 
    """
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    plt.figure(figsize=(10, 6))

    # Plot the normalized prices (ensure you use the correct column name)
    plt.plot(stock_data['Date'], stock_data['Normalized Price'], label=stock_name)

    # Add labels and title
    plt.title(f"Normalized Stock Price for {stock_name}")
    plt.xlabel('Date')
    plt.ylabel('Normalized Price')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display legend
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()
    