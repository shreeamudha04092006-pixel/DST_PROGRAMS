a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

if len(a[0]) != len(b):
    print("Error: Incompatible dimensions")
else:
    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            total = 0

            for k in range(len(b)):
                total += a[i][k] * b[k][j]

            row.append(total)

        result.append(row)

    print("Product matrix:")
    for row in result:
        print(row)