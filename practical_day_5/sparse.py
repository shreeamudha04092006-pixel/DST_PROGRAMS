matrix = [
    [0, 0, 5, 0],
    [0, 8, 0, 0],
    [3, 0, 0, 6]
]

result = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            result.append((i, j, matrix[i][j]))

print(result)