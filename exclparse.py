import pandas as pd

# Load the Excel file
excel_file = 'PriceHistoryCapm.xlsx'  # Store the Excel file path here

# Load all sheet names from the Excel file
xls = pd.ExcelFile(excel_file)
sheet_names = xls.sheet_names
"""
funtion: get_stock_name
    - extracts stock name from sheet name
"""
def get_stock_name(sheet_name):
    if "Price History" in sheet_name:
        return sheet_name.split("Price History")[-1].strip()
    return "Unknown"

"""
function: get_date_and_price
        - extracts dates and prices from excel cells A3 (Date) and B3 (Price)
"""
def get_date_and_price(sheet_df):
    dates = sheet_df.iloc[2:, 0]  # Column A (0th index) for 'Date'
    prices = sheet_df.iloc[2:, 1]  # Column B (1st index) for 'Price'
    return dates, prices

"""
function: process_sheets
    - process all shees in excel and return the data.
"""
def process_sheets(sheet_names, excel_file):
    data = {}
    
    for sheet in sheet_names:
        # Load the sheet into a DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet)
        
        # Get stock name, dates, and prices
        stock_name = get_stock_name(sheet)
        dates, prices = get_date_and_price(df)
        
        # Store the extracted data
        data[sheet] = {
            'Stock Name': stock_name,
            'Date': dates,
            'Price': prices
        }
    
    return data
