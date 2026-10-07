items = []
subtotal = 0

while True:
    value = input("Enter item price or done: ")

    if value.lower() == "done":
        break

    price = float(value)
    items.append(price)
    subtotal += price

if subtotal >= 500:
    discount_rate = 10
elif subtotal >= 300:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100
amount = subtotal - discount

tax = amount * 5 / 100
final_amount = amount + tax

print("\nItem         Price")
print("-----------------")

for i, price in enumerate(items, 1):
    print(f"Item {i:<5} {price:8.2f}")

print("-----------------")
print(f"Subtotal      {subtotal:8.2f}")
print(f"Discount      {discount:8.2f}")
print(f"Tax           {tax:8.2f}")
print(f"Final         {final_amount:8.2f}")