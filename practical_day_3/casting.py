try:
    integer_input = input("Integer: ")
    decimal_input = input("Decimal: ")

    num1 = int(integer_input)
    num2 = float(decimal_input)

    print("Integer Value :", num1)
    print("Integer Type :", type(num1).__name__)

    print("Float Value :", num2)
    print("Float Type :", type(num2).__name__)

    print("Rounded Value :", round(num2))

    print(f"{num1} / {int(num2)} = {num1 / int(num2):.4f}")
    print(f"{num1} // {int(num2)} =", num1 // int(num2))
    print(f"{num1} % {int(num2)} =", num1 % int(num2))
    print(f"{num1} ** 2 =", num1 ** 2)

except ValueError:
    print("Invalid numeric input")
except ZeroDivisionError:
    print("Cannot divide by zero")