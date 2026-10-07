value = input("Enter a value: ")

print("Original value type :", type(value).__name__)

try:
    integer_value = int(value)
    print("Integer value       :", integer_value)
    print("Integer type        :", type(integer_value).__name__)
except ValueError:
    print("Invalid integer conversion")

try:
    float_value = float(value)
    print("Float value         :", float_value)
    print("Float type          :", type(float_value).__name__)
except ValueError:
    print("Invalid float conversion")