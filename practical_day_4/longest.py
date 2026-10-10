
n = int(input("Enter count: "))
nums = list(map(int, input("Enter numbers: ").split()))

if n <= 0 or len(nums) != n:
    print("Invalid input")
else:
    current_value = nums[0]
    current_count = 1

    best_value = nums[0]
    best_count = 1

    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            current_count += 1
        else:
            current_value = nums[i]
            current_count = 1

        if current_count > best_count:
            best_count = current_count
            best_value = current_value

    print("Value =", best_value)
    print("Length =", best_count)
