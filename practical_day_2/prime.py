n = 10
number = 12345

# Prime numbers
print("Primes:", end=" ")

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i, end=" ")

# Factorial
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("\nFactorial:", factorial)

# Fibonacci
a = 0
b = 1

print("Fibonacci:", end=" ")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Digit Sum
temp = number
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum = digit_sum + digit
    temp = temp // 10

print("\nDigit Sum:", digit_sum)

# Reverse
temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse:", reverse)