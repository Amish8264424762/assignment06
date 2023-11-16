"""
Description: A class used to test the Mortgage class.
Author: Amish
Date: 10-11-2023
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""


from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    def test_invalid_loan_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(0, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 5.0, PaymentFrequency.MONTHLY, 30)

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, MortgageRate.FIXED_5, "MONTHLY", 30)

    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 40)

    def test_valid_inputs(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        self.assertEqual(mortgage.loan_amount, 100000)
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.amortization, 30)

