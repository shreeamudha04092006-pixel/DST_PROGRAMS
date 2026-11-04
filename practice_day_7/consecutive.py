def longest_consecutive(nums):

    numbers = set(nums)

    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            count = 1

            while num + count in numbers:
                count = count + 1

            if count > longest:
                longest = count

    return longest


nums = [100, 4, 200, 1, 3, 2]

print("Longest consecutive sequence length:",
      longest_consecutive(nums))