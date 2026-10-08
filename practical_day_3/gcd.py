num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Decimal to Binary
n = num1
binary = ""

if n == 0:
    binary = "0"
else:
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

# Decimal to Octal
n = num1
octal = ""

if n == 0:
    octal = "0"
else:
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n //= 8

# Decimal to Hexadecimal
n = num1
hexadecimal = ""
digits = "0123456789ABCDEF"

if n == 0:
    hexadecimal = "0"
else:
    while n > 0:
        remainder = n % 16
        hexadecimal = digits[remainder] + hexadecimal
        n //= 16

# GCD
a = num1
b = num2

while b != 0:
    a, b = b, a % b

gcd = a

# LCM
lcm = (num1 * num2) // gcd

print("Binary       :", binary)
print("Octal        :", octal)
print("Hexadecimal  :", hexadecimal)
print("GCD          :", gcd)
print("LCM          :", lcm)