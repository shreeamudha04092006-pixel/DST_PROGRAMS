celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print(f"Kelvin: {kelvin:.2f} K")

print("\nConversion Table")
print("Celsius   Fahrenheit   Kelvin")

for c in range(-40, 101, 10):
    f = (c * 9 / 5) + 32
    k = c + 273.15
    print(f"{c:7.2f} {f:12.2f} {k:10.2f}")