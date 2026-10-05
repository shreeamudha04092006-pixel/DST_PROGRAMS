words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

result = list(groups.values())

print(result)