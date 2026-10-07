
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

average = (a + b + c) / 3

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)

n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    if n % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")
