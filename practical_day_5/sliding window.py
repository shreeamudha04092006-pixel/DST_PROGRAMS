sales = [10, 20, 30, 40, 50, 60]
k = 3

result = []

for i in range(len(sales) - k + 1):
    window = sales[i:i + k]
    avg = sum(window) / k
    result.append(round(avg, 2))

print("Window averages:", result)