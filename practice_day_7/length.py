def length_of_last_word(s):

    words = s.strip().split()

    if len(words) == 0:
        return 0

    last_word = words[-1]

    return len(last_word)


s = " Embedded Python "

print("Length of last word:", length_of_last_word(s))