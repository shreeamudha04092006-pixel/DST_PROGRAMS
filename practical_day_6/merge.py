store_a = {'LED': 20, 'Cable': 10, 'Board': 3}
store_b = {'Cable': 5, 'Sensor': 7, 'LED': 8}

result = store_a.copy()

for item, quantity in store_b.items():
    if item in result:
        result[item] += quantity
    else:
        result[item] = quantity

print("Combined inventory:", result)