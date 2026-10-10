invalid = 0

while True:
    num = int(input("Enter a number: "))

    if num < 1 or num > 100:
        print("Invalid input")
        invalid += 1
        continue

    print("Accepted value:", num)
    break

print("Invalid attempts:", invalid)