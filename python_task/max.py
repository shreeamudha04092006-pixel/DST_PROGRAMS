def find_max(nums):

    large = nums[0]

    for i in nums:
        if i > large:
            large = i

    return large


nums = [10, 25, 5, 40, 15]

print("Largest number:", find_max(nums))