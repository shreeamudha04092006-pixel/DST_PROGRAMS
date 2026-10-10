while True:
    print("1. Celsius to Fahrenheit")
    print("2. Kilometres to Miles")
    print("3. Kilograms to Pounds")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        c = float(input("Enter Celsius: "))
        f = (c * 9 / 5) + 32
        print("Fahrenheit:", f)

    elif choice == 2:
        km = float(input("Enter kilometres: "))
        miles = km * 0.621371
        print("Kilometres to Miles:", round(miles, 2))

    elif choice == 3:
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print("Kilograms to Pounds:", round(pounds, 2))

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")
        continue