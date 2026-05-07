

print("Interest Calculator")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))


interest = (principal * rate * time) / 100
total = principal + interest

print("\nSimple Interest:", interest)
print("Total Amount:", total)