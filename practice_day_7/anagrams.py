def group_anagrams(strs):

    groups = {}

    for word in strs:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(strs))