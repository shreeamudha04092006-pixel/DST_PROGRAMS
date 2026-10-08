start = int(input("Start: "))
end = int(input("End: "))

print("Number Prime Perfect Armstrong Palindrome Digit Sum Digits Binary")

for num in range(start, end + 1):

    # Prime
    if num < 2:
        prime = False
    else:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

    # Perfect
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    perfect = (num > 0 and divisor_sum == num)

    # Digit information
    temp = num
    digits = []

    if temp == 0:
        digits = [0]
    else:
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10

    digit_sum = sum(digits)
    digit_count = len(digits)

    # Armstrong
    armstrong_sum = 0
    for digit in digits:
        armstrong_sum += digit ** digit_count

    armstrong = (armstrong_sum == num)

    # Palindrome
    original = str(num)
    palindrome = (original == original[::-1])

    # Binary without bin()
    if num == 0:
        binary = "0"
    else:
        n = num
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2

    print(
        num,
        "Yes" if prime else "No",
        "Yes" if perfect else "No",
        "Yes" if armstrong else "No",
        "Yes" if palindrome else "No",
        digit_sum,
        digit_count,
        binary
    )