def find_min(nums):

    small = nums[0]

    for i in nums:
        if i < small:
            small = i

    return small


nums = [10, 25, 5, 40, 15]

print("Minimum number:", find_min(nums))