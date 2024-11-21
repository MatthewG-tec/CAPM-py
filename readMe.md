By: Matthew Gillett - matthew.gillett@uleth.ca
Id: 001230643

Capital Asset Pricing Model Stock Expected Return:

Structure:
    1. main.py
        - loads stock price data from excel file, through exclparse.py.
        - normalizes stock prices and calculates monthly return.
        - calculates expected return using CAPM.
        - runs unit tests from capmTest.py automatically each compile. 
    2. capm.py
        - contains the core fianancial functions:
            - CalcExpectedReturn, Normalize, CalcMonthlyReturn, and CalcBeta.
    3. exclparse.py
        - handles loading and parsing stock price data from excel file.
        - processes all sheets and prices with corresponding dates. 
    4. plotter.py
        - provides functionality to plot the normalized stock prices through the historical 
        prices.
    5. capmTest.py
        - contains unit tests to verify the correctness of the financial functions in capm.py
Required Libraries:
    - Numpy, matplotlib, unittest
    - Can use "pip install numpy matplotlib plotter
Compiling:
    - Once Libraries are installed and python
    - python main.py (runs the whole program)
Data:
    - Pulled from the FactSet data base.
    - Access through dhillon school of business student account.

** If you want to run on IDE I used https://www.spyder-ide.org/ comes standard with all financial libraries