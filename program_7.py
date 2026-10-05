n = int(input("Enter N: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

average = total / n

print("Sum:", total)
print("Average:", average)