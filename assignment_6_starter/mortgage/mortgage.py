"""
Description: A class meant to manage Mortgage options.
Author: Amish
Date: 10-11-2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

# mortgage.py

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount, rate, frequency, amortization):
        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.loan_amount = loan_amount

        # Validate Rate
        if not isinstance(rate, MortgageRate):
            raise ValueError("Invalid Rate provided.")
        self.rate = rate

        # Validate Frequency
        if not isinstance(frequency, PaymentFrequency):
            raise ValueError("Invalid Frequency provided.")
        self.frequency = frequency

        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Invalid Amortization provided.")
        self.amortization = amortization

        # Accessor and Mutator for Loan Amount
        @property
        def loan_amount(self):
            return self._loan_amount

        @loan_amount.setter
        def loan_amount(self, value):
            if value <= 0:
                raise ValueError("Loan Amount must be positive.")
            self._loan_amount = value

         # Accessor and Mutator for Rate
        @property
        def rate(self):
            return self._rate

        @rate.setter
        def rate(self, value):
            if not isinstance(value, MortgageRate):
                raise ValueError("Invalid Rate provided.")
            self._rate = value

         # Accessor and Mutator for Frequency
        @property
        def frequency(self):
            return self._frequency

        @frequency.setter
        def frequency(self, value):
            if not isinstance(value, PaymentFrequency):
                raise ValueError("Invalid Frequency provided.")
            self._frequency = value

         # Accessor and Mutator for Amortization
        @property
        def amortization(self):
            return self._amortization

        @amortization.setter
        def amortization(self, value):
            if value not in VALID_AMORTIZATION:
                raise ValueError("Invalid Amortization provided.")
            self._amortization = value


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









