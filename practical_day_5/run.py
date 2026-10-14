values = [4, 4, 4, 2, 2, 7, 7, 4, 4, 9]

result = []
count = 1

for i in range(1, len(values)):
    if values[i] == values[i - 1]:
        count += 1
    else:
        result.append((values[i - 1], count))
        count = 1

result.append((values[-1], count))

print("Compressed list:", result)