def find_max_length(nums):

    balance = 0
    result = 0

    seen = {0: -1}

    for i in range(len(nums)):

        if nums[i] == 0:
            balance = balance - 1

        else:
            balance = balance + 1

        if balance in seen:

            length = i - seen[balance]

            if length > result:
                result = length

        else:
            seen[balance] = i

    return result


nums = [0, 1, 0]

print("Maximum balanced subarray length:",
      find_max_length(nums))