x = 123

negative = False

if x < 0:
    negative = True
    x = -x

reverse = 0

while x > 0:
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10

if negative:
    reverse = -reverse

print(reverse)