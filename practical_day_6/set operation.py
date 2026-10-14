A = {101, 102, 103, 105}
B = {102, 104, 105, 106}

both = A & B
only_A = A - B
either = A | B

print("Both courses:", sorted(both))
print("Only Course A:", sorted(only_A))
print("Either course:", sorted(either))