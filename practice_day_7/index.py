def str_str(haystack, needle):

    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):

        found = True

        for j in range(len(needle)):

            if haystack[i + j] != needle[j]:
                found = False
                break

        if found:
            return i

    return -1


haystack = "datascience"
needle = "science"

print("First occurrence index:", str_str(haystack, needle))