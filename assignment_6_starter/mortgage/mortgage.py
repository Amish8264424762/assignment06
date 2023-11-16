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
        



