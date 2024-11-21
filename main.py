from exclparse import process_sheets, excel_file, sheet_names
from capm import CalcExpectedReturn, Normalize, CalcMonthlyReturn, CalcBeta
from plotter import plot_normalized_prices
from capmTest import run_tests
import pandas as pd

# Added to avoid unnecessary terminal clutter
pd.set_option('future.no_silent_downcasting', True)

def main():
    # Call the process_sheets function from exclparse.py to get data from Excel
    sheet_data = process_sheets(sheet_names, excel_file)
    
    """
    10 Year Treasury Rate Gov T-bills = 4.08%
        - https://ycharts.com/indicators/10_year_treasury_rate#:~:text=Basic%20Info,long%20term%20average%20of%204.25%25.
    10 year S&P 500 market return = 13.05%
        - https://www.investopedia.com/ask/answers/042415/what-average-annual-return-sp-500.asp
    """
    # Input values for CAPM
    Rf = 0.0408  # Risk-free rate Gov T-bills US
    market_return = 0.01305  # Market return (8%) avg returns sp500
    
    # Extract S&P 500 market data for comparison
    sp500_data = sheet_data['Price History SP50']
    market_df = pd.DataFrame({
        'Date': pd.to_datetime(sp500_data['Date'], errors='coerce'),
        'Price': pd.to_numeric(sp500_data['Price'], errors='coerce')
    })
    
    # Remove any rows with NaN values
    market_df = market_df.dropna()
    
    # Sort market data by date in ascending order
    market_df = market_df.sort_values('Date')
    
    # Normalize and calculate monthly returns for the market
    market_df = Normalize(market_df)
    market_df = CalcMonthlyReturn(market_df)

    # Prepare for comparison
    results = []

    # Loop through stock sheets (including SP50)
    for sheet, stock_data in sheet_data.items():
        # Create a DataFrame for the stock data
        df = pd.DataFrame({
            'Stock Name': [stock_data['Stock Name']] * len(stock_data['Date']),
            'Date': pd.to_datetime(stock_data['Date'], errors='coerce'),
            'Price': pd.to_numeric(stock_data['Price'], errors='coerce')
        })
        
        # Remove any rows with NaN values
        df = df.dropna()
        
        # Sort the dataframe by date in ascending order
        df = df.sort_values('Date')
        
        # Normalize the price
        df = Normalize(df)
        
        # Calculate monthly returns for the stock
        df = CalcMonthlyReturn(df)
        
        # Merge the stock data and market data on the 'Date' column
        merged_df = pd.merge(df, market_df, on='Date', how='inner', suffixes=('_stock', '_market'))
        
        # Calculate beta between stock and market returns
        beta = CalcBeta(merged_df['Monthly Return_stock'], merged_df['Monthly Return_market'])
        
        # Calculate expected return using the CAPM formula
        expected_return = CalcExpectedReturn(Rf, beta, market_return)
        
        # Store results for comparison at the end
        results.append({
            'Stock Name': stock_data['Stock Name'],
            'Expected Return': expected_return,
            'Beta': beta
        })
        
        # Print stock details
        print(f"\n{'='*40}")
        print(f"Sheet: {stock_data['Stock Name']}")
        print(f"Expected Return (CAPM): {expected_return:.2f}")
        print(f"Beta: {beta:.2f}")
        
        # Print the first 10 rows of the DataFrame
        print(merged_df[['Stock Name', 'Date', 'Price_stock', 'Normalized Price_stock', 'Monthly Return_stock']].head(10).to_string(index=False))
        
        # Call plot function for normalized prices
        plot_normalized_prices(df, stock_data['Stock Name'])
        print(f"{'='*40}\n")

    # Print comparison with S&P 500 after all computations
    print("\nComparison with S&P 500:")
    for result in results:
        print(f"Stock: {result['Stock Name']}, Expected Return: {result['Expected Return']:.5f}, Beta: {result['Beta']:.2f}")

    # End of program outputs
    print("\nEnd of program computations.\n")

test_result = run_tests()

# Check the test results
if test_result.wasSuccessful():
    print("Tests: Passed")
else:
    print(f"Tests: Failed ({len(test_result.failures)} failures)")

if __name__ == '__main__':
    main()
