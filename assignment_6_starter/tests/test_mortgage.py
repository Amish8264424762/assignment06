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

    def test_mutator_negative_loan_amount(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(-100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)

    def test_mutator_zero_loan_amount(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(0, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)

    def test_mutator_positive_loan_amount(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        mortgage.loan_amount = 150000
        self.assertEqual(mortgage.loan_amount, 150000)

    def test_mutator_valid_rate(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        mortgage.rate = MortgageRate.VARIABLE_1
        self.assertEqual(mortgage.rate, MortgageRate.VARIABLE_1)

    def test_mutator_invalid_rate(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
            mortgage.rate = 0.05

    def test_mutator_valid_frequency(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        mortgage.frequency = PaymentFrequency.BI_WEEKLY
        self.assertEqual(mortgage.frequency, PaymentFrequency.BI_WEEKLY)

    def test_mutator_invalid_frequency(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
            mortgage.frequency = "WEEKLY"

    def test_mutator_valid_amortization(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        mortgage.amortization = 15
        self.assertEqual(mortgage.amortization, 15)

    def test_mutator_invalid_amortization(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
            mortgage.amortization = 35



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

        # Additional checks using accessors
        self.assertEqual(mortgage.get_loan_amount(), 100000)
        self.assertEqual(mortgage.get_rate(), MortgageRate.FIXED_5)
        self.assertEqual(mortgage.get_frequency(), PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.get_amortization(), 30)

    def calculate_payment(self) -> float:
        # Mortgage formula
        n = self.amortization * self.frequency
        r = self.rate.value / self.frequency / 100  
        pv = self.loan_amount
        payment = pv * r / (1 - (1 + r) ** -n)
        return round(payment, 2)

    def test_calculate_payment(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        # Manually calculated expected payment based on the given example
        expected_payment = 4046.23
        self.assertAlmostEqual(mortgage.calculate_payment(), expected_payment, places=2)

    def test_str_representation(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        expected_str = (
            "Mortgage Amount: $682,912.43\n"
            "Rate: 5.89%\n"
            "Amortization: 30\n"
            "Frequency: Monthly -- Calculated Payment: $4,046.23"
        )
        self.assertEqual(str(mortgage), expected_str)

    def test_repr_representation(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        expected_repr = "[682912.43, 0.0589, 30, 12]"
        self.assertEqual(repr(mortgage), expected_repr)
 







