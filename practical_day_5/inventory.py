products = [
    ("Sensor", 4, 150.0),
    ("Cable", 12, 25.0),
    ("Board", 3, 800.0)
]

total = 0
low_stock = []

for name, quantity, price in products:
    value = quantity * price
    print(f"{name}: Value = {value:.2f}")

    total += value

    if quantity < 5:
        low_stock.append(name)

print("Low-stock products:", low_stock)
print(f"Total inventory value: {total:.2f}")