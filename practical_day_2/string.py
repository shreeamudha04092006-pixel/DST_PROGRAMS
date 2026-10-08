n = 5

# Right Triangle
print("Right Triangle")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Pyramid
print("\nPyramid")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Number Triangle
print("\nNumber Triangle")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Multiplication Grid
print("\nMultiplication Grid")

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j, end="    ")
    print()