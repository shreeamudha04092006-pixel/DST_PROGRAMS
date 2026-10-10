n = int(input("Enter a number: "))
skipped = 0

for i in range(1, 21):
    result = n * i

    if result > 100:
        break

    if result % 3 == 0:
        skipped += 1
        continue

    print(n, "x", i, "=", result)

print("Skipped results:", skipped)