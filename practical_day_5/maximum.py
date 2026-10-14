matrix = [
    [1, 3, 1],
    [2, 5, 2],
    [4, 2, 1]
]

rows = len(matrix)
cols = len(matrix[0])

dp = [[0] * cols for _ in range(rows)]

dp[0][0] = matrix[0][0]

for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            continue

        top = dp[i - 1][j] if i > 0 else -1
        left = dp[i][j - 1] if j > 0 else -1

        dp[i][j] = matrix[i][j] + max(top, left)

path = []
i = rows - 1
j = cols - 1

while i > 0 or j > 0:
    path.append(matrix[i][j])

    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

path.append(matrix[0][0])
path.reverse()

print("Maximum path sum:", dp[-1][-1])
print("Path:", path)