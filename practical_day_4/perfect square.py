
L, R = map(int, input("Enter L and R: ").split())

found = False

for num in range(max(0, L), R + 1):
    i = 0

    while i * i < num:
        i += 1

    if i * i == num:
        print("First perfect square:", num)
        found = True
        break

if not found:
    print("No perfect square found")
