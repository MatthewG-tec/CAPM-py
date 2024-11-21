import unittest
import pandas as pd
from capm import CalcExpectedReturn, Normalize, CalcMonthlyReturn, CalcBeta

class TestCapmFunctions(unittest.TestCase):
    def setUp(self):
        self.rf = 0.03
        self.beta = 1.2
        self.market_return = 0.08
        
        # Create the DataFrame
        data = {
            'Date': pd.date_range(start='2023-01-01', periods=5, freq='M'),
            'Price': [100, 105, 102, 108, 110]
        }
        self.df = pd.DataFrame(data)
        
        # Calculate expected monthly returns for testing CalcBeta
        self.stock_returns = self.df['Price'].pct_change().dropna().values
        self.market_returns = [0.04, 0.03, 0.05, 0.02]
        self.market_returns = self.market_returns[:len(self.stock_returns)]
        
        """ Test CAPM expected return calculation """
    def test_calc_expected_return(self):
        expected_return = CalcExpectedReturn(self.rf, self.beta, self.market_return)
        self.assertAlmostEqual(expected_return, 0.086, places=2)
        
        """ Test CAPM with zero beta (expected return = risk-free rate) """
    def test_calc_expected_return_zero_beta(self):
        expected_return = CalcExpectedReturn(self.rf, 0, self.market_return)
        self.assertAlmostEqual(expected_return, self.rf)
        
        """ Test CAPM when market return equals risk-free rate (expected return = risk-free rate) """
    def test_calc_expected_return_zero_market_return(self):
        expected_return = CalcExpectedReturn(self.rf, self.beta, self.rf)
        self.assertAlmostEqual(expected_return, self.rf)
        
        """ Test normalization of stock prices """
    def test_normalize(self):
        normalized_df = Normalize(self.df.copy())
        self.assertTrue('Normalized Price' in normalized_df.columns)
        self.assertAlmostEqual(normalized_df['Normalized Price'].iloc[0], 1.0)

        """ Test monthly return calculation """
    def test_calc_monthly_return(self):
        monthly_return_df = CalcMonthlyReturn(self.df.copy())
        self.assertTrue('Monthly Return' in monthly_return_df.columns)
        self.assertAlmostEqual(monthly_return_df['Monthly Return'].iloc[1], 0.05)

        """ Test beta calculation between stock and market returns """
    def test_calc_beta(self):
        beta = CalcBeta(self.stock_returns, self.market_returns)
        self.assertIsInstance(beta, float)

        """ Test CalcBeta with constant stock prices (beta should be zero) """
    def test_calc_beta_zero_variation(self):
        constant_returns = [0.0, 0.0, 0.0, 0.0]
        beta = CalcBeta(constant_returns, self.market_returns)
        self.assertAlmostEqual(beta, 0.0)

def run_tests():
    """ Run the tests and return results """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCapmFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result
