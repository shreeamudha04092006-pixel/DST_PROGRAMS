s = 'ADOBECODEBANC'
t = 'ABC'

need = {}

for char in t:
    if char in need:
        need[char] += 1
    else:
        need[char] = 1

window = {}

left = 0
right = 0

formed = 0
required = len(need)

min_length = float('inf')
min_left = 0

while right < len(s):

    char = s[right]

    if char in window:
        window[char] += 1
    else:
        window[char] = 1

    if char in need and window[char] == need[char]:
        formed += 1

    while formed == required:

        if right - left + 1 < min_length:
            min_length = right - left + 1
            min_left = left

        left_char = s[left]

        window[left_char] -= 1

        if left_char in need and window[left_char] < need[left_char]:
            formed -= 1

        left += 1

    right += 1

if min_length == float('inf'):
    answer = ''
else:
    answer = s[min_left:min_left + min_length]

print("Minimum window:", answer)