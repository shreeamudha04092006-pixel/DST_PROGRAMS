def average_readings(*args):

    if len(args) == 0:
        return None

    total = 0

    for i in args:
        total = total + i

    average = total / len(args)

    return average


print("Average:", average_readings(10, 20, 30, 40))

if average_readings() == None:
    print("No readings provided")