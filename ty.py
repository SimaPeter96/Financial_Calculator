import math

def investment_calculator():
    print("Investment Calculator")
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate (in percentage): "))
    years = int(input("Enter the number of years: "))
    interest_type = input("Enter the interest type (simple/compound): ").lower()

    if interest_type == "simple":
        interest = principal * (1 + (interest_rate / 100) * years)
    elif interest_type == "compound":
        interest = principal * math.pow(1 + (interest_rate / 100), years)
    else:
        print("Invalid interest type.")
        return

    total_amount = principal + interest
    print(f"Total amount after {years} years: {total_amount:.2f}")


def home_loan_calculator():
    print("Home Loan Repayment Calculator")
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the interest rate (in percentage): "))
    loan_term = int(input("Enter the loan term (in months): "))

    monthly_interest_rate = (interest_rate / 100) / 12 
    monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -loan_term))

    print(f"Monthly repayment amount: {monthly_repayment:.2f}")


def finance_calculator():
    print("Welcome to the Finance Calculator!")
    print("Select an option:")
    print("1. Investment Calculator")
    print("2. Home Loan Repayment Calculator")

    option = input("Enter your choice (1/2): ")

    if option == "1":
        investment_calculator()
    elif option == "2":
        home_loan_calculator()
    else:
        print("Invalid option.")


finance_calculator()
