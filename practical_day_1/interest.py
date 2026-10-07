principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

if principal < 0 or time < 0:
    print("Principal and time must be non-negative.")
else:
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"Principal      : {principal:.2f}")
    print(f"Rate           : {rate:.2f}%")
    print(f"Time           : {time:.2f} years")
    print(f"Simple Interest: {simple_interest:.2f}")
    print(f"Total Amount   : {total_amount:.2f}")