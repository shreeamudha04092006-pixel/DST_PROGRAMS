def top_k_frequent(nums, k):

    freq = {}

    for num in nums:

        if num in freq:
            freq[num] = freq[num] + 1

        else:
            freq[num] = 1

    result = sorted(freq, key=freq.get, reverse=True)

    return result[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print("Top", k, "frequent values:", top_k_frequent(nums, k))