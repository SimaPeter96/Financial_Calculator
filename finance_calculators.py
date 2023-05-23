import math

print("Select an option from\n1.Investment \n2.Bond")

# Input from user starts conditional statements

inv_bond = input("Enter either Investment or Bond: ").lower()

if inv_bond == "investment":
    pr = float(input("Enter principal amount for investment: "))
    rate = float(input("Enter amount of interest rate: "))
    r = (rate / 100) / 12
    time = float(input("Enter duration for investment in years: "))
    simple_compound = input("Select either 'Simple' or 'Compound' interest: ").lower()

    if simple_compound == "simple":
        simple_compound = pr * (1 + r * time)
        total = simple_compound
        print(f"Interest earned over {time} years: {total:.2f}")
    elif simple_compound == "compound":
        simple_compound = pr * math.pow((1 + r), time)
        total = simple_compound
        print(f"Interest earned over {time} years: {total:.2f}")
    else:
        print("Invalid input.")

elif inv_bond == "bond":
    pri = float(input("Enter the current value of the house: "))
    intr = float(input("Enter the interest rate: "))
    i = ((intr / 100) / 12) / 12
    no = float(input("Enter the duration in months: "))
    monthly = (i * pri) / (1 - (1 + i) ** -no)
    print(f"Monthly repayment: {monthly:.2f}")
else:
    print("Invalid input.")
