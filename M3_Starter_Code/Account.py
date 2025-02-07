""" Create an Account class with methods"""

class Account:
    """Creating an Account class with methods"""

    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    # This method sets the interest rate of the account.
    def set_interest(self, interest):
        """Sets the interest rate for the account"""
        self.interest = interest

    # This method calculates the interest earned over a given number of months.
    def calculate_interest(self, months):
        """Calculates the interest earned over a given number of months"""
        return self.balance * (self.interest / 100) * (months / 12)
