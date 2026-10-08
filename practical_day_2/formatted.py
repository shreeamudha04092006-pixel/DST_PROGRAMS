customer = "Aarthi"
units = 250

if units <= 100:
    amount = units * 2

elif units <= 200:
    amount = (100 * 2) + ((units - 100) * 4)

else:
    amount = (100 * 2) + (100 * 4) + ((units - 200) * 7)

print("Customer :", customer)
print("Units    :", units)
print(f"Amount   : ₹{amount:.2f}")