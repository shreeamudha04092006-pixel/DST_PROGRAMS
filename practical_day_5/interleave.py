a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

result = []

for i in range(len(a)):
    result.append(a[i])
    result.append(b[i])

print("Interleaved list:", result)