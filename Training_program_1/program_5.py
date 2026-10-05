age = int(input("Enter age: "))

voting = "Eligible" if age >= 18 else "Not Eligible"
discount = "Eligible" if age >= 60 else "Not Eligible"

print("Voting:", voting)
print("Senior Citizen Discount:", discount)