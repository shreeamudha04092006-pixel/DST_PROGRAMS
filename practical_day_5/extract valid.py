readings = [8, 10, 20, 35, 51, 40]

result = [
    round(c * 9/5 + 32, 1)
    for c in readings
    if 10 <= c <= 50
]

print("Converted readings:", result)