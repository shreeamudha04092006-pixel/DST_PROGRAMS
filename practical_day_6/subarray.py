nums = [1, 1, 1]
k = 2

prefix_sum = 0
count = 0

freq = {0: 1}

for num in nums:
    prefix_sum += num

    required = prefix_sum - k

    if required in freq:
        count += freq[required]

    if prefix_sum in freq:
        freq[prefix_sum] += 1
    else:
        freq[prefix_sum] = 1

print("Count:", count)