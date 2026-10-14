stock = {'LED': 20, 'RESISTOR': 50, 'SENSOR': 4}
requested = ['LED', 'SENSOR', 'SWITCH']

for item in requested:
    quantity = stock.get(item)

    if quantity is not None:
        print(item + ":", quantity, "available")
    else:
        print(item + ": unavailable")