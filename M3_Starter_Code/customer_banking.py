# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the initial savings account balance: "))
    savings_interest = float(input("Enter the annual interest rate for savings (as %): "))
    savings_maturity = int(input("Enter the number of months for savings account interest calculation: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nSavings Account:")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Balance: ${updated_savings_balance:.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the initial CD account balance: "))
    cd_interest = float(input("Enter the annual interest rate for CD (as %): "))
    cd_maturity = int(input("Enter the number of months for CD account interest calculation: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nCD Account:")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
