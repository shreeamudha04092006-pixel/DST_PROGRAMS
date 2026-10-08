deliveries = 3
distances = [3, 8, 12]

total_distance = 0
total_earnings = 0

for distance in distances:

    total_distance = total_distance + distance

    if distance <= 5:
        earning = 40
    else:
        earning = 40 + (distance - 5) * 8

    total_earnings = total_earnings + earning

average_distance = total_distance / deliveries

print(f"Total Distance   : {total_distance:.2f} km")
print(f"Total Earnings   : ₹{total_earnings:.2f}")
print(f"Average Distance : {average_distance:.2f} km")