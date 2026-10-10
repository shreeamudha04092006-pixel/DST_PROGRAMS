normal = 0
large = 0
suspicious = 0
total = 0

while True:
    amount = int(input("Enter amount: "))

    if amount == -1:
        break

    if amount == 0:
        pass
    elif amount < 0:
        continue
    elif amount <= 1000:
        normal += 1
        total += amount
    elif amount <= 5000:
        large += 1
        total += amount
    else:
        suspicious += 1

    if suspicious == 3:
        break

print("Normal transactions:", normal)
print("Large transactions:", large)
print("Suspicious transactions:", suspicious)
print("Total valid amount:", total)