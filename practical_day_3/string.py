s = input()

i = 0

# Remove leading spaces
while i < len(s) and s[i] == " ":
    i += 1

# Sign
sign = 1

if i < len(s) and s[i] == '-':
    sign = -1
    i += 1

elif i < len(s) and s[i] == '+':
    i += 1

# Convert digits
result = 0

while i < len(s) and '0' <= s[i] <= '9':
    result = result * 10 + (ord(s[i]) - ord('0'))
    i += 1

print(sign * result)