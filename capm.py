import pandas as pd
import numpy as np

def CalcExpectedReturn(rf, beta, market_return):
    """ 
    Calculate expected return using CAPM formula.
    
    Parameters:
        rf (float): Risk-free rate
        beta (float): Stock's beta
        market_return (float): Market return
        
    Returns:
        float: Expected return based on CAPM formula.
    """
    return rf + beta * (market_return - rf)

def Normalize(df):
    """
    Normalize stock data based on the initial price.
    
    Parameters: 
        df (DataFrame): Containing 'Date' and 'Price' columns
    
    Returns:
        DataFrame with normalized stock prices
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    initial_price = df['Price'].iloc[0]
    df['Normalized Price'] = df['Price'] / initial_price
    return df

def CalcMonthlyReturn(df):
    """
    Calculate monthly returns.
    
    Parameters:
        df: DataFrame containing 'Price' data
        
    Returns:
        DataFrame with monthly returns added
    """
    df = df.sort_values('Date')
    df['Monthly Return'] = df['Price'].pct_change().fillna(0)
    return df

def CalcBeta(stock_returns, market_returns):
    """
    Calculate beta between stock and market returns.
    
    Parameters:
        stock_returns: Monthly return of the stock
        market_returns: Monthly return of market index
        
    Returns:
        float: Calculated beta of the stock relative to the market
    """
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    market_variance = np.var(market_returns)
    
    beta = covariance / market_variance
    return beta
