matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = []

for i in range(len(matrix)):
    if i % 2 == 0:
        result.extend(matrix[i])
    else:
        result.extend(matrix[i][::-1])

print("Zigzag list:", result)