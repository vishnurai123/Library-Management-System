import unittest
from datetime import date, timedelta

class TestLoanRules(unittest.TestCase):
    def test_loan_period(self):
        from config import LOAN_DAYS
        self.assertEqual((date.today() + timedelta(days=LOAN_DAYS) - date.today()).days, LOAN_DAYS)

if __name__ == "__main__":
    unittest.main()
