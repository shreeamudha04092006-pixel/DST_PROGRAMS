
n = int(input("Enter count: "))
nums = list(map(int, input("Enter numbers: ").split()))

positive = negative = zero = 0
even = odd = 0
both = only3 = only5 = neither = 0

for num in nums:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    if num != 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    if num != 0:
        if num % 3 == 0 and num % 5 == 0:
            both += 1
        elif num % 3 == 0:
            only3 += 1
        elif num % 5 == 0:
            only5 += 1
        else:
            neither += 1
    else:
        neither += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)
print("Divisible by both 3 and 5:", both)
print("Divisible only by 3:", only3)
print("Divisible only by 5:", only5)
print("Divisible by neither:", neither)
