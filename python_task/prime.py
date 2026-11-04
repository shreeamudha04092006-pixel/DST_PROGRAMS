def find_prime(nums):

    for num in nums:

        if num > 1:

            count = 0

            for i in range(2, num):

                if num % i == 0:
                    count = count + 1

            if count == 0:
                print(num)


nums = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter number: "))
    nums.append(value)

print("Prime numbers:")

find_prime(nums)