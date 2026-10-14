names = ['Anu', 'Arun', 'Bala', 'Banu', 'Cathy', 'Asha']

result = {}

for name in names:
    first_letter = name[0].upper()

    if first_letter not in result:
        result[first_letter] = []

    result[first_letter].append(name)

print(result)