def second_largest(nums):

    large = nums[0]
    second = None

    for i in nums:

        if i > large:
            second = large
            large = i

        elif i != large:

            if second == None or i > second:
                second = i

    return second


nums = [10, 25, 5, 40, 15]

print("Second largest:", second_largest(nums))